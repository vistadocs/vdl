---
title: XOBW*1*6 Deployment, Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: 
app_code: XOBW
app_name: HealtheVet Web Services Client (HWSC)
section: GUI
app_status: active
pkg_ns: XOBW
patch_ver: 1
patch_id: XOBW*1*6
group_key: "XOBW:XOBW:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - patch
  - configuration
  - back
  - xobw
  - vista
  - cache
  - procedure
page_count: 0
word_count: 1608
section_count: 14
table_count: 0
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p6_dibr.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p6_dibr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=180"
---

---
title: |
  <span id="_Toc186420068" class="anchor"></span>HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> 1.0

  Deployment, Installation, Back-Out, and Rollback Guide (DIBR)
---

![](xobw-1-6-deployment-installation-back-out-and-rollback-guide/001.png)

August 2020

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

Revision History

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 29%" />
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
<td>08/18/2020</td>
<td>1.0</td>
<td><p>XOBW*1.0*6:</p>
<ul>
<li><p>Initial document created for HWSC 1.0</p></li>
<li><p>Update Title page, Revision History, and Footers</p></li>
</ul></td>
<td><p>HWSC Developers</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Coordinate with System Administrator](#coordinate-with-system-administrator)
  - [VistA Environment, KIDS, and SSL/TLS Configurations](#vista-environment-kids-and-ssltls-configurations)
  - [Skills Needed for the Installation](#skills-needed-for-the-installation)
  - [Access Requirements—Privileges and Permissions Needed for the Installation](#access-requirementsprivileges-and-permissions-needed-for-the-installation)
    - [Caché System Administration Account Access](#caché-system-administration-account-access)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Obtain and Extract Distribution Files](#obtain-and-extract-distribution-files)
    - [Software](#software)
    - [Documentation](#documentation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
- [Installation Procedure](#installation-procedure)
  - [Patch Installation Instructions](#patch-installation-instructions)
    - [Cache System Management Portal](#cache-system-management-portal)
  - [Post Installation Procedure](#post-installation-procedure)
- [Implementation Procedure](#implementation-procedure)
  - [Verify Installation](#verify-installation)
- [Back-Out Plan](#back-out-plan)
  - [Back-Out Procedure](#back-out-procedure)
As the Department of Veterans Affairs (VA) and VistA applications employ further use of web services, there is a need to move towards more modern, secure communications protocols.
The current SSL/TLS configurations utilize older, insecure protocols. This patch will introduce a new SSL/TLS Configuration which utilizes TLSv1.2. This new configuration will be named ‘encrypt_only_tlsv12’.
Since there is no current software using this SSL/TLS ‘encrypt_only_tlsv12’ configuration, so there is no impact to current functionality. The new SSL/TLS configuration enables the VistA routines to make use of a newer security protocol.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to provide instructions for setting up the TLSv1.2 configuration in the Cache Management Portal.

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Coordinate with System Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers of the HWSC Patch XOBW\*1.0\*6 *must* coordinate with their respective system administration support group (e.g., HBMC Health Systems team) to receive assistance in performing the complete installation.

## VistA Environment, KIDS, and SSL/TLS Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers *must* coordinate with their system administrator to understand the number of nodes where Veterans Health Information Systems and Technology Architecture (VistA) is running and understand which nodes to which the installer has access. This applies to both VistA Test and Production accounts.

VistA applications are hosted in a Caché environment that can contain a cluster of one or more computer nodes. The basic topology is split into a set of Front-End nodes and a set of Back-End nodes (database nodes). For a small site, a single computer node can serve as both. For larger sites, the number of Front-End and Back-End nodes can vary.

A traditional KIDS installation is performed *ONCE and ONLY* on a Back-End database node. Changes to the Back-End node are visible to all other nodes, except for SSL/TLS Configurations.

> **NOTE:** The TLS/SSL configuration *must* be installed in all nodes, both front-end server nodes and database server nodes.

## Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installer needs to be familiar with the VistA environment and coordinate with a system administrator to be able to do the following:

- Obtain VistA software from FORUM and Secure File Transfer Protocol (SFTP) download sites (i.e., Product Support Anonymous Directories).
- Possess access to the Cache Management Portal with the %All or %Manager role.
- Understand VistA’s cluster of front-end and back-end (database) servers.

## Access Requirements—Privileges and Permissions Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers *must* coordinate with their system administrator to determine which level of access they have.

The following privileges and permissions to resources are required in order to create the HWSC Patch XOBW\*1.0\*6 Secure Socket Layer/Transport Layer Security (SSL/TLS) Configuration:

- Caché System Administration Account Access

### Caché System Administration Account Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers with a Programmer Support account should have the following roles (i.e., greater than the %Developer role):

- %All
- %Manager

To confirm you have the appropriate Caché privileges, look at \$ROLES. For example:

\>W \$ROLES

%All,%Developer

If you do *not* have one of the %All or %Manager roles, you *must* contact the system administrator for assistance.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your VistA Server in order to install and use the HWSC software:

- VistA account running on InterSystems’ Caché 2017.1.3 on Linux.
- VistA accounts *must* contain the fully patched versions of the following packages:
- HWSC 1.0
- Kernel 8.0
- Kernel Toolkit 7.3
- MailMan 8.0
- VA FileMan 22.0 (or higher)

  Note: These software packages *must* be properly installed and fully patched prior to configuring the TLSv1.2 setup in the Cache Management Portal. Patches *must* be installed in published sequence. You can obtain all released VistA patches (including patch description and installation instructions) from the Patch module on FORUM or through normal procedures.

## Obtain and Extract Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC Patch XOBW\*1.0\*6 is an informational patch only.

### Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for HealtheVet Web Services Client is available on the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/application.asp?appid=180>.

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories via Secure File Transfer Protocol (SFTP).

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for HWSC Patch XOBW\*1.0\*6.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no cron scripts for the HWSC Patch XOBW\*1.0\*6.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps *must* be completed by a Cache Systems Manager with the %Manager role.

Patch XOBW\*1.0\*6 is an informational patch, and as such *does not* require a “true” installation of software. The System Administrator will set up the entire configuration via the Cache Management Portal.

The Transport Layer Security (SSL/TLS) configuration *must* be installed on each of the nodes in the cluster.

> **NOTE:** The TLS/SSL configuration must be installed in all nodes, both front-end server nodes and database server nodes.

The configuration list with patch XOBW\*1.0\*4, prior to Patch XOBW\*1.0\*6, is shown in <u>Figure 1</u>.

Figure 1: Current Configuration List from Patch XOBW\*1.0\*4

![](xobw-1-6-deployment-installation-back-out-and-rollback-guide/002.png)

### Cache System Management Portal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  As a System Manager, open the Cache Management Portal.
2.  Navigate to System Administration, Security, and then SSL/TLS Configurations.
3.  Select Create New Configuration on the SSL/TLS Configurations web page.
4.  Create the new configuration by setting the following information on the form.

> Configuration Name: encrypt_only_tlsv12

> Description: XOBW\*1.0\*6

> Enabled: Checked

> Type: Client

> Peer certificate verification level: None

> Private key type: RSA

> Password: Leave as is

> Protocols:

> SSLv3: Un-Checked

> TLSv1.0: Un-Checked

> TLSv1.1: Un-Checked

> TLSv1.2: Checked

> Enabled ciphersuites: ALL:!aNULL:!eNULL:!EXP:!SSLv2

The new configuration setup for Cache 2017 is shown in <u>Figure 2</u>.

Figure : Cache 2017 Configuration Setup

![](xobw-1-6-deployment-installation-back-out-and-rollback-guide/003.png)

## Post Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A post-installation procedure is not applicable for Patch XOBW\*1.0\*6, as this patch does not involve the installation of any software. The System Administrator is advised to use the Cache Management Portal to set up all the nodes. Patch XOBW\*1.0\*6 is an informational patch only, and as such does not require a “true” installation of software. The System Administrator will set up the entire configuration via the Cache Management Portal.

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Verify Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installer should coordinate with their respective system administration support group (e.g., HBMC Health Systems team) to receive assistance in performing and verifying the complete installation via the Cache Management Portal.

# Back-Out Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

Since this is an informational patch only, please follow the instructions in the Back-Out Procedure to remove the new SSL/TLS Configuration using the Cache Management Portal.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC Patch XOBW\*1.0\*6 installation does not affect any existing VistA applications. If there is a need to back out to the previous state, please perform the steps below.

Prior to back-out, the configuration setup of Patch XOBW\*1.0\*6 appears as shown in <u>Figure 3</u>.

Figure : Cache TLS/SSL Configuration List

![](xobw-1-6-deployment-installation-back-out-and-rollback-guide/004.png)

1.  Select the “Delete” link for the ‘ecrypt_only_tlsv12’ configuration. A pop-up window appears as shown in <u>Figure 4</u>.

> Figure : Confirm Deletion of the Configuration

> ![](xobw-1-6-deployment-installation-back-out-and-rollback-guide/005.png)

2.  Select Yes to confirm deletion of the configuration. The back-out procedure is now complete and the ‘encrypt_only_tlsv12’ configuration will no longer be visible in the SSL/TLS Configuration list.