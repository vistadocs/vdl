---
title: TBI Version 4.2 Description Document
doc_type: DESC
doc_label: Description Document
doc_layer: anchor
doc_subject: 
app_code: TBI
app_name: "Registry: Traumatic Brain Injury"
section: CLI
app_status: active
pkg_ns: TBI
patch_ver: 4.2
patch_id: TBI*4.2
group_key: "TBI:TBI:4.2"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](tbi-version-4-2-description-document/001.png)![](tbi-version-4-2-description-document/002.png)
audience: 
keywords: 
  - table
  - build
  - contents
  - configuration
  - class
  - strong
  - style
  - width
  - management
  - release
page_count: 0
word_count: 1611
section_count: 3
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2018
revision_count: 20
revision_newest: 05/15/2018
revision_oldest: 5/14/2013
docx_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbivdd.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Reg-Traumatic_Brain_Injury/tbivdd.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=198"
---

Version Description Document

Traumatic Brain Injury (TBI) Registry

Version v3.4.16

![](tbi-version-4-2-description-document/001.png)![](tbi-version-4-2-description-document/002.png)

May 2018

Document Version 2.8

Document Revision History

| Date       | Document Version | Description                                                                      | VDD Author / Team Role             | VA Group or Contract Company |
|------------|------------------|----------------------------------------------------------------------------------|------------------------------------|------------------------------|
| 05/15/2018 | 2.8              | New Release Details                                                              | <span class="mark">REDACTED</span> | Liberty ITs                  |
| 05/01/2018 | 2.7              | Updated Release Details                                                          | <span class="mark">REDACTED</span> | Liberty ITs                  |
| 04/15/2018 | 2.6              | Updated Release Details                                                          | <span class="mark">REDACTED</span> | Liberty ITs                  |
| 01/03/2018 | 2.5              | Updated Release Details                                                          | <span class="mark">REDACTED</span> | Liberty ITs                  |
| 12/26/2017 | 2.4              | Updated Release Details                                                          | <span class="mark">REDACTED</span> | Liberty ITs                  |
| 12/07/2017 | 2.3              | Updated for Release                                                              | <span class="mark">REDACTED</span> | Liberty ITs                  |
| 11/21/2017 | 2.1              | Update to version 2.2 of template                                                | <span class="mark">REDACTED</span> | Liberty IT                   |
| 9/4/2015   | 1.0              | Update to version 2.1 of template                                                | <span class="mark">REDACTED</span> | ManTech                      |
| 5/14/2013  | 0.1              | HREG Sustainment Sprint 19 Release of version v5.0.193.0, Forum Patch TBI\*2\*11 | <span class="mark">REDACTED</span> | ManTech                      |

Deliverable Version History, detailing date of changes, release/revision, descriiption of change, project name, and VA department.

Deliverable (Product) Version History

| Date       | Release / Revision | Description            | Project Name | VA Department       |
|------------|--------------------|------------------------|--------------|---------------------|
| 05/15/2018 | TBI 3.4.16.17      | TBIe v 3.4.16.17       | Development  | Product Development |
| 05/08/2018 | TBI 3.4.16.15      | TBIe v 3.4.16.15       | Development  | Product Development |
| 01/10/2018 | TBI v3.3.16.6      | TBIe v3.3.16.6         | Development  | Product Development |
| 12/26/2017 | TBI v3.3.16.4      | TBIe v3.3.16.4         | Development  | Product Development |
| 10/1/17    | TBI v3.2.15.7      | TBI v3.3.15.7          | Development  | Product Development |
| 7/8/2016   | TBI\*2\*17         | Release 9              | Sustainment  | Product Development |
| 4/8/2016   | TBI\*2\*16         | Release 7              | Sustainment  | Product Development |
| 3/7/2016   | TBI\*2\*14         | Release 6              | Sustainment  | Product Development |
| 2/3/2016   | TBI\*2\*13         | Release 5a             | Sustainment  | Product Development |
| 9/29/2015  | TBI\*2\*12         | Release 2 Sprint 22/23 | Sustainment  | Product Development |
| 6/9/2015   | TBI\*2\*11         | Sprint 19 Work Items   | Sustainment  | Product Development |

Revision History, detailing date of changes, version number, descriiption of change, and author of change.

VA requires the Version Description Document (VDD) to identify, maintain, enhance, and recreate the product (IT asset) throughout its lifecycle. The VDD reinforces strong risk management practices and helps protect VA from loss of the product (IT asset), which is especially important with a regular rotation of personnel and contractors.

The VDD is the authoritative inventory and roadmap of all Configuration Items that make up the deployable product/system. Configuration Items include source code files, builds/packaging, tools, baselines, locations, and associated product files. The VDD is itself a Configuration Item maintained under change control in the TRM-approved configuration management system, which is part of the VA Federated Configuration Management Data Base (CMDB).

Project Managers and Configuration Managers use the VDD template as a tool for managing Configuration Items associated with the deployable product. Project Managers distribute the VDD template to IT Configuration Managers (or IT Architect/Development Lead) at the beginning of the product build process (ProPath, Product Build: BLD-1 Develop Product Component). The Configuration Manager creates/updates the VDD each time the deliverable (file set) leaves the development environment, such as for testing or deployment. For product procedures, refer to the Software Configuration Management Procedures Template (ProPath, Project Planning: PRP 3.7). The Project Manager is responsible for ensuring the Configuration Manager completes the VDD and places the VDD with the deliverables (files) in the TRM-approved configuration management system.

Table of Contents

# General Configuration Management (CM) Information


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [General Configuration Management (CM) Information](#general-configuration-management-cm-information)
- [Configuration Management (CM) Tools](#configuration-management-cm-tools)
- [Configuration Management of Documents](#configuration-management-of-documents)
- [Configuration Management Development Files](#configuration-management-development-files)
    - [Component(s)](#components)
    - [### Build Information](#build-information)
    - [### CCM/RTC Build Definition](#ccmrtc-build-definition)
    - [Build Label or Number](#build-label-or-number)
- [Build and Packaging](#build-and-packaging)
  - [Build Logs](#build-logs)
  - [Build System/Process Information](#build-systemprocess-information)
- [Change Tracking](#change-tracking)
- [# Release (Deployment) Information](#release-deployment-information)
- [Additional Supporting Documentation](#additional-supporting-documentation)
| Deliverable (Product) Name  | Configuration Manager              | VDD Package Name                  | Project / Delivery Team |
|-----------------------------|------------------------------------|-----------------------------------|-------------------------|
| TBI: TRAUMATIC BRAIN INJURY | <span class="mark">REDACTED</span> | TBIe v3.4.16.17 core v504.16.6697 | HREG Sustainment        |
General Configuration management information includes deliverable (product) name, configuration manager, VDD package name, and project/delivery team.

# Configuration Management (CM) Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Deliverable/Application Version History, detailing date of changes, release/revision, descriiption of change, project name, and VA department</caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 19%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>CM Tools</th>
<th>CM Tool Location</th>
<th><p>Tool</p>
<p>Onsite/</p>
<p>Offsite</p></th>
<th><p>CM Tool Access</p>
<p>Point of Contact</p></th>
<th>Access Information (Forms or other access requirements)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Rational Change and Configuration Management (CCM/RTC)</td>
<td><mark>REDACTED</mark></td>
<td>Onsite</td>
<td>VA Rational Tools Team</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Deliverable/Application Version History, detailing date of changes, release/revision, descriiption of change, project name, and VA department

# Configuration Management of Documents 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCM/RTC location for the documents and CCM/RTC explanation for the information.

<table>
<caption>CCM/RTC location and information for documents and the explanation of CCM/RTC information required..</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>CCM/RTC Information</th>
<th>Explanation</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>CCM URL</strong></td>
<td>https://ccm.rational.oit.va.gov:9443/ccm/web</td>
</tr>
<tr class="even">
<td><strong>CCM Project Area</strong></td>
<td>Registries (CM)</td>
</tr>
<tr class="odd">
<td><strong>CCM Team Area</strong></td>
<td>Registries (CM)</td>
</tr>
<tr class="even">
<td><strong>CCM Stream</strong></td>
<td>Registries Sustainment (Branch)</td>
</tr>
<tr class="odd">
<td><strong>Baseline ID</strong></td>
<td>TBIe v3.4.16.17 core v504.16.6697</td>
</tr>
<tr class="even">
<td><strong>Components</strong></td>
<td>Registries TBI Documentation</td>
</tr>
<tr class="odd">
<td><strong>Directory Path</strong></td>
<td>“…\Registries TBI Documentation\” See below for subfolders</td>
</tr>
<tr class="even">
<td><strong>Documents included in the Baseline</strong></td>
<td><p>TBI Deployment Installation Roll Back Back-out Guide</p>
<p>TBI VDD</p>
<p>TBI User Manual</p>
<p>TBI POM</p>
<p>TBI Installation Guide</p></td>
</tr>
</tbody>
</table>

CCM/RTC location and information for documents and the explanation of CCM/RTC information required..

# Configuration Management Development Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CCM/RTC location for the documents and CCM/RTC explanation for the information.

| CCM/RTC Information  | Explanation                             |
|----------------------|-----------------------------------------|
| CCM URL          | https://clm.rational.oit.va.gov/ccm/web |
| CCM Project Area | Registries (CM)                         |
| CCM Team Area    | Registries (CM)                         |
| Stream           | Registries Sustainment (Branch)         |
| Baseline ID      | See component list below                |

General build information that results from the build process.

### Component(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Where a set of artifacts are grouped and managed.

<table>
<caption>Names and descriptions of components.</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Registries TBI </p>
<p>(TBIe v3.4.16.17)</p></td>
<td>TBI_UserInterface</td>
</tr>
<tr class="even">
<td>Registries_CORE_dll (HRE CORE v504.16.6697)</td>
<td>Contains common DLLs</td>
</tr>
<tr class="odd">
<td>Registries_CORE_Scr (HRE CORE v504.16.6697)</td>
<td>Contains source for common DLLs</td>
</tr>
</tbody>
</table>

Names and descriptions of components.

### ### Build Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General build information that results from the build process.

<table>
<caption>Names and descriptions of build information.</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Build Output</strong></td>
<td>See RTC Registries TBI Documentation\CM\BuildLogs</td>
</tr>
<tr class="even">
<td><strong>Build Output Directory</strong></td>
<td>N/A</td>
</tr>
<tr class="odd">
<td><strong>Target Deployment Location</strong></td>
<td><p>\\VAAUSCRSWEB71\Deployment Files\Development\TBI</p>
<p>(Note: special access required)</p></td>
</tr>
</tbody>
</table>

Names and descriptions of build information.

### ### CCM/RTC Build Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name of the build definition, which controls what is built and how it is built.

| Name | Description |
|----------|-----------------|
| N/A      | N/A             |

The name of the build log that is attached in the VDD.zip file or the name of the build log and location it can be found within the build system.

### Build Label or Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The identifier for the derived object or package that was produced for deployment and/or install.

| Name                          | Description                   |
|-----------------------------------|-----------------------------------|
| TBIe v3.4.16.17 core v504.16.6697 | TBIe v3.4.16.17 core v504.16.6697 |

Names and descriptions of derived objects or pachages produced for deployment install.

# Build and Packaging 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Build Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See RTC Registries TBI Documentation\CM\BuildLogs

## Build System/Process Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See RTC Registries TBI Documentation\CM\BuildProcess

# Change Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Change Tracking, detailed by tool, tool location, onsite or offsite, tool access/POC, and access information.</caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 19%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>Change Tracking Tool</th>
<th>Change Tracking Tool Location</th>
<th><p>Tool</p>
<p>Onsite/</p>
<p>Offsite</p></th>
<th>Change Tracking Tool Access / POC</th>
<th>Access Information (Forms or other access requirements)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Rational Change and Configuration Management (CCM/RTC)</td>
<td><mark>REDACTED</mark></td>
<td>Onsite</td>
<td>VA Rational Tools Team</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Change Tracking, detailed by tool, tool location, onsite or offsite, tool access/POC, and access information.

| Location             | Terms                              |
|----------------------|------------------------------------|
| CCM URL          | <span class="mark">REDACTED</span> |
| CCM Project Area | Registries (CM)                    |
| CCM Team Area    | Registries (CM)                    |

Change Tracking, detailed by tool, tool location, onsite or offsite, tool access/POC, and access information.

| Work Item                                             | Summary                                                            |
|-------------------------------------------------------|--------------------------------------------------------------------|
| <span id="_Toc494954840" class="anchor"></span>500469 | TBIe - All Patient Phase Treatment Outcome Report                  |
| 500472                                                | TBIe - Rehabilitation and Reintegration Care Plan Report           |
| 500460                                                | TBIe - Patient Comprehensive Trend and Outcome Report              |
| 694377                                                | TBIe - 508 Compliance                                              |
| 716498                                                | Defect: TBIe Reports: R&RCPR, Avg Number of Days Calculation       |
| 716499                                                | Defect: TBIe Reports: R&RCPR, Question Answer Text Alignment       |
| 716500                                                | Defect: TBIe Reports: R&RCPR, Patient List Facility Results        |
| 716501                                                | Defect: TBIe Reports: APTPOR Calculation Columns                   |
| 716502                                                | Defect: TBIe Reports: PTCOR Historical M2PI Data                   |
| 716503                                                | Defect: TBIe Reports: PTCOR Summary Page Avg Discharge Calculation |
| 716504                                                | Defect: TBIe Reports: PTCOR 'Change in episode' calculations       |
| 708644                                                | 508 Defect: Red Banner Path Not Completely Read                    |
| 727400                                                | TBIe-Defects: TBIe Build 4 Reports UAT Round 3                     |

Work Item ID and Summary

# # Release (Deployment) Information 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption>Release Deployment information, including identification, POC name, and POC contact informaton.</caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 41%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>Release Identification</th>
<th>Release Package POC Name</th>
<th>Release Package POC Email</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>TBIe v3.4.16.17 core v504.16.6697</p>
<p>(Rel.Maj.Min.Patch.Build_subbuild)</p></td>
<td>HREG Release Management Team <mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

Release Deployment information, including identification, POC name, and POC contact informaton.

<table>
<caption>Release Package information, including identification, description, delivery method and location.</caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th>Release Package (Component) Identified</th>
<th>Release Package Description</th>
<th>Release Package Delivery Method</th>
<th>Release Package Location Identified</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TBIe v3.4.16.17 core v504.16.6697.zip</td>
<td>Publish target</td>
<td>File System</td>
<td><p>\\VAAUSCRSWEB71\Deployment Files\Production\TBI</p>
<p>(Note: special access required)</p></td>
</tr>
</tbody>
</table>

Release Package information, including identification, description, delivery method and location.

# Additional Supporting Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Document Name | Revision | Date |
|---------------|----------|------|
| N/A           |          |      |

Additional supporting documentation ncludes name, revision, and date.