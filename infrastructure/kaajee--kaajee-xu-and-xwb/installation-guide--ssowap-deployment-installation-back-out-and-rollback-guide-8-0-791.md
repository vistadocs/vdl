---
title: KAAJEE SSOWAP Deployment, Installation, Back-Out, and Rollback Guide (8.0*791)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: KAAJEE
app_name: KAAJEE (XU and XWB)
section: INF
app_status: active
pkg_ns: 
patch_ver: 8.0
patch_id: 
group_key: "KAAJEE::8.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - deployment
  - patch
  - vista
  - back
  - application
  - site
  - rollback
page_count: 0
word_count: 1280
section_count: 14
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/KAAJEE/kaajee_xu_8_791_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/KAAJEE/kaajee_xu_8_791_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=151"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>KERNEL AUTHENTICATION & AUTHORIZATION FOR J2EE Single Sign-On Web Application Plugin (KAAJEE SSOWAP)

  Deployment, Installation, Back-Out, and Rollback Guide
---

![](kaajee-ssowap-deployment-installation-back-out-and-rollback-guide-8-0-791/001.png)

May 2024

XU\*8\*791

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Revision History

When updates occur, the Title Page lists the new revised date, and this page describes the changes. Bookmarks link the described content changes to its place within manual. There are no bookmarks for format updates. Page numbers change with each update; therefore, they are not included as a reference in the Revision History.

| Date | Version | Description                                                  |
|----------|-------------|------------------------------------------------------------------|
| 05/2024  | 1.0         | Deployment Installation Backout Rollback Guide for KAAJEE SSOWAP |

<span id="_Toc161052826" class="anchor"></span>Table 1: Deployment, Installation, Back-out, and Rollback Roles and Responsibilities

Artifact Rationale

This document describes the Deployment, Installation, Back-out, and Rollback Plan for new products going into the VA Enterprise. The plan includes information about system support, issue tracking, escalation processes, and roles and responsibilities involved in all those activities. Its purpose is to provide clients, stakeholders, and support personnel with a smooth transition to the new product or software, and should be structured appropriately, to reflect particulars of these procedures at a single or at multiple locations.

Table of Contents

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
- [Patch Installation](#patch-installation)
  - [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [VistA Installation Procedure](#vista-installation-procedure)
  - [Installation Verification Procedure](#installation-verification-procedure)
- [WebLogic Installation](#weblogic-installation)
- [Rollback](#rollback)
This document describes how to deploy and install the Blind Rehabilitation patch XU\*8\*791web application*,* as well as how to back-out the product and rollback to a previous version or data set. This is a VistA “Informational” patch.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the web application will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Blind Rehabilitation web application requires that Identify and Access Management (IAM), Blind Single Sign-On Internal (SSOi) be provisioned for the application and that users of the application Link any of their existing VistA accounts with IAM’s Link My Account.

XU\*8\*791 project is for installation on a fully patched Veterans Health Information Systems and Technology Architecture (VistA) system. XU\*8\*791 is a VistA “Informational” patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints.

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment, installation, back-out, and rollback roles and responsibilities are shown in Table 1.

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 16%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Team</strong></th>
<th><strong>Phase / Role</strong></th>
<th><strong>Tasks</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Project Manager</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment</td>
</tr>
<tr class="even">
<td>Software Quality Assurance (SQA) Test Sites</td>
<td>Deployment</td>
<td>Test for operational readiness</td>
</tr>
<tr class="odd">
<td>Project Manager and Release Manager</td>
<td>Deployment</td>
<td>Execute deployment</td>
</tr>
<tr class="even">
<td>Individual VistA Sites</td>
<td>Installation</td>
<td><p>Plan and schedule installation.</p>
<p>This patch is “Informational”</p></td>
</tr>
<tr class="odd">
<td>Release Manager</td>
<td>Back-out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out)</td>
</tr>
<tr class="even">
<td>Sustainment Team</td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support</td>
</tr>
</tbody>
</table>

# Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The deployment is planned as a standard VistA National Patch Module (NPM) patch rollout. Once approval has been given to nationally release, ‘Informational’ patch XU\*8\*791 will be released from the NPM.

XU\*8\*791 will be released as an ‘Informational’ patch. There are no VistA software changes..

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The duration of deployment and installation is an ‘Informational’ patch. There is no changes to VistA.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the XU\*8\*791 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XU\*8\*791 will be nationally released to all VAMCs and deployed on the KAAJEE SSOWAP GUI/Web Server.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Initial Operating Capability (IOC) sites are:

- Houston VAMC
- Washington DC VAMC

The testing did not involve test site VistA software.

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XU\*8\*791 will not require site preparation.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resources involved in the release of XU\*8\*791 are the assigned Application Coordinators and the project VistA development team. The team will work in coordination with the test location testers.

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KAAJEE SSOWAP is a plugin. Designed to be used by the consuming application. XU\*8\*791 is being consumed and tested by VPFS.

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When XU\*8\*791 is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Blind Rehabilitation Package..

# Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

XU\*8\*791 “Informational” Patch has no VistA software components.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This product is a VistA “Informational” patch. Sites are responsible for marking the patch as a “Non-Kids” patch using the Patch Monitor Patch Processing Menu.

This is a web application Java Build. This is a centralized server promotion. No installation is required at local sites.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## VistA Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Staff performing the installation of XU\*8\*791 patch will need access to FORUM.

This patch is “Informational.”

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# WebLogic Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference the VPFS Installation Guide, Section 6 - VPFS Application Installation.

# Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference the VPFS Installation Guide, Section 10 - Rolling back the VPFS Application Install.