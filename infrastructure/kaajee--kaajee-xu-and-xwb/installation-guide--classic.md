---
consolidated_title: "kaajee classic installation guide"
app_code: KAAJEE
doc_type: IG
master_source: "KAAJEE Classic Installation Guide 1.2 (WebLogic 10.3.6 and WebLogic 12.1)"
master_pub_date: August 2020
consolidated_from: 2 versions
prior_versions:
  - "KAAJEE Classic Installation Guide"
---

> ![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/001.png)

> KERNEL AUTHENTICATION & AUTHORIZATION FOR J2EE (KAAJEE) VERSION 1.2.0

> FOR WEBLOGIC (WL) VERSIONS 10.3.6 AND HIGHER

> INSTALLATION GUIDE

> August 2020

> Department of Veterans Affairs Office of Information and Technology Product Development

> *This page is left blank intentionally.*

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
  - [Documentation Revisions](#documentation-revisions)
  - [Patch Revisions](#patch-revisions)
- [Contents](#contents)
- [Figures](#figures)
- [Tables](#tables)
- [Orientation](#orientation)
  - [How to Use this Manual](#how-to-use-this-manual)
  - [Assumptions About the Reader](#assumptions-about-the-reader)
  - [Reference Materials](#reference-materials)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Purpose](#purpose)
  - [Distribution Files](#distribution-files)
  - [Installer/Developer Notes—KAAJEE Software First-Time Installations and Upgrades](#installerdeveloper-noteskaajee-software-first-time-installations-and-upgrades)
  - [Application Server Environment Requirements](#application-server-environment-requirements)
- [Installation Overview](#installation-overview)
  - [VistA M Server](#vista-m-server)
  - [Deploy a J2EE Web-Based Application with the KAAJEE "Plug-In"](#deploy-a-j2ee-web-based-application-with-the-kaajee-plug-in)
- [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)
  - [Confirm/Obtain VistA M Server Distribution Files](#confirmobtain-vista-m-server-distribution-files)
    - [(recommended)](#recommended)
  - [Do Not Run any KAAJEE-based Software During the Installation (recommended)](#do-not-run-any-kaajee-based-software-during-the-installation-recommended)
  - [Retrieve and Install the KAAJEE-related VistA M Server Patch](#retrieve-and-install-the-kaajee-related-vista-m-server-patch)
    - [(required)](#required)
- [Application Server/Web Application configuration instructions](#application-serverweb-application-configuration-instructions)
  - [Configure SDS 18.0 (or higher) JDBC Connections with the WebLogic Server (required)](#configure-sds-180-or-higher-jdbc-connections-with-the-weblogic-server-required)
  - [Ensure the Existence of, or Create, a KAAJEE User with Administrative Privileges (required)](#ensure-the-existence-of-or-create-a-kaajee-user-with-administrative-privileges-required)
  - [KAAJEE Classic dependencies configuration/installation](#kaajee-classic-dependencies-configurationinstallation)
- [Appendix A: Installation Back-Out or Roll-Back Procedure](#appendix-a-installation-back-out-or-roll-back-procedure)
  - [VistA M Server](#vista-m-server-1)
  - [J2EE Application Server](#j2ee-application-server)

## Documentation Revisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

> <span id="_bookmark0" class="anchor"></span>Table i. Documentation revision history

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
</thead>
<tbody>
<tr class="odd">
<td>08/2020</td>
<td>Splitting the documentation for KAAJEE SSPI, KAAJEE Classic and KAAJEE SSOWAP up</td>
<td><p>Health Product Support (HPS)</p>
<p>REDACTED</p></td>
</tr>
<tr class="even">
<td>07/2018</td>
<td><p>Updated software and documentation with TRM and Fortify compliance items.</p>
<p><strong>Software Version: 1.2.0.005 Kernel Patch: XU*8.0*695</strong></p></td>
<td><p>Health Product Support (HPS)</p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td>03/2011</td>
<td><p>Software and documentation for KAAJEE 1.1.0.007 and KAAJEE Security Service Provider Interface (SSPI) 1.1.0.002, referencing VistALink 1.6 and WebLogic 10.3.6 and higher.</p>
<p><strong>Software Version: 1.1.0.007</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.1.0.002</strong></p>
<p><strong>Kernel Patch: XU*8.0*504</strong></p></td>
<td><p>Product Development Services Security Program HWSC development team.</p>
<p>Bay Pines, FL Office of Information Field Office (OIFO):</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2006</td>
<td><p>Initial software and documentation for KAAJEE 1.0.0.019 and KAAJEE Security Service Provider Interface (SSPI) 1.0.0.010, referencing VistALink 1.5 and WebLogic 8.1.</p>
<p><strong>Software Version: 1.0.0.019</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.0.0.010</strong></p>
<blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/002.png) <strong>NOTE:</strong> For a description of the current KAAJEE software version numbering scheme, please review the readme.txt file distributed with the KAAJEE software.</p>
<p>In the future, the Development Technology Advisory Committee (DTAC) will be the authoritative source for determining future version numbering schemes for all Health<em><u>e</u></em>Vet-VistA software file and folder names.</p>
</blockquote></td>
<td><p>ISS KAAJEE Development Team</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Patch Revisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  [Pre-Installation Instructions 1-1](#pre-installation-instructions)
    1.  [Purpose 1-1](#purpose)
    2.  [Distribution Files 1-1](#distribution-files)
    3.  [Installer/Developer Notes—KAAJEE Software First-Time Installations and Upgrades 1-1](#installerdeveloper-noteskaajee-software-first-time-installations-and-upgrades)
    4.  [Application Server Environment Requirements 1-2](#application-server-environment-requirements)
2.  [Installation Overview 2-1](#installation-overview)
    1.  [VistA M Server 2-1](#vista-m-server)
    2.  [Deploy a J2EE Web-Based Application with the KAAJEE "Plug-In" 2-1](#deploy-a-j2ee-web-based-application-with-the-kaajee-plug-in)
3.  [VistA M Server Installation Instructions 3-1](#vista-m-server-installation-instructions)
    1.  [Confirm/Obtain VistA M Server Distribution Files *(recommended)* 3-1](#confirmobtain-vista-m-server-distribution-files)
    2.  [Site Configuration *(required)* 3-2](#bookmark14)
        1.  [Validate User Division Entries 3-2](#validate-user-division-entries)
        2.  [Validate Institution Associations 3-3](#validate-institution-associations)
    3.  [Do Not Run any KAAJEE-based Software During the Installation *(recommended)* 3-4](#do-not-run-any-kaajee-based-software-during-the-installation-recommended)
    4.  [Verify KIDS Install Platform *(required)* 3-4](#bookmark18)
    5.  [Retrieve and Install the KAAJEE-related VistA M Server Patch *(required)* 3-4](#retrieve-and-install-the-kaajee-related-vista-m-server-patch)
[Application Server/Web Application configuration instructions 3-1](#application-serverweb-application-configuration-instructions)
[4 4-1](#application-serverweb-application-configuration-instructions)
1.  [Configure SDS 18.0 (or higher) JDBC Connections with the WebLogic Server *(required)* 4-1](#configure-sds-18.0-or-higher-jdbc-connections-with-the-weblogic-server-required)
2.  [Ensure the Existence of, or Create, a KAAJEE User with Administrative Privileges *(required)*4-1](#ensure-the-existence-of-or-create-a-kaajee-user-with-administrative-privileges-required) [4.3 Edit the KAAJEE Configuration File *(required)* 4-3](#bookmark26)
    1.  [Locate the kaajeeConfig.xml File *(required)* 4-3](#bookmark27)
    2.  [Edit the Station Number List in the kaajeeConfig.xml File *(required)* 4-4](#edit-the-station-number-list-in-the-kaajeeconfig.xml-file-required)
    3.  [Redeploy and Test the Web Application with the Updated kaajeeConfig.xml File](#redeploy-and-test-the-web-application-with-the-updated-kaajeeconfig.xml-file-required)
[*(required)* 4-5](#redeploy-and-test-the-web-application-with-the-updated-kaajeeconfig.xml-file-required)
4.  [KAAJEE Classic dependencies configuration/installation 4-5](#kaajee-classic-dependencies-configurationinstallation)
    1.  [ESAPI library dependencies 4-5](#cautionesapi-library-dependencies)
    2.  [(Linux/Windows) Configure log4j for All J2EE-based Application Log Entries](#linuxwindows-configure-log4j-for-all-j2ee-based-application-log-entries-required)
[*(required)* 4-6](#linuxwindows-configure-log4j-for-all-j2ee-based-application-log-entries-required)
3.  [Configure Application for log4j 4-7](#configure-application-for-log4j)
4.  [Edit the File Name and Location for All Log Entries 4-7](#edit-the-file-name-and-location-for-all-log-entries)
5.  [Add KAAJEE-specific Logger Tags 4-7](#add-kaajee-specific-logger-tags)
> [Appendix A: Installation Back-Out or Roll-Back Procedure 1](#appendix-a-installation-back-out-or-roll-back-procedure)

# Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Figure 4-34. Sample excerpt from a web.xml file—Using the run-as and security-role tags 4-2](#_bookmark24)

> [Figure 4-35. Sample excerpt from a weblogic.xml file—Using the run-as-role-assignment tag 4-2](#_bookmark25)

> [Figure 4.5-1. Sample Station Number excerpt of the kaajeeConfig.xml file 4-4](#_bookmark28)

> [Figure 4-37. Sample excerpt of the mylog4j.xml file—Editing common log file name and location](#_bookmark36) [(Windows) 4-7](#_bookmark36)

> [Figure 4-3. Sample excerpt of the mylog4j.xml file—Adding KAAJEE logger information 4-8](#_bookmark38)

# Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [Table i. Documentation revision history iii](#_bookmark0)

> [Table ii. Documentation symbol/term descriptions viii](#_bookmark1)

> [Table 1-1. Application server minimum software/network tools/documentation required for KAAJEE 1-2](#_bookmark7)

> [Table 3-1. KAAJEE-related VistA M Server distribution files and environment configuration 3-1](#_bookmark13)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Use this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Throughout this manual, advice and instructions are offered regarding the installation and use of KAAJEE and the functionality it provides for Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) software products.

> The installation instructions for KAAJEE are organized and described in this guide as follows:

1.  [Pre-Installation Instructions.](#pre-installation-instructions)
2.  [Installation Overview](#installation-overview)
3.  [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)
4.  Java 2 Platforms, Enterprise Edition (J2EE) Application Server Installation Instructions

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/003.png)</p>
</blockquote></th>
<th><blockquote>
<p>Where necessary, separate steps for the following two supported operating systems are provided:</p>
</blockquote>
<ul>
<li><blockquote>
<p>Linux (i.e., Red Hat Enterprise ES 6.0 or higher)</p>
</blockquote></li>
<li><blockquote>
<p>Windows</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> There are no special legal requirements involved in the use of KAAJEE.

> This manual uses several methods to highlight different aspects of the material:

- Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

> <span id="_bookmark1" class="anchor"></span>Table ii. Documentation symbol/term descriptions

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symbol</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/004.png)</p>
</blockquote></td>
<td><strong>NOTE/REF:</strong> Used to inform the reader of general information including references to additional reading material.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/005.png)</p>
</blockquote></td>
<td><strong>CAUTION or DISCLAIMER:</strong> Used to inform the reader to take special notice of critical information.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/006.png)</p>
</blockquote></td>
<td><strong>UPGRADES/FIRST-TIME INSTALLATION:</strong> Used to denote Upgrade or First- time installation instructions only.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/007.png)</p>
</blockquote></td>
<td>Skip forward to the referenced step or procedure that is indicated.</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/008.png)</p>
</blockquote></td>
<td>Instructions that only apply to the Linux operating systems (i.e., Red Hat Enterprise ES 3.0 or higher) are set off and indicated with this Linux "Tux" penguin icon.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Symbol</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/009.png)</p>
</blockquote></td>
<td><p>Instructions that only apply to Microsoft Windows operating systems</p>
<p>(i.e., Microsoft Windows 2000 or XP) are set off and indicated with this stylized "Windows" icon.</p></td>
</tr>
</tbody>
</table>

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
  - User's responses to online prompts and some software code reserved/key words will be bold typeface.
  - Author's comments, if any, are displayed in italics or as "callout" boxes.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/010.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> Callout boxes refer to labels or descriptions usually enclosed within a box,</p>
<p>which point to specific areas of a displayed image.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- Java software code, variables, and file/folder names can be written in lower or mixed case.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

## Assumptions About the Reader

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual is written with the assumption that the reader is familiar with the following:

- VistALink—VistA M Server and Application Server software
- Linux (i.e., Red Hat Enterprise ES 6.0 or higher) or Microsoft Windows environment
- ![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/011.png)Java Programming language Java 1.7 Standard Edition (J2SE) Java Development Kit (JDK,

> a.k.a. Java Software Development Kit \[SDK\])

- WebLogic 10.3.6 and higher—Application server
- Oracle Database 11*g*—Database (e.g., Security Service Provider Interface \[SSPI\] or Standard Data Services \[SDS\] 13.0 (or higher) database/tables)
- Oracle SQL\*Plus Software 11 (or higher)

> This manual provides an overall explanation of the installation procedures and functionality provided by the Kernel Authentication & Authorization for J2EE (KAAJEE) on Weblogic Application Server Versions 10.3.6 and higher software; however, no attempt is made to explain how the overall HealtheVet- VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the VA Intranet for a general orientation to HealtheVet-VistA at the following address:

> REDACTED

## Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Readers who wish to learn more about KAAJEE should consult the following:

- *Kernel Authentication & Authorization for J2EE (KAAJEE) Installation Guide (KAAJEE 1.2.0.xxx, & SSPI 1.2.0.xxx)*, this manual
- *Kernel Authentication & Authorization for J2EE (KAAJEE) Deployment Guide (KAAJEE 1.2.0.xxx, & SSPI 1.2.0.xxx)*
- KAAJEE Web site: REDACTED
- *Kernel Systems Management Guide*
- *VistALink Installation Guide*
- *VistALink System Management Guide*
- *VistALink Developer Guide*

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/012.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on VistALink, please refer to the Application Modernization Foundations Web site located at the following Web address:</p>
<p>REDACTED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Health*<u>e</u>*Vet-VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> [<u>http://www.adobe.com/</u>](http://www.adobe.com/)

> Health*<u>e</u>*Vet-VistA documentation can be downloaded from the VHA Software Document Library (VDL) Web site:

> [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

> Health*<u>e</u>*Vet-VistA documentation and software can also be downloaded from the Enterprise Product Support (EPS) anonymous directories:

- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

- Albany OIFO ftp://REDACTED
- Hines OIFO ftp://REDACTED
- Salt Lake City OIFO ftp://REDACTED

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/013.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links</strong></p>
<p><strong>are provided and are consistent with the stated purpose of this VA Intranet Service.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this guide is to provide instructions for installing the Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) Kernel Authentication and Authorization for Java (2) Enterprise Edition (KAAJEE) and related software.

> KAAJEE is *not* an application but a framework. Users of the software need to understand how it integrates in their working environment. Thus, installing KAAJEE means to understand what jars and files need to be put where and what are the configuration files that you need to have and edit.

> KAAJEE provides secure sign-on architecture for Health*<u>e</u>*Vet-VistA Web-based applications.

> These Health*<u>e</u>*Vet-VistA Web-based applications are able to authenticating against Kernel on the VistA M Server via an Internet Browser on the client workstation and a middle tier application server

> (e.g., WebLogic).

## Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/014.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> Please refer to "<a href="#_bookmark7">Table 1-1. Application server minimum software/network</a> <a href="#_bookmark7">tools/documentation required for KAAJEE</a>" for confirmation of all KAAJEE and related</p>
<p>software and documentation files.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/015.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For the KAAJEE software preview/test release, all distribution files are available at the following Web address:</p>
<p>REDACTED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installer/Developer Notes—KAAJEE Software First-Time Installations and Upgrades

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> First-time KAAJEE installers *must* perform *all* installation steps/procedures, except where noted. Those installation steps/procedures that can be skipped during a first-time installation will be displayed as follows:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/016.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>FIRST-Time INSTALLATION:</strong> <em>First-time installation-specific instructions or information that can be skipped will be found here.</em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> If you were a test site prior to the final release of KAAJEE, we have notated those installation steps/procedures that have special information based on the final software upgrades that may affect how you install the released version of KAAJEE or provide other pertinent information. The upgrade information will be displayed as follows:

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/017.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>UPGRADES:</strong> <em>Upgrade-specific instructions or information will be found here.</em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> In addition, we will use this section to also highlight any KAAJEE code changes from previous test/preview versions of the software to the released version of the software that may affect development teams coding KAAJEE-enabled applications.

## Application Server Environment Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/018.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> The information in this topic is directed at the systems management personnel</p>
<p>responsible for maintaining the application servers.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The following minimum software tools and files are required to install the KAAJEE software and documentation for application servers running KAAJEE-based Web applications:

> <span id="_bookmark7" class="anchor"></span>Table 1-1. Application server minimum software/network tools/documentation required for KAAJEE

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Software/Configuration/ Documentation</strong></th>
<th><strong>Version and Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td><p>One of the following operating systems:</p>
<ul>
<li><blockquote>
<p>Linux (i.e., Red Hat Enterprise ES 3.0 or higher)</p>
</blockquote></li>
<li><blockquote>
<p>Microsoft Windows XP or 2000</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>Application Server Software</td>
<td>WebLogic Versions 10.3 and higher application servers.</td>
</tr>
<tr class="odd">
<td>SSPI Software</td>
<td><p>KAAJEE SSPI 1.2.0.xxx</p>
<blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/019.png) <strong>REF:</strong> Installation and configuration instructions are included in the Chapter 3, "," in this manual.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VistALink Software</td>
<td>Version 1.6</td>
</tr>
<tr class="odd">
<td>VistA Kernel Software</td>
<td>Patch XU*8*504</td>
</tr>
<tr class="even">
<td>KAAJEE_CLASSIC_1_2_RN.PDF</td>
<td><p><strong>Release Notes</strong> describes the changes to KAAJEE</p>
<p>1.1 to include new features and enhancements.</p></td>
</tr>
<tr class="odd">
<td>KAAJEE_CLASSIC_1_2_IG.PDF</td>
<td><blockquote>
<p><strong>Installation Guide</strong>.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>KAAJEE_CLASSIC_1_2_DG.PDF</td>
<td><blockquote>
<p><strong>Deployment Guide</strong> outlines the details of KAAJEE- related software and gives guidelines on how the</p>
<p>software is used within Health<em>e</em>Vet-Veterans Health</p>
</blockquote></td>
</tr>
</tbody>
</table>

Pre-Installation Instructions

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Software/Configuration/ Documentation</strong></th>
<th><strong>Version and Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>Information Systems and Technology Architecture (VistA). It contains the User Manual, Programmer Manual, and Technical Manual information for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>kaajee_security_provider_1.2.0.xxx.zip</td>
<td><blockquote>
<p><strong>Security Provider Interface (SSPI) Software.</strong> The KAAJEE SSPI software download Zip file for installation on the application server.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>kaajee_security_provider_1.2.0.xxx.zip.MD5</td>
<td><blockquote>
<p><strong>Security Service Provider Interface (SSPI) Software Checksum.</strong> The MD5 checksum value for the KAAJEE SSPI software download Zip file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> *This page is left blank intentionally.*

# Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides an overview of the installation procedures for the Kernel Authentication and Authorization for Java (2) Enterprise Edition (KAAJEE). The chapters that follow address the specific installations that comprise KAAJEE:

- [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/020.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> Instructions for the VistA M Server installation can also be found in the description for Kernel Patch XU*8*504, located in the Patch Module on FORUM.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> •

## VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Kernel Patch XU\*8\*504 is the custodial patch for the M server installation of the KAAJEE software. In addition, ensure that the M server system is current with patches for KERNEL, VistALink, and Remote Procedure Call (RPC) Broker.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/021.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> For information on the minimum software tools and files that are required to install the KAAJEE software, see the section titled "<a href="#application-server-environment-requirements">Application Server Environment Requirements</a>" in this documentation.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Deploy a J2EE Web-Based Application with the KAAJEE "Plug-In"

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For details how to deploy a J2EE web-based application with the KAAJEE "plug-in," refer to the Kernel Authentication & Authorization for J2EE (KAAJEE) Deployment Guide for Weblogic Application Server Versions 10.3.6 and higher.

# VistA M Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The installation instructions in this section are directed at the Information Resource Management (IRM) staff located at a site and are applicable for the Test/Production accounts in the VistA Caché environment.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/022.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> For additional information on the VistA M server installation of the KAAJEE software, see the description for Kernel Patch XU*8*504 located in the Patch Module on FORUM.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/023.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> For information on the minimum software tools and files required to install the KAAJEE software in its entirety (i.e., covering the Java 2 Enterprise Edition [J2EE] and VistA M installations), see the section titled "<a href="#application-server-environment-requirements">Application Server Environment Requirements</a>" in this</p>
<p>documentation.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Confirm/Obtain VistA M Server Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following files and environment configuration are needed to install the Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE)-related VistA M Server software:

> <span id="_bookmark13" class="anchor"></span>Table 3-1. KAAJEE-related VistA M Server distribution files and environment configuration

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Minimum Software/Configuration</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td>InterSystems Caché</td>
</tr>
<tr class="even">
<td>Fully Patched M Accounts</td>
<td><p>You should have both a development Test account and a Production account for KAAJEE software.</p>
<p>The account(s) <em>must</em> contain the <em>fully</em> patched versions of the following software:</p>
<ul>
<li><blockquote>
<p>Kernel 8.0</p>
</blockquote></li>
<li><blockquote>
<p>Kernel Toolkit 7.3</p>
</blockquote></li>
<li><blockquote>
<p>RPC Broker 1.1</p>
</blockquote></li>
<li><blockquote>
<p>VA FileMan 22.2</p>
</blockquote></li>
<li><blockquote>
<p>VistALink 1.6</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VistALink Software</p>
</blockquote></td>
<td><blockquote>
<p>Version 1.6.1 (also listed above)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>VistA Kernel Software</p>
</blockquote></td>
<td><blockquote>
<p>Patch XU*8*504</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KAAJEE_1_2_RELEASENOTES.PD F</p>
</blockquote></td>
<td><blockquote>
<p><strong>Release Notes</strong> describes the changes to KAAJEE 1.2 to include new features and enhancements.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>KAAJEE_1_2_INSTALLGUIDE.PDF</p>
</blockquote></td>
<td><blockquote>
<p><strong>Installation Guide</strong> describes in detail the installation procedures for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>KAAJEE_1_2_DEPLOYGUIDE.PDF</p>
</blockquote></td>
<td><blockquote>
<p><strong>Deployment Guide</strong> outlines the details of KAAJEE-related software and gives guidelines on how the software is used</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Minimum Software/Configuration</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>within Health<em><u>e</u></em>Vet-Veterans Health Information Systems and Technology Architecture (VistA). It contains the User Manual, Programmer Manual, and Technical Manual information for KAAJEE.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/024.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For the KAAJEE software release, all distribution files, unless otherwise noted, are available for download from the Enterprise VistA Support (EVS) anonymous directories:</p>
</blockquote>
<ul>
<li><blockquote>
<p>/</p>
</blockquote></li>
<li><blockquote>
<p>Preferred Method REDACTED</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  <span id="bookmark14" class="anchor"></span>Site Configuration *(required)*

> The KERNEL SYSTEM PARAMETERS file (#8989.3) holds the site parameters for the installation of Kernel. This allows users to configure and fine tune Kernel for:

- Site-specific requirements and optimization needs.
- Health*<u>e</u>*Vet-VistA software application requirements.

> Some parameters are defined by IRM during the Kernel software installation process (e.g., agency information, volume set multiple, default parameters). Other parameters can be edited subsequent to installation (e.g., spooling, response time, and audit parameters). Priorities can also be set for interactive users and for TaskMan. Defaults for fields (e.g., timed read, auto menu, and ask device) are defined for use when not otherwise specified for a user or device. The values in the KERNEL SYSTEM PARAMETERS file (#8989.3) can be edited with the Enter/Edit Kernel Site Parameters option \[XUSITEPARM\].

#### Validate User Division Entries

> During the authentication process for Web-based applications that are KAAJEE-enabled, KAAJEE displays a list of validated institutions to the user. KAAJEE uses the Standard Data Services (SDS) tables

0.  (or higher) as the authoritative source to validate the list of station numbers that are stored in the

> \<login-station-numbers\> tag in the kaajeeConfig.xml file. After a user selects an institution from this validated list, the software follows the VistA authentication process (i.e., Kernel Signon).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/025.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> The validation of the VistA institution occurs <em>before</em> the actual login to the VistA M Server, but <em>after</em> the user selects the <strong>Login</strong> button on the KAAJEE Web login page. The selected institution is checked against the SDS 13.0 (or higher) tables for an entry and a VistA</p>
<p>Provider. Also, KAAJEE checks that an entry exists in the KAAJEE configuration file.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> VistA M Server Installation Instructions

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/026.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on the &lt;login-station-numbers&gt; tag and/or the kaajeeConfig.xml file, please refer to the "<a href="#bookmark26">Edit the KAAJEE Configuration File <em>(required)</em></a>" topic in the "," chapter</p>
<p>in this manual.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> The VistA authentication process (i.e., Kernel Signon) requires that each user be associated with at least one division/institution. The local DUZ(2) variable on the VistA M Server stores the Internal Entry Number (IEN) of the login institution. Entries in the DIVISION multiple (#16) in the NEW PERSON file (#200) permit users to sign onto the institution(s) stored in this field. If there are *no* entries in the DIVISION multiple (#16) of the NEW PERSON file (#200) for the user signing on, information about the login institution comes from the value in the DEFAULT INSTITUTION field (#217) in the KERNEL SYSTEM PARAMETERS file (#8989.3).

> Therefore, sites running any application that is used to sign onto VistA *must* verify that the institution(s) are set up correctly for the application user, as follows:

- Multi-divisional Sites: The DIVISION multiple (#16) in the NEW PERSON file (#200) *must* be set up for all users. This assures that the application users have access to only those stations for which they are authorized.
- *Non*-multi-divisional Sites: Sites *must* verify that the value in the DEFAULT INSTITUTION field (#217) in the KERNEL SYSTEM PARAMETERS file (#8989.3) is correct.

#### Validate Institution Associations

> KAAJEE uses the Standard Data Services (SDS) tables 13.0 (or higher) as the authoritative source for institution data. Data in the ASSOCIATIONS Multiple field (#14) in the local site's INSTITUTION file (#4) is uploaded to FORUM, which is then used to populate the SDS tables. Thus, in order to sign onto VistA the data in the ASSOCIATIONS Multiple field (#14) *must* have correct information.

> The ASSOCIATIONS Multiple is used to link groups of institutions into associations. The ASSOCIATIONS Multiple consists of the following subfields:

- ASSOCIATIONS (#.01)—This field is a pointer to the INSTITUTIONS ASSOCIATION TYPES file (#4.05).
- PARENT OF ASSOCIATION (#1)—This field points back to the INSTITUTION file (#4) to indicate the parent of the association. This field is cross-referenced to find the children of a parent for an association type.

> In the ASSOCIATIONS Multiple, child facilities point to their administrative parent. All clinics point to a division parent, all divisions point to a primary facility parent, primary facilities point to an HCS parent or VISN parent. HCS entries point to a VISN parent. Thus, all parent relationships eventually resolve to a VISN. The first entry (IEN=1) in the ASSOCIATIONS Multiple references the VISN to which the division belongs, so that the PARENT OF ASSOCIATION field in that entry *must* point to a VISN in the INSTITUTION file (#4), and the second entry (IEN=2) references the actual parent of the current institution.

> Therefore, sites running any application that is used to sign onto VistA *must* verify that the ASSOCIATION Multiple field (#14) in the INSTITUTION file (#4) has a file entry for their own

> institution (and all child divisions if it's a multi-divisional site), and make sure that it is set up correctly. If changes are needed, use the IMF edit option \[XUMF IMF ADD EDIT\] to update those entries.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/027.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on the XUMF IMF ADD EDIT option as well as the ASSOCIATIONS Multiple and PARENT OF ASSOCIATION fields data requirements, please refer to the Institution File Redesign (IFR) supplemental documentation located on the VDL at the following Web address:</p>
<p><a href="http://www.va.gov/vdl/application.asp?appID=9"><u>http://www.va.gov/vdl/application.asp?appID=9</u></a></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Do Not Run any KAAJEE-based Software During the Installation *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> No Health*<u>e</u>*Vet-VistA Web-based and KAAJEE-enabled software should be running while the KAAJEE installation on the VistA M Server is taking place.

3.  <span id="bookmark18" class="anchor"></span>Verify KIDS Install Platform *(required)*

> Verify that the Kernel Installation and Distribution System (KIDS) platform on your system is ready to install VistA M Server patches.

## Retrieve and Install the KAAJEE-related VistA M Server Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Kernel Patch XU\*8\*504 is the custodial patch for the M server installation of the KAAJEE software. All VistA M Server patches are distributed in Kernel 8.0 KIDS format. Follow the normal procedures to obtain and install released patches.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/028.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>Make sure that the Kernel, Kernel Toolkit, RPC Broker, VA FileMan, and VistALink software is fully patched. Patches must be installed in their published sequence.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/029.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on these patches, please refer to the Patch Module on FORUM.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/030.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>Congratulations! You have now completed the installation of KAAJEE-related software on the VistA M Server.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Application Server/Web Application configuration instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Configure SDS 18.0 (or higher) JDBC Connections with the WebLogic Server *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/031.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>UPGRADES:</strong> Skip this step if you have already configured the SDS tables, unless it is specifically noted that changes are required in the KAAJEE software release e-mail or Web site.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> To configure the Standard Data Services (SDS) tables for a J2EE DataSource, please refer to the "Configuring for a J2EE DataSource" topic in the *SDS API Installation Guide*.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/032.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> The <em>SDS API Installation Guide</em> is included in the SDS software distribution ZIP files, which are available for download at the following Web address:</p>
<p>REDACTED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Ensure the Existence of, or Create, a KAAJEE User with Administrative Privileges *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For KAAJEE to execute correctly, the files web.xml and weblogic.xml has content that declares that KAAJEE will run with the needed privileges.

> Check that your WebLogic server already has a user named “KAAJEE” and is part of the Administrators group, or it is part of the Admin global security role. If there is such a user, your installation of the KAAJEE enable web application will execute properly.

#### WebLogic Security Realm:

#### If you need to create a new user in WebLogic, ensure that

1.  It is named KAAJEE
2.  It is assigned to the Administrators group

#### Active Directory Authentication Provider:

#### If your WebLogic domain has integrated an Active Directory authentication provider, and you will be creating the user in Active Directory, ensure that

1.  It is named KAAJEE

#### The user is part of a group that can be mapped in the WebLogic security realm to the Global Security Role named Admin.

> The following shows the contents of the web.xml and weblogic.xml files as it pertains to the

> KAAJEE user.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/033.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> See the KAAJEE Deployment Guide for the contents of the web.xml and weblogic.xml files and additional details.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> web.xml:

> This file has a \<run-as\> tag, which causes it to run with the necessary administrative privileges. In addition, a corresponding security-role tag is defined. See the sample in [Figure 4-1.](#_bookmark24)

> <span id="_bookmark24" class="anchor"></span>Figure 4-1. Sample excerpt from a web.xml file—Using the run-as and security-role tags

> weblogic.xml:

> This file has a \<run-as\> tag, which causes it to run as an administrative user whose username is “KAAJEE.” In addition, a corresponding security-role tag is defined. See the sample in [Figure 4-4](#_bookmark36).

> <span id="_bookmark25" class="anchor"></span>Figure 4-2. Sample excerpt from a weblogic.xml file—Using the run-as-role-assignment tag

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/034.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>Important! The “KAAJEE” user or alternate must exist in the WebLogic Application server and have system administration privileges.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

1.  <span id="bookmark26" class="anchor"></span>Edit the KAAJEE Configuration File *(required)*
    1.  <span id="bookmark27" class="anchor"></span>Locate the kaajeeConfig.xml File *(required)*

> The EMC, or Application Server Administrator, must first locate the kaajeeConfig.xml file in the Web application ear or standalone war file, as follows:

####### Exploded Ear Files

> Navigate to the WEB-INF directory in the application's exploded ear/war file—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

####### Ear Files

1.  Unzip the application's ear file—Explode the artifact.
2.  For any war file that implements KAAJEE authentication inside the ear file, unzip the war file.
3.  Navigate to the WEB-INF directory—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

####### Standalone War Files

1.  Unzip the application's war file that implements KAAJEE authentication.
2.  Navigate to the WEB-INF directory—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

> The following is a sample excerpt of the kaajeeConfig.xml file as distributed with KAAJEE 1.1.0.007:

> <span id="_bookmark28" class="anchor"></span>Figure 4.3-1. Sample Station Number excerpt of the kaajeeConfig.xml file

> \<?xml version="1.0" encoding="UTF-8"?\>

> \<kaajee-config [xmlns:xsi="http://www.w3.org/2001/XMLSchema](http://www.w3.org/2001/XMLSchema-instance)-instance" xsi:noNamespaceSchemaLocation="kaajeeConfig.xsd"\>

> \<!-- host application name, used for login page display and logging --\>

> \<host-application-name\>KAAJEE Sample\</host-application-name\>

> \<!-- put each station number for KAAJEE login here --\>

> \<login-station-numbers\>

> \<station-number\>\###\</station-number\>

> \<station-number\>\###9XX\</station-number\>

> \<station-number\>\###9XX\</station-number\>

> \<station-number\>\###XX\</station-number\>

> \<station-number\>\###XX\</station-number\>

> \<station-number\>\###\</station-number\>

> \<station-number\>\###9XX\</station-number\>

> \<station-number\>\###9XX\</station-number\>

> \<station-number\>\###XX\</station-number\>

> \<station-number\>\###XX\</station-number\>

> \</login-station-numbers\>

> Users *must* initially configure this file to change these (placeholder) Station Numbers, as distributed with KAAJEE....

> \</kaajee-config\>

#### Edit the Station Number List in the kaajeeConfig.xml File *(required)*

> Use a text editor (e.g., Microsoft Notepad) or other xml editing software to open and edit the kaajeeConfig.xml file. The \<station-number\> tags control the Station Number list displayed to the end- user in KAAJEE's login Web page Institution drop-down list. In [Figure 4.3-1,](#_bookmark28) we represent the application-specific Station Numbers as placeholders displayed in bold typeface beginning with "\###".

> In the kaajeeConfig.xml file, you *must* replace these placeholder Station Number values with the appropriate valid values for the user to log into for your Web-based application. You can specify both division-level and facility-level Station Numbers, as appropriate for your application. To be valid, the values entered *must* be recognized by Standard Data Services (SDS).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/035.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> For every login Station Number you enter here, KAAJEE uses this as the Station Number parameter it passes to VistALink's Institution Mapping to retrieve a JNDI connector name for VistALink; therefore, every login station number should have a mapping configured in</p>
<p>VistALink's Institution Mapping.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/036.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on the kaajeeConfig.xml file, please refer to Chapter 6, "KAAJEE Configuration File," in the <em>KAAJEE Deployment Guide</em>.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Redeploy and Test the Web Application with the Updated kaajeeConfig.xml File *(required)*

> Use WebLogic to redeploy the Web application ear or standalone war file with the updated kaajeeConfig.xml file on all appropriate application servers. Test the redeployed application.

####### Exploded Ear Files

> Leave application as an exploded ear file.

####### Packaged Ear Files

1.  Zip any unzipped war files that implements KAAJEE authentication into a war, replacing the old war file.
2.  Zip up the application ear file.

####### Standalone War Files

> Zip any unzipped war files into a war, replacing the old war file.

## KAAJEE Classic dependencies configuration/installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/037.png)ESAPI library dependencies

> KAAJEE Classic 1.2.x has been upgraded to use ESAPI libraries for user input sanitation and validation. There is a new dependent library esapi-2.10.jar with the accompanying property files – ESAPI.properties and validation.properties. The library must be included in application’s dependencies. The property files must be placed on application’s classpath (\APP-INF or \WEB- INF). All the libraries are located at the \APP-INF\lib folder of the kaajeeSampleApp\*.ear file.

#### (Linux/Windows) Configure log4j for All J2EE-based Application Log Entries *(required)*

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/038.png)</p>
</blockquote></th>
<th><strong>UPGRADES:</strong> Skip this step if you have already configured log4j <em>and</em> added the KAAJEE- specific logger information to the active log4j configuration file on the application server, unless it is specifically noted that changes are required in the KAAJEE software release e-mail or Web site.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/039.png)</p>
</blockquote></td>
<td><p><strong>Note - KAAJEE Classic 1.2.x has been upgraded to use log4j2 libraries. There are two new dependent libraries – log4j-api-2.10.0.jar and log4j-core-2.10.0.jar, replacing the old one. Both libraries must be included in application’s dependencies. If you have application still using the older log4j 1 API, make sure to use the bridge library as well – log4j-1.2-api- 2.10.0.jar. All the libraries are located at the \APP-INF\lib folder of the kaajeeSampleApp*.ear file.</strong></p>
<p><strong>There are API signature changes and configuration file format changes For more information please visit:</strong> <a href="https://logging.apache.org/log4j/2.x/"><u>https://logging.apache.org/log4j/2.x/</u></a></p></td>
</tr>
</tbody>
</table>

> In order to provide a unified logger and consolidate all log/error entries into one file, all J2EE-based application-specific loggers *must* be added to the same log4j configuration file, which should be the active log4j configuration file for the server. After locating the active log4j configuration file used on the server you are configuring (e.g., mylog4j.xml file), add in the KAAJEE (and Fat-client Kernel Authentication and Authorization, or FatKAAT) loggers to that file.

> To locate the active log4j configuration file, look for the"-Dlog4j.configuration=" argument in the startup script file (i.e., setDomainEnv.sh/.cmd). The "-Dlog4j.configuration=" should be set to the absolute location of the configuration file (e.g., c:/mydirectory/mylog4j.xml). If no such argument is present, look for a file named "log4j.xml" in a folder on the server classpath.

> You *must* configure log4j for the first time, if all three of the following conditions exist:

- The "-Dlog4j.configuration=" argument does *not* exist in the WebLogic JVM startup script files.
- The "log4j.xml" file does *not* exist in the classpath.
- There is no pre-existing log4j configuration file in the folder placed on the classpath of the WebLogic Application Server containing the configuration files for all Health*<u>e</u>*Vet-VistA J2EE applications (e.g., \<HEV CONFIGURATION FOLDER\>).

> For first time log4j configuration procedures, please refer to the "log4j Configuration File" topic in the

> *VistALink Installation Guide (1.6)*. Also, sample log4j configuration files are included with the VistALink

6.  software distribution.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/040.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on VistALink, please refer to the Application Modernization Foundations Web site located at the following Web address:</p>
<p>REDACTED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Once the log4j file is initially configured, you need to configure the file specifically for KAAJEE log entries as outlined below.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/041.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>REF:</strong> For more information on log4j guidelines, please refer to the Application Structure &amp; Integration Services (ASIS) <em>Log4j Guidelines for HealtheVet-VistA Applications</em> document available at the following Web address:</p>
<p>REDACTED</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Configure Application for log4j

> Follow the Log4J instructions ([<u>http://jakarta.apache.org/log4j/docs/</u>](http://jakarta.apache.org/log4j/docs/)) to configure your application for Log4J.

#### Edit the File Name and Location for All Log Entries

> Edit the "verboseDailyRollingFileAppender" \<appender name\> tag in the active log4j configuration file (e.g., mylog4j.xml file). The "File" \<param name\> tag should point to the common file name and location where all J2EE-based application daily log entries for that domain will be recorded, as shown below:

> <span id="_bookmark36" class="anchor"></span>Figure 4-4. Sample excerpt of the mylog4j.xml file—Editing common log file name and location (Windows)

> In this example ([Figure 4-4](#_bookmark36)), the following common log file name and location is indicated:

> C:/AllAppData/bea/user_projects/domains/AllAppDomain/log/AllApp.log

> The application server administrator should point to the same log file established for that domain on the application server where *all* J2EE-based applications are logging their entries.

#### Add KAAJEE-specific Logger Tags

> Add the following four KAAJEE-specific logger tags to the active log4j configuration file (e.g., mylog4j.xml file) on the application server:

- REDACTED
- REDACTED

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/042.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> <a href="#_bookmark38">Figure 4-3</a> shows the detailed logger tag information that <em>must</em> be added to the active log4j configuration file (e.g., mylog4j.xml file) for KAAJEE.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Generally, the log level should be set as follows:

- Integrating KAAJEE—Set log level to DEBUG.
- Normal Operation Mode—Set log level to ERROR.

> The following figure shows the detailed logger tag information that *must* be added to the active log4j configuration file (e.g., mylog4j.xml file) for KAAJEE:

> <span id="_bookmark38" class="anchor"></span>Figure 4-3. Sample excerpt of the mylog4j.xml file—Adding KAAJEE logger information

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/043.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>NOTE:</strong> The log level value in this sample log4j.xml configuration file is currently set to "debug" mode for KAAJEE-related logger entries. To set those logger entries to normal</p>
<p>operations you would change "debug" to "error."</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](kaajee-classic-installation-guide-1-2-weblogic-10-3-6-and-weblogic-12-1/044.png)</p>
</blockquote></th>
<th><blockquote>
<p><strong>Congratulations! You have now completed the installation and configuration of KAAJEE-related software on the WebLogic Application Server.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Upon completing the installation of KAAJEE-related software on the VistA M Server and WebLogic Application Server, you are now

> ready to develop/run Health*e*Vet-VistA Web-based applications that use KAAJEE.

> *This page is left blank intentionally*.

# Appendix A: Installation Back-Out or Roll-Back Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> KAAJEE 1.1 comprises both a Java and an M component, similar to KAAJEE 1.0.

## VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The M component in KAAJE 1.1 (Patch XU\*8\*504) includes a new routine but doesn’t change any of the existing KAAJEE 1.0 routines. You can use the Kernel Installation and Distribution System (KIDS) option Backup a Transport Global \[XPD BACKUP\] to remove this routine.

> If the installation fails, the recommended actions are as follows:

1.  Review the install logs.
2.  Determine and address the cause of install failure.
3.  Re-run the installation.

> Optionally delete the following KAAJEE 1.1 components:

- Routine:
  - XUSKAAJ1
- Options:
  - XUS KAAJEE PROXY LOGON
  - XUS KAAJEE WEB LOGON
- Remote Procedure Calls (RPCs):
  - XUS KAAJEE GET CCOW TOKEN
  - XUS KAAJEE GET USER VIA PROXY
- Security Key:
  - XUKAAJEE_SAMPLE
- Application Proxy:
  - KAAJEE,PROXY

## J2EE Application Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Java component in KAAJEE 1.1 is not a stand-alone Web application. It is an embedded set of Java components and a Java library to be embedded within a consuming Web application. Therefore, there is no back-out/roll-back procedure specific to KAAJEE 1.1. Each consuming application would have to devise their own back-out/roll-back procedure.

> *This page is left blank intentionally.*

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: KAAJEE Classic Installation Guide

## Installer/Developer Notes—KAAJEE Classic Software First-Time Installations and Upgrades

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

First-time KAAJEE installers *must* perform *all* installation steps/procedures, except where noted. Those installation steps/procedures that can be skipped during a first-time installation will be displayed as follows:

|                                                                                                                                                       |                                                                                                                                     |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/014.png) | FIRST-Time INSTALLATION: *First-time installation-specific instructions or information that can be skipped will be found here.* |

If you were a test site prior to the final release of KAAJEE, we have notated those installation steps/procedures that have special information based on the final software upgrades that may affect how you install the released version of KAAJEE or provide other pertinent information. The upgrade information will be displayed as follows:

|                                                                                                                                                       |                                                                                  |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/015.png) | UPGRADES: *Upgrade-specific instructions or information will be found here.* |

In addition, we will use this section to also highlight any KAAJEE code changes from previous test/preview versions of the software to the released version of the software that may affect development teams coding KAAJEE-enabled applications.

## Confirm/Obtain VistA M Server Distribution Files *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following files and environment configuration are needed to install the Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE)-related VistA M Server software:

<span id="_Toc63338755" class="anchor"></span>Table ‑. KAAJEE-related VistA M Server distribution files and environment configuration

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Software/Configuration</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Operating System Software</td>
<td>InterSystems Caché</td>
</tr>
<tr class="even">
<td>Fully Patched M Accounts</td>
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
<td>VistALink Software</td>
<td>Version 1.6.7 (also listed above)</td>
</tr>
<tr class="even">
<td>VistA Kernel Software</td>
<td>Patch XU*8*504</td>
</tr>
<tr class="odd">
<td>KAAJEE_CLASSIC_8_749_RN.PDF</td>
<td><strong>Release Notes</strong> describes the changes to KAAJEE 1.2 to include new features and enhancements.</td>
</tr>
<tr class="even">
<td>KAAJEE_CLASSIC_8_749_IG.PDF</td>
<td><blockquote>
<p><strong>Installation Guide</strong> describes in detail the installation procedures for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>KAAJEE_CLASSIC_8_749_DEPG.PDF</td>
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
<td>![](kaajee-classic-installation-guide/022.png)</td>
<td><p><strong>REF:</strong> For the KAAJEE software release, all distribution files, unless otherwise noted, are available for download from the Enterprise VistA Support (EVS) anonymous directories:</p>
<ul>
<li><blockquote>
<p>Preferred Method REDACTED</p>
</blockquote></li>
</ul></td>
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

|                                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/023.png) | NOTE: The validation of the VistA institution occurs *before* the actual login to the VistA M Server, but *after* the user selects the Login button on the KAAJEE Classic Web login page. The selected institution is checked against the SDS 19.0 (or higher) tables for an entry and a VistA Provider. Also, KAAJEE Classic checks that an entry exists in the KAAJEE configuration file. |

|                                                                                                              |                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/024.png) | REF: For more information on the \<login-station-numbers\> tag and/or the kaajeeConfig.xml file, please refer to the "Edit the KAAJEE Configuration File *(required)*" topic in the "J2EE Application Server Installation Instructions," chapter in this manual. |

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
<td>![](kaajee-classic-installation-guide/025.png)</td>
<td><p><strong>REF:</strong> For more information on the XUMF IMF ADD EDIT option as well as the ASSOCIATIONS Multiple and PARENT OF ASSOCIATION fields data requirements, please refer to the Institution File Redesign (IFR) supplemental documentation located on the VDL at the following Web address:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appID=9">http://www.va.gov/vdl/application.asp?appID=9</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Verify KIDS Install Platform *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Verify that the Kernel Installation and Distribution System (KIDS) platform on your system is ready to install VistA M Server patches.

## Retrieve and Install the KAAJEE-related VistA M Server Patch *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8\*504 is the custodial patch for the M server installation of the KAAJEE software. All VistA M Server patches are distributed in Kernel 8.0 KIDS format. Follow the normal procedures to obtain and install released patches.

|                                                                                                                   |                                                                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/026.png) | Make sure that the Kernel, Kernel Toolkit, RPC Broker, VA FileMan, and VistALink software is fully patched. Patches must be installed in their published sequence. |

|                                                                                                              |                                                                                            |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/027.png) | REF: For more information on these patches, please refer to the Patch Module on FORUM. |

|                                                                                                                   |                                                                                                            |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/028.png) | Congratulations! You have now completed the installation of KAAJEE-related software on the VistA M Server. |

## Configure SDS 19.0 (or higher) JDBC Connections with the WebLogic Server *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                       |                                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/029.png) | UPGRADES: Skip this step if you have already configured the SDS tables, unless it is specifically noted that changes are required in the KAAJEE software release e-mail or Web site. |

To configure the Standard Data Services (SDS) tables for a J2EE DataSource, please refer to the "Configuring for a J2EE DataSource" topic in the *SDS API Installation Guide*.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-classic-installation-guide/030.png)</td>
<td><p><strong>REF:</strong> The <em>SDS API Installation Guide</em> is included in the SDS software distribution ZIP files, which are available for download at the following Web address:</p>
<blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Edit the KAAJEE Configuration File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Locate the kaajeeConfig.xml File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The EMC, or Application Server Administrator, must first locate the kaajeeConfig.xml file in the Web application ear or standalone war file, as follows:

Exploded Ear Files

> Navigate to the WEB-INF directory in the application's exploded ear/war file—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

Ear Files

> 1\. Unzip the application's ear file—Explode the artifact.

> 2\. For any war file that implements KAAJEE authentication inside the ear file, unzip the war file.

> 3\. Navigate to the WEB-INF directory—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

Standalone War Files

> 1\. Unzip the application's war file that implements KAAJEE authentication.

> 2\. Navigate to the WEB-INF directory—Locate the KAAJEE configuration file (i.e. kaajeeConfig.xml)

The following is a sample excerpt of the kaajeeConfig.xml file as distributed with KAAJEE 1.1.0.007:

<span id="_Ref107708020" class="anchor"></span>Figure ‑. Sample Station Number excerpt of the kaajeeConfig.xml file

\<?xml version="1.0" encoding="UTF-8"?\>

\<kaajee-config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="kaajeeConfig.xsd"\>

\<!-- host application name, used for login page display and logging --\>

\<host-application-name\>KAAJEE Sample\</host-application-name\>

\<!-- put each station number for KAAJEE login here --\>

\<login-station-numbers\>

\<station-number\>\###\</station-number\>

\<station-number\>\###9XX\</station-number\>

\<station-number\>\###9XX\</station-number\>

\<station-number\>\###XX\</station-number\>

\<station-number\>\###XX\</station-number\>

\<station-number\>\###\</station-number\>

\<station-number\>\###9XX\</station-number\>

\<station-number\>\###9XX\</station-number\>

\<station-number\>\###XX\</station-number\>

\<station-number\>\###XX\</station-number\>

\</login-station-numbers\>

...

\</kaajee-config\>

### Edit the Station Number List in the kaajeeConfig.xml File *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use a text editor (e.g., Microsoft Notepad) or other xml editing software to open and edit the kaajeeConfig.xml file. The \<station-number\> tags control the Station Number list displayed to the end-user in KAAJEE's login Web page Institution drop-down list. In Figure 4.5‑1, we represent the application-specific Station Numbers as placeholders displayed in bold typeface beginning with "\###".

In the kaajeeConfig.xml file, you *must* replace these placeholder Station Number values with the appropriate valid values for the user to log into for your Web-based application. You can specify both division-level and facility-level Station Numbers, as appropriate for your application. To be valid, the values entered *must* be recognized by Standard Data Services (SDS).

|                                                                                                              |                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/033.png) | NOTE: For every login Station Number you enter here, KAAJEE uses this as the Station Number parameter it passes to VistALink's Institution Mapping to retrieve a JNDI connector name for VistALink; therefore, every login station number should have a mapping configured in VistALink's Institution Mapping. |

|                                                                                                              |                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/034.png) | REF: For more information on the kaajeeConfig.xml file, please refer to Chapter 6, "KAAJEE Configuration File," in the *KAAJEE Deployment Guide*. |

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

### (Linux/Windows) Configure log4j for All J2EE-based Application Log Entries *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-classic-installation-guide/035.png)</td>
<td><strong>UPGRADES:</strong> Skip this step if you have already configured log4j <em>and</em> added the KAAJEE-specific logger information to the active log4j configuration file on the application server, unless it is specifically noted that changes are required in the KAAJEE software release e-mail or Web site.</td>
</tr>
<tr class="even">
<td>![](kaajee-classic-installation-guide/036.png)</td>
<td><p><strong>Note - KAAJEE Classic 1.2.x has been upgraded to use log4j2 libraries. There are two new dependent libraries – log4j-api-2.10.0.jar and log4j-core-2.10.0.jar, replacing the old one. Both libraries must be included in application’s dependencies. If you have application still using the older log4j 1 API, make sure to use the bridge library as well – log4j-1.2-api-2.10.0.jar. All the libraries are located at the \APP-INF\lib folder of the kaajeeSampleApp*.ear file.</strong></p>
<p><strong>There are API signature changes and configuration file format changes</strong></p>
<p><strong>For more information please visit:</strong> <a href="https://logging.apache.org/log4j/2.x/">https://logging.apache.org/log4j/2.x/</a></p></td>
</tr>
</tbody>
</table>

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
<td>![](kaajee-classic-installation-guide/037.png)</td>
<td><p><strong>REF:</strong> For more information on VistALink, please refer to the Application Modernization Foundations Web site located at the following Web address:</p>
<blockquote>
<p>REDACTED</p>
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
<td>![](kaajee-classic-installation-guide/038.png)</td>
<td><p><strong>REF:</strong> For more information on log4j guidelines, please refer to the Application Structure &amp; Integration Services (ASIS) <em>Log4j Guidelines for HealtheVet-VistA Applications</em> document available at the following Web address:</p>
<blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Configure Application for log4j

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the Log4J instructions (<http://jakarta.apache.org/log4j/docs/>) to configure your application for Log4J.

### Edit the File Name and Location for All Log Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the "verboseDailyRollingFileAppender" \<appender name\> tag in the active log4j configuration file (e.g., mylog4j.xml file). The "File" \<param name\> tag should point to the common file name and location where all J2EE-based application daily log entries for that domain will be recorded, as shown below:

<span id="_Ref101584411" class="anchor"></span>Figure ‑. Sample excerpt of the mylog4j.xml file—Editing common log file name and location (Windows)

\<?xml version="1.0" encoding="UTF-8"?\>

\<Configuration xmlns="http://logging.apache.org/log4j/2.0/config"\>

\<Appenders\>

\<File name="FILE" fileName="logfile.log" append="true"\>

\<PatternLayout pattern="%-5p \| %d{yyyy-MM-dd HH:mm:ss} \| \[%t\] %C{2} (%F:%L) - %m%n"/\>

\</File\>

\<Console name="STDOUT" target="SYSTEM_OUT"\>

\<PatternLayout pattern="%-5p \| %d{yyyy-MM-dd HH:mm:ss} \| \[%t\] %C{2} (%F:%L) - %m%n"/\>

\</Console\>

\</Appenders\>

\<Loggers\>

\<Logger name="com.memorynotfound" level="debug"/\>

\<Root level="info"\>

\<AppenderRef ref="STDOUT"/\>

\<AppenderRef ref="FILE"/\>

\</Root\>

\</Loggers\>

\</Configuration\>

In this example (Figure 4‑37), the following common log file name and location is indicated:

> logfile.log

The application server administrator should point to the same log file established for that domain on the application server where *all* J2EE-based applications are logging their entries.

### Add KAAJEE-specific Logger Tags

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Add the following four KAAJEE-specific logger tags to the active log4j configuration file (e.g., mylog4j.xml file) on the application server:

- REDACTED
- REDACTED

|                                                                                                              |                                                                                                                                                                 |
|--------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/039.png) | NOTE: Figure 4‑3 shows the detailed logger tag information that *must* be added to the active log4j configuration file (e.g., mylog4j.xml file) for KAAJEE. |

Generally, the log level should be set as follows:

- Integrating KAAJEE—Set log level to DEBUG.
- Normal Operation Mode—Set log level to ERROR.

The following figure shows the detailed logger tag information that *must* be added to the active log4j configuration file (e.g., mylog4j.xml file) for KAAJEE:

<span id="_Ref101259714" class="anchor"></span>Figure ‑. Sample excerpt of the mylog4j.xml file—Adding KAAJEE logger information

.

.

.

\<logger name="REDACTED" additivity="false" \>

\<level value="debug" /\>

\<appender-ref ref="verboseDailyRollingFileAppender"/\>

\</logger\>

\<logger name="REDACTED" additivity="false" \>

\<level value="debug" /\>

\<appender-ref ref="verboseDailyRollingFileAppender"/\>

\</logger\>

.

.

.

|                                                                                                              |                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/040.png) | NOTE: The log level value in this sample log4j.xml configuration file is currently set to "debug" mode for KAAJEE-related logger entries. To set those logger entries to normal operations you would change "debug" to "error." |

|                                                                                                                   |                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-classic-installation-guide/041.png) | Congratulations! You have now completed the installation and configuration of KAAJEE Classic-related software on the WebLogic Application Server. |

> Upon completing the installation of KAAJEE-related software on the VistA M Server and WebLogic Application Server, you are now ready to develop/run Health*<u>e</u>*Vet-VistA Web-based applications that use KAAJEE Classic.

#########  

*This page is left blank intentionally*.

######### Appendix A: Installation Back-Out or Roll-Back Procedure

KAAJEE Classic 8.0.749 is comprised of only J2EE components

VistA M Server

- No VistA components were installed with this patch

J2EE Application Server

The Java component in KAAJEE Classic is not a stand-alone Web application. It is an embedded set of Java components and a Java library to be embedded within a consuming Web application. Therefore, there is no back-out/roll-back procedure specific to KAAJEE Classic. Each consuming application would have to devise their own back-out/roll-back procedure.

*This page is left blank intentionally.*
