---
title: XWB*1.1*73 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: (DIBRG)
app_code: XWB
app_name: Remote Procedure Call (RPC) Broker
section: INF
app_status: active
pkg_ns: XWB
patch_ver: 1.1
patch_id: XWB*1.1*73
group_key: "XWB:XWB:1.1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - broker
  - table
  - installation
  - strong
  - client
  - back
  - software
  - deployment
  - contents
  - class
page_count: 0
word_count: 12772
section_count: 31
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_73_dibrg_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_73_dibrg_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=23"
---

---
title: |
  RPC Broker 1.1; Patch XWB\*1.1\*73

  Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) (REDACTED)
---

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/001.png)

September 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

<span id="_Toc209429662" class="anchor"></span>Revision History

Documentation Revisions

<table>
<caption><p><span id="_Ref473639233" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/14/2021</td>
<td>1.0</td>
<td><p>Initial RPC Broker Version 1.1 Patch XWB*1.1*73 Deployment, Installation, Back-Out, and Rollback Guide.</p>
<p><strong>RPC Broker 1.1</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref473639233" class="anchor"></span>Table : Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc82525154" class="anchor"></span>List of Figures

[Figure 1: Sample Linux xinetd.d Script to Define the Listener Process to be Started [19](#_Ref470097935)](#_Ref470097935)

[Figure 2: RPC Broker Client Agent Icons (connected, *not* connected) [21](#_Toc82525226)](#_Toc82525226)

<span id="_Toc82525155" class="anchor"></span>List of Tables

<span id="_Toc336760250" class="anchor"></span>

Orientation

How to Use this Manual

This manual provides advice and instructions for deploying and installing the Veterans Health Information Systems and Technology Architecture (VistA) Remote Procedure Call (RPC) Broker (also referred to as “Broker”) Version 1.1 software, which includes the RPC Broker 1.1 Development Kit (BDK).

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—Personnel responsible for regional and local computer management and system security on VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimer

This manual provides an overall explanation of RPC Broker and the functionality contained in RPC Broker 1.1; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/004.png)       | NOTE/REF: Used to inform the reader of general information including references to additional reading material                   |
| ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/005.png) | CAUTION / DISCLAIMER /SKIP THIS STEP / RECOMMENDATION: Used to caution the reader to take special notice of critical information |

<span id="_Ref473729190" class="anchor"></span>Table : Commonly Used RPC Broker Terms

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666.”
- Patient and user names are formatted as follows:
- \[Application Name\]PATIENT,\[N\]
- \[Application Name\]USER,\[N\]

Where “*Application Name*” is defined in the Approved Application Abbreviations document and “*N*” represents the first name as a number spelled out and incremented with each new entry.

For example, in RPC Broker (XWB) test patient names would be documented as follows:

XWBPATIENT,ONE; XWBPATIENT,TWO; XWBPATIENT,14, etc.

For example, in RPC Broker (XWB) test user names would be documented as follows:

XWBUSER,ONE; XWBUSER,TWO; XWBUSER,14, etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are in boldface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is in boldface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- (Optional) Screen capture content that varies depending on the site, system, and user input is indicated with an italicized placeholder name between two angle brackets and highlighted in green, as shown here:

<span class="mark">\<*Placeholder Name*\></span>

- Some software code reserved/key words are in boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/007.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, perform the following procedure:

1.  Right-click anywhere on the customizable Toolbar in Word 2010 (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and press Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and press Add to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

Commonly Used Terms

<u>Table 2</u> lists terms and their descriptions that you may find helpful while reading the RPC Broker documentation:

<table>
<caption><p><span id="_Ref473643111" class="anchor"></span>Table : Roles and Responsibilities</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Client</td>
<td>A single term used interchangeably to refer to a user, the workstation (i.e., PC), and the portion of the program that runs on the workstation.</td>
</tr>
<tr class="even">
<td>Component</td>
<td><p>A software object that contains data and code. A component may or may not be visible.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/009.png) <strong>REF:</strong> For a more detailed description, see the <em>Embarcadero Delphi for Windows User Guide</em>.</p></td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>The Graphical User Interface application that is developed for the client workstation.</td>
</tr>
<tr class="even">
<td>Host</td>
<td>The term Host is used interchangeably with the term Server.</td>
</tr>
<tr class="odd">
<td>Server</td>
<td>The computer where the data and the RPC Broker remote procedure calls (RPCs) reside.</td>
</tr>
</tbody>
</table>

<span id="_Ref473643111" class="anchor"></span>Table : Roles and Responsibilities

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/010.png) REF: For additional terms and definitions, see the “Glossary” section in the other RPC Broker manuals.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/011.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.  
  
REF: For more information, see the *RPC Broker Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/012.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- Remote Procedure Call (RPC) Broker—VistA Client/Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language
- Object Pascal programming language
- Object Pascal programming language/Embarcadero Delphi Integrated Development Environment (IDE)—RPC Broker

References

Readers who wish to learn more about RPC Broker should consult the following:

- *RPC Broker Release Notes*
- *RPC Broker Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)* (this manual)
- *RPC Broker Systems Management Guide*
- *RPC Broker Technical Manual*
- *RPC Broker User Guide*
- *RPC Broker Developer’s Guide*—Document
- RPC Broker VA Intranet website.  
    
  This site provides additional information (e.g., Frequently Asked Questions \[FAQs\], advisories), documentation links, archives of older documentation and software downloads.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) website: <http://www.va.gov/vdl/>

The RPC Broker documentation is located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=23>

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
    - [VistA M Server Distribution Files](#vista-m-server-distribution-files)
    - [Standard Client Workstation Distribution Files](#standard-client-workstation-distribution-files)
    - [Programmer-Only Client Workstation Distribution Files](#programmer-only-client-workstation-distribution-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [VistA M Server Installation Instructions](#vista-m-server-installation-instructions)
    - [Standard Client Workstation Installation Instructions](#standard-client-workstation-installation-instructions)
    - [Programmer-Only Client Workstation Installation Instructions](#programmer-only-client-workstation-installation-instructions)
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
    - [VistA M Servers](#vista-m-servers)
    - [Standard Client Workstations](#standard-client-workstations)
    - [Programmer-Only Client Workstations](#programmer-only-client-workstations)
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
This document describes how to deploy and install the Veterans Health Information Systems and Technology Architecture (VistA) Remote Procedure Call (RPC) Broker (also referred to as “Broker”) 1.1 software and Patch XWB\*1.1\*73, as well as how to back-out the product and rollback to a previous version or data set.
RPC Broker 1.1 provides programmers with the capability to develop VistA client/server software. RPC Broker 1.1 Patch XWB\*1.1\*73 includes an updated Broker Development Kit (BDK).
As of RPC Broker Patch XWB\*1.1\*65, the BDK provides 2-Factor Authentication (2FA) support. It uses the Secure Token Service (STS) delegated authentication model. 2-factor authentication support on the VistA server is handled by VistA Kernel software. No RPC Broker changes are needed in VistA to enable 2-factor authentication on a Broker listener. Delphi RPC Broker client applications are automatically upgraded to the new 2-factor authentication method when using this latest version of the BDK.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the VistA RPC Broker 1.1 is deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists and describes all application, system, financial, and other dependencies for this deployment, including upstream processing.

There are no dependencies for RPC Broker 1.1 Patch XWB\*1.1\*73 BDK release other than the operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the target physical environment for deployment. The RPC Broker security controls are operationally capable within full implementation of National Institute of Standards and Technology (NIST) controls. It is in compliance with Directive 6500, Section 508 compliance, and performance impacts of the deployment environment.

There are no constraints for RPC Broker 1.1 Patch XWB\*1.1\*73 BDK release other than the operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the teams that will perform the steps described in this guide.

<u>Table 3</u> identifies the technical and support personnel who are involved in the deployment, installation, back-out, and rollback of the Veterans Health Information Systems and Technology Architecture (VistA) RPC Broker 1.1 Patch XWB\*1.1\*73 Broker Development Kit (BDK) release.

<table>
<caption><p><span id="_Ref484611329" class="anchor"></span>Table : RPC Broker Patch XWB*1.1*73 Deployment Timeline</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 27%" />
<col style="width: 14%" />
<col style="width: 34%" />
<col style="width: 18%" />
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
<td>EPMO Implementation Team</td>
<td>Installation</td>
<td>Ensure authority to operate and that certificate authority security documentation is in place.</td>
<td>Release Prep Phase</td>
</tr>
<tr class="odd">
<td>8</td>
<td>EPMO Implementation Team<br />
VistA Infrastructure (VI) Development Team</td>
<td>Installations</td>
<td>Coordinate training.</td>
<td>Release Prep Phase</td>
</tr>
<tr class="even">
<td>9</td>
<td>EPMO Implementation Team<br />
VistA Infrastructure (VI) Development Team</td>
<td>Back-Out</td>
<td>Confirm availability of back-out instructions and back-out strategy (what are the criteria that trigger a back-out).</td>
<td>Build Phase</td>
</tr>
<tr class="odd">
<td>10</td>
<td>SDE Field Operations (FO)<br />
Enterprise Operations (EO)</td>
<td>Post Deployment</td>
<td>Hardware, Software and System Support.</td>
<td>Post Release</td>
</tr>
</tbody>
</table>

<span id="_Ref484611329" class="anchor"></span>Table : RPC Broker Patch XWB\*1.1\*73 Deployment Timeline

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the RPC Broker 1.1 Patch XWB\*1.1\*73 Broker Development Kit (BDK) deployment.

The RPC Broker 1.1 Patch XWB\*1.1\*73 BDK deployment is planned as a simultaneous rollout. National release is scheduled for September 2021.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker 1.1 Patch XWB\*1.1\*73 BDK deployment and installation is scheduled to run for 30 days from release, which is the typical Veterans Health Information Systems and Technology Architecture (VistA) national patch rollout schedule.

<u>Table 4</u> provides an *estimate* of the RPC Broker Patch XWB\*1.1\*73 deployment timeline dates:

<table>
<caption><p><span id="_Ref473643192" class="anchor"></span>Table : Site Preparation</p></caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 31%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>Deployment</th>
<th>Start</th>
<th>Finish</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Patch Development and Release</td>
<td>04/08/2021</td>
<td>09/30/2021<br />
Est. Release September 2021</td>
</tr>
<tr class="even">
<td>Site Installation and Deployment</td>
<td>Not Applicable (N/A); <a href="#notice"><strong><sup>*</sup></strong>See NOTICE below</a>.</td>
<td>N/A; <a href="#notice"><strong><sup>*</sup></strong>See NOTICE below</a>.</td>
</tr>
<tr class="odd">
<td>Sustainment</td>
<td>N/A; <a href="#notice"><strong><sup>*</sup></strong>See NOTICE below</a>.</td>
<td>N/A; <a href="#notice"><strong><sup>*</sup></strong>See NOTICE below</a>.</td>
</tr>
</tbody>
</table>

<span id="_Ref473643192" class="anchor"></span>Table : Site Preparation

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/013.png) <span id="notice" class="anchor"></span><sup>\*</sup>NOTICE: There is no VistA site installation, deployment, or sustainment required by RPC Broker Patch XWB\*1.1\*73. This patch is a Programmer-Only Client Workstation installation. There is no VistA M Server installation required with this patch (i.e., no VistA PackMan or KIDS files). Also, there are no client side (Windows executable) programs for *Standard* Client Workstations. The patch is intended for Delphi developer client workstations only.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Site Readiness Assessment for the locations that will receive the RPC Broker 1.1 Patch XWB\*1.1\*73 deployment. This will be a typical national release of a VistA patch to all VistA production sites.

Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Field Office (FO), National Data Center Program (NDCP), and Austin Information Technology Center (AITC) during the design phase as appropriate. Field site coordination is done by FO unless otherwise stipulated by FO.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the deployment topology (local sites, etc.) for RPC Broker 1.1 Patch XWB\*1.1\*73.

RPC Broker 1.1 Patch XWB\*1.1\*73 will be distributed to local and regional system administrators and support personnel responsible for each of the 130 VistA parent systems. The actual code will be available to developers from the Product Support (PS) Anonymous Directories. (The code will be available to developers from secure file transfer (SFTP) sites listed in the patch description.)

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the physical locations (sites) that will host the deployed RPC Broker 1.1 Patch XWB\*1.1\*73.

The RPC Broker 1.1 Patch XWB\*1.1\*73 code is directly deployed to VA sites. The code is available to developers of Embarcadero Delphi Graphical User Interface (GUI) applications. The code is compiled into the applications and is then deployed to the sites that use those applications.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the preparation required for the site at which the system will operate.

There are no special site preparations or changes that *must* occur to the operational site and no specific features or items that need to be modified to adapt to RPC Broker 1.1 Patch XWB\*1.1\*73.

As a precursor to the RPC Broker 1.1 Patch XWB\*1.1\*73 deployment, the RPC Broker documentation set (including this *Deployment, Installation, Back-Out, and Rollback Guide \[DIBRG\]* and *Release Notes*) will be added to the VA Software Document Library (VDL) at: <https://www.va.gov/vdl/application.asp?appid=23>

<u>Table 5</u> describes preparation required by the site prior to deployment:

| Site/Other           | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------------|-----------------------|-----------------------------------------|---------------|-------|
| Not Applicable (N/A) | N/A                   | N/A                                     | N/A           | N/A   |

<span id="_Ref470091986" class="anchor"></span>Table : Hardware Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the hardware, software, facilities, documentation, and any other resources, other than personnel, required for the deployment and installation of RPC Broker 1.1 Patch XWB\*1.1\*73.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for installation of RPC Broker 1.1 Patch XWB\*1.1\*73 as it runs in a standard Microsoft Windows 32-bit operating system. There is also no need for specific hardware to assist in the deployment of RPC Broker 1.1 Patch XWB\*1.1\*73.

<u>Table 6</u> describes hardware specifications required at each site prior to deployment of RPC broker 1.1:

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-------------------|-------|---------|---------------|--------------|-------|
| N/A               | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Ref373317182" class="anchor"></span>Table : VistA M Server—Minimum Software Requirements

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/014.png) REF: For details about who is responsible for preparing the site to meet these hardware specifications, see <u>Table 3</u>.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the RPC Broker 1.1 can be a *multi-part* process. Separate software requirements are provided in this guide for each of the following target environments:

- <u>VistA M Server Software Requirements</u>
- <u>Standard Client Workstation Software Requirements</u>
- <u>Programmer-Only Client Workstation Software Requirements</u>

#### VistA M Server Software Requirements

<u>Table 7</u> lists the *minimum* software requirements for the VistA M Server in order to install and use RPC Broker 1.1:

<table>
<caption><p><span id="_Ref373317241" class="anchor"></span>Table : <em>Standard</em> Client Workstation—Minimum Software Requirements</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th>Software</th>
<th>Version</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>InterSystems Caché</td>
<td>2014.1.3 for Linux, Windows 7, and OpenVMS</td>
<td>Server Operating System Fully Patched.</td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>8.0</td>
<td><p>VistA Legacy Software Fully Patched M Accounts.</p>
<p>Patches <em>must</em> be installed in published sequence.</p></td>
</tr>
<tr class="odd">
<td>Kernel Toolkit</td>
<td>7.3</td>
<td><p>VistA Legacy Software Fully Patched M Accounts.</p>
<p>Patches <em>must</em> be installed in published sequence.</p></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td>22.2</td>
<td><p>VistA Legacy Software Fully Patched M Accounts.</p>
<p>Patches <em>must</em> be installed in published sequence.</p></td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td>1.1</td>
<td><p>VistA Legacy Software Fully Patched M Accounts.</p>
<p>Patches <em>must</em> be installed in published sequence.</p>
<p>You should have both a development Test account and a Production account for the Broker software.</p></td>
</tr>
<tr class="even">
<td>Linux, VMS, or Microsoft<sup>®</sup></td>
<td>TCP/IP</td>
<td>Server Network Communications Software. The server needs to have TCP/IP running.</td>
</tr>
</tbody>
</table>

<span id="_Ref373317241" class="anchor"></span>Table : *Standard* Client Workstation—Minimum Software Requirements

#### *Standard* Client Workstation Software Requirements

<u>Table 8</u> lists the *minimum* software requirements for the *Standard* Client Workstation in order to install and use RPC Broker 1.1:

<table>
<caption><p><span id="_Ref373317375" class="anchor"></span>Table : <em>Programmer-Only</em> Client Workstation—Minimum Software Requirements</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 23%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Software</th>
<th>Version</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Microsoft<sup>®</sup> Windows</td>
<td><ul>
<li><p>Windows Server 2012 R2</p></li>
<li><p>10</p></li>
<li><p>8.1</p></li>
<li><p>7</p></li>
</ul></td>
<td>Fully Patched Operating System.</td>
</tr>
<tr class="even">
<td>Microsoft<sup>®</sup></td>
<td>TCP/IP</td>
<td>Network Communications Software The RPC Broker requires networked client workstations running Microsoft’s<sup>®</sup> native TCP/IP stack.</td>
</tr>
</tbody>
</table>

<span id="_Ref373317375" class="anchor"></span>Table : *Programmer-Only* Client Workstation—Minimum Software Requirements

#### *Programmer-Only* Client Workstation Software Requirements

The workstation requirements for *Programmer-Only* Client Workstations are the same as for *Standard* Client Workstations (see <u>Table 8</u> in Section <u>3.3.2.2</u>).

<u>Table 9</u> lists the additional *minimum* software requirements for the *Programmer-Only* Client Workstation in order to install and use RPC Broker 1.1 Patch XWB\*1.1\*73 BDK release:

<table>
<caption><p><span id="_Ref473643112" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 22%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th>Software</th>
<th>Version</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Delphi</td>
<td><ul>
<li><p>10.4</p></li>
<li><p>10.3</p></li>
<li><p>10.2</p></li>
<li><p>10.1</p></li>
<li><p>10.0</p></li>
<li><p>XE8</p></li>
</ul></td>
<td><p>(required) For the Broker Development Kit (BDK).</p>
<p>Delphi is <em>not</em> required for developers who use the RPC Broker Dynamic Link Library (DLL), rather than the TRPCBroker Delphi component. For such developers, any development product that supports linking to 32-bit Microsoft<sup>®</sup> Windows DLLs can be used.</p>
<p>The RPC Broker 1.1 (and greater) does <em>not</em> support development of Delphi in the following environments:</p>
<ul>
<li><p>64-bit environment.</p></li>
<li><p>16-bit environments: Delphi 1.0 16-bit (i.e., Microsoft<sup>®</sup> Windows 3.1 and below) applications. However, the Broker routines on the VistA M Server continue to support VistA applications previously developed in the 16-bit environment.</p></li>
</ul>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/015.png) CAUTION: This statement defines the extent of support relative to use of Delphi. The Office of Information and Technology (OIT) only supports the Broker Development Kit (BDK) running in the currently offered version of Delphi and the immediately previous version of Delphi. This level of support became effective 06/12/2000.<br />
<br />
Sites can continue to use outdated versions of the RPC Broker Development Kit, but do so with the understanding that:</p>
<ul>
<li><blockquote>
<p><strong>Support is <em>not</em> available.</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Continued use of outdated versions does <em>not</em> afford features that can be essential to effective client/server operations in the VistA environment.</strong></p>
</blockquote></li>
</ul>
<blockquote>
<p><strong>An archive of old (<em>no longer supported</em>) Broker Development Kits is maintained in the VA Intranet Broker Archive.</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Ref473643112" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/016.png) REF: For details about who is responsible for preparing the site to meet these software specifications, see <u>Table 3</u>.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any notifications activities and how they will occur.

Prior to the deployment of the RPC Broker 1.1 Patch XWB\*1.1\*73 BDK release, a product announcement will be sent via email to current Points of Contact (POC) on record for each site describing the product and a brief description of the deployment and post-deployment support. Included will be links to the RPC Broker 1.1 VA Software Document Library (VDL) and Rational repositories, which contain further information about the release and the deployment, including the deployment schedule and required pre-installation activities.

The RPC Broker 1.1 Patch XWB\*1.1\*73 Implementation Team will respond to email requests for assistance and further information and, where appropriate, re-direct these requests to specialist technical staff.

#### Deployment/Installation/Back-Out Checklist

Tracking of installation for VistA RPC Broker patches is monitored in FORUM.

<u>Table 10</u> provides a checklist to be used to capture the coordination effort and document the day/time/individual when each activity (deploy, install, back-out) is completed for standard RPC Broker 1.1 patch releases.

| Activity | Day | Time | Individual who completed task |
|----------|-----|------|-------------------------------|
| Deploy   |     |      |                               |
| Install  |     |      |                               |
| Back-Out |     |      |                               |

<span id="_Ref373318148" class="anchor"></span>Table : Pre-Installation and System Requirement Considerations *before* Installing the BDK

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 is client/server software that can involve a *multi-part* installation process. Separate installation procedures are provided in this guide for each of the following target environments:

- Veterans Health Information Systems and Technology Architecture (VistA) M Servers
- *Standard* Client Workstations
- *Programmer-Only* Client Workstations

RPC Broker Patch XWB\*1.1\*73 is a Broker Development Kit (BDK) release, but it only requires installation or subsequent back-out on the VistA M Server and *Programmer-Only* Client Workstations.

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the minimum requirements for the product to be installed.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/017.png) REF: For a list of the minimum hardware and software requirements, including platform, Operating System (OS), and storage requirements required for RPC Broker 1.1 Patch XWB\*1.1\*73 Broker Development Kit (BDK) release, see the following:

- Section <u>3.3.1</u>, “<u>Hardware</u>”
- Section <u>3.3.2</u>, “<u>Software</u>”

<u>Table 11</u> lists the items that installers should consider before installing the RPC Broker BDK:

<table>
<caption><p><span id="_Ref373317540" class="anchor"></span>Table : VistA M Server—Distribution Files</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Item</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Installation Sequence</strong></td>
<td>The <em>Programmer-Only</em> Client Workstation installation no longer requires that the <em>Standard</em> Client Workstation software be installed prior to installing the <em>Programmer-Only</em> Client Workstation.</td>
</tr>
<tr class="even">
<td><strong>Microsoft</strong><sup>®</sup> <strong>Windows Registry Access</strong></td>
<td>The RPC Broker Development Kit installation on the client workstation does <em>not</em> require Administrator privileges, as it is loaded into a standard Embarcadero Delphi development environment. The Embarcadero Delphi software may require administrative privileges to install if it is to be made available to all users on a workstation.</td>
</tr>
<tr class="odd">
<td><strong>Source Code</strong></td>
<td><p>The release of the source code does <em>not</em> affect how a developer uses the Broker components or other parts of the BDK.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/018.png) CAUTION: Modified BDK source code should <em>not</em> be used to create VistA GUI applications.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/019.png) <strong>NOTE:</strong> Suggestions for changes to the BDK should be done via Service Desk Manager (SDM) (for bugs) or NSR (for enhancements) for review and possible inclusion in a future patch.</p></td>
</tr>
<tr class="even">
<td><strong>DesignTime and RunTime Packages</strong></td>
<td><p>The BDK has separate <strong>RunTime</strong> and <strong>DesignTime</strong> packages. The packages are as follows:</p>
<ul>
<li><p>XWB_<strong>DXE<em>n</em></strong> or XWB_<strong>DesignTime</strong></p></li>
<li><p>XWB_<strong>RXE<em>n</em></strong> or XWB_<strong>RunTime</strong></p></li>
</ul>
<p>Where:</p>
<ul>
<li><p>“<strong>D</strong>”—<strong>DesignTime</strong></p></li>
<li><p>“<strong>R</strong>”—<strong>RunTime</strong></p></li>
<li><p>“<em><strong>XEn</strong></em>”—Number indicating the version of Delphi with which it should be used (e.g., <strong>XWB_DXE8</strong> is the <strong>DesignTime</strong> package for Delphi XE8). The “<strong>DesignTime</strong>” and “<strong>RunTime</strong>” packages are used by both Delphi 10 Seattle and 10 Berlin.</p></li>
</ul>
<p>The <strong>RunTime</strong> package should <em>not</em> be used to create executables that depend on a separate <strong>XWB_RXE<em>n</em>.bpl</strong> installed on client workstations. There is no procedure in place at this time to reliably install the correct version of the <strong>RunTime</strong> bpl on client workstations<em>.</em></p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/020.png) CAUTION: Do <em>not</em> compile your project so that it relies on dynamic linking with the BDK’s RunTime package; that is, do <em>not</em> check the “Build with runtime packages” box on the Packages tab of the Project Options dialogue.</p></td>
</tr>
<tr class="odd">
<td><strong>Package Dependencies</strong></td>
<td><p>A Package may have been defined to <em>require</em> the Broker package. Patch XWB*1.1*14 changed the identity of the Broker <strong>DesignTime</strong> package. If you try to install a package into the Delphi IDE that requires the Broker, you may receive an error message similar to the following:</p>
<p>Can’t load package &lt;Package1&gt;.<br />
One of the library files needed to run this package cannot be found.</p>
<p>To resolve this problem:</p>
<ol type="1">
<li><p>Open the DPK file associated with that package.</p></li>
<li><p>Delete the reference to the old version of the Broker in the “Requires” section.</p></li>
<li><p>Add a reference to the <strong>DesignTime</strong> Broker package (XWB_DXEn) into the “Requires” section.</p></li>
<li><p>Recompile and install the package.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Component Dependencies</strong></td>
<td><p>Some VA-developed components may reference the TRPCBroker component. If you develop applications using such components, be aware that installing a newer version of the TRPCBroker component may cause incompatibilities, until the Broker-dependent components have been recompiled with the new version of the TRPCBroker component. Any such incompatibilities would show up as a compilation error:</p>
<p>Unit &lt;Unit1&gt; was compiled with a different version of &lt;Unit2&gt;</p>
<p>To resolve this problem, you need to either of the following:</p>
<ul>
<li><p>Obtain the source code for the components so that you can recompile the components with the new BDK units.</p></li>
<li><p>Obtain a compiled version of their component that was compiled with the same version of the BDK you are using.</p></li>
</ul>
<p>The VA FileMan Delphi Components (FMDC) is one example of a package whose source code references the TRPCBroker component. Patch FMDC*1.0*1 was released to issue the FMDC source code, so that you can easily recompile FMDC whenever new BDKs are released.</p></td>
</tr>
<tr class="odd">
<td><strong>Delphi XE<em>n</em> Standard Edition</strong></td>
<td><p>Delphi comes in three flavors:</p>
<ul>
<li><p>Standard</p></li>
<li><p>Professional</p></li>
<li><p>Enterprise</p></li>
</ul>
<p>The Standard editions of Delphi are targeted mainly at students, and as such leaves out many features. The Standard Editions do <em>not</em> ship with Delphi’s OpenHelp help system. This makes it difficult to integrate the BDK help with Delphi XE<em>n</em>, Standard Editions.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/021.png) CAUTION: We do <em>not recommend</em> using the Standard Editions of Delphi for RPC Broker development at this time.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref373317540" class="anchor"></span>Table : VistA M Server—Distribution Files

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 Patch XWB\*1.1\*73 should be installed when RPC Broker-based applications on the *Programmer-Only* Client Workstation are *not* in use.

Installation of the *Programmer-Only* Client Workstations software distributed with this patch should take no longer than 5 minutes.

All VistA Infrastructure patches *must* be installed within 30 days of national release.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of the RPC Broker 1.1 can be a *multi-part* process. Separate download files are provided in this guide for each of the following target environments:

- <u>VistA M Server Distribution Files</u>
- <u>Standard Client Workstation Distribution Files</u>
- <u>Programmer-Only Client Workstation Distribution Files</u>

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/022.png) DISCLAIMER: RPC Broker Patch XWB\*1.1\*73 is a BDK release only for the VistA M Serve-side and *Programmer-Only* Client Workstation!  
  
There are no updates to the *Standard* Client Workstations, so you do *not* need to download files for that environment.

All RPC Broker software can be downloaded from the Product Support (PS) Anonymous Directories. Also, all RPC Broker documentation is available in Adobe<sup>®</sup> Acrobat PDF format and can be downloaded from the VA Software Document Library (VDL) website: <https://www.va.gov/vdl/application.asp?appid=23>

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/023.png) REF: Prior versions of RPC Broker software and documentation distributions can be obtained from the VA Intranet RPC Broker Archive website.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/024.png) NOTE: For all patches, first read the patch installation instructions in the patch description located in National Patch Module (NPM) on FORUM.  
  
REF: For any supplemental instructions *not* included in the manuals, see the latest Readme file (i.e., xwb_1_1_p73_rm.pdf file).

### VistA M Server Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/025.png) There are no RPC Broker 1.1 VistA M Server software routines distributed with the RPC Broker Patch XWB\*1.1\*73 BDK release! The VistA M Server software was last updated with RPC Broker Patch XWB\*1.1\*65.

Download the documentation distribution files in <u>Table 12</u> that were last updated with RPC Broker Patch XWB\*1.1\*65:

<table>
<caption><p><span id="_Ref373317133" class="anchor"></span>Table : <em>Standard</em> Client Workstation—Base Distribution Files</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 10%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>xwb_1_1_65_pd.pdf</strong></td>
<td>ASCII</td>
<td><p><strong>Patch Description</strong>. This provides any pre-installation instructions, instructions, and additional information to install the patch.</p>
<p>Follow all patch installation instructions.</p></td>
</tr>
<tr class="even">
<td><strong>xwb_1_1_ig.pdf</strong></td>
<td>Binary</td>
<td><strong>Installation Guide</strong> (manual). Use this manual in conjunction with the patch description on FORUM and any additional Readme text files.</td>
</tr>
<tr class="odd">
<td><strong>xwb_1_1_P65_readme.pdf</strong></td>
<td>Binary</td>
<td><strong>Readme File</strong> (manual). Use this manual in conjunction with the patch description on FORUM and any DIBRG files.</td>
</tr>
</tbody>
</table>

<span id="_Ref373317133" class="anchor"></span>Table : *Standard* Client Workstation—Base Distribution Files

### *Standard* Client Workstation Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/026.png) SKIP THIS STEP: You do *not* need to retrieve the distribution files in this section for RPC Broker Patch XWB\*1.1\*73 BDK release! The instructions in this section are retained here for historical reference only but may be updated in a *future* release.  
  
The *Standard* Client Workstation installation took place with the initial release of RPC Broker 1.1. There have been no updates to the *Standard* Client Workstation software since RPC Broker Patch XWB\*1.1\*58.

Download the base software distribution file in <u>Table 13</u> that was last updated with RPC Broker Patch XWB\*1.1\*58 and is needed to install the RPC Broker 1.1 software on the *Standard* Client Workstation:

<table>
<caption><p><span id="_Ref448845755" class="anchor"></span>Table : <em>Standard</em> Client Workstation—Interactive Installation Distribution Files</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>xwb1_1ws.exe</strong></td>
<td>Binary</td>
<td><p><strong><em>Standard</em> Client Workstation Software</strong> (client software). This is a self-installing executable. This software is installed on client workstations to run RPC Broker applications.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/027.png) <strong>REF:</strong> For more information, see the “System Features” section in the <em>RPC Broker Systems Management Guide</em>.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref448845755" class="anchor"></span>Table : *Standard* Client Workstation—Interactive Installation Distribution Files

Download the software and documentation distribution files in <u>Table 14</u> that are needed to interactively install the RPC Broker 1.1 software on the *Standard* Client Workstation.

<table>
<caption><p><span id="_Ref448845783" class="anchor"></span>Table : <em>Standard</em> Client Workstation—<em>Non</em>-Interactive Installation Distribution Files</p></caption>
<colgroup>
<col style="width: 21%" />
<col style="width: 10%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>xwb_1_1_rm.txt</strong></td>
<td>ASCII</td>
<td><p><strong>Readme File</strong> (manual). This file provides any pre-installation instructions, last minute changes, new instructions, and additional information to supplement the manuals.</p>
<p>Read all sections of this file prior to following the installation instructions in the <em>RPC Broker Deployment, Installation, Back-Out, and Rollback Guide</em> (i.e., <strong>xwb_1_1_ig.pdf</strong>).</p></td>
</tr>
<tr class="even">
<td><strong>xwb_1_1_ig.pdf</strong></td>
<td>Binary</td>
<td><strong>Installation Guide</strong> (manual). Use this manual in conjunction with the Readme text file (i.e., <strong>xwb_1_1_rm.txt</strong>).</td>
</tr>
<tr class="odd">
<td><strong>xwb1_1ws.exe</strong></td>
<td>Binary</td>
<td><p><strong><em>Standard</em> Client Workstation</strong> (client software). This is a self-installing executable. This software is installed on client workstations to run RPC Broker applications.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/028.png) <strong>REF:</strong> For more information, see the “System Features” section in the <em>RPC Broker Systems Management Guide</em>.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/029.png) CAUTION: This self-installing executable is <em>not</em> Windows 7 compatible and requires Admin privilege to run. In future releases, the RPC Broker Development Team will write an “msi” for files to be pushed to client workstations, rather than using the “exe” self-extracting loader.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref448845783" class="anchor"></span>Table : *Standard* Client Workstation—*Non*-Interactive Installation Distribution Files

Download the software and documentation distribution files in <u>Table 15</u> that are needed to *non*-interactively install the RPC Broker 1.1 software on the *Standard* Client Workstation:

<table>
<caption><p><span id="_Ref373316572" class="anchor"></span>Table : <em>Programmer-Only</em> Client Workstation—BDK Distribution Files</p></caption>
<colgroup>
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>xwb_1_1_rm.txt</strong></td>
<td>ASCII</td>
<td><p><strong>Readme File</strong> (manual). This file provides any pre-installation instructions, last minute changes, new instructions, and additional information to supplement the manuals.</p>
<p>Read all sections of this file prior to following the installation instructions in the <em>RPC Broker Deployment, Installation, Back-Out, and Rollback Guide</em> (i.e., <strong>xwb_1_1_ig.pdf</strong>).</p></td>
</tr>
<tr class="even">
<td><strong>xwb_1_1_ig.pdf</strong></td>
<td>Binary</td>
<td><strong>Installation Guide</strong> (manual). Use this manual in conjunction with the Readme text file (i.e., <strong>xwb_1_1_rm.txt</strong>).</td>
</tr>
<tr class="odd">
<td><strong>xwb1_1ws.exe</strong></td>
<td>Binary</td>
<td><p><strong><em>Standard</em> Client Workstation</strong> (client software). This is a self-installing executable. This software is installed on client workstations to run RPC Broker applications.</p>
<p>![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/030.png) <strong>REF:</strong> For more information, see the “System Features” section in the <em>RPC Broker Systems Management Guide</em>.</p></td>
</tr>
<tr class="even">
<td><strong>xwb_dflt.ini</strong></td>
<td>ASCII</td>
<td><strong>Initialization File</strong> (client software). Use for <em>non</em>-interactive installation of the Broker on <em>Standard</em> Client Workstations.</td>
</tr>
</tbody>
</table>

<span id="_Ref373316572" class="anchor"></span>Table : *Programmer-Only* Client Workstation—BDK Distribution Files

### *Programmer-Only* Client Workstation Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download the software and documentation distribution files in <u>Table 16</u> that are needed to install the RPC Broker 1.1 Broker Development Kit (BDK) Patch XWB\*1.1\*73 software on the *Programmer-Only* Client Workstation. This version of the BDK supports Delphi Versions: 10.4, 10.3, 10.2, 10.1, 10.0, and XE8.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 9%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th>Type</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>xwb_1_1_73_rm.pdf</strong></td>
<td>Binary</td>
<td><p><strong>Readme File</strong> (manual). This file provides any pre-installation instructions, last minute changes, new instructions, and additional information to supplement the manuals.</p>
<p>Read all sections of this file prior to following the installation instructions in the <em>RPC Broker Deployment, Installation, Back-Out, and Rollback Guide</em> (i.e.,<strong> xwb_1_1_73_dibrg.pdf</strong>).</p></td>
</tr>
<tr class="even">
<td><strong>xwb_1_1_73_dibrg.pdf</strong></td>
<td>Binary</td>
<td><strong>Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)</strong> (manual). Use this manual in conjunction with the Readme text file (i.e., <strong>xwb_1_1_73_rm.pdf</strong>).</td>
</tr>
<tr class="odd">
<td><strong>xwb_1_1_dg.pdf</strong></td>
<td>Binary</td>
<td><strong>Developer’s Guide</strong> (manual).</td>
</tr>
<tr class="even">
<td><strong>xwb_1_1_ug.pdf</strong></td>
<td>Binary</td>
<td><strong>User Guide</strong> (manual).</td>
</tr>
<tr class="odd">
<td><strong>xwb_1_1_sm.pdf</strong></td>
<td>Binary</td>
<td><strong>Systems Management Guide</strong> (manual).</td>
</tr>
<tr class="even">
<td><strong>xwb_1_1_tm.pdf</strong></td>
<td>Binary</td>
<td><strong>Technical Manual</strong> (manual).</td>
</tr>
<tr class="odd">
<td><strong>xwb_1_1_rn.pdf</strong></td>
<td>Binary</td>
<td><strong>Release Notes</strong> (manual).</td>
</tr>
<tr class="even">
<td><strong>XWB_1_1_P73.ZIP</strong></td>
<td>Binary</td>
<td><p><strong><em>Programmer-Only</em> Client Workstation Software</strong> (client software). This is a Zip file that contains the following:</p>
<ul>
<li><p>Source code.</p></li>
<li><p>Samples.</p></li>
<li><p>Broker Development Kit (BDK): Provides the RPC Broker Delphi Components for development of RPC Broker-enabled applications.</p></li>
</ul></td>
</tr>
</tbody>
</table>

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 does *not* create any required databases. It uses the already installed VA FileMan database.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 does *not* provide any installation scripts.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 does *not* provide any cron scripts.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General skills required to perform the RPC Broker 1.1 installation are listed below:

- Back up the system

*\[VistA M Server and Programmer-Only/Standard Client Workstations\]*

- Create directories on the Host file system

*\[Programmer-Only/Standard Client Workstation\]*

- Copy files using commands of the Host file system

*\[VistA M Server and Programmer-Only/Standard Client Workstations\]*

- Run a Kernel Installation & Distribution System (KIDS) installation

*\[VistA M Server\]*

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/031.png) REF: Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as other VA and VistA publications.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Separate installation procedures are provided in this guide for each of the following target environments:

- <u>VistA M Server Installation Instructions</u>
- <u>*Standard* Client Workstation Installation Instructions</u>—For *Standard* Client Workstations, two methods are provided for installing the RPC Broker client software:
- <u>Interactive Installation Instructions</u>—User input required.
- <u>*Non-Interactive* Installation Instructions</u>—“Silent”; no user input required.
- <u>*Programmer-Only* Client Workstation Installation Instructions</u>

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/032.png) DISCLAIMER: RPC Broker Patch XWB\*1.1\*73 is a BDK release with updates only to the *Programmer-Only* Client Workstations!  
  
There are no updates to the VistA M Server software and *Standard* Client Workstations, so you do *not* need to do any installation for that environment.

### VistA M Server Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/033.png) SKIP THIS STEP: Since there are no VistA M Server software routines distributed with the RPC Broker Patch XWB\*1.1\*73 BDK release, you do *not* need to perform the installation steps in this section! The RPC Broker 1.1 VistA M Server software was last updated with RPC Broker Patch XWB\*1.1\*65.  
  
The instructions in this section are retained here for historical reference only but may be updated in a *future* release.

The instructions in this section are applicable for the Test and Production accounts in the Caché environment.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/034.png) NOTE: Install the server software in a Test account prior to installing it in a Production account.

#### Confirm Distribution Files *(recommended)*

Verify that you have downloaded the files listed in <u>Table 12</u>.

#### Retrieve Released RPC Broker 1.1 Patches *(required)*

Prior to installation of the RPC Broker Development Kit, all current server-side patches should be installed.

Obtain all released RPC Broker 1.1 server-side patches from the Patch Module on FORUM or through normal procedures.

#### Install RPC Broker Patch XWB\*1.1\*73 *(required)*

On the VistA M server use KIDS to install RPC Broker Patch XWB\*1.1\*73 (i.e., routines and remote procedures). Follow the instructions in the "Patch Installation" section in the Patch XWB\*1.1\*73 Patch Description (PD) document located on the National Patch Module (NPM) on FORUM.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/035.png) REF: For more information on KIDS, see the *Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide*: <https://www.va.gov/vdl/application.asp?appid=10>

#### Setup for XWB LISTENER STARTER Option *(recommended)*

The XWB LISTENER STARTER option needs some setup performed, so that it knows how to specify on what nodes to launch listeners.

To set up the XWB LISTENER STARTER option on a server where the listener processes are started within VistA, perform the following procedure:

1.  Use VA FileMan to edit the BOX-VOLUME PAIR (#.01) field in the TASKMAN SITE PARAMETERS (#14.7) file. For each Box-Volume pair where you plan to run a Broker Listener, make sure that the Box-Volume pair is entered in the BOX-VOLUME PAIR field.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/036.png) REF: For more information on configuring TaskMan, see the “Task Manager System Management: Configuration” section in the *Kernel 8.0 & Kernel Toolkit 7.3 Systems Management Guide* located on the VDL at: <http://www.va.gov/vdl/application.asp?appid=10>

2.  Type the following at the M prompt:

S XWBCHK=“ALLOW”

3.  Invoke VA FileMan using D Q^DI and edit the RPC BROKER SITE PARAMETERS (#8994.1) file:
1.  Select your site domain in the DOMAIN NAME (#.01) field; only one entry is allowed here.
2.  For nodes where you plan to run Broker Listeners, enter/make sure their Box-Volume pairs are entered in the BOX-VOLUME PAIRS (#.01) subfield of the LISTENER (#7) Multiple:
- For each Box-Volume pair enter all the ports in the PORT (#.01) subfield of the PORT Multiple that you plan to use for the Listeners.
- Also, enter the UCI in the UCI (#1) field of the PORT Multiple where the Listener should run.

To set up the XWB LISTENER STARTER option on a server where the listener processes are started as an operating system process (e.g., Linux), create a script to be run by the operating system. For Linux, create a xinetd.d script to define the process to be started as shown in <u>Figure 1</u>:

<span id="_Ref470097935" class="anchor"></span>Figure : Sample Linux xinetd.d Script to Define the Listener Process to be Started

\#default: on

\#description: VA RPC Broker Listener for Sample VistA - port \<REDACTED\>

\#

service sam_rpct

{

type = UNLISTED

disable = no

flags = REUSE

socket_type = stream

protocol = tcp

port = \<REDACTED\>

wait = no

user = samtcpip

env = TZ=/usr/share/zoneinfo/US/Pacific

server = /srv/vista/sam/cache/samr0tsvr/bin/csession

server_args = samr0tsvr -ci -U SAM CACHEVMS^XWBTCPM

instances = UNLIMITED

per_source = UNLIMITED

}

\#end

#### Start the Broker Listener on the Server *(recommended)*

RPC Broker 1.1 uses an M Listener that should always be running in the background, listening to a known port. To start a single Listener on a given port on a server where the listener processes are started within VistA, perform the following procedure:

1.  Log into the VistA M Server.
4.  Enter the following command at the M prompt:

D STRT^XWBTCP(*\<listener port\>*)

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/037.png) NOTE: Sites can choose any available *\<listener port\>* greater than 1024 (i.e., sockets 1 to 1024 are reserved for standard, well-known services such as SMTP, FTP, Telnet, etc.).

Alternatively, with Caché, you can invoke VA FileMan (D Q^DI) and edit the RPC BROKER SITE PARAMETERS (#8994.1) file. Set the STATUS field to START and, assuming that TaskMan is running, the Listener is started. The STATUS field changes to RUNNING.

#### Automatically Start the Broker Listeners *(optional)*

The XWB LISTENER STARTER option can be used to start all configured Broker Listeners at one time on a server where the listener processes are started within VistA (i.e., listeners configured to start in the RPC Broker’s site parameters). Additionally, this option can be used to automatically start all of the Listener processes you need when TaskMan starts up, such as after the system is rebooted or configuration is restarted.

For servers where listeners are started as an operating system process, consult the operating system documentation regarding automatically starting processes.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/038.png) REF: For information on automatically starting the Broker Listeners via the XWB LISTENER STARTER option, see the “Broker Listeners and Ports” section in the *RPC Broker Systems Management Guide*.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/039.png) CONGRATULATIONS: The installation of the RPC Broker software on the *VistA M Server* is complete!

### *Standard* Client Workstation Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/040.png) SKIP THIS STEP: You do *not* need to perform the installation steps in this section for RPC Broker Patch XWB\*1.1\*73 BDK release! The instructions in this section are retained here for historical reference only but may be updated in a *future* release.  
  
The *Standard* Client Workstation installation took place with the initial release of RPC Broker 1.1. There have been no updates to the *Standard* Client Workstation software since RPC Broker Patch XWB\*1.1\*58.

Two sets of instructions are provided for *Standard* Client Workstations:

- Interactive
- *Non*-Interactive

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/041.png) CAUTION: RPC Broker 1.0 distributed and installed the RPCBI.DLL and Client Manager (i.e., CLMAN.EXE) in the VISTA/Broker directory on the *Standard* Client Workstation. RPC Broker 1.1 does *not* use these files; however, they should *not* be removed from client workstations.

#### Interactive Installation Instructions

#### Confirm Distribution Files *(recommended)*

Verify that you have downloaded the files listed in <u>Table 13</u> and <u>Table 14</u>.

#### Shut Down Microsoft<sup>®</sup> Windows Applications *(required)*

You *must not* be running *any* application that uses the Broker during the installation. It is also *recommended* that you shut down all other Microsoft<sup>®</sup> Windows-based applications running on the workstation.

#### Shut Down the Client Agent *(required)*

If the RPC Broker Client Agent is running, shut it down. To determine if the Client Agent is running, look in the workstation’s menu bar tray. If you see one of the following the RPC Broker Client Agent icons, the Client Agent is running:

<span id="_Toc82525226" class="anchor"></span>Figure : RPC Broker Client Agent Icons (connected, *not* connected)

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/042.png)Or ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/043.png)

If it is running, to shut down the Broker Client Agent, do one of the following:

- Right-click on the RPC Broker Client Agent icon in the workstation’s menu bar tray and choose ShutDown from the pop-up Client Agent menu.
- Double-click on the RPC Broker Client Agent icon to open the Client Agent window, and then click ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/044.png) in that window.

At the prompt “If you close the client agent, your ability to access the VistA server may be reduced. Do you want to proceed with closing the client agent?” select Yes.

#### Run the Installation Program *(required)*

Run XWB1_1WS.EXE on the client workstation, which starts the interactive *Standard* Client Workstation installation. For example, on a Microsoft<sup>®</sup> Windows 7 system, perform the following procedure:

1.  Go to the Start menu.
5.  Select the Run option (may need to enable the Run command first in Windows 7).
6.  Click Browse to locate XWB1_1WS.EXE.
7.  Click OK to run XWB1_1WS.EXE.
8.  Follow the online instructions provided when you run the installation program. We *strongly recommend* the following:
1.  Accept default directories—When prompted to accept the default Broker Directories, click OK.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/045.png) CAUTION: RPC Broker 1.1 is a 32-bit application. We *strongly recommend* that you load it in a separate directory from any previously installed RPC Broker 1.0 16-bit application.

3.  Always start the Client Agent—When prompted whether to always start the Broker Client Agent, click Yes. This starts the Broker Client Agent whenever Microsoft<sup>®</sup> Windows starts.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/046.png) REF: For a complete listing of installed client files after installation, see the “Files” section in the *RPC Broker Technical Manual*.

#### Restart Microsoft<sup>®</sup> Windows *(recommended)*

Restart Microsoft<sup>®</sup> Windows so the latest version of the Broker Client Agent is running.

#### Add Listeners/Ports to the Microsoft<sup>®</sup> Windows Registry *(optional)*

If system administrators want to add, modify, or delete servers and ports to be used by the Broker, see the “Edit Broker Servers Application” section in the *RPC Broker Systems Management Guide*.

#### *Non*-Interactive Installation Instructions

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/047.png) CAUTION: The *Standard* Client Workstation installation does more than copy files into directories; it also makes entries in the Microsoft<sup>®</sup> Windows Registry. Thus, simply doing a mass copy of files from a server to various *Standard* Client Workstations is insufficient.

#### Confirm Distribution Files (*recommended*)

Verify that you have downloaded the files listed in <u>Table 13</u> and <u>Table 15</u>.

#### Load and Run XWB1_1WS.EXE with Switches *(required)*

Prior to beginning an installation, you *must not* be running the Broker Client Agent or *any* application that uses the Broker during the installation. It is also *recommended* that you shut down all other Microsoft<sup>®</sup> Windows-based applications running on the workstation.

To start the *non*-interactive *Standard* Client Workstation installation setup program, run XWB1_1WS.EXE *with switches:*XWB1_1WS.EXE /S AUTO

The switches *must* be in UPPERCASE. Follow the procedures on how to run a program *non*-interactively as described in your operating system’s systems manual.

#### Finish Remaining Installation Tasks *(recommended)*

To complete the *non*-interactive installation, follow the steps in Sections <u>4.8.2.1.5</u> – <u>4.8.2.1.6</u> of the “<u>Interactive Installation Instructions</u>” section. Special workstation management software and/or local procedures may enable you to perform these remaining steps *non*-interactively.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/048.png) CONGRATULATIONS: The installation of the RPC Broker software on the *Standard* Client Workstation is complete!

### *Programmer-Only* Client Workstation Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker 1.1 Patch XWB\*1.1\*73 Broker Development Kit (BDK) software gets installed on *Programmer-Only* Client Workstations. There are separate installation procedures, depending on the Delphi version for which support is needed:

- Delphi/RAD Studio v10.4
- Delphi 10.3
- Delphi 10.2
- Delphi 10.1
- Delphi 10.0
- Delphi XE8

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/049.png) NOTE: Delphi Versions *prior* to Delphi XE8 are no longer supported.

#### Confirm Distribution Files *(recommended)*

Verify that you have downloaded the files listed in Table 16.

#### Uninstall any Previous BDK Installed with Delphi *(required)*

To uninstall any previous BDK installed with Delphi, perform the following procedure:

1.  Start Delphi and close any open projects.
9.  From the Delphi menu, select Component \| Install Packages.
10. Remove any previous version of the BDK from the Design Packages listing. To do this:
1.  Scroll through the listing of installed design packages until you find the entry for the previous version of the BDK (e.g., TRPCBroker).

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/050.png) NOTE: The name of the previous BDK version may be: VistA RPC Broker, VistaBroker, or it may start with the pattern VistA Broker -- designtime\*.  
  
The remainder of this section refers to this package as *YourOldBroker*.

2.  Select (highlight) this entry.
3.  Click Remove.
4.  Delphi presents one of two confirmation dialogue boxes, which say one of the following:

Confirm 1:

Remove ‘c:\program files\\..\\*YourOldBroker*.bpl’ from the design package list?

If Delphi presents this confirmation dialogue, click Yes.

Confirm 2:

Package(s) *xxx* will be uninstalled because they require package *YourOldBroker*. Continue remove?

If this is correct, press OK.

Any packages dependent on the RPC Broker are also uninstalled. You need to re-install them after you install or update the TRPCBroker component files. If you click No, you *cannot* uninstall the previous RPC Broker software.

5.  If you chose to remove any packages, Delphi may also present a “Remove Runtime Packages” dialogue, stating:

The package names in the following list are not used by any installed packages. Remove the selected names from the runtime packages list?

If Delphi presents this dialogue, press Yes or OK.

6.  Press OK in the “Project Options” dialogue box to finish the uninstallation.
11. Close Delphi; answer No if you are prompted to save changes to any projects.

#### Install the RPC Broker Software *(required)*

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/051.png) CAUTION: Prior to installing the RPC Broker, make sure that you exit/close *all* versions of Delphi running on your system.

To install the RPC Broker BDK software, perform the following procedure:

1.  <span id="install_bdk_software_step_01" class="anchor"></span>Navigate to the following directory:

C:\Program Files (x86)\VistA

2.  <span id="install_bdk_software_step_02" class="anchor"></span>Backup existing RPC Broker Development Kit (BDK) software: Rename the existing BDK32 directory (e.g., BDK32_P72; XWB\*1.1\*72 was the previous BDK release) to maintain the existing files as a backup.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/052.png) NOTE: You need Administrator privileges on your computer to write to this directory.

Alternatively, copy the renamed backup files into a separate directory that you control. For example:

C:\Users\\*\<YourName\>*\My Documents\\BDK32_P72

3.  Unzip xwb_1_1_p73.zip file in the directory in [Step 1](#install_bdk_software_step_01), making sure the “use folders” box is checked; this creates the BDK32 directory and subdirectories under the VistA directory in [Step 1](#install_bdk_software_step_01).
4.  After unzipping (installing) the zip file components, there should be a BDK32 directory with the following subdirectories:
- BAPI32dll—Contains the sample header files for using RPC Broker functions from other programming languages
- BAPI32_73—Contains the Bapi32.dll project files for building the BDK library (DLL) for use with other programming languages (C#, Visual Basic, etc.)
- Help—Contains the RPC Broker Help file (.pdf).
- Samples—Contains sample programs compiled with Delphi 10 Seattle.
- BrokerEx—Contains BrokerExample
- BSE—Contains a Broker Security Enhancement sample application
- Source—Contains the source code and related files for the components.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/053.png) NOTE: The BDK installation supports several different versions of Delphi, which as of patch XWB\*1.1\*73 includes Delphi Versions: 10.4, 10.3, 10.2, 10.1, 10.0, and XE8.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/054.png) NOTE: The ServerList.exe application has *not* been updated since patch XWB\*1.1\*60. This “beta” application can be used to set Windows Registry IPv4 or IPv6 entries for VistA server address/port/SSHUser combinations. This is *not* a released version and has *not* been field tested or reviewed for Section 508 compliance.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/055.png) NOTE: The “Bin” directory is gone. Users are now instructed to compile the BDK themselves, which creates the bpl and dcp files in a directory set by their Delphi environment (varies by version).

5.  Open Delphi.
6.  Enter the directories into the Library path fields:
1.  Open the menu Tools \| Options.
4.  Expand the Environment Options \| Delphi Options and select the Library tab.
5.  Press the ellipsis (…) at the right of the combo box for Library path.
6.  Add entries for the following paths ahead of all other entries:
- C:\Program Files (x86)\VistA\BDK32 (should be first in the list)
- C:\Program Files (x86)\VistA\BDK32\Source
7.  After entering both directories, press OK to close the dialogue.
7.  To install the components into Delphi, it is best to compile and build them in your version of the Delphi IDE, so that all of the necessary files are placed in the proper default directories during installation.  
      
    In the instructions that follow, replace the “*\#*” with your version of Delphi (e.g., “#” should be replaced with “8” for Delphi XE8). For Delphi 10 Seattle or 10 Berlin, use the “DesignTime” and “RunTime” packages.
8.  Select the menu File \| Open and select the XWB_RXE*\#*.dpk (or XWB_RunTime.dpk) file from the BDK32\Source directory.
9.  For the R or RunTime files:
1.  Right-click on the XWB_RXE*\#*.bpl (or XWB_RunTime.bpl) file in the Project Manager dialogue.
2.  Click Compile.
3.  Select the menu File \| Close All; respond YES if it asks to save changes.

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/056.png) NOTE: The RunTime files should always be compiled first, since the DesignTime files are dependent upon them.

10. Select the menu File \| Open and select the XWB_DXE*\#*.dpk (or XWB_DesignTime.dpk) file from the BDK32\Source directory:
1.  Right-click on the XWB_DXE*\#*.bpl (or XWB_DesignTime.bpl) file in the Project Manager dialogue.
2.  Click Build.
11. For the D or DesignTime files:
1.  Right-click on the XWB_DXE*\#*.bpl (or XWB_DesignTime.bpl) file in the Project Manager dialogue.
2.  Click Install to install or update the version of the component.
3.  Close *all* files; respond YES if it asks to save changes.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the installation of the RPC Broker BDK components in Delphi, verify the component installation. If the RPC Broker components installed correctly, you should see the following components on the Kernel tab of the Delphi palette:

- ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/057.png)—TCCOWRPCBroker
- ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/058.png)—TContextorControl
- ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/059.png)—TRPCBroker (original component)
- ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/060.png)—TXWBRichEdit
- ![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/061.png)—TXWBSSOiToken

![](xwb-1-1-73-deployment-installation-back-out-and-rollback-guide-dibrg/062.png) CONGRATULATIONS: The installation of the RPC Broker software on the *Programmer-Only* Client Workstation is complete! You are now ready to work with the RPC Broker interface and Broker Development Kit (BDK) to install VistA GUI applications that use the RPC Broker.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker 1.1 Patch XWB\*1.1\*73 does *not* require any system configuration.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker 1.1 Patch XWB\*1.1\*73 does *not* require any database tuning.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the back-out strategy for RPC Broker Patch XWB\*1.1\*73, including the established time limits or other parameters that comprise the rationale for the strategy.

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from Veterans Health Administration (VHA) and Enterprise Program Management (EPMO). In the case of the initial release, a back-out would include removal of data, files, and routines. In the case of future patches and releases, the back-out strategy would be dependent on the contents of the released functionality and could include restoration of file definitions, routines, or data.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include impact on production Veterans Health Information Systems and Technology Architecture (VistA) end-users and impact on Wide Area Network (WAN).

RPC Broker 1.1 is client/server software that involves installation in the following environments:

- Veterans Health Information Systems and Technology Architecture (VistA) M Servers
- *Standard* Client Workstations
- *Programmer-Only* Client Workstations

RPC Broker Patch XWB\*1.1\*73 is a Broker Development Kit (BDK) release, but it only requires installation or subsequent back-out on the *Programmer-Only* Client Workstations.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for RPC Broker Patch XWB\*1.1\*73. There are no resources or standards set for RPC Broker load testing, and a load testing environment is *not* available.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) for the RPC Broker Patch XWB\*1.1\*73 is performed during development of Graphical User Interface (GUI) applications. RPC Broker BDK users are other developers. Multiple project teams, including CPRS and VistA Imaging, are already developing using this code. Upon release, all GUI applications that interface into VistA will use this BDK version.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker Patch XWB\*1.1\*73 back-out criteria follow existing VistA patch back-out procedures.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker Patch XWB\*1.1\*73 back-out risks are the same risks established with existing VistA patch back-out procedures.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with Veterans Health Administration (VHA), Office of Information and Technology (OIT), and Enterprise Program Management Office (EPMO) representatives.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA M Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker Patch XWB\*1.1\*73 BDK installation does *not* add any new or update any existing VistA M Server routines, so no back-out is required on VistA M Servers.

### *Standard* Client Workstations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker Patch XWB\*1.1\*73 BDK installation does *not* add any new or update any existing components on the *Standard* Client Workstation, so no back-out is required on *Standard* Client Workstations.

### *Programmer-Only* Client Workstations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker Patch XWB\*1.1\*73 installation provides an updated Broker Development Kit (BDK). To back-out the new BDK software and restore the previous BDK on the *Programmer-Only* Client Workstations, perform the following procedure:

1.  <span id="backout_programmer_workstation_step_1" class="anchor"></span>On the *Programmer-Only* Client Workstation, navigate to the following directory:

C:\Program Files (x86)\VistA

10. Delete the BDK32 directory.
11. Locate the BDK backup directory from [Step 2](#install_bdk_software_step_02) in Section 4.8.3.3. For example:

C:\Program Files (x86)\VistA\\BDK32_P72

Or:

C:\Users\\*\<YourName\>*\My Documents\\BDK32_P72

12. Rename the backup file to BDK32.
13. Copy the restored BDK32 to the directory in [Step 1](#backout_programmer_workstation_step_1).

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the BDK32 directory has been restored to the version released with RPC Broker Patch XWB\*1.1\*72, perform the following procedure:

1.  On the *Programmer-Only* Client Workstation, navigate to the following directory:

C:\Program Files (x86)\VistA\BDK32

14. Verify the following directory structure exists:
- BAPI32dll
- Help
- Samples
- BrokerEx
- BSE
- Source

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. This section includes the specific steps to roll back to the previous state of the data and platform settings, if required. It includes the order of restoration for multiple interdependent systems.

The Veterans Health Information Systems and Technology Architecture (VistA) RPC Broker Patch XWB\*1.1\*73 Broker Development Kit (BDK) does *not* export any other data, so a database rollback is *not* required.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 BDK release does *not* export any data, so there are no rollback considerations required.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 BDK release does *not* export any data that would require a rollback, so there is no rollback criteria.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 BDK release does *not* export any data that would require a rollback, so there are no rollback risks.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback *can* be authorized by system administrators once a problem has been identified. Office of Information and Technology (OIT) and Enterprise Program Management Office (EPMO) VistA Infrastructure (VI) Development Team should be informed immediately via a MailMan message sent to:

VA OIT PD Infrastructure Dev. & Doc. *\<\<REDACTED\>@va.gov\>*

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 BDK release does *not* export any data any data that would require a rollback, so no rollback procedure is required.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. RPC Broker Patch XWB\*1.1\*73 BDK release does *not* export any data any data that would require a rollback, so no rollback verification procedure is required.