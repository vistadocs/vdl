---
title: Hybrid DICOM Image Gateway (HDIG) Installation Guide Revision 3.2
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: MAG
patch_ver: 3.2
patch_id: MAG*3.2
group_key: "MAG:MAG:3.2"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - blockquote
  - dicom
  - hdig
  - class
  - table
  - service
  - contents
  - strong
  - vista
  - device
page_count: 0
word_count: 14415
section_count: 18
table_count: 2
figure_count: 0
appendix_count: 5
has_toc: False
is_stub: False
pub_date: July 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_HDIG_Installation_Guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/MAG_HDIG_Installation_Guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/001.png)

> VistA Imaging Hybrid DICOM ImageGatewayInstallation Guide

July 2019 – Revision 3.2

> Department of Veterans Affairs

> Product Development

> Health Provider Systems

HybridDICOM Image Gateway Installation Guide VistAJuly 2019Property of the US Government

This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.

While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

Product names mentioned in this document may be trademarks or registered trademarks of their respective companies and are hereby acknowledged.

VistA Imaging Product Development  

Internet: <span class="mark">REDACTED</span>  
VA intranet: <span class="mark">REDACTED</span>

Revision History

| Date     | Rev | Notes                                                                                    |
|--------------|---------|----------------------------------------------------------------------------------------------|
| Sep 13 2011  | 1       | Initial draft for end of contract date 9/13/2013. <span class="mark">REDACTED</span> (Rev 1) |
| May 9 2016   | 2       | Updates for MAG\*3.0\*162. <span class="mark">REDACTED</span>                                |
| May 31 2019  | 3       | Updates for MAG\*3.0\*204. <span class="mark">REDACTED</span>                                |
| July 17 2019 | 3.2     | Updates for MAG\*3.0\*204. <span class="mark">REDACTED</span>                                |

> Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [The Hybrid DICOM Image Gateway](#the-hybrid-dicom-image-gateway)
  - [Intended Audience](#intended-audience)
  - [Terms of Use](#terms-of-use)
  - [Terms and Abbreviations](#terms-and-abbreviations)
  - [Document Conventions](#document-conventions)
- [Installing a New HDIG](#installing-a-new-hdig)
  - [Preparing for a New HDIG Installation](#preparing-for-a-new-hdig-installation)
    - [Setting up VistA](#setting-up-vista)
    - [FDA Requirements](#fda-requirements)
    - [Requirements for the HDIG Host](#requirements-for-the-hdig-host)
    - [Site Information](#site-information)
    - [Apache Tomcat Application Password](#apache-tomcat-application-password)
    - [Laurel Bridge License](#laurel-bridge-license)
    - [VistA Site Service](#vista-site-service)
    - [Java Version](#java-version)
    - [Additional Considerations](#additional-considerations)
  - [New HDIG Installation](#new-hdig-installation)
    - [Running the HDIG Installer](#running-the-hdig-installer)
- [Updating an Existing HDIG](#updating-an-existing-hdig)
  - [Preparing for an HDIG](#preparing-for-an-hdig)
    - [.NET Version Update](#net-version-update)
    - [Java Version](#java-version-1)
  - [Updating the HDIG](#updating-the-hdig)
- [HDIG Post-Installation](#hdig-post-installation)
  - [Configuring the HDIG](#configuring-the-hdig)
    - [Verify Antivirus Scanning Exclusions](#verify-antivirus-scanning-exclusions)
    - [Increasing the Memory Allocated to the HDIG](#increasing-the-memory-allocated-to-the-hdig)
    - [Email Notifications](#email-notifications)
    - [Error Messages and Email Handling](#error-messages-and-email-handling)
    - [Warning Message Bundling for Email Handling](#warning-message-bundling-for-email-handling)
    - [Warning Email Handling Configuration Guidelines](#warning-email-handling-configuration-guidelines)
  - [Configure the HDIG for Each Image Processing Server](#configure-the-hdig-for-each-image-processing-server)
    - [Verify the HDIG Service Account Credentials](#verify-the-hdig-service-account-credentials)
    - [Updating the HDIG Administrator Email Address(es)](#updating-the-hdig-administrator-email-addresses)
    - [Save the HDIG Stat Page as the Home page](#save-the-hdig-stat-page-as-the-home-page)
    - [Save the HDIG Logs Page as a favorite](#save-the-hdig-logs-page-as-a-favorite)
  - [Testing the HDIG Operation](#testing-the-hdig-operation)
    - [Review the HDIG Stats Page for Each Image Gateway Server](#review-the-hdig-stats-page-for-each-image-gateway-server)
    - [Test and Review HDIG and Legacy Image Processing](#test-and-review-hdig-and-legacy-image-processing)
- [Post-Installation](#post-installation)
  - [Complete Appendix D – Post-Install Checklist](#complete-appendix-d-post-install-checklist)
- [Appendix A Activating the DCF Toolkit Product Serial Number](#appendix-a-activating-the-dcf-toolkit-product-serial-number)
  - [Network Activation](#network-activation)
  - [Manual Activation](#manual-activation)
- [Appendix B The DICOM AE Security Matrix](#appendix-b-the-dicom-ae-security-matrix)
  - [Overview - Configuring the DICOM AE Security Matrix](#overview-configuring-the-dicom-ae-security-matrix)
    - [Entries for Storage Functionality](#entries-for-storage-functionality)
    - [Entries for Query/Retrieve Functionality](#entries-for-queryretrieve-functionality)
    - [Entries for Import Functionality - Media](#entries-for-import-functionality-media)
    - [Entries for Import Functionality – Network Import](#entries-for-import-functionality-network-import)
  - [Fields in the DICOM AE SECURITY MATRIX](#fields-in-the-dicom-ae-security-matrix)
    - [Example DICOM AE SECURITY MATRIX Values (partial)](#example-dicom-ae-security-matrix-values-partial)
    - [Adding Devices to the DICOM AE SECURITY MATRIX](#adding-devices-to-the-dicom-ae-security-matrix)
    - [Entries for Storage Commitment Requests](#entries-for-storage-commitment-requests)
- [Appendix C Pre-Install Checklist](#appendix-c-pre-install-checklist)
- [Appendix D Post-Install Checklist](#appendix-d-post-install-checklist)
- [Appendix E DCF Toolkit Enterprise License Request Form](#appendix-e-dcf-toolkit-enterprise-license-request-form)

## The Hybrid DICOM Image Gateway

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Hybrid Digital Imaging and Communications in Medicine (DICOM) Image Gateway (HDIG) is a new component of the DICOM Gateway, introduced in MAG\*3.0\*34 to enable the storage of the newly supported Service Object Pair (SOP) classes.

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/002.png)

When you install the HDIG, you can select these components:

- DICOM Listener. The DICOM Listener listens on a specific port for incoming DICOM objects from pre-defined DICOM devices (Application Entities). It validates all newly supported SOP classes and stores the DICOM objects that pass the various validation checks in the new database structure. It forwards the previously supported SOP classes to the legacy gateway application for processing and storage in the old database.
- Archiver. The Archiver archives the newly supported SOP classes.
- New Abstract Maker. The new Abstract Maker creates abstracts (thumbnail icons) for the newly supported SOP classes.

In the course of installing the HDIG, you are prompted to select the components you want to enable on the specific gateway. You can enable all components on one gateway. You must have at least one instance of each component enabled at your site.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is intended for VA staff responsible for managing a local HDIG.

This document presumes a working knowledge of the VistA environment, VistA Imaging components and workflow, and Windows administration.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HDIG is a component of VistA Imaging and is regulated as a medical device by the Food and Drug Administration (FDA). Use of the HDIG is subject to the following provisions:

| ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/003.png) | Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.                                                                                                                                                  |
|------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/004.png) | The FDA classifies VistA Imaging, and the VIX (as a component of VistA Imaging) as a medical device. Unauthorized modifications to VistA Imaging, including the VIX, such as the installation of unapproved software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820). |
| ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/005.png) | Because software distribution/inventory management tools can install inappropriate or unapproved software without a local administrator’s knowledge, sites must exclude the VIX server from such systems.                                                                                                                              |

## Terms and Abbreviations 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following terms are used in this document.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACL</td>
<td><blockquote>
<p>Access Control List</p>
</blockquote></td>
</tr>
<tr class="even">
<td>AE</td>
<td><blockquote>
<p>Application Entity: An end point of a DICOM information exchange, including the DICOM network or media interface software; that is, the software that sends or receives DICOM information objects or messages. A single device may have multiple Application Entities.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AESM</td>
<td><blockquote>
<p>DICOM AE SECURITY MATRIX – a file in VistA for defining DICOM modality roles and service privileges</p>
</blockquote></td>
</tr>
<tr class="even">
<td>AE_Title</td>
<td><blockquote>
<p>The unique name assigned to a DICOM application to identify the application to other DICOM applications on the network.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Application log</td>
<td><blockquote>
<p>The primary log on the HDIG to which it writes application-level events.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Codec</td>
<td><blockquote>
<p>Encoding/Decoding of digital information</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>cPACS</td>
<td><blockquote>
<p>Commercial PACS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CPU</td>
<td><blockquote>
<p>Central Processing Unit</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CVIX</td>
<td><blockquote>
<p>Centralized VistA Imaging eXchange</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DCF</td>
<td><blockquote>
<p>DICOM Connectivity Framework</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DICOM</td>
<td><blockquote>
<p>Digital Imaging and Communication in Medicine</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DICOM Correct</td>
<td><blockquote>
<p>The name assigned to the process used to correct DICOM Objects that fail processing on the DICOM Gateway.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DICOM Importer</td>
<td><blockquote>
<p>Refers to the application that performs the automated DICOM import process from outside facilities.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DICOM Role</td>
<td><blockquote>
<p>Defines how a DICOM Service will perform the role as either a SCP or a SCU.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DICOM Service</td>
<td><blockquote>
<p>Consists of many different services, most of which involve transmission of data over a network</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DoD</td>
<td><blockquote>
<p>Department of Defense</p>
</blockquote></td>
</tr>
<tr class="even">
<td>DVD</td>
<td><blockquote>
<p>Digital Versatile Disc</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>HDIG</td>
<td><blockquote>
<p>Hybrid DICOM Image Gateway: An image gateway that combines the legacy DICOM Gateway and the new VISA Gateway. It implements DICOM services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IHS</td>
<td><blockquote>
<p>Indian Health Services</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>JRE</td>
<td><blockquote>
<p>Java Runtime Environment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>KIDS</td>
<td><blockquote>
<p>Kernel Installation and Distribution System</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Modality Device</td>
<td><blockquote>
<p>The type of DICOM device being used to generate or utilize DICOM objects.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Outside Facility</td>
<td><blockquote>
<p>External to the local facility. It can be another VA facility, a DoD facility, or another institution.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PACS</td>
<td><blockquote>
<p>Picture Archiving and Communications System</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PSN</td>
<td><blockquote>
<p>Product Serial Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Q/R</td>
<td><blockquote>
<p>Query/Retrieve</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RPC</td>
<td><blockquote>
<p>Remote Procedure Call</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SCP</td>
<td><blockquote>
<p>Service Class Provider</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SCU</td>
<td><blockquote>
<p>Service Class User</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SOP</td>
<td><blockquote>
<p>Service Object Pair</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SOP Class</td>
<td><blockquote>
<p>Unique identifier assigned by the DICOM Standard to identify DICOM objects.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Staging</td>
<td><blockquote>
<p>Copying study data from either media or an authorized network location into temporary persistent storage for later reconciliation. There are two types of staging (controlled by Security Keys):</p>
<p><em>Basic Staging</em>: An authorized user copies all study data from an authorized source to Importer Persistent Storage.</p>
<p><em>Advanced Staging</em>: An authorized user can view source data by study and copy data by study to Importer Persistent Storage.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>Supported SOP</p>
<p>Class</p></td>
<td><blockquote>
<p>A DICOM Object that can be processed by the DICOM Gateway and delivered to other VistA Imaging applications for use within VistA Imaging.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UID</td>
<td><blockquote>
<p>Unique identifier</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA</td>
<td><blockquote>
<p>US Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VISA</td>
<td><blockquote>
<p>VistA Imaging Services Architecture</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VistA</td>
<td><blockquote>
<p>Veterans Health Information Systems and Technology Architecture</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VIX</td>
<td><blockquote>
<p>VistA Imaging eXchange</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Document Conventions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following typographic conventions are used in this document.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 30%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Symbol/Typeface</th>
<th><blockquote>
<p>Meaning/Use</p>
</blockquote></th>
<th><blockquote>
<p>Example</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Bold</strong></td>
<td><blockquote>
<p>User input, selection, GUI element (menu item, button, field)</p>
</blockquote></td>
<td><blockquote>
<p>Click <strong>Finish</strong>.</p>
<p>Choose <strong>Open</strong> from the <strong>File</strong> menu.</p>
<p>Type the user account name in the <strong>Name</strong> field.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>Monospaced font</p>
<p>(typically, in a box)</p>
<p>(Bold indicates user input or selection).</p></td>
<td><blockquote>
<p>Command-line sample or output (such as character-based screen captures and computer source code), menus, file names</p>
</blockquote></td>
<td><blockquote>
<p>Navigate to the</p>
<p>\Docs\Imaging_Docs_Latest folder.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><em>Italics</em></td>
<td><blockquote>
<p>Emphasis, reference to section in the document or another document, or a variable</p>
</blockquote></td>
<td><blockquote>
<p>For more information, see the <em>VistA</em></p>
<p><em>Imaging DICOM Gateway</em></p>
<p><em>Installation Guide</em>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Square brackets, monospace or italics</td>
<td><blockquote>
<p>Variable, placeholder, VistA menu</p>
</blockquote></td>
<td><blockquote>
<p>Access the Kernel Installation and</p>
<p>Distribution System Menu [XPD MAIN].</p>
<p>;;3.0;IMAGING;[Patch</p>
<p>List];Mar 19, 2002;Build 1989;Feb 21, 2011</p>
<p>MAG*3.0*&lt;<em>PatchNumber</em>&gt;.KID</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p><strong>&lt;Enter&gt;</strong></p>
<p>in character-based screen captures</p></td>
<td><blockquote>
<p>Indicates that the user should press the Enter or Return key.</p>
</blockquote></td>
<td><blockquote>
<p>THEN PRINT FIELD: <strong>&lt;Enter&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 30%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>Symbol/Typeface</th>
<th><blockquote>
<p>Meaning/Use</p>
</blockquote></th>
<th><blockquote>
<p>Example</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UPPERCASE</td>
<td><blockquote>
<p>M code, variable names, or the formal name of options, field/file names, and security keys.</p>
</blockquote></td>
<td><blockquote>
<p>The XUPROGMODE key</p>
</blockquote></td>
</tr>
</tbody>
</table>

# Installing a New HDIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to implement a new HDIG.

Tip: If you are updating an existing HDIG, refer to section Updating an Existing HDIG.

## Preparing for a New HDIG Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before starting the HDIG installation, do the following:

### Setting up VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must install the compatible KIDS package on the VistA system before installing the HDIG server software. For information about how to install the KIDS package, see the patch description of the patch you are installing.

### FDA Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HDIG is a component of VistA Imaging and is therefore regulated as a medical device by the FDA.

### Requirements for the HDIG Host 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A VistA Imaging Exchange (VIX) is required for the HDIG software and the VIX must be running latest version. If you do not have a VIX or the latest version installed, please refer to the [*VIX Installation Guide*](https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_vix_installation_guide.pdf).

> **IMPORTANT:** The VIX server and the HDIG must be on different computers.

You must install the HDIG on all DICOM Image Gateways. Do not install the HDIG on dedicated TEXT or ROUTING gateways that do not process images.

Installing the HDIG updates the Query/Retrieve service and the server side of the DICOM Importer III application. You must enable the DICOM Listener on all DICOM Gateways on which you want to have any of the following:

- DICOM Listener to receive and process incoming images
- DICOM Importer III server to process imported images and DICOM Correct to correct patient or study lookup errors
- Query/Retrieve service

#### Hardware Requirements 

Minimum hardware requirements for installing the HDIG:

- Eight gigabytes of RAM are recommended.
- A dedicated local drive for the HDIG with at least 75 gigabytes of disk space. A larger drive may be desirable based on usage.

#### Network Requirements 

- The HDIG cannot be installed on the same server as the VIX.
- Ports 443, 8080 and 8443 must be accessible to VA wide area network IP addresses/FQDN from the HDIG server.
- The VistA Site Service must be accessible from the HDIG computer. The VistA Site Service is a central repository of information used by Imaging components to connect to other sites. For more information about it, see the *VistA Imaging System Technical Manual*.

#### Operating System and Environment Requirements 

The HDIG can only run on a computer with the following infrastructure elements installed:

- Windows Server 2012 Standard or Enterprise Edition

> <span class="mark">Note: Use Windows Updater to install any security updates available for .NET 4.6.2 and above. If there are issues installing the .NET framework, please reach out to the Helpdesk or CLIN3.</span>

> <span class="mark">Note: More recent .NET updates can be installed but be certain that .NET 4.6.2 and above are included in the installation.</span>

> <span class="mark">Note: If the Tier 1 equipment vendor (i.e., HP) template is used to create the virtual machine, then the appropriate .NET version may be included.</span>

#### Older Modalities and DICOM Modality Worklist Support 

If you are a site that has any older modalities installed, then verify that the modality is able to fully support the DICOM Modality Worklist function – Query by Accession Number. Some of the older devices only support query by case numbers.

### Site Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Make sure you have the following information about your site and VistA installation, which you must supply when you install the HDIG:

- Division and/or site code: the value of the field STATION NUMBER as defined in the INSTITUTION file (#4)
- Name of the VistA host and the domain
- Name of the DICOM Gateway host
- DICOM Gateway service account details:
  - DICOM Gateway Service Account logon
- Access code
- Verify code

### Apache Tomcat Application Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Prepare a password to be used for the Apache Tomcat administrator account that will be created as part of the HDIG installation process.
- This account will be rarely used; it only needs to be secured properly.
- The password is case-sensitive and only alphanumeric characters are allowed.
2.  Prepare a password to be used for the Apache Tomcat application account that will be created as part of the HDIG installation process.
- This Windows account, which will be named “apachetomcat” when it is created by the HDIG installer, is used to run the HDIG in the Tomcat environment. This account is limited to only the functions it needs to run the HDIG.
- The password is case sensitive, must contain at least eight characters, and must contain at least one capital letter and one number.

### Laurel Bridge License

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation requires an upgrade to the Laurel Bridge DCF license for each gateway that performs DICOM image processing. Time required to complete this task will vary depending on the number of DICOM Gateways.

> Request the product serial numbers from Laurel Bridge. See Appendix A, Appendix A Activating the DCF Toolkit Product Serial Number.

> Note: The DICOM Listener, which is included as part of the Query/Retrieve application, requires an upgrade of the existing Laurel Bridge DCF License to version 3.3.x.

> Upgrading the license keys is a two-part process. As part of the planning process, required information is submitted to Laurel Bridge to request Product Serial Numbers for each gateway server that will have an HDIG installed.

> During the installation of the HDIG, the Product Serial Numbers will be used to activate the new licenses on the HDIGs.

### VistA Site Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Site Service resides on the Centralized VistA Imaging eXchange (CVIX) host. Make sure that you have the location (URL) of the VistA Site Service and that the service is accessible from the computer on which you are installing the HDIG.

To find out if the VistA Site Service is accessible, try to access the VistA Site Service location (URL) from a browser on the computer on which you plan to install the HDIG: <span class="mark">REDACTED</span>

### Java Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Validate with the specific patch description document for the current version of Java. If the server has a different version of Java than the required version specified in patch description, the wizard will install/uninstall the Java version.

### Additional Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Verify that the DICOM Correct queue is empty (#2006.575).
- If you are using the Importer, verify that all studies have been reconciled and that the Importer queue is empty (#2006.5752).
- MAG\*3.0\*118 introduced a new file called the DICOM AE SECURITY MATRIX file (#2006.9192). The time it takes to configure this file will depend on the number of modality devices being configured. Estimate approximately one minute per device. Note: This should be configured after installing the KIDS but prior to performing the Gateway installations.

## New HDIG Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains how to install a new installation of the Hybrid DICOM Image Gateway (HDIG).

> **NOTE:** The screenshots are provided as a representation and the actual screenshots may show different patch numbers, path locations and other details.

### Running the HDIG Installer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HDIG installer runs two consecutive installation processes. The first is very short; it installs the HDIG installation wizard. The second installs and configures the HDIG.

#### Step 1 - Install the HDIG Installer 

1.  Log into the computer on which the HDIG will be installed using the administrator account you used to install the DICOM Gateway portion of the patch.
2.  Copy the HDIG installation file (MAG3_0P\<patch \#\>\_HDIG_Setup.msi) to a local folder on the server.

> **NOTE:** When you run the HDIG installer, make sure that all other applications are closed and that the focus is left on the installer. If you have other applications running, including other instances of the installer, you may get an error message.

3.  Do the following to prepare the HDIG Installation Wizard:
    1.  Double-click the HDIG installation file.

> Figure 1: HDIG Installation Wizard Welcome Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/006.png)

2.  When the Welcome page displays, click Next.
3.  When the Confirm Installation page displays, click Next.

> Figure 2: HDIG Installation Wizard Confirmation Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/007.png)

> Figure 3: HDIG Installation Wizard Installation Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/008.png)

> The following screen appears:

> Figure 4: HDIG Installation Wizard Installation Complete Page

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/009.png)

4.  When the Installation Complete screen displays, click Close.

#### Step 2 - Running the HDIG Installer 

1.  Choose Start \| All Programs \| Vista Imaging Programs \| HDIG Installation Wizard to start the HDIG Installation Wizard.

> Figure 5: Manual Search Field

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/010.png)

1.  When attempting to run the HDIG Installation Wizard you may receive the following error:

> Figure 6: Error Message  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/011.png)

> **NOTE:** You must have an active internet connection to click “Yes” and follow the next steps. If you do not have an active internet connection, STOP HERE and please contact your Help Desk/CLIN3 for assistance.

2.  Clicking Yes will bring you to the download page for .NET Framework 4.6.2, or click on the following [link](https://www.microsoft.com/en-us/download/details.aspx?id=53344) to access the offline installer.

> Figure 7: Download Page for .NET Framework 4.6.2  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/012.png)

3.  Click the DOWNLOAD button to download the .NET Framework 4.6.2 (NOT Developer Pack) and save it to your hard drive.

> Figure 8: .NET Framework 4.6.2 Download Message  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/013.png)

4.  Find the application file and run it to begin the install.

> Figure 9: Application File  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/014.png)

5.  Agree to the License terms and conditions and click Install.

> Figure 10: Microsoft .NET Framework 4.6.2 License Terms  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/015.png)

6.  The update will begin installation

> Figure 11: Microsoft .NET Framework 4.6.2 Installer  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/016.png)

7.  Once installation is complete, you must click Restart

> Figure 12: .NET Framework 4.6.2 Installation Complete  
> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/017.png)

2.  After successfully restarting, re-run the HDIG Service Installation Wizard. When the Welcome to the HDIG Service Installation Wizard dialog box displays, click Next.

> Figure 13: HDIG Service Installation Wizard Welcome Page

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/018.png)

3.  If the installer detects that the Gateway server has less than 3.5 GBs of memory, the following dialog box appears.

> Figure 14: Less than 3.5 GBs of Memory Detection Message

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/019.png)

4.  In the Specify the VA site the HDIG will service dialog box, enter the Site Number of the site where the HDIG service is installed, then click Lookup Server Addresses.

> Figure 15: Specify the VA Site the HDIG Will Service Dialog Box

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/020.png)

5.  Verify that the information the lookup retrieved is correct, then click Next.
6.  In the Specify the DICOM Configuration dialog box, enter the required information.
    1.  DICOM Image Gateway properties – The properties of the computer on which the DICOM Image Gateway resides:
- Server – The name of the host on which the DICOM Gateway has been installed (the host on which you are installing the HDIG).
- Designated Port – The number of the TCP port that the DICOM Gateway uses to communicate with the other VistA components. The port is 60001. You cannot modify this port.

> Figure 16: Specifying the DICOM Image Gateway

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/021.png)

1.  DICOM Image Gateway service account properties – The properties of the service account the HDIG uses to access the VistA menu options. You can get the account properties from the VistA administrator at your site.
- Access – The access code for accessing VistA
- Verify – The verify code for accessing VistA
- Confirm Verify – A field in which you type the verify code for accessing VistA again.

> Figure 17: Specifying the DICOM Configuration

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/022.png)

1.  DICOM Image Gateway services – The components (services) that the HDIG provides. You can enable all components on one computer. At least one component must be selected. By default, all components are selected. If you do not want to enable all components, clear the ones that you do not want to be enabled.
- DICOM Listener Enabled – This checkbox must be selected, if you plan to activate the DICOM Listener, enable the Query/Retrieve application, or enable the DICOM Importer on this gateway.
- Archive Enabled – This checkbox must be selected to activate the Archiver on this computer. Activating the Archiver enables archiving of the newly supported SOP classes for the site.
- Thumbnail Processing Enabled – This checkbox must be selected to enable the new Abstract Maker on this gateway.

> Figure 18: Configure Services Section of Figure 17

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/023.png)

1.  Send email notifications to: – This field specifies the email address or addresses to which the HDIG sends notifications when the HDIG detects invalid service account credentials. You must enter at least one email address in the field. If you want to enter more than one address, use a comma to separate the addresses.

> Figure 19: Send Email Notification to Section of Figure 17

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/024.png)

> Note: This email address does not configure the email address used for queuing email messages.

7.  Click Validate. The installation program checks the information. If it detects an error, it displays a tooltip with information about the error. When it validates the configuration, Next becomes available.
8.  Click Next to continue. When the Install the HDIG Prerequisites dialog box displays, review the list of required prerequisites.

> Figure 20: Required HDIG Prerequisites ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/025.png)

> For any items flagged with ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/026.png), see the following notes.

1.  \<account\> has Administrator role – This check verifies that an administrator account is being used. If not, cancel the installation and restart it using a Windows administrator account.
2.  Current operating system is \<OperatingSystem\> – This check verifies that the proper operating system is present. If a different operating system is used, the installation cannot continue.
3.  The Java Runtime Environment \<Version\> is installed. – Click Install if this component has not been installed already.
4.  Apache Tomcat – Click Install to create the Apache Tomcat administrator account. Provide the password defined in the Apache Tomcat Application Password section above. Type the password again in the Confirm Password field and click OK.

> Figure 21: Apache Tomcat Setup

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/027.png)

The Laurel Bridge DCF Toolkit

1.  If you enabled the DICOM Listener and the Laurel Bridge DCF Toolkit is not installed, click Install next to The Laurel Bridge DCF Toolkit prerequisite.

> If the HDIG host can connect to the Internet, an Activate DCF License dialog box opens. The Network Activation tab in the dialog box is already selected and some fields are pre-populated.

2.  Enter all of the following information in the Network Activation tab:
    - Product Serial Number – The new Laurel Bridge DCF toolkit serial number (include dashes).
    - Site – The name of your site.
    - Host – The name of the Server.
    - Number of CPUs – The number of CPUs on the server hosting the HDIG.
    - Contact name and Contact email – The administrator of your local VistA Imaging system.

> Figure 22: Activate DCF License Dialog Box

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/028.png)

3.  Click Activate. After a brief delay, the Status field will display a green Success message.

> Figure 23: Status Field Success Message

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/029.png)

4.  Click Exit with success. The Activate DCF License window will close and the updated Laurel Bridge toolkit will be installed (installation will only take a second or two).

> Figure 24: Exit with Success Option

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/030.png)

5.  If the HDIG host *cannot* connect to the Internet and can access the Laurel Bridge Web site, activate the license manually, as instructed in Appendix A Manual Activation of the SUPPLY.
6.  If you did not enable the DICOM Listener, the Install button is grayed out and the text next to it reads The Laurel Bridge DCF toolkit is not required.
7.  If the required version of the Laurel Bridge DCF toolkit is installed, there is a green check mark next to the text The Laurel Bridge DCF Toolkit is installed.
8.  Service Account– Click Create to create the HDIG service account. Provide the password if requested. Type the password again in the Confirm Password field and click OK

> Figure 25: Service Account Setup Page

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/031.png)

9.  When all items in the Prerequisites dialog have an ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/032.png) icon next to them, click Next.

> Figure 26: Completed Install the HDIG Prerequisites Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/033.png)

> Note: The HDIG installer was built using the same VISA foundation as the VIX, including the same installer program. There may be some references to the VIX directories even though an HDIG is being installed.

10. In the Specify the location of the HDIG cache and configuration folders dialog box, select the drive where you want the HDIG configuration files to reside, then click Create.

> **NOTE:** The HDIG configuration files must be on the local system drive (the drive on which the operating system is installed, which is typically C:\\.

11. Select the drive where the cache will be located, then click Create.

> Tip: We recommend using a different physical drive for the HDIG cache, if the computer on which you are installing the HDIG has another physical drive.

> Figure 27: Specify the Location of the HDIG Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/034.png)

12. Click Next.
13. In the Install the HDIG dialog box, click Install.

> Figure 28: Install the HDIG Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/035.png)

14. When installation completes, click Finish to exit the wizard. The HDIG service starts automatically after it is installed.

> Figure 29: HDIG Installation Complete

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/036.png)

# Updating an Existing HDIG 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Preparing for an HDIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### .NET Version Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">Note: Use Windows Updater to install any security updates available for .NET 4.6.2 and above. If there are issues installing the .NET framework, please reach out to the Helpdesk or Clin3.</span>

<span class="mark">Note: More recent .NET updates can be installed but make sure that .NET 4.6.2 and above are included in the installation.</span>

To verify your version of .NET:

1.  From the Start menu, choose Run, enter *regedit*, and then select OK.

> Note: You must have administrative credentials to run regedit.

2.  In the Registry Editor, open the following subkey: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\NET Framework Setup\NDP\v4\Full. If the Full subkey isn't present, then you don't have the .NET Framework 4.5 or later installed.

> Note: The NET Framework Setup folder in the registry does *not* begin with a period.

3.  Check for a DWORD entry named Release. If it exists, then you have .NET Framework 4.5 or later versions installed. Its value is a release key that corresponds to a particular version of the .NET Framework. In the following figure, for example, the value of the Release entry is *378389*, which is the release key for .NET Framework 4.5.

> Figure 30: DWORD Release Entry Name Example

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/037.png)

> Figure 31: .NET Framework Release Keys

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/038.png)

4.  Check to make sure .NET 4.6.2 and above is installed installing the HDIG Installer.

If your .NET version is not 4.6.2 or later:

1.  click on the following [link](https://www.microsoft.com/en-us/download/details.aspx?id=53344) to access the offline installer.

> Figure 32: Download Page for .NET Framework 4.6.2

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/039.png)

2.  Click the DOWNLOAD button to download the .NET Framework 4.6.2 (NOT Developer Pack) and save to your hard drive

> Figure 33: .NET Framework 4.6.2 Download Message

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/040.png)

3.  Find the application file and run it to begin the install

> Figure 34: Application File

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/041.png)

4.  Agree to the License terms and conditions and click Install

> Figure 35: Microsoft .NET Framework 4.6.2 License Terms

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/042.png)

5.  The update will begin installation

> Figure 36: Microsoft .NET Framework 4.6.2 Installer

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/043.png)

6.  Once installation is complete, you must click Restart

> Figure 37: .NET Framework 4.6.2 Installation Complete

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/044.png)

### Java Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Validate the specific patch description document for the current version of Java. If the server has a different version of Java than the required version specified in patch description, the wizard will install/uninstall the Java version.

## Updating the HDIG

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Go to the Control Panel, choose Add/Remove Programs, and remove the current version of the HDIG instance.

> Figure 38: Uninstall Programs in the Control Panel (Windows 2012 R2)

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/045.png)

1.  At the Update HDIG Components screen, click the Uninstall version 30.XXX.X.X button to remove the previous version of the HDIG.

> Figure 39: Uninstall Confirmation

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/046.png)

2.  At the Specify the VA site that the HDIG will service screen, enter the Site Number of the site where the HDIG service is installed, then click Lookup Server Addresses.

> Figure 40: Specify the VA Site the HDIG Will Service Dialog Box

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/047.png)

3.  Click Next. The DICOM Configuration screen opens.

> Figure 41: Specifying the DICOM Configuration

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/048.png)

4.  Click Next. The Install the HDIG Prerequisites screen opens. Items with a green check are successfully installed. Items with a red X require installation. Click the Install button next to each one in order. This portion of the installation may take 15-20 minutes. For more information on prerequisites, refer to the Running the HDIG Installer section above.

    Note: After Installing Java and BEFORE Installing Apache:

> In some cases, it was observed that old Apache entries were not removed from the Windows Registry Editor (regedit).

> BEFORE PROCEEDING TO INSTALL THE NEWEST APACHE TOMCAT VERSION, please RUN “regedit” and “RIGHT-CLICK + DELETE” the entries for previous versions of Apache under the HKEY_LOCAL_MACHINE \> SOFTWARE \> APACHE SOFTWARE FOUNDATION \> TOMCAT folder. For more information please contact the CLIN3 help desk.

> Figure 42: Tomcat 6.0

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/049.png)

> Figure 43: Required HDIG Prerequisites

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/050.png)

5.  When all the prerequisite installations have completed, the Next button is enabled. Click Next.

> Figure 44: Completed Install the HDIG Prerequisites Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/051.png)

6.  Specify the location of the HDIG cache and configuration folders. Click Next.

> Figure 45: Specify the Location of the HDIG Page

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/052.png)

7.  The Install the HDIG screen opens. Click Install.

> Figure 46: HDIG Installation Complete

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/053.png)

# HDIG Post-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides information about the additional steps you must perform after installing the software.

After installing the patches, you must perform these steps:

1.  Verify antivirus scan exclusions for designated directories.
2.  Verify the memory allocated to the HDIG. (For DICOM Gateways with RAM of 2 GB.)
3.  Starting image processing on the legacy Image Gateways by running option 2-3.
4.  Review the HDIG Stat Page for each image-processing server.
5.  Review the HDIG Logs.
6.  Check for emails from the server notification service.
7.  If you plan to import studies from outside locations over the network, you must configure an Outside Location.

## Configuring the HDIG 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing the HDIG, there are several configuration steps required, to be followed by multiple steps to test and verify the HDIG is working properly.

### Verify Antivirus Scanning Exclusions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify the following exclusions to the antivirus scanning application definitions:

C:\DICOM\VixCache

C:\DICOM\Image_In

C:\DICOM\Image_Out

> **NOTE:** if the default drive of C was not used, change the designation of the drive where these directories reside.

The exclusions should also be applied on the root directory of each drive that hosts an image share. For example, G:\\

### Increasing the Memory Allocated to the HDIG 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On DICOM Gateways with RAM of 2 GB or less, you must increase the memory allocated to the HDIG (Apache Tomcat 8) service, because the processing of some DICOM datasets (mostly of new SOP Classes or new modality devices) requires a lot of memory. Increasing the memory may have a slight impact on the HDIG performance, but it will reduce the risk of failure due to insufficient memory (not having enough Java Heap Space).

To Upgrade the Memory on the Tomcat Application Server:

1.  Check the total memory allocated to the server by going to “Control Panel” \> “System”.
2.  Stop the Apache Tomcat server by selecting “Services”.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/054.png)

3.  Open the command prompt “as Administrator”.
4.  If Tomcat’s version is 8.0, execute the following steps:
    1.  Run the following command within the command prompt window

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/055.png)

> Tomcat8w //ES/Tomcat8

2.  Once the popup has opened, click on “Java”
3.  If the total memory or RAM on the server is 8GB, please add the following parameters under the existing parameters in the popup window (Maximum size allowed for a transfer file has been tested at 750MB).

> From:

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/056.png)

> To:

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/057.png)

-Xms2048M

-Xmx6144M

-XX:PermSize=512M

-XX:MaxPermSize=1024M

4.  If the total memory or RAM on the server is 4GB, add the following parameters under existing parameters within the popup window (Maximum size allowed for a transfer file has been tested at 500MB).

> From:

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/058.png)

> To:

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/059.png)

> -Xms2048M

> -Xmx3072M

> -XX:PermSize=512M

-XX:MaxPermSize=1024M

5.  Click Apply and OK.
6.  Start the Apache Tomcat server

### Email Notifications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two types of email notifications sent by the HDIG: ERROR email notifications and WARNING email notifications. The HDIG handles the two notifications differently.

### Error Messages and Email Handling 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system has a pre-configured time period for checking to see if there are any error messages to be sent (The system default is 60 seconds.). At the end of the specified time period, if there are any error messages to be sent, they are bundled and sent as one email.

### Warning Message Bundling for Email Handling 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two thresholds that are checked when determining when to send a warning email bundle. These two thresholds are email count and email bundle size. Whichever of the two conditions are satisfied first, triggers the sending of an email.

The email count threshold has a system default of 100. Warning messages are bundled into groups of 100 email messages. Each time the configured threshold is met, an email is sent to the email address configured in the legacy gateway with all of the warnings.

A second threshold, the email bundle size is also checked. The system default is that the email bundle should not exceed 5MB in size. If there are large warning email messages and this 5MB threshold is reached before the email bundle reaches the email count threshold, the email bundle will be sent.

### Warning Email Handling Configuration Guidelines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The proper settings will make sure, that generated emails are not too frequent for the recipient(s) and not too large for the mail server in use. The recommendation is that you use the system defined defaults. However, you can adjust the default settings by editing

the NotificationEmailConfiguration.config XML file in the C:\VixConfig folder. (For assistance editing this XML file, please request assistance from the CLIN 3 team.) Guidelines for settings and behavior:

- If you want more warning messages bundled (less frequent emails), set xxx higher (default is 100).
- If your email server cannot handle 5MB emails, lower it to the accepted value (example; 1MB is 1\*1024\*1024=1048576). Lowering the bundle size will result in more frequent emails.

## Configure the HDIG for Each Image Processing Server 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify the HDIG Service Account Credentials 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the HDIG Stats Page; http://\<HDIG Hostname.Domain\>:8080/HDIGManagementWebApp/ViewHDIGStats.jsp Note: URLs are case sensitive

For first time installs, the screen will appear as follows:

2.  Click Update the HDIG service account credentials.

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/060.png)

3.  Enter the Access Code of the DICOM Gateway Service Account.
4.  Enter the Verify Code of the DICOM Gateway Service Account.

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/061.png)

After the credentials have been validated, the page will appear as follows:

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/062.png)

### Updating the HDIG Administrator Email Address(es) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Review the HDIG email address used to alert for invalid service account credentials by clicking on Update the Administrator email address(es) update if needed.

> Note: You must enter at least one email address in the field. If you want to enter more than one address, use a comma to separate the addresses.

2.  Verify the email address(es) by performing the following steps.
3.  Use CTRL^C to copy the email address from the HDIG page.
4.  Open your email client and initiate a new email.
5.  Use CTRL^V to paste the email address into the TO box of the email message.
6.  Type MAG\*3.0\*xxx Install Test email in the subject line.
7.  Send the email.
8.  Check your email inbox to verify you received the email.

### Save the HDIG Stat Page as the Home page 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Set the View HDIG Statistics page as the Microsoft Edge/Google Chrome Home page.
2.  Click Tools, then Internet Options.
3.  Under the Home page section, choose Use current, click Apply and then OK.

### Save the HDIG Logs Page as a favorite 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Access the HDIG Logs page; https://\<HDIG Hostname.Domain\>/Vix/ssl/JavaLogs.jsp Note: The HDIG logs are secured, to open the logs page enter the access and verify codes of a Vista account that holds the security key MAG VIX ADMIN.
2.  Click Favorites, then Add to Favorites.
3.  Name as \<server name\> HDIG Logs, click Add.

## Testing the HDIG Operation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Review the HDIG Stats Page for Each Image Gateway Server 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If not opened already, access the HDIG Stats Home page or http://\<HDIG Hostname.Domain\>:8080/HDIGManagementWebApp/ViewHDIGStats.jsp.
2.  Check for proper values in the Basic Information fields Hostname, Site Number, Site Name and Version \<30.136.35.3\>.
3.  Review the Inbound Activity section of the HDIG Stats Page to ensure all instruments on each specific gateway are listening on the proper ports as indicated in the INSTRUMENT.DIC file.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/063.png)

Starting image processing on the legacy Image Gateways by running option 2-3 Process DICOM Images.

### Test and Review HDIG and Legacy Image Processing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Begin a limited transmission of images to one or more image gateway servers.

1.  If not opened already, access the HDIG Stats Home page or http://\<HDIG Hostname.Domain\>:8080/HDIGManagementWebApp/ViewHDIGStats.jsp.
2.  Review the section Inbound Associations for processed and rejected data by AE\_ Title.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/064.png)

3.  Review the section Inbound DIMSE Messages for processed and rejected data by AE_Title.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/065.png)

4.  Review the section Inbound Objects for processed and rejected data by AE Title.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/066.png)

5.  Review the section Inbound Modality Devices for processed and rejected data, duplicate objects, and IOD violations, by modality.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/067.png)

6.  Review the legacy telnet window running the option 2-3 Process DICOM Images
7.  If not opened already, access the HDIG Logs page; https://\<HDIG

> Hostname\>/Vix/ssl/JavaLogs.jsp Note - the HDIG logs are secured, to open the logs page enter the access and verify codes of a Vista account that holds the security key

> MAG VIX ADMIN.

8.  Open and review the HDIGSummary.log for each image processing server to ensure there are not AE_Title’s incorrectly configured (or missing) in the DICOM AE SECURITY MATRIX.

> Example entries indicating configuration problems:

1.  The Remote AE_Title, EYE6, does not have permission to access VistA Imaging. This permission is configurable using DICOM AE SECURITY MATRIX.
2.  The calling AE_Title, OTECH_QR, does not have permission to perform a CStore DIMSE Service. This permission is configurable using DICOM AE SECURITY MATRIX.
9.  Open and review the ImagingExchangeWebApp.log for ERROR messages.
10. Open and review the VistaRealm.log for domain and log-on errors.
11. Check other notification services, specifically the email notification account designated as the mail group in the legacy Gateway Configuration Parameters.

# Post-Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Complete Appendix D – Post-Install Checklist 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Print *Appendix D,Post-Install Checklist*.
2.  Complete the checklists.
3.  Document any issues or problems encountered for future installs/upgrades.
4.  File.

# Appendix A Activating the DCF Toolkit Product Serial Number 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Product Serial Numbers are required for each DCF toolkit installed at your site. Each product serial number is issued for a specific computer. You must activate each product serial number on each computer for the DICOM Listener instance to work on that computer.

You activate the product serial number when you run the HDIG installer. You activate the product serial number through the Laurel Bridge Web site. There are two types of activation depending on whether the computer can access the Laurel Bridge Web site directly through the Internet or not.

- Network activation – If the computer can connect to the Internet, you can activate the license using your network connection to the Internet.
- Manualactivation – If the computer is not on a network that connects to the Internet, you must activate the license manually.

## Network Activation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the computer on which you are running the installer is connected to the Internet and can access the Laurel Bridge Web site, you activate the DCF toolkit product serial number (license) automatically through the network.

To activate the DCF Toolkit license through the network:

1.  In the Requirements page of the HDIG installer, click Install next to the Laurel Bridge DCF Toolkit requirement to display the Activate DCF License dialog box.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/068.png)(Skip this step if the dialog box is displayed.)

> Post Installation

2.  Enter the following information in the Network Activation tab of the Activate DCF License dialog box:
    1.  \<*account*\> has Administrator role – This check verifies that an administrator account is being used. If not, cancel the installation and restart it using a Windows administrator account.
    2.  Product Serial Number – The serial number of the DCF toolkit. c Site – The name of your site. d Host – The name of the computer on which you are installing the DCF toolkit.

> e Number of CPUs – The number of CPUs on the computer on which you are installing the DCF toolkit. f Contact name – Your name.

> g Contact e-mail – Your e-mail address.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/069.png)

3.  Click Activate.
4.  The Status field displays a message about the status of the request.
5.  If there are errors and the request does not go through, the Messages field provides more details about the error.
6.  If the request is successful, the Status field displays the message Success and the activation code.
7.  If the request is successful, click the button Exit with success.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/070.png)

## Manual Activation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the computer on which you are running the HDIG installer is not connected to the Internet, you must activate the DCF toolkit product serial number (license) manually.

To activate the DCF Toolkit license manually:

1 In the Requirements page of the HDIG installer, click Install next to the Laurel Bridge DCF Toolkit requirement to display the Activate DCF License dialog box. (Skip this step if the dialog box is displayed.)

2 Click the Manual Activation tab.

> ![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/071.png)

1.  Copy the activation request code displayed in the Activation Request Code field.
2.  <span class="mark">REDACTED</span> .
3.  The VA License coordinator will then activate the product serial number through the Laurel Bridge Web site and e-mail you the activation code.
4.  Copy the activation code from the e-mail message and paste it in the Activation Code field.
7.  Click the Activate button.
8.  The Status field indicates that the activation was successful.

Click the Exit with success button.

# Appendix B The DICOM AE Security Matrix 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DICOM AE SECURITY MATRIX file (#2006.9192) includes the configuration settings of all remote devices that use DICOM services to connect to the VistA system. This includes devices that can send data to the VistA system, devices that can query the data stored in the VistA system, and devices that can retrieve images from the VistA system. The remote devices support these DICOM services. The DICOM services at each local site are identified with unique16-character strings called Application Entities (AE).

A remote device can have more than one DICOM service. For example, when a remote device stores images in VistA, the service associated with it is the storage service class (C-STORE). If the same device queries VistA, it uses the query service class (C-FIND). The device has a DICOM role associated with each service class. For example, a remote device that sends data to VistA is a service class user (SCU) of the storage service class

(C-STORE). VistA is a service class provider (SCP) of the storage service class (CSTORE). There can be devices at different locations with the same AE title, service, and role. However, the combination of the remote AE_Title, the service, role and site (location) number defines a device uniquely. AE Titles, per the DICOM Standard are a maximum of 16-character, unique alphanumeric strings per Application Entity. The DICOM AE SECURITY MATRIX and HDIG implementation for AE titles is not case sensitive.

MAG\*3.0\*79 introduced changes to the AE Security Matrix, which allows remote SCUs to issue Storage Commitment requests and also provide the information that the local SCP needs to return the response to the requesting SCU.

After installing the patch software, you must add an entry to the DICOM AE SECURITY MATRIX with the appropriate DICOM services and roles for each device at your site from which you want the DICOM Listener to receive data. If a device is not defined in the DICOM AE SECURITY MATRIX, it will not be able to send images or other data to the DICOM Listener and the data from the device will not be stored in the VistA system.

If you are using the Query/Retrieve application, you must also define all remote devices that can query and retrieve data from the VistA system in the DICOM AE SECURITY MATRIX.

The following figure illustrates the logical relationships of the DICOM services and roles. The image shows two devices that are configured to connect to the VistA system through the DICOM Gateways (Hybrid DICOM Image Gateways).

- An ultrasound device sending DICOM objects to the VistA system. The device is configured as a Service Class User of the C-STORE service (C-STORE SCU), which can send images to the DICOM Gateway (which is the C-STORE SCP for this device). The DICOM Listener on the DICOM Gateway is enabled. The DICOM Listener listens on a specific port for incoming DICOM objects from the ultrasound device, it processes the images and sends them to the VistA system. The DICOM Gateway is the Service Class Provider of the C-STORE service (C-STORE SCP).
- A 3-D reconstruction station is configured to query the VistA system through the Query/Retrieve application on the DICOM Gateway. The Query/Retrieve application is installed on the DICOM Gateway together with the DICOM Listener (which is a component of the HDIG). The 3-D reconstruction station is configured as a Service Class User of the C-FIND and the C-MOVE services (C-FIND SCU and C-MOVE SCU). The DICOM Gateway acts as the Service Class Provider of these services (CFIND SCP and C-MOVE SCP). Because the retrieved images are stored on the local disk, the 3-D reconstruction station is also defined as a Service Class Provider of the C-STORE service (C-STORE SCP). The DICOM Gateway acts as the Service Class User of the C-STORE service (C-STORE SCU).

> **NOTE:** Only the remote devices (the ultrasound device and the 3-D reconstruction station) are defined as entries in the DICOM AE SECURITY MATRIX. The local AE titles (the DICOM Listener and the Query/Retrieve application) are not separate entries in the DICOM AE SECURITY MATRIX, but part of the remote entry for each DICOM AE definition.

![](hybrid-dicom-image-gateway-hdig-installation-guide-revision-3-2/072.png)

DICOM Services and Roles

The DICOM AE SECURITY MATRIX contains an entry for importing studies from media using the DICOM Importer. If you plan to import studies from remote locations using a network connection or network drive, you must configure additional entries.

## Overview - Configuring the DICOM AE Security Matrix 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Entries for Storage Functionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must add an entry for each device at your site from which you want the DICOM Listener to receive data. If a device is not defined in the DICOM AE SECURITY MATRIX, it will not be able to send images or other data to the HDIG and the data from the device will not be stored in the VistA system.

Each device is a service class user (SCU) of the Storage service class (C-STORE). The DICOM Listener (which runs on the DICOM Gateway), is a service class provider (SCP) of the Storage service class (C-STORE).

### Entries for Query/Retrieve Functionality 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are using the Query/Retrieve application, you must also configure the remote devices that can query and retrieve images from the VistA database. The configuration of the devices that use Query/Retrieve to get information from VistA Imaging database is stored in the DICOM AE SECURITY MATRIX

- Each device is a service class user (SCU) of the C-MOVE and of the C-FIND service classes. The Query/Retrieve application (which runs on the DICOM Gateway) is the service class provider (SCP) of the C-MOVE and of the C-FIND service classes.
- Each device that stores the images it retrieves from the VistA database is also a service class provider (SCP) of the Storage service class (C-STORE). The Query/Retrieve application (which runs on the DICOM Gateway) is the service class user (SCU) of the storage service class (C-STORE). Thus, you must define each device that would store the retrieved images as a C-STORE SCP. The same device that is defined as a C-FIND SCU and a C-MOVE SCU, can also be defined as a CSTORE SCP, if the device stores the images it retrieves in a local directory.

### Entries for Import Functionality - Media 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the MAG\*3.0\*118 KIDS package is installed, a default entry is added to the DICOM AE SECURITY MATRIX file (#2006.9192). The entry has a REMOTE AE TITLE (field 1.1) called IMPORTER that is defined as a Service Class User of the CSTORE Service (C-STORE SCU). This entry allows the DICOM Importer to import data from media such as CDs, DVDs, thumb drives and the like. If you are importing studies from media (such as DVDs, CDs, thumb drives) and you are *not* importing studies over the network from an outside location, you can use the entry that has already been defined. You do not have to define additional entries.

### Entries for Import Functionality – Network Import 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are importing studies data over the network from an outside location, you must define additional entries. You should have an entry for every community-based outpatient clinic (CBOC) that sends studies to your VistA system over the network. If your site gets studies from multiple origins, you can define separate entries for each origin, such as VA, DoD, or commercial-based clinics or use the same entry for studies imported from multiple origins. The DICOM AE SECURITY MATRIX has a field called ORIGIN INDEX whose value indicates the origin of the study. If you choose not to define individual entries for every origin, you can set the value of this field to the most common origin and edit it later.

The DICOM AE SECURITY MATRIX file (#2006.9192) has a field called FORCE RECONCILIATION field(# 1.3). The value indicates whether the imported images are queued in the DICOM Importer queue for reconciliation or not. For devices that send studies through the network from an outside location, such as an ultrasound device in a Community-Based Outpatient Clinic (CBOC), set the value to YES. The images will be queued in the DICOM Importer queue to be reconciled manually. In all other cases, use the default value – NO.

## Fields in the DICOM AE SECURITY MATRIX 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DICOM AE SECURITY MATRIX file (#2006.9192) includes a listing of all the AE titles that are configured for the site and their configuration parameters. The following table provides information about the fields.

Fields in the DICOM AE SECURITY MATRIX file (#2006.9192)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 45%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Possible Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>AE NAME (#2006.9192,</p>
<p>.01)</p></td>
<td><blockquote>
<p>The name of the device. This is a unique descriptive name that allows you to identify the device. Example: <strong>CT 3<sup>rd</sup> Floor</strong>.</p>
</blockquote></td>
<td>This is a free text field 1-30 characters long.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 45%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Possible Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LOCAL AE TITLE</p>
<p>(#2006.9192, 1)</p></td>
<td><blockquote>
<p>The AE title of the local application entity that the remote device is accessing (local with respect to the VistA system at your site). For example, VISTA_STORAGE is the AE title of the DICOM Gateway to which remote devices send images to the VistA system.</p>
</blockquote></td>
<td><p>This is a free text field 1-16 characters long.</p>
<p>Use VISTA_STORAGE for devices that store data in the VistA system using the DICOM Gateway.</p>
<p>Use DICOM_QR for devices that use Q/R to query the VistA system.</p>
<p>Use IMPORTER for devices Import devices that connect to the network.</p></td>
</tr>
<tr class="even">
<td><p>REMOTE AE TITLE</p>
<p>(#2006.9192, 1.1)</p></td>
<td><blockquote>
<p>The AE title of the remote device (remote with respect to your VistA system). For example a device that sends images to the DICOM Gateway, or a device that queries the VistA database.</p>
</blockquote></td>
<td><p>This is a free text field 1-16 characters long.</p>
<p>The value must be specified and should not contain spaces.</p></td>
</tr>
<tr class="odd">
<td><p>FORCE</p>
<p>RECONCILIATION</p>
<p>(#2006.9192,1.3)</p></td>
<td><blockquote>
<p>This field is relevant only for the DICOM Import devices connected to the network. The value indicates whether the imported images are queued in the DICOM Importer queue for reconciliation or not.</p>
<p>For all other devices, use the default value – NO.</p>
</blockquote></td>
<td><p>NO</p>
<p>YES</p></td>
</tr>
<tr class="even">
<td><p>ORIGIN INDEX</p>
<p>(#2006.9192,1.4)</p></td>
<td><blockquote>
<p>This field is relevant only for the DICOM</p>
<p>Import devices connected to the network.</p>
</blockquote></td>
<td><p>V = VA (US Department of Veterans Affairs)</p>
<p>D = Department of</p>
<p>Defense</p>
<p>F = FEE (Commercial institutions)</p>
<p>N = NON-VA origin</p>
<p>I = IHS Indian Health</p>
<p>Services</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 45%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Field</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Possible Values</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>SITE</p>
<p>(#2006.9192, 2)</p>
</blockquote></td>
<td><blockquote>
<p>The division or the site (for sites that are not part of a division) in which the device resides.</p>
</blockquote></td>
<td><blockquote>
<p>The name of the division</p>
<p>(site) or its number in the INSTITUTION file (#4): the file that contains a listing of VA institutions.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>IP ADDRESS</p>
<p>(#2006.9192, 3)</p>
</blockquote></td>
<td><blockquote>
<p>The IP address (or host name) of the device (remote AE title).</p>
<p>Only required for Q/R devices.</p>
</blockquote></td>
<td><blockquote>
<p>A string 1-30 characters long.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PORT NUMBER</p>
<p>(#2006.9192, 4)</p>
</blockquote></td>
<td><blockquote>
<p>The port number used to communicate with the device (remote AE title). Only required for Q/R devices</p>
</blockquote></td>
<td><blockquote>
<p>A number between 199999.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DICOM SERVICE</p>
<p>(#2006.919212, .01)</p>
</blockquote></td>
<td><blockquote>
<p>The DICOM Service Class of the device. Each device that sends data to the VistA system should be defined as a Service Class User</p>
<p>(SCU) of the Storage Service Class (C-STORE).</p>
<p>Each device that queries the VistA system should be defined as a Service Class User (SCU) of the C-FIND and the C-MOVE Service Classes.</p>
<p>If new DICOM Objects are sent to VistA</p>
<p>Imaging gateway, it should be defined as a Service Class User (SCU) of the Storage Service Class (C-STORE).</p>
<p>If the retrieved objects are stored on the devices local drive, it should also be defined as a Service Class Provider (SCP) of the Storage Service Class (C-STORE).</p>
</blockquote></td>
<td><blockquote>
<p>The valid values and their meaning are:</p>
</blockquote>
<ol type="1">
<li><p>= C-STORE (Storage)</p></li>
<li><p>= C-FIND (Query)</p></li>
<li><p>= C-MOVE (Retrieve)</p></li>
<li><p>= C-ECHO</p></li>
<li><p>=STORAGE</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DICOM ROLE</p>
<p>(#2006.919212, 1)</p>
</blockquote></td>
<td><blockquote>
<p>The DICOM role of the device. Each device is defined as a Service Class User (SCU) or a Service Class Provider (SCP) of a specific DICOM Service Class.</p>
<p>An SCU is the user of a DICOM service. For example, a device that sends data to the VistA system is an SCU for the C-STORE service.</p>
</blockquote></td>
<td><blockquote>
<p>The valid values and their meaning are:</p>
</blockquote>
<ol start="6" type="1">
<li><p>= SCU</p></li>
<li><p>= SCP</p></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 45%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Possible Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>SERVICE TYPE</p>
<p>(#2006.9192, 11)</p></td>
<td><blockquote>
<p>The type of service that generated the order with which the object is associated.</p>
</blockquote></td>
<td><p>RAD = Radiology</p>
<p>CON = Consult</p></td>
</tr>
<tr class="even">
<td><p>RELAX VALIDATION<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>(#2006.9192, 10)</p></td>
<td><blockquote>
<p>The value of this flag determines if the HDIG should relax validation for the object or perform full validation.</p>
<p>When this field is set to YES, the HDIG does not send error messages to the sending device when an object that passed basic validation fails the full IOD validation. The HDIG processes objects that pass the basic IOD validation, but fail the complete IOD validation and does not report the validation error to the sending device. When the</p>
<p>RELAX VALIDATION flag is set to NO, the HDIG rejects the object if the object fails the full IOD validation and reports the validation errors to the sending device.</p>
</blockquote></td>
<td><p>NO</p>
<p>YES</p></td>
</tr>
<tr class="odd">
<td><p>REJECT<sup>1</sup> (#2006.9192,</p>
<p>6)</p></td>
<td><blockquote>
<p>When the value is set to YES, the HDIG sends a Reject message to the device that sent the object every time an object is rejected because it failed basic IOD validation. When the flag is set to NO, the HDIG sends an Error message indicating that there is a problem in the processing flow, but without any other details.</p>
</blockquote></td>
<td><p>NO</p>
<p>YES</p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Indicates a flag relevant only for devices sending data to the DICOM Gateway.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 43%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><strong>Possible Values</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VALIDATE<sup>1</sup></p>
<p>(#2006.9192, 9)</p></td>
<td><blockquote>
<p>When the value is set to YES, the DICOM Listener performs full IOD validation. If the object fails full IOD validation, the HDIG checks the setting of the RELAX VALIDATION flag. If the RELAX VALIDATION flag is set to YES, the HDIG processes the object without rejecting it, as explained in the description of the RELAX VALIDATION flag. Otherwise, it rejects the object and sends a message. The setting of the REJECT flag determines the verbosity of the message.</p>
<p>If the VALIDATE flag is set to NO, the HDIG does not perform full IOD validation; it performs only basic IOD validation.</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>WARNING<sup>1</sup></p>
<p>(#2006.9192, 7)</p></td>
<td><blockquote>
<p>When the value is set to YES, the HDIG sends a message to the device that sent the object, every time the HDIG finds a duplicate or illegal UID. When the flag is set to NO, the HDIG sends a warning message indicating that there is a problem in the processing flow, but without any other details.</p>
</blockquote></td>
<td><p>NO</p>
<p>YES</p></td>
</tr>
<tr class="odd">
<td><p>RESERR<sup>1</sup> (#2006.9192,</p>
<p>8)</p></td>
<td><blockquote>
<p>When the RESERR flag is set to YES, the DICOM listener sends a message to the device that sent the object, every time the HDIG cannot store the object because of a problem with the resource (VistA database, RAID disk, or other storage resource), such as problems connecting to the resource, lack of disk space to store the object, and so on. When the flag is set to NO, the HDIG sends an Error message indicating that there is a problem in the processing flow, but without any other details.</p>
</blockquote></td>
<td><p>NO</p>
<p>YES</p></td>
</tr>
<tr class="even">
<td>N RESPONSE DELAY (#2006.9192, 13)</td>
<td>This is the number of minutes the HDIG will wait before responding to a DIMSE N-ACTION request from this Remote AE TITLE.  (MAG*3.0*79).</td>
<td>A number between 0 and 99999, 0 decimal digits.</td>
</tr>
<tr class="odd">
<td>N RESPONSE RETRIES (#2006.9192, 14)</td>
<td>This is the number of times an HDIG will attempt to re-deliver a DIMSE N-RESPONSE message to this Remote AE TITLE (MAG*3.0*79).</td>
<td>A number between 0 and 99999, 0 decimal digits.</td>
</tr>
</tbody>
</table>

### Example DICOM AE SECURITY MATRIX Values (partial) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 18%" />
<col style="width: 22%" />
<col style="width: 18%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Parameter</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Storage Device</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Q/R Device</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Network Importer</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AE NAME</td>
<td><blockquote>
<p>The name of the device.</p>
</blockquote></td>
<td><blockquote>
<p>CT 3<sup>rd</sup> Floor</p>
</blockquote></td>
<td><blockquote>
<p>QR 3D</p>
<p>Workstation</p>
</blockquote></td>
<td><blockquote>
<p>SLC_3<sup>rd</sup>_Party_PET</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>LOCAL AE</p>
<p>TITLE</p></td>
<td><blockquote>
<p>The AE title (name) of the local application entity (local to your VistA system) with which the device communicates.</p>
</blockquote></td>
<td><blockquote>
<p>VISTA_STORAGE</p>
</blockquote></td>
<td><blockquote>
<p>DICOM_QR</p>
</blockquote></td>
<td><blockquote>
<p>IMPORTER</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>REMOTE AE</p>
<p>TITLE</p></td>
<td><blockquote>
<p>The AE title of the device you are adding.</p>
</blockquote></td>
<td><blockquote>
<p><strong>CT_SCAN3</strong></p>
</blockquote></td>
<td><blockquote>
<p>QR_3D_WORK</p>
<p>ST</p>
</blockquote></td>
<td><blockquote>
<p>SLC_3<sup>rd</sup>_Party_PET</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>FORCE</p>
<p>RECONCILIA</p>
<p>TION</p></td>
<td><blockquote>
<p>Relevant for network import only.</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>NO</p>
</blockquote></td>
<td><blockquote>
<p>YES</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>ORIGIN</p>
<p>INDEX</p></td>
<td><blockquote>
<p>The origin (source) of the study.</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
<td><blockquote>
<p><em>&lt;Choose a value&gt;</em></p>
<p><em>DoD</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td>SITE</td>
<td><blockquote>
<p>The division or the site.</p>
</blockquote></td>
<td><blockquote>
<p><em>&lt;YourSite&gt;</em></p>
<p>Example: 660 for Salt Lake</p>
<p>City</p>
</blockquote></td>
<td><blockquote>
<p><em>&lt;YourSite&gt;</em></p>
</blockquote></td>
<td><blockquote>
<p><em>&lt;YourSite&gt;</em></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IP ADDRESS</td>
<td><blockquote>
<p>The IP address (or host name) of the device.</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
<td><blockquote>
<p>&lt;<em>QRWorstatio nIP</em>&gt;</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>PORT</p>
<p>NUMBER</p></td>
<td><blockquote>
<p>The port number used to connect to the remote device.</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
<td><blockquote>
<p>&lt;<em>3DWorkstati onPort#</em>&gt;</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Flags</td>
<td><blockquote>
<p>REJECT, WARNING</p>
<p>RESERR,</p>
<p>VALIDATE, RELAX</p>
<p>VALIDATION, SERVICE</p>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Select values based on your needs</p>
<p>YES</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
<td><blockquote>
<p>not used accept defaults</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **NOTE:** See the next section for defining DICOM Services and Roles.

### Adding Devices to the DICOM AE SECURITY MATRIX 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You must add an entry in the DICOM AE SECURITY MATRIX for each device

(AE_Title) that you want to store data in the VistA system or to query the VistA system. You add devices to the DICOM AE SECURITY MATRIX using VistA menu option Configure AE SECURITY MATRIX Settings \[MAGV AE SEC MX SETTINGS\] located on the Imaging System Manager Menu \[MAG SYS MENU\].

> **NOTE:** Bold in the screen samples indicates what you enter or select.

The following summarizes the objects you must define and their roles:

- Each device that sends data to the DICOM Gateway must be defined as a C-STORE SCU.
- Each device that queries the VistA system must be defined as a:
  - C-FIND SCU
  - C-MOVE SCU
  - C-STORE SCP (if the device stores the Q/R results on a local drive)
- Each DICOM Importer server instance that receives studies through the network from an outside location must be defined as a CSTORE SCU.
- To enable Storage Commitment for an SCU, the value STORAGE COMMIT has to be added to the entry’s DICOM SERVICE AND ROLE multiple field as an SCU.

To add devices to the DICOM AE SECURITY MATRIX file and set their properties:

1.  At the Select OPTION NAME prompt, enter Imaging System Manager Menu.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Log into VistA and choose the Imaging System Manager Menu [MAG SYS MENU] when prompted:</p>
<p>Select OPTION NAME: Imaging System Manager Menu</p>
<p>HL7 Imaging HL7 Messaging Maintenance ...</p>
<p>IX Image Index Conversion Menu ... LS Edit Network Location STATUS</p>
<p>TR Telereader Menu ...</p>
<p>Ad hoc Enterprise Site Report</p>
<p>Configure AE Security Matrix Settings</p>
<p>Delete Image Group</p>
<p>Delete Study by Accession Number</p>
<p>Enter/edit Reason</p>
<p>Imaging Database Integrity Checker Menu ...</p>
<p>Imaging Site Reports ...</p>
<p>Importer Menu ...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  Press \<Enter\> to proceed.
3.  When prompted with Select Imaging System Manager Menu Option: type Con and press \<Enter\> to select the option with Configure AE SECURITY MATRIX Settings. This option lets you add new devices to the DICOM AE SECURITY MATRIX and edit or delete existing ones.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Imaging System Manager Menu Option: Configure AE Security Matrix Settings</p>
<p>DICOM AE SECURITY MATRIX APPLICATION EDIT</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  To determine what devices have already been configured, type ? and press \<Enter\>. This displays the list of devices that have already been configured and their DICOM service and role as illustrated.

> Select DICOM AE SECURITY MATRIX AE NAME: ?

> Answer with DICOM AE SECURITY MATRIX NUMBER, or AE NAME:

> 1 IMPORTER SALT LAKE CITY IMPORTER

> C-STORE SCU

> You may enter a new DICOM AE SECURITY MATRIX, if you wish Answer must be 1-30 characters in length.

> Select DICOM AE SECURITY MATRIX AE NAME:

Adding a Storage Device

1.  Type the name of the device at the prompt and press \<Enter\> to proceed. The name can be descriptive. It can be 1-30 characters long and must be unique for every VistA system

> Select DICOM AE SECURITY MATRIX AE NAME:CT 3<sup>rd</sup> Floor

2.  Type YES when prompted to confirm the name of the device you are adding.

> Are you adding 'CT 3<sup>rd</sup> Floor' as

> a new DICOM AE SECURITY MATRIX (the 10TH)? No// YES (Yes)

3.  Define the site of your VistA system when prompted. You can define the location using the site number or the site name. Typically, you would be prompted with the default site location as illustrated in the following example. If you do not need to change it, press \<Enter\> to accept the default. If there are multiple sites that match the default string, you are prompted to select one of them. Select the desired site and press \<Enter\> to continue.

> DICOM AE SECURITY MATRIX SITE: 660//

1.  660 SALT LAKE CITY UT 660
2.  660AA SALT LAKE DOM UT VAMC 660AA

> CHOOSE 1-2: 1 SALT LAKE CITY UT 660

4.  Type the Remote AE_Title (the AE_Title of the device) at the prompt. The AE_Title can be a maximum of 16 characters , should NOT have spaces, and is not case sensitive.

> DICOM AE SECURITY MATRIX REMOTE AE TITLE: CT_SCAN3

5.  Press \<Enter\> to continue.
6.  Accept the default value – VISTA_STORAGE – and press \<Enter\> to continue.

> LOCAL AE TITLE: VISTA_STORAGE//

7.  Accept the default value, NO.

> FORCE RECONCILIATION: NO// NO

8.  Accept the default value, VA, only required for MAG\*3.0\*118 Importer devices.

> ORIGIN INDEX: V// VA

9.  For IP address press \<Enter\> to continue.

> Note: IP Address number are only required when configuring a device to use Query/Retrieve.

> IP ADDRESS:

10. For TCP port number press \<Enter\> to continue.

> Note: Port numbers are only required when configuring a device to use Query/Retrieve.

> PORT NUMBER:

11. Define the flags of the device when prompted. If you choose to change the default values of any of the flags *for the specific device*, follow the prompts.

> Note: The flag values are relevant only for devices that send images to the VistA system. If you are adding a device that queries the VistA system, accept the defaults.

- To accept the defaults, press \<Enter\>.
- To change the values of *any* of the flags, type NO and press \<Enter\>.

> Flag Names Flag Values

> -------------------------------

> REJECT YES

> WARNING YES

> RESERR YES

> VALIDATE YES

> RELAX VALIDATION YES

> SERVICE TYPE RADIOLOGY

> Accept these defaults? YES//

> Note: SERVICE TYPE can accept either RADIOLOGY or CONSULT

12. When prompted, define the DICOM service of the device and its role.

> Tip: You can enter ? to display the possible values.

> Select DICOM SERVICE: 1 (1 C-STORE)

> Are you adding 'C-STORE' as a new DICOM SERVICE (the 3RD for this DICOM AE

> SEC

> URITY MATRIX)? No// Y (Yes)

> DICOM ROLE: 2 SCP

> Select DICOM SERVICE: "C-STORE" (1 C-STORE)

> Are you adding 'C-STORE' as a new DICOM SERVICE (the 4TH for this DICOM AE

> SEC

> URITY MATRIX)? No// Y (Yes)

> DICOM ROLE: 2 SCU

13. When you define the DICOM role and service pair, you are prompted to define another DICOM service and role pair. Press \<Enter\> to continue.
14. Repeat this procedure to define the properties of all the storage devices that you want to add to the DICOM AE SECURITY MATRIX.

### Entries for Storage Commitment Requests 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enable Storage Commitment for an SCU, the value STORAGE COMMIT has to be added to the entry’s DICOM SERVICE AND ROLE multiple field as an SCU. In addition, the entry requires the definition of the host (IP address) and port, of the remote SCU, needed to accept the association made with reverse role negotiation.

Any SCU (that has not been configured) issuing a Storage Commitment request in the AE Security Matrix will receive a reject response for the N-ACTION request issued. The association for DICOM Storage Commitment will be accepted because it is controlled by the DICOM DCF_Toolkit Listen file used by the SCP. It is assumed that the SCU supports reverse role negotiation and is configured to accept an incoming association request.

In order to generate a meaningful Storage Commitment response for the sender, it is required that at least one remote C-MOVE SCU be defined in the DICOM AE SECURITY MATRIX (#2006.9192). This is because the entry’s local AE title is where the Storage Commitment response building module picks up the C-MOVE SCP AE (Retrieve AE Title) of the VistA system.

Example 1:

A *Storage Commitment SCU* entry with new field values and fields highlighted (N-Response-Delay is entered in minutes):

AE NAME: IVV-SCU LOCAL AE TITLE: VISTA_STORAGE

SITE: SALT LAKE CITY IP ADDRESS: REDACTED

PORT NUMBER: REDACTED REMOTE AE TITLE: IVV_SCU

FORCE RECONCILIATION: NO ORIGIN INDEX: VA

REJECT: YES WARNING: YES

RESERR: YES VALIDATE: NO

RELAX VALIDATION: YES SERVICE TYPE: RADIOLOGY

N RESPONSE DELAY: 2N RESPONSE RETRIES: 2

DICOM SERVICE: C-STORE DICOM ROLE: SCU

DICOM SERVICE: C-FIND DICOM ROLE: SCU

DICOM SERVICE: STORAGE COMMIT DICOM ROLE: SCUExample 2:

A *C-MOVE SCU* entry with needed field highlighted (used for Retrieve AE Title in DICOM Response message, so sender knows where to get committed item from):

AE NAME: QR LOCAL AE TITLE: DICOM_QR

SITE: SALT LAKE CITY REMOTE AE TITLE: QR_SCU

FORCE RECONCILIATION: NO ORIGIN INDEX: VA

REJECT: YES WARNING: YES

RESERR: YES VALIDATE: YES

RELAX VALIDATION: YES SERVICE TYPE: RADIOLOGY

DICOM SERVICE: C-MOVE DICOM ROLE: SCU

Adding a Query Retrieve Remote Device (MAG\*3.0\*116)

1.  Type the name of the device at the prompt and press \<Enter\> to proceed. The name can be descriptive. It can be 1-30 characters long and must be unique for every VistA system

> Select DICOM AE SECURITY MATRIX AE NAME:CT 3D Workstation

2.  Type YES when prompted to confirm the name of the device you are adding.

> Are you adding 'CT 3D Workstation ' as

> a new DICOM AE SECURITY MATRIX (the 12TH)? No// YES (Yes)

3.  Define the site of your VistA system when prompted. You can define the location using the site number or the site name. Typically, you would be prompted with the default site location as illustrated in the following example. If you do not need to change it, press \<Enter\> to accept the default. If there are multiple sites that match the default string, you are prompted to select one of them. Select the desired site and press \<Enter\> to continue.

> DICOM AE SECURITY MATRIX SITE: 660//

1.  660 SALT LAKE CITY UT 660
2.  660AA SALT LAKE DOM UT VAMC 660AA

> CHOOSE 1-2: 1 SALT LAKE CITY UT 660

4.  Type the Remote AE_Title (the AE_Title of the device) at the prompt. The AE_Title can be a maximum of 16 characters, should NOT have spaces, and is not case sensitive.

> DICOM AE SECURITY MATRIX REMOTE AE TITLE: CT_3D_Workstation

5.  Press \<Enter\> to continue.
6.  Change the default value – VISTA_STORAGE to DICOM_QR – and press \<Enter\> to continue.

> LOCAL AE TITLE: DICOM_QR//

7.  Accept the default value, NO.

> FORCE RECONCILIATION: NO// NO

8.  Accept the default value, V.

> ORIGIN INDEX: V// V

9.  For IP address, enter the IP Address or Host Name of the device and press \<Enter\> to continue.

> Note: IP Address number/Host Name are required when configuring a device to use Query/Retrieve.

> IP ADDRESS: 10.0.X.XXX

10. Type the TCP port number the remote device uses. Then press \<Enter\> to continue.

> Note: Port numbers are required when configuring a device to use Query/Retrieve.

> PORT NUMBER: 104

11. Define the flags of the device when prompted. Press \<Enter\> to accept the default values.

> Note: The flag values are relevant only for devices that send images to the VistA system. If you are adding a device that queries the VistA system, accept the defaults.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Flag Names Flag Values</p>
<p>-------------------------------</p>
<p>REJECT YES</p>
<p>WARNING YES</p>
<p>RESERR YES</p>
<p>VALIDATE YES</p>
<p>RELAX VALIDATION YES</p>
<p>SERVICE TYPE RADIOLOGY</p>
<p>Accept these defaults? YES//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

12. When prompted, define the DICOM service of the device and its role.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 32%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>DICOM Q/R Processing</strong></th>
<th><blockquote>
<p><strong>DICOM Service</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>DICOM Role</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Find</td>
<td><blockquote>
<p>C-FIND</p>
</blockquote></td>
<td><blockquote>
<p>SCU</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Retrieve</td>
<td><blockquote>
<p>C-MOVE</p>
</blockquote></td>
<td><blockquote>
<p>SCU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Workstation storage</td>
<td><blockquote>
<p>C-STORE</p>
</blockquote></td>
<td><blockquote>
<p>SCP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PACS storage</td>
<td><blockquote>
<p>C-STORE</p>
</blockquote></td>
<td><blockquote>
<p>SCU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>DICOM Storage Processing</strong></td>
<td><blockquote>
<p><strong>DICOM Service</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>DICOM Role</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Store</td>
<td><blockquote>
<p>C-STORE</p>
</blockquote></td>
<td><blockquote>
<p>SCU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Store</td>
<td><blockquote>
<p>C-STORE</p>
</blockquote></td>
<td><blockquote>
<p>SCP</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Storage commit</td>
<td><blockquote>
<p>STORAGE COMMIT</p>
</blockquote></td>
<td><blockquote>
<p>SCU</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **NOTE:** You can define two roles for the same DICOM service. To do so, use quotes when you specify the service the second time. The following screen example illustrates defining two roles for the same DICOM service: C-STORE SCP and C-STORE SCU

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select DICOM SERVICE: ??</p>
<p>You may enter a new DICOM SERVICE AND ROLE, if you wish</p>
<p>This is the DICOM service associated with this entry.</p>
<p>Choose from:</p>
<ol type="1">
<li><p>C-STORE</p></li>
<li><p>C-FIND</p></li>
<li><p>C-MOVE</p></li>
<li><p>C-GET</p></li>
<li><p>N-ACTION</p></li>
<li><p>N-CREATE</p></li>
<li><p>N-EVENT-REPORT</p></li>
<li><p>N-GET</p></li>
<li><p>N-SET</p></li>
<li><p>N-DELETE</p></li>
<li><p>C-ECHO</p></li>
</ol>
<p>Select DICOM SERVICE: 2 (2 C-FIND)</p>
<p>Are you adding 'C-FIND' as a new DICOM SERVICE (the 1ST for this DICOM AE</p>
<p>SECURITY MATRIX)? No// ????</p>
<p>Answer with 'Yes' or 'No'? yes (Yes)</p>
<p>DICOM ROLE: ??</p>
<p>This is the DICOM role, Service Class User (SCU) or Service Class Provider ( SCP), associated with the entry.</p>
<p>Choose from:</p>
<ol type="1">
<li><p>SCU</p></li>
<li><p>SCP</p></li>
</ol>
<p>DICOM ROLE: 1 SCU</p>
<p>Select DICOM SERVICE: 3 (3 C-MOVE)</p>
<p>Are you adding 'C-MOVE' as a new DICOM SERVICE (the 2ND for this DICOM AE SECURITY MATRIX)? No// yes (Yes)</p>
<p>DICOM ROLE: 1 SCU</p>
<p>Select DICOM SERVICE: 1 (1 C-STORE)</p>
<p>Are you adding 'C-STORE' as a new DICOM SERVICE (the 3RD for this DICOM AE SECURITY MATRIX)? No// yes (Yes)</p>
<p>DICOM ROLE: 1 SCU</p>
<p>Select DICOM SERVICE: "C-STORE" (1 C-STORE)</p>
<p>Are you adding 'C-STORE' as a new DICOM SERVICE (the 4TH for this DICOM AE SECURITY MATRIX)? No// y (Yes)</p>
<p>DICOM ROLE: 2 SCP</p>
<p>Select DICOM SERVICE: STORAGE COMMIT (5 STORAGE COMMIT)</p>
<p>Are you adding ‘STORAGE COMMIT’ as a new DICOM SERVICE (the 5TH for this DICOM AE SECURITY MATRIX)? No// y (Yes)</p>
<p>DICOM ROLE: 1 SCU</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Tip: You can enter ? to display the possible values.

13. When you define the DICOM role and service pair, you are prompted to define another DICOM service and role pair. If you need to define another DICOM service and role pair, follow the prompts. Otherwise, press enter to continue.
14. Repeat this procedure to define the properties of all Query/Retrieve devices that you want to add to the DICOM AE SECURITY MATRIX.
15. Press \<Enter\> to continue.

Adding an Importer Network Storage Device (MAG\*3.0\*118)

1.  Type the name of the device at the prompt and press \<Enter\> to proceed. The name can be descriptive. It can be 1-30 characters long and must be unique for every VistA system

> Select DICOM AE SECURITY MATRIX AE NAME:SLC_3<sup>rd</sup>\_Party_PET

2.  Type YES when prompted to confirm the name of the device you are adding.

> Are you adding ‘SLC_3<sup>rd</sup>\_Party_PET’ as

> a new DICOM AE SECURITY MATRIX (the 13TH)? No// YES (Yes)

3.  Define the site of your VistA system when prompted. You can define the location using the site number or the site name. Typically, you would be prompted with the default site location as illustrated in the following example. If you do not need to change it, press \<Enter\> to accept the default. If there are multiple sites that match the default string, you are prompted to select one of them. Select the desired site and press \<Enter\> to continue.

> DICOM AE SECURITY MATRIX SITE: 660//

1.  660 SALT LAKE CITY UT 660
2.  660AA SALT LAKE DOM UT VAMC 660AA

> CHOOSE 1-2: 1 SALT LAKE CITY UT 660

4.  Type the Remote AE_Title (the AE_Title of the device) at the prompt. The AE_Title can be a maximum of 16 characters, should NOT have spaces, and is not case sensitive.

> DICOM AE SECURITY MATRIX REMOTE AE TITLE: SLC_3<sup>rd</sup>\_Party_PET

5.  Press \<Enter\> to continue.
6.  Change the default value – VISTA_STORAGE – to - IMPORTER - and press \<Enter\> to continue.

> Note: IMPORTER is a default value in the DICOM AE SECURITY MATRIX.

> LOCAL AE TITLE: IMPORTER//

7.  Change the default value, NO to YES.

> FORCE RECONCILIATION: NO// YES

8.  Specify the value for the field ORIGIN INDEX.

> Note: Choices are:

> V = VA (US Department of Veterans Affairs)

> D = Department of Defense

> F = FEE (Commercial institutions) N = NON-VA origin

> I = IHS Indian Health Services

> ORIGIN INDEX: V// VA

9.  For IP address, press \<Enter\> to continue.

> Note: IP Address number are only required when configuring a device to use Query/Retrieve.

> IP ADDRESS:

10. For TCP port, press \<Enter\> to continue.

> Note: Port numbers are only required when configuring a device to use Query/Retrieve.

> PORT NUMBER:

11. Define the flags of the device when prompted. If you choose to accept the default values of any of the flags *for the specific device*, follow the prompts.

> Note: The flag values are relevant only for devices that send images to the VistA system.

> Note: Choices for SERVICE TYPE are RADIOLOGY or CONSULT.

- To accept the defaults, press \<Enter\>.
- To change the values of *any* of the flags, type NO and press \<Enter\>.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Flag Names Flag Values</p>
<p>-------------------------------</p>
<p>REJECT YES</p>
<p>WARNING YES</p>
<p>RESERR YES</p>
<p>VALIDATE YES</p>
<p>RELAX VALIDATION YES</p>
<p>SERVICE TYPE RADIOLOGY</p>
<p>Accept these defaults? YES//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

12. When prompted, define the DICOM service of the device and its role.

> Select DICOM SERVICE: 1 (1 C-STORE)

> Are you adding 'C-STORE' as a new DICOM SERVICE (the 3RD for this DICOM AE

> SEC

> URITY MATRIX)? No// Y (Yes)

> DICOM ROLE: 2 SCP

> Select DICOM SERVICE: "C-STORE" (1 C-STORE)

> Are you adding 'C-STORE' as a new DICOM SERVICE (the 4TH for this DICOM AE

> SEC

> URITY MATRIX)? No// Y (Yes)

> DICOM ROLE: 2 SCU

> Tip: You can enter ? to display the possible values.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select DICOM SERVICE: ?</p>
<p>You may enter a new DICOM SERVICE AND ROLE, if you wish</p>
<p>Select a DICOM Service.</p>
<p>Choose from:</p>
<ol type="1">
<li><p>C-STORE</p></li>
<li><p>C-FIND</p></li>
<li><p>C-MOVE</p></li>
<li><p>C-GET</p></li>
<li><p>N-ACTION</p></li>
<li><p>N-CREATE</p></li>
<li><p>N-EVENT-REPORT</p></li>
<li><p>N-GET</p></li>
<li><p>N-SET</p></li>
<li><p>N-DELETE</p></li>
<li><p>C-ECHO</p></li>
</ol>
<p>Select DICOM SERVICE: 2 (2 C-FIND)</p>
<p>Are you adding 'C-FIND' as a new DICOM SERVICE (the 1ST for this DICOM AE SECURITY MATRIX)? No// Y (Yes)</p>
<p>DICOM ROLE: ?</p>
<p>Select a DICOM Role. Choose from:</p>
<ol type="1">
<li><p>SCU</p></li>
<li><p>SCP</p></li>
</ol>
<p>DICOM ROLE: 1 SCU</p>
<p>Select DICOM SERVICE: 3 (3 C-MOVE)</p>
<p>Are you adding 'C-MOVE' as a new DICOM SERVICE (the 2ND for this DICOM AE</p>
<p>SECU</p>
<p>RITY MATRIX)? No// Y (Yes)</p>
<p>DICOM ROLE: 1 SCU</p>
<p>Select DICOM SERVICE: 1 (1 C-STORE)</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Are you adding 'C-STORE' as a new DICOM SERVICE (the 3RD for this DICOM AE

> SEC

> URITY MATRIX)? No// Y (Yes)

> DICOM ROLE: 2 SCP

> Select DICOM SERVICE:

13. When you define the DICOM role and service pair, you are prompted to define another DICOM service and role pair. If you need to define another DICOM service and role pair, follow the prompts. Otherwise, press \<Enter\> to continue.
14. Repeat this procedure to define the properties of all Network Storage devices that you want to add to the DICOM AE SECURITY MATRIX.

# Appendix C Pre-Install Checklist 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Site Info
    1.  Site Name:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    2.  Site Code:\_\_\_\_\_\_\_\_\_
    3.  Other Sites Supported:\_\_\_\_\_\_\_ \_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_
    4.  Site Contact Name: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    5.  Site Contact Phone:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    6.  Site Contact E-mail Address:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2.  Documentation Review Completed (Date):
    1.  Review related patch descriptions: \_\_\_\_\_\_\_\_\_\_\_\_
    2.  DICOM Gateway User Manual:\_\_\_\_\_\_\_\_\_\_\_\_
    3.  Appendix A of this document – Activating the DCF Toolkit

> Product Serial Number:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

4.  Appendix B of this document – The DICOM AE Security

> Matrix:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

5.  Review related user manuals:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3.  Do you have a VIX installed (YES/NO)? \_\_\_\_\_\_\_\_\_\_
4.  Are the prerequisite patches installed (YES/NO)?
5.  Do you have a Radiology Commercial PACS System (cPACS)?
    1.  Manufacturer: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    2.  Model:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    3.  Software Version:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    4.  Does it receive DICOM data directly from modalities or from VistA

> (Circle One): MODALITIES VISTA

6.  Did you request and receive Product Serial Numbers (PSN) from Laurel Bridge (YES/NO)? \_\_\_\_\_\_
7.  Dictionaries
    1.  Do all of your DICOM Gateways share a single set of dictionaries

> (YES/NO)?\_\_\_\_\_\_\_\_\_\_

2.  Copy of MODALITY.DIC provided (YES/NO)?\_\_\_\_\_\_\_\_\_
3.  Copy of INSTRUMENT.DIC provided (YES/NO)?\_\_\_\_\_\_\_\_\_
4.  What is the RPC VistA Server port number:\_\_\_\_\_\_\_\_\_\_\_
8.  What e-mail addresses will be used for gateway e-mail notifications?

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

9.  Was the .NET Framework 4.6.2 or above software able to be installed on all gateways (YES/NO)?\_\_\_\_\_\_\_\_\_\_

# Appendix D Post-Install Checklist 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 1\. KIDS install date: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> 2\. VistA System Configured:

1.  DICOM AE SECURITY MATRIX configured:\_\_\_\_\_\_\_\_\_\_\_\_\_\_
2.  What method was used to configure?: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
3.  IMAGING SITE PARAMETER file updated: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
4.  Users Configured:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
5.  Outside Locations configured:\_\_\_\_\_\_\_\_\_\_\_\_\_
3.  HDIG installed (Date): \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
4.  HDIG update verified by: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
5.  Gateway Install
    1.  Gateway(s) install date - start:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    2.  Gateway(s) install date - complete:\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    3.  Gateway update verified by: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    4.  Anti-virus exclusions configured: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    5.  Reviewed MODALITY.DIC file installed: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    6.  Reviewed INSTRUMENT.DIC file installed: \_\_\_\_\_\_\_\_\_\_\_\_\_
    7.  Legacy menu updates performed: \_\_\_\_\_\_\_\_\_\_\_\_
    8.  HDIG memory increased: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
    9.  Verified that each instrument on the gateway is storing images correctly: \_\_\_\_\_\_\_\_\_\_\_\_\_
    10. Verified new DICOM Correct is working for radiology: \_\_\_\_\_\_\_
    11. Verified new DICOM Correct is working for consults: \_\_\_\_\_\_\_\_
    12. Verified Query/Retrieve is working properly: \_\_\_\_\_\_\_\_\_\_\_\_\_
    13. Verified Query/Retrieve for NTP is working correctly: \_\_\_\_\_\_\_\_
    14. DICOM AE SECURITY MATRIX configuration verified via
    15. HDIG Summary Logs:\_\_\_\_\_\_\_\_\_\_\_
    16. HDIG Summary Log viewed for each HDIG: \_\_\_\_\_\_\_\_\_\_\_
    17. ImagingExchangeWebApp.log reviewed for each server? \_\_\_\_\_\_
    18. Gateway Inventory worksheet – Post Install completed: \_\_\_\_\_\_\_
6.  Importer III Desktop Client Install
    1.  User worksheet – Post Install configuration complete: \_\_\_\_\_\_\_\_\_
    2.  Workstation worksheet – Post Install configuration complete:\_\_\_\_\_\_\_\_\_\_\_\_
    3.  Users trained on software: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

# Appendix E DCF Toolkit Enterprise License Request Form 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Site Name: (example: Biloxi, MS)

Station Number: (as specified in the STATION NUMBER field 99 of the INSTITUTION file)

Contact Name: <u>.</u>

> E-mail: . Phone:

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Server Name</strong></th>
<th><p><strong># of</strong></p>
<p><strong>CPUs</strong></p></th>
<th><strong>Previous DCF?</strong></th>
<th><blockquote>
<p><strong>Product Serial Number</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

(Note 1: A CPU chip containing multiple hyper-threaded or multi-core processing elements is counted as a single CPU.) (Note 2: HP Sites - DL360 machines = 1 CPU, DL380 machines = 2CPUs)

(Note 3: Dell Sites - Normally only a single socket (Single socket = 1 CPU) is populated in the imaging servers but it is possible that this is not the case for all Dell systems in VHA. If you have questions call your DELL sales rep., and provide the service tag \# and S/N of the processor/server.