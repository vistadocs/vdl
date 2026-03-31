---
title: KAAJEE SSOWAP Installation Guide (8.0*791)
doc_type: IG
doc_label: Installation Guide
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
description: The purpose of this guide is to provide instructions for installing the Health<u>e</u>Vet-Veterans Health Information Systems and Technology Architecture (VistA) Kernel Authentication and Authorization for Java (2) Enterprise Edition Single SignOn Web Application Plugin (KAAJEE SSOWAP) and related s
audience: 
keywords: 
  - kaajee
  - table
  - contents
  - strong
  - server
  - software
  - application
  - installation
  - vista
  - ssowap
page_count: 0
word_count: 4998
section_count: 18
table_count: 44
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: May 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/KAAJEE/kaajee_ssowap_8_791_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/KAAJEE/kaajee_ssowap_8_791_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=151"
---

![](kaajee-ssowap-installation-guide-8-0-791/001.png)

KERNEL AUTHENTICATION & AUTHORIZATION FOR J2EE Single Sign-On Web Application Plugin (KAAJEE SSOWAP) VERSION 8.0.791FOR WEBLOGIC (WL) VERSIONS 12.2 AND HIGHERINSTALLATION GUIDE

May 2024

Office of Information and Technology

Product Development

*This page is left blank intentionally.*

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Figures](#figures)
- [Tables](#tables)
- [Orientation](#orientation)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Purpose](#purpose)
  - [Distribution Files](#distribution-files)
  - [Application Server Environment Requirements](#application-server-environment-requirements)
- [Installation Overview](#installation-overview)
  - [VistA M Server](#vista-m-server)
  - [WebLogic Server](#weblogic-server)
  - [Deploy a J2EE Web-Based Application with the KAAJEE SSOWAP "Plug-In"](#deploy-a-j2ee-web-based-application-with-the-kaajee-ssowap-plug-in)
- [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)
  - [Confirm/Obtain VistA M Server Distribution Files (recommended)](#confirmobtain-vista-m-server-distribution-files-recommended)
  - [Site Configuration (required)](#site-configuration-required)
    - [Validate User Division Entries](#validate-user-division-entries)
    - [Validate Institution Associations](#validate-institution-associations)
  - [Do Not Run any KAAJEE-based Software During the Installation (recommended)](#do-not-run-any-kaajee-based-software-during-the-installation-recommended)
  - [Verify KIDS Install Platform (required)](#verify-kids-install-platform-required)
  - [Retrieve and Install the KAAJEE-related VistA M Server Patch (required)](#retrieve-and-install-the-kaajee-related-vista-m-server-patch-required)
  - [Configure the security certificate on the WebLogic Server (required)](#configure-the-security-certificate-on-the-weblogic-server-required)
  - [Configure SDS 19.0 (or higher) JDBC Connections with the WebLogic Server (required)](#configure-sds-190-or-higher-jdbc-connections-with-the-weblogic-server-required)
  - [Ensure the Existence of, or Creation,](#ensure-the-existence-of-or-creation)
  - [of a SSOWAPUSER with Administrative Privileges (required)](#of-a-ssowapuser-with-administrative-privileges-required)
  - [Edit the KAAJEE Configuration File (required)](#edit-the-kaajee-configuration-file-required)
    - [Locate the kaajeeConfig.xml File (required)](#locate-the-kaajeeconfigxml-file-required)
    - [Edit the Station Number List in the kaajeeConfig.xml File](#edit-the-station-number-list-in-the-kaajeeconfigxml-file)
    - [Redeploy and Test the Web Application with the Updated kaajeeConfig.xml File (required)](#redeploy-and-test-the-web-application-with-the-updated-kaajeeconfigxml-file-required)
  - [(Linux/Windows) Configure log4j for All J2EE-based Application Log Entries (required)](#linuxwindows-configure-log4j-for-all-j2ee-based-application-log-entries-required)
    - [Configure Application for log4j](#configure-application-for-log4j)
Documentation Revisions
The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.
<span id="_Toc44314849" class="anchor"></span>Table i. Documentation revision history
<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 59%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
<tr class="odd">
<th>05/2024</th>
<th><p>Updated version of KAAJEE SSOWAP</p>
<p><strong>KAAJEE SSOWAP patch, XU*8.0*791</strong></p></th>
<th><mark>REDACTED</mark></th>
</tr>
<tr class="header">
<th>12/2021</th>
<th><p>New version of KAAJEE SSOWAP for WL 12/2/Java 8</p>
<p><strong>KAAJEE SSOWAP patch, XU*8.0*747,</strong> makes Technical Reference Model (TRM) compliance changes and upgrades/certification of a KAAJEE Single Sign-On Web Application Plugin (SSOWAP) component for the WebLogic 12.2/Java 1.8 platform and above.</p></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/2021</td>
<td>WebLogic 12.2/Java 8 release.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/2020</td>
<td>Splitting information into new SSOWAP-focused documentation.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/2018</td>
<td><p>Updated software and documentation with TRM and Fortify compliance items.</p>
<p><strong>Software Version: 1.2.0.005</strong></p>
<p><strong>Kernel Patch: XU*8.0*695</strong></p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>03/2011</td>
<td><p>Software and documentation for KAAJEE 1.1.0.007 and KAAJEE Security Service Provider Interface (SSPI) 1.1.0.002, referencing VistALink 1.6 and WebLogic 10.3.6 and higher.</p>
<p><strong>Software Version: 1.1.0.007</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.1.0.002</strong></p>
<p><strong>Kernel Patch: XU*8.0*504</strong></p></td>
<td><ul>
<li><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>05/2006</td>
<td><p>Initial software and documentation for KAAJEE 1.0.0.019 and KAAJEE Security Service Provider Interface (SSPI) 1.0.0.010, referencing VistALink 1.5 and WebLogic 8.1.</p>
<p><strong>Software Version: 1.0.0.019</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.0.0.010</strong></p>
<p>![](kaajee-ssowap-installation-guide-8-0-791/002.png) <strong>NOTE:</strong> For a description of the current KAAJEE software version numbering scheme, please review the readme.txt file distributed with the KAAJEE software.</p>
<blockquote>
<p>In the future, the Development Technology Advisory Committee (DTAC) will be the authoritative source for determining future version numbering schemes for all Health<em><u>e</u></em>Vet-VistA software file and folder names.</p>
</blockquote></td>
<td><ul>
<li><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>
Patch Revisions
For a complete list of patches related to this software, please refer to the Patch Module on FORUM.
Contents

# Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the installation and use of KAAJEE and the functionality it provides for Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) software products.

The installation instructions for KAAJEE are organized and described in this guide as follows:

1.  Pre-Installation Instructions.
2.  Installation Overview
3.  VistA M Server Installation Instructions
4.  Java 2 Platforms, Enterprise Edition (J2EE) Application Server Installation Instructions

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/003.png)</td>
<td><p>Where necessary, separate steps for the following two supported operating systems are provided:</p>
<ul>
<li><p>Linux (i.e., Red Hat Enterprise ES 8.0 or higher)</p></li>
<li><p>Windows</p></li>
</ul></td>
</tr>
</tbody>
</table>

There are no special legal requirements involved in the use of KAAJEE.

This manual uses several methods to highlight different aspects of the material:

- Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

<span id="_Ref345831418" class="anchor"></span>Table ii. Documentation symbol/term descriptions

| Symbol                                                                                                                                            | Description                                                                                                                                                       |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/004.png)                                        | NOTE/REF: Used to inform the reader of general information including references to additional reading material.                                                   |
| ![](kaajee-ssowap-installation-guide-8-0-791/005.png)                                       | CAUTION or DISCLAIMER: Used to inform the reader to take special notice of critical information.                                                                  |
| ![](kaajee-ssowap-installation-guide-8-0-791/006.png) | UPGRADES/FIRST-TIME INSTALLATION: Used to denote Upgrade or First-time installation instructions only.                                                            |
| ![](kaajee-ssowap-installation-guide-8-0-791/007.png)                                                                                                     | Skip forward to the referenced step or procedure that is indicated.                                                                                                   |
| ![](kaajee-ssowap-installation-guide-8-0-791/008.png)                                                                                                     | Instructions that only apply to the Linux operating systems (i.e., Red Hat Enterprise ES 3.0 or higher) are set off and indicated with this Linux "Tux" penguin icon. |
|                                                                                                                                                       | Instructions that only apply to Microsoft Windows operating systems (i.e., Microsoft Windows 2000 or XP) are set off and indicated with this stylized "Windows" icon. |

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts and some software code reserved/key words will be bold typeface.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/009.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- Java software code, variables, and file/folder names can be written in lower or mixed case.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistALink—VistA M Server and Application Server software
- Linux (i.e., Red Hat Enterprise ES 7.0 or higher) or Microsoft Windows environment
- Java Programming languageJava 1.8 Standard Edition (J2SE) Java Development Kit (JDK, a.k.a. Java Software Development Kit \[SDK\])
- WebLogic 12.2 and higher—Application server
- Oracle Database 19*g*—Database (e.g., Security Service Provider Interface \[SSPI\] or Standard Data Services \[SDS\] 19.0 (or higher) database/tables)
- Oracle SQL\*Plus Software 13 (or higher)

This manual provides an overall explanation of the installation procedures and functionality provided by the Kernel Authentication & Authorization for J2EE Single Sign-On Web Application Plugin (KAAJEE SSOWAP) on Weblogic Application Server Versions 12.2 and higher software; however, no attempt is made to explain how the overall HealtheVet-VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere.

Reference Materials

Readers who wish to learn more about KAAJEE should consult the following:

- *Kernel Systems Management Guide*
- *VistALink Installation Guide*
- *VistALink System Management Guide*
- *VistALink Developer Guide*

Health*<u>e</u>*Vet-VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

Health*<u>e</u>*Vet-VistA documentation can be downloaded from the VHA Software Document Library (VDL) Web site:

> <http://www.va.gov/vdl/>

Health*<u>e</u>*Vet-VistA documentation and software can also be downloaded from the Enterprise Product Support (EPS) anonymous directories:

- Preferred Method download.vista.med.va.gov

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/010.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing the Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) Kernel Authentication and Authorization for Java (2) Enterprise Edition Single SignOn Web Application Plugin (KAAJEE SSOWAP) and related software.

KAAJEE SSOWAP is *not* an application, but a framework. Users of the software need to understand how it integrates in their working environment. Thus, installing KAAJEE SSOWAP means to understand what jars and files need to be put where and what are the configuration files that you need to have and edit.

KAAJEE SSOWAP provides secure two factor sign-on architecture for Health*<u>e</u>*Vet-VistA Web-based applications.

These Health*<u>e</u>*Vet-VistA Web-based applications are able to authenticate against Kernel on the VistA M Server via an Internet Browser on the client workstation and a middle tier application server (e.g., WebLogic).

## Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/011.png) | NOTE: Please refer to "Table 1‑1. Application server minimum software/network tools/documentation required for KAAJEE" for confirmation of all KAAJEE and related software and documentation files. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/012.png)</td>
<td><p><strong>REF:</strong> For the KAAJEE software preview/test release, all distribution files are available at the following Web address:</p>
<ul>
<li><blockquote>
<p>Preferred Method download.vista.med.va.gov</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Application Server Environment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/013.png) | NOTE: The information in this topic is directed at the systems management personnel responsible for maintaining the application servers. |

The following minimum software tools and files are required to install the KAAJEE software and documentation for application servers running KAAJEE-based Web applications:

<span id="_Ref193265772" class="anchor"></span>Table 1‑1. Application server minimum software/network tools/documentation required for KAAJEE

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Software/Configuration/<br />
Documentation</strong></th>
<th><strong>Version and Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td><p>One of the following operating systems:</p>
<ul>
<li><blockquote>
<p>Linux (i.e., Red Hat Enterprise ES 7.0 or higher)</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Application Server Software</td>
<td>WebLogic Versions 12.2 and higher application servers.</td>
</tr>
<tr class="odd">
<td>SSPI Software</td>
<td>KAAJEE SSPI 8.0.748 and above</td>
</tr>
<tr class="even">
<td>VistALink Software</td>
<td>Version 1.6.7</td>
</tr>
<tr class="odd">
<td>VistA Kernel Software</td>
<td>Patch XU*8*504</td>
</tr>
<tr class="even">
<td>KAAJEE_SSOWAP_8.0.791_RN.PDF</td>
<td><strong>Release Notes</strong> describes the changes to KAAJEE SSOWAP to include new features and enhancements.</td>
</tr>
<tr class="odd">
<td>KAAJEE_SSOWAP_8.0.791_IG.PDF</td>
<td><blockquote>
<p><strong>Installation Guide</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>KAAJEE_SSOWAP_8.0.791_DEPL.PDF</td>
<td><blockquote>
<p><strong>Deployment Guide</strong> outlines the details of KAAJEE-related software and gives guidelines on how the software is used within Health<em><u>e</u></em>Vet-Veterans Health Information Systems and Technology Architecture (VistA). It contains the User Manual, Programmer Manual, and Technical Manual information for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XU_8.0.791.zip</td>
<td><blockquote>
<p><strong>KAAJEE SSOWAP Software.</strong> The KAAJEE SSPI software download Zip file for installation on the application server.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XU_8.0.791.zip.MD5</td>
<td><blockquote>
<p><strong>KAAJEE SSOWAP Software Checksum.</strong> The MD5 checksum value for the KAAJEE SSPI software download Zip file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

*This page is left blank intentionally.*

# Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides an overview of the installation procedures for the Kernel Authentication and Authorization for Java (2) Enterprise Edition Single SignOn Web Application Plugin (KAAJEE SSOWAP). The chapters that follow address the specific installations that comprise KAAJEE:

- VistA M Server Installation Instructions

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/014.png) | NOTE: Instructions for the VistA M Server installation can also be found in the description for Kernel Patch XU\*8\*504, located in the Patch Module on FORUM. |

## VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8\*504 is the custodial patch for the M server installation of the KAAJEE SSOWAP software. In addition, ensure that the M server system is current with patches for KERNEL, VistALink, and Remote Procedure Call (RPC) Broker.

|                                                                                                                |                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/015.png) | NOTE: For information on the minimum software tools and files that are required to install the KAAJEE software, see the section titled "Application Server Environment Requirements" in this documentation. |

## WebLogic Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WebLogic server will need to be configured with a security identity certificate for the server and added to the keystore along with intermediary and root certificates.

## Deploy a J2EE Web-Based Application with the KAAJEE SSOWAP "Plug-In"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For details how to deploy a J2EE web-based application with the KAAJEE "plug-in," refer to the Kernel Authentication & Authorization for J2EE Single SignOn Web Application Plugin (KAAJEE SSOWAP) Deployment Guide for Weblogic Application Server Versions 12.2 and higher.

# VistA M Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation instructions in this section are directed at the Information Resource Management (IRM) staff located at a site and are applicable for the Test/Production accounts in the VistA Caché environment.

|                                                                                                                |                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/016.png) | NOTE: For additional information on the VistA M server installation of the KAAJEE software, see the description for Kernel Patch XU\*8\*504 located in the Patch Module on FORUM. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/017.png) | NOTE: For information on the minimum software tools and files required to install the KAAJEE software in its entirety (i.e., covering the Java 2 Enterprise Edition \[J2EE\] and VistA M installations), see the section titled "Application Server Environment Requirements" in this documentation. |

## Confirm/Obtain VistA M Server Distribution Files *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files and environment configuration are needed to install the Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE)-related VistA M Server software:

<span id="_Toc167776479" class="anchor"></span>Table 3‑1. KAAJEE-related VistA M Server distribution files and environment configuration

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>Minimum Software/Configuration</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2">Operating System Software</td>
<td>InterSystems Caché</td>
</tr>
<tr class="even">
<td colspan="2">Fully Patched M Accounts</td>
<td><p>You should have both a development Test account and a Production account for KAAJEE software.</p>
<p>The account(s) <em>must</em> contain the <em>fully</em> patched versions of the following software:</p>
<ul>
<li><p>Kernel 8.0</p></li>
<li><p>Kernel Toolkit 7.3</p></li>
<li><p>RPC Broker 1.1</p></li>
<li><p>VA FileMan 22.2</p></li>
<li><p>VistALink 1.6.7</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>VistALink Application Server Software</td>
<td>VistALink VistA Software</td>
<td></td>
</tr>
<tr class="even">
<td>Version 1.6.7</td>
<td>XOBV*1.6*7</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2">VistA Kernel Software</td>
<td>Patch XU*8*504</td>
</tr>
<tr class="even">
<td colspan="2">KAAJEE_SSOWAP_8.0.791_RN.PDF</td>
<td><strong>Release Notes</strong> describes the changes to KAAJEE SSOWAP to include new features and enhancements.</td>
</tr>
<tr class="odd">
<td colspan="2">KAAJEE_SSOWAP_8.0.747_IG.PDF</td>
<td><blockquote>
<p><strong>Installation Guide</strong> describes in detail the installation procedures for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2">KAAJEE_SSOWAP_8.0.747_DEPL.PDF</td>
<td><blockquote>
<p><strong>Deployment Guide</strong> outlines the details of KAAJEE-related software and gives guidelines on how the software is used within Health<em><u>e</u></em>Vet-Veterans Health Information Systems and Technology Architecture (VistA). It contains the User Manual, Programmer Manual, and Technical Manual information for KAAJEE.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/018.png)</td>
<td><p><strong>REF:</strong> For the KAAJEE software release, all distribution files, unless otherwise noted, are available for download from the Enterprise VistA Support (EVS) anonymous directories:</p>
<ul>
<li><blockquote>
<p>Preferred Method <mark>REDACTED</mark></p>
</blockquote></li>
</ul>
<blockquote>
<p>This method transmits the files from the first available FTP server.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Site Configuration *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The KERNEL SYSTEM PARAMETERS file (#8989.3) holds the site parameters for the installation of Kernel. This allows users to configure and fine tune Kernel for:

- Site-specific requirements and optimization needs.
- Health*<u>e</u>*Vet-VistA software application requirements.

Some parameters are defined by IRM during the Kernel software installation process (e.g., agency information, volume set multiple, default parameters). Other parameters can be edited subsequent to installation (e.g., spooling, response time, and audit parameters). Priorities can also be set for interactive users and for TaskMan. Defaults for fields (e.g., timed read, auto menu, and ask device) are defined for use when not otherwise specified for a user or device. The values in the KERNEL SYSTEM PARAMETERS file (#8989.3) can be edited with the Enter/Edit Kernel Site Parameters option \[XUSITEPARM\].

### Validate User Division Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During the authentication process for Web-based applications that are KAAJEE-enabled, KAAJEE displays a list of validated institutions to the user. KAAJEE uses the Standard Data Services (SDS) tables 13.0 (or higher) as the authoritative source to validate the list of station numbers that are stored in the \<login-station-numbers\> tag in the kaajeeConfig.xml file. After a user selects an institution from this validated list, the software follows the VistA authentication process (i.e., Kernel Signon).

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/019.png) | NOTE: The validation of the VistA institution occurs *before* the actual login to the VistA M Server, but *after* the user selects the Login button on the KAAJEE Web login page. The selected institution is checked against the SDS 19.0 (or higher) tables for an entry and a VistA Provider. Also, KAAJEE checks that an entry exists in the KAAJEE configuration file. |

The VistA authentication process (i.e., Kernel Signon) requires that each user be associated with at least one division/institution. The local DUZ(2) variable on the VistA M Server stores the Internal Entry Number (IEN) of the login institution. Entries in the DIVISION multiple (#16) in the NEW PERSON file (#200) permit users to sign onto the institution(s) stored in this field. If there are *no* entries in the DIVISION multiple (#16) of the NEW PERSON file (#200) for the user signing on, information about the login institution comes from the value in the DEFAULT INSTITUTION field (#217) in the KERNEL SYSTEM PARAMETERS file (#8989.3).

Therefore, sites running any application that is used to sign onto VistA *must* verify that the institution(s) are set up correctly for the application user, as follows:

- Multi-divisional Sites: The DIVISION multiple (#16) in the NEW PERSON file (#200) *must* be set up for all users. This assures that the application users have access to only those stations for which they are authorized.
- *Non*-multi-divisional Sites: Sites *must* verify that the value in the DEFAULT INSTITUTION field (#217) in the KERNEL SYSTEM PARAMETERS file (#8989.3) is correct.

### Validate Institution Associations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KAAJEE uses the Standard Data Services (SDS) tables 19.0 (or higher) as the authoritative source for institution data. Data in the ASSOCIATIONS Multiple field (#14) in the local site's INSTITUTION file (#4) is uploaded to FORUM, which is then used to populate the SDS tables. Thus, in order to sign onto VistA the data in the ASSOCIATIONS Multiple field (#14) *must* have correct information.

The ASSOCIATIONS Multiple is used to link groups of institutions into associations. The ASSOCIATIONS Multiple consists of the following subfields:

- ASSOCIATIONS (#.01)—This field is a pointer to the INSTITUTIONS ASSOCIATION TYPES file (#4.05).
- PARENT OF ASSOCIATION (#1)—This field points back to the INSTITUTION file (#4) to indicate the parent of the association. This field is cross-referenced to find the children of a parent for an association type.

In the ASSOCIATIONS Multiple, child facilities point to their administrative parent. All clinics point to a division parent, all divisions point to a primary facility parent, primary facilities point to an HCS parent or VISN parent. HCS entries point to a VISN parent. Thus, all parent relationships eventually resolve to a VISN. The first entry (IEN=1) in the ASSOCIATIONS Multiple references the VISN to which the division belongs, so that the PARENT OF ASSOCIATION field in that entry *must* point to a VISN in the INSTITUTION file (#4), and the second entry (IEN=2) references the actual parent of the current institution.

Therefore, sites running any application that is used to sign onto VistA *must* verify that the ASSOCIATION Multiple field (#14) in the INSTITUTION file (#4) has a file entry for their own institution (and all child divisions if it's a multi-divisional site), and make sure that it is set up correctly. If changes are needed, use the IMF edit option \[XUMF IMF ADD EDIT\] to update those entries.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/020.png)</td>
<td><p><strong>REF:</strong> For more information on the XUMF IMF ADD EDIT option as well as the ASSOCIATIONS Multiple and PARENT OF ASSOCIATION fields data requirements, please refer to the Institution File Redesign (IFR) supplemental documentation located on the VDL at the following Web address:</p>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Do Not Run any KAAJEE-based Software During the Installation *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No Health*<u>e</u>*Vet-VistA Web-based and KAAJEE-enabled software should be running while the KAAJEE installation on the VistA M Server is taking place.

## Verify KIDS Install Platform *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the Kernel Installation and Distribution System (KIDS) platform on your system is ready to install VistA M Server patches.

## Retrieve and Install the KAAJEE-related VistA M Server Patch *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8\*504 is the custodial patch for the M server installation of the KAAJEE software. All VistA M Server patches are distributed in Kernel 8.0 KIDS format. Follow the normal procedures to obtain and install released patches.

|                                                                                                                   |                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/021.png) | Make sure that the Kernel, Kernel Toolkit, RPC Broker, VA FileMan, and VistALink software is fully patched. Patches must be installed in their published sequence. |

|                                                                                                                |                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/022.png) | REF: For more information on these patches, please refer to the Patch Module on FORUM. |

|                                                                                                                   |                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/023.png) | Congratulations! You have now completed the installation of KAAJEE-related software on the VistA M Server. |

## Configure the security certificate on the WebLogic Server *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                       |                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/024.png) | UPGRADES: Skip this step if you have already configured the certificate and the keystore, unless it is specifically noted that changes are required in the KAAJEE SSOWAP software release e-mail or Web site. |

To configure the certificate, use the following steps:

1.  Obtain the identity certificate from the certificate authority at VA - yourServerCert.crt
2.  Obtain the intermediary and root certificates from the certificate authority at VA - DigiCert-Global-G2-TLS-RSA-SHA256-2020-CA1.cer and DigiCert-Global-Root-G2.cer in this example.
3.  Add the identity cert and the intermediary/root certs to the same keystore. Below are the sample commands:

> keytool -import -alias DigiCert-Global-Root-G2 -file DigiCert-Global-Root-G2.cer -keystore yourServerStore.jks -storepass XXX ;

> keytool -import -alias DigiCert-Global-G2-TLS-RSA-SHA256-2020-CA1 -file DigiCert-Global-G2-TLS-RSA-SHA256-2020-CA1.cer -keystore yourServerStore.jks -storepass XXX ;

> keytool -import -alias id -file yourServerCert.crt -keystore yourServerStore.jks -storepass XXX ;

4.  Take a note of the alias under which the identity cert has been imported.
5.  Install the yourServerStore.jks on the server by navigating to: [Home](http://vac20wbdweb810.web.vaec.va.gov:7001/console/console.portal?_nfpb=true&_pageLabel=HomePage1) \>[Summary of Environment](http://vac20wbdweb810.web.vaec.va.gov:7001/console/console.portal?_nfpb=true&_pageLabel=EnvironmentsSummaryPage) \>[Summary of Servers](http://vac20wbdweb810.web.vaec.va.gov:7001/console/console.portal?_nfpb=true&_pageLabel=CoreServerServerTablePage) \>ManagedServer001

> ![](kaajee-ssowap-installation-guide-8-0-791/025.png)

6.  Configure the identity certificate for mutual SSL connection with the STS service; use the same alias id you have entered on step 4:

> ![](kaajee-ssowap-installation-guide-8-0-791/026.png)

7.  Make sure the Use Server Certs option is checked under the Advanced section:

> ![](kaajee-ssowap-installation-guide-8-0-791/027.png)

|                                                                                                                   |                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/028.png) | Congratulations! You have now completed the installation of identity and root certs on the WebLogic Server. |

## Configure SDS 19.0 (or higher) JDBC Connections with the WebLogic Server *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                       |                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/029.png) | UPGRADES: Skip this step if you have already configured the SDS tables, unless it is specifically noted that changes are required in the KAAJEE software release e-mail or Web site. |

To configure the Standard Data Services (SDS) tables for a J2EE DataSource, please refer to the "Configuring for a J2EE DataSource" topic in the *SDS API Installation Guide*.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/030.png)</td>
<td><p><strong>REF:</strong> The <em>SDS API Installation Guide</em> is included in the SDS software distribution ZIP files, which are available for download at the following Web address:</p>
<blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Ensure the Existence of, or Creation, 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## of a SSOWAP_USER with Administrative Privileges *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For KAAJEE to execute correctly, the files web.xml and weblogic.xml has content that declares that KAAJEE will run with the needed privileges.

Check that your WebLogic server already has a user named “SSOWAP_USER” and is part of the Administrators group, or it is part of the Admin global security role. If there is such a user, your installation of the KAAJEE enable web application will execute properly.

WebLogic Security Realm:

If you need to create a new user in WebLogic, ensure that

> 1\. It is named SSOWAP_USER

> 2\. It is assigned to the Administrators group

Active Directory Authentication Provider:

If your WebLogic domain has integrated an Active Directory authentication provider, and you will be creating the user in Active Directory, ensure that

> 1\. It is named SSOWAP_USER

> 2\. The user is part of a group that can be mapped in the WebLogic security realm to the Global Security Role named Admin.

The following shows the contents of the web.xml and weblogic.xml files as it pertains to the KAAJEE user.

|                                                                                                                |                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/031.png) | REF: See the KAAJEE Deployment Guide for the contents of the web.xml and weblogic.xml files and additional details. |

web.xml:

This file has a \<run-as\> tag, which causes it to run with the necessary administrative privileges. In addition, a corresponding security-role tag is defined. See the sample in Figure 3‑1.

<span id="_Ref202094452" class="anchor"></span>Figure 3‑1. Sample excerpt from a web.xml file—Using the run-as and security-role tags

> \<servlet\>

> \<servlet-name\>LoginController\</servlet-name\>

> \<servlet-class\>

> gov.va.med.authentication.kernel.servlet.ssowap.LoginController

> \</servlet-class\>

> \<run-as\>

> \<role-name\>adminuserrole\</role-name\>

> \</run-as\>

> \</servlet\>

> \<security-role\>

> \<role-name\>adminuserrole\</role-name\>

> \</security-role\>

weblogic.xml:

This file has a \<run-as\> tag, which causes it to run as an administrative user whose username is “KAAJEE.” In addition, a corresponding security-role tag is defined.

<span id="_Toc167776474" class="anchor"></span>Figure 3‑2. Sample excerpt from a weblogic.xml file—Using the run-as-role-assignment tag

> \<run-as-role-assignment\>

> \<role-name\>adminuserrole\</role-name\>

> \<run-as-principal-name\>SSOWAP_USER\</run-as-principal-name\>

> \</run-as-role-assignment\>

|                                                                                                                   |                                                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/032.png) | Important! The “SSOWAP_USER” user or alternate must exist in the WebLogic Application server and have system administration privileges. |

## Edit the KAAJEE Configuration File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Locate the kaajeeConfig.xml File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EMC, or Application Server Administrator, must first locate the kaajeeConfig.xml file in the Web application ear or standalone war file, as follows:

Exploded Ear Files

> Navigate to the WEB-INF directory in the sample application's exploded ear/war file—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

Ear Files

> 1\. Unzip the application's ear file—Explode the artifact.

> 2\. For any war file that implements KAAJEE authentication inside the ear file, unzip the war file.

> 3\. Navigate to the WEB-INF directory—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

Standalone War Files

> 1\. Unzip the application's war file that implements KAAJEE authentication.

> 2\. Navigate to the WEB-INF directory—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

The following is a sample excerpt of the kaajeeConfig.xml file as distributed with KAAJEE SSOWAP:

<span id="_Ref107708020" class="anchor"></span>Figure 3.9‑1. Sample Station Number excerpt of the kaajeeConfig.xml file

![](kaajee-ssowap-installation-guide-8-0-791/033.png)

### Edit the Station Number List in the kaajeeConfig.xml File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With KAAJEE SSOWAP station numbers are retrieved from the VA Provisioning Services dynamically.

No manual editing of station numbers the kaajeeConfig.xml file is required.

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/034.png) | NOTE: There is a new configuration setting being introduced: \<sts-service-address\> - this is a required setting and KAAJEE SSOWAP will not work without it. |

|     |     |
|-----|-----|
|     |     |

### Redeploy and Test the Web Application with the Updated kaajeeConfig.xml File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use WebLogic to redeploy the Web application ear or standalone war file with the updated kaajeeConfig.xml file on all appropriate application servers. Test the redeployed application.

Exploded Ear Files

> Leave application as an exploded ear file.

Packaged Ear Files

> 1\. Zip any unzipped war files that implements KAAJEE authentication into a war, replacing the old war file.

> 2\. Zip up the application ear file.

Standalone War Files

> Zip any unzipped war files into a war, replacing the old war file.

## (Linux/Windows) Configure log4j for All J2EE-based Application Log Entries *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                       |                                                                                                                                                                                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/035.png) | UPGRADES: Skip this step if you have already configured log4j *and* added the KAAJEE-specific logger information to the active log4j configuration file on the application server, unless it is specifically noted that changes are required in the KAAJEE software release e-mail or Web site. |

In order to provide a unified logger and consolidate all log/error entries into one file, all J2EE-based application-specific loggers *must* be added to the same log4j configuration file, which should be the active log4j configuration file for the server. After locating the active log4j configuration file used on the server you are configuring (e.g., mylog4j.xml file), add in the KAAJEE (and Fat-client Kernel Authentication and Authorization, or FatKAAT) loggers to that file.

To locate the active log4j configuration file, look for the"-Dlog4j.configuration=" argument in the startup script file (i.e., setDomainEnv.sh/.cmd). The "-Dlog4j.configuration=" should be set to the absolute location of the configuration file (e.g., c:/mydirectory/mylog4j.xml). If no such argument is present, look for a file named "log4j.xml" in a folder on the server classpath.

You *must* configure log4j for the first time, if all three of the following conditions exist:

- The "-Dlog4j.configuration=" argument does *not* exist in the WebLogic JVM startup script files.
- The "log4j.xml" file does *not* exist in the classpath.
- There is no pre-existing log4j configuration file in the folder placed on the classpath of the WebLogic Application Server containing the configuration files for all Health*<u>e</u>*Vet-VistA J2EE applications (e.g., \<HEV CONFIGURATION FOLDER\>).

For first time log4j configuration procedures, please refer to the "log4j Configuration File" topic in the *VistALink Installation Guide (1.6)*. Also, sample log4j configuration files are included with the VistALink 1.6 software distribution.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/036.png)</td>
<td><p><strong>REF:</strong> For more information on VistALink, please refer to the Application Modernization Foundations Web site located at the following Web address:</p>
<blockquote>
<p>http://vaww.vista.med.va.gov/vistalink</p>
</blockquote></td>
</tr>
</tbody>
</table>

Once the log4j file is initially configured, you need to configure the file specifically for KAAJEE log entries as outlined below.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-installation-guide-8-0-791/037.png)</td>
<td><p><strong>REF:</strong> For more information on log4j guidelines, please refer to the Application Structure &amp; Integration Services (ASIS) <em>Log4j Guidelines for HealtheVet-VistA Applications</em> document available at the following Web address:</p>
<blockquote>
<p>http://vista.med.va.gov/vistaarch/healthevet/Documents/Log4j%20Guidance%201.0.doc</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Configure Application for log4j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

KAAJEE SSOWAP has been updated with the log4j2 API. Follow the Log4J instructions (<https://logging.apache.org/log4j/log4j-2.1/manual/configuration.html>) to configure your application for Log4J.

|                                                                                                                   |                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-installation-guide-8-0-791/038.png) | Congratulations! You have now completed the installation and configuration of KAAJEE-related software on the WebLogic Application Server. |

#########  

*This page is left blank intentionally*.

######### Appendix A: Installation Back-Out or Roll-Back Procedure

J2EE Application Server

The Java component in KAAJEE SSOWAP is not a stand-alone Web application. It is an embedded set of Java components and a Java library to be embedded within a consuming Web application. Therefore, there is no back-out/roll-back procedure specific to KAAJEE SSOWAP. Each consuming application would have to devise their own back-out/roll-back procedure.

*This page is left blank intentionally.*