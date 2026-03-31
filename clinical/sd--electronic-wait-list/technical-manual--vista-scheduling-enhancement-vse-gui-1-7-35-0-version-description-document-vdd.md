---
title: VistA Scheduling Enhancement (VSE) GUI 1.7.35.0 Version Description Document (VDD
doc_type: VDD
doc_label: Version Description Document
doc_layer: anchor
doc_subject: .0  (VDD
app_code: SD
app_name: Scheduling
section: CLI
app_status: archive
pkg_ns: SD
patch_ver: 1.7.35
patch_id: SD*1.7.35
group_key: "SD:SD:1.7.35"
file_numbers: []
security_keys: []
menu_options: 0
description: "--- title: | VistA Scheduling Enhancements (VSE) Version Description Document (VDD) for VS GUI Release 1.7.35.0 with VistA Patch SD\5.3\831 ---"
audience: 
keywords: 
  - table
  - contents
  - build
  - span
  - class
  - configuration
  - release
  - management
  - product
  - package
page_count: 0
word_count: 1357
section_count: 9
table_count: 9
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2022
revision_count: 2
revision_newest: 1/10/2023
revision_oldest: 1/3/2023
docx_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_release_1_7_35_0_vdd.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Scheduling_Archive/vs_gui_release_1_7_35_0_vdd.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=399"
---

---
title: |
  VistA Scheduling Enhancements (VSE)  
    
  Version Description Document (VDD) for  
    
  VS GUI Release 1.7.35.0 with VistA Patch SD\*5.3\*831
---

![](vista-scheduling-enhancement-vse-gui-1-7-35-0-version-description-document-vdd/001.png)

December 2022  

Office of Information and Technology (OIT)

Revision History

| Date      | Version | Description                                            | Author      |
|-----------|---------|--------------------------------------------------------|-------------|
| 1/10/2023 | 1.0     | Final Version                                          | Liberty ITS |
| 1/3/2023  | 0.1     | Baseline for VS GUI 1.7.35 with and Patch SD\*5.3\*831 | Liberty ITS |

<span id="_Toc101362171" class="anchor"></span>Table 1: General CM Information

Artifact Rationale

VA requires the Version Description Document (VDD) to identify, maintain, enhance, and recreate the product (IT asset) throughout its lifecycle. The VDD reinforces strong risk management practices and helps protect VA from loss of the product (IT asset), which is especially important with a regular rotation of personnel and contractors. The VDD is a mandated document that will be verified prior to Release.

The VDD is the authoritative inventory and roadmap of all Configuration Items (CIs) that make up the deployable product/system. CIs include source code files, builds/packaging, tools, baselines, locations, and associated product files. The VDD is a CI maintained under change control in the TRM-approved configuration management system, which is part of the VA Federated Configuration Management Database (CMDB).

Project Managers (PMs) and Configuration Managers (CMs) use the VDD as a tool for managing CIs and baselines associated with the deployable product. It is the responsibility of the Project Manager (PM) to ensure the processes are followed within the product build process (ProPath, Product Build: BLD-1 Develop Product Component). The expectation is for the VDD to be controlled as a source file with one VDD per Product. There may be multiple versions managed within the SCM repository, all following the baseline process. Information Technology (IT) Configuration Managers, or IT Architect/Development Leads, ensure the creation and modification of the Product’s VDD is integrated with any parallel activities performed on said product. The CM creates/updates the VDD each time the deliverable (file set) leaves the development environment, for testing or deployment. The VDD is the representation and result of the Software Configuration Management Procedures being followed. The Product’s procedures, along with work instructions, are to be created and maintained by the IT CMs, or IT Architect/Development Leads. For product procedure information, refer to the Software Configuration Management Procedures template (ProPath, Project Planning: PRP 3.7). The PM is responsible for ensuring the CM maintains versions of the VDD and deliverables (files) in the TRM-approved configuration management system.

Table of Contents

Table of Tables

# General Configuration Management (CM) Information


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [General Configuration Management (CM) Information](#general-configuration-management-cm-information)
- [CM Tools](#cm-tools)
- [Configuration Management of Documents](#configuration-management-of-documents)
  - [Release Documentation](#release-documentation)
  - [Baseline and Component](#baseline-and-component)
  - [Build Information](#build-information)
  - [Build Label or Number](#build-label-or-number)
- [Build and Packaging](#build-and-packaging)
  - [Build Logs](#build-logs)
  - [Build System/Process Information](#build-systemprocess-information)
- [Change Tracking](#change-tracking)
  - [Change and Configuration Management Repository](#change-and-configuration-management-repository)
  - [Changes Since Last VDD](#changes-since-last-vdd)
- [Release (Deployment) Information](#release-deployment-information)
The product name, Configuration Manager, VDD package name, and the project delivery team information are provided in Table 1.
| Deliverable (Product Name)        | Configuration Manager              | VDD Package Name                 | Project Name/ Delivery Team |
|-----------------------------------|------------------------------------|----------------------------------|-----------------------------|
| VistA Scheduling Patch            | <span class="mark">Redacted</span> | SD\*5.3\*831                     | VSE/ Liberty ITS            |
| VS Graphical User Interface (GUI) | <span class="mark">Redacted</span> | VA VistA Scheduling GUI 1.7.35.0 | VSE/ Liberty ITS            |
<span id="_Ref54079246" class="anchor"></span>Table 2: CM Tools Details

# CM Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CM tools in use by the contract team are presented in Table 2.

<table>
<caption><p><span id="_Toc101362173" class="anchor"></span>Table 3: Documentation Repository Information</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th>CM Tools</th>
<th>Jira, GitHub Enterprise Cloud (EC), FORUM</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CM Tool Location</td>
<td>Hines Data Center</td>
</tr>
<tr class="even">
<td>Tool Onsite/Offsite</td>
<td>Onsite</td>
</tr>
<tr class="odd">
<td>CM Tool Access Point of Contact (POC)</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>Access Information (Forms or other access requirements)</td>
<td><p>GitHub EC: Submit a request for access to the VSE-Scheduling-Team in GitHub EC via email</p>
<p>Jira: Must have a Max.gov account. Submit a request to the DevOps Tool Suite (DOTS) Service Desk</p></td>
</tr>
</tbody>
</table>

<span id="_Toc101362173" class="anchor"></span>Table 3: Documentation Repository Information

# Configuration Management of Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections detail the configuration management of documents.

## Release Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Details about the repository for all approved release documentation are listed in Table 3.

| GH EC Information      | Explanation                              |
|------------------------|------------------------------------------|
| GitHub EC URL          | GitHub EC URL                            |
| GitHub EC Project Area | EPMO/Scheduling-GUI-Product              |
| GitHub EC Team Area    | EPMO/VSE-Scheduling-Team                 |
| GitHub EC Repository   | GitHub EC Repository                     |
| Components             | Approved, release-specific documentation |

<span id="_Ref71704616" class="anchor"></span>Table 4: Code Locations

## Baseline and Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Repositories where product code is identified as baselined, grouped, and managed are listed in Table 4.

| Name                          | Description                   |
|-------------------------------|-------------------------------|
| GitHub EC GUI Code Repository | GitHub EC GUI Code Repository |
| VistA Code                    | FORUM                         |

<span id="_Ref39227063" class="anchor"></span>Table 5: General Build Information

## Build Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The output that results from the build process is detailed in Table 5. Note that the VS GUI package is a Windows Installer file (msi), and the VistA patch is a Kernel Installation and Distribution System (KIDS) build.

<table>
<caption><p><span id="_Toc101362176" class="anchor"></span>Table 6: Build Label(s)/Number(s)</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Build Output</td>
<td><p>VS GUI package (msi file)</p>
<p>VistA patch SD*5.3*831 (KIDS)</p></td>
</tr>
<tr class="even">
<td>Build Output Directory</td>
<td><p>GUI: <u>SOFTWARE</u></p>
<p>VistA Patch: FORUM</p></td>
</tr>
<tr class="odd">
<td>Target Deployment Location</td>
<td><p>VS GUI: VistA Application Central Server (or similar technology depending on site)</p>
<p>VS GUI: Local Workstations via System Center Configuration Manager (SCCM) push (depending on site)</p></td>
</tr>
</tbody>
</table>

<span id="_Toc101362176" class="anchor"></span>Table 6: Build Label(s)/Number(s)

## Build Label or Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The identifier(s) for the derived object(s) or package(s) produced for deployment and/or installation.

| Name                                       | Description                               |
|--------------------------------------------|-------------------------------------------|
| VA VistA Scheduling SD\*5.3\*831           | VistA patch SD\*5.3\*831                  |
| VISTASCHEDULINGGUIINSTALLER_1_7_35_0_P.MSI | VS GUI R1.7.35.0 package - Production msi |
| VISTASCHEDULINGGUIINSTALLER_1_7_35_0_T.MSI | VS GUI R1.7.35.0 package – Test msi       |

<span id="_Toc101362177" class="anchor"></span>Table 7: Change Tracking

# Build and Packaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following subsections detail build and packaging information.

## Build Logs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See <u>Table 5</u> for the link to the location of the VistA GUI build log.

## Build System/Process Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA patches are coded and housed in FORUM. VS GUI code is created and housed in the GitHub EC repository. See Table 4 for more information.

# Change Tracking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA-approved change management tools are GitHub Enterprise Cloud (EC) and Jira. Details are provided in Table 7.

| Change Tracking Tools                                   | Jira, GitHub EC                    |
|---------------------------------------------------------|------------------------------------|
| Change Tracking Tool Location                           | Hines Data Center                  |
| Tool Onsite/Offsite                                     | Onsite                             |
| Change Tracking Tool Access/POC                         | <span class="mark">Redacted</span> |
| Access Information (Forms or other access requirements) | See <u>Table 2</u>                 |

<span id="_Toc101362178" class="anchor"></span>Table 8: VSE CCM Repository

## Change and Configuration Management Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information about the change and configuration management repository is detailed in Table 8.

| CCM URL          | VSE Jira                            |
|------------------|-------------------------------------|
| CCM Project Area | VistA Scheduling Enhancements (VSE) |
| CCM Team Area    | VistA Scheduling Enhancements (VSE) |

<span id="_Toc101362179" class="anchor"></span>Table 9: Enhancements and Defect Fixes

## Changes Since Last VDD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Changes since the last published VDD are provided in Table 9. The work item ID is the Jira issue number.

| Work Item ID                                                | Summary of Change                                                                                                |
|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| <span id="_Toc101362170" class="anchor"></span>\[VSE-3453\] | UI: Fix Phone Number Formatting in Patient Info                                                                  |
| \[VSE-4299\]                                                | VistA: Create a tool to clean up stuck orders                                                                    |
| \[VSE-4301\]                                                | UI: Disable the Duration Field in the New Appt Dialog for Fixed Timeslot Clinics                                 |
| \[VSE-4563\]                                                | VS GUI: Patient Record Flag Scrolling to the Bottom                                                              |
| \[VSE-4625\]                                                | VS GUI does not unlock request when clicking away, switching patients, or reloading grid                         |
| \[VSE-3017\]                                                | VistA: Add clinic time zone field to appointment object                                                          |
| \[VSE-3854\]                                                | VistA: Create a SDES RPC to undo Check-Out for an appointment                                                    |
| \[VSE-4118\]                                                | VistA: Modify SDES GET PAT FLAGS to return local patient flags                                                   |
| \[VSE-4148\]                                                | VistA: Write SDES RPCs for profile service gaps                                                                  |
| \[VSE-4149\]                                                | VistA: Create SDES RPC to mark appt as No Show                                                                   |
| \[VSE-4150\]                                                | VistA: Create SDES RPC to Undo No Show                                                                           |
| \[VSE-4152\]                                                | VistA: Modify RPCs that utilize stop codes to put AMIS logic into a tag                                          |
| \[VSE-4267\]                                                | VistA: Create an SDES RPC to batch retrieve clinic information                                                   |
| \[VSE-4380\]                                                | UI: Modify Patient Comments to Include Line Breaks                                                               |
| \[VSE-4449\]                                                | VistA: Modify SDES GET APPT REQ BY \* RPCs to return Service Connected Percentage                                |
| \[VSE-4477\]                                                | VistA: SDES RPC to return local and national canned cancellation comments                                        |
| \[VSE-4480\]                                                | VistA: Modify SDES GET CLIN AVAILABILITY to return an error when clinic institution does not have a timezone set |
| \[VSE-4557\]                                                | VistA: Remove SDES PCESAVE                                                                                       |
| \[VSE-4558\]                                                | VistA: Modify SDES EDITAPPT to send an error that appointment length cannot be edited                            |
| \[VSE-4561\]                                                | Display Child Facility for Veteran Appointment Requests                                                          |

<span id="_Toc101362180" class="anchor"></span>Table 10: Release Package POC Information

# Release (Deployment) Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The release identification and Implementation Manager’s information, and release package information are detailed in Tables 10 and 11.

| Release Identification | Release Package POC Name           | Release Package POC Email          |
|------------------------|------------------------------------|------------------------------------|
| VS GUI 1.7.35.0        | <span class="mark">Redacted</span> | <span class="mark">Redacted</span> |

<span id="_Toc101362181" class="anchor"></span>Table 11: Release Package Information

<table>
<caption>Release Package InformationRelease Package Information</caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Release Package (Component) Identified</th>
<th><p>VistA Scheduling GUI Application v1.7.35.0</p>
<p>VistA patch SD*5.3*831</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Release Package Description</td>
<td>VS GUI Application v1.7.35.0 with supporting patch SD*5.3*831</td>
</tr>
<tr class="even">
<td>Release Package Delivery Method</td>
<td>See Build Information</td>
</tr>
<tr class="odd">
<td>Release Package Location Identified</td>
<td>See Build Information</td>
</tr>
</tbody>
</table>

Release Package InformationRelease Package Information