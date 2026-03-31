---
title: Blind Rehab Version 5.1 Technical Manual/ Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: ANRV
app_name: Blind Rehabilitation
section: CLI
app_status: archive
pkg_ns: ANRV
patch_ver: 5.1
patch_id: ANRV*5.1
group_key: "ANRV:ANRV:5.1"
file_numbers: 
  - 2
security_keys: []
menu_options: 4
description: 
audience: 
keywords: 
  - table
  - contents
  - blind
  - patient
  - rehabilitation
  - security
  - application
  - vista
  - version
  - class
page_count: 0
word_count: 8824
section_count: 41
table_count: 14
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Blind_Rehabilitation_Archive/br_5_1_technical_manual_security_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Blind_Rehabilitation_Archive/br_5_1_technical_manual_security_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=333"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Blind Rehabilitation (ANRV)

  Technical Manual/Security Guide (TMSG)
---

![](blind-rehab-version-5-1-technical-manual-security-guide/001.png)

Aug 2022

ANRV\*5.1\*1

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

<table>
<caption>Revision History showing date artifact was created or revised, version number, description, and author.</caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 52%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Date</strong></em></th>
<th><em><strong>Description</strong></em></th>
<th><em><strong>Author</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/26/2005</td>
<td>Draft I</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/15/2006</td>
<td>Draft II</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>04/20/2006</td>
<td>Draft III</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>05/25/2006</td>
<td>EVS Requested Revisions</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>11/13/2006</td>
<td>Updates for version 5.0.27.5</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>12/06/2006</td>
<td>Updates for version 5.0.27.6</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>03/07/2007</td>
<td><p>The following changes have occurred since the 5.0.26.8 version of this document:</p>
<p><strong>Page 4</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Blind Rehabilitation from 5.0.26.8 to 5.0.27.6</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of VistALink from 1.5.0.026 to 1.5.1.002</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Person Service Lookup from 4.0.4.3 to 4.0.4.4</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Standard Data Service API from 7.0 to 10.0</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Standard Data Service Database from 9.9 to 10.0</p>
</blockquote></li>
</ul>
<p><strong>Page 16</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Blind Rehabilitation from 5.0.26.8 to 5.0.27.6</p>
</blockquote></li>
</ul>
<p><strong>Page 17</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Person Service Lookup from 4.0.4.3 to 4.0.4.4</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Standard Data Services from 7.0 to 10.0 in two places</p>
</blockquote></li>
<li><blockquote>
<p>Removed vljConnector-1.5.0.026.jar, vljFoundationsLib-1.5.0.026.jar and vljSecurity-1.5.0.026.jar libraries</p>
</blockquote></li>
</ul>
<p><strong>Page 24</strong>:</p>
<ul>
<li><blockquote>
<p>Changed the description for the Crystal Enterprise v10 application to read "...publish and execute developed reports." instead of "...publish and test developed reports."</p>
</blockquote></li>
</ul>
<p><strong>Page 26</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Standard Data Service API from 7.0 to 10.0</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Standard Data Service Database from 9.9 to 10.0</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Person Service Lookup from 4.0.4.3 to 4.0.4.4</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/23/2010</td>
<td><p>The following changes have occurred for the version 5.0.29.4</p>
<p><strong>Page 4</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Blind Rehabilitation from 5.0.27.6 to 5.0.29.4</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of VistALink from 1.5.0.026 to 1.5.2.004</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Kaajee 1.0.0.019 to 1.0.1.003</p>
</blockquote></li>
<li><blockquote>
<p>Changed version number of Standard Data Service Database from 10.0 to 18.0</p>
</blockquote></li>
</ul>
<p><strong>Page 16</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Blind Rehabilitation from 5.0.27.6 to 5.0.29.4</p>
</blockquote></li>
</ul>
<p><strong>Page 17</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Standard Data Services Jars from 10.0 to 18.0 in two places</p>
</blockquote></li>
</ul>
<p><strong>Page 26</strong>:</p>
<ul>
<li><blockquote>
<p>Changed version number of Standard Data Service Database from 10.0 to 18.0</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>8/17/2022</td>
<td><p>Updated the table of contents with reference numbers.</p>
<p>Removed KAAJEE from the document</p>
<p>Updeated Version from 5.0 to 5.1</p>
<p>Replaced Struts with JSF throughout document</p>
<p>Updated Section 1 Introduction with updated specifics for the latest release</p>
<p>Updated Section 1.1 Enhanced technology with updated specifics for the latest release</p>
<p>Updated Section 1.3 VistA software requirements to remove requirements no longer required</p>
<p>Updated Section 1.4 and removed KAAJEE that is no longer used</p>
<p>Updated Section 2.2 Document names</p>
<p>Updated Section3 Implementation and Maintenance to match the 5.1 process</p>
<p>Updated Section 3.1 Server deployment graphic</p>
<p>Updated Section 10 Builds with builds used in 5.1</p>
<p>Updated Section 13 Updated Product security</p>
<p>Updated Section 15 with new software versions, file names, and jar file names</p>
<p>Removed Section 15.6 EJB Archive file as it longer is relevant with newest version.</p>
<p>Section 15.7, removed two paragraphs as they are no longer relevant</p>
<p>Updated Section 15.8 with new infor related to 5.1</p>
<p>Removed 15.9 Exceptions as they are no longer relevant with version 5.1</p>
<p>Removed 15.10 Service imports as they are no longer relevant with Version 5.1</p>
<p>Updated section 16.1 Development Platform applications and versions</p>
<p>Updated Section 16.2.1 ANT to Maven</p>
<p>Removed Section 16.2.3 Chainsaw as it is no longer used</p>
<p>Removed Section 16.3.3 KAAJEE</p>
<p>Updated Section 17.4 Data Validation with current 5.1 details</p>
<p>Updated Section 17.8 Site Parameters</p>
<p>Removed 19 Data Conversion as it is not part of 5.1</p>
<p>Due to the shift of the cloud the sequence diagrams no longer apply and were removed.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Revision History showing date artifact was created or revised, version number, description, and author.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Benfits](#benfits)
  - [Enhanced Technology](#enhanced-technology)
  - [VistA Software Requirements](#vista-software-requirements)
  - [HealtheVet-VistA Software Requirements](#healthevet-vista-software-requirements)
- [Orientation](#orientation)
  - [Recommended Users](#recommended-users)
  - [Documentation and Maintenance](#documentation-and-maintenance)
  - [VistA intranet](#vista-intranet)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [BR Production Centralized Server Deployment](#br-production-centralized-server-deployment)
  - [BR Sample Configuration](#br-sample-configuration)
- [VistA Files](#vista-files)
- [Routines](#routines)
- [Security Keys](#security-keys)
- [Exported VistA Options](#exported-vista-options)
- [Parameter Definition](#parameter-definition)
- [Remote Procedure](#remote-procedure)
- [Required Builds](#required-builds)
- [External Interfaces](#external-interfaces)
- [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
- [Software Product Security](#software-product-security)
- [Security Management](#security-management)
  - [Strategic Initiatives Overview](#strategic-initiatives-overview)
  - [Application Security](#application-security)
  - [Audit Trail](#audit-trail)
  - [Remote Systems](#remote-systems)
  - [Archiving Purging](#archiving-purging)
  - [Contingency Planning](#contingency-planning)
  - [Eletronic Signatures](#eletronic-signatures)
  - [Security Keys](#security-keys-1)
  - [File Security](#file-security)
  - [Reference](#reference)
  - [Official Policies](#official-policies)
- [Blind Rehabilitation Application](#blind-rehabilitation-application)
  - [Enterprise Archive](#enterprise-archive)
    - [Application xml](#application-xml)
    - [Weblogic-Application xml](#weblogic-application-xml)
    - [APP-INF Directory](#app-inf-directory)
  - [Web Archive File](#web-archive-file)
    - [Directory Contents](#directory-contents)
  - [Web Archive Web.xml File](#web-archive-webxml-file)
  - [Web Archive Weblogic.xml File](#web-archive-weblogicxml-file)
  - [JSF Config File](#jsf-config-file)
  - [Application Property Files](#application-property-files)
  - [Other Configuration Files](#other-configuration-files)
- [Java Enterprise Developer Workstation](#java-enterprise-developer-workstation)
  - [Development Platform](#development-platform)
  - [Development Tools](#development-tools)
    - [Maven](#maven)
    - [Log4j](#log4j)
    - [Libraries](#libraries)
  - [HealtheVet Services](#healthevet-services)
    - [SDS](#sds)
    - [VLJ](#vlj)
    - [KAAJEE](#kaajee)
    - [PSL](#psl)
    - [PSC (Formerly PSD)](#psc-formerly-psd)
- [Business Rule Implementation](#business-rule-implementation)
  - [Web Security](#web-security)
  - [Data Validation- View Layer](#data-validation-view-layer)
  - [Data Validation- Control Layer](#data-validation-control-layer)
  - [Data Validation- Business Layer](#data-validation-business-layer)
  - [Data Validation- Model Layer](#data-validation-model-layer)
  - [Transactions](#transactions)
  - [Notifications](#notifications)
  - [Concurrency](#concurrency)
  - [Overnight Processing](#overnight-processing)
  - [MPI Interaction](#mpi-interaction)
- [Glossary/Acronym List](#glossaryacronym-list)
- [Operations and Maintenance Responsibilities](#operations-and-maintenance-responsibilities)
- [Approval Signatures](#approval-signatures)
The Blind Rehabilitation Services (BRS) application coordinates a healthcare service delivery system that provides a continuum of care for blind and visually impaired veterans served by the VA, extending from their home environment to the local VA facility and to the appropriate rehabilitation setting. These services include adjustment to blindness counseling, patient and family education, benefits analysis, comprehensive residential inpatient training, outpatient rehabilitation services, the provision of assistive technology, and research that assists the veteran in acquiring the skills and capabilities necessary for development of personal independence and emotional stability. BRS serves as a registry that collects demographic and clinical data by providing enhanced tracking and reporting by:
- Visual Impairment Service Teams (VIST) Coordinators
- Blind Rehabilitation Centers (BRCs)
- Blind Rehabilitation Outpatient Specialists (BROS)
- Visual Impairment Services Outpatient Rehabilitation (VISOR) Programs
- Visual Impairment Center to Optimize Remaining Sight (VICTORS)
BRS creates, modifies, and tracks referrals in an electronic referral process to track patient applications for service, notifications feature to alert users of pending referrals, encounters/progress notes will be automatically created for assessments and field visits, nationwide centralization of BRS services data to allow nationwide reporting, ad-hoc reporting capabilities, allows the ability to track BRS patient care access across institutions, and patients can be referred or transferred to other institutions if they move without having to recreate patient data.
The Blind Rehabilitation Technical Manual/Security Guide gives a technical description of the application and the security features. The intended audience of this guide is IRM, EMC, EVS, SQA, and developers supporting the Blind Rehabilitation product.

## Benfits

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Complies with Health*<u>e</u>*Vet-VistA Architecture
- Complies with 508 regulations, using W3C standards
- Accessible web based application, via a web browser
- Supports the OI Single Sign-on initiative
- User authentication via role based permissions
- User friendly
- Seamless continuum of care
- Minimum user disruption
- Simplified data entry
- Better identification and treatment of veterans
- Consolidates data
- Enables system driven waiting times and waiting list tracking and reporting capabilities
- Enables users to receive comprehensive views of a patient’s BR Services across institutions
- Facilitates data tracking and auditing capabilities
- Improves accountability
- Enhanced reporting features
- Provides Data Standardization which improves and provides consolidated data reporting
- Improved blind services tracking
- Enables Research and Provides Outcomes tracking and reporting capabilities
- Improves VHA organizational communication
- Transmits to the Health Data Repository

## Enhanced Technology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A single consolidated database on the AWS cloud will replace the AITC server based design.
- Fulfills the congressional mandate on waiting times and waiting list calculations
- Electronic referral process to track patient applications for service
- Notifications feature to alert users of pending referrals
- Encounters/Progress Notes will be automatically created for assessments and field visits (PCE interface) in a future version.
- Nationwide centralization of Blind Rehabilitation services data to allow nationwide reporting
- Ad-hoc reporting capabilities with Jasper reports will replace Crystal reporting
- Secure Web Access (128 Bit SSL) from any authorized VA workstation
- Improved technology using web browser access and improved data security, via the VHA intranet
- Uses modern system architecture which allows for faster system enhancements
- Enhancements will be rolled out to all users at the same time ensuring consistent data
- Allows ability to track BR patient care access across institutions
- Patients can be referred or transferred to other institutions if they move without having to recreate patient data
- Patient lookup using the Health*<u>e</u>*Vet Person Lookup Service (PSL) and Person Service Demographics (PSC)
- Standardized lookup tables using the Health*<u>e</u>*Vet Standard Data Service (SDS)
- Improved data integrity
- Minimize the maintenance and support required by IT support staff

## VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before the installation of Blind Rehabilitation V5.0, the following packages must be installed and fully patched.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 18%" />
<col style="width: 26%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Software</th>
<th>Version</th>
<th>Required Patches</th>
<th>Health<u>e</u>Vet Dependency</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td>V. 8</td>
<td><p>XU*8*238</p>
<p>XU*8*265</p>
<p>XU*8*284</p>
<p>XU*8*309</p>
<p>XU*8*337</p>
<p>XU*8*361</p>
<p>XU*8*343</p></td>
<td><p>XU*8*325 (Person Service Lookup Dependency)</p>
<p>)</p></td>
</tr>
<tr class="even">
<td>Kernel Toolkit</td>
<td>V. 7.3</td>
<td><p>XT*7.3*89</p>
<p>XT*7.3*67</p></td>
<td></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>V. 22</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VistALink</td>
<td>V. 1.5.2.004</td>
<td></td>
<td>XOBU*1.5</td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td>V. 1.1</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>TIU</td>
<td>V. 1.0</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>OERR</td>
<td>V. 3.0</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Registration</td>
<td>V. 5.3</td>
<td><p>DG*5.3*615</p>
<p>DG*5.3*620</p></td>
<td><p>DG*5.3*538 (Person Service Lookup)</p>
<p>DG*5.3*557 (Patient Services)</p></td>
</tr>
</tbody>
</table>

## HealtheVet-VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the installation of Blind Rehabilitation 5.1, the following java packages are used. These components are supplied with the Blind Rehab software distribution zip file and are installed at the Centralized application server.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Software</strong></em></th>
<th><em><strong>Version</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VistALink</td>
<td>V 1.5.2.004</td>
</tr>
<tr class="even">
<td>Person Service Construct (formerly Person Service Demographics. Referred to as PSC or PSD)</td>
<td>V. 2.0.0.7</td>
</tr>
<tr class="odd">
<td>Standard Data Service</td>
<td><p>API V 18.0</p>
<p>Database V 18.0</p></td>
</tr>
</tbody>
</table>

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Recommended Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience for the Blind Rehabilitation 5.1 Technical and Security Guide includes:

Information Resource Management (IRM)

Enterprise VistA Support (EVS)

Health Systems Implementation, Training and Enterprise Support (HSITES)

Enterprise Management Center Office (EMC)

## Documentation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation V. 5.1 VistA Installation/Implementation Guide

Blind Rehabilitation V. 5.1 Centralized Server Installation/Implementation Guide

Blind Rehabilitation V. 5.1 Release Notes

Blind Rehabilitation V. 5.1 User Manual

Online Help is available from within the application

|                  |                                               |                  |
|------------------|-----------------------------------------------|------------------|
| File Name        | Description                                   | Retrieval Format |
| ANRV5_1_1CIG.PDF | Centralized Installation/Implementation Guide | Binary           |
| ANRV5_1_1VIG.PDF | VistA Installation/Implementation Guide       | Binary           |
| ANRV5_1_1RN.PDF  | Release Notes                                 | Binary           |
| ANRV5_1_1TM.PDF  | Technical/Security Manual                     | Binary           |
| ANRV5_1UM.PDF    | User Manual                                   | Binary           |

## VistA intranet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for this product is available on the intranet at the following address:

<https://www.va.gov/vdl/>.

This address takes you to the VistA Documentation Library (VDL), which has a listing of all the clinical software manuals <span class="mark">REDACTED</span>

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the *Blind Rehabilitation v. 5.1 Installation/Implementation Guides* for additional information about installing and implementing the software.

Implementation is comprised of a centralized application on the AWS cloud:

<span class="mark">REDACTED</span>

Interfaced to all field VistA servers via VistALink connections.

Information accessed through VistA Link RPCs

Installation of Blind Rehab KIDS build at each VistA site

User setup on local VistA and central Blind Rehab application

> NOTE: Virtual server recovery includes recovery of the Operating System, Database (if applicable), application and all relevant files.

1)  System Recovery

> The following subsections define the process and procedures necessary to restore the system to a fully operational state after a service interruption. Each of the subsections starts at a specific system state and ends up with a fully operational system.

2)  Restart after non-scheduled system interruption
    1.  Verify the database servers are started and the database is running
    2.  Verify web server is started, and Apached Web Server is running
    3.  Verify application server is started; start WebLogic Administrative server per documentation and then log into the admin console to start the managed servers.
3)  Restart after database restore is done by the Systems Oparations Group
4)  Back out Procedures

> The Deployment, Installation, Back-out, and Rollback Plan for this product can be found in Rational project area documentation stream as required by VIP a copy can be requested if the requestor does not have access to the Rational Project area.

5)  Roleback procedures

> The Deployment, Installation, Back-out, and Rollback Plan for this product can be found in Rational project area documentation stream as required by VIP a copy can be requested if the requestor does not have access to the Rational Project area.

## BR Production Centralized Server Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](blind-rehab-version-5-1-technical-manual-security-guide/002.png)

## BR Sample Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](blind-rehab-version-5-1-technical-manual-security-guide/003.png)

# VistA Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no files added to VistA with this software.

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are included in the Blind Rehabilitation software:

| Routine | Description                                                               |
|---------|---------------------------------------------------------------------------|
| ANRVJ1  | VistA routine used for interfacing to VistA until services are available. |
| ANRVP   | Post installation routine                                                 |

# Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA file 200 Security Keys are included in the Blind Rehabilitation software:

| Routine       | Description                                                                                                                                                                                                                            |
|---------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ANRVUSERROLE  | This key is used for Authorization in combination with the option to allow a user access to the Blind Rehabilitation software. All users of the system must have at minimum the ANRVUSERROLE security key and ANRVJ_BLINDREHAB Option. |
| ANRVADMINROLE | Security key for Administrators of the system.                                                                                                                                                                                         |

# Exported VistA Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The option menus exported by Blind Rehabilitation are all located in the ANRV namespace. A number of options are deleted at the site and 1 new option is added to allow access to the Blind Rehabilitation software.

| Internal Entry Name            | Option Name                        | Action         | Description                                                                                          |
|--------------------------------|------------------------------------|----------------|------------------------------------------------------------------------------------------------------|
| ANRVJ_BLINDREHAB               | BLIND REHAB/VIST 5.1               | Send to Site   | Added to VistA this option allows access to the RPC’s at the local site for Blind Rehabilitation 5.1 |
| ANRV DELETE REFERRAL           | Delete VIST Referral Roster        | Delete At Site | Removed from VistA                                                                                   |
| ANRV DELETE ROSTER             | Delete VIST Patient Record         | Delete At Site | Removed from VistA                                                                                   |
| ANRV EDIT VIST OPTIONS         | Edit VIST Options Menu             | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT CHECKLIST      | Enter/Edit VIST Benefits Checklist | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT INACTIVE VIST  | Enter/Edit Inactive VIST Roster    | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT REFERRAL       | Enter/Edit VIST Referral Roster    | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT VARO CLAIMS    | Enter/Edit VARO Claims Roster      | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT VIST LETTER    | Edit VIST Letter                   | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT VIST PARAMETER | Enter/Edit VIST Parameter          | Delete At Site | Removed from VistA                                                                                   |
| ANRV ENTER/EDIT VIST PATIENT   | Enter/Edit VIST Patient Record     | Delete At Site | Removed from VistA                                                                                   |
| ANRV EYE DIAG NARRATIVE        | Eye Diagnosis Narrative            | Delete At Site | Removed from VistA                                                                                   |
| ANRV LETTER MENU               | VIST Letter Menu                   | Delete At Site | Removed from VistA                                                                                   |
| ANRV PATIENT REVIEW            | ANRV PATIENT REVIEW RPC’S          |                |                                                                                                      |

# Parameter Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Parameter Definition is included in the Blind Rehabilitation software:

| Parameter        | Description                                                                                                                                                                                                                                                                                                                                            |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ANRV GUI VERSION | This site parameter is installed in VISTA in the PARAMETERS file 8989.5 automatically by the ANRVJP post installation routine using KIDS. The parameter allows the Blind Rehabilitation application to check the VistA sites software version and will not allow users to log into the system if the remote system is not running the correct version. |

# Remote Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Remote Procedures are included in the Blind Rehabilitation software and are installed in the REMOTE PROCEDURE File (# 8994):

| Remote Procedure      | Description                                                      |
|-----------------------|------------------------------------------------------------------|
| ANRV CREATE ENCOUNTER | This RPC is for future use.                                      |
| ANRV GET PN TITLES    | This RPC is for future use.                                      |
| ANRV PROBLEM LIST     | This RPC gets a patients problem list to display in Blind Rehab. |
| ANRVJ1_RPC_MAIN       | This is the main RPC entry point.                                |

# Required Builds

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VistA Builds must be installed or the ANRV\*5.1 KIDS will not load, during installation these are checked to ensure the VistA system is compatible with the Blind Rehab software.

| Build        | Description                                                                                                        |
|--------------|--------------------------------------------------------------------------------------------------------------------|
| DG\*5.3\*538 | Uniform API used by the Person Service Lookup component of Blind Rehabilitation.                                   |
| DG\*5.3\*557 | Uniform API used by the Person Service Demographics and Construct component of Blind Rehabilitation.               |
| XOBV 1.5     | Uniform API used by the VistALink component of Blind Rehabilitation this allows for communication to the VistA DB. |

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 23%" />
<col style="width: 31%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th>Screen</th>
<th>Data Elements</th>
<th>Interface Via</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Patient Lookup</td>
<td><p>ICN</p>
<p>PATIENT_NAME</p>
<p>PATIENT_ADDRESS</p>
<p>PATIENT_CITY</p>
<p>PATIENT_STATE</p>
<p>PATIENT_ZIP</p>
<p>PATIENT_HOME_PHONE</p>
<p>PATIENT_BIRTH_DATE</p></td>
<td>VistALink</td>
<td>Provides a uniform patient lookup using VA standards</td>
</tr>
<tr class="even">
<td>2</td>
<td>Enter Blind Rehab Staff</td>
<td><p>DFN</p>
<p>PERSON_NAME</p></td>
<td>VistALink</td>
<td>This uses an RPC to get user data from the VistA site and is used for adding users to the system</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Enter Blind Rehab Staff – Alternative 2</td>
<td><p>VPID (VA Person Id)</p>
<p>PERSON_NAME</p></td>
<td>Person Service</td>
<td><p>Covers access to Person Identifying data in the VistA 200File.</p>
<p>(Providers, Employees, IT Users</p></td>
</tr>
<tr class="even">
<td>3</td>
<td>Single Sign On</td>
<td><p>VPID/ICN</p>
<p>PERSON_NAME</p></td>
<td>SSO</td>
<td>Single Sign On provides a service to allow the user to sign in once</td>
</tr>
<tr class="odd">
<td>5</td>
<td>PCE Problem List</td>
<td><p>DFN</p>
<p>PROBLEM_LIST</p></td>
<td><p>Problem List</p>
<p>DBIA446</p></td>
<td>Used to display the patients Problems List</td>
</tr>
<tr class="even">
<td>6</td>
<td>Registration Screen</td>
<td>PRIMARY_ELIGIBILITY</td>
<td><p>Patient file (#2.361)</p>
<p>DBIA3789</p></td>
<td>From Registration, Patient file #2</td>
</tr>
</tbody>
</table>

.

# Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of approved DBIAs for Blind Rehabilitation.

| DGRR GUI PATIENT LOOKUP    | \#4686              |
|----------------------------|---------------------|
| DGRR PATIENT SERVICE QUERY | \#4686              |
| GET DFN^MPIF001            | \#2701              |
| DATA2PCE^PXAPI             | \#1889 (future use) |
| SELECTED^VSIT              | \#1905 (future use) |
| TIU SIGN RECORD            | \#1790 (future use) |
| TIU REQUIRES COSIGNATURE   | \#1800 (future use) |
| TIU CREATE RECORD          | \#1806 (future use) |
| TIU DELETE RECORD          | \#1811 (future use) |
| TIU GET PN TITLES          | \#1782 (future use) |
| FEE BASIS                  | \#2347 (future use) |
| ORQQPL LIST                | \#1642              |

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation implements Single Sign-on (SSO) based on established VHA and HSD&D requirements.. Users of the system can access Blind Rehabilitation by entering their current VistA Access and Verify Codes along with their institution. The users information is checked against the VistA system first by authenticating their access, verify code, and institution combination. Then they are authenticated by checking to ensure they have the appropriate Option Menu (ANRVJ_BLINDREHAB) and Security Key (ANRVUSERROLE) from VistA against the custom Weblogic security principle that uses both the principle and Oracle database entries to allow or disallow user access to the Blind Rehabilitation application. Additional authentication occurs inside the Blind Rehabilitation software to ensure the user has access to the VistA institution and to provide the user with a session containing the Blind Rehabilitation application menus assigned to that user within the application. Users with correct login credentials are allowed access to the application and can only access the menus that have been assigned to them.

Patient and user context management via CCOW was added to the application, however it is currently disabled due to accessibility (Section 508) issues created by the CCOW applet. CCOW will be re-enabled in a future release following the resolution of the introduced accessibility issues.

Secure socket layer (128Bit - SSL) encryption is used to protect data that is transmitted between the browser and the Web server.

The security layer is designed to insulate Blind Rehabilitation from requiring major changes as the underlying enterprise security system evolves. Blind Rehabilitation provides an abstraction in the form of Java interfaces, which allow for flexibility in the implementation.

Blind Rehabilitation provides the following:

Authentication – provided by wrapping the JAAS authentication mechanism, implementation for authentication must be provided by modules that provide the support

Authorization – provided by wrapping the JAAS authentication mechanism based on multiple principal subjects. Authorization is based on actions authorized by access control as defined by JAAS.

Audit – a function is provided by the supporting back end security system. Audit is not a front-end client based feature and is not defined in JAAS or the Security Module interfaces.

# Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data contained in and messaged to BR is compliant with all applicable organizational and legislative security and privacy policies (for example, Health Insurance Portability and Accountability Act (HIPAA), the Privacy Act of 1996); Veterans Health Administration’s Authentication, Authorization, Accountability (AAA) standards, guidance and procedures established by the VHA Health Information Security Office, and policy and guidance issued by the Department of Veterans Affairs Office of Cyber Security.

## Strategic Initiatives Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The securing of data by controlling and recording access to it is paramount. Efforts that are external to the BR Project are also underway to ensure the security of data. The following efforts, although external to the BR Project, will influence the provision of security for the project:

The VA and VHA have each developed enterprise architectures that call for the introduction of a Common Health Information Security Services (CHISS) function. In a common health information security services design, functions such as user authentication and high-level authorization are processed by a ‘common’ or shared application instead of the old model of performing those functions inside each application.

The Interim Security Services for Rehosted Applications (ISSRA) project will serve as a bridge between the current security model and the one that will be implemented as CHISS. ISSRA will provide the user authentication and authorization services; Blind Rehab will be a ‘customer’ of ISSRA and will work closely with that team to ensure that the security requirements are completely and accurately defined. The current ISSRA security component used in Blind Rehabilitation is SSO. At some future time, SSO will be replaced with an Enterprise level authentication/authorization component.

## Application Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Security risks to BR are mitigated by:
- Java Secure Coding Guidelines
- Single Sign-on (SSO)
- Role-based Access
- Audit Trail
- Network Security
- 128bit SSL (HTTPS) Access to Web Server
- BR Site Server Security
- Physical Security

## Audit Trail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An audit trail creates retrievable record of the users’ interactions with the system. The ability to trace users to edits of specific records creates an identification that can be accessed in the event of a security breach or system defect.

The audit trail starts when a user accesses, submits a new record, or updates an existing record. The user ID is captured from their login and is stored in the audit trail along. The stored record has supporting classes that can be called by the system for reporting information about user transactions.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This system connects to remote VistA systems throughout the organization. The data transmitted from a user’s desktop to the Blind Rehab web server is encrypted through 128bit SSL (HTTPS). Data transmitted from the application server to the remote VistA sites and to the MPI over the VA Intranet is not encrypted.

## Archiving Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Archiving and purging capabilities are not currently available and were not requested or required.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites utilizing Blind Rehabilitation 5.1 should develop a local contingency plan to use in the event of product problems in a live environment. The facility contingency plan must identify the procedure for maintaining functionality provided by this package in the event of system outage. Field station Information Security Officers (ISOs) may obtain assistance from their Regional Information Officer (RISO).

## Eletronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ANRVUSERROLE and ANRVADMINROLE are VistA security keys used by this product to enhance the “strong” security of SSO.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new VistA files are distributed with this product.

## Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Researchers have access to the Blind Rehabilitation application in accord with Patient Care Services Information Letter 11-2002-002 and the Federal Register Volume 66, Number 103, Pages 29209-29212.

## Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation 5.1 software release references no official policy unique to the product regarding the modification of software and distribution of the version.

# Blind Rehabilitation Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation is designed to run on a J2EE 8 compliant application server running on a 8u341 JVM.

## Enterprise Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BR deploys as a java enterprise archive named BR-EAR-*major.minor.revision.buildnumber*.ear containing the following elements. Example file name: BR_EAR_5.1.0.ear.

### Application xml

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file exists in the META-INF directory per the java enterprise 8.0 specifications. This file describes the modules of the EAR file, which BR-web.war

### Weblogic-Application xml

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file exists in the META-INF directory. This is a basic deployment descriptor for WebLogic applications. No special or proprietary settings are used in this deployment descriptor.

### APP-INF Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The APP-INF/lib directory contains external jar files needed for the BR enterprise application:

| *Library Name*           | *Description*                    |
|------------------------------|--------------------------------------|
| commons-beanutils.jar        | Apache-Jakarta Commons               |
| commons-collections.jar      | Apache-Jakarta Commons               |
| commons-digester.jar         | Apache-Jakarta Commons               |
| commons-fileupload.jar       | Apache-Jakarta Commons               |
| commons-httpclient-2.0.1.jar | Apache-Jakarta Commons               |
| commons-lang.jar             | Apache-Jakarta Commons               |
| commons-logging.jar          | Apache-Jakarta Commons               |
| commons-resources.jar        | Apache-Jakarta Commons               |
| commons-validator.jar        | Apache-Jakarta Commons               |
| hapi-0.4.3.jar               | Open source HL7 API (Sourceforge)    |
| itext-1.02b.jar              | Open source JAVA-PDF (Sourceforge)   |
| jakarta-oro.jar              | Apache-Jakarta ORO                   |
| jakarta-regexp-1.3.jar       | Apache-Jakarta Regular Expressions   |
| junit.jar                    | Open source Test Class (Sourceforge) |
| Jasper.jar                   | Jasper reports 619                   |
| log4j-2.17.2.jar             | Apache-Logging                       |
| vha-stddata-basic-18.0.jar   | VA Standard Data Service             |
| vha-stddata-client-18.0.jar  | VA Standard Data Service             |

## Web Archive File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BR enterprise archive contains the BR web archive, BR-web.war. The file contains a root directory, virtual directories, and the WEB-INF directory.

### Directory Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| *Directory Name*        | *Description*                                                                                                            |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|
| /                           | Root directory contains entry, home, layout, tile definition and other root level pages                                      |
| Admin                       | BR Administrative pages                                                                                                      |
| assessmentTrainingEncounter | BR Assessment and Training pages                                                                                             |
| benefitsChecklist           | BR Benefit Checklist pages                                                                                                   |
| Brstaff                     | BR Staff (User setup) pages                                                                                                  |
| clinicalAssessment          | BR Clinical Assessment Pages                                                                                                 |
| Common                      | BR Common pages and JavaScript files                                                                                         |
| Css                         | BR Stylesheet files                                                                                                          |
| educationInService          | BR Education and In-service pages                                                                                            |
| Encounters                  | BR Encounter pages                                                                                                           |
| eyeExam                     | BR Eye Exam pages                                                                                                            |
| help                        | BR Help pages and resources                                                                                                  |
| images                      | BR Web related images                                                                                                        |
| letters                     | BR Letter pages                                                                                                              |
| lib                         | Sentillion CCOW applet resources                                                                                             |
| menu                        | BR Menu pages                                                                                                                |
| patient                     | BR and PLU(PSL) patient related pages                                                                                        |
| plu                         | PLU related patient resources                                                                                                |
| referrals                   | BR Referral pages                                                                                                            |
| reports                     | BR Report criteria and Individual report response pages                                                                      |
| reviews                     | BR Reviews (Annual Outcome Survey and Pre-Post Review) pages                                                                 |
| stylesheets                 | PLU Stylesheet files                                                                                                         |
| test                        | BR Various development test pages                                                                                            |
| user                        | BR Login pages prior to integration (deprecated)                                                                             |
| varo                        | BR VARO Claim pages                                                                                                          |
| vista                       | BR Various development test pages for VistA functions                                                                        |
| vistAnnualReview            | BR VIST Annual Review pages                                                                                                  |
| vistFieldVisits             | BR VIST Visits pages                                                                                                         |
| waitlist                    | BR Waitlist Record search, list, and edit pages                                                                              |
| WEB-INF                     | Various deployment descriptor, tag library descriptor, tile definition descriptor, struts config, and other descriptor files |
| WEB-INF/classes             | BR Java Classes used by the Web module                                                                                       |

## Web Archive Web.xml File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BR Web module archive contains a file named web.xml. This file contains:

Context parameters

Servlets

Servlet mappings

Filters

Filter mappings

Security roles

Security constraints

SSO login configuration

Taglib declarations

Welcome files

Error pages

Listeners

## Web Archive Weblogic.xml File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Weblogic.xml contains the mapping of the logical Java enterprise role to the physical WebLogic security realm.

## JSF Config File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Weblogic.xml contains the mapping of the logical Java enterprise role to the physical WebLogic security realm.

## Application Property Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehab uses several property files to control its runtime behavior. The files are located on the file system in the /conf directory. These include:

<u>Application.properties</u> – the main property file containing settings for the application. Deployed on the file system.

<u>Log4j.properties</u> – property file used to control the logging behavior of the application. Deployed on the file system. Has default settings for log file appenders, file names, file rotation, logging format, and socket appenders.

## Other Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BR also depends on the following service dependency configuration files that need to be configured during deployment:

| Application.properties                   | SDS’s configuration file |
|------------------------------------------|--------------------------|
| PatientLookup.properties                 | a PSL configuration file |
| PersonLookupResources.properteis         | a PSL configuration file |
| XXX.va.XXX.vistalink.connectorConfig.xml | a VLJ configuration file |

Please review the Blind Rehab Centralized Installation manual and the respective Health*<u>e</u>*Vet Component documentation for more information on these configuration files.

# Java Enterprise Developer Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehab java enterprise developer workstations are dependent on remote and local services. All VA java service dependencies are generally deployed locally on the developer’s workstation to isolate development work from external problems.

## Development Platform

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following infrastructure was used to develop Blind Rehabilitation on Windows workstations:

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th><em><strong>Application</strong></em></th>
<th><em><strong>Description</strong></em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sun Java JDK 8</td>
<td>Java compiler. JAVA_HOME must be set to the base directory where this is installed.</td>
</tr>
<tr class="even">
<td>WebLogic Server 12.2.14</td>
<td>All developers need to setup local WebLogic servers on their workstations.</td>
</tr>
<tr class="odd">
<td>Eclipse</td>
<td>Eclipse latest versionAny suitable text editor may be used however.</td>
</tr>
<tr class="even">
<td>Edge/Chrome</td>
<td>Blind Rehab is a web application; therefore, developers are required to have VA supported versions of browsers installed.</td>
</tr>
<tr class="odd">
<td>Source Control Management</td>
<td><p>Github.BR Repository are</p>
<ul>
<li><p>Product: <a href="https://github.ec.XX.XXX/EPMO/vista-edis-gui-product">https://github.ec.XX.XXX/EPMO/vista-edis-gui-product</a></p></li>
<li><p>VistA: <a href="https://github.ec.va.gov/EPMO/vista-edp">https://github.ec. XX.XXX /EPMO/vista-edp</a></p></li>
<li><p>Source: <a href="https://github.ec.va.gov/EPMO/edis-gui">https://github.ec. XX.XXX /EPMO/edis-gui</a></p></li>
<li><p>Security: <a href="https://github.ec.va.gov/EPMO/lib-hps-security-java">https://github.ec. XX.XXX /EPMO/lib-hps-security-java</a></p></li>
</ul></td>
</tr>
<tr class="even">
<td>Cache/IRIS</td>
<td>Cache is needed to support a VistA environment for VistALink interaction. Remote instances are preferred, but local Cache instances can be used.</td>
</tr>
<tr class="odd">
<td>Oracle 19c</td>
<td>Oracle 19c database may be setup locally or remotely for development. SQLPUS or other capable SQL client may be used to access Oracle. Command line scripting of sql scripts must use SQLplus.</td>
</tr>
<tr class="even">
<td>Jasper reports</td>
<td>The Jasper reports designer tool is needed on developer workstations who create or maintain the defined (non Adhoc) reports.</td>
</tr>
</tbody>
</table>

## Development Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General development deployment of BR is done using the ANT deploy target in the build.xml file. Developers using this target to deploy the application will also need to configure the build.properties file located in the development root directory to match their local environment.

### Maven

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Maven 3.8.3 is the build tool for Blind Rehab. Each project contains a build file in the root directory named POM.xml.

### Log4j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Log4j 1.2.8 is the logging tool used in the Blind Rehab logging framework. The logging framework is encapsulated in the XXX.va.XXX.br.util.BRLogger class. This encapsulation isolates the system from changes in the logging tool. If the logging tool is replaced in a future version, only XXX.va.XXX.br.util.BRLogger class should need to be modified.

### Libraries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional libraries are necessary for development and/or building of Blind Rehab. These libraries change over time and a current list is available in the Blind Rehab build.xml file of each project.

## HealtheVet Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following VA services are deployed locally in a Weblogic server:

SDS

VLJ

PSL

### SDS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Standard Data Services API V. 18.0, Database V 18.0 is the version used by Blind Rehab.

### VLJ

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vista Link Java 1.5 is the version used by Blind Rehab.

### KAAJEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PSL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Person Service Lookup 4.0.4.4 is the version used by Blind Rehab.

### PSC (Formerly PSD)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Service Construct R2 is the version used by Blind Rehab

# Business Rule Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Web Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BR menu options are created dynamically based on the roles that a user has assigned to them. Users are not presented with menu links that are outside of their roles.

Select lists that contain Institutions in primary user functions are loaded only with Institutions assigned to that user. Select lists in administrative and program office functions are loaded with the complete Institution list for Blind Rehabilitation services.

N/A

## Data Validation- View Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data entry validations are generally performed by JavaScript in each data entry page. This is done to provide immediate feedback to the user for correction and place focus on the data element responsible for the problem. This also removes the overhead of a complete http post operation just to determine that a data entry field may be invalid. Business rules are not implemented in the pages except where validation of one field depends on the value entered in another field.

## Data Validation- Control Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation uses the open source JSF Framework to assist in the flow between pages and initiate the actions performed as pages are submitted. Blind Rehab extends the JFS Action classes in the XXX.va.XXX.br.ui.jsf.actions package to provide the control layer of the application. The BR action classes determine which function a user is intending to perform and either forward to the proper page or call business delegates to perform a transaction, and then forward to the result page. The action classes create Blind Rehab data objects from the submitted page values and validate entries at that time. The action classes also verify proper session state before performing transactions.

## Data Validation- Business Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

T The business delegates validate the business function that a user is attempting to conduct, performs audit trail recordkeeping, create User Transaction contexts for update transactions The classes call the appropriate data access object(s) (DAO) to interact with the database or VistA.

## Data Validation- Model Layer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Model objects in Blind Rehab are contained in the XXX.va.XXX.br.bo and XXX.va.XXX.br.dto packages. These objects help control data validation by using private data attributes, multiple constructors, and getter/setter methods.

Final data integrity checks are performed by the XXX.va.XXX.br.dao package and database DDL. Most BR DAO classes access only the Oracle database. These ‘internal’ data DAO’s manage record keys, data format conversions, and conversion of improper null values to valid empty values. The Oracle database schema DDL contains a significant number of constraints that describe primary key columns, protect referential integrity, and ensure existence of all required (“not NULL”) fields.

Several DAO objects are capable of interfacing with VistA systems over the VistALink connectors. Data which is retrieved from or saved to VistA is handled and validated by these “external” data DAO’s.

## Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BR uses Java User Transactions to wrap all create and update functions. This allows for simple rollback of all steps in a failed transaction or full commit for successful transactions. BR does not use Java user transactions for query only functions. BR does not have any record deletion capability accessible from the user interface.

Transactions can only be performed by the running Blind Rehab application (system user) or a fully logged in and authorized Blind Rehab user account. All transactions are logged to the AUDIT_TRAIL table with the identity of the user who performed it.

Transactions and the associated audit trail record cannot be undone or deleted through any UI provided facility. Because transactions can affect multiple data records in complex interactions, rolling back a transaction requires investigation of the data affected and a planned course of action to revert any changes. This will need to be a coordinated effort between the user, Tier 2 support, and Tier 3 support.

## Notifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notifications are currently in use only for newly created referrals. Upon login, the system performs an automated referral search on behalf of the user. The referral search parameters are controlled by:

The logging in user’s roles (must be able to create or search for referrals)

The user’s assigned institutions (only searches with those institutions)

The ReferralAutoSearch parameters in the application.properties file (for number of days back and referral states to include)

After the search is complete and if referrals were found, a notification is added to the UserState object associated with the user’s http session. The list of notifications is displayed in the Home page. A URL anchor (link) is part of the notification and directs the user to the result list for that notification.

The notification framework is being enhanced to allow for multiple types of Notifications and to store them between logins. Starting in build 5.1, notifications are being used to alert users to patients who have become deceased.

## Concurrency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BR uses optimistic concurrency. This is performed in the DAO layer. Prior to updating a record, the DAO will check the Modified Date/Timestamp of the object to be updated and compare it to the current record in the database. If the database record was updated after the user initially acquired the record (updated by another user), a Blind Rehab Exception is thrown to alert the user that they must refresh and re-edit the record they are modifying before saving is allowed. Database record locking was avoided because of its proprietary nature and access problems when a record lock is not released. A more sophisticated and non-proprietary in-memory object lock has been discussed and may be implemented later.

## Overnight Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Blind Rehabilitation performs the following scheduled overnight processing:

Demographic updates for all patients. Because BR is a separate centralized database from the authoritative VistA servers where the patient data resides, it must be refreshed periodically to remain synchronized. This process is handled by the PSDUpdater class. PSDUpdater runs once every 24 hours at a start time defined in the application.properties file. The PSDUpdater first obtains a list of all Blind Rehab patients grouped by home Institution (station) and then uses the Patient Service Construct (PSC) to acquire full demographic updates for the patients from their originating VistA server. PSC has a batching mechanism, which currently allows retrieving updates for 500 patients in each batch. Demographic data such as name, address, date of birth, and date of death are updated. If a patient is discovered to have become deceased (has a date of death), they will be flagged as an inactive patient during this process as well. Starting in version 5.1, newly deceased patients will have any open referrals cancelled and a deceased patient notification will be generated to alert their tracking user.

## MPI Interaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BR database stores Patient demographic data as a copy of the data that originated at a VistA server. Most demographic data can be updated during the overnight process, however, the key field for patients in VistA, the Integration Control Number (ICN) cannot be. Changes to a Patient ICN must be handled through interaction with the VA Master Patient Index (MPI). This interaction is conducted via direct HL7 messaging over TCP/IP sockets. For more information on the MPI related interaction and messages, please visit the MPI VDL link <https://www.va.gov/vdl/>

During processing of these interactions, the HL7 messages are logged in the BR application log4j output file and stored in the audit trail table

Blind Rehabilitation-MPI interaction is composed of the following interactions:

Registering interest in a patient with the MPI system.

Upon initial save of a patient or after conversion of a patient record into BR, register interest in the patient with MPI. This is done by sending an HL7 QBP (Query By Parameter) and receiving an HL7 RSP (Response Segment Pattern) response:

![](blind-rehab-version-5-1-technical-manual-security-guide/004.png)

The Blind Rehabilitation application will be interested in any changes to patient identifier information. The Blind Rehabilitation application will send MPI a QBP message that will contain a fully qualified source system id (i.e. in your implementation that is station \# and DFN) for each patient in which we are interested. There will be one QBP message per fully qualified source id of interest. MPI will then send an RSP message that will supply the fully qualified enterprise id (i.e. ICN and 200M) or a “No record Found” response that will be used to update the Blind Rehabilitation database. If an ICN is supplied the Blind Rehabilitation application should immediately update the ICN stored for the corresponding patient. If a “no record found” response is sent then the ICN provided either in the initial load or by the PS Lookup should be used until an unsolicited ADT-A24 is sent (see Linking of a source id to an ICN section). (See MPI Interface spec for specific examples). Note that the QBP is sent over a socket that is created by the Blind Rehabilitation application, and the Accept ACK is returned over the same socket. At this point, the socket is closed. The RSP message is then sent over a socket that is created by MPI and the Accept ACK is returned over this socket.

After successfully processing of the RSP, the patient is marked as registered by setting the MPI_REGISTERED column of the PATIENT table to ‘Y’. All patients in Blind Rehabilitation must be registered with the MPI. This is the only Blind Rehabilitation initiated MPI event.

Duplicate resolutions for enterprise systems (ICN Merge).

![](blind-rehab-version-5-1-technical-manual-security-guide/005.png)

Example:

MSH^~\|\\^MPIF TRIGGER^200M~MPI.FO-ALBANY.XXX.VA.XXX~DNS^MPIF TRIGGER^200BR~domainname~DNS^20041110132901-0500^^ADT~A24^200890416^T^2.4^^^AL^AL^

EVN^A24^20041110132901-0500

PID^1^^1008520398V272129\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|036664114\~\~~USSSA&&0363~SS~VA FACILITY ID&553&L\|7171324\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^MPIPATIENT~ELEVEN\~\~\~\~~L^MPIMAIDEN\~\~\~\~\~~M^19690303^F^^^~

~NEW YORK CITY~36\~\~~N^^^^^^^^^^^^^

^^^^^^^

PD1^^^DETROIT,MI~D~553

PID^2^^1008520400V272129\~\~~USVHA&&0363~NI~VA FACILITY ID&553&L\|036664114\~\~~USSSA&&0363~SS~VA FACILITY ID&553&L\|7171324\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^MPIPATIENT~ELEVEN\~\~\~\~~L^MPIMAIDEN\~\~\~\~\~~M^19690303^F^^^~

~NEW YORK CITY~36\~\~~N^^^^^^^^^^^^^

MPI will send the Blind Rehabilitation system notification when an enterprise ICN duplicate is found. An enterprise duplicate is defined as a patient having two or more ICN numbers assigned to them in MPI. For an enterprise duplicate, an ADT-A24 message will be sent. This message’s first PID segment will contain the new patient identifier information, and the second PID will contain the old patient identifier information. Between these two PID segments, the DFN/Station Number will not change, but ICN will. Note that the ADT A24 is sent over a socket that is created by MPI, and the Accept ACK is returned over the same socket. At this point, the socket is closed. The Application ACK message is then sent over a socket that is created by the Blind Rehabilitation application and the Accept ACK is returned over this socket.

After successfully processing this ADT-A24, the patient is marked as ‘Not-Selectable’ in Blind rehab by setting the ICN_CHANGE_NOTIFICATION column of the PATIENT table to ‘M’ (for merge). Users will not be able to select or enter/edit data for the patient until a manual merge is completed. Since this event indicates that a patient has multiple records in the database, one primary patient record needs to be chosen and the duplicates removed. All the child records associated with the duplicate patient records will need to be associated with the proper patient record. This process involves caregiver decisions and cannot be automated. The caregiver will need to work with EVS support, IMDQ, BR developers, and the BR DBA to resolve the issue. Once the duplicate has been resolved, the DBA may manually set the ICN_CHANGE_NOTIFICATION indicator to ‘N’.

This condition is rare but requires support assistance to resolve. To help resolve the event and respond proactively, an email message is generated when this event is processed. The email is sent to a mail group defined in the application.properties file with appropriate descriptions of the event. This email is intended to inform the EVS support group that manual clean up of a Blind Rehabilitation record is required and prompt them to contact the affected user.

Duplicate resolutions for source systems (ICN Merge).

![](blind-rehab-version-5-1-technical-manual-security-guide/006.png)

Example:

MSH^~\|\\^MPIF TRIGGER^200M~MPI.FO-ALBANY.XXX.VA.XXX~DNS^MPIF TRIGGER^200BR~domainname~DNS^20041110132901-0500^^ADT~A24^200890416^T^2.4^^^AL^AL^

EVN^A24^20041110132901-0500

PID^1^^1008520398V272129\~\~~USVHA&&0363~NI~VA FACILITY ID&200M&L\|036664114\~\~~USSSA&&0363~SS~VA FACILITY ID&553&L\|7171324\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^MPIPATIENT~ELEVEN\~\~\~\~~L^MPIMAIDEN\~\~\~\~\~~M^19690303^F^^^~

~NEW YORK CITY~36\~\~~N^^^^^^^^^^^^^

^^^^^^^

PD1^^^DETROIT,MI~D~553

PID^2^^10085203400V272129\~\~~USVHA&&0363~NI~VA FACILITY ID&553&L\|036664114\~\~~USSSA&&0363~SS~VA FACILITY ID&553&L\|7171323\~\~~USVHA&&0363~PI~VA FACILITY ID&553&L^^MPIPATIENT~ELEVEN\~\~\~\~~L^MPIMAIDEN\~\~\~\~\~~M^19690303^F^^^~

~NEW YORK CITY~36\~\~~N^^^^^^^^^^^^^

^^^^^^^

MPI will send the Blind Rehabilitation system notification when a source system duplicate is found. A source system duplicate is defined as a patient having two or more patient records assigned to them on a legacy VistA site. For a source system duplicate, an ADT-A24 message will be sent. This message’s first PID segment will contain the TO patient identifier information (i.e. ICN and DFN), and the second PID will contain the FROM patient identifier information (i.e. ICN and DFN). Between these segments, the DFN/Station Number will change, and the ICN may or may not change. Note that the ADT A24 is sent over a socket that is created by MPI, and the Accept ACK is returned over the same socket. At this point, the socket is closed. The Application ACK message is then sent over a socket that is created by the Blind Rehabilitation application and the Accept ACK is returned over this socket.

After successfully processing this ADT-A24, the patient is marked as ‘Not-Selectable’ in Blind rehab by setting the ICN_CHANGE_NOTIFICATION column of the PATIENT table to ‘M’ (for merge). Users will not be able to select or enter/edit data for the patient until a manual merge is completed. Since this event indicates that a patient has multiple records in the database, one primary patient record needs to be chosen and the duplicates removed. All the child records associated with the duplicate patient records will need to be associated with the proper patient record. This process involves caregiver decisions and cannot be automated. The caregiver will need to work with EVS support, BR developers, and the BR DBA to resolve the issue. Once the duplicate has been resolved, the DBA may manually set the ICN_CHANGE_NOTIFICATION indicator to ‘N’.

This condition is rare but requires support assistance to resolve. To help resolve the event and respond proactively, an email message is generated when this event is processed. The email is sent to a mail group defined in the application.properties file with appropriate descriptions of the event. This email is intended to inform the EVS support group that manual clean up of a Blind Rehabilitation record is required and prompt them to contact the affected user

Resolution of multiple patients sharing the same ICN (ICN Split):

![](blind-rehab-version-5-1-technical-manual-security-guide/007.png)

MPI will send the Blind Rehabilitation system notification when a fully qualified source id was erroneously linked to an ICN that resulted in two patients sharing the same ICN number. MPI will send an ADT-A43 in order to accomplish this notification. The ADT-A43 message’s PID segment will contain the TO patient identifier information (i.e. DFN and ICN), and the MRG segment will contain the FROM patient identifier information (i.e. DFN and ICN). Note that the ADT A43 is sent over a socket that is created by MPI, and the Accept ACK is returned over the same socket. At this point, the socket is closed. The Application ACK message is then sent over a socket that is created by the Blind Rehabilitation application and the Accept ACK is returned over this socket.

After successfully processing this ADT-A43, the patient is marked as ‘Not-Selectable’ in Blind Rehab by setting the ICN_CHANGE_NOTIFICATION column of the PATIENT table to ‘S’ (for split). Users will not be able to select or enter/edit data for the patient until a manual split is completed. Since this event indicates that two different people were associated with one patient ICN, a new patient record will need to be created and the appropriate child records associated with the appropriate patient. This process involves caregiver decisions and cannot be automated. The caregiver will need to work with EVS support, BR developers, and the BR DBA to resolve the issue. Once the duplicate has been resolved, the DBA may manually set the ICN_CHANGE_NOTIFICATION indicator to ‘N’.

This condition is very rare but requires support assistance to resolve. To help resolve the event and respond proactively, an email message is generated when this event is processed. The email is sent to a mail group defined in the application.properties file with appropriate descriptions of the event. This email is intended to inform the EVS support group that manual clean up of a Blind Rehabilitation record is required and prompt them to contact the affected user

Linking of a source id to an ICN (ICN Change):

![](blind-rehab-version-5-1-technical-manual-security-guide/008.png)

MPI will send the Blind Rehabilitation system notification for those fully qualified source system ids that have been previously registered via QBP (i.e. “No record found” from registering an interest in a patient with MPI). This message’s first and second PID segment will contain the TO patient identifier information (i.e. ICN and DFN). Note that the ADT A24 is sent over a socket that is created by MPI, and the Accept ACK is returned over the same socket. At this point, the socket is closed. The Application ACK message is then sent over a socket that is created by the Blind Rehabilitation application and the Accept ACK is returned over this socket.

After successfully processing this ADT-A24, the existing patient record is examined to see if the current ICN has changed. If the existing patient record is found, the INTEGRATION_CONTROL_NUMBER column of the PATIENT table is updated to the new ICN number in the message. This event does not disable the patient for selection. Users will be unaware that this event has occurred, as they cannot view the ICN number in the Blind Rehab application. This is the most common of the MPI initiated events and does not require support or user interaction. It is processed automatically by the Blind Rehab application.

MPI Inquiry of Blind Rehab Patient Data:

![](blind-rehab-version-5-1-technical-manual-security-guide/009.png)

MPI may occasionally inquire about the patient information that the Blind Rehabilitation system currently has. MPI will perform this by sending a QRY-A19 message. The Blind Rehabilitation application will be responsible for querying its data and sending a pertinent response via an ADR-A19 message. The QRY-A19 and ADR-A19 messages will be one per patient. (See MPI interface spec for specific examples). Note that the QRY is sent over a socket that is created by MPI, and the Accept ACK is returned over the same socket. At this point, the socket is closed. The ADR message is then sent over a socket that is created by the Blind Rehabilitation application and the Accept ACK is returned over this socket.

Additional messages from MPI:

The Blind Rehabilitation system will simply ACK any HL7 messages sent that are not included in this document. Nothing is done in response to these messages, but an ACK will be sent in order to be compliant with the HL7 specification

# Glossary/Acronym List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| *Term/Acronym*                                | *Description*                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AAA                                               | (Veteran Health Administration) Authentication, Authorization and Accountability Standards                                                                                                                                                                                                                                                                                                                                                                                  |
| AAIP                                              | Authentication and Authorization Infrastructure Program                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ADPAC                                             | Automated Data Processing Application Coordinator                                                                                                                                                                                                                                                                                                                                                                                                                           |
| AMIS                                              | Automated Management Information System                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| API                                               | Application Program Interface                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Audit Trail                                       | A history of the changes made to a record including old data, new data, and the name of the user who made the change. Record of access and modifications                                                                                                                                                                                                                                                                                                                    |
| BCMA                                              | Bar Code Medication Administration. A VistA software application that validates medications against active orders before the medication is given to the patient.                                                                                                                                                                                                                                                                                                            |
| BR                                                | Blind Rehabilitation Project                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Blind Rehabilitation Center (BRC)                 | A residential inpatient program that provides comprehensive adjustment to blindness training and serves as a resource to a catchments area usuallycomprised of multiple Veterans Integrated Service Networks (VISN).                                                                                                                                                                                                                                                        |
| BRC Application Letter                            | This is a cover letter for a Blind Rehabilitation Center (BRC) Application packet. This letter requires editing and is used to print for individual veterans.                                                                                                                                                                                                                                                                                                               |
| BRC Follow-up Letter                              | This is a questionnaire sent to the veteran following blind rehabilitation training. It is used to assist the center or clinic in following-up on the veteran.                                                                                                                                                                                                                                                                                                              |
| Blind Rehabilitation Outpatient Specialist (BROS) | Blind Rehabilitation instructors possessing advanced technical knowledge and competencies in at least two Blind Rehabilitation disciplines at the journeyman level.\[2\]                                                                                                                                                                                                                                                                                                    |
| CAT                                               | Computer Access Training                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| CARF                                              | Commission on the Accreditation of Rehabilitative Facilities                                                                                                                                                                                                                                                                                                                                                                                                                |
| CCOW                                              | Clinical Context Object Work Group                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| CCOW Term Telnet                                  | An application (written in Delphi) which is RPCBroker aware and capable of CCOW with CCOW, which can be used to access the Roll and Scroll environment, such as List Manager, in VistA.                                                                                                                                                                                                                                                                                     |
| CCOW Timing Program                               | A program, written in Delphi that tests the amount of time for Remote Procedure Calls to be processed by the server.                                                                                                                                                                                                                                                                                                                                                        |
| CHISS                                             | Common Health Information Security Services                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| C&P                                               | Compensation & Pension                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Claim Letter                                      | This is a cover letter to a Veterans Administration Regional Office (VARO) when filing a claim on behalf of a VIST veteran. This letter is used to print for individual veterans.                                                                                                                                                                                                                                                                                           |
| Common Procedure Terminology (CPT)                | A method for coding procedures performed on a patient, for billing purposes.                                                                                                                                                                                                                                                                                                                                                                                                |
| CPRS                                              | A VistA software application that provides an integrated patient record system for use by clinicians, managers, quality assurance staff, and researchers                                                                                                                                                                                                                                                                                                                    |
| CPRS/CCR                                          | Computerized Patient Record System/Computerized Clinical Reminder Module                                                                                                                                                                                                                                                                                                                                                                                                    |
| CPRS/VSM                                          | Computerized Patient Record System/Vital Signs Module                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Computerized Patient Record System (CPRS)         | A clinical record system that integrates many VistA packages to provide a common entry and data retrieval point for clinicians and other hospital personnel. (CPRS). CPRS is a Veterans Health Information Systems and Technology Architecture (VistA) software application that enables clinicians, nurses, clerks, and others to enter, review, and continuously update all information connected with patients.                                                          |
| Context Vault                                     | Data store that houses user sign-on credentials in a CCOW user context.                                                                                                                                                                                                                                                                                                                                                                                                     |
| DaIS                                              | Development and Infrastructure Support                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DBIA                                              | Data Base Integration Agreement                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DELPHI                                            | A Rapid Application Development (RAD) system/application developed by Borland International, Inc. Delphi is similar to Visual Basic from Microsoft, but whereas Visual Basic is based on the BASIC programming language, Delphi is based on Pascal.                                                                                                                                                                                                                         |
| Division                                          | The subunit under institute has 5-6 digits/letter division ID and less than a 35 character name                                                                                                                                                                                                                                                                                                                                                                             |
| EJB                                               | Enterprise Java Bean                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Encounter                                         | A contact between a patient and a provider who has the primary responsibility of assessing and treating the patient. A patient may have multiple encounters per visit. Outpatient encounters include scheduled appointments and walk-in unscheduled visits. A clinician’s telephone communications with a patient may be represented by a separate visit entry. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter. |
| Episode of Care                                   | An interval of care by a health care facility or provider for a specific medical problem or condition. It may be continuous or it may consist of a series of intervals marked by one or more brief separations from care, and can also identify the sequence of care (e.g., emergency, inpatient, outpatient), thus serving as one measure of health care provided.                                                                                                         |
| FSOD                                              | Functional Status Outcomes Database                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Graphical User Interface (GUI)                    | A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.                                                                                                                                                                                                                                                                                              |
| HCFA                                              | Health Care Financing Administration                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| HCPCS                                             | HCFA Common Procedure Coding System                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HFS                                               | Host File Server is a system (WinNT/Dec Alpha) file access mechanism that enables the M software (server software) to access the system-level files.                                                                                                                                                                                                                                                                                                                        |
| Health*<u>e</u>*Vet-VistA                         | The Health*<u>e</u>*Vet-VistA architecture will be a services-based architecture. Applications will be constructed in tiers with distinct user interface, middle and data tiers. Two types of services will exist, core services (infrastructure and data) and application services (a single logical authoritative source of data).                                                                                                                                        |
| HIPAA                                             | Health Insurance Portability and Accountability Act of 1996. Also referred to as, HIPAA.                                                                                                                                                                                                                                                                                                                                                                                    |
| HL7                                               | Health Level Seven                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| HSD&D                                             | Health Systems Design & Development                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| HSM                                               | Hospital-Supplied Self Medication                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HTTP                                              | Hyper Text Transfer Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| HTTPS                                             | Secured HTTP Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ICD9                                              | International Classification of Diseases 9<sup>th</sup> Edition                                                                                                                                                                                                                                                                                                                                                                                                             |
| ICN                                               | Identification Control Number                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| IDL                                               | Iterative Development Lifecycle                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| IE                                                | Internet Explorer                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| IEN                                               | Internal Entry Number                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Independent Verification and Validation (IV&V)    | The IV&V team supports the HSD&D mission by promoting standardization, improving software release quality and effectiveness of healthcare delivery through planned and controlled evaluation, testing, and integration of healthcare information systems. Visit the http://vista.XXX.va.XXX/ivv/ site for additional information.                                                                                                                                           |
| Inpatient Visit                                   | The admission of a patient to a VAMC and any clinically significant change related to treatment of that patient. For example, a treating specialty change is clinically significant, whereas a bed switch is not. The clinically significant visits created throughout the inpatient stay would be related to the inpatient admission visit. If the patient is seen in an outpatient clinic while an inpatient, this is treated as a separate encounter.                    |
| Institution                                       | A major hospital with subdivisions, usually has a name \< 30 letters and a three-digit division ID                                                                                                                                                                                                                                                                                                                                                                          |
| Invitation for VIST Review                        | This is an invitation to blinded veterans from VIST, offering a health evaluation. Veterans may accept or deny the invitation. This letter satisfies the requirements of M-2, Part XXIII and is meant to be printed as a mass mailing.                                                                                                                                                                                                                                      |
| IP                                                | Meds Inpatient Medications                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| IRM                                               | Information Resources Management                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| IRS Exemption Letter                              | This letter advises the Internal Revenue Service of legally blind status of veterans. This letter requires editing and is to be printed for individual veterans.                                                                                                                                                                                                                                                                                                            |
| ISO                                               | Information Security Officer                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ISSRA                                             | Interim Security Services for Rehosted Applications                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Iterative Development                             | The technique used to deliver the functionality of a system in a successive series of releases of increasing completeness. Each iteration is focused on defining, analyzing, designing, building, and testing a set of requirements.                                                                                                                                                                                                                                        |
| IV                                                | Intravenous                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| J2EE                                              | The Java 2 Platform, Enterprise Edition (J2EE) is an environment for developing and deploying enterprise applications. The J2EE platform consists of a set of services, APIs, and protocols that provide the functionality for developing multi-tiered, Web-based applications.                                                                                                                                                                                             |
| JAAS                                              | [Java Authentication and Authorization Service. For more information refer to the JAAS Web site at the following address: http://java.sun.com/products/jaas/index-14.html](http://java.sun.com/products/jaas/index-14.html)                                                                                                                                                                                                                                                 |
| JAVA                                              | Java is a programming language. It can be used to complete applications that may run on a single computer or be distributed among servers and clients in a network.                                                                                                                                                                                                                                                                                                         |
| JCAHO                                             | Joint Commission on the Accreditation of Health Care Organizations                                                                                                                                                                                                                                                                                                                                                                                                          |
| JDBC                                              | Java Database Connection                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| JSP                                               | Java Server Page                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Kernel                                            | Set of VistA software routines that function as an intermediary between the host operating system/application and the VistA application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.                                                                                                                                    |
| Kiosk                                             | Public workstations shared by multiple users.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| List Manager                                      | A VistA software product that creates a framework for user actions. List Manager is part of the VistA software infrastructure.                                                                                                                                                                                                                                                                                                                                              |
| LOINC                                             | Logical Observation Identifier Names and Codes                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MAH                                               | Medication Administration History                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MAS                                               | Medical Administration Service                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| MH Assistant                                      | Mental Health Assistant                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MPI                                               | Master Patient Index                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| MST                                               | Military Sexual Trauma                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MTAS                                              | Middle Tier WebLogic Application Server                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| MVC                                               | Model View Controller                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| New Person (#200) File                            | A VistA file that contains data on employees, users, practitioners, etc. of the VA.                                                                                                                                                                                                                                                                                                                                                                                         |
| NOIS                                              | National Online Information System                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| NVS                                               | National VistA Support                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| O-R                                               | Object-Relational                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OCS                                               | VA Office of Cyber Security                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| OID                                               | Oracle Internet Directory                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ORACLE                                            | Oracle is a relational database that supports the Structured Query Language (SQL), now an industry standard.                                                                                                                                                                                                                                                                                                                                                                |
| ORACLE 9iAS                                       | Oracle 9i Application Server                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PATS                                              | Patient Advocate Tracking System/application. When completed, the Patient Advocate Tracking System/application will replace the current, site-based Patient Representative package with a national level application.                                                                                                                                                                                                                                                       |
| PCE                                               | Patient Care Encounter                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| PIMS                                              | Patient Information Management System                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PIR                                               | Patient Incident Review File                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PLU                                               | Patient Lookup                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| PSC                                               | Patient Service Construct                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| PSD                                               | Patient Service Demographics                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| PSL                                               | Person Service Lookup                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| PRN                                               | Pro Re Nata, Latin meaning ‘as needed’                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Prototype                                         | An initial working model as proof of concept of a product or new version of an existing product.                                                                                                                                                                                                                                                                                                                                                                            |
| Provider                                          | The entity that furnishes health care to consumers. An individual or defined group of individuals who provide a defined unit of health care services (defined = codable) to one or more individuals at a single session.                                                                                                                                                                                                                                                    |
| PTF                                               | Patient Treatment File (PTF) at AAC                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RDBMS                                             | Relational Database Management System                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Registration                                      | Registration File                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| RN                                                | Registered Nurse                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ROES                                              | Remote Order Entry System                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| SAS                                               | SAS is a company that provides data analysis, data mining, and data storage                                                                                                                                                                                                                                                                                                                                                                                                 |
| ScreenMan                                         | VA FileMan utility that provides a screen-oriented interface for editing and displaying data                                                                                                                                                                                                                                                                                                                                                                                |
| SDD                                               | Software Design Document                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| SQA                                               | Software Quality Assurance                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SDS                                               | Standard Data Service                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SRS                                               | Software Requirements Specifications                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SSL                                               | Secure Socket Layer                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SSO                                               | Single Sign On                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| TCP/IP                                            | Transmission Control Protocol/Internet Protocol                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Thin-client                                       | A simple client program, which relies on most of the function of the system being in the server, usually the Web browser in a Web domain                                                                                                                                                                                                                                                                                                                                    |
| TIU                                               | Text Integration Utility                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| User                                              | An Administrator, a Clinician, or a Researcher                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VA                                                | Veterans Affairs                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VA FileMan                                        | VistA database management system.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VAMC                                              | Veterans Affairs Medical Centers                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VARO                                              | Veterans Administration Regional Office                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VHA                                               | Veterans Health Administration                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VISN                                              | Veterans Integrated Service Network                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VIST                                              | Visual Impairment Service Team                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VistA                                             | Veterans Health Information Systems and Technology Architecture                                                                                                                                                                                                                                                                                                                                                                                                             |
| VistA MailMan                                     | VistA electronic mail system                                                                                                                                                                                                                                                                                                                                                                                                                                                |

# Operations and Maintenance Responsibilities 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Role & Brief Description                                                                                                                                                                                                                                               | Assigned Organization                        | Contact Information                |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------|------------------------------------|
| Tier 0: Local End User Support (e.g. Automated Data Processing Application Coordinator (ADPACS))                                                                                                                                                                       | Local IT                                     | Local IT                           |
| Enterprise Service Desk Tier 1: Provide first contact resolution via Knowledge Documents retained in CA Service Desk Manager.                                                                                                                                          | ITOPs (Enterprise Service Desk)              | 855-NSD-HELP (855-673-4357)        |
| Tier 2: The second level of service provider functions, which include problem screening, definition, and resolution. Service requests that cannot be resolved at this level in a set period of time are elevated to appropriate service providers at the Tier 3 level. | Sub Product Line                             | Kim Rust                           |
| Tier 3: The third level of service provider functions, which consist primarily of problem identification, diagnosis, and resolution. Service requests that cannot be resolved at the Tier 2 level are typically referred to the Tier 3 for resolution.                 | Enterprise Operations                        | HDSO SUS Triage                    |
| Receiving Org/Sustainment Manager: Coordinates ongoing support activities including budget reporting, contract management, and technical risk management during O&M.                                                                                                   | EPMO: Transition, Release, and Support (TRS) | Malachy Gossett and Philip VanCamp |
| COR \*\* Check with the Contracting Officer to determine if a certified COR is required and at what level during O&M.                                                                                                                                                  | EPMO                                         | John Elliott                       |
| Contracting Office                                                                                                                                                                                                                                                     | Technical Acquisition Center (TAC)           |                                    |

# Approval Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REVIEW DATE:

SCRIBE:

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Portfolio Director Date

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Product Owner Date

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Receiving Organization POC Date

Signed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Operations Support POC Date