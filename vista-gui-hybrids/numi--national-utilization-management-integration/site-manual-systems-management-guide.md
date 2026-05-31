---
title: NUMI Systems Management Guide Version 15.15
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: null
app_code: NUMI
app_name: National Utilization Management Integration
section: GUI
app_status: archive
pkg_ns: NUMI
patch_ver: 15.15
patch_id: NUMI*15.15
group_key: NUMI:NUMI:15.15
file_numbers: []
security_keys: []
menu_options: 0
description: NUMI is a web-based application that supports field Utilization Management (UM) staff in performing reviews of clinical care activities. NUMI automates the documentation of clinical features relevant to each patient's condition and the associated clinical services provided as part of Veterans Health
audience: ''
keywords: []
page_count: 0
word_count: 29979
section_count: 35
table_count: 42
figure_count: 0
appendix_count: 9
has_toc: false
is_stub: false
pub_date: October 2024
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/National_Utilization_Management_Integration_Archive/numi_15_15_smg_r.docx
pdf_url: https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/National_Utilization_Management_Integration_Archive/numi_15_15_smg_r.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=285
audit_applied: '2026-05-31'
master_source: NUMI Systems Management Guide Version 15.15
master_pub_date: October 2024
consolidated_from: 5 versions
prior_versions:
- NUMI Systems Management Guide Version 15.10
- NUMI Systems Management Guide Version 15.11
- NUMI Systems Management Guide Version 15.9
- NUMI Systems Management Guide
consolidated_title: numi systems management guide
---

SystemsManagementGuide

> Version1.1.15.15

![](numi-systems-management-guide-version-15-15/001.png)

*Department of Veterans Affairs*

October 2024

Revision History

<table>
<caption><p><span id="Table_1:_SMG_Document_Sections" class="anchor"></span>Table : System Management Guide Document Sections</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 59%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>Date of Revision</th>
<th>Description of Change</th>
<th>Author Information</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/7/2024</td>
<td>Updated link to Enhanced Reports in <a href="#8.2_General_Information">General Information</a> section</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>7/07/2024</td>
<td>Added SQL Database Entity Relationship diagram</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>05/16/2024</td>
<td>Updated version to 15.15</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>01/24/2024</td>
<td>Updated version to 15.14</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/1/2023</td>
<td>Updated version to 15.13</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>1/9/2023</td>
<td>Updated version to 15.11</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/15/2021</td>
<td>Updated version to 15.10</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>8/19/2021</td>
<td>Updated System Achitecture Overview diagram (Figure 1)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>12/3/2020</td>
<td>Updated version to 15.9.1 in title and footer. Footer month and year have been updated.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>12/27/2019</td>
<td>Updated version to 15.9 and added system architect figure</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>8/24/2019</td>
<td>Updated version number (15.8)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>6/27/2019</td>
<td>Added 11.4.3: After Hours Management for SA audience</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>9/17/2018</td>
<td>Updated version number (15.6)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>04/24/2018</td>
<td>Update version number( 15.5) and Login Information</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>01/10/2018</td>
<td>Updated document to include NUMI configuration change</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>11/27/2017</td>
<td>Updated document as per HPS feedback.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>11/14/2017</td>
<td>Updated version number and Contract information (version 15.4)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/25/2017</td>
<td>Document updated and reviewed</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>04/12/2017</td>
<td>Added Hospitalization Admission review Type values</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>04/05/2017</td>
<td>Updates due to HPS review</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>03/01/2017</td>
<td>Updates for IAM SSO integration (version 15.2)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>10/01/2016</td>
<td>Updates for MDWS–VIA Migration (version 15.0)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>9/30/2016</td>
<td><blockquote>
<p>Changed Remedy to CA/SDM and updated other support groups to reflect current support system for NUMI application in CA/SDM.</p>
</blockquote></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>9/19/2016</td>
<td><blockquote>
<p>Updated document with feedback received from HPS team review</p>
</blockquote></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>9/13/2016</td>
<td><blockquote>
<p>Changed the version number from 1.1.14.3 to 1.1.14.4. Updated reporting link changes to Enhanced Reports in NUMI 14.4 release.</p>
</blockquote></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>07/14/2015</td>
<td>Changed the version number from 1.1.14.2 to 1.1.14.3</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>04/16/2015</td>
<td>Changed the version number from 1.1.14.1 to 1.1.14.2</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>08/01/2013</td>
<td><p>NUMI version numbers and document dates updated. References to Fee Based items removed from sections 3.5 and 7.2.1. SSRS and replicated database servers added to section 3.1 and CPU and memory requirements added to all servers listed in section 3.1. Our interpretation of "security relevant events" added to section 8.3.2.</p>
<p>Brief description of the InfoLog table added to section 11, Troubleshooting.</p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>07/01/2013</td>
<td>Initial baseline – per project closeout</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>3/15/019</td>
<td>Updated version number (15.7)</td>
<td><mark>Redacted</mark></td>
</tr>
</tbody>
</table>

<span id="Table_1:_SMG_Document_Sections" class="anchor"></span>Table : System Management Guide Document Sections

Table of Contents

Table of Tables

Table of Figures

# Orientation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Orientation](#orientation)
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Target Audience](#target-audience)
  - [Document Overview](#document-overview)
- [System Requirements](#system-requirements)
  - [Physical Architecture](#physical-architecture)
  - [System Architecture](#system-architecture)
    - [Application Server Components](#application-server-components)
    - [Load Balancer](#load-balancer)
  - [NUMI Web Application](#numi-web-application)
  - [Controller Layer](#controller-layer)
    - [Stay Synchronizer](#stay-synchronizer)
    - [Data Access Layer (DAL)](#data-access-layer-dal)
    - [NUMI Exchange](#numi-exchange)
    - [VistA Integration Adapter (VIA)](#vista-integration-adapter-via)
    - [Care Enhance Review Management Enterprise (CERMe)](#care-enhance-review-management-enterprise-cerme)
  - [NUMI UserInterface (UI) Components](#numi-userinterface-ui-components)
- [Parameters](#parameters)
  - [Timeout Parameter](#timeout-parameter)
  - [Lockout Parameters](#lockout-parameters)
  - [Date Format Parameters](#date-format-parameters)
    - [Date Value Parameters](#date-value-parameters)
    - [Day Being Reviewed Date Parameters](#day-being-reviewed-date-parameters)
    - [Start Date and End Date Parameters](#start-date-and-end-date-parameters)
  - [Text Entry Field Parameters](#text-entry-field-parameters)
- [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
- [Database Information](#database-information)
  - [Relational Tables](#relational-tables)
    - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Schema](#schema)
  - [Database Users](#database-users)
  - [Database Tables](#database-tables)
    - [Table: AdminLogging](#table-adminlogging)
    - [Table: AdmissionReviewType](#table-admissionreviewtype)
    - [Table: AdmissionSource](#table-admissionsource)
    - [Table: CareLevel](#table-carelevel)
    - [Table: CareType](#table-caretype)
    - [Table: CERMeReviewXML](#table-cermereviewxml)
    - [Table: CriteriaMetDetailedOutcome](#table-criteriametdetailedoutcome)
    - [Table: DismissStayReason](#table-dismissstayreason)
    - [Table: ExchangeAuthentication](#table-exchangeauthentication)
    - [Table: ExchangeAuthenticationPermissions](#table-exchangeauthenticationpermissions)
    - [Table: ExchangeAuthenticationRoles](#table-exchangeauthenticationroles)
    - [Table: ExchangeLog](#table-exchangelog)
    - [Table: FacilityTreatingSpecialty](#table-facilitytreatingspecialty)
    - [Table: ExchangeState](#table-exchangestate)
    - [Table: MASMovementTransactionType](#table-masmovementtransactiontype)
    - [Table: InfoLog](#table-infolog)
    - [Table: MASMovementType](#table-masmovementtype)
    - [Table: NumiConfig](#table-numiconfig)
    - [Table: NumiUser](#table-numiuser)
    - [Table: NumiUserSiteActivityBitmask](#table-numiusersiteactivitybitmask)
    - [Table: Patient](#table-patient)
    - [Table: PatientAudit](#table-patientaudit)
    - [Table: PatientReview](#table-patientreview)
    - [Table: PatientReviewAudit](#table-patientreviewaudit)
    - [Table: PatientReviewReason](#table-patientreviewreason)
    - [Table: PatientStay](#table-patientstay)
    - [Table: PatientStayAudit](#table-patientstayaudit)
    - [Table: Physician](#table-physician)
    - [Table: PhysicianAdvisorPatientReason](#table-physicianadvisorpatientreason)
    - [Table: PhysicianAdvisorPatientReview](#table-physicianadvisorpatientreview)
    - [Table: PhysicianAdvisorPatientReviewAudit](#table-physicianadvisorpatientreviewaudit)
    - [Table: Reason](#table-reason)
    - [Table: ReasonCategory](#table-reasoncategory)
    - [Table: Region](#table-region)
    - [Table: Reports](#table-reports)
    - [Table: ReviewType](#table-reviewtype)
    - [Table: ServiceSection](#table-servicesection)
    - [Table: Site](#table-site)
    - [Table: Status](#table-status)
    - [Table: TreatingSpecialtyDismissalType](#table-treatingspecialtydismissaltype)
    - [Table: VISN](#table-visn)
    - [Table: WardLocation](#table-wardlocation)
    - [Table: WebLog](#table-weblog)
  - [SQL Jobs](#sql-jobs)
    - [Table: SQLJobs](#table-sqljobs)
  - [Report Database](#report-database)
    - [Report Database Configuration](#report-database-configuration)
- [Exported Groups and/or Options and Menus](#exported-groups-andor-options-and-menus)
  - [Exported Groups and/or Options](#exported-groups-andor-options)
  - [Menus](#menus)
    - [Admin Menu](#admin-menu)
    - [Tools Menu](#tools-menu)
    - [Help Menu](#help-menu)
- [Security Keys and/or Roles](#security-keys-andor-roles)
  - [VistA Rights needed for NUMI users](#vista-rights-needed-for-numi-users)
  - [General Information](#general-information)
    - [Audit and Accountability Policy and Procedures](#audit-and-accountability-policy-and-procedures)
    - [Auditable Events](#auditable-events)
    - [Content of Audit Records](#content-of-audit-records)
    - [Audit Storage Capacity](#audit-storage-capacity)
    - [Response to Audit Processing Failures](#response-to-audit-processing-failures)
    - [Audit Monitoring, Analysis and Reporting](#audit-monitoring-analysis-and-reporting)
    - [Audit Reduction and Report Generation](#audit-reduction-and-report-generation)
    - [Time Stamps](#time-stamps)
    - [Protection of Audit Information](#protection-of-audit-information)
    - [Audit Record Retention](#audit-record-retention)
  - [Security - Authentication and Authorization](#security-authentication-and-authorization)
    - [Identification and Authentication Policy and Procedures](#identification-and-authentication-policy-and-procedures)
    - [User Identification and Authentication](#user-identification-and-authentication)
    - [Device Identification and Authentication](#device-identification-and-authentication)
    - [Identifier Management](#identifier-management)
    - [Authenticator Management](#authenticator-management)
    - [Authenticator Feedback](#authenticator-feedback)
    - [Cryptographic Module Authentication](#cryptographic-module-authentication)
  - [Security – Access Control](#security-access-control)
    - [Physical and Environmental Protection Policy & Procedure](#physical-and-environmental-protection-policy-procedure)
    - [Physical Access Authorizations](#physical-access-authorizations)
    - [Physical Access Control](#physical-access-control)
    - [Access Control for Transmission Medium](#access-control-for-transmission-medium)
    - [Access Control for Display Medium](#access-control-for-display-medium)
    - [Monitoring Physical Access](#monitoring-physical-access)
    - [Visitor Control](#visitor-control)
    - [Access Records](#access-records)
  - [Mail Groups, Alerts and Bulletins](#mail-groups-alerts-and-bulletins)
  - [Security - Contingency Planning](#security-contingency-planning)
    - [Contingency Planning Policy and Procedures](#contingency-planning-policy-and-procedures)
    - [Contingency Plan](#contingency-plan)
    - [Contingency Training](#contingency-training)
    - [Contingency Plan Testing and Exercises](#contingency-plan-testing-and-exercises)
    - [Contingency Plan Update](#contingency-plan-update)
    - [Alternate Storage Site](#alternate-storage-site)
    - [Alternate Processing Site](#alternate-processing-site)
    - [Telecommunications Services](#telecommunications-services)
    - [Information System Backup](#information-system-backup)
    - [Information System Recovery and Reconstitution](#information-system-recovery-and-reconstitution)
  - [File Security](#file-security)
- [Java Components (Client-Sided Java Components)](#java-components-client-sided-java-components)
- [Set-up and Configuration](#set-up-and-configuration)
  - [Deployment Package](#deployment-package)
- [Troubleshooting](#troubleshooting)
  - [High Level NUMI Exceptions](#high-level-numi-exceptions)
  - [Error Components and their Meaning](#error-components-and-their-meaning)
  - [Common Executable Errors](#common-executable-errors)
  - [General Troubleshooting](#general-troubleshooting)
    - [CERMe](#cerme)
    - [Tier 2 and Tier 3 Support](#tier-2-and-tier-3-support)
    - [After Hours Management](#after-hours-management)
  - [Interface Control Document (ICD) References for Messaging Specifications](#interface-control-document-icd-references-for-messaging-specifications)
- [Appendix A– Acronyms and Terms](#appendix-a-acronyms-and-terms)
- [Appendix B - Dependencies](#appendix-b-dependencies)
- [Appendix C – Interfacing](#appendix-c-interfacing)
- [Appendix D – References and Official Policies](#appendix-d-references-and-official-policies)
- [Appendix E – Section 508 Compliance](#appendix-e-section-508-compliance)
- [Appendix F – NUMI Development Tools](#appendix-f-numi-development-tools)
- [Appendix G– NUMI Workflow Example](#appendix-g-numi-workflow-example)
- [Appendix H – Free Text Search Criteria](#appendix-h-free-text-search-criteria)
- [Appendix I– NUMI Database Servers](#appendix-i-numi-database-servers)
Not applicable. There are no software or audience-specific notations or directions (e.g., symbols used to indicate terminal dialogues or user responses) for National Utilization Management Integration (NUMI).

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI is a web-based application that supports field Utilization Management (UM) staff in performing reviews of clinical care activities. NUMI automates the documentation of clinical features relevant to each patient's condition and the associated clinical services provided as part of Veterans Health Administration's (VHA's) medical benefits package.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI Systems Management Guide gives a technical description of NUMI for supporting and maintaining the application.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide provides technical personnel with information on the interactions between the components that are part of the NUMI architecture, to enable them to support and maintain the system.

## Target Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended target audience of this guide includes Developers, Systems Administrators, Information Resource Management (IRM), and Product Support.

## Document Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 1 lists the chapters in this guide.

| Chapter | Chapter Name                         | Chapter Includes                                                                                          |
|-------------|------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| 1           | Orientation                              | Not Applicable                                                                                                |
| 2           | Introduction                             | Purpose, Scope, Target Audience, and Document Overview                                                        |
| 3           | System Requirements                      | Overview of the NUMI system                                                                                   |
| 4           | Parameters                               | Description of NUMI system parameters                                                                         |
| 5           | Remote Procedure Calls (RPC)             | RPCs being utilized for NUMI                                                                                  |
| 6           | Database Information                     | Database tables                                                                                               |
| 7           | Exported Groups and/or Options and Menus | NUMI menu descriptions;(Exported Groups and/or Options are Not Applicable)                                    |
| 8           | Security Keys and/or Roles               | Security keys, roles and other related information                                                            |
| 9           | Java Components                          | Not Applicable                                                                                                |
| 10          | Setup and Configuration                  | Setup and configuration information                                                                           |
| 11          | Troubleshooting                          | Troubleshooting information for NUMI exceptions                                                               |
| Appendix A  | Acronyms and Terms                       | A list of acronyms and terms used in this guide and their descriptors                                         |
| Appendix B  | Dependencies                             | Information about NUMI dependencies                                                                           |
| Appendix C  | Interfacing                              | Information about NUMI interfaces                                                                             |
| Appendix D  | References and Official Policies         | References and policies relevant to the NUMI project                                                          |
| Appendix E  | Section 508 Compliance                   | Information about Section 508 compliance guidelines                                                           |
| Appendix F  | NUMI Development Tools                   | A description of the tools used to develop NUMI                                                               |
| Appendix G  | NUMI Workflow Example                    | An example of the NUMI application workflow from a UM user's perspective                                      |
| Appendix H  | Free Text Search Criteria                | A listing of tables/columns checked during Free Text searches from UM Review Listing and Search Patient pages |
| Appendix I  | NUMI Database Servers                    | Database Server names                                                                                         |

<span id="Table_2:_NUMIService_Operations" class="anchor"></span>Table 2: NUMIService Operations

# System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI will be utilized at all Veterans Integrated Services Networks (VISNs), to provide a standard way of capturing and evaluating patient conditions at all the VA medical facilities. NUMI provides a centralized Web application and database for all VISNs and Veterans Administration Medical Centers. The NUMI application is dependent on the functional operation of the Veterans Information Systems and Technology Architecture (VistA) Integration Adapter (VIA), Internet Information Server (IIS) application servers, VistA, and the Care Enhance Review Management Enterprise (CERMe) commercial off the shelf (COTS) product, the Stay Synchronizer and the Structured Query Language (SQL) Server Database.

## Physical Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a traditional three-tiered approach to software development, the middle tier, or business object layer is the layer of architecture that models and enforces the business rules and/or data of an organization. NUMI interacts with VistA through the VIA services (See Section 3.4.4). The interaction with the CERMe COTS product is through Extensible Markup Language (XML) and JavaScript.

The NUMI target configuration is a three machine cluster, consisting of the NUMI/CERMe Web Server, NUMI Exchange Web Server and NUMI Database Server. The NUMI/CERMe Web server runs the web applications for NUMI and CERMe, while the NUMI Exchange Web server runs the NUMI Exchange web service.

The NUMI and the CERMe databases reside on the NUMI Database server. The NUMI database stores information on patient movements. The CERMe database stores the Change Healthcare InterQual® criteria, which is used by the UM reviewers to determine patients' level of care and to manage Stay information. The minimum server and workstation software dependencies required to support the NUMI architecture are:

<u>NUMI/CERMe Web Server (Application Server)</u>: 16GB RAM, 2.4GHz Xeon, Windows 2019 Server; Internet Information Services (IIS) v8.0; Microsoft (MS).NET 4.6.2 Framework; CERMe application; and NUMI Application.

<u>NUMI Exchange Web Server</u>: 4GB RAM, 2.4GHz Xeon, Windows 2019 Server; Internet Information Services (IIS) v8.0; MS.NET 4.6.2 Framework; and Web Services Enhancements 3.0.

<u>NUMI Database Server</u>: 64GB RAM, 2.8GHz Xeon, Windows 2019 Server; MS SQL Server 2019; Stay Synchronizer; NUMI Database; and CERMe Database.

<u>NUMI</u> SQL Server Reports Server <u>(SSRS)</u>: 8GB RAM, 2.8GHz Xeon, Windows 2019 Server; MS SQL Server 2019; MS SQL Server Reporting Services 2019.<u>NUMI Replicated Database Server</u>: 16GB RAM, 2.8GHz Xeon, Windows 2008 Server; MS SQL Server 2019; NUMI Database.

<u>NUMI</u> <u>Workstation</u>: Minimum specifications: 2GB RAM, 2GHz Pentium 4; Operating System (O/S): Microsoft Windows 10 Enterprise (standard VA configuration for desktops); Microsoft Edge in IE Mode; JavaScript; and Adobe Acrobat Reader.

## System Architecture

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All servers have dual quad-core processors, large RAID arrays, and are running on a Windows 2019 server. The 64-bit servers are set up with a 146GB RAID -one array and a 410GB RAID - 5 (with one 'hot spare' in each server). The database servers additionally have dual Host Bus Adapter cards in them to make the required Storage Area Network (SAN) connections.

<u>Primary Site</u>: Two web servers, connected to a hardware load balancer; two web-services servers; and a database server connected to the SAN.

Below is an image that replicates the system architecture in the production environment.

![](numi-systems-management-guide-version-15-15/002.png)

<span id="_Toc169781995" class="anchor"></span>Figure 1: System Architecture Overview

### Application Server Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI was built on the MS.NET 4.7.2 framework. The application server runs on an Internet Information Services (IIS) Application Server v8.0. The application requires MS ASP .NET 2.0 Ajax Extensions 1.0 and Web Services Enhancements 3.0 to enable the interactions with the Web Services. NUMI utilizes the VIA service to access patient information from VistA.

The NUMI application server is installed on 2 web servers, configured for fail over. This ensures that requests are being submitted to the application server. A load balancer directs the requests to the server with the least load, giving the user an improved response time.

### Load Balancer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The load balancer at the primary production site will be configured to distribute requests evenly between the two web application servers.

## NUMI Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI web application consists of services that interact with the Controller layer and, subsequently, VIA services to retrieve patient information from VistA. The NUMI web application makes JavaScript calls to the CERMe application to retrieve Change Healthcare InterQual® information. Together, this information enables the users to determine what is needed to provide the appropriate level of care to the patients. The NUMI web application interacts with the NUMI.

GUI (graphical user interface) components and the NUMI front end, which is viewed by the UM users.

## Controller Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Controller layer manages the interactions between the NUMI web application, the VIA services and the NUMI database. Components of the controller include the Business Logic Layer, Business Object Layer, and the Data Access Layer (DAL). To facilitate interactions with the NUMI web application, calls are made to the VIA NUMIService (see [<u>Table 2</u>](#Table_2:_NUMIService_Operations) for the list of NUMIService operations), and managed by the Controller layer.

### Stay Synchronizer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stay Synchronizer is a Windows service which retrieves admission, transfer and discharge data from the VistA systems across the VA. Reminders will be updated by the Synchronizer when it detects that a stay has changed. This includes stays that have been dismissed or that have had continuing stay reminders set by the reviewer.

The Synchronizer consists of an hourly and daily import of admission, transfer, and discharge records from VistA. The daily synchronization occurs at midnight local time for each VistA system. The Synchronizer can also be configured to retry missed daily synchronizations. For example, if the Synchronizer stops working on the first of the month and is restarted on the second, it will attempt to synchronize the admission, transfer, and discharge records it missed on the first.

Data flows from VistA to NUMI. NUMI does not send anything back to VistA. If information changes in VistA, the corresponding information in NUMI will be overwritten in the next Synchronizer feed. However, if a patient stay is deleted in VistA it is not automatically deleted in NUMI. To address that situation, NUMI Administrators will be able to manually inactivate the stay in NUMI.

### Data Access Layer (DAL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI DAL is a component of the Controller layer. It facilitates access to the NUMI database, the data source used to store the patient review data, using a data access object solution strategy. This data is consolidated from the data retrieved from VistA and the criteria retrieved from CERMe, establishing a patient review history for use by the NUMI application.

### NUMI Exchange

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI Exchange web service will provide interoperability to different VA applications and systems by exposing NUMI data from the NUMI database. Only applications with valid authentication and privileges will be allowed to execute the published web service methods; all requests are logged. Future implementations and enhancements will allow for creation and updating of database records. NUMI Exchange should be secured with a valid Secure Socket Layer certificate.

NUMI Exchange is implemented through a web method named GetLevelOfCareBySite at Inpatient.asmx. It has the following input parameters:

AuthenticationID (guid/uniqueidentifier) SiteCodeList (string/varchar (2000))

The SiteCodeList can be a SiteCode from a single site (which will result in returned data from one site), a comma-separated list of several SiteCodes (which will return data from multiple sites), or an empty string. An empty string parameter will return data from all sites. GetLevelOfCareBySite has the following parameters:

Message (string) - Used to display error messages Array of...

SITE_CODE (string/varchar (10)) PATIENT_SSN (string/varchar (15)) LEVEL_OF_CARE (byte/bit)

ASSIGNMENT_DATE (DateTime/smalldatetime)

### VistA Integration Adapter (VIA)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VIA is a suite of web services that exposes medical domain data and functionality by accessing legacy systems where data resides. VIA exposes this healthcare data by means of web services constructed with modular and extensible architecture. The VIA system is standards-based and designed to support existing data and performance requirements while anticipating growth in the exposure of new data domains through web service interfaces. This provides a single enterprise application executing in a particular site, which can be scaled to support the anticipated growth of usage by the user community and the current demands for healthcare data.

The VIA product modularizes the services exposed to external applications and encapsulates the internal service execution logic to enable rapid change through the use of dependency injection and other techniques for developing loosely coupled, maintainable architectures. Dependency injection is a software engineering pattern that helps alleviate the need for hardcoding components, such as RPC identifiers and specific service modules.

VIA web services provide synchronous access to data retrieved from multiple data sources, primarily VistA. A single service call may invoke other services in a federated fashion. This is done by executing the calls to data access services in separate threads maintained by a managed thread pool. At the completion of the data retrieval requests, the data is aggregated and combined to provide the response to the client system that initiated the service request.

Table 2 contains the list of VIA NUMIService operations used by the NUMI web application. NUMI communicates to VIA and VIA communicates to VistA.

The NUMI web application is configured to receive a maximum of 10,000 records per VIA service call. This value is configured in the NumiServiceImplService WSDL implementation by changing the MaxOccurs as shown in the example below:

\<xs:sequence\>

\<xs:element minOccurs="0" maxOccurs="10000" form="unqualified" name="taggedText" type="tns:taggedText" /\>

\</xs:sequence\>

<table>
<caption><p><span id="Table_3:_NUMI_UI_Components" class="anchor"></span>Table 3: NUMI UI Components</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Method</strong></th>
<th><strong>Summary</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>inpatientStayTO</td>
<td><strong>getStayMovements</strong> (QueryBean queryBean)<br />
Get patient movement records associated with a checkin ID.</td>
</tr>
<tr class="even">
<td>taggedInpatientStayArrays</td>
<td><strong>getStayMovementsByDateRange</strong> (QueryBean queryBean)<br />
Gets patient movement records falling within given start and end dateTime.</td>
</tr>
<tr class="odd">
<td>taggedInpatientStayArrays</td>
<td><strong>getStayMovementsByPatient</strong> (QueryBean queryBean)<br />
Gets all selected patient movement records.</td>
</tr>
<tr class="even">
<td>regionArray</td>
<td><strong>getVHA</strong> (QueryBean queryBean)<br />
Get all VHA sites.</td>
</tr>
<tr class="odd">
<td>taggedTextArray</td>
<td><strong>issueConfidentialityBulletin</strong> (QueryBean queryBean)<br />
Get patient confidentiality from all connected sites.</td>
</tr>
<tr class="even">
<td>userTO</td>
<td><strong>loginVIA</strong> (String siteCode, String accessCode, String verifyCode, QueryBean queryBean)<br />
Authenticates a user against VistA.</td>
</tr>
<tr class="odd">
<td>taggedPatientArray</td>
<td><strong>Match</strong> (QueryBean queryBean)<br />
Match patients at logged-in site using the target received.</td>
</tr>
<tr class="even">
<td>patientTO</td>
<td><strong>Select</strong> (QueryBean queryBean)<br />
Select a patient at logged-in site.</td>
</tr>
<tr class="odd">
<td>taggedUserArrays</td>
<td><strong>userLookup</strong> (QueryBean queryBean)<br />
Finds a user by partial name.</td>
</tr>
<tr class="even">
<td>userTO</td>
<td><p><strong>batch Login (</strong>QueryBean queryBean<strong>)</strong></p>
<p>Authenticates the NUMI application against VIA. Used by synchronizer</p></td>
</tr>
</tbody>
</table>

<span id="Table_3:_NUMI_UI_Components" class="anchor"></span>Table 3: NUMI UI Components

### Care Enhance Review Management Enterprise (CERMe)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CERMe is a COTS web application developed by the Change Healthcare Corporation. During the documentation of the clinical features relevant to the patient's condition, CERMe is used by the Utilization Management staff to review the patient information against the InterQual® criteria, thus establishing the appropriate level of care. The CERMe web application is deployed to the same server as NUMI, though the web application runs in a separate web container. The CERMe database is on the same database server as the NUMI database.

## NUMI UserInterface (UI) Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI UI is developed as Active Server Pages (ASP).net pages. Known officially as "web forms"(files with the extension ASPX); the ASP.net pages are the main building block for application development. These Web forms contain static (X) HTML markup, as well as markup defining server-side Web Controls and User Controls where the developers place all the required static and dynamic content for the web page. The NUMI web forms interact with the VIA service through the Controller layer. Table 3 describes the major web forms developed for the NUMI application.

<table>
<caption><p><span id="Table_4:_Authorized_NUMI_Database_Users" class="anchor"></span>Table 4: Authorized NUMI Database Users</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AdminQuery.aspx</td>
<td>NUMI administrators can query the NUMI database through the interface on this page.</td>
</tr>
<tr class="even">
<td>AdminSites.aspx</td>
<td>Site Admin page. This page allows authorized users to add VistA users to Primary Reviewer, Physician Reviewer, Site Administrator, Report Only panels, and remove them from the panels.</td>
</tr>
<tr class="odd">
<td>Authenticated/Default.aspx</td>
<td>Select NUMI configuration values can be updated by NUMI administrators on this page.</td>
</tr>
<tr class="even">
<td>CERME.aspx</td>
<td>CERMe page. This is the NUMI page that facilitates access to Change Healthcare's CERMe InterQual® criteria.</td>
</tr>
<tr class="odd">
<td>DeceasedWarning.aspx</td>
<td>NUMI splash screen. This page displays a warning prior to displaying a deceased patient's record.</td>
</tr>
<tr class="even">
<td>DismissalAdmin.aspx</td>
<td>Site administrators can configure treating specialties as Reviewable or Not Reviewable.</td>
</tr>
<tr class="odd">
<td>History.aspx</td>
<td>NUMI History Page. This page allows an authorized user to view the patient stay history. The user can review current or previous stays by selecting items from Movement and Review tables.</td>
</tr>
<tr class="even">
<td>Home.aspx/Default.aspx</td>
<td>Select VISN, then Site (NUMI home. This page enables an authorized user to login to NUMI.</td>
</tr>
<tr class="odd">
<td>Login.aspx</td>
<td>This is an intermediate page that handles authentication headers passed in by the Identity and Access Management (IAM) Single Sign On (SSO) login page. This page immediately redirects to Default.aspx after the headers are read and a forms authentication ticket has been created.</td>
</tr>
<tr class="even">
<td>Logout.aspx</td>
<td>NUMI Logout page. his page is accessed from the Tools menu and is where users will logout of NUMI.</td>
</tr>
<tr class="odd">
<td>NumiUserEdit.aspx</td>
<td>NUMI New User/Privileges page. This page includes functionality for editing user privileges and is accessed from the Admin menu. The page allows authorized users to add and edit NUMI users, and deactivate user site access.</td>
</tr>
<tr class="even">
<td>NumiUserList.aspx</td>
<td>NUMI User List page. This page is accessed from the Admin menu and allows authorized users to retrieve a list of NUMI users by VistA, or by site.</td>
</tr>
<tr class="odd">
<td>PAReview.aspx</td>
<td>NUMI Physician Reviewer Review page. This page allows a Physician Reviewer to perform a patient review.</td>
</tr>
<tr class="even">
<td>PatientDetails.aspx</td>
<td>Report #7 - Patient Details Report. This report is accessed from the Reports menu and allows users to see all reviews saved for a specific patient for a selected time period.</td>
</tr>
<tr class="odd">
<td>PatientLevelMetNotMet.aspx</td>
<td>Report #5 - Patient Level Met/Not Met Report. This report is accessed from the Reports menu and allows users to see a basic patient level report.</td>
</tr>
<tr class="even">
<td>PatientLevelMetNotMetCustom.aspx</td>
<td>Report #6 – Patient Level Met/Not Met Custom Report. This report shows the same information that Report #5 does, except it includes information that was typed into the Custom field on the Primary Review screen.</td>
</tr>
<tr class="odd">
<td>PatientSelection.aspx</td>
<td>NUMI Patient Selection/Worklist Page. This page is accessed from the Tools menu and allows an authorized user to select a patient based on patient selection methods, and other criteria.</td>
</tr>
<tr class="even">
<td>PatientSelectionDismissed.aspx</td>
<td>NUMI Dismissed Patient Stays page This page is accessed from the Tools menu and allows users to see the list of patient stays dismissed from an earlier review.</td>
</tr>
<tr class="odd">
<td>PatientSelectionSearch.aspx</td>
<td>Free Text Patient Search page. This page is accessed from the Tools menu and allows users to search for patients using various filters and text entry options.</td>
</tr>
<tr class="even">
<td>PatientStayAdmin.aspx</td>
<td>Patient Stay Administration page. This page is accessed from the Tools menu and allows users to search for stays that are on NUMI but have been removed from VistA.</td>
</tr>
<tr class="odd">
<td>PatientWorksheet.aspx</td>
<td>Patient Worksheet page. This page displays after a button is selected on the History page. Users can print a hardcopy out and take it with them on rounds.</td>
</tr>
<tr class="even">
<td>PhysicianAdvisor.aspx</td>
<td><p>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports.</p>
<p>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</p></td>
</tr>
<tr class="odd">
<td>PhysicianUMAdvisorResponse.aspx</td>
<td><p>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports.</p>
<p>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</p></td>
</tr>
<tr class="even">
<td>PortraitReport.aspx</td>
<td>After reports have been generated and a print preview button is selected, the output will display in a PortraitReport.aspx window.</td>
</tr>
<tr class="odd">
<td>PrimaryReview.aspx</td>
<td>NUMI Primary Review page. This page allows users to perform a primary review (and indicate whether a Physician Reviewer review is required if criteria is not met).</td>
</tr>
<tr class="even">
<td>ReasonsCSReviews.aspx</td>
<td>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="odd">
<td>ReasonsforAdmReviews.aspx</td>
<td><p>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports.</p>
<p>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</p></td>
</tr>
<tr class="even">
<td>Review.aspx</td>
<td>Review Summary page. This page allows users to look at Primary Review, Physician Reviewer summary information for patients, as well as view only CERMe Review text.</td>
</tr>
<tr class="odd">
<td>ReviewSelection.aspx</td>
<td><p>NUMI Patient Reviews page. This page is accessed from the Tools menu and allows users to work with reviews that have been saved for later review or locked to the database.</p>
<p>Authorized users can unlock primary review and physician reviewer reviews and delete reviews from this page.</p></td>
</tr>
<tr class="even">
<td>SensitiveWarning.aspx</td>
<td>NUMI splash screen. This page displays a warning prior to displaying a restricted patient's record. This ensures that users are aware prior to retrieving a Sensitive record and that the record is protected by the Privacy Act of 1974.</td>
</tr>
<tr class="odd">
<td>ServerReconnect.aspx</td>
<td>Blank web page used by JavaScript to re-establish connection between the client side and server side; this keeps the user logged in after screen mouse movements, clicks, and key presses.</td>
</tr>
<tr class="even">
<td>ServerRecycled.aspx</td>
<td>This page displays a message to inform the user that their web session has terminated unexpectedly. This is different than a timeout due to idleness.</td>
</tr>
<tr class="odd">
<td>SummaryMetNotMet.aspx</td>
<td><p>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports.</p>
<p>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</p></td>
</tr>
<tr class="even">
<td>SummaryRLOCReason.aspx</td>
<td><p>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports.</p>
<p>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</p></td>
</tr>
<tr class="odd">
<td>SyncOnDemand.aspx</td>
<td>NUMI Sync on Demand page. This page is accessed from the Tools menu and allows an authorized user to synchronize the patient stays with the information in VistA.</td>
</tr>
<tr class="even">
<td>TimeOut.aspx</td>
<td>This page displays a message to the user informing them that they were automatically logged out from the system due to idleness.</td>
</tr>
<tr class="odd">
<td>Unscheduled30DayReadmit.aspx</td>
<td><p>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports.</p>
<p>https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</p></td>
</tr>
<tr class="even">
<td>Welcome.aspx</td>
<td>This page will be used in future versions of NUMI; currently it will simply redirect the user to their home page.</td>
</tr>
</tbody>
</table>

<span id="Table_4:_Authorized_NUMI_Database_Users" class="anchor"></span>Table 4: Authorized NUMI Database Users

# Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides an overview of NUMI application parameters.

## Timeout Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application times out after twenty (20) minutes of inactivity by the user. Users may experience shorter timeouts if their browser timeout is less than 20 minutes. After a timeout, users will need to reinitiate the normal login procedures

## Lockout Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA will initiate a login restriction to NUMI for 20 minutes after a pre-determined number of unsuccessful login attempts. The precise number of permitted attempts varies by VistA, and lockout is according to local VistA policy. An error message will display to the user and, after 20 minutes have elapsed, VistA will automatically clear the login restriction and the user can try to login again. Users may request their local IRM to reset the login attempt count on their VistA profile to avoid the 20 minute delay.

## Date Format Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application uses a consistent date format on the GUI – mm/dd/yyyy. This is the same way it is displayed in VistA.

### Date Value Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Valid values for 'Month' are 1 thru 12
- Valid values for 'Day' are 1 thru 31

### Day Being Reviewed Date Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In the "Day Being Reviewed Date" field on the Primary Review screen, the calendar will only permit users to select a date between the Admission and Discharge dates. If they manually type in a date, it must be within that range. If a date outside that range is provided, a message similar to this will display: "Please select a review date between \<*admit date*\> and \<*discharge date*\>".

### Start Date and End Date Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- When selecting "Start Date" and "End Date" values in NUMI, the End Date must be after the Start Date or the user will get an error message. Start Date and End Date fields in NUMI are located in:
- The "Reminder Date" filter on the Patient Selection/Worklist screen
- The "Date" filter on the Patient Reviews screen
- All Report filter screens

## Text Entry Field Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The system imposes restrictions on how many characters can be entered into certain text entry fields.
- The system imposes a maximum limit of 100 text entry characters in the Custom text entry field on the Primary Review screen
- The system imposes a maximum limit of 4,000 text entry characters in the Comments field on the Physician Advisor Review screen

# Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPCs for NUMI are handled by VIA. VIA interacts directly with VistA. NUMI does not.

# Database Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI database stores information on patient movements. NUMI does not modify, update or delete data on the VistA system. A Data Access Objects (DAO) solution strategy was utilized for the database architecture. The DAO avoids the need to create a shared data source, thus eliminating the need to collate the information dynamically. This gives the application the ability to access data from multiple data sources, encapsulating the data through the application programming interface (API), presenting it in the appropriate form for each database. The NUMI DAO architecture model is depicted in Figure 2 and the VIA DAO architecture model is depicted in Figure 3.

![](numi-systems-management-guide-version-15-15/003.png)

<span id="_Ref475614078" class="anchor"></span>Figure 2: NUMI DAO Architecture Model

![](numi-systems-management-guide-version-15-15/004.png)

<span id="_Ref475614094" class="anchor"></span>Figure 3: VIA DAO Architecture Model

The DAO manages the connection with the data source to obtain and store data. As for the validation being done prior to storing the data in the NUMI database and what happens if the validation fails, schema-level validation as well as valid data checks depend on the operation. In fully automated operations, an event is stored in the database. This can be checked by Tier 3 support. In user-interactive operations, the system will prompt the user for the correct input.

By implementing the access mechanism required to work with the data source, the business component that relies on the DAO is able to use the simpler API exposed by the DAO for its clients. This interface does not change when the underlying data source implementation changes, thus allowing the DAO to adapt to different storage schemes without affecting its clients or business components. This middle tier translates the requests into the relevant SQL and provides the results in an array of objects that the GUI can interpret.

The DAO does not directly access any database. It sends requests in the format accepted by the target database management system, to retrieve or modify data on the target system.

When talking to a SQL database backend, the DAOs use SQL stored procedures to select, update, and delete database information. Information from VistA is retrieved by NUMI, talking to VIA using Web Services.

## Relational Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information about the NUMI tables and how they inter-relate is managed by the Tier 3 Development Team.

### Entity Relationship Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This figure is a complete Entity Relationship Diagram for the NUMI database in SQL Server.

![](numi-systems-management-guide-version-15-15/005.png)

<span id="_Toc169781998" class="anchor"></span>Figure : NUMI Entity Relationship Diagram

## Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable. Schemas are not called in the SQL server like they are in the Oracle database.

## Database Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4 identifies the authorized NUMI database users. The name of the database is NUMI.

<table>
<caption><p><span id="_Toc169781946" class="anchor"></span>Table 5: AdminLogging</p></caption>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NUMI_OWNER</td>
<td><ul>
<li><p>Owns the NUMI database only.</p></li>
<li><p>Can perform all Data Definition Language activities including: altering, creating and deleting tables, indices, views, stored procedures, etc.</p></li>
<li><p>Cannot perform any Administrator activities.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>NUMI_USER</td>
<td><ul>
<li><p>This user only has Data Manipulation Language roles.</p></li>
<li><p>Can insert, update and select tables and call stored procedures and functions.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc169781946" class="anchor"></span>Table 5: AdminLogging

## Database Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The UM patient review data is stored in the NUMI database. The NUMI data model is defined based on the Entity-Relationship Model and is managed by the Tier 3 Development Team. The data model depicts the elements and fields that support the NUMI infrastructure and the database structure must be able to support data coming from multiple data sources. Subsections 6.4.1 thru 6.4.43 describe the database tables for NUMI and list the data elements, associated data types and File Number/Field Number from VistA (where applicable).

> **NOTE:** The "Internal Entry Number" (IEN) is for a VistA file. The acronym IEN appears in some tables.

### Table: AdminLogging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name     | Data Type     | Indexed | Primary Key | Foreign Key |
|------------------|---------------|---------|-------------|-------------|
| AdminLoggingID   | int           | Yes     | Yes         | No          |
| ConnectionString | varchar(50)   | No      | No          | No          |
| DomainUser       | varchar(50)   | No      | No          | No          |
| Query            | nvarchar(max) | No      | No          | No          |
| DateCreated      | datetime      | No      | No          | No          |

<span id="_Toc169781947" class="anchor"></span>Table 6: AdmissionReviewType

### Table: AdmissionReviewType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name            | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------|---------------|---------|-------------|-------------|
| AdmissionReviewTypeID   | tinyint       | Yes     | Yes         | No          |
| AdmissionReviewTypeDesc | nvarchar(50)  | No      | No          | No          |
| DateInactive            | smalldatetime | No      | No          | No          |
| Inactive                | bit           | No      | No          | No          |
| ColumnOrder             | tinyint       | No      | No          | No          |
| AdmissionReviewMask     | bit           | No      | No          | No          |

<span id="_Toc169781948" class="anchor"></span>Table 7: AdmissionSource

### Table: AdmissionSource

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name        | Data Type     | Indexed | Primary Key | Foreign Key |
|---------------------|---------------|---------|-------------|-------------|
| AdmissionSourceID   | int           | Yes     | Yes         | No          |
| AdmissionSourceDesc | nvarchar(50)  | Yes     | No          | No          |
| DateInactive        | smalldatetime | No      | No          | No          |
| ColumnOrder         | int           | No      | No          | No          |

<span id="_Toc169781949" class="anchor"></span>Table 8: CareLevel

### Table: CareLevel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                                   | Data Type     | Indexed | Primary Key | Foreign Key |
|------------------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| CareLevelID                                                                                                                                    | tinyint       | Yes     | Yes         | No          |
| Identification number for a Level of Care                                                                                                      |               |         |             |             |
| CareLevelType                                                                                                                                  | tinyint       | No      | No          | No          |
| Care level that is associated with a patient                                                                                                   |               |         |             |             |
| CreatedByNumiUserID                                                                                                                            | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                                          |               |         |             |             |
| ModifiedByNumiUserID                                                                                                                           | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                                          |               |         |             |             |
| CareLevelDesc                                                                                                                                  | varchar(250)  | Yes     | No          | No          |
| Description of the level of care being given to a patient                                                                                      |               |         |             |             |
| Version                                                                                                                                        | varchar(10)   | No      | No          | No          |
| Version associated with CareLevel                                                                                                              |               |         |             |             |
| DateCreated                                                                                                                                    | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                               |               |         |             |             |
| DateModified                                                                                                                                   | datetime      | No      | No          | No          |
| Date that the record was modified                                                                                                              |               |         |             |             |
| DateInactive                                                                                                                                   | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                           |               |         |             |             |
| Inactive                                                                                                                                       | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive            |               |         |             |             |
| CLOC                                                                                                                                           | bit           | No      | No          | No          |
| Indicator to identify if care level is applicable for Current Level of Care (CLOC) when the value is 1. A value of 0 means it is not CLOC.     |               |         |             |             |
| RLOC                                                                                                                                           | bit           | No      | No          | No          |
| Indicator to identify if care level is applicable for Recommended Level of Care (RLOC) when the value is 1. A value of 0 means it is not RLOC. |               |         |             |             |

<span id="_Toc169781950" class="anchor"></span>Table 9: CareType

### Table: CareType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name | Data Type     | Indexed | Primary Key | Foreign Key |
|--------------|---------------|---------|-------------|-------------|
| CareTypeID   | int           | Yes     | Yes         | No          |
| CareTypeDesc | varchar(50)   | No      | No          | No          |
| DateInactive | smalldatetime | No      | No          | No          |
| Inactive     | bit           | No      | No          | No          |

<span id="_Toc169781951" class="anchor"></span>Table 10: CERMeReviewXML

### Table: CERMeReviewXML

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| CermeReviewXMLID                                                                                                                    | bigint        | Yes     | Yes         | No          |
| PatientReviewID                                                                                                                     | bigint        | Yes     | No          | Yes         |
| CERMEXML                                                                                                                            | varchar(max)  | No      | No          | No          |
| Extended Markup Language required to analyze fields from Change Healthcare CERMe                                                    |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |

<span id="_Toc169781952" class="anchor"></span>Table 11: CriteriaMetDetailedOutcome

### Table: CriteriaMetDetailedOutcome

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| criteriaMetDetailedOutcomeID                                                                                                        | tinyint       | Yes     | Yes         | No          |
| Identification number for a criteria met detailed outcome                                                                           |               |         |             |             |
| detailedOutcome                                                                                                                     | varchar(50)   | No      | No          | No          |
| Detailed description of a criteria met detailed outcome                                                                             |               |         |             |             |
| criteriaMet                                                                                                                         | bit           | No      | No          | No          |
| Value for critieria met in previous versions of CERMe, used to map new values to old reports                                        |               |         |             |             |
| dateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |

<span id="_Toc169781953" class="anchor"></span>Table 12: DismissStayReason

### Table: DismissStayReason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| ColumnOrder                                                                                                                         | tinyint       | No      | No          | No          |
| Order in which Facility Treating Specialty values are displayed on application screens                                              |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| DismissStayReasonDesc                                                                                                               | varchar(50)   | No      | No          | No          |
| Description of the reason for a patient stay dismissal                                                                              |               |         |             |             |
| DismissStayReasonID                                                                                                                 | tinyint       | Yes     | Yes         | No          |
| Identification number for a Dismissed stay Reason                                                                                   |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |

<span id="_Toc169781954" class="anchor"></span>Table 13: ExchangeAuthentication

### Table: ExchangeAuthentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name     | Data Type        | Indexed | Primary Key | Foreign Key |
|------------------|------------------|---------|-------------|-------------|
| AuthenticationID | uniqueidentifier | Yes     | Yes         | No          |
| TeamName         | varchar(50)      | No      | No          | No          |
| TeamContact      | varchar(50)      | No      | No          | No          |
| ContactEmail     | varchar(50)      | No      | No          | No          |
| ContactPhone     | varchar(10)      | No      | No          | No          |
| DateCreated      | datetime         | No      | No          | No          |
| DateModified     | datetime         | No      | No          | No          |
| DateInactive     | datetime         | No      | No          | No          |
| Inactive         | bit              | No      | No          | No          |

<span id="_Toc169781955" class="anchor"></span>Table 14: ExchangeAuthenticationPermissions

### Table: ExchangeAuthenticationPermissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name     | Data Type        | Indexed | Primary Key | Foreign Key |
|------------------|------------------|---------|-------------|-------------|
| PermissionID     | int              | Yes     | Yes         | No          |
| AuthenticationID | uniqueidentifier | No      | No          | Yes         |
| RoleID           | int              | No      | No          | Yes         |
| CanSelect        | bit              | No      | No          | No          |
| CanCreate        | bit              | No      | No          | No          |
| CanUpdate        | bit              | No      | No          | No          |
| CanDelete        | bit              | No      | No          | No          |
| DateCreated      | datetime         | No      | No          | No          |
| DateModified     | datetime         | No      | No          | No          |
| DateInactive     | datetime         | No      | No          | No          |
| Inactive         | bit              | No      | No          | No          |

<span id="_Toc169781956" class="anchor"></span>Table 15: ExchangeAuthenticationRoles

### Table: ExchangeAuthenticationRoles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name    | Data Type   | Indexed | Primary Key | Foreign Key |
|-----------------|-------------|---------|-------------|-------------|
| RoleID          | int         | Yes     | Yes         | No          |
| RoleDescription | varchar(50) | No      | No          | No          |
| DateInactive    | datetime    | No      | No          | No          |
| Inactive        | bit         | No      | No          | No          |

<span id="_Toc169781957" class="anchor"></span>Table 16: ExchangeLog

### Table: ExchangeLog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name     | Data Type        | Indexed | Primary Key | Foreign Key |
|------------------|------------------|---------|-------------|-------------|
| ExchangeLogID    | int              | Yes     | Yes         | No          |
| AuthenticationID | uniqueidentifier | No      | No          | No          |
| RemoteAddress    | varchar(50)      | No      | No          | No          |
| MethodName       | varchar(50)      | No      | No          | No          |
| MethodParameters | varchar(max)     | No      | No          | No          |
| DateCreated      | datetime         | No      | No          | No          |

<span id="_Toc169781958" class="anchor"></span>Table 17: FacilityTreatingSpecialty

### Table: FacilityTreatingSpecialty

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781959" class="anchor"></span>Table 18: ExchangeState</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 17%" />
<col style="width: 9%" />
<col style="width: 14%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FacilityTreatingSpecialtyDesc</td>
<td>varchar(100)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Description of a Facility Treating Specialty</td>
<td>VistA File / Field 45.7 / .01</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FacilityTreatingSpecialtyID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a Facility Treating Specialty</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FacilityTreatingSpecialtyIEN</td>
<td>varchar(50)</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identifier for a Facility Treating Specialty</td>
<td>VistA File / Field 45.7/.01</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ServiceSectionID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Service Section</td>
<td><p>VistA File / Field</p>
<p>45.7 / 1</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SiteID</td>
<td>smallint</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Site</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SpecialtyID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a Treating Specialty that can be associated with ANY Facility or Ward</td>
<td><p>VistA File / Field</p>
<p>45.7 / 1</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>TreatingSpecialtyDismissalTypeID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Dismissal Type associated with Facility Treating Specialty</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CreatedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateCreated</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was created</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateModified</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was modified</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ModifiedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc169781959" class="anchor"></span>Table 18: ExchangeState

### Table: ExchangeState

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name    | Data Type   | Indexed | Primary Key | Foreign Key |
|-----------------|-------------|---------|-------------|-------------|
| ExchangeStateID | int         | Yes     | Yes         | No          |
| Description     | varchar(50) | No      | No          | No          |
| DateInactive    | datetime    | No      | No          | No          |
| Inactive        | bit         | No      | No          | No          |

<span id="_Toc169781960" class="anchor"></span>Table 19: MASMovementTransactionType

### Table: MASMovementTransactionType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781961" class="anchor"></span>Table 20: InfoLog</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Element Name</strong></th>
<th><strong>Data Type</strong></th>
<th><strong>Indexed</strong></th>
<th><strong>Primary Key</strong></th>
<th><strong>Foreign Key</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementTransactionTypeDesc</td>
<td>varchar(100)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Description of a Medical Administration Service Movement Transaction Type</td>
<td><p>VistA File / Field</p>
<p>405.2 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementTransactionTypeID</td>
<td>tinyint</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a Medical Administration Service Movement Transaction Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementTransactionTypeIEN</td>
<td>varchar(50)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identifier for a Medical Administration Service Movement Transaction Type</td>
<td><p>VistA File / Field 405 / .18</p>
<p>405.2 / IEN</p></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc169781961" class="anchor"></span>Table 20: InfoLog

### Table: InfoLog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                     | Data Type     | Indexed | Primary Key | Foreign Key |
|----------------------------------|---------------|---------|-------------|-------------|
| InfoLogID                        | bigint        | Yes     | Yes         | No          |
| Log Record ID number             |               |         |             |             |
| Info                             | nvarchar(200) | No      | No          | No          |
| Error Message                    |               |         |             |             |
| Error                            | bit           | No      | No          | No          |
| Indicator of error               |               |         |             |             |
| StartTime                        | datetime      | No      | No          | No          |
| Start time that error was logged |               |         |             |             |
| EndTime                          | datetime      | No      | No          | No          |
| End Time that error was logged   |               |         |             |             |
| UserName                         | nvarchar(50)  | No      | No          | No          |
| Identity of Logged on Vista User |               |         |             |             |
| UserID                           | nvarchar(50)  | No      | No          | No          |
| Vista User ID                    |               |         |             |             |
| ProcessId                        | int           | No      | No          | No          |
| Identity of Process              |               |         |             |             |
| ThreadId                         | int           | No      | No          | No          |
| Identity of Thread               |               |         |             |             |
| ProcessName                      | nvarchar(50)  | No      | No          | No          |
| Name of Process                  |               |         |             |             |
| ClassName                        | nvarchar(200) | No      | No          | No          |
| Name of Class                    |               |         |             |             |
| MethodName                       | nvarchar(50)  | No      | No          | No          |
| Name of Method                   |               |         |             |             |
| Date Created                     | datetime      | No      | No          | No          |
| Created Date                     |               |         |             |             |

<span id="_Toc169781962" class="anchor"></span>Table 21: MASMovementType

### Table: MASMovementType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781963" class="anchor"></span>Table 22: NumiConfig</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementName</td>
<td>varchar(100)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Description of a Medical Administration Service Movement</td>
<td><p>VistA File / Field</p>
<p>405.2 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementTypeID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a Medical Administration Service Movement Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementTypeIEN</td>
<td>varchar(50)</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identifier for a Medical Administration Service Movement Type</td>
<td><p>VistA File / Field</p>
<p>405 / .18</p>
<p>405.2 / IEN</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SiteID</td>
<td>smallint</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Site</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc169781963" class="anchor"></span>Table 22: NumiConfig

### Table: NumiConfig

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name     | Data Type | Indexed | Primary Key | Foreign Key |
|----------------------|---------------|-------------|-----------------|-----------------|
| NumiConfigID         | int           | Yes         | Yes             | No              |
| SiteID               | smallint      | No          | No              | No              |
| ConfigSetting        | varchar(100)  | No          | No              | No              |
| ConfigValue          | varchar(max)  | No          | No              | No              |
| CreatedByNumiUserID  | int           | No          | No              | No              |
| ModifiedByNumiUserID | int           | No          | No              | No              |
| DateCreated          | datetime      | No          | No              | No              |
| DateModified         | datetime      | No          | No              | No              |
| DateInactive         | datetime      | No          | No              | No              |
| Inactive             | bit           | No          | No              | No              |

<span id="_Toc169781964" class="anchor"></span>Table 23: NumiUser

### Table: NumiUser

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                                                             | Data Type                    | Indexed | Primary Key | Foreign Key |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------|---------|-------------|-------------|
| CreatedByNumiUserID                                                                                                                                                      | int                          | No      | No          | No          |
| Identification number for a NUMI user                                                                                                                                    |                              |         |             |             |
| DateCreated                                                                                                                                                              | datetime                     | No      | No          | No          |
| Date that the record was created                                                                                                                                         |                              |         |             |             |
| DateInactive                                                                                                                                                             | smalldatetime                | No      | No          | No          |
| Date that the record was inactivated                                                                                                                                     |                              |         |             |             |
| DateModified                                                                                                                                                             | datetime                     | No      | No          | No          |
| Date that the record was modified                                                                                                                                        |                              |         |             |             |
| DUZ                                                                                                                                                                      | bigint                       | Yes     | Yes         | No          |
| Vista identifier for a User                                                                                                                                              | VistA File / Field 200 / IEN |         |             |             |
| Inactive                                                                                                                                                                 | bit                          | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive                                      |                              |         |             |             |
| IsSuperUser                                                                                                                                                              | bit                          | No      | No          | No          |
| Indicator that the User is a SuperUser within the NUMI application; a value of 0 means that the User is NOT a SuperUser, a value of 1 means that the user IS a SuperUser |                              |         |             |             |
| ModifiedByNumiUserID                                                                                                                                                     | int                          | No      | No          | No          |
| Identification number for a NUMI user                                                                                                                                    |                              |         |             |             |
| networkCredential                                                                                                                                                        | varchar(40)                  | No      | No          | No          |
| Windows Active Directory identifier associated with the User                                                                                                             |                              |         |             |             |
| NumiUserID                                                                                                                                                               | int                          | Yes     | No          | No          |
| Identification number for a User                                                                                                                                         |                              |         |             |             |
| SiteID                                                                                                                                                                   | smallint                     | Yes     | Yes         | Yes         |
| Identification number for a Site                                                                                                                                         |                              |         |             |             |
| VISTAName                                                                                                                                                                | varchar(80)                  | No      | No          | No          |
| Name that the VistA system associates with a user                                                                                                                        | VistA File / Field200 / .01  |         |             |             |
| IncludeObservation                                                                                                                                                       | bit                          | No      | No          | No          |

<span id="_Toc169781965" class="anchor"></span>Table 24: NumiUserSiteActivityBitmask

### Table: NumiUserSiteActivityBitmask

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| ActivityBitmask                                                                                                                     | binary(32)    | Yes     | No          | No          |
| CreatedByNumiUserID                                                                                                                 | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| DateCreated                                                                                                                         | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                    |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| DateModified                                                                                                                        | datetime      | No      | No          | No          |
| Date that the record was modified                                                                                                   |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| ModifiedByNumiUserID                                                                                                                | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| NumiUserID                                                                                                                          | int           | Yes     | Yes         | Yes         |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| NumiUserSiteActivityBitmaskID                                                                                                       | bigint        | Yes     | No          | No          |
| Reason                                                                                                                              | varchar(2000) | No      | No          | No          |
| SiteID                                                                                                                              | smallint      | Yes     | Yes         | Yes         |
| Identification number for a Site                                                                                                    |               |         |             |             |

<span id="_Toc169781966" class="anchor"></span>Table 25: Patient

### Table: Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781967" class="anchor"></span>Table 26: PatientAudit</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ConfirmedVistaTestPatient</td>
<td>bit</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DeceasedDate</td>
<td>smalldatetime</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date a patient was deceased</td>
<td><p>VistA File / Field</p>
<p>2 / .351</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DFN</td>
<td>Bigint</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification of a patient Data File Number</td>
<td><p>VistA File / Field</p>
<p>2 / IEN</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ICN</td>
<td>Bigint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td></td>
<td><p>VistA File / Field</p>
<p>2 / 991.01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>Bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MergeToDfn</td>
<td>Bigint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>PatientID</td>
<td>int</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Identification number for a patient</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PatientName</td>
<td>varchar(100)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Name that the NUMI system associates with a patient</td>
<td><p>VistA File / Field</p>
<p>2 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PseudoSSN</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Fake Social Security Number associated with a patient to protect the patient's identity</td>
<td><p>VistA File / Field</p>
<p>2 / .09</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SensitivityLevel</td>
<td>varchar(1)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Indicator that a patient is either Sensitive or non- Sensitive for identity protection. A value of 0 indicates that the patient does not require additional identity protection, a value of 1 indicates that the patient needs additional identity protection</td>
<td><p>VistA File / Field</p>
<p>38.1 / N/A</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Sex</td>
<td>varchar(1)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Sex designation associated with a patient</td>
<td><p>VistA File / Field</p>
<p>2 / .02</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SiteID</td>
<td>smallint</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a Site</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>SSN</td>
<td>varchar(15)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Social Security Number associated with a patient</td>
<td><p>VistA File / Field</p>
<p>2 / .09</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VistaTestPatient</td>
<td>bit</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Indicator that a patient is a fictional "Test patient" copied over from VistA. A value of 0 indicates that the patient is a real patient; a value of 1 indicates that the patient is fictitious. This field is not currently used by the NUMI system</td>
<td><p>VistA File / Field</p>
<p>2 / 2</p></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc169781967" class="anchor"></span>Table 26: PatientAudit

### Table: PatientAudit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                     | Data Type     | Indexed | Primary Key | Foreign Key |
|----------------------------------|---------------|---------|-------------|-------------|
| Comments                         | varchar(2000) | No      | No          | No          |
| Comments                         |               |         |             |             |
| CreatedBy                        | int           | No      | No          | Yes         |
| DateCreated                      | datetime      | No      | No          | No          |
| Date that the record was created |               |         |             |             |
| PatientAuditID                   | int           | Yes     | Yes         | No          |
| PatientID                        | int           | No      | No          | Yes         |

<span id="_Toc169781968" class="anchor"></span>Table 27: PatientReview

### Table: PatientReview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781969" class="anchor"></span>Table 28: PatientReviewAudit</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Comments</td>
<td>varchar(4000)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Comments</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CreatedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CriteriaMet</td>
<td>bit</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that a patient has met InterQual criteria for the current Level of Care. A value of 0 indicates that the patient has NOT met the InterQual criteria, a value of 1 indicates that the patient has met the InterQual criteria</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CurrentCareLevelID</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Level of Care</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>CurrentCareLevelOther</td>
<td>varchar(1000)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Additional description about the current level of care in a patient review</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Custom</td>
<td>varchar(25)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Comments - maximum length 25 characters</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateCreated</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was created</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateModified</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>FacilityTreatingSpecialtyID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Facility Treating Specialty</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>HospitalAdmissionReview</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td><p>Identification number for a Hospitalization Admission review Type. Possible values and their meaning are listed below:</p>
<p>0 No Review</p>
<p>1 Not an Admission Review</p>
<p>2 Hosp Acute Adm - Traditional Criteria</p>
<p>3 Admission Review-Type- Unknown</p>
<p>4 BH Initial Review</p>
<p>5 Transfer to Higher Level of Care</p>
<p>6 Transfer to/from Acute Care and BH</p>
<p>7 Observation converted to Hospital Admission</p>
<p>8 Hosp Acute Adm - Condition-Specific Criteria</p>
<p>9 Conversion to New Condition-Specific Criteria</p>
<p>10 Observation Review</p>
<p>11 Hospital Acute Admission</p>
<p>12 Admission Converted to Observation</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>InitialCompletedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>InsuranceCompanyDesc</td>
<td>varchar(6000)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Name of the patient's Insurance Company</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>IQSubsetID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification of an InterQual subset designation associated with a patient review</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>MASMovementTransactionTypeID</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Medical Administration Service Movement Transaction Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ModifiedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>NoPaReviewRequired</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that a Physician Advisor review, is needed. A value of 0 indicates a Physician Advisor review is NECESSARY, a value of 1 a Physician Advisor review is NOT necessary</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PatientAge</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Age of a patient associated with a review</td>
<td><p>VistA File / Field</p>
<p>2 / .033</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PatientID</td>
<td>int</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a patient</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PatientReviewID</td>
<td>bigint</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a patient review</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PatientStayID</td>
<td>bigint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a patient stay</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ReasonID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Reason Code</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RecommendedCareLevelID</td>
<td>tinyint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Level of Care</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>RecommendedCareLevelOther</td>
<td>varchar(2000)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Additional description about the recommended level of care in a patient review</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ReviewDate</td>
<td>smalldatetime</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date a patient was reviewed</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ReviewLevel</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>ReviewTypeID</td>
<td>tinyint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a patient review Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>ServiceSectionID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a Service Section</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>StatusChangeDate</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Date that the patient's status changed</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>StatusID</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a patient review status</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>StatusNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a NUMI user status</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>TeamID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>UMRAttendingPhysicianID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for an Attending Physician</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>UMRFacilityTreatingSpecialtyID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Facility Treating Specialty</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>UMRServiceSectionID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Service Section</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>UMRWardLocationID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Ward location</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Unscheduled30DayReadmit</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistaAttendingPhysicianID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>VistA identification number for a Physician Advisor</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>WardLocationID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a Ward location</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>criteriaMetOutcomeId</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>NotMetComment</td>
<td>nvarchar(100)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>SubsetDescription</td>
<td>varchar(max)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>VersionCID</td>
<td>varchar(30)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>EpisodeDayOfCare</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>AdmissionSourceID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>UMRAdmissionSourceID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>AdmittingPhysicianID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>UMRAdmittingPhysicianID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc169781969" class="anchor"></span>Table 28: PatientReviewAudit

### Table: PatientReviewAudit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                     | Data Type     | Indexed | Primary Key | Foreign Key |
|----------------------------------|---------------|---------|-------------|-------------|
| Comments                         | varchar(2000) | No      | No          | No          |
| Comments                         |               |         |             |             |
| CreatedBy                        | int           | No      | No          | Yes         |
| DateCreated                      | datetime      | No      | No          | No          |
| Date that the record was created |               |         |             |             |
| PatientReviewAuditID             | bigint        | Yes     | Yes         | No          |
| PatientReviewID                  | bigint        | No      | No          | Yes         |
| StatusID                         | tinyint       | No      | No          | Yes         |

<span id="_Toc169781970" class="anchor"></span>Table 29: PatientReviewReason

### Table: PatientReviewReason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| OtherDesc                                                                                                                           | varchar(500)  | No      | No          | No          |
| Additional description about a patient review reason                                                                                |               |         |             |             |
| PatientReviewID                                                                                                                     | bigint        | Yes     | Yes         | Yes         |
| Identification number for a patient review                                                                                          |               |         |             |             |
| PatientReviewReasonID                                                                                                               | bigint        | Yes     | No          | No          |
| Identification number for a patient review reason                                                                                   |               |         |             |             |
| ReasonID                                                                                                                            | smallint      | Yes     | Yes         | Yes         |
| Identification number for a patient review reason                                                                                   |               |         |             |             |

<span id="_Toc169781971" class="anchor"></span>Table 30: PatientStay

### Table: PatientStay

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781972" class="anchor"></span>Table 31: PatientStayAudit</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AdmissionDiagnosis</td>
<td>varchar(50)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Diagnosis for the patient at time of Admission</td>
<td>VistA File / Field 405 / .1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AdmissionDRGID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for an Admission Diagnosis Related Group</td>
<td><p>VistA File / Field</p>
<p>45 / 9</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AdmissionMASMovementTypeID</td>
<td>Smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Medical Administration Service Admission Movement Type</td>
<td><p>VistA File / Field</p>
<p>405 / .18</p>
<p>405.2 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AdmissionMovementIEN</td>
<td>varchar(50)</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identifier for a patient's Admission Movement</td>
<td><p>VistA File / Field</p>
<p>405 / IEN</p>
<p>405 / .14</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AdmitDate</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the patient was admitted to the hospital</td>
<td><p>VistA File / Field</p>
<p>405 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AdmittingPhysicianID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td><p>VistA File / Field</p>
<p>405 / .19</p>
<p>356.94 / .03</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>AssignedReviewerID</td>
<td>int</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateCreated</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was created</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateModified</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was modified</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DischargeDate</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the patient was discharged from the hospital</td>
<td>VistA File / Field 405 / .01</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DischargeDRGID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for an Discharge Diagnosis Related Group</td>
<td><p>VistA File / Field</p>
<p>45.84 / 6</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DischargeMovementIEN</td>
<td>varchar(50)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identifier for a patient's Discharge Movement</td>
<td><p>VistA File / Field</p>
<p>405 / IEN</p>
<p>405 / .17</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>dismissStayReason</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification of a dismissed stay reason</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DispositionPlaceID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td></td>
<td><p>VistA File / Field</p>
<p>45 / 75</p>
<p>45.6 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DispositionTypeID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td></td>
<td><p>VistA File / Field</p>
<p>45 / 72</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>InvalidStay</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the stay is not a valid stay for Utilization Management purposes. A value of 0 indicates that the stay IS valid for Utilization Management review, a value of 1 indicates that the stay is NOT valid for Utilization Management review</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastAttendingPhysicianID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastFacilityTreatingSpecialtyID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Facility Treating Specialty</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastMASMovementTransactionTypeID</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Medical Administration Service Last Movement Transaction Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastMASMovementTypeID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Medical Administration Service Last Movement Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastMovementDate</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date of last time a patient was moved/transferred prior to discharge</td>
<td><p>VistA File / Field</p>
<p>405 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastMovementIEN</td>
<td>varchar(50)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identifier for a patient's last stay Movement</td>
<td><p>VistA File / Field</p>
<p>405 / IEN</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastServiceSectionID</td>
<td>smallint</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Service Section</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastWardLocationID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Ward location</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LengthofStay</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Duration of a patient's stay in the hospital</td>
<td><p>VistA File / Field</p>
<p>45 / 81</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ModifiedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>NUMIHashCode</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>PatientID</td>
<td>int</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="odd">
<td>Identification number for a patient</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PatientStayID</td>
<td>bigint</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PriorStayDischargeDate</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Date that the patient was discharged on their prior stay</td>
<td><p>VistA File / Field</p>
<p>405 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>PTFIEN</td>
<td>varchar(50)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td></td>
<td><p>VistA File / Field</p>
<p>405 / .16</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Readmission14Day</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Indicator that the patient was readmitted to treatment within 14 days of discharge. A value of 0 indicates that the patient was NOT readmitted within 14 days of discharge, a value of 1 indicates that the patient WAS readmitted within 14 days of discharge</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Readmission24Hr</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="odd">
<td>Readmission30Day</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the patient was readmitted to treatment within 30 days of discharge. A value of 0 indicates that the patient was NOT readmitted within 30 days of discharge, a value of 1 indicates that the patient WAS readmitted within 30 days of discharge</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ReminderDate</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date determining when the patient will be included in results within a range of Reminder Dates. This is primarily used for "worklist" kinds of screens and reports</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ReminderType</td>
<td>tinyint</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a patient stay Reminder Type</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ServiceConnectedAdmission</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td></td>
<td><p>VistA File / Field</p>
<p>405 / .11</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>LastAdmissionSourceID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
</tbody>
</table>

<span id="_Toc169781972" class="anchor"></span>Table 31: PatientStayAudit

### Table: PatientStayAudit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                          | Data Type     | Indexed | Primary Key | Foreign Key |
|---------------------------------------|---------------|---------|-------------|-------------|
| Comments                              | varchar(2000) | No      | No          | No          |
| Comments                              |               |         |             |             |
| CreatedBy                             | int           | No      | No          | Yes         |
| Identification number for a NUMI user |               |         |             |             |
| DateCreated                           | datetime      | No      | No          | No          |
| Date that the record was created      |               |         |             |             |
| PatientStayAuditID                    | bigint        | Yes     | Yes         | No          |
|                                       |               |         |             |             |
| PatientStayID                         | bigint        | No      | No          | Yes         |
|                                       |               |         |             |             |
| StatusID                              | tinyint       | No      | No          | Yes         |
|                                       |               |         |             |             |
| IsAutoDismissed                       | bit           | No      | No          | No          |

<span id="_Toc169781973" class="anchor"></span>Table 32: Physician

### Table: Physician

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781974" class="anchor"></span>Table 33: PhysicianAdvisorPatientReason</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CreatedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateCreated</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was created</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DateModified</td>
<td>datetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was modified</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Disuser</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>This field is currently not used in NUMI, and not brought in from VistA. The reference to the VistA File/Field value is for informational purposes, and future use.</td>
<td><p>VistA File / Field</p>
<p>200 / 7</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>DUZ</td>
<td>bigint</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Vista identifier for a User</td>
<td><p>VistA File / Field</p>
<p>405 / .19</p>
<p>200 / IEN</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ModifiedByNumiUserID</td>
<td>int</td>
<td>No</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PhysicianID</td>
<td>int</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a NUMI user</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>PhysicianName</td>
<td>varchar(100)</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Name of the Physician</td>
<td><p>VistA File / Field</p>
<p>200 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Reason</td>
<td>varchar(200)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Reason provided by a Physician Advisor</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SiteID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Site</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc169781974" class="anchor"></span>Table 33: PhysicianAdvisorPatientReason

### Table: PhysicianAdvisorPatientReason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| CreatedByNumiUserID                                                                                                                 | int           | No      | No          | No          |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| DateCreated                                                                                                                         | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                    |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| DateModified                                                                                                                        | datetime      | No      | No          | No          |
| Date that the record was modified                                                                                                   |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| ModifiedByNumiUserID                                                                                                                | int           | No      | No          | No          |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| PAReasonCategory                                                                                                                    | tinyint       | No      | No          | No          |
| Identification of a Physician Advisor reason category                                                                               |               |         |             |             |
| PAReasonName                                                                                                                        | varchar(200)  | No      | No          | No          |
| Name of a Physician Advisor review reason                                                                                           |               |         |             |             |
| PhysicianAdvisorPatientReasonID                                                                                                     | smallint      | Yes     | Yes         | No          |
| Identification number for a Physician Advisor review reason                                                                         |               |         |             |             |

<span id="_Toc169781975" class="anchor"></span>Table 34: PhysicianAdvisorPatientReview

### Table: PhysicianAdvisorPatientReview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| Comments                                                                                                                            | varchar(4000) | No      | No          | No          |
| Comments                                                                                                                            |               |         |             |             |
| CreatedByNumiUserID                                                                                                                 | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| DateCreated                                                                                                                         | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                    |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| DateModified                                                                                                                        | datetime      | No      | No          | No          |
| Date that the record was modified                                                                                                   |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| ModifiedByNumiUserID                                                                                                                | int           | No      | No          | Yes         |
| Identification number for a NUMI user OtherDesc                                                                                     | varchar(2000) | No      | No          | No          |
| Additional description about the physician advisor portion of a patient review                                                      |               |         |             |             |
| PatientReviewID                                                                                                                     | bigint        | Yes     | No          | Yes         |
| Identification number for a patient review                                                                                          |               |         |             |             |
| PhysicianAdvisorID                                                                                                                  | int           | Yes     | No          | Yes         |
| Identification number for a Physician Advisor                                                                                       |               |         |             |             |
| PhysicianAdvisorPatientReasonID                                                                                                     | smallint      | No      | No          | Yes         |
| Identification number for a Physician Advisor patient review reason                                                                 |               |         |             |             |
| PhysicianAdvisorPatientReviewID                                                                                                     | bigint        | Yes     | Yes         | No          |
| Identification number for a Physician Advisor patient review                                                                        |               |         |             |             |
| RecommendedCareLevelID                                                                                                              | tinyint       | No      | No          | Yes         |
| Identification number for a Recommended Level of Care                                                                               |               |         |             |             |
| RecommendedCareLevelOther                                                                                                           | varchar(2000) | No      | No          | No          |
| Additional description about the physician advisor recommended level of care portion of a patient review                            |               |         |             |             |
| StatusChangeDate                                                                                                                    | datetime      | No      | No          | No          |
| Date that the Physician Advisor record status was changed                                                                           |               |         |             |             |
| StatusID                                                                                                                            | tinyint       | No      | No          | Yes         |
| Identification number for a Physician Advisor review status                                                                         |               |         |             |             |
| StatusNumiUserID                                                                                                                    | int           | No      | No          | Yes         |
| Identification number for a NUMI user Physician Advisor review status                                                               |               |         |             |             |

<span id="_Toc169781976" class="anchor"></span>Table 35: PhysicianAdvisorPatientReviewAudit

### Table: PhysicianAdvisorPatientReviewAudit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                         | Data Type     | Indexed | Primary Key | Foreign Key |
|--------------------------------------|---------------|---------|-------------|-------------|
| Comments                             | varchar(2000) | No      | No          | No          |
| Comments                             |               |         |             |             |
| CreatedBy                            | int           | No      | No          | Yes         |
| DateCreated                          | datetime      | No      | No          | No          |
| Date that the record was created     |               |         |             |             |
| PhysicianAdvisorPatientReviewAuditID | bigint        | Yes     | Yes         | No          |
| PhysicianAdvisorPatientReviewID      | bigint        | No      | No          | Yes         |
| StatusID                             | tinyint       | No      | No          | Yes         |

<span id="_Toc169781977" class="anchor"></span>Table 36: Reason

### Table: Reason

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| CreatedByNumiUserID                                                                                                                 | int           | No      | No          | Yes         |
| Date that the record was created                                                                                                    |               |         |             |             |
| DateCreated                                                                                                                         | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                    |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| DateModified                                                                                                                        | datetime      | No      | No          | No          |
| Date that the record was modified                                                                                                   |               |         |             |             |
| Description                                                                                                                         | varchar(1000) | No      | No          | No          |
| Description of a reason                                                                                                             |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| IsParentReason                                                                                                                      | bit           | Yes     | No          | No          |
| ModifiedByNumiUserID                                                                                                                | int           | No      | No          | Yes         |
| Date that the record was modified                                                                                                   |               |         |             |             |
| ParentReasonID                                                                                                                      | smallint      | Yes     | No          | No          |
| Identification for a parent reason                                                                                                  |               |         |             |             |
| ReasonCategoryID                                                                                                                    | smallint      | Yes     | No          | Yes         |
| Identification for a reason category                                                                                                |               |         |             |             |
| ReasonCode                                                                                                                          | varchar(100)  | No      | No          | No          |
| Identification number for a Reason Code                                                                                             |               |         |             |             |
| ReasonDesc                                                                                                                          | varchar(900)  | No      | No          | No          |
| Description of a reason                                                                                                             |               |         |             |             |
| ReasonFactorID                                                                                                                      | tinyint       | Yes     | No          | No          |
| ReasonID                                                                                                                            | smallint      | Yes     | Yes         | No          |
| Identification for a reason                                                                                                         |               |         |             |             |
| ReviewerTypeID                                                                                                                      | tinyint       | Yes     | No          | No          |
| Identification for a reviewer type                                                                                                  |               |         |             |             |
| ReviewTypeID                                                                                                                        | tinyint       | Yes     | No          | Yes         |
| Identification for a review type                                                                                                    |               |         |             |             |

<span id="_Toc169781978" class="anchor"></span>Table 37: ReasonCategory

### Table: ReasonCategory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name       | Data Type     | Indexed | Primary Key | Foreign Key |
|--------------------|---------------|---------|-------------|-------------|
| ReasonCategoryID   | smallint      | Yes     | Yes         | No          |
| ReasonCategoryDesc | varchar(50)   | No      | No          | No          |
| DateInactive       | smalldatetime | No      | No          | No          |
| Inactive           | bit           | No      | No          | No          |

<span id="_Toc169781979" class="anchor"></span>Table 38: Region

### Table: Region

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| Description                                                                                                                         | varchar(200)  | No      | No          | No          |
| Description of a Region                                                                                                             |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| RegionCode                                                                                                                          | varchar(10)   | Yes     | No          | No          |
| Identification code for a Region                                                                                                    |               |         |             |             |
| RegionID                                                                                                                            | tinyint       | Yes     | Yes         | No          |
| Identification number for a Region                                                                                                  |               |         |             |             |
| RegionName                                                                                                                          | varchar(100)  | No      | No          | No          |
| Description of a Region name                                                                                                        |               |         |             |             |

<span id="_Toc169781980" class="anchor"></span>Table 39: Reports

### Table: Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| createDate                                                                                                                          | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                    |               |         |             |             |
| Inactive                                                                                                                            | tinyint       | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| inactiveDate                                                                                                                        | datetime      | No      | No          | No          |
| lastUpdateDate                                                                                                                      | datetime      | No      | No          | No          |
| Date that the record was last updated                                                                                               |               |         |             |             |
| reportDescription                                                                                                                   | varchar(1000) | No      | No          | No          |
| Description of a report                                                                                                             |               |         |             |             |
| reportDisplayName                                                                                                                   | varchar(60)   | No      | No          | No          |
| Identification of a report                                                                                                          |               |         |             |             |
| reportFileName                                                                                                                      | varchar(80)   | No      | No          | No          |
| reportId                                                                                                                            | bigint        | Yes     | Yes         | No          |
| Identification number for a report                                                                                                  |               |         |             |             |
| reportSortOrder                                                                                                                     | smallint      | Yes     | No          | No          |
| Order in which Reports are displayed on application screens                                                                         |               |         |             |             |
| ssrsreportpath                                                                                                                      | varchar(120)  | No      | No          | No          |
|                                                                                                                                     |               |         |             |             |

<span id="_Toc169781981" class="anchor"></span>Table 40: ReviewType

### Table: ReviewType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| Abbreviation                                                                                                                        | varchar(10)   | No      | No          | No          |
| CERMEName                                                                                                                           | varchar(5)    | Yes     | No          | No          |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| ReviewTypeDesc                                                                                                                      | varchar(20)   | No      | No          | No          |
| Description of a review type                                                                                                        |               |         |             |             |
| ReviewTypeID                                                                                                                        | tinyint       | Yes     | Yes         | No          |
| Identification number for a review type                                                                                             |               |         |             |             |

<span id="_Toc169781982" class="anchor"></span>Table 41: ServiceSection

### Table: ServiceSection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc169781983" class="anchor"></span>Table 42: Site</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th>Element Name</th>
<th>Data Type</th>
<th>Indexed</th>
<th>Primary Key</th>
<th>Foreign Key</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DateInactive</td>
<td>smalldatetime</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Date that the record was inactivated</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Inactive</td>
<td>bit</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td><p>Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1</p>
<p>means that the record is inactive</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ServiceSectionDesc</td>
<td>varchar(100)</td>
<td>No</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Description of a Service Section</td>
<td><p>VistA File / Field</p>
<p>49 / .01</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ServiceSectionID</td>
<td>smallint</td>
<td>Yes</td>
<td>No</td>
<td>No</td>
</tr>
<tr class="even">
<td>Identification number for a Service Section</td>
<td><p>VistA File / Field</p>
<p>49 / IEN</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>ServiceSectionIEN</td>
<td>varchar(50)</td>
<td>Yes</td>
<td>Yes</td>
<td>No</td>
</tr>
<tr class="even">
<td>VistA identification number for a Service Section</td>
<td><p>VistA File / Field</p>
<p>49 / IE</p></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>SiteID</td>
<td>smallint</td>
<td>Yes</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>Identification number for a Site</td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc169781983" class="anchor"></span>Table 42: Site

### Table: Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| DateActive                                                                                                                          | smalldatetime | No      | No          | No          |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| DisplayName                                                                                                                         | varchar(100)  | No      | No          | No          |
| Name of the displayed Site name                                                                                                     |               |         |             |             |
| FaciltyName                                                                                                                         | varchar(200)  | No      | No          | No          |
| Name of a Site Facility                                                                                                             |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| Moniker                                                                                                                             | varchar(10)   | Yes     | No          | No          |
| Offset                                                                                                                              | smallint      | Yes     | No          | No          |
| SiteCode                                                                                                                            | varchar(10)   | Yes     | No          | No          |
| Identification code for a site                                                                                                      |               |         |             |             |
| SiteID                                                                                                                              | smallint      | Yes     | Yes         | No          |
| Identification number for a Site                                                                                                    |               |         |             |             |
| SiteName                                                                                                                            | varchar(100)  | Yes     | No          | No          |
| Name of a Site name                                                                                                                 |               |         |             |             |
| Synchronize                                                                                                                         | tinyint       | Yes     | No          | No          |
| VISNID                                                                                                                              | tinyint       | Yes     | No          | Yes         |
| Identification number for a Veterans Integrated Service Network site                                                                |               |         |             |             |
| IsStandardTime                                                                                                                      | bit           | No      | No          | No          |

<span id="_Toc169781984" class="anchor"></span>Table 43: Status

### Table: Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| CreatedByNumiUserID                                                                                                                 | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| DateCreated                                                                                                                         | datetime      | No      | No          | No          |
| Date that the record was created                                                                                                    |               |         |             |             |
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| DateModified                                                                                                                        | datetime      | No      | No          | No          |
| Date that the record was modified                                                                                                   |               |         |             |             |
| Enumeration                                                                                                                         | tinyint       | No      | No          | No          |
| Date that the record was modified                                                                                                   |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| ModifiedByNumiUserID                                                                                                                | int           | No      | No          | Yes         |
| Identification number for a NUMI user                                                                                               |               |         |             |             |
| StatusDesc                                                                                                                          | varchar(50)   | Yes     | No          | No          |
| Description of a Status                                                                                                             |               |         |             |             |
| StatusID                                                                                                                            | tinyint       | Yes     | Yes         | No          |
| Identification number for a Status                                                                                                  |               |         |             |             |

<span id="_Toc169781985" class="anchor"></span>Table 44: TreatingSpecialtyDismissalType

### Table: TreatingSpecialtyDismissalType

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                     | Data Type     | Indexed | Primary Key | Foreign Key |
|----------------------------------|---------------|---------|-------------|-------------|
| TreatingSpecialtyDismissalTypeID | int           | Yes     | Yes         | No          |
| DismissalTypeDesc                | nvarchar(50)  | No      | No          | No          |
| DateInactive                     | smalldatetime | No      | No          | No          |
| Inactive                         | bit           | No      | No          | No          |
| IsNonReviewable                  | bit           | No      | No          | No          |

<span id="_Toc169781986" class="anchor"></span>Table 45: VISN

### Table: VISN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type     | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|---------------|---------|-------------|-------------|
| DateInactive                                                                                                                        | smalldatetime | No      | No          | No          |
| Date that the record was inactivated                                                                                                |               |         |             |             |
| Description                                                                                                                         | varchar(200)  | No      | No          | No          |
| Description of a Veterans Integrated Service Network                                                                                |               |         |             |             |
| Inactive                                                                                                                            | bit           | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |               |         |             |             |
| RegionID                                                                                                                            | tinyint       | Yes     | No          | Yes         |
| Identification number of a Veterans Integrated Service Network Region                                                               |               |         |             |             |
| VISNCode                                                                                                                            | varchar(10)   | Yes     | No          | No          |
| Identification code of a Veterans Integrated Service Network                                                                        |               |         |             |             |
| VISNID                                                                                                                              | tinyint       | Yes     | Yes         | No          |
| Identification number of a Veterans Integrated Service Network                                                                      |               |         |             |             |
| VISNName                                                                                                                            | varchar(100)  | Yes     | No          | No          |
| Name of a Veterans Integrated Service Network                                                                                       |               |         |             |             |

<span id="_Toc169781987" class="anchor"></span>Table 46: WardLocation

### Table: WardLocation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name                                                                                                                        | Data Type                   | Indexed | Primary Key | Foreign Key |
|-------------------------------------------------------------------------------------------------------------------------------------|-----------------------------|---------|-------------|-------------|
| Bedsection                                                                                                                          | varchar(100)                | No      | No          | No          |
| Identifies a section of beds within a Ward location                                                                                 | VistA File / Field 42 / .02 |         |             |             |
| DateInactive                                                                                                                        | smalldatetime               | No      | No          | No          |
| Date that the record was inactivated                                                                                                |                             |         |             |             |
| Inactive                                                                                                                            | bit                         | No      | No          | No          |
| Indicator that the record is inactive; a value of 0 means that the record is ACTIVE, a value of 1 means that the record is inactive |                             |         |             |             |
| Service                                                                                                                             | varchar(100)                | No      | No          | No          |
| Identifies a Service associated with a Ward location                                                                                | VistA File / Field 42 / .03 |         |             |             |
| SiteID                                                                                                                              | smallint                    | Yes     | Yes         | Yes         |
| Identification number for a Site                                                                                                    |                             |         |             |             |
| SpecialtyID                                                                                                                         | smallint                    | Yes     | No          | No          |
| Identification number for a Treating Specialty that can be associated with ANY Facility or Ward                                     |                             |         |             |             |
| WardLocationDesc                                                                                                                    | varchar(100)                | Yes     | No          | No          |
| Description of a Ward location                                                                                                      | VistA File / Field 42 / .01 |         |             |             |
| WardLocationID                                                                                                                      | smallint                    | Yes     | No          | No          |
| Identification number for a Ward location                                                                                           |                             |         |             |             |
| WardLocationIEN                                                                                                                     | varchar(50)                 | Yes     | Yes         | No          |
| VistA identifier for a Ward location                                                                                                | VistA File / Field 42 / IEN |         |             |             |

<span id="_Toc169781988" class="anchor"></span>Table 47: WebLog

### Table: WebLog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Element Name       | Data Type     | Indexed | Primary Key | Foreign Key |
|--------------------|---------------|---------|-------------|-------------|
| DFN                | bigint        | No      | No          | No          |
| LookupSiteID       | smallint      | Yes     | No          | Yes         |
| Message            | varchar(4000) | No      | No          | No          |
| NumiUserID         | int           | Yes     | No          | No          |
| PatientSensitivity | tinyint       | No      | No          | No          |
| RemoteAddress      | varchar(50)   | No      | No          | No          |
| RequestPage        | varchar(100)  | No      | No          | No          |
| WebLogID           | bigint        | Yes     | Yes         | No          |

<span id="_Toc169781989" class="anchor"></span>Table 48: SQLJobs

## SQL Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table: SQLJobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="Table_5:_High_level_NUMI_exceptions" class="anchor"></span>Table 49: High level NUMI exceptions</p></caption>
<colgroup>
<col style="width: 61%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Job Name</strong></th>
<th><strong>Schedule</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>LogSyncDB_ValidateSynchronizer</td>
<td>Every hour</td>
</tr>
<tr class="even">
<td>Counts number of Raw Stays synced within the past three hours and emails a warning to a predefined list of administrators if count equals zero.</td>
<td></td>
</tr>
<tr class="odd">
<td>NUMI_PhysicianAdvisorPatientReview_AutoExpire</td>
<td>Every day at 12:00AM (Server Time)</td>
</tr>
<tr class="even">
<td>Updates and auto-expires PUMA reviews older than 14 days.</td>
<td></td>
</tr>
<tr class="odd">
<td>NUMI_usp_DaylightSavingsSite</td>
<td>Five different times one morning every spring</td>
</tr>
<tr class="even">
<td><p>Runs the NUMI stored procedure usp_DaylightSavingsSite.</p>
<p>Updates the offset field in the NUMI Site table for the change from standard time to daylight savings time.</p></td>
<td></td>
</tr>
<tr class="odd">
<td>NUMI_usp_StandardTimeSite</td>
<td>One time one morning every fall</td>
</tr>
<tr class="even">
<td><p>Runs the NUMI stored procedure usp_StandardTimeSite.</p>
<p>Updates the offset field in the NUMI Site table for the change from daylight savings time to standard time.</p></td>
<td></td>
</tr>
</tbody>
</table>

<span id="Table_5:_High_level_NUMI_exceptions" class="anchor"></span>Table 49: High level NUMI exceptions

## Report Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI can be configured to use a replicated database to produce reports. This enables a database load to be split off for report generation from the operational NUMI database to a report database.

### Report Database Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The report database connection information is configured in the NumiWebApp.config file. The information is contained in the application setting key "reportDbConnectionString". The default setting is the NUMI operational database. To change to a replicated database, enter the replicated database connection information in the application setting key.

# Exported Groups and/or Options and Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Exported Groups and/or Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable.

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI provides menus which are accessible to users on the major UI screens. Those menus provide access to various features of the NUMI application. This section describes the menus and their underlying functionality.

### Admin Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Admin Menu is only available to NUMI site administrator users. Non-administrator users will not see this menu option on the UI. If administrator users have problems using this menu or its features, administrator users should validate that their profile indicates they have the appropriate access privileges.

*Users* option - This feature is used to find VistA users, add/edit NUMI user information, assign user privileges, and deactivate user sites.

*Admin Sites* option - This feature is used to find VistA users, and add or remove users from the Physician Advisor Reviewer, Primary Reviewer, Site Administrators, and Report Access lists.

*Treating Specialty Configuration* option- This feature allows Administrators to modify the current configuration of dismissal behaviors on Facility Treating Specialties. Administrators can change the Dismissal Behavior for Treating Specialties with or without a Dismissal Behavior configured, as well as configure a Treating Specialty that has no Dismissal Behavior."

### Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Tools Menu is accessible to all NUMI users. However, the accessibility of certain options is based on individual access privileges.

*Patient Selection/Worklist* option - This feature is available to all users and lets them work with the Patient Selection screen, where they can select stays to perform primary reviews.

*UtilizationManagement Review Listing* option - This feature lets users work with the Patient Reviews screen, where they can see reviews that have either been saved for later, or saved/locked to the database. All users can Unlock and Copy reviews, and they can Delete their own reviews. Administrator users can Unlock, Copy and Delete any reviews.

*Dismissed Patient Stays* option - This feature is available to all users and lets them work with the Dismissed Patient Stays screen, where they can see patient stay reminders that have been dismissed.

*Free Text Search* option - This feature is available to all users and lets them search for patients using exact words, similar words, partial words or specific words. They can also filter by Date, Reviewer, Ward, Service and Treating Specialty, Movement Type and Patient.

*Physician Advisor Review* option - This feature is available to Physician Advisor users and lets them work with their Worklist. From this screen, they can access and work on the reviews that have been assigned to them.

*Manual VistA Synchronization* – This feature is available to all users and lets them synchronize stay information between VistA and NUMI. A feed containing admissions and ward transfer information is passed to NUMI from VistA once every hour (at the top of the hour) during the daytime, and again at midnight. With this feature, users do not need to wait for the next feed. They can retrieve and synchronize information on demand. This feature comes in handy when they know a patient has been admitted to the hospital and is in VistA, but they do not see them in NUMI yet.

*Patient Stay Administration* option – This feature is available to NUMI Administrator users. Patient stays that are in NUMI, but that NUMI can no longer find in VistA, are marked invalid in the system and will show up on the Patient Stay Administration screen. NUMI Administrators will use this feature to verify the status of the stay in VistA and delete patient stays in NUMI that are no longer in VistA, or that NUMI incorrectly marked invalid due to VistA connection problems. This situation may exist because an invalid patient admission was entered and the record was deleted from the hospital database – but not before it was sent to NUMI. Here is some background information about how this process works:

Patient movements are entered into VistA and then synchronized into the NUMI database. Every time a stay is touched in NUMI, NUMI goes back to VistA to update the stay record with any changes in VistA. If nothing is returned from VistA when the record is requested, then NUMI marks its record of the stay as Invalid, and removes it from the patient selection list. It is put in a limbo state, but not deleted. NUMI Administrators can then review the invalid stays using this screen. Selecting them from the table will cause NUMI to again try to retrieve them from VistA. If it cannot, the Administrator can delete the patient stay from NUMI. If NUMI can retrieve the stay, then the Administrator has the option of selecting the Restore button to reactivate the stay.

*Log out from NUMI* option—This feature is available to all users and will redirect them to the Logout screen. From this screen, users can choose to log back in or log out from the SSO.

### Help Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Online help for NUMI functionality consists of a Help Menu option on the major NUMI screens. The only option under this menu is User Guide. Selecting the option redirects users to the main Office of Quality, Safety and Value (OQSV) web page, where they will have hyperlinked access to view the latest version of the NUMI User Guide.

Help for CERME topics is available on the CERME screen in NUMI. Users will have access to a help dropdown containing help topics related to Change Healthcare CERME.

# Security Keys and/or Roles

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no VistA security keys or secondary menu options, and there are not any roles in NUMI. There are, however, six sets of activities which control a number of things, giving the appearance that there are roles. The activity sets are:

- ACCESS_ADMIN_TOOLS (add/remove users, add/remove permissions, and unlock and delete reviews)
- CREATE_AND_CONDUCT_PRIMARY_REVIEW
- CONDUCT_PHYSICIAN_ADVISOR_REVIEW
- REPORT_ACCESS
- FEE_BASED_CREATE_AND_CONDUCT_PRIMARY_REVIEW
- FEE_BASED_REPORT_ACCESS

## VistA Rights needed for NUMI users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

UM Reviewers will need to use Computerized Patient Record System (CPRS) to look up patient information while they work in NUMI, and will minimally need CPRS access. NUMI users must have the option *CPRSChart version n.n.n.n* (*OR CPRS GUI CHART*) on their menus.

<span id="8.2_General_Information" class="anchor"></span>It is also highly recommended that the VIAB WEB SERVICES OPTION be added to the System Command Options \[XUCOMMAND\] menu in each site's VistA system. If you do not add this to the Common Menu, you will need to add it to the secondary menu of each individual NUMI user.

## General Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI application is only accessible to authorized users. A User first needs to authenticate with the VA Identity and Access Management (IAM) before accessing the NUMI Login page. To authenticate with IAM, the user should select their VA Personal Identity Verification (PIV) card certificate and enter their PIV Personal Identification Number (PIN). NUMI also supports Secure Token Service (STS) integration with IAM. On successful authentication, the user will be directed to the appropriate landing page. If STS login fails, then users will be defaulted to the login page where NUMI confirms the domain ID of the IAM authenticated user. On the NUMI login page, the user selects a VISN, Site, access code, and verify code. NUMI verifies the credentials against VistA and the NumiUser table.

The Tier 3 Development Team will initially grant access to the system by manually adding the user to the NUMI database. Once NUMI is in production, the process of adding/editing NUMI users and assigning privileges will be performed at the facility level by designated NUMI Site Administrators.

Through online administration screens, Site Administrators can add and edit NUMI user information, and designate access privileges after verifying the existence of a valid VistA account. They can also deactivate one or more of a user's Sites (while there is no way to actually delete users, deactivating all of their Sites will essentially remove their NUMI access), and add or delete users from available lists.

NUMI has five designated 'roles' for users:

- Primary Reviewer
- Physician Advisor Reviewer
- Report Access
- Site Administrator
- Super Users

All authorized NUMI users have access to NUMI Enhanced Reports SharePoint site: [https://dvagov.sharepoint.com/sites/vhaum/SitePages/Enhanced-Reports-2.0.aspx](https://dvagov.sharepoint.com/sites/vhaum/SitePages/Enhanced-Reports-2.0.aspx?xsdata=MDV8MDJ8fDEyZGRlYzcwZmVjYjQ3NzIzNDZhMDhkY2UzYjlkODE0fGU5NWYxYjIzYWJhZjQ1ZWU4MjFkYjdhYjI1MWFiM2JmfDB8MHw2Mzg2MzU2MzQ1NjY2MjE3NTV8VW5rbm93bnxUV0ZwYkdac2IzZDhleUpXSWpvaU1DNHdMakF3TURBaUxDSlFJam9pVjJsdU16SWlMQ0pCVGlJNklrMWhhV3dpTENKWFZDSTZNbjA9fDB8fHw%3d&sdata=SGpoUUdJS1dEb256MnpvWU1BdExHbkpPZklZNGtrK3ZJRXpnVmtnRXpiVT0%3d)

This section provides a detailed description of the auditing functionality that is available in and performed by the NUMI software. As is required by Health Insurance Portability and Accountability Act (HIPAA), in order to reduce healthcare fraud and abuse and guarantee security and privacy of patient data, the NUMI system includes functionality which keeps track of all activity related to a patient's record.

### Audit and Accountability Policy and Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization develops, disseminates, and periodically reviews/updates: (i) a formal, documented, audit and accountability policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and (ii) formal, documented procedures to facilitate the implementation of the audit and accountability policy and associated audit and accountability controls.

<u>Control Implementation</u>: VA has identified this control as an agency-wide common control provided VA-wide by Office of Cyber Security (OCS).

### Auditable Events

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system generates audit records for the following events.

<u>Control Implementation</u>: The information system generates audit records for the following events: userid, date and time of event, actions of system administrators and operators, production of printed output, new objects and deletion of objects in user address space, security relevant events (logging into and out of the NUMI application), system configuration activities and events, events relating to use of privileges, all events relating to user identification and authentication, and the setting of userid' s.

The NUMI application will provide the means to create an audit trail of pertinent security and data related changes. It will log the following "events" on a user-by-user basis:

- All modifications to the NUMI database (insert, update, delete)
- Logging into and out of the NUMI application
- Database purges

### Content of Audit Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system produces audit records that contain sufficient information in audit records to establish what events occurred, the sources of the events, and the outcomes of the events.

<u>Control Implementation</u>: The NUMI application audit records capture sufficient information to establish what events occurred (identified by type, location, or subject), the sources of the events, and the outcomes of the events. A custom audit logger will be configured to save audit records to the database for reporting purposes. Information sent will include:

- User name
- Type of event
- Date and time of the event
- Other event-specific information

### Audit Storage Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization allocates sufficient audit record storage capacity and configures auditing to reduce the likelihood of such capacity being exceeded.

<u>Control Implementation</u>: The NUMI application allocates sufficient audit record storage capacity and establishes configuration settings to prevent such capacity from being exceeded.

### Response to Audit Processing Failures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system alerts appropriate organizational officials in the event of an audit processing failure, and take appropriate actions.

<u>Control Implementation</u>: In the event of an audit failure or audit storage capacity being reached, the NUMI application shall alert appropriate VA officials and takes the following additional actions: The system will notify the System Administrator and Information Security Officer by e-mail when approaching capacity and overwrite old audit records when full; it will provide a warning when allocated audit record equals or is greater than 85 percentage of maximum audit record storage: the space allocated allows for at least 1 week of data capture after the warning is generated. Currently the only auditing of events within the system boundary is at the O/S level.

### Audit Monitoring, Analysis and Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization regularly reviews/analyzes information system audit records for indications of inappropriate or unusual activity, investigates suspicious activity or suspected violations, reports findings to appropriate officials and takes necessary actions.

<u>Continuous Monitoring Guidance</u>: VA has identified this technical control for continuous monitoring activities at moderate and high impact levels. The production support team will be monitoring this control on some periodic basis by re-running the Security Control Assessment tests for AU-6 and documenting those activities, results, and any Plan of Actions and Milestones (POA&Ms) that may result within Security Management and Reporting Tool (SMART) Federal Information Security Management Act (FISMA).

<u>Control Implementation</u>: The Corporate Data Center Operations (CDCO) Security Team regularly review and analyze audit records for indications of inappropriate or unusual activity, investigates suspicious activity or suspected violations, reports findings to appropriate NUMI project and CDCO officials. The system employs automated mechanisms to integrate audit monitoring, analysis, and reporting into an overall process for investigation and response to suspicious activities.

### Audit Reduction and Report Generation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system provides an audit reduction and report generation capability.

<u>Control Implementation</u>: The NUMI application provides the capability to automatically process audit records for events of interest based upon selectable, event criteria. Currently the only auditing of events within the system boundary is at the O/S level.

### Time Stamps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system provides time stamps for use in audit record generation.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided VA-wide by CDCO. All CDCO servers are synchronized to an external time server creating accurate time stamps for audit record generation.

### Protection of Audit Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system protects audit information and audit tools from unauthorized access, modification, and deletion.

<u>Control Implementation</u>: The NUMI application protects audit information and audit tools from unauthorized access, modification, and deletion. Audit records are stored on a NUMI database.

### Audit Record Retention

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization retains audit records for to provide support for after-the-fact investigations of security incidents and to meet regulatory and organizational information retention requirements.

<u>Control Implementation</u>: The CDCO Security Team retains the NUMI application audit records for a minimum of one year or as documented in the National Archives and Records Administration retention periods, HIPAA legislation, VHA, or whichever is greater to provide support for after-the-fact investigations of security incidents and to meet regulatory and organizational information retention requirements.

## Security - Authentication and Authorization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Authentication and Authorization processes employed by the NUMI software.

### Identification and Authentication Policy and Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization develops, disseminates, and periodically reviews/updates: (i) a formal, documented, identification and authentication policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities and compliance; (ii) formal, documented procedures to facilitate the implementation of the identification and authentication policy and associated identification and authentication controls.

<u>Control Implementation</u>: VA has identified this control as an agency-wide common control provided VA-wide by OCS.

### User Identification and Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system uniquely identifies and authenticates users (or processes acting on behalf of users).

<u>Continuous Monitoring Guidance</u>: VA has identified this technical control for continuous monitoring activities at all impact levels. The NUMI project team will be monitoring this control on some periodic basis by re-running the Security Control Assessment tests for IA-2 and documenting those activities, results, and any POA&Ms that may result within SMART FISMA.

<u>Control Implementation</u>: The NUMI application uniquely identifies and authenticates users (or processes acting on behalf of users). Authentication of user identities is accomplished through the use of passwords, tokens, biometrics, or in the case of multifactor authentication, some combination thereof. The Control Enhancement requires multifactor authentication for remote system access that is National Institute of Standards and Technology defined level 3 or 4.

Currently the NUMI application System meets the Level 2 definition providing single factor remote network authentication. At Level 2, identity proofing requirements are introduced, requiring presentation of identifying materials or information.

### Device Identification and Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system identifies and authenticates specific devices before establishing a connection.

<u>Control Implementation</u>: The NUMI application identifies and authenticates specific devices utilizing VA authentication solutions to identify and authenticate devices on local and wide area networks. The application uses shared known information such as Transmission Control Protocol/Internet Protocol addresses to authenticate authorized devices.

### Identifier Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization manages user identifiers by: (i) uniquely identifying each user; (ii) verifying the identity of each user; (iii) receiving authorization to issue a user identifier from an appropriate organization official; (iv) issuing the user identifier to the intended party; (v) disabling the user identifier after of inactivity; and (vi) archiving user identifiers.

<u>Control Implementation</u>: The organization manages user identifiers by uniquely identifying each user verifying the identity of each user. Users sign on to the NUMI application using a SAML token obtained from Security Token Service using the IAM SiteMinder token, which grants them access to the appropriate VistA resources to run the NUMI application.

### Authenticator Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization manages information system authenticators by: (i) defining initial authenticator content; (ii) establishing administrative procedures for initial authenticator distribution, for lost/compromised, or damaged authenticators, and for revoking authenticators; (iii) changing default authenticators upon information system installation; and (iv) changing/refreshing authenticators periodically.

<u>Control Implementation</u>: The NUMI application manages information system authenticators through established procedures. NUMI utilizes SSO via IAM, granting them access specific content in the application. IAM manages two-factor authentication (2FA) and lost/compromised passwords, resetting passwords, revoking passwords and maintenance of system authenticators.

### Authenticator Feedback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system provides feedback to a user during an attempted authentication that feedback does not compromise the authentication mechanism.

<u>Control Implementation</u>: The NUMI application provides appropriate feedback to users during attempted authentication that does not compromise the authentication mechanism. This includes displaying asterisks when a user types a password, so it is not compromised.

### Cryptographic Module Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The information system employs authentication methods that meet the requirements of applicable laws, Executive Orders, directives, policies, regulations, standards, and guidance for authentication to a cryptographic module.

<u>Control Implementation</u>: VA Enterprise has not implemented cryptographic mechanisms in HL7 or VHA Health Information Model message transmission at this time.

## Security – Access Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes Access Control security relevant to the NUMI system.

### Physical and Environmental Protection Policy & Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization develops, disseminates, and periodically reviews/updates: (i) a formal, documented, physical and environmental protection policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and (ii) formal, documented procedures to facilitate the implementation of the physical and environmental protection policy and associated physical and environmental protection controls.

<u>Control Implementation</u>: VA has identified this control as an agency-wide common control provided VA-wide by OCS.

### Physical Access Authorizations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization develops and keeps current a list of personnel with authorized access to the facility where the information system resides (except those areas within the facility officially designated as publicly accessible) and issues appropriate authorization credentials.

Designated officials within the organization review and approve the access list and authorization credentials.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. The CDCO develops and keeps current lists of personnel with authorized access to the facility as well as to information systems (except those areas officially designated as publicly accessible) and issues appropriate authorization credentials. Designated officials within the CDCO review and approve the access list and authorization credentials at least annually.

### Physical Access Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization controls all physical access points (including designated entry/exit points) to the facility where the information system resides (except those areas within the facility officially designated as publicly accessible) and verifies individual access authorizations before granting access to the facility. The organization controls access to areas officially designated as publicly accessible, as appropriate, in accordance with the organization's assessment of risk.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. The CDCO controls all physical access points (including designated entry and exit points) to facilities containing information systems and verifies individual access authorizations before granting access to the facility. The CDCO also controls access to areas officially designated as publicly accessible, as appropriate, in accordance with the CDCO's assessment of risk.

### Access Control for Transmission Medium

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization controls physical access to information system distribution and transmission lines within organizational facilities.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. VA does not require, at this time, application of control PE-4 for Moderate impact applications.

### Access Control for Display Medium

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization controls physical access to information system devices that display information to prevent unauthorized individuals from observing the display output.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. The CDCO controls physical access to information system devices that display information to prevent unauthorized individuals from observing the display output. CDCO is not a public access facility thus reducing the likelihood of unauthorized individuals observing displayed information. In addition, access to the CDCO computer room, Security Services office space, and contracting office space is further limited by badge-controlled access for authorized individuals only.

### Monitoring Physical Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization monitors physical access to the information system to detect and respond to physical security incidents.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO.

### Visitor Control

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization controls physical access to the information system by authenticating visitors before authorizing access to the facility where the information system resides other than areas designated as publicly accessible.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. The CDCO controls physical access to information systems by authenticating visitors before authorizing access to the facility or areas other than those designated as publicly accessible.

### Access Records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization maintains visitor access records to the facility where the information system resides (except for those areas within the facility officially designated as publicly accessible) that includes: (i) name and organization of the person visiting; (ii) signature of the visitor; (iii) form of identification; (iv) date of access; (v) time of entry and departure; (vi) purpose of visit; and (vii) name and organization of person visited. Designated officials within the organization review the visitor access records after closeout.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO.

## Mail Groups, Alerts and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mail Groups and Bulletins are Not Applicable. The NUMI software utilizes none of these.

There is only one alert that is created by the software. The Synchronizer Service will send off an email alert if zero Raw Stays have been imported in the past three hours.

## Security - Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes contingency planning that is associated with the NUMI system.

### Contingency Planning Policy and Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization develops, disseminates, and periodically reviews/updates: (i) a formal, documented, contingency planning policy that addresses purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance; and (ii) formal, documented procedures to facilitate the implementation of the contingency planning policy and associated contingency planning controls.

<u>Control Implementation</u>: VA has identified this control as an agency-wide common control provided VA-wide by OCS.

### Contingency Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization develops and implements a Contingency Plan for the information system addressing contingency roles, responsibilities, assigned individuals with contact information, and activities associated with restoring the system after a disruption or failure. Designated officials within the organization review and approve the Contingency Plan and distribute copies of the plan to key contingency personnel.

<u>Control Implementation</u>: The NUMI project is dependent on the production site to develop, maintain, and test their Contingency Plan which encompasses the NUMI application within their physical boundaries. The Contingency Plan addresses contingency roles, responsibilities, assigned individuals with contact information, and activities associated with restoring the system after a disruption or failure. Designated officials within the organization review and approve the Contingency Plan and distribute copies of the plan to key contingency personnel. The NUMI System Owner or designated officials verify annually the Contingency Plan's maintenance and testing to verify the NUMI application requirements are met.

### Contingency Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization trains personnel in their contingency roles and responsibilities with respect to the information system and provides refresher training.

<u>Control Enhancements</u>: (1) The organization incorporates simulated events into contingency training to facilitate effective response by personnel in crisis situations. (2) The organization employs automated mechanisms to provide a more thorough and realistic training environment.

<u>Control Implementation</u>: VA has identified this control as a wide common control provided VA- wide by OCS.

### Contingency Plan Testing and Exercises

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization: (i) tests and/or exercises the Contingency Plan for the information system using to determine the plan's effectiveness and the organization's readiness to execute the plan; and (ii) reviews the Contingency Plan test/exercise results and initiates corrective actions.

<u>Continuous Monitoring Guidance</u>: VA has identified this technical control for continuous monitoring activities at MODERATE and HIGH impact levels. This will be done by monitoring this control on some periodic basis by re-running the Security Control Assessment tests for CP-4 and documenting those activities, results, and any POA&Ms that may result within SMART FISMA.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO.

### Contingency Plan Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization reviews the Contingency Plan for the information system and revises the plan to address system/organizational changes or problems encountered during plan implementation, execution, or testing.

<u>Control Implementation</u>: The NUMI application is dependent on the CDCO to develop, maintain, and test their Contingency Plan which encompasses the NUMI application within their physical boundaries. The NUMI System Owner or designated officials verify annually the CDCO Contingency Plan's maintenance and testing to verify NUMI application requirements are met.

The project team will revise the plan to address the system or organizational changes or problems encountered during plan implementation, execution, or testing, as required.

### Alternate Storage Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization identifies an alternate storage site and initiates necessary agreements to permit the storage of information system backup information. The frequency of information system backups and the transfer rate of backup information to the alternate storage site (if so designated) are consistent with the organization's recovery time objectives and recovery point objectives.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. The organization identifies an alternate storage site that is geographically separated from the primary storage site so as not to be susceptible to the same hazards. (2) The organization configures the alternate storage site to facilitate timely and effective recovery operations. (3) The organization identifies potential accessibility problems to the alternate storage site in the event of an area-wide disruption or disaster and outlines explicit mitigation actions.

The Continuity of Operations Planning (COOP) identifies the designated CDCO off-site storage facility, as well as the critical platform specific components necessary for recovery operations that will be stored at the site.

The off-site storage facility is geographically separated from the primary storage site so as not to be susceptible to the same hazards, and is configured to facilitate timely and effective recovery operations. CDCO also uses several offsite storage approaches ranging from the warm sites with replicated storage, offsite tape storage and an offsite subscription worksite recovery center.

The NUMI project team will identify an alternate storage site and initiate necessary agreements to permit the storage of information system backup information. The alternate storage site must be geographically separated from the primary storage site so as not to be susceptible to the same hazards. This facility is configured to facilitate timely and effective recovery operations. Any potential vulnerabilities of the alternate storage site will also be identified in the event of an area- wide disruption or disaster.

### Alternate Processing Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization identifies an alternate processing site and initiates necessary agreements to permit the resumption of information system operations for critical mission/business functions within when the primary processing capabilities are unavailable.

<u>Control Enhancements</u>: Equipment and supplies required to resume operations within the organization-defined time period are either available at the alternate site or contracts are in place to support delivery to the site. Timeframes to resume information system operations are consistent with organization-established recovery time objectives:

1.  The organization identifies an alternate processing site that is geographically separated from the primary processing site so as not to be susceptible to the same hazards
2.  The organization identifies potential accessibility problems to the alternate processing site in the event of an area-wide disruption or disaster and outlines explicit mitigation actions
3.  The organization develops alternate processing site agreements that contain priority-of-service provisions in accordance with the organization's availability requirements.
4.  The organization fully configures the alternate processing site so that it is ready to be used as the operational site supporting a minimum required operational capability.

<u>Control Implementation</u>: VA has identified this control as an agency-wide common control provided VA-wide by CDCO.

The CDCO COOP plans identify the designated CDCO alternate processing sites, necessary agreements to permit the resumption of information system operations for critical mission and business are established with each site, and critical equipment is pre-positioned at the site.

1.  CDCO's service level agreements call for a base level of 99% system availability. This availability is bounded by the demarcation point for the VA Wide Area Network and excludes periods of scheduled maintenance and information systems not included within CDCO's accredited Local Area Network.
2.  Systems are classified for recovery around three basic Recovery Time Objectives (RTOs) and two Recovery Point Objectives (RPOs). The RTOs supported are 12 hours, 72 hours, and 30 days. The RPOs supported are 2 hours data loss and last back up.

Data is protected in normal operations through mirroring and periodic tape backup stored off site. In the case of essential support and mission critical systems, a second mirror of the data is maintained at the designated recovery site for the system. These procedures are covered in the Contingency Plans for the applicable platforms and applications. For systems the customer or the CDCO (for infrastructure) have designated as mission critical, the RTO of 12 hours is supported by underpinning contracts for maintenance services and software support that allow incidents to be resolved within the 12-hour window.

### Telecommunications Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization identifies primary and alternate telecommunications services to support the information system and initiates necessary agreements to permit the resumption of system operations for critical mission/business functions within when the primary telecommunications capabilities are unavailable.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO.

### Information System Backup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization conducts backups of user-level and system-level information (including system state information) contained in the information system and protects backup information at the storage location.

<u>Continuous Monitoring</u>: VA has identified this technical control for continuous monitoring activities at all impact levels. This control will be monitored by re-running the Security Control Assessment tests for CM-9 and documenting those activities, results, and any POA&Ms that may result within SMART FISMA.

Control Implementation: VA has identified this control as a facility common control provided at the facility level by CDCO.

The CDCO performs full system backups, which are conducted once weekly. Applications and O/S are backed up on a need-to-be basis. Backups of sensitive, critical, and valuable information are stored in an environmentally protected and access-controlled site at least five miles from the site where the original copies reside. Backup tapes are verified at least once per quarter and whenever the COOP is tested.

### Information System Recovery and Reconstitution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Control</u>: The organization employs mechanisms with supporting procedures to allow the information system to be recovered and reconstituted to a known secure state after a disruption or failure.

<u>Control Implementation</u>: VA has identified this control as a facility common control provided at the facility level by CDCO. The COOP addresses recovery procedures in the event of a partial or full scale business disruption event. The plan includes recovery objectives that may be used to gauge the effectiveness of the recovery operations.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. There are no VA FileMan files associated with the NUMI software.

# Java Components (Client-Sided Java Components)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. There is no software being loaded to user workstations for NUMI.

# Set-up and Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI server configuration installed at the primary production site includes:

- 1 Load Balancer
- 2 NUMI Exchange Web Servers
- 2 NUMI/CERMe Web application Servers
- 1 Database server for NUMI and CERME
- 1 Replicated database server for reporting
- 1 SSRS web hosting server for reporting

The load balancer manages the distribution of user requests between the two available web application servers.

The Web Servers are installed with NUMI Exchange web services. These servers use a 64-bit O/S. NUMI Exchange provides interoperability between NUMI and other VA systems and applications.

The Web Application Servers are installed with NUMI and CERMe. These servers use a 64-bit O/S, which is supported by Change Healthcare Corporation. NUMI interacts with CERMe to obtain InterQual® criteria, used to ensure the patients are receiving the appropriate level of care.

The Database Server is installed and configured with the NUMI and CERMe databases. These servers use a 64-bit O/S.

Installation of the application requires that certain files, tools and utilities are present on the servers. The Tier 3 Development Team also utilizes various tools and supporting technologies in the development of the application.

## Deployment Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI web application is deployed to the NUMI web server. During the application installation, various configuration files must be modified to support the user environments and connectivity. The NUMI deployment package is provided by the Tier 3 Development Team.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides information about troubleshooting possible NUMI application errors. The NUMI database contains a table called InfoLog that can be used as a starting point for diagnosing the various system errors that may occur in the NUMI application. When configured in the NumiWebApp.config file, errors will be logged to this database table including (but not limited to) error message, the class and method where the error occurred in code, and the date/time the error occurred. In addition to errors, long running VIA transactions will also be logged to the InfoLog table. Also, configurable in the NumiWebApp.config file is a VIA timeout threshold value. VIA transactions that take longer to complete than this value will be recorded in the InfoLog table.

## High Level NUMI Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 49 lists some high level exceptions that would require troubleshooting.

| Exception Description                                    |
|----------------------------------------------------------|
| Unable to login                                          |
| Unable to access/view NUMI information                   |
| Application Timeout                                      |
| Application Lockout                                      |
| Login delays                                             |
| Network connect problems                                 |
| Unable to modify reviews                                 |
| Unable to find reviews                                   |
| Patient information not displaying                       |
| Unable to see information for multiple sites             |
| Unable to select criteria checkboxes on the CERMe screen |
| Screen resolution/display problems                       |

<span id="Table_6:_Front_End_Messages" class="anchor"></span>Table 50: Front End Messages

## Error Components and their Meaning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 50 describes some messages that may display to users on the NUMI front end. Regarding back end messages, all NUMI-specific messages visible to end users or support are passed to the UI for troubleshooting and support. Additionally, the infrastructure (e.g., IIS; MS SQLServer; the Windows O/S; other network components) may report additional information. Documentation for those particular subsystems must be consulted for more details.

<table>
<caption><p><span id="_Toc169781992" class="anchor"></span>Table 51: After Hours Remediation</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 28%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>GUI Message or Symptom</strong></th>
<th><strong>High Level Corrective Action</strong></th>
<th><strong>NUMI Action</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>'Please select a VISN'.</td>
<td>User did not select a VISN on the Select VISN, then Site screen.</td>
<td>Instruct user to select a VISN from the VISN dropdown.</td>
</tr>
<tr class="even">
<td>'Please select your hospital site'.</td>
<td>User did not select a Site on the Select VISN, then Site screen.</td>
<td>Instruct user to select a Site from the Site dropdown.</td>
</tr>
<tr class="odd">
<td>"Unable to login to VistA. The error was: VERIFY CODE must be changed before continued use".</td>
<td>User's VistA Verify Code has expired and needs to be changed.</td>
<td>Instruct user to login to VistA and change their Verify Code. Then they can try to login again.</td>
</tr>
<tr class="even">
<td>User cannot login.</td>
<td>VistA backups are running.</td>
<td>VistA backups run Monday-Friday at 1:30a.m. Instruct user to try logging in again at a later time.</td>
</tr>
<tr class="odd">
<td>User cannot see NUMI information.</td>
<td>User's browser does not allow pop- ups.</td>
<td>Instruct user to change their browser settings to accept pop- ups.</td>
</tr>
<tr class="even">
<td>'This site might require the following ActiveX control…'</td>
<td>User's browser does not allow ActiveX controls.</td>
<td>Instruct user to change their browser settings to accept ActiveX controls by selecting 'Install ActiveX Control' from the ActiveX dropdown.</td>
</tr>
<tr class="odd">
<td>User cannot access NUMI.</td>
<td>User is not using EDGE browser</td>
<td>Instruct user to install current EDGE browser and try logging in again.</td>
</tr>
<tr class="even">
<td>"You must select a patient"</td>
<td>User searched by patient name on Patient Selection/Worklist screen but did not click on a patient name in the result set.</td>
<td>Instruct the user to reinitiate their search and click on a patient name when the results display.</td>
</tr>
<tr class="odd">
<td>"Stay &lt;stay number&gt; for patient &lt;patient name&gt; cannot be retrieved from VistA and may be invalid. Please choose a different stay".</td>
<td>The user selected a stay from the Patient Selection/Worklist screen that is in NUMI but no longer in VistA.</td>
<td>One possible reason for this warning may be that an invalid patient admission was entered and the record was deleted from the hospital database, but not before it was sent to NUMI. Instruct the user to select a different stay.</td>
</tr>
<tr class="even">
<td>User is involuntarily logged out.</td>
<td>Application timeout occurs after the user has been idle for 20 minutes.</td>
<td>Instruct user to try logging in again. See Section 0 for more details about timeouts).</td>
</tr>
<tr class="odd">
<td>User cannot login to NUMI.</td>
<td>User exceeded the maximum number of permitted login attempts. [This number varies by VistA and is based on the local VistA policy].</td>
<td>VistA will lock the user's Access and Verify Codes for 20 minutes. After 20 minutes, VistA will automatically reset the Access and Verify Codes and the user can try to login again. (See Section 4.4 for more details about lockouts).</td>
</tr>
<tr class="even">
<td>User cannot login to NUMI.</td>
<td>VistA locked the user out of the application for exceeding the maximum number of login attempts.</td>
<td>If VistA has locked the user out, they will not be able to try logging in again for 20 minutes, at which time VistA will automatically unlock the Access/Verify Codes.</td>
</tr>
<tr class="odd">
<td>User cannot access NUMI.</td>
<td>User's PC is not connected to the network.</td>
<td>Check the user's PC connection to the network. Contact VA Helpdesk if you need further assistance.</td>
</tr>
<tr class="even">
<td>User cannot access NUMI.</td>
<td>A power outage may have occurred at the primary or secondary production sites.</td>
<td>Check with appropriate support staff at the primary and secondary production sites and if a power outage has occurred, request estimate of power restoration. Advise users.</td>
</tr>
<tr class="odd">
<td>User cannot access NUMI.</td>
<td>A problem with an application, database or web server may have occurred.</td>
<td>Check with appropriate support staff to determine if there are problems with the application, database or web servers. If there are server problems, request estimate of system restoration. Advise users</td>
</tr>
<tr class="even">
<td>User is unable to update a Review.</td>
<td>The review has been finalized and locked to the database.</td>
<td>If the user needs to modify the review, a NUMI Administrator will need to unlock the review.</td>
</tr>
<tr class="odd">
<td>User is unable to find a review.</td>
<td>Review has been deleted from NUMI.</td>
<td>If a review has been deleted it cannot be restored. Users with appropriate access rights should use caution when deleting reviews, for this reason.</td>
</tr>
<tr class="even">
<td>User is unable to find a patient movement.</td>
<td>Patient movement has been dismissed.</td>
<td>Instruct user to select 'Dismissed Patient Select' option from the Tools menu. The review should display in the search results.</td>
</tr>
<tr class="odd">
<td>User is unable to find a review.</td>
<td>Review has been performed. Once a patient review has been performed, the patient's name will be removed from the Dismissed Patient Stays screen.</td>
<td>Instruct user that the review will display on the Patient Selection/Worklist screen 24 hours later (assuming the next day's date has been selected as the Next Review Date).</td>
</tr>
<tr class="even">
<td>User is unable to find a review.</td>
<td>Review has been saved for later review.</td>
<td>Instruct user to select 'Utilization Management Review Listing' from the Tools menu. The review should display in the search results.</td>
</tr>
<tr class="odd">
<td>User cannot find a patient in NUMI.</td>
<td>Patient data is in VistA but is not showing up in NUMI.</td>
<td>There is an hourly feed of Admissions from VistA to NUMI, 24x7. Then the entire day will again be updated at midnight (per each time zone). User can either wait until the next feed, or they can use the synchronization feature under the Tools menu and manually synchronize NUMI with VistA.</td>
</tr>
<tr class="even">
<td>User cannot find patient information in NUMI.</td>
<td>Patient data is not in VistA or patient has not been admitted.</td>
<td>Patient information needs to be added to VistA or patient needs to be admitted.</td>
</tr>
<tr class="odd">
<td>Patient name does not display in the Patient Movements List.</td>
<td>Patient record has been selected for review</td>
<td>Once patient record is selected for review their name will be removed from the Patient Movements List. The name will display again in 24-72 hours.</td>
</tr>
<tr class="even">
<td>Patient name does not display in the Patient Movements List.</td>
<td>Next Review Reminder for the patient has been dismissed</td>
<td>If the Next Review Reminder has been dismissed for the patient, the record will not display in the Patient Movements List again unless it is selected for review from the Dismissed Patient Stays screen. Once the record is selected for review it will display in the Patient Movements List 24 hours later (provided the next day's date was identified as the Next Review Date).</td>
</tr>
<tr class="odd">
<td>User is unable to find a review.</td>
<td>Review has been saved for later review.</td>
<td>Instruct user to select the Utilization Management Review Listing option from the Tools menu. The review should display in the search results.</td>
</tr>
<tr class="even">
<td>User cannot access one or more sites.</td>
<td>User does not have permission to visit different sites, or the sites they can visit have not been added to their profile.</td>
<td>A user's site administrator can grant them access rights to multiple sites by updating the user's profile from the Add User Permissions admin screen.</td>
</tr>
<tr class="odd">
<td><p>User with appropriate permissions' Security or</p>
<p>Add-on settings are incorrect.</p></td>
<td>Security and Add-on settings are set up incorrectly.</td>
<td><p>Under Internet Options &gt; Manage Add-ons, verify that the Toolbar add-ons are set to "Enable".</p>
<p>Under Internet Options &gt; Security &gt; Internet &gt; Custom Level, verify that Active Scripting is set to "Enable".</p>
<p>Under Internet Options &gt; Security &gt; Local Intranet &gt; Custom Level, verify that Active Scripting is set to "Enable".</p>
<p>Under Internet Options &gt; Security &gt; Trusted Sites &gt; Custom Level, verify that Active Scripting is set to "Enable".</p>
<p>Under Internet Options &gt; General, click the Delete Files button.</p>
<p>Under Internet Options &gt; General, click the Delete Cookies button.</p></td>
</tr>
<tr class="even">
<td>NUMI screens do not display all information.</td>
<td>Screen cuts off information.</td>
<td>Incompatible screen resolution setting. Instruct user to set their screen resolution to 1024x768 or higher.</td>
</tr>
<tr class="odd">
<td>NUMI screen display is too large or too small.</td>
<td>Screen text/icon display too large or too small.</td>
<td>Incompatible screen resolution setting. Instruct user to set their screen resolution to 1024x768 or higher.</td>
</tr>
<tr class="even">
<td>"Warning – Patient is Deceased"</td>
<td>The user has selected a patient who is deceased.</td>
<td>Instruct the user to click the 'Continue Primary Review' button, if they wish to continue working with the review.</td>
</tr>
<tr class="odd">
<td>"Warning – Sensitive Patient"</td>
<td>The user has selected a patient whose record contains sensitive information.</td>
<td>Instruct user to click the 'Continue Primary Review' button, to continue working. The user will need to prove they have a need to know. Access to this patient is tracked and their station Security Officer will contact them for their justification.</td>
</tr>
<tr class="even">
<td>"Changing the subset for this review will erase all criteria point selections, criteria point notes and outcomes for this review. Do you want to change the subset for this review?"</td>
<td>The user has selected the 'Change Subset' button.</td>
<td>User can select 'Yes' option to change the subset or 'No' to cancel.</td>
</tr>
<tr class="odd">
<td>"Changing this choice will erase all criteria. Click Yes to change or No to keep the old value."</td>
<td>Changing Current Level of Care value on the CERMe screen will erase all criteria selections on the screen.</td>
<td>User can select 'Yes' option to change the Current Level of Care or 'No' to cancel.</td>
</tr>
<tr class="even">
<td>"Admit to Inpatient / Observation"</td>
<td>Selection of certain criteria on the CERMe screen produces system message recommending admission.</td>
<td>User selects 'OK' button to continue working on the review.</td>
</tr>
<tr class="odd">
<td>"Admit to Inpatient / Observation and refer to Dual Diagnosis criteria subset for Concurrent review."</td>
<td>Selection of certain criteria on the CERMe screen produces system message recommending admission.</td>
<td>User selects 'OK' button to continue working on the review.</td>
</tr>
<tr class="even">
<td>'Unsupported review type. Please use another CERME review'.</td>
<td>User has opened a review that is not supported in NUMI and then clicked the 'Continue Primary Review' button on the CERME screen. [A behavioral psych procedure is one example of when this message may display].</td>
<td>CERME supports the review but NUMI does not. A reason for this message may be that the user selected a Behavioral Health Procedure Review. Procedure Reviews are not supported in NUMI. Instruct user to select another review.</td>
</tr>
<tr class="odd">
<td>'You must select a patient'.</td>
<td>User has performed a search but did not select a patient name in the Patient Selection/Worklist screen result table.</td>
<td>Instruct must click on the name of the patient they wish to work within the result table.</td>
</tr>
<tr class="even">
<td>'There are no more review steps'.</td>
<td>User clicked 'Next Step' button on the CERME screen.</td>
<td>This is a known Change Healthcare CERME message. It is not a NUMI system error that requires a help desk ticket. To bypass the message, instruct user to click 'OK', and then click the 'Continue Primary Review' button.</td>
</tr>
<tr class="odd">
<td><p>"This review will now lock into the NUMI database.</p>
<p>Further changes require an administrator. Are you sure you are ready to lock this review?"</p></td>
<td>Selecting the FINAL SAVE/Lock to Database button locks the review and commits the information to the database.</td>
<td><p>If a user wishes to unlock a review, follow these guidelines when instructing them in how to do this:</p>
<ul>
<li><p>Primary Reviewers can Unlock and Delete their own reviews.</p></li>
<li><p>NUMI site administrators can Unlock and Delete any reviews</p></li>
<li><p>NUMI site administrators can Unlock or Delete reviews on behalf of a Physician Advisor</p></li>
</ul></td>
</tr>
<tr class="even">
<td>"The Web page you are viewing is trying to close the window. Do you want to close this window?"</td>
<td>User initiates Logout action. System prompts for confirmation that user wants to logout of NUMI.</td>
<td>User selects 'Yes' to continue with Logout or 'No'. User can also click a 'here' hyperlink to login again.</td>
</tr>
<tr class="odd">
<td>No insurance information displays for the patient.</td>
<td>User has no insurance information on file.</td>
<td>No further action necessary.</td>
</tr>
<tr class="even">
<td>"Please select a reason".</td>
<td>User did not select a Stay Reason while working on the Primary Review screen.</td>
<td>Instruct the user to select a Stay Reason.</td>
</tr>
<tr class="odd">
<td>"You do not have admin access to modify user privileges for: &lt;user name&gt;.</td>
<td>The user does not have administrative permissions for NUMI.</td>
<td>Instruct the user to contact the NUMI POC for their facility if they have a need to be able to perform administrative tasks on NUMI.</td>
</tr>
<tr class="even">
<td>User unable to perform certain activities even though their privileges are correct.</td>
<td>A user's privileges were changed but they are still unable to perform certain activities on NUMI.</td>
<td>Changes to privileges will not take effect until the user logs out and back in. Instruct the user to do that and they should be able to access the features they need.</td>
</tr>
<tr class="odd">
<td><p>"Invalid URL Information entered ReviewManager.xml, URL tag. Check if URL points to the right Database or Check for URL syntax in CERME / Driver documentation. If using ODBC, check ODBC name as entered in Windows matches ReviewManager.xml entry. Userid/Password combination may not be correct. Error accessing</p>
<p>/rm/iqm/html/gateway"</p>
<p>OR….</p>
<p>"CERME has lost connection with the database server".</p></td>
<td>The user receives this message when trying to perform a review on the CERME screen in NUMI.</td>
<td><p>This error would occur when the CERME server loses connectivity with the database. The resolution is to submit a CA Technologies/Service Desk Manager (CA/SDM) help ticket so that someone in the support chain (e.g., Tier 3) can restart the CERME server service, or the application server (the actual hardware) can be rebooted by on-site support.</p>
<p><strong>NOTE:</strong> This problem is believed to be limited to a previous version of CERME and the newest version does not appear to be susceptible to the same problem.</p></td>
</tr>
<tr class="even">
<td>User has questions / problems while working on the CERME screen.</td>
<td>Determine whether the question/problem relates to NUMI or CERME functionality. The only NUMI functionality on the screen is the tabs at the top of the CERME screen and the <em>Continue</em> <em>Primary</em> <em>Review</em> button. See the NUMI Action column for the appropriate next steps.</td>
<td><p>Instruct the user to either create a CA Technologies/ (CA/SDM) ticket, or call the VA SD and ask them to place one for them.</p>
<p>The ticket will then go through the PS/PIMS team and be referred to Tier 3 support, if necessary, if the question/problem relates to NUMI functionality.</p>
<p>If the question/problem relates to CERME functionality or the UM process or the application of the clinical criteria, advise the user to call or go to the Change Healthcare Customer Support Hub for assistance.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc169781992" class="anchor"></span>Table 51: After Hours Remediation

## Common Executable Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not Applicable. There are no common executable (.exe) messages in NUMI. The only messages generated are validation messages.

## General Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  
2.  
3.  
4.  

### CERMe

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Problems related to CERMe functionality are to be reported to Change Healthcare Corporation for research and resolution.

### Tier 2 and Tier 3 Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For problems related to the NUMI application, please call your local NUMI site administrator. If the problem cannot be resolved by the site administrator, contact local IT support. If the issue can't be resolved locally, you may create a Service Now ticket in IT Service Management (ITSM) through the self-serve portal, or call the Enterprise Service Desk (ESD) at 888-596-4357. A ticket can be created at any time, but software support teams work during regular daytime business hours, and only tickets designated as emergencies will be addressed during off-hours. Below is the Service Now configuration for NUMI support:

CATEGORY: Affected Service

Affected Service: National Utilization Management Integration

GROUP: PLM.Health.HealthCareAdmin

A member of the Tier 2 VistA Front Office group will respond to the ticket, and if it cannot be resolved at the Tier 2 level they will refer it to the Tier 3 support group.

### After Hours Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](numi-systems-management-guide-version-15-15/006.png)

<span id="_Toc169781999" class="anchor"></span>Figure : Architect Overview

<table>
<caption><p><span id="Table_7:_Acronyms_and_Terms" class="anchor"></span>Table 52: Acronyms and Terms</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 28%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>Symptom</th>
<th>High Level Corrective Action</th>
<th>NUMI Action</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>User cannot reach NUMI login screen.</td>
<td><p>Open ticket to address SSOI</p>
<p>Assigned group:</p>
<p>ACS Tier 3 Support</p></td>
<td>N/A</td>
</tr>
<tr class="even">
<td>Dropdown list on NUMI login not loading</td>
<td><p>Open ticket with VIA</p>
<p>Assigned group:</p>
<p>NTL SUP VIA</p></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td><strong>Reviews not opening in CERME</strong></td>
<td><strong>Restart CERME service</strong></td>
<td><strong>Restart CERME service</strong></td>
</tr>
<tr class="even">
<td>Intermittent unhandled exceptions while clicking on patients</td>
<td><p>Open ticket with VIA</p>
<p>Assigned group:</p>
<p>NTL SUP VIA</p></td>
<td><p>Check NUMI db info log table with this query:</p>
<p>select info, username, datecreated from infolog</p>
<p>where datecreated &gt; 'today'</p>
<p>and info like '%closed%'  </p>
<p>If the info field contains a similar error to:</p>
<p><em>Error connecting to VIA: The underlying connection was closed: An unexpected error occurred on a send.</em></p>
<p><em>The underlying connection was closed: An unexpected error occurred on a receive.</em></p>
<p>Use this a confirmation of the problem and open ticket with VIA.</p></td>
</tr>
</tbody>
</table>

<span id="Table_7:_Acronyms_and_Terms" class="anchor"></span>Table 52: Acronyms and Terms

## Interface Control Document (ICD) References for Messaging Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable. NUMI does not utilize Health Level 7 (HL7) messages or use any ICD references to them.

# Appendix A– Acronyms and Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 52 contains descriptors for acronyms and terms used in this document.

<table>
<caption><p><span id="Table_8:_Free_Text_Search_from_Utilizati" class="anchor"></span>Table 53: Free Text Search from UM Review Listing and Free Text Pages</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Acronym / Term</strong></th>
<th><strong>Descriptor</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>.NET Framework</td>
<td>A software component that is a part of MS Windows O/S. It has a large library of pre-coded solutions to common program requirements, and manages the execution of programs written specifically for the framework. The.NET Framework is a key MS offering, and is intended to be used by most new applications created for the Windows platform</td>
</tr>
<tr class="even">
<td>Active X</td>
<td>A component object model developed by MS for Windows platforms. Software based on ActiveX technology is prevalent in the form of Internet Explorer plugins and, more commonly, in ActiveX controls, ActiveX based applications launched from web pages</td>
</tr>
<tr class="odd">
<td>ActiveX Control</td>
<td>A reusable component which implements the IUnknown interface. Such components do not amount to an entire application; rather they provide a small building-block that can be shared by different software. The fact that command buttons look the same in almost any program on a platform is an example of component reusability that is not just limited to ActiveX controls. ActiveX controls are very important prior to the computer's security and are normally used to setup passwords</td>
</tr>
<tr class="even">
<td>Agile Iterative Development</td>
<td>A conceptual framework for software engineering that promotes development iterations throughout the life-cycle of the project. Software developed during one unit of time is referred to as an 'Iteration'. Each Iteration is an entire software project including planning, requirements analysis, design, coding, testing, and documentation</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Programming Interface</td>
</tr>
<tr class="even">
<td>ASP</td>
<td>Active Server Pages- MS's first server-side script engine for dynamically-generated web pages</td>
</tr>
<tr class="odd">
<td>ASP.NET</td>
<td>A web application framework marketed by MS that programmers can use to build dynamic web sites, web applications and web services. It is part of MS's .Net platform and is the successor to MS's ASP technology</td>
</tr>
<tr class="even">
<td>C# (C 'Sharp')</td>
<td>An object-oriented programming language developed by MS as part of the .Net initiative</td>
</tr>
<tr class="odd">
<td>CDCO</td>
<td>Corporate Data Center Operations</td>
</tr>
<tr class="even">
<td>CERMe</td>
<td>Care Enhance Review Management Enterprise</td>
</tr>
<tr class="odd">
<td>Component</td>
<td>An assembly, or part thereof, that is essential to the operation of some larger assembly and is an immediate subdivision of the assembly to which it belongs</td>
</tr>
<tr class="even">
<td>COOP</td>
<td>Continuity of Operations Planning</td>
</tr>
<tr class="odd">
<td>COTS</td>
<td>Commercial Off The Shelf</td>
</tr>
<tr class="even">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="odd">
<td>DAL</td>
<td>Data Access Layer</td>
</tr>
<tr class="even">
<td>DAO</td>
<td>Data Access Objects</td>
</tr>
<tr class="odd">
<td>ERM</td>
<td>Entity-Relationship Model</td>
</tr>
<tr class="even">
<td>FISMA</td>
<td>Federal Information Security Management Act</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface</td>
</tr>
<tr class="even">
<td>HIPPA</td>
<td>Health Insurance Portability and Accountability Act</td>
</tr>
<tr class="odd">
<td>HTTPS</td>
<td>Hyper Text Transfer Protocol Secured</td>
</tr>
<tr class="even">
<td>IAM</td>
<td>Identity and Access Management—The authentication service that validates the logged in user through PIV or other mechanisms.</td>
</tr>
<tr class="odd">
<td>ICD</td>
<td>Interface Control Document</td>
</tr>
<tr class="even">
<td>IIS</td>
<td>Internet Information Server</td>
</tr>
<tr class="odd">
<td>IRM</td>
<td>Information Resource Management</td>
</tr>
<tr class="even">
<td>IEN</td>
<td>Internal Entry Number</td>
</tr>
<tr class="odd">
<td>Internet Information Server</td>
<td>A set of Internet-based services for servers using MS Windows. It is the world's second most popular web server in terms of overall websites, behind Apache HTTP Server</td>
</tr>
<tr class="even">
<td>Interconnection Security Agreement</td>
<td>Federally mandated for any system, contractor or agency that touches the Federal network. This is a component of the Security Certification and Accreditation (C&amp;A) process which is also Federally mandated</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td>Information Security Officer</td>
</tr>
<tr class="even">
<td>JavaScript</td>
<td>A scripting language most often used for client-side web development. JavaScript was influenced by many languages and was designed to have a similar look to Java, but be easier for non-programmers to work with. The language is best known for its use in websites (as client-side JavaScript), but is also used to enable scripting access to objects embedded in other applications</td>
</tr>
<tr class="odd">
<td>MDO</td>
<td>Medical Domain Objects</td>
</tr>
<tr class="even">
<td>MDWS</td>
<td>Medical Domain Web Services. MDWS was the mechanism for importing VistA information into NUMI before VIA.</td>
</tr>
<tr class="odd">
<td>Medora UM</td>
<td>A class III Web-based application that interfaces with CERMe</td>
</tr>
<tr class="even">
<td>Module</td>
<td>An interchangeable subassembly that constitutes part of a larger device or system</td>
</tr>
<tr class="odd">
<td>MSBuild</td>
<td>Development tool used for build scripts</td>
</tr>
<tr class="even">
<td>National Utilization</td>
<td>A Web-based application that automates documentation of clinical features</td>
</tr>
<tr class="odd">
<td>Management Integration</td>
<td>relevant to each patient's condition and the associated clinical services provided as part of VHA's medical benefits pack</td>
</tr>
<tr class="even">
<td>NUMI</td>
<td>National Utilization Management Integration</td>
</tr>
<tr class="odd">
<td>OCS</td>
<td>Office of Cyber Security</td>
</tr>
<tr class="even">
<td>O/S</td>
<td>Operating System</td>
</tr>
<tr class="odd">
<td>OQSV</td>
<td>Office of Quality, Safety and Value</td>
</tr>
<tr class="even">
<td>PIV</td>
<td>Personal Identity Verification</td>
</tr>
<tr class="odd">
<td>POA&amp;Ms</td>
<td>Plan of Actions and Milestones</td>
</tr>
<tr class="even">
<td>Production Environment</td>
<td>Used for live product operation. The build manager creates production builds for this environment and coordinates installation with the operations staff</td>
</tr>
<tr class="odd">
<td></td>
<td>Quality, Safety and Value</td>
</tr>
<tr class="even">
<td>RAID</td>
<td>Redundant Array of Inexpensive Disks</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td>Remote Procedure Call- A client/server infrastructure that increases the interoperability, portability and flexibility of an application by allowing the application to be distributed over multiple platforms</td>
</tr>
<tr class="even">
<td>RTC</td>
<td>Rational Jazz Team Server</td>
</tr>
<tr class="odd">
<td>RTO</td>
<td>Recovery Time Objectives</td>
</tr>
<tr class="even">
<td>Runtime</td>
<td>Describes the operation of a computer program, the duration of its execution, from beginning to termination</td>
</tr>
<tr class="odd">
<td>SAN</td>
<td>Storage Area Network</td>
</tr>
<tr class="even">
<td>SDM</td>
<td>Service Desk Manager</td>
</tr>
<tr class="odd">
<td>Secure Sockets Layer</td>
<td><p>Encrypts data so that no one who intercepts is able to read it</p>
<p>Can assure a client that they are dealing with the real server they intended to connect to</p>
<p>Can prevent any unauthorized clients from connecting to the server</p>
<p>Prevents anyone from meddling with data going to or coming from the server</p></td>
</tr>
<tr class="even">
<td>Security Requirements</td>
<td>Document support for the Certification and Accreditation (C&amp;A) process relevant to the acceptance of the NUMI application as production-ready by the OCS</td>
</tr>
<tr class="odd">
<td>SLA</td>
<td>Service Level Agreement- A document describing the level of service and support that shall be provided to a system or application</td>
</tr>
<tr class="even">
<td>SMART FISMA</td>
<td>Security Management and Reporting Tool FISMA.SMART FISMA is a database that monitors FISMA compliance.</td>
</tr>
<tr class="odd">
<td>SOAP</td>
<td>Simple Object Access Protocol. A protocol for exchanging XML-based messages over computer networks, normally using HTTP/HTTPS.SOAP forms the foundation layer of the web services protocol stack providing a basic messaging framework upon which abstract layers can be built</td>
</tr>
<tr class="even">
<td>SQL</td>
<td>Structured Query Language</td>
</tr>
<tr class="odd">
<td>SSL</td>
<td>Secure Socket Layer</td>
</tr>
<tr class="even">
<td>SSO</td>
<td>Single Sign On</td>
</tr>
<tr class="odd">
<td>SSRS</td>
<td>SQL Server Reports Server</td>
</tr>
<tr class="even">
<td>Subversion</td>
<td>Development tool used for source control (including tagged releases)</td>
</tr>
<tr class="odd">
<td>Trac</td>
<td>An enhanced Wiki and issue tracking system for software development projects. Trac uses a minimalistic approach to web-based software project management</td>
</tr>
<tr class="even">
<td>UI</td>
<td>User Interface</td>
</tr>
<tr class="odd">
<td>UM</td>
<td>Utilization Management-The process of evaluating and determining the coverage and the appropriateness of medical care services across the patient health care continuum to ensure the proper use of resources</td>
</tr>
<tr class="even">
<td>Stay Synchronizer</td>
<td>A mechanism for getting information for a Stay in ADT's prior to the query date range</td>
</tr>
<tr class="odd">
<td>UML</td>
<td>Unified Modeling Language</td>
</tr>
<tr class="even">
<td>Unified Modeling Language</td>
<td>An ISO specification language for modeling objects</td>
</tr>
<tr class="odd">
<td>URL</td>
<td>Uniform Resource Locator</td>
</tr>
<tr class="even">
<td>User Interface</td>
<td>Specifies the features for user interface (specific page) models or paradigms</td>
</tr>
<tr class="odd">
<td>VB.NET (Visual Basic .NET)</td>
<td>An object-oriented computer language that can be viewed as an evolution of MS's Visual Basic (VB) implemented on the MS .Net Framework</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="odd">
<td>VIA</td>
<td>VistA Integration Adapter</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Information Systems Technology Architecture</td>
</tr>
<tr class="odd">
<td>VISN</td>
<td>Veterans Integrated Service Network. References one of the many Veteran's Administration sites</td>
</tr>
<tr class="even">
<td>VWS</td>
<td>VistA Web Services</td>
</tr>
<tr class="odd">
<td>VWS Services</td>
<td>Required to get patient and patient movement data from VistA and provide as Web service</td>
</tr>
<tr class="even">
<td>Web Services</td>
<td>A software system designed to support interoperable Machine to Machine interaction over a network. The term refers to Clients and Servers that communicate using XML messages that follow the SOAP standard</td>
</tr>
<tr class="odd">
<td>Web Service Description Language</td>
<td>Web services programming language</td>
</tr>
<tr class="even">
<td>Wiki</td>
<td>Software that allows users to create, edit, and link web pages easily</td>
</tr>
<tr class="odd">
<td>WSDL</td>
<td>Web Services Description Language</td>
</tr>
<tr class="even">
<td>XML</td>
<td>Extensible Markup Language- A general-purpose markup language. Its primary purpose is to facilitate the sharing of structured data across different information systems, particularly via the Internet. Required to parse fields from Change Healthcare CERMe</td>
</tr>
<tr class="odd">
<td>XPath (XML Path Language)</td>
<td>A language for selecting nodes from an XML document. In addition, XPath may be used to compute values (strings, numbers, or boolean values) from the content of an XML document</td>
</tr>
</tbody>
</table>

<span id="Table_8:_Free_Text_Search_from_Utilizati" class="anchor"></span>Table 53: Free Text Search from UM Review Listing and Free Text Pages

# Appendix B - Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix describes general dependencies associated with NUMI.

- The software for the VIA is functional and operating
- The software for the IIS application servers is functional and operating
- The software for VistA is functional and operating
- The software for CERMe is functional and operating
- The Stay Synchronizer is functional and operating
- The SQL Server Database is functional and operating
- The primary production site is fully operational
- Computer center equipment, including components supporting the NUMI application is connected to an Uninterruptible Power Supply that provides electricity, even during a power failure
- The equipment, connections and capabilities required to operate the NUMI application are available and functional
- Backups of the application software and data are intact and available
- Service Level Agreements are in place and maintained to support the NUMI hardware, software, interfacing systems and communications providers

# Appendix C – Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix describes interfaces that are associated with the NUMI software. (There are no external interface models or external design elements for NUMI). NUMI interfaces with a COTS product from Change Healthcare Corporation. Change Healthcare CERMe provides CERMe Review Text that is presented to users in Read-Only format.

The process for interfacing NUMI with Change Healthcare is:

- User performs review in the NUMI Web application
- User selects Save and an XML string is sent to CERMe
- The CERMe servlet launches
- User is allowed to enter additional data
- User chooses Save in the CERMe software
- The data is processed through the algorithm
- The results are sent back to NUMI as an XML string
- NUMI stores the CERMe results
- NUMI then needs a link back to a minimal record in CERMe The CERMe Interface provides:
- An Editor account that allows users to add/update reviews with the embedded CERMe Interface
- A Read Only account that allows users to view the contents of a review performed in the CERMe Interface - but not to make changes

User account setup is determined by the user permissions, as determined by NUMI.

# Appendix D – References and Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix identifies references and official policies relevant to the NUMI project.

- FIPS 199, "Standards for Security Categorization of Federal Information and Information Systems"
- FIPS 200, "Minimum Security Requirements for Federal Information and Information Systems"
- FIPS 201-1, "Personal Identity Verification of Federal Employees and Contractors"
- FIPS 140-2, "Security Requirements for Cryptographic Modules"
- CDCO Directive 7600, CDCO Handbook 7600.1
- VA Directive 6500.3, "Information Security Program"
- VA Directive and Handbook 0710, "Personnel Suitability and Security Program"
- VA Directive and Handbook 0730, "Security and Law Enforcement"
- VA Directive 6100, "Telecommunications"
- VA Directive and Handbook 6102, "Internet/Intranet Services"
- VA Directive 6502, "Privacy Program"
- NIST SP 800-12, "An Introduction to Computer Security: The NIST Handbook"
- NIST SP 800-18, Revision 1 "Guide for Developing System Security Plans"
- NIST SP 800-23, "Guideline to Federal Organizations on Security Assurance and Acquisition/Use of Tested/Evaluated Products"
- NIST SP 800-26, "Security Self-Assessment Guide for Information Technology Systems"
- NIST SP 800-27, Rev A, "Engineering Principles for Information Technology Security (A Baseline for Achieving Security)"
- NIST SP 800-28, "Guidelines on Active Content and Mobile Code"
- NIST SP 800-30, "Risk Management Guide for Information Technology Systems"
- NIST SP 800-34, "Contingency Planning Guide for Information Technology Systems"
- NIST SP 800-35, "Guide to Information Technology Security Services"
- NIST SP 800-36, "Guide to Selecting Information Security Products"
- NIST SP 800-37, Draft, "Guide for the Security Certification and Accreditation of Federal Information Systems"
- NIST SP 800-40, "Procedures for Handling Security Patches"
- NIST SP 800-42, "Guideline on Network Security Testing"
- NIST SP 800-46, "Security for Telecommuting and Broadband Communications"
- NIST SP 800-47, "Security Guide for Interconnecting Information Technology Systems"
- NIST SP 800-48, "Wireless Network Security: 802.11, Bluetooth, and Handheld Devices"
- NIST SP 800-50, "Building an Information Technology Security Awareness and Training Program"
- NIST SP 800-53, Revision 1 Final, "Recommended Security Controls for Federal Information Systems"
- NIST SP 800-53A, Draft, "Techniques and Procedures for Verifying the Effectiveness of Security Controls in Federal Information Systems"
- NIST SP 800-56A, "Recommendation on Key Establishment Schemes"
- NIST SP 800-57, "Recommendation on Key Management"
- NIST SP 800-60, "Guide for Mapping Types of Information and Information Systems to Security Categories"
- NIST SP 800-61, "Computer Security Incident Handling Guide"
- NIST SP 800-63, "Electronic Authentication Guideline: Recommendations of the National Institute of Standards and Technology"
- NIST SP 800-64, "Security Considerations in the Information System Development Life Cycle"
- NIST SP 800-65, "Integrating Security into the Capital Planning and Investment Control Process"
- NIST SP 800-66, "An Introductory Resource Guide for Implementation of the Health Insurance Portability and Accountability Act (HIPAA) Security Rule"
- NIST SP 800-88, "Guidelines for Media Sanitization"

# Appendix E – Section 508 Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix describes the approach used by the NUMI team to ensure that the NUMI application is in compliance with 508 requirements to provide visually impaired users of Web pages with access equivalent to that of users of the UI. The paragraphs that are quoted in this appendix come from Electronic and Information Technology Accessibility Standards Final Rule (Federal Register 21 December 2000, 36 CFR Part 1194).

Paragraph (a)

"*A text equivalent for every non-text element shall be provided (e.g., via "alt" "longdesc" or in element content).*"

This requirement is met in NUMI mostly through the design of the framework used by individual pages. Alternate text was added to all graphical buttons, identifying the object, its state (e.g., whether disabled or not), and what it does, in a clear and concise manner. Images that serve as graphic elements or placeholders that do not convey any meaning do not need to be given alternate text. However, testing programs that look for Section 508 compliance may flag such images as problems when they are not.

Paragraph (b)

"*Equivalent alternative for any multimedia presentation shall be synchronized with the presentation.*" No multimedia presentations shall be used.

Paragraph (c)

"*Web pages shall be designed so that all information conveyed with color is also available without color, for example form context or markup.*"

The tabs at the top of each page and the buttons on each page convey information using the color they take on. For instance, the current tab may be highlighted in blue and a button that is disabled may appear gray.

In order to be compliant with this paragraph, text was added to explain the state of a button. In the case of a tab, the alternate text for the tab would say, "Currently in the X section" or alternate text for a button might identify its state.

Paragraph (d)

"*Documents shall be organized so they are readable without requiring an associated style sheet."*

Style sheets are used to display the text in a particular style, color and font size. This can present a problem if the style sheet does not allow the user to increase or decrease the font size. Using relative measurements allows the fonts to change based on the user's preferences.

Paragraph (e) "*Redundant text links shall be provided for each active region of a server side image map.*"

Server side image maps shall not be used.

Paragraph (f)

"*Client-side image maps shall be provided instead of server-side image maps except where the regions cannot be defined with an available geometric shap*e."

Client side image maps shall not be used.

Paragraph (g)

"*Row and column headers shall be identified for data tables.*"

The application uses tables for both page formatting and data presentation. For the tables that present data, row and column headers are clearly identified for screen reader accessibility.

Paragraph (h)

"*Markup shall be used to associate data cells and header cells for data tables that have two or more logical levels of row or column headers.*"

Text is provided to distinguish between data and header cell contents, and to associate content with the appropriate headers.

Paragraph (i)

"*Frames shall be titled with text that facilitates frame identification and navigation.*" Frames technology shall not be used.

Paragraph (j)

"*Pages shall be designed to avoid causing the screen to flicker with frequency greater than 2 Hz and lower than 55 Hz.*"

Screen flicker is kept to a minimum and falls within the accepted range.

Paragraph (k)

"*A text-only page, with equivalent information or functionality, shall be provided to make a Web site comply with the provisions of this part, when compliance cannot be accomplished in any other way. The content of the text-only page shall be updated whenever the primary page changes.*"

NUMI has been made compliant on all pages with the exception of the COTS product CERME, held within it's own iFrame. This is a Change Healthcare product and when the vendor implements accessibility options we will ensure they're provided to users of NUMI.

Paragraph (l)

"*When pages utilize scripting languages to display content, or to create interface elements the information provided by the script shall be identified with functional text that can be read by assistive technology.*"

The site uses scripting extensively for form validation and navigation. Most of this scripting does not write content to the browser and does not affect content. However, several issues remain: The margin text that runs in the left panel of the page uses a script to update the content of that area depending on what field the user's cursor is currently in. This updated information is not available to a user of an assistive technology. To address this problem, NUMI displays the margin text for the user in a dialog box if the user presses a keyboard shortcut.

Another issue associated with scripting and accessibility concerns the way buttons work. The user takes an action by clicking on a button, which in turn triggers a script to run and execute a particular action. If the user cannot use the mouse to click on the button, the action cannot take place. To address this problem, buttons are programmed to trigger actions if the user hits a key on the keyboard while focus is on a button.

Paragraph (m)

"*When a Web page requires that an applet, plug-in or other application be present on the client system to interpret page content, the page must provide a link to a plug-in or applet that complies with §1194.21(a) through (l)."*

The site does not require any applet or plug-in to display site content.

Paragraph (n)

"*When electronic forms are designed to be completed on-line, the form shall allow people using assistive technology to access the information, field elements, and functionality required for completion and submission of the form, including all direction and cues."*

All form fields identify their content to the screen reader. In addition, the forms are designed in such a way as to maximize usability in terms of direct access to information, field elements, and functionality (equivalent to that of the graphical view), including directions, context-sensitive help, etc.

Paragraph (o)

"*A method shall be provided that permits users to skip repetitive navigation links."*

NUMI navigational links appear at the page top and bottom. To address this issue, links were added to the top of the page taking the user to the main areas within the page. One link goes to the main content. Another links to the navigational elements.

In addition to the accessibility links, the text only view of the site reorganizes the content of the page. Repetitive links and content fall to the bottom of the screen, while the main content of the page remains near the top. Also keyboard shortcuts were added to make jumping between sections of the page easier.

Paragraph (p)

"*When a timed response is required, the user shall be alerted and given sufficient time to indicate more time is required."*

The site does not have a timed response per prompt. However, in compliance with security requirements, the site has a timeout so that if the user does not take an appropriate action in the form within a given amount of time the session is terminated. The site gives warnings that this is going to take place, which gives a user ample opportunity to take the appropriate action to keep the session from timing out. The users cannot change the time set for the timeout, as this is determined by VHA security policy. However, by acting on the timeout warnings, the user can extend/reset the 20-minute timeout period.

#### Assistive Technology

There are many products available to assist persons with disabilities, such as speech or refreshable Braille screen readers, programs that can enlarge portions of the screen, or hardware alternatives to keyboards and mice. It is beyond the scope of this document to reference all the different assistive technologies that are available and how NUMI would work with each. Below are the major categories of assistive devices and what shall be done in NUMI to support each.

Screen readers: Alternate text shall be given to all visual information, including graphical buttons and form controls.

Screen magnification and text enlargement: The graphical view shall be resizable to accommodate different screen sizes and resolutions.

Alternative input devices: All elements were designed to allow manipulation without the need for a pointing device. In addition keyboard shortcuts shall be provided to make navigation inside a page easier. Assuming the assistive technologies are following industry standards, NUMI shall work with assistive technologies.

#### Testing for 508 Compliance

Testing for compliance to 508 guidelines can be challenging, especially on a site as complex as NUMI. Often automated tools are used to make the job easier. For a standard website this would be a straightforward process; the tool would be run and it would list any possible compliance issues. Any issues found would then be verified by a manual test. Automated tools are often ineffective on sites with a high level of user interactivity. Because NUMI is an application that interacts with the user to such a high degree, automated tools are rendered incapable of properly testing the application. That is why testing of NUMI shall be carried out manually, using actual assistive technologies or some of the techniques described below.

The simplest test for accessibility shall be to attempt to use the application using only the keyboard. The tab key moves the highlight from one element to the next allowing elements to be activated or data to be input. A tester shall verify if buttons can be activated and if form fields can be manipulated using only the keyboard.

Another test to see if page elements would be readable to assistive technology shall be to see if all graphical elements are giving meaningful alternate text. To do this the tester can hover the pointer over the element (image) and see if a tool tip appears. They shall verify that the text of the tool tip describes what the element is or does.

Another way to test the site shall be to use a screen reader to try to navigate and use the site. The tester shall verify that the information and auditory cues that are being conveyed by the screen reader provide sufficient information for the user to know what to do on any given page in the site.

# Appendix F – NUMI Development Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Appendix addresses tools used for the development of NUMI. <u>C# / .ASP.NET</u>

This language was chosen for development of NUMI by the Tier 3 development team, who did the initial field development.

MS Internet Information Server (IIS)

IIS is the application server that is required to publish .NET applications. IIS v.7.5 is being used for NUMI development and will be used for NUMI production.

MS.NET Framework 2.0

MS.NET is a software technology that is available with the MS operation system. It includes a library of pre-coded solutions to common programming problems and a virtual machine that manages the execution of programs written for this framework, and is used by a wide variety of Windows applications. The MS .NET framework and MS C# are being used in the development of the NUMI application. The NUMI GUI is being developed as ASPs, accessible to authorized users. The middle tier interacts with the VIA web services. The patient review information is stored in the NUMI database tools that are used to support the integration.

Log4Net

Apache Log4Net is a tool to help the programmer output log statements to a variety of output targets. It is the .NET version of Java's Log4J. Log4Net is a part of the Log4J framework to the .NET runtime. The framework has remained similar to the original Log4J, while taking advantage of new features in the .NET runtime.

Log4Net is used in NUMI to log programming error codes and system messages. Logging in the first release is not expected to be read by anyone other than the developers. More robust auditing is targeted for the next major release. In the meantime, in addition to various text log files, NUMI has a separate database that has tables to capture each synchronization event for each site, and a table that captures records that cannot be captured in the NUMI database due to bad data or other anomalies.

Rational Jazz Team Server

Rational Jazz Team Server (RTC) is the source version control system which is used to maintain current and historical versions of files such as source code, web pages, and documentation. RTC is used for the NUMI source code control.

Change Healthcare CERME

CERMe is the COTS product that has been integrated into NUMI to calculate utilization and runs on a Jetty web server.

Visual Studio

This is the Integrated Development Environment (IDE) used to develop and test the NUMI application. Visual Studio is used to develop console and GUI applications along with Windows Forms applications, web sites, web applications, and web services in both native codes together with managed code for all platforms supported by .NET Framework.

# Appendix G– NUMI Workflow Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error! Not a valid bookmark self-reference. and Error! Not a valid bookmark self-reference. describe an example NUMI workflow from a UM user's perspective.

![](numi-systems-management-guide-version-15-15/007.png)

<span id="_Toc169782000" class="anchor"></span>Figure : NUMI Workflow Example (part 1)

![](numi-systems-management-guide-version-15-15/008.png)

<span id="_Toc169782001" class="anchor"></span>Figure : NUMI Workflow Example (part 2)

# Appendix H – Free Text Search Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain database tables/columns are checked when a user performs a Free Text search in NUMI.

Table 53 lists tables and columns checked during search from UM Review Listing and Free Text Search pages:

| Table                      | Column                         |
|----------------------------|--------------------------------|
| FacilityTreatingSpecialty  | FacilityTreatingSpecialtyDesc  |
| MASMovementTransactionType | MASMovementTransactionTypeDesc |
| NumiUser                   | VISTAName                      |
| Physician                  | PhysicianName                  |
| WardLocation               | WardLocationDesc               |
| Patient                    | PatientName                    |
| Patient                    | SSN                            |
| PatientReview              | Comments                       |
| PatientReview              | Custom                         |
| PatientStay                | AdmissionDiagnosis             |

#### NUMI Free Text Search Functionality

Full-text queries perform linguistic searches against text data in full-text indexes by operating on words and phrases based on rules of a particular language. Full-text queries include simple words and phrases or multiple forms of a word or phrase from database. Users can perform a Free Text search in NUMI in 4 different ways:

Search by'*Exact'*word

In full-text search: A word is considered to be a token. A token is identified by appropriate word breakers, following the linguistic rules of the specified language. A valid phrase can consist of multiple words, with or without punctuation between them.

Search by'*Similar'*word

(Thesaurus): A thesaurus defines user-specified synonyms for terms. For example, if an entry, "{car, automobile, truck, van}", is added to a thesaurus, you can search for the thesaurus form of the word "car". All rows in the table queried that include the words "automobile", "truck", "van", or "car", appear in the result set because each of these words belong to the synonym expansion set containing the word "car".

Search by'*Partial'*word

(Part Of): A prefix term refers to a string that is affixed to the front of a word to produce a derivative word or an inflected form.

For a single prefix term, any word starting with the specified term will be part of the result set. For example, the term "auto" matches "automatic", "automobile" and so forth.

For a phrase, each word within the phrase is considered to be a prefix term. For example, the term "auto tran\*" matches "automatic transmission" and "automobile transducer", but it does not match "automatic motor transmission".

Search by'*Specific'* word

(Inflectional): The inflectional forms are the different tenses of a verb or the singular and plural forms of a noun. For example, search for the inflectional form of the word "drive". If various rows in the table include the words "drive", "drives", "drove", "driving" and "driven", all would be in the result set because each of these can be inflectionally generated from the word drive.

# Appendix I– NUMI Database Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NUMI database servers are all on Virtual Machines The servers all use Dynamic Host Configuration Protocol. Instead of connecting to them via Internet Protocol addresses, they must be connected to via their Domain Name System names instead. Users who have an account in the Administrators group can access these servers.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: NUMI Systems Management Guide Version 15.10

### Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Reports Menu is available to all NUMI users. The Reports Menu contains a link to the NUMI Enhanced Reports SharePoint site: <span class="mark">REDACTED</span>

### From: NUMI Systems Management Guide Version 15.9

## NUMI User Interface (UI) Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NUMI UI is developed as Active Server Pages (ASP).net pages. Known officially as "web forms"(files with the extension ASPX); the ASP.net pages are the main building block for application development. These Web forms contain static (X) HTML markup, as well as markup defining server-side Web Controls and User Controls where the developers place all the required static and dynamic content for the web page. The NUMI web forms interact with the VIA service through the Controller layer. Table 3 describes the major web forms developed for the NUMI application.

<table>
<caption><p><span id="Table_4:_Authorized_NUMI_Database_Users" class="anchor"></span>Table 4: Authorized NUMI Database Users</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AdminQuery.aspx</td>
<td>NUMI administrators can query the NUMI database through the interface on this page.</td>
</tr>
<tr class="even">
<td>AdminSites.aspx</td>
<td>Site Admin page. This page allows authorized users to add VistA users to Primary Reviewer, Physician Reviewer, Site Administrator, Report Only panels, and remove them from the panels.</td>
</tr>
<tr class="odd">
<td>Authenticated/Default.aspx</td>
<td>Select NUMI configuration values can be updated by NUMI administrators on this page.</td>
</tr>
<tr class="even">
<td>CERME.aspx</td>
<td>CERMe page. This is the NUMI page that facilitates access to Change Healthcare's CERMe InterQual® criteria.</td>
</tr>
<tr class="odd">
<td>DeceasedWarning.aspx</td>
<td>NUMI splash screen. This page displays a warning prior to displaying a deceased patient's record.</td>
</tr>
<tr class="even">
<td>DismissalAdmin.aspx</td>
<td>Site administrators can configure treating specialties as Reviewable or Not Reviewable.</td>
</tr>
<tr class="odd">
<td>History.aspx</td>
<td>NUMI History Page. This page allows an authorized user to view the patient stay history. The user can review current or previous stays by selecting items from Movement and Review tables.</td>
</tr>
<tr class="even">
<td>Home.aspx/Default.aspx</td>
<td>Select VISN, then Site (NUMI home. This page enables an authorized user to login to NUMI.</td>
</tr>
<tr class="odd">
<td>Login.aspx</td>
<td>This is an intermediate page that handles authentication headers passed in by the Identity and Access Management (IAM) Single Sign On (SSO) login page. This page immediately redirects to Default.aspx after the headers are read and a forms authentication ticket has been created.</td>
</tr>
<tr class="even">
<td>Logout.aspx</td>
<td>NUMI Logout page. his page is accessed from the Tools menu and is where users will logout of NUMI.</td>
</tr>
<tr class="odd">
<td>NumiUserEdit.aspx</td>
<td>NUMI New User/Privileges page. This page includes functionality for editing user privileges and is accessed from the Admin menu. The page allows authorized users to add and edit NUMI users, and deactivate user site access.</td>
</tr>
<tr class="even">
<td>NumiUserList.aspx</td>
<td>NUMI User List page. This page is accessed from the Admin menu and allows authorized users to retrieve a list of NUMI users by VistA, or by site.</td>
</tr>
<tr class="odd">
<td>PAReview.aspx</td>
<td>NUMI Physician Reviewer Review page. This page allows a Physician Reviewer to perform a patient review.</td>
</tr>
<tr class="even">
<td>PatientDetails.aspx</td>
<td>Report #7 - Patient Details Report. This report is accessed from the Reports menu and allows users to see all reviews saved for a specific patient for a selected time period.</td>
</tr>
<tr class="odd">
<td>PatientLevelMetNotMet.aspx</td>
<td>Report #5 - Patient Level Met/Not Met Report. This report is accessed from the Reports menu and allows users to see a basic patient level report.</td>
</tr>
<tr class="even">
<td>PatientLevelMetNotMetCustom.aspx</td>
<td>Report #6 – Patient Level Met/Not Met Custom Report. This report shows the same information that Report #5 does, except it includes information that was typed into the Custom field on the Primary Review screen.</td>
</tr>
<tr class="odd">
<td>PatientSelection.aspx</td>
<td>NUMI Patient Selection/Worklist Page. This page is accessed from the Tools menu and allows an authorized user to select a patient based on patient selection methods, and other criteria.</td>
</tr>
<tr class="even">
<td>PatientSelectionDismissed.aspx</td>
<td>NUMI Dismissed Patient Stays page This page is accessed from the Tools menu and allows users to see the list of patient stays dismissed from an earlier review.</td>
</tr>
<tr class="odd">
<td>PatientSelectionSearch.aspx</td>
<td>Free Text Patient Search page. This page is accessed from the Tools menu and allows users to search for patients using various filters and text entry options.</td>
</tr>
<tr class="even">
<td>PatientStayAdmin.aspx</td>
<td>Patient Stay Administration page. This page is accessed from the Tools menu and allows users to search for stays that are on NUMI but have been removed from VistA.</td>
</tr>
<tr class="odd">
<td>PatientWorksheet.aspx</td>
<td>Patient Worksheet page. This page displays after a button is selected on the History page. Users can print a hardcopy out and take it with them on rounds.</td>
</tr>
<tr class="even">
<td>PhysicianAdvisor.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="odd">
<td>PhysicianUMAdvisorResponse.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="even">
<td>PortraitReport.aspx</td>
<td>After reports have been generated and a print preview button is selected, the output will display in a PortraitReport.aspx window.</td>
</tr>
<tr class="odd">
<td>PrimaryReview.aspx</td>
<td>NUMI Primary Review page. This page allows users to perform a primary review (and indicate whether a Physician Reviewer review is required if criteria is not met).</td>
</tr>
<tr class="even">
<td>ReasonsCSReviews.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="odd">
<td>ReasonsforAdmReviews.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="even">
<td>Review.aspx</td>
<td>Review Summary page. This page allows users to look at Primary Review, Physician Reviewer summary information for patients, as well as view only CERMe Review text.</td>
</tr>
<tr class="odd">
<td>ReviewSelection.aspx</td>
<td><p>NUMI Patient Reviews page. This page is accessed from the Tools menu and allows users to work with reviews that have been saved for later review or locked to the database.</p>
<p>Authorized users can unlock primary review and physician reviewer reviews and delete reviews from this page.</p></td>
</tr>
<tr class="even">
<td>SensitiveWarning.aspx</td>
<td>NUMI splash screen. This page displays a warning prior to displaying a restricted patient's record. This ensures that users are aware prior to retrieving a Sensitive record and that the record is protected by the Privacy Act of 1974.</td>
</tr>
<tr class="odd">
<td>ServerReconnect.aspx</td>
<td>Blank web page used by JavaScript to re-establish connection between the client side and server side; this keeps the user logged in after screen mouse movements, clicks, and key presses.</td>
</tr>
<tr class="even">
<td>ServerRecycled.aspx</td>
<td>This page displays a message to inform the user that their web session has terminated unexpectedly. This is different than a timeout due to idleness.</td>
</tr>
<tr class="odd">
<td>SummaryMetNotMet.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="even">
<td>SummaryRLOCReason.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="odd">
<td>SyncOnDemand.aspx</td>
<td>NUMI Sync on Demand page. This page is accessed from the Tools menu and allows an authorized user to synchronize the patient stays with the information in VistA.</td>
</tr>
<tr class="even">
<td>TimeOut.aspx</td>
<td>This page displays a message to the user informing them that they were automatically logged out from the system due to idleness.</td>
</tr>
<tr class="odd">
<td>Unscheduled30DayReadmit.aspx</td>
<td>Decommissioned page in NUMI 14.4. Replaced by external NUMI Enhanced reports. https://vaww.rtp.portal.va.gov/OQSV/10A4B/NUMI/enhanced/SitePages/Home.aspx</td>
</tr>
<tr class="even">
<td>Welcome.aspx</td>
<td>This page will be used in future versions of NUMI; currently it will simply redirect the user to their home page.</td>
</tr>
</tbody>
</table>

<span id="Table_4:_Authorized_NUMI_Database_Users" class="anchor"></span>Table 4: Authorized NUMI Database Users
