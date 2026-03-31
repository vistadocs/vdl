---
title: VSM Installation, Back-out, and Rollback Guide (DIBRG)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: plain
doc_subject: 
app_code: KMPV
app_name: VistA System Monitor (VSM)
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - vista
  - installation
  - back
  - software
  - monitor
  - rollback
  - patch
  - deployment
page_count: 0
word_count: 5621
section_count: 30
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/VistA_System_Monitor_(VSM)/kmp_dibrg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/VistA_System_Monitor_(VSM)/kmp_dibrg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=218"
---

---
title: |
  <span id="_Toc186420068" class="anchor"></span>VistA System Monitor (VSM) 3.0

  Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)
---

![](vsm-installation-back-out-and-rollback-guide-dibrg/001.png)

July 2020

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

Capacity and Performance Engineering (CPE)

<span id="revision_history" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref431821080" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 41%" />
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
<td>07/22/2020</td>
<td>1.0</td>
<td><p>Initial VistA System Monitor (VSM) 3.0 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG):</p>
<ul>
<li><p>Converted the current Installation Guide into a Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) via the DIBRG template Version 2.2, released on March 2016.</p></li>
<li><p>Upgraded to real time VistA System Monitor 3.0.</p></li>
<li><p>Changed transmission to real time using HyperText Transport Protocol (HTTP).</p></li>
<li><p>Updated the following monitors:</p></li>
</ul>
<ul>
<li><p>VistA Timed Collection Monitor (VTCM)</p></li>
<li><p>VistA Storage Monitor (VSTM)</p></li>
<li><p>VistA Business Event Monitor (VBEM)</p></li>
<li><p>VistA Message Count Monitor (VMCM)</p></li>
<li><p>VistA HL7 Monitor (VHLM)</p></li>
</ul>
<ul>
<li><p>Added the following new monitors:</p></li>
</ul>
<ul>
<li><p>Vista Coversheet Monitor (VCSM).</p></li>
<li><p>VistA Error Trap Monitor (VETM).</p></li>
</ul></td>
<td>Enterprise Program Management Office (EPMO) Capacity and Performance Engineering (CPE)</td>
</tr>
</tbody>
</table>

<span id="_Ref431821080" class="anchor"></span>Table : Documentation Symbol Descriptions

Table of Contents

<span id="_Toc46403803" class="anchor"></span>List of Figures

<span id="_Toc46403804" class="anchor"></span>List of Tables

<span id="_Toc46403805" class="anchor"></span>Orientation

How to Use this Manual

The Deployment, Installation, Back-out, and Rollback Guide (DIBRG) defines the ordered, technical steps required to install the product, and if necessary, to back out the installation, and roll back to the previously installed version of the product.

Throughout this manual, advice and instructions are offered regarding the use of VistA System Monitor (VSM) 3.0 software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—System engineers and Capacity Management personnel responsible for enterprise capacity planning and system architecture.
- System Administrators—System administrators and Capacity Management personnel at local and regional Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- EPMO Developers—VistA legacy development teams.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation Disclaimer

This manual provides an overall explanation of using the VistA System Monitor (VSM) 3.0 software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) Enterprise Program Management Office (EPMO) Intranet Website.

![](vsm-installation-back-out-and-rollback-guide-dibrg/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                                                                | Description                                                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vsm-installation-back-out-and-rollback-guide-dibrg/003.png)                                             | NOTE / REF: Used to inform the reader of general information including references to additional reading material.                         |
| ![](vsm-installation-back-out-and-rollback-guide-dibrg/004.png)                                     | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information.                         |
| ![](vsm-installation-back-out-and-rollback-guide-dibrg/005.png) | SPECIAL INSTALLATION NOTE: Used to denote special installation instructions only (e.g., virgin installations or platform-specific steps). |

<span id="_Ref44917434" class="anchor"></span>Table : Deployment, Installation, Back-Out, and Rollback Roles and Responsibilities<span id="ColumnTitle_03" class="anchor"></span>

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*PATIENT,*\<N\>*
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*USER,*\<N\>*

Where “\<*APPLICATION NAME/ABBREVIATION/NAMESPACE\>*” is defined in the Approved Application Abbreviations document and “\<*N*\>” represents the first name as a number spelled out or as a number value and incremented with each new entry.

For example, in VSM (KMP) test patient and user names would be documented as follows:

- KMPPATIENT,ONE or KMPUSER,ONE
- KMPPATIENT,TWO or KMPUSER,TWO
- KMPPATIENT,THREE or KMPUSER,THREE
- KMPPATIENT,14 or KMPUSER,14
- Etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](vsm-installation-back-out-and-rollback-guide-dibrg/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](vsm-installation-back-out-and-rollback-guide-dibrg/007.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to the toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in the Toolbar to navigate back and forth in the Word document when selecting hyperlinks within the document.

![](vsm-installation-back-out-and-rollback-guide-dibrg/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](vsm-installation-back-out-and-rollback-guide-dibrg/009.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.  
  
REF: For further information, see the *VistA System Monitor (VSM) Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](vsm-installation-back-out-and-rollback-guide-dibrg/010.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about VSM should consult the following:

- *VistA System Monitor (VSM) Deployment, Installation, Back-Out, and Rollback Guide(DIBRG)* (this manual)
- *VistA System Monitor (VSM) User Manual*
- *VistA System Monitor (VSM) Technical Manual*

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL): <http://www.va.gov/vdl/>

![](vsm-installation-back-out-and-rollback-guide-dibrg/011.png) REF: See the [VistA System Monitor (VSM) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=218).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

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
    - [Hardware](#hardware)
    - [Software](#software)
    - [Communications](#communications)
- [Installation](#installation)
  - [Pre-Installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
    - [Software](#software-1)
    - [Documentation](#documentation)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [Patch Installation Instructions](#patch-installation-instructions)
    - [Caché Task Manager](#caché-task-manager)
  - [Installation Verification Procedure](#installation-verification-procedure)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
The Veterans Health Information Systems and Technology Architecture (VistA) System Monitor (VSM) 3.0 software collects Caché and VistA metrics related to system capacity and business usage. The package is made up of multiple collectors. The KMP\*4.0\*1 patch upgraded the following five collectors to provide data in real time:
- VistA Timed Collection Monitor (VTCM)—Collects Caché metrics at regularly scheduled intervals such that they can be used in conjunction with metrics gathered via other deployed collection tools.
- VistA Storage Monitor (VSTM)—Collects storage metrics for each database once daily.
- VistA Business Event Monitor (VBEM)—Collects Cache metrics for VistA functions (Menu Options, TaskMan Jobs and Remote Procedure Calls).
- VistA Message Count Monitor (VMCM)—Collects inbound and outbound Health Level Seven (HL7) and HL7 Optimized (HLO) message counts at regularly scheduled intervals.
- VistA HL7 Monitor (VHLM)—Collects metadata about HL7 messages (SYNC and ASYNC) as well as HLO messages.
  Additionally, the KMP\*4.0\*1 patch deployed the following two monitors:
- Vista Coversheet Monitor (VCSM)—Collects timing metrics related to the Computerized Patient Record System (CPRS) coversheets.
- VistA Error Trap Monitor (VETM)—Collects data from the sites Kernel Error Trap, ERROR LOG (#3.075) file.
This data is used for understanding VistA systems as they relate to the infrastructure on which they are deployed and to provide data for application performance monitoring.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for deploying and installing the VistA Capacity and Performance Engineering (CPE) VistA System Monitor (VSM) 3.0 software (KMP\*4.0\*1 patch).

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists and describes all application, system, financial, and other dependencies for this deployment, including upstream processing.

There are no dependencies for VSM 3.0 Patch KMP\*4.0\*1 release other than the operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no constraints for VSM 3.0 Patch KMP\*4.0\*1 release other than the operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the teams that will perform the steps described in this guide.

<u>Table 2</u> identifies the technical and support personnel who are involved in the deployment, installation, back-out, and rollback of the Veterans Health Information Systems and Technology Architecture (VistA) System Monitor (VSM) 3.0 software (KMP\*4.0\*1) release.

<table>
<caption><p>Table 3: VSM 3.0 Patch KMP*4.0*1 Deployment Timeline</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 29%" />
<col style="width: 14%" />
<col style="width: 36%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>ID</th>
<th>Team</th>
<th>Phase / Role</th>
<th>Tasks</th>
<th>Project Phase (See Schedule)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>Enterprise Program Management Office (EPMO) Implementation Team</td>
<td>Deployment</td>
<td>Plan and schedule deployment (including orchestration with vendors).</td>
<td>Planning</td>
</tr>
<tr class="even">
<td>2</td>
<td>EPMO Implementation Team</td>
<td>Deployment</td>
<td>Determine and document the roles and responsibilities of those involved in the deployment.</td>
<td>Planning</td>
</tr>
<tr class="odd">
<td>3</td>
<td>Software Quality Assurance (SQA)</td>
<td>Deployment</td>
<td>Test for operational readiness.</td>
<td>Build</td>
</tr>
<tr class="even">
<td>4</td>
<td>Product Support (PS)</td>
<td>Deployment</td>
<td>Execute deployment.</td>
<td>Release Prep Phase</td>
</tr>
<tr class="odd">
<td>5</td>
<td>EPMO Implementation Team</td>
<td>Installation</td>
<td>Plan and schedule installation.</td>
<td>Build Phase</td>
</tr>
<tr class="even">
<td>6</td>
<td>EPMO Implementation Team<br />
Capacity and Performance Engineering (CPE) Team</td>
<td>Back-Out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
<td>Build Phase</td>
</tr>
<tr class="odd">
<td>7</td>
<td>SDE Field Operations (FO)<br />
Enterprise Operations (EO)</td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support.</td>
<td>Post Release</td>
</tr>
</tbody>
</table>

Table 3: VSM 3.0 Patch KMP\*4.0\*1 Deployment Timeline

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the VSM 3.0 Patch KMP\*4.0\*1 deployment.

The VSM 3.0 Patch KMP\*4.0\*1 deployment is planned as a simultaneous rollout. National release is scheduled for August 2020.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSM 3.0 Patch KMP\*4.0\*1 deployment and installation is scheduled to run for 30 days from release, which is the typical Veterans Health Information Systems and Technology Architecture (VistA) national patch rollout schedule.

<u>Table 3</u> provides an *estimate* of the VSM 3.0 Patch KMP\*4.0\*1 deployment timeline dates:

| Deployment                       | Start        | Finish        |
|----------------------------------|--------------|---------------|
| Patch Development and Release    | 1/1/2020 | 8/1/2020  |
| Site Installation and Deployment | 8/1/2020 | 8/31/2020 |
| Sustainment                      | 9/1/2020 | N/A       |

<span id="_Ref44918407" class="anchor"></span>Table : Site Preparation

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Site Readiness Assessment for the locations that will receive the VSM 3.0 Patch KMP\*4.0\*1 deployment. This will be a typical national release of a VistA patch to all VistA production sites.

Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Field Office (FO), National Data Center Program (NDCP), and Austin Information Technology Center (AITC) during the design phase as appropriate. Field site coordination is done by FO unless otherwise stipulated by FO.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the deployment topology (local sites, etc.) for VSM 3.0 Patch KMP\*4.0\*1.

VSM 3.0 Patch KMP\*4.0\*1 will be distributed to local and regional system administrators and support personnel responsible for each of the 130 VistA parent systems. The actual code will be available to developers from the Product Support (PS) Anonymous Directories. (The code will be available to developers from secure file transfer (SFTP) sites listed in the patch description.)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the physical locations (sites) that will host the deployed VSM 3.0 Patch KMP\*4.0\*1.

The VSM 3.0 Patch KMP\*4.0\*1 code is directly deployed to VA sites.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the preparation required for the site at which the system will operate.

There are no special site preparations or changes that *must* occur to the operational site and no specific features or items that need to be modified to adapt to VSM 3.0 Patch KMP\*4.0\*1.

As a precursor to the VSM 3.0 Patch KMP\*4.0\*1 deployment, the VSM documentation set (including this *Deployment, Installation, Back-Out, and Rollback Guide \[DIBRG\]*) will be added to the VA Software Document Library (VDL) at: <https://www.va.gov/vdl/application.asp?appid=218>

<u>Table 4</u> describes preparation required by the site prior to deployment.

| Site/Other           | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------------|-----------------------|-----------------------------------------|---------------|-------|
| Not Applicable (N/A) | N/A                   | N/A                                     | N/A           | N/A   |

<span id="_Ref44918161" class="anchor"></span>Table : Hardware Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the hardware, software, facilities, documentation, and any other resources, other than personnel, required for the VSM 3.0 Patch KMP\*4.0\*1 deployment and installation.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for installation of VSM 3.0 Patch KMP\*4.0\*1. There is also no need for specific hardware to assist in the deployment of VSM 3.0 Patch KMP\*4.0\*1.

<u>Table 5</u> describes hardware specifications required at each site prior to deployment.

| Required Hardware    | Model | Version | Configuration | Manufacturer | Other |
|----------------------|-------|---------|---------------|--------------|-------|
| Not Applicable (N/A) | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Ref44920296" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

![](vsm-installation-back-out-and-rollback-guide-dibrg/012.png) REF: For details about who is responsible for preparing the site to meet these hardware specifications, see <u>Table 2</u>.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your VistA Server in order to install and use the VSM 3.0 Patch KMP\*4.0\*1 software:

- VistA System Monitor 2.0 *must* already be installed. This includes patch releases: XU\*8.0\*568 and XU\*8.0\*670.
- VistA account running on InterSystems’ Caché for Linux, NT, or OpenVMS.
- VistA accounts *must* contain the fully patched versions of the following packages:
- Kernel 8.0
- Kernel Toolkit 7.3
- MailMan 8.0
- VA FileMan 22.2
- VSM 2.0

![](vsm-installation-back-out-and-rollback-guide-dibrg/013.png) REF: For details about who is responsible for preparing the site to meet these software specifications, see <u>Table 2</u>.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any notifications activities and how they will occur.

Prior to the deployment of the VSM 3.0 Patch KMP\*4.0\*1 release, a product announcement will be sent via email to current Points of Contact (POC) on record for each site describing the product and a brief description of the deployment and post-deployment support. Included will be links to the [VSM 3.0 VA Software Document Library (VDL)](file:///C:\Users\VHAISFBLOMT\AppData\Roaming\Microsoft\Word\VA%20Software%20Document%20Library%20(VDL)%20at:%20https:\www.va.gov\vdl\application.asp%3fappid=218) and Rational/GitHub repositories, which contain further information about the release and the deployment, including the deployment schedule and required pre-installation activities.

The VSM 3.0 Patch KMP\*4.0\*1 Implementation Team will respond to email requests for assistance and further information and, where appropriate, re-direct these requests to specialist technical staff.

#### Deployment/Installation/Back-Out Checklist

Tracking of installation for VSM 3.0 Patch KMP\*4.0\*1 is monitored in FORUM.

<u>Table 6</u> provides a checklist to be used to capture the coordination effort and document the day/time/individual when each activity (deploy, install, back-out) is completed for VSM 3.0 patch releases.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

<span id="_Toc46403864" class="anchor"></span>Table : VSM Documentation

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum software tools are required on your VistA Server in order to install and use the VSM 3.0 Patch KMP\*4.0\*1 software:

- VistA System Monitor (VSM) 2.0 *must* already be installed. This includes patch releases: XU\*8.0\*568 and XU\*8.0\*670.
- VistA account running on InterSystems’ Caché for Linux, NT, or OpenVMS.
- VistA accounts *must* contain the fully patched versions of the following packages:
- Kernel 8.0
- Kernel Toolkit 7.3
- MailMan 8.0
- VA FileMan 22.2\*
- VSM 1.0

![](vsm-installation-back-out-and-rollback-guide-dibrg/014.png) NOTE: These software packages *must* be properly installed and fully patched *prior* to installing the VSM 3.0 Patch KMP\*4.0\*1 software distribution. Patches *must* be installed in published sequence. You can obtain all released VistA patches (including patch description and installation instructions), from the National Patch Module (NPM) on FORUM or through normal procedures.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *recommended* that sites take the following approach to installing the VistA System Monitor (VSM) 3.0 software:

1.  Obtain the [VSM 3.0 documentation](file:///C:\Users\VHAISFBLOMT\AppData\Roaming\Microsoft\Word\VA%20Software%20Document%20Library%20(VDL)%20at:%20https:\www.va.gov\vdl\application.asp%3fappid=218).
10. Install the software into a Test account.
11. Install the software into a Production system.

The installation of VistA System Monitor (VSM) 3.0 software only affects the VSM options. Therefore, this installation can be performed at any time of the day with no disruption. Installation should take approximately 2 minutes.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment of the VistA System Monitor (VSM) 3.0 software is released via the National Patch Module (NPM) on FORUM using MailMan and Kernel Installation & Distribution System (KIDS); there is no host file with this patch. Use KIDS to install the VistA System Monitor (VSM) 3.0 software.

The purpose of VSM 3.0 is to upgrade the following as part of the Capacity Management (KMP\*) VistA System Monitor (KMP) tools suite to real time metric transmission:

- VistA Timed Collection Monitor (VTCM)—Collects Caché metrics at regularly scheduled intervals such that they can be used in conjunction with metrics gathered via other deployed collection tools.
- VistA Storage Monitor (VSTM)—Collects storage metrics for each database once daily.
- VistA Business Event Monitor (VBEM)—Collects Cache metrics for VistA functions (Menu Options, TaskMan Jobs and Remote Procedure Calls).
- VistA Message Count Monitor (VMCM)—Collects inbound and outbound Health Level Seven (HL7) and HL7 Optimized (HLO) message counts at regularly scheduled intervals.
- VistA HL7 Monitor (VHLM)—Collects metadata about HL7 messages (SYNC and ASYNC) as well as HLO messages.

Additionally, the following two monitors will be deployed:

- Vista Coversheet Monitor (VCSM)—Collects timing metrics related to the CPRS coversheets.
- VistA Error Trap Monitor (VETM)—Collects data from the sites Kernel Error Trap, ERROR LOG (#3.075) file.

### Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for Vista System Monitor (VSM) is available on the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/application.asp?appid=218>.

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories via Secure File Transfer Protocol (SFTP).

| File Name     | FTP Mode | Description                                                |
|---------------|----------|------------------------------------------------------------|
| kmp_dibrg.pdf | Binary   | VSM Deployment, Installation, Back-out, and Rollback Guide |
| kmp_um.pdf    | Binary   | VSM User Manual                                            |
| kmp_tm.pdf    | Binary   | VSM Technical Manual                                       |

VSM DocumentationVSM Documentation

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSM 3.0 software installation does *not* create any databases. VSM uses the existing VA FileMan database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for the Vista System Monitor (VSM) 3.0 software installation.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no cron scripts for the Vista System Monitor (VSM) 3.0 software installation.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installer needs to know how to do the following:

- Obtain VistA software from FORUM.
- Run a Kernel Installation and Distribution System (KIDS) installation.
- Use the VistA Systems Manager Menu \[EVE\]EVE menu.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patch Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch installation instructions are documented in VSM 3.0 Patch KMP\*4.0\*1 on FORUM. This is a standard VistA patch installation. Use the Kernel Installation & Distribution System (KIDS) to install the VistA System Monitor (VSM) 3.0 software. Monitors will be started automatically on production systems.

This installation updates the following VSM files in the ^KMPV global:

- VSM CONFIGURATION (#8969): Contains configuration parameters for each monitor and most recent run times.
- VSM MONITOR DEFAULTS (#8969.02): Contains default configuration parameters for each monitor allowing restoration of monitor defaults.
- VSM CACHE TASK LOG (#8969.03): Contains run time for each monitor and node for forensic purposes. This file will be purged upon each monitor run to contain a maximum of six (6) months of entries.

The ^KMPTMP(“KMPV”) global is used to store temporary VSM data. To ensure global size is kept to a minimum, a purge function is run at the daily start of all monitors. Data is kept only up to the maximum number of days configured in the VSM CONFIGURATION (#8969) file. This parameter has a maximum of seven (7) days.

![](vsm-installation-back-out-and-rollback-guide-dibrg/015.png) CAUTION: The ^KMPTMP("KMPV") global should *not* be journaled!

![](vsm-installation-back-out-and-rollback-guide-dibrg/016.png) REF: Details regarding imported files, options, protocols, etc. can be found in the *VSM Technical Manual*.

### Caché Task Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA System Monitors are dependent on the Caché Task Manager to start the collection routine each morning on each node of the VistA environment.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the VSM installation, do the following:

1.  Use the VSM MANAGEMENT \[KMPV VSM MANAGEMENT\] option located under the Capacity Planning \[XTCM MAIN\] option to verify the VSM installation:

> <span id="_Toc46403854" class="anchor"></span>Figure : VSM Management—Main

> ![](vsm-installation-back-out-and-rollback-guide-dibrg/017.png)

![](vsm-installation-back-out-and-rollback-guide-dibrg/018.png) NOTE: the VSM MANAGEMENT option requires the KMPVROPS security key.

12. Once in the “VSM MANAGEMENT” screen:
1.  Choose VIEW.
2.  Choose the monitor (e.g., VTCM), as shown in <u>Figure 2</u>:

> <span id="_Ref44932635" class="anchor"></span>Figure : VSM Management—Menu: View Action

> ![](vsm-installation-back-out-and-rollback-guide-dibrg/019.png)

13. The monitor chosen is then displayed, as shown in <u>Figure 3</u>:

> <span id="_Ref436755056" class="anchor"></span>Figure : VSM Management—View Configuration

> REDACTED

![](vsm-installation-back-out-and-rollback-guide-dibrg/020.png) NOTE: The monitor is turned on by default for production systems. If it is a test system, the monitor will be off after installation, since the ALLOW TEST SYSTEM default value is NO.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special system configuration requirements with the VSM 3.0 software installation.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special database tuning requirements for the VSM 3.0 software installation.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

This software provides the means to revert most functionality back to that of VSM 2.0. This is accomplished on the remote console by the CPE VSM Admins. Contact:

VA IT EPMO CPE VistA System Monitor \<REDACTED@va.gov\>

If this is *not* sufficient. then a patch will need to be created and deployed to all sites to revert back to full VSM 2.0 functionality.

![](vsm-installation-back-out-and-rollback-guide-dibrg/021.png) NOTE: For patch back-out procedures, see the patch description.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from:

- Veterans Health Administration (VHA)
- Enterprise Program Management Office (EPMO) Capacity
- Performance Engineering (CPE)

In the case of the initial release, a back-out would include removal of data, files, and routines. In the case of future patches and releases, the back-out strategy would be dependent on the contents of the released functionality and could include restoration of file definitions, routines, or data.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include impact on production VistA end-users and impact on the Wide Area Network (WAN).

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for VSM.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM User Acceptance Testing (UAT) is performed during VistA patch testing at test sites.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSM back-out criteria follow existing VistA back-out procedures.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VSM back-out risks are the same risks established with existing VistA back-out procedures.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with VHA and EPMO CPE representatives.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This software provides the means to revert most functionality back to VSM 2.0. This is accomplished on the remote console by the CPE VSM Admins. Contact:

VA IT EPMO CPE VistA System Monitor \<REDACTED@va.gov\>

If this is *not* sufficient then a patch will need to be created and deployed to all sites that to revert to full VSM Version 2.0 functionality.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data.

The VistA System Monitor (VSM) 3.0 software collects system data throughout the day and sends that data to the national database as it is collected. Data is deleted at the site upon acknowledgement from the national server that data has been received. If there is a problem with receiving the acknowledgement, then data is purged after seven (7) days. In the case that the purge does *not* work then the monitors can be stopped and all data deleted at the site using the Delete Data option. This option is found on the main VistA menu, as shown in <u>Figure 4</u>:

<span id="_Ref509998959" class="anchor"></span>Figure : VSM Rollback Procedure—Delete Data Option

Capacity Planning…

VSM MANAGEMENT

Delete Data

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM data should be deleted only if it has been determined that the automatic data management features are *not* working.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VSM data should be deleted if there are more than seven (7) days of data in the ^KMPTMP(“KMPV”, global.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The risk to rollback would be the loss of system, business and message metrics for that period of time. This risk is much less than any potential harm to a system and should be considered a low risk.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback *can* be authorized by system administrators once a problem has been identified. The Capacity and Performance Engineering (CPE) group should be informed immediately via email to the following address:

VA IT EPMO CPE VistA System Monitor \<REDACTED@va.gov\>

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data can be deleted at the site using the Delete Data option. This option is found on the main VistA menu, as shown in <u>Figure 4</u>.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two ways to roll back VSM 3.0 back to VMS 2.0. The method used is dependent on the reason for the rollback:

- Can Receive HTTP Requests—If the site can successfully receive HTTP requests, the rollback mechanism can be executed from the VSM Manager Application by CPE engineers. The site will receive an HTTP message that will call VistA code to revert the configuration for each monitor back to VSM 2.0.
- *Cannot* Receive HTTP Requests—If the site *cannot* successfully receive HTTP requests, a routine is available that could be run manually to revert the configuration for each monitor back to VMS 2.0.

![](vsm-installation-back-out-and-rollback-guide-dibrg/022.png) NOTE: VMS 2.0 software code will still exist at the site for this express purpose of facilitating a rollback if ever needed.