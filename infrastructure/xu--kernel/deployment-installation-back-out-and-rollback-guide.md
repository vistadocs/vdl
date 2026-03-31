---
consolidated_title: "deployment, installation, back-out, and rollback guide"
app_code: XU
doc_type: DIBR
master_source: "XU*8*702 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
master_pub_date: August 2020
consolidated_from: 5 versions
prior_versions:
  - "XU*8*671 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
  - "XU*8*688 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
  - "XU*8*765 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
  - "XU*8*775 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)"
---

---
title: |
  <span id="_Hlk46159836" class="anchor"></span>Kernel 8.0; Patch XU\*8.0\*702

  Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)
---

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/001.png)

August 2020

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
<td>08/11/2020</td>
<td>1.3</td>
<td><p>Updates: Section <u>4.8.2.3</u>:</p>
<ul>
<li><p>Added explanatory note in Step 2, following <u>Figure 9</u>.</p></li>
<li><p>Added explanatory note in Step 4, following <u>Figure 11</u>.</p>
<p><strong>Kernel 8.0; Patch XU*8.0*702</strong></p></li>
</ul></td>
<td>VistA Infrastructure (VI) Development Team</td>
</tr>
<tr class="even">
<td>07/22/2020</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>4.5</u>, <u>4.8.2.1</u>, and <u>7.2.2</u>: Updated references to the DLL to reflect the latest version, which is Version <strong>8.0.702.3</strong>.</p></li>
<li><p>Section <u>4.8.2</u>, <u>4.8.2.3</u>, <u>Figure 8</u>, <u>Figure 10</u>, <u>Figure 11</u>, and <u>Figure 15</u>: Updated the <strong>.rdox</strong> file configuration steps that replace the old method. This resolves a latency issue found in the old setup where in some circumstances the Visual Basic (VB) script would not trigger.</p></li>
<li><p>Verified document is Section 508 conformant.</p>
<p><strong>Kernel 8.0; Patch XU*8.0*702</strong></p></li>
</ul></td>
<td>VistA Infrastructure (VI) Development Team</td>
</tr>
<tr class="odd">
<td>04/09/2020</td>
<td>1.1</td>
<td><p>Updates based on new DLL file for Patch XU*8.0*702 that is being pushed through SCCM:</p>
<ul>
<li><p>Section <u>4.3.1</u>; <u>Table 10</u>: Removed DLL reference within ZIP file. The DLL is pushed by SCCM nationally and will be available within Software Center. The DLL is <em>not</em> being released as part of the ZIP file.</p></li>
<li><p>Section <u>4.5</u>: Changed DLL version reference to <strong>8.0.702.2</strong>.</p></li>
<li><p>Section <u>4.8.2.1</u>: Changed DLL version reference to <strong>8.0.702.2</strong>.</p></li>
</ul>
<p>Section <u>7.2.2</u>; <u>Figure 15</u>: New screenshot of DLL properties window for DLL Version <strong>8.0.702.2</strong>, which was created on <strong>03/26/2020</strong>.</p>
<p><strong>Kernel 8.0; Patch XU*8.0*702</strong></p></td>
<td>VistA Infrastructure (VI) Development Team</td>
</tr>
<tr class="even">
<td>03/23/2020</td>
<td>1.0</td>
<td><p>Final Patch XU*8.0*702 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG) for release:</p>
<ul>
<li><p>Document baseline release revision number 1.0.</p></li>
<li><p>Deleted prior development document revision history.</p></li>
<li><p>Removed VA Intranet site links for upload to the VA Software Document Library (VDL) Internet site.</p></li>
</ul>
<p><strong>Kernel 8.0; Patch XU*8.0*702</strong></p></td>
<td>VistA Infrastructure (VI) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref473639233" class="anchor"></span>Table : Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc48043905" class="anchor"></span>List of Figures

<span id="_Toc48043906" class="anchor"></span>List of Tables

<span id="_Toc336760250" class="anchor"></span>

Orientation

How to Use this Manual

This manual provides advice and instructions for deploying and installing the Veterans Health Information Systems and Technology Architecture (VistA) Kernel Patch XU\*8.0\*702.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—VistA legacy and other development teams.
- System Administrators—Personnel responsible for regional and local computer management and system security on VistA M Servers and client workstations.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).
- Area Managers.
- Automated Data Processing Application Coordinator (ADPACS).
- Chief Health Informatics Officer (CHIO).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimer

This manual provides an overall explanation and functionality of Kernel Patch XU\*8.0\*702; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/004.png)       | NOTE/REF: Used to inform the reader of general information including references to additional reading material                   |
| ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/005.png) | CAUTION / DISCLAIMER /SKIP THIS STEP / RECOMMENDATION: Used to caution the reader to take special notice of critical information |

<span id="_Ref473643111" class="anchor"></span>Table : Roles and Responsibilities

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666.”
- Patient and user names are formatted as follows:
- \[Application Name\]PATIENT,\[N\]
- \[Application Name\]USER,\[N\]

Where “*Application Name*” is defined in the Approved Application Abbreviations document and “*N*” represents the first name as a number spelled out and incremented with each new entry.

For example, in Kernel (XU) test patient names would be documented as follows:

XUPATIENT,ONE; XUPATIENT,TWO; XUPATIENT,14, etc.

For example, in Kernel (XU) test user names would be documented as follows:

XUUSER,ONE; XUUSER,TWO; XUUSER,14, etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are in boldface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is in boldface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are in boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/007.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

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

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/009.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.  
  
REF: For more information, see the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/010.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel 8.0—VistA M Server software
- Remote Procedure Call (RPC) Broker 1.1—VistA Client/Server software
- VA FileMan 22.2 data structures and terminology—VistA M Server software
- M programming language
- Microsoft<sup>®</sup> Windows environment
- Terminal emulator software:

Micro Focus<sup>®</sup> Reflection (v16)

- Microsoft<sup>®</sup> Visual Basic Editor:

Ability to import macros as described in Section <u>4.8.2</u>, “<u>Client Workstation Instructions—Micro Focus® Reflection (v16)</u>.”

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/011.png) DISCLAIMER: The installation and configuration steps described in this manual should be performed by regional or local system administrators who maintain enterprise client workstations, as it requires Administrative privileges.  
  
The instructions in this manual are written and can be used to set up on an individual client workstation (Dynamic Link Library \[DLL\] and Visual Basic \[VB\] script); however, they are intended more for national (mass) deployment. These instructions are intended for regional or local system administrators to set up a “push” version of the Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software to invoke 2-Factor Authentication (2FA). The configured Reflection terminal emulator software would then be distributed (pushed) throughout the enterprise using a custom System Center Configuration Manager (SCCM) script to push the 2FA-enabled Reflection software settings files and the DLL to all required client workstations.

References

For additional information with regard to Patch XU\*8.0\*702 project team, 2FA, PIV, and IAM Link My Account, consult the following:

- Reflection PIV Project SharePoint (VA Intranet internal project team collaboration site)
- PIV Enabled Vista SharePoint (VA Intranet site)
- Link My Account Summary Sheet (VA Intranet site)
- PIV Help.docx(VA Intranet site)
- *Patch XU\*8.0\*702 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)* (this manual)
- *Patch XU\*8.0\*702 Quick Reference Guide*
- *Patch XU\*8.0\*702 VistA-Reflection PIV 2-Factor Authentication Test Plan* (VA Intranet site)

Readers who wish to learn more about Kernel should consult the following:

- *Kernel Release Notes*
- *Kernel Patch XU\*8.0\*702 Deployment, Installation, Back-Out, and Rollback Guide* (this manual)
- *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*
- *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*
- *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*
- Kernel VA Intranet website.  
    
  This site provides additional information, documentation links, archives of older documentation and software downloads.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) website: <http://www.va.gov/vdl/>

The Kernel documentation is located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=10>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Dependencies](#dependencies)
    - [Kernel Patch XU\8.0\702 Dependencies](#kernel-patch-xu80702-dependencies)
    - [2-Factor Authentication (2FA) Dependencies](#2-factor-authentication-2fa-dependencies)
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
    - [Distribution Files](#distribution-files)
    - [Extract Zip Files](#extract-zip-files)
    - [File and Documentation Maintenance](#file-and-documentation-maintenance)
  - [Database Creation](#database-creation)
  - [Installation DLL and VB Script](#installation-dll-and-vb-script)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
  - [Installation Procedure](#installation-procedure)
    - [VistA M Server Instructions](#vista-m-server-instructions)
    - [Client Workstation Instructions—Micro Focus<sup>®</sup> Reflection (v16)](#client-workstation-instructionsmicro-focussupsup-reflection-v16)
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
  - [Back-Out Verification Procedure](#back-out-verification-procedure)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
  - [Rollback Verification Procedure](#rollback-verification-procedure)
- [Troubleshooting](#troubleshooting)
  - [Installation Notes](#installation-notes)
    - [VistA M Server](#vista-m-server)
    - [Client Workstation](#client-workstation)
  - [DLL and .rdox Session Files](#dll-and-rdox-session-files)
    - [Phased Rollout of DLL and .rdox Files](#phased-rollout-of-dll-and-rdox-files)
    - [Verify Correct DLL File](#verify-correct-dll-file)
    - [Missing DLL](#missing-dll)
  - [Micro Focus Connection Setting/Configuration](#micro-focus-connection-settingconfiguration)
  - [New User Signon Processes](#new-user-signon-processes)
    - [Verify Code Expiration Bypass](#verify-code-expiration-bypass)
  - [Link My Account](#link-my-account)
  - [Technical Support](#technical-support)
  - [Issues and Concerns](#issues-and-concerns)
This document describes how to deploy and install the Veterans Health Information Systems and Technology Architecture (VistA) Kernel Patch XU\*8.0\*702, as well as how to back-out the product and rollback to a previous version or data set if required.
Kernel Patch XU\*8.0\*702 and associated components provides enhancements needed to implement Single Sign-On internal (SSOi) for identification and Personal Identification Verification (PIV) 2-Factor Authentication (2FA) of users into Veterans Health Information Systems and Technology Architecture (VistA) using the Micro Focus<sup>®</sup> Reflection \[v16\] terminal emulator software (see <u>Figure 1</u>).
Kernel Patch XU\*8.0\*702 adds code to VistA to accept an Identity and Access Management (IAM) Security Assertion Mark-up Language (SAML) token for PIV authentication using the Micro Focus<sup>®</sup> Reflection \[v16\] terminal emulator software.
Kernel Patch XU\*8.0\*702 provides the VistA Kernel utilities needed to implement the following requirements:
VAIQ \#7613595 "Mandatory Use of PIV Multifactor Authentication to VA Information Systems" dated June 30, 2015, requires all VA Information Technology (IT) systems to be Personal Identification Verification (PIV)-enabled and requires the use of multifactor authentication when using a local, network, or remote account to log into a VA information system.
The use of these utilities is expected to improve security and auditing capabilities in accordance with VA Handbook 6500, Appendix F and revision 4 of National Institute of Standards and Technology (NIST) SP 800-53. As required by Federal Information Processing Standards (FIPS) 199 and using guidance from NIST SP 800-60, the *recommended* security categorization for these applications is HIGH.
Integration with Identity and Access Management (IAM) services are mandated by executive management via the following memorandums:
- IAM Identity Services (IdS) mandate memorandum (VAIQ \#7011145). All applications within VA *must* comply with IAM requirements to ensure that references to the identities of Veterans and their beneficiaries are accurate.
- IAM Access Services (AcS) functionality within VA is mandated by VAIQ \#7060071 REDACTED
The Visual Basic (VB) script and Dynamic Link Library (DLL) files that are distributed in association with this patch release are used to enable Micro Focus<sup>®</sup> Reflection (v16) 2-Factor Authentication (2FA) into IAM, and use the received IAM SAML token to authenticate into VistA:
- DLL performs the authentication with IAM and returns a SAML token.
- VB script calls the DLL and passes the SAML token to VistA.
<span id="_Toc411336914" class="anchor"></span>
Figure : PIV 2FA Reflection Login Workflow
![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/012.png)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide a single, common document that describes how, when, where, and to whom the VistA Kernel Patch XU\*8.0\*702 is deployed and installed, as well as how it is to be backed out and rolled back, if necessary. This guide also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, rollback, and troubleshooting are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists and describes all application, system, financial, and other dependencies for this deployment, including upstream processing.

### Kernel Patch XU\*8.0\*702 Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VistA M Server—Kernel Patch XU\*8.0\*702 is dependent on [Kernel Patch XU\*8.0\*701](#kernel-patch-xu8.0701) and <u>Kernel Patch XU\*8.0\*659</u> being installed on the same VistA M Server.
- Client Workstation—The following terminal emulator software *must* be installed on the target client workstation in order to configure the software for 2-Factor Authentication (2FA):

Micro Focus<sup>®</sup> Reflection (v16)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/013.png) DISCLAIMER: Department of Veterans Affairs (VA) does *not* own or maintain the Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software. This document only describes how to configure that software to invoke 2-Factor Authentication (2FA). Ongoing maintenance of the Reflection software is outside the scope of this document.

There are no other direct dependencies; other than the typical operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

### 2-Factor Authentication (2FA) Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Except for Kernel Patch XU\*8.0\*659 and XU\*8.0\*701, the following Kernel and RPC Broker patches are *not* direct dependencies of Kernel Patch XU\*8.0\*702; however, these patches are required for the overall implementation of 2FA:

- <u>Kernel Patch XU\*8.0\*655</u> (released 09/15/2015)
- <u>Kernel Patch XU\*8.0\*659</u> (released 08/30/2016)
- [Kernel Patch XU\*8.0\*701](#kernel-patch-xu8.0701) (released 02/11/2020)
- Kernel Patch XU\*8.0\*702 (this patch)
- <u>RPC Broker Patch XWB\*1.1\*64</u> (released 11/18/2016)
- <u>RPC Broker Patch XWB\*1.1\*65</u> (released 03/27/2017)
- <u>RPC Broker Patch XWB\*1.1\*71</u> (release: TBD)

All of these patches adhere to the following policies:

- VAIQ \#7613595 "Mandatory Use of PIV Multifactor Authentication to VA Information Systems" dated June 30, 2015, requires all VA IT systems to be PIV-enabled and requires the use of multifactor authentication when using a local, network, or remote account to log into a VA information system.
- The use of these utilities is expected to improve security and auditing capabilities in accordance with VA Handbook 6500 Appendix F and revision 4 of NIST SP 800-53. As required by FIPS 199 and using guidance from NIST SP 800-60, the recommended security categorization for these applications is HIGH.
- Integration with Identity and Access Management (IAM) services are mandated by executive management via the following memorandums:
- IAM Identity Services (IdS) mandate memorandum (VAIQ \#7011145). All applications within VA must comply with IAM requirements to ensure that references to the identities of Veterans and their beneficiaries are accurate.
- IAM Access Services (AcS) functionality within VA is mandated by VAIQ \#7060071 REDACTED

#### Kernel Patch XU\*8.0\*655

Kernel Patch XU\*8.0\*655 provided enhanced Single Sign-On (SSO) utilities to support advanced models for identification and authentication of users into VistA. Specifically, Identity and Access Management (IAM):

- Ensured enterprise mandate for Personal Identity Verification (PIV) compliance was met for VistA access.
- Ensured Continuous Readiness in Information Security Program (CRISP) on-boarding and off-boarding enterprise mandate was met for VistA access.
- Automated and improved accuracy in creation of VistA accounts as a path to moving Veterans Health Administration (VHA) and Veterans Business Administration (VBA) applications away from reliance on "anonymous" VistA accounts that represented systems rather than people.
- Integrated VistA user management within the IAM context and provided mapping from the VistA user identifier and enterprise user identifiers (Active Directory \[AD\], PIV).
- Integrated all forms of user access to VistA ("roll-and-scroll" terminal session, Computerized Patient Record System \[CPRS\], calls from remote systems, etc.) with the IAM SSO user session.
- Added the following to be used by the IAM Binding application and the IAM Provisioning application (both in development):
- Five new remote procedures.
- Two context options.
- Two REMOTE APPLICATION (#8994.5) file entries.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/014.png) NOTE: Kernel Patch XU\*8.0\*655 was released 09/15/2015.

#### Kernel Patch XU\*8.0\*659

Kernel Patch XU\*8.0\*659 provided enhancements needed to implement Single Sign-On Internal (SSOi) for identification and authentication of users into VistA. Specifically, Identity and Access Management (IAM):

- Added or updated remote procedures to provide Kernel support for the IAM Provisioning and IAM Binding applications.
- Added or updated remote procedures to fully implement Kernel processing of IAM Secure Token Service (STS) tokens for secure authentication and identification of users authenticated by IAM using Active Directory credentials (KERBEROS or PIV Card).
- Added the XUS IAM BIND USER and XUS ESSO VALIDATE remote procedures to the XUS SIGNON menu option to make them available to all users.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/015.png) NOTE: Kernel Patch XU\*8.0\*659 was released 08/30/2016.

#### Kernel Patch XU\*8.0\*701

Kernel Patch XU\*8.0\*701 provided enhancements and security fixes for VistA user authorization via Single Sign-On Internal (SSOi). These enhancements and fixes include:

- Fixes serious SSOi (IAM STS SAML) token validation problems that were found in released <u>Kernel Patch XU\*8.0\*659</u> in support of PIV 2FA. It introduces both "strict" and "*non*-strict" credential token validation to properly apply verifications.
- Fixes a problem affecting users with certain last names when using PIV 2FA.
- Completes the work that was started in Kernel Patch XU\*8\*630 in support of applications, such as Join Legacy Viewer (JLV).
- Allows the use of the SSOi token as a more secure alternative to the Broker Security Enhancement (BSE) token.
- Does *not* require users to change their Verify code when using PIV (SSOi).
- Fixes an existing improper lock synchronization on the FAILED ACCESS ATTEMPTS LOG (#3.05) file.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/016.png) NOTE: Kernel Patch XU\*8.0\*701 was released 02/11/2020.

#### RPC Broker Patch XWB\*1.1\*64

RPC Broker Patch XWB\*1.1\*64 was the patch for the IAM “Link My Accounts” application. This patch made changes in the Remote Procedure Call (RPC) Broker listener processes to support emerging technologies and made bug fixes. As part of 2-Factor Authentication (2FA), this patch made the XUS IAM BIND USER RPC available to all users in any context to implement binding of the VistA user account to the user's Active Directory account using the Identity and Access Management (IAM) Binding application.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/017.png) NOTE: RPC Broker Patch XWB\*1.1\*64 was released 11/18/2016.

#### RPC Broker Patch XWB\*1.1\*65

RPC Broker Patch XWB\*1.1\*65 was one in a series of patches to support the VA's transition to SSO with Identity and Access Management (IAM) Secure Token Service (STS). This patch provided the Delphi Broker Development Kit (BDK) utilities needed to implement this requirement. Delphi GUI client applications compiled with this BDK automatically made use of IAM STS tokens for user identification and authentication into VistA servers. Access codes/Verify codes are retained as an alternative method of authentication in case of an invalid STS token, STS server unreachable, or failure to install the required VistA-side patches.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/018.png) NOTE: RPC Broker Patch XWB\*1.1\*65 was released 03/27/2017.

#### RPC Broker Patch XWB\*1.1\*71

RPC Broker Patch XWB\*1.1\*71 is another in a series of patches to support the VA's transition to SSO with Identity and Access Management (IAM) Secure Token Service (STS). This patch provides the Delphi Broker Development Kit (BDK) utilities needed to implement this requirement. Delphi GUI client applications compiled with this BDK will automatically make use of IAM STS tokens for user identification and authentication into VistA servers. Access codes/Verify codes are retained as an alternative method of authentication in case of an invalid STS token, STS server unreachable, or failure to install the required VistA-side patches.

This patch introduces a rewrite of the IAM/SAML token exchange without relying on Microsoft Internet Explorer as a COM layer and provides built-in SOAP/XML/SAML/Certificate Store communication and functionality. Additionally, this version of the BDK allows for Active Directory (AD) Username/Password authentication as a backup to PIV, in case of lost/forgotten PIV cards and the user requesting a temporary PIV card exemption to allow the use of AD authentication.

The DLL included with patch XU\*8.0\*702 was built with BDK components/code provided by this patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the target physical environment for deployment. The Kernel security controls are operationally capable within full implementation of National Institute of Standards and Technology (NIST) controls. It is in compliance with Directive 6500, Section 508, and performance impacts of the deployment environment.

There are no constraints for Kernel Patch XU\*8.0\*702 release other than the operating system and software dependencies described in Section <u>3.3.2</u>, “<u>Software</u>.”

# Roles and Responsibilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the teams that will perform the steps described in this guide.

<u>Table 2</u> identifies the technical and support personnel who are involved in the deployment, installation, back-out, and rollback of the Veterans Health Information Systems and Technology Architecture (VistA) Kernel Patch XU\*8.0\*702 release.

<table>
<caption><p><span id="_Ref33614097" class="anchor"></span>Table : Deployment Timeline</p></caption>
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
<td>Back-out</td>
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

<span id="_Ref33614097" class="anchor"></span>Table : Deployment Timeline

# Deployment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the schedule and milestones for the Kernel Patch XU\*8.0\*702 deployment.

Kernel Patch XU\*8.0\*702 deployment is planned as a simultaneous rollout. National release date is scheduled for 12/05/2019.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/019.png) NOTE: This is just a *proposed* National release date. It is assumed that field testing would be done concurrent with software Quality assurance (SQA) review (starting 11/05/2019).

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 deployment and installation is scheduled to run for 30 days from release, which is the typical Veterans Health Information Systems and Technology Architecture (VistA) national patch rollout schedule.

| Deployment                       | Start      | Finish     |
|----------------------------------|------------|------------|
| Patch Development and Release    | 08/27/2018 | 03/15/2020 |
| Site Installation and Deployment | 03/23/2020 | 04/23/2020 |
| Sustainment                      | 04/23/2020 | Ongoing    |

<span id="_Ref473643192" class="anchor"></span>Table : Site Preparation

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the Site Readiness Assessment for the locations that will receive Kernel Patch XU\*8.0\*702 deployment. This will be a national release of a VistA patch with an associated Visual Basic (VB) script and Dynamic Link Library (DLL) file to all VistA production sites.

Topology determinations are made by Enterprise Systems Engineering (ESE) and vetted by Enterprise Service Line (ESL), Field Office (FO), National Data Center Program (NDCP), and Austin Information Technology Center (AITC) during the design phase as appropriate. Field site coordination is done by ESL unless otherwise stipulated by ESL.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the deployment topology (local sites, etc.) for Kernel Patch XU\*8.0\*702.

Kernel Patch XU\*8.0\*702 will be distributed to local and regional system administrators and support personnel responsible for each of the 130 VistA parent systems. The VistA M Server code, VB script, and DLL will be available to developers from the Product Support (PS) Anonymous Directories.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/020.png) NOTE: The code will be available to developers from secure file transfer \[SFTP) sites listed in the patch description.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 VistA M Server code is directly deployed to all VA sites following the standard deployment procedure used for all VistA patches.

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the preparation required for the site at which the system will operate.

There are no special site preparations or changes that *must* occur to the operational site and no specific features or items that need to be modified to adapt to Kernel Patch XU\*8.0\*702.

As a precursor to Kernel Patch XU\*8.0\*702 deployment, the Kernel documentation set (including this Deployment, Installation, Back-Out, and Rollback Guide) will be added to the VA Software Document Library (VDL) at: <https://www.va.gov/vdl/application.asp?appid=10>

<u>Table 4</u> describes preparation required by the site prior to deployment.

| Site/Other           | Problem/Change Needed | Features to Adapt/Modify to New Product | Actions/Steps | Owner |
|----------------------|-----------------------|-----------------------------------------|---------------|-------|
| Not Applicable (N/A) | N/A                   | N/A                                     | N/A           | N/A   |

<span id="_Ref470091986" class="anchor"></span>Table : Hardware Specifications

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the hardware, software, facilities, documentation, and any other resources, other than personnel, required for the deployment and installation of Kernel Patch XU\*8.0\*702.

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no specific hardware requirements for installation of Kernel Patch XU\*8.0\*702 as it runs in a typical VistA M Server environment. There is also no need for specific hardware to assist in the deployment of Kernel Patch XU\*8.0\*702.

<u>Table 5</u> describes hardware specifications required at each site prior to deployment of Kernel Patch XU\*8.0\*702.

| Required Hardware | Model | Version | Configuration | Manufacturer | Other |
|-------------------|-------|---------|---------------|--------------|-------|
| N/A               | N/A   | N/A     | N/A           | N/A          | N/A   |

<span id="_Ref373317182" class="anchor"></span>Table : VistA M Server—Minimum Software Requirements

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/021.png) REF: For details about who is responsible for preparing the site to meet these hardware specifications, see <u>Table 2</u>.

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation of Kernel Patch XU\*8.0\*702 is a typical Kernel Installation & Distribution System (KIDS) install of a VistA patch in the following environments:

- <u>VistA M Server Software Requirements</u>
- <u>Client Workstation Software Requirements</u>

In addition to Kernel Patch XU\*8.0\*702 VistA M Server code, this software distribution includes a Visual Basic (VB) script and a Dynamic Link Library (DLL) file that are used to implement 2-Factor Authentication (2FA) with the Reflection terminal emulator software that is loaded on most client workstations.

#### VistA M Server Software Requirements

<u>Table 6</u> lists the *minimum* software requirements for the VistA M Server in order to install and use Kernel Patch XU\*8.0\*702:

<table>
<caption><p><span id="_Ref479227195" class="anchor"></span>Table : Client Workstation—Minimum Software Requirement</p></caption>
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
<td>2017.1.3 for Linux, Windows 7, and OpenVMS</td>
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
<p>Patches <em>must</em> be installed in published sequence.</p></td>
</tr>
<tr class="even">
<td>MailMan</td>
<td>8.0</td>
<td><p>VistA Legacy Software Fully Patched M Accounts.</p>
<p>Patches <em>must</em> be installed in published sequence.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref479227195" class="anchor"></span>Table : Client Workstation—Minimum Software Requirement

#### Client Workstation Software Requirements

<u>Table 7</u> lists the *minimum* software requirements for the VistA M Server in order to install and use Kernel Patch XU\*8.0\*702:

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/022.png) NOTE: You only need to have the following terminal emulator software application installed on the client workstation.

| Software                           | Version | Description                 |
|------------------------------------|---------|-----------------------------|
| Micro Focus<sup>®</sup> Reflection | 16.x    | Terminal Emulator Software. |

<span id="_Ref473643112" class="anchor"></span>Table : Deployment/Installation/Back-Out Checklist

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/023.png) NOTE: This section does *not* describe how to install the Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software. Terminal emulator software is pushed to all client workstations and maintained by the Office of Information Field Office (OIFO) System Center Configuration Manager (SCCM) group.  
  
In addition to Kernel Patch XU\*8.0\*702 VistA M Server code, this software distribution includes a Visual Basic (VB) script and a Dynamic Link Library (DLL) file that are used to implement 2-Factor Authentication (2FA) with the Reflection terminal emulator software that is loaded on most client workstations.

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes any notifications activities and how they will occur.

Prior to the deployment of Kernel Patch XU\*8.0\*702, a product announcement will be sent via email to current Points of Contact (POC) on record for each site describing the product and a brief description of the deployment and post-deployment support. Included will be links to the Kernel 8.0 VA Software Document Library (VDL) and Rational repositories, which contain further information about the release and the deployment, including the deployment schedule and required pre-installation activities.

Kernel Patch XU\*8.0\*702 Implementation Team will respond to email requests for assistance and further information and, where appropriate, re-direct these requests to specialist technical staff.

#### Deployment/Installation/Back-Out Checklist

Tracking of installation for VistA Kernel patches is monitored in FORUM.

<u>Table 8</u> provides a checklist to be used to capture the coordination effort and document the day/time/individual when each activity (deploy, install, back-out) is completed for standard Kernel 8.0 patch releases and associated VB script and DLL to enable 2-Factor Authentication (2FA) with the Reflection terminal emulator software.

| Activity                                                        | Day | Time | Individual who completed task |
|-----------------------------------------------------------------|-----|------|-------------------------------|
| Deploy                                                          |     |      |                               |
| Install Patch XU\*8.0\*702 on VistA M Server                    |     |      |                               |
| Install/Load VB Script and DLL                                  |     |      |                               |
| Configure Reflection Software for 2-Factor Authentication (2FA) |     |      |                               |
| Back-Out                                                        |     |      |                               |

<span id="_Ref373318148" class="anchor"></span>Table : Pre-Installation and System Requirement Considerations *before* Installing Kernel Patch XU\*8.0\*702

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 provides enhancements needed to implement Single Sign-On internal (SSOi) for identification and authentication of users into Veterans Health Information Systems and Technology Architecture (VistA) for terminal emulator access (i.e., Micro Focus<sup>®</sup> Reflection \[v16\] terminal emulator software).

## Pre-Installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides the minimum requirements for the product to be installed.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/024.png) REF: For a list of the minimum hardware and software requirements, including platform, Operating System (OS), and storage requirements required for Kernel Patch XU\*8.0\*702, see the following:

- Section <u>3.3.1</u>, “<u>Hardware</u>”
- Section <u>3.3.2</u>, “<u>Software</u>”

<u>Table 9</u> lists the items that installers should consider before installing Kernel Patch XU\*8.0\*702:

<table>
<caption><p><span id="_Ref373317540" class="anchor"></span>Table : Distribution Files</p></caption>
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
<td><strong>VistA M Servers</strong></td>
<td>Kernel Patch XU*8.0*659 <em>must</em> be installed before installing Kernel Patch XU*8.0*702 in VistA.</td>
</tr>
<tr class="even">
<td><strong>Client Workstations Terminal Emulator Software</strong></td>
<td><p>Verify the terminal emulator software that is in use on all client workstations. The current VA-approved terminal emulator software is:</p>
<p><strong>Micro Focus<sup>®</sup> Reflection (v16)</strong></p></td>
</tr>
</tbody>
</table>

<span id="_Ref373317540" class="anchor"></span>Table : Distribution Files

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 should be installed on VistA M Servers. Also, it requires additional system configuration for any installed terminal emulator software on client workstations (i.e., Micro Focus<sup>®</sup> Reflection \[v16\] terminal emulator software).

All VistA Infrastructure patches *must* be installed within 30 days of national release.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Patch XU\*8.0\*702 download files are listed in <u>Table 10</u>.

All Kernel software can be downloaded from the Product Support (PS) Anonymous Directories. Also, all Kernel documentation is available in Adobe<sup>®</sup> Acrobat PDF format and can be downloaded from the VA Software Document Library (VDL) website: <https://www.va.gov/vdl/application.asp?appid=10>

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/025.png) NOTE: For all patches, first read the patch installation instructions in the patch description located in National Patch Module (NPM) on FORUM.

### Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Download the software and documentation distribution files in <u>Table 10</u> that are needed to install Kernel Patch XU\*8.0\*702 on the VistA M Server and configure the terminal emulator software on the client workstation:

<table>
<caption><p><span id="_Ref30074311" class="anchor"></span>Table : Known Issues</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 10%" />
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
<td>XU*8.0*702 Patch Description</td>
<td>ASCII</td>
<td><p><strong>Patch Description (PD)</strong>. This provides any pre-installation instructions, instructions, and additional information to install the patch.</p>
<p>Follow all patch installation instructions.</p></td>
</tr>
<tr class="even">
<td>xu_8_0_p702_dibr.pdf</td>
<td>Binary</td>
<td><strong>Deployment, Installation, Back-Out, and Rollback Guide</strong> (manual). Use this manual in conjunction with the patch description on FORUM.</td>
</tr>
<tr class="odd">
<td>XU_8_702.zip</td>
<td>Binary</td>
<td><p><strong>Visual Basic (VB) Script</strong> (zip file). This zip file contains the following VB script file for the installation required for the <strong>Micro Focus<sup>®</sup> Reflection (v16)</strong> terminal emulator (roll-and-scroll) software on the client workstation:</p>
<p><strong>XUSSOi-1.0p702_v16.bas (Micro Focus<sup>®</sup> Reflection [v16] VB script)</strong></p></td>
</tr>
</tbody>
</table>

<span id="_Ref30074311" class="anchor"></span>Table : Known Issues

### Extract Zip Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the client workstation, extract all files from the XU_8_702.zip distribution file (<u>Table 10</u>):

1.  Copy the XU_8_702.zip file to a temporary location. For example:

C:\Temp\Patch-702

10. Use Microsoft<sup>®</sup> Windows Explorer to extract all of the files:
1.  Right-click on XU_8_702.zip file name.
2.  Select Extract All.
3.  In the “Extract Compressed (Zipped) Folders” dialogue, accept the default location displayed, or select a new destination folder.
4.  Select Extract.

### File and Documentation Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any required maintenance or changes to the DLL and VB Script (<u>Table 10</u>) will be deployed via a new patch with updated instructions included.

The included Kernel DLL is built using components/code from the RPC Broker Development Kit (BDK) released with [RPC Broker Patch XWB\*1.1\*71](#rpc-broker-patch-xwb1.171). A new BDK would *not* require a change to the Kernel DLL, because none of the RPC Broker functions are being used, only the parts required for IAM 2FA authentication.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 does *not* create any required databases. It uses the already installed VA FileMan database.

## Installation DLL and VB Script

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 provides the following installation DLL and VB script via the XU_8_702.zip file (<u>Table 10</u>):

- XUIAMSSOi.dll (Version 8.0.702.3)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/026.png) NOTE: The DLL file will be automatically placed on workstations with Micro Focus® Reflection installed by the Client Technologies team.

- XUSSOi-1.0p702_v16.bas (Micro Focus<sup>®</sup> Reflection \[v16\] Visual Basic script)

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 does *not* provide any cron scripts[^1].

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General skills required to perform the Kernel Patch XU\*8.0\*702 installation are listed below:

- Back up the system

*\[VistA M Server and Client Workstation\]*

- Copy files using commands

*\[VistA M Server and Client Workstation\]*

- Run a Kernel Installation & Distribution System (KIDS) installation

*\[VistA M Server\]*

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/027.png) REF: Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as other VA and VistA publications.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Separate installation procedures are provided in this guide for each of the following target environments:

- <u>VistA M Server Instructions</u>
- <u>Client Workstation Instructions—Micro Focus<sup>®</sup> Reflection (v16)</u>

### VistA M Server Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The instructions in this section are applicable for the Test and Production accounts in the Caché environment.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/028.png) NOTE: Install the server software in a Test account *prior* to installing it in a Production account.

#### Confirm Distribution Files *(recommended)*

Verify that you have downloaded the files listed in <u>Table 10</u>.

#### Retrieve Released Kernel 8.0 Patches *(required)*

Prior to installation of the Kernel Development Kit, all current server-side patches should be installed.

Obtain all released Kernel 8.0 server-side patches from the Patch Module on FORUM or through normal procedures.

#### Install Kernel Patch XU\*8.0\*702

Install Kernel Patch XU\*8.0\*702 from the VistA MailMan message per directions in the patch description.

### Client Workstation Instructions—Micro Focus<sup>®</sup> Reflection (v16)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to configure the pre-installed Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software (i.e., Reflection Workspace v16.0) as an interface to 2-Factor Authentication (2FA). The terminal emulator instructions are applicable to both modifying an existing session file (.rdox) individually on a workstation or a GOLD version of a .rdox session file that is setup to be distributed to many workstations.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/029.png) NOTE: This section does *not* describe how to install the Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software. Terminal emulator software is pushed to all client workstations and maintained by the Office of Information Field Office (OIFO) System Center Configuration Manager (SCCM) group.

The configuration of Micro Focus<sup>®</sup> Reflection (v16) for 2FA includes the following steps:

- <u>Copy DLL to Reflection Program Files Folder</u>—Copy the DLL to the location where Micro Focus<sup>®</sup> Reflection (v16) reads it on start up.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/030.png) NOTE: The DLL file will be automatically placed on workstations with Micro Focus<sup>®</sup> Reflection installed by the Client Technologies team.

- <u>Import Visual Basic Script</u>—Import VB Script to the “Project” environment within Micro Focus<sup>®</sup> Reflection (v16), so the script is available to and contained within the configured .rdox file, allowing its portability for deployment to workstations.
- <u>Set Connection Action</u>—Set the Connection Action to:

"Run a macro or other action after the initial connection” action (mapping that action to the “XUSSOi.XUSSOProcess” subroutine in the VB script).

#### Copy DLL to Reflection Program Files Folder

Copy the XUIAMSSOi.dll file to the location where Micro Focus<sup>®</sup> Reflection (v16) reads it on start up.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/031.png) ATTENTION: This step requires Administrative privileges on the client workstation. Also, the DLL file will be automatically placed on workstations with Micro Focus<sup>®</sup> Reflection installed by the Client Technologies team.

On the client workstation, from the extracted files (see Section <u>4.3.2</u>, “<u>Extract Zip Files</u>”), copy the XUIAMSSOi.dll file (Version 8.0.702.3) into the following directory:

C:\Program Files (x86)\Micro Focus\Reflection

The DLL[^2] file is copied to this location, so it is loaded when Micro Focus<sup>®</sup> Reflection (v16) is launched. This folder is also set in the PATH environment variable on all workstations that have the Micro Focus<sup>®</sup> Reflection software installed. This allows the DLL to be referenced without defined paths in the VB script, yet still load from a faster default path on the workstation.

#### Import Visual Basic Script

The step-by-step instructions in this section import the XUSSOi-1.0p702_v16.bas Visual Basic script to the “Project” environment within the Micro Focus<sup>®</sup> Reflection (v16) session file (.rdox), so the script is contained and available to the specific .rdox file and portable if it needs to be distributed to multiple workstations after setup.

For Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software on the client workstation, do the following:

1.  From the extracted files (see Section <u>4.3.2</u>, “<u>Extract Zip Files</u>”), copy the XUSSOi-1.0p702_v16.bas Visual Basic script (“v16”) into a temporary directory. For example:

<span id="Step_1_v16_file_location" class="anchor"></span>C:\Temp\Patch-702

The XUSSOi-1.0p702_v16.bas file can be deleted after the installation is complete.

2.  Open/launch an existing Micro Focus<sup>®</sup> Reflection session file (.rdox) that is configured to connect to a VistA system. At this point, a VistA connection is *not* needed, so the session can be allowed to timeout without entering ACCESS/VERIFY codes.
11. Depending on the Micro Focus<sup>®</sup> Reflection (v16) mode in use (see <u>Figure 2</u>), open the Microsoft<sup>®</sup> Visual Basic Editor by either of the following methods:
- “Ribbon” Mode—On the Tools tab under Macros, select Visual Basic.
- “Classic” Mode—From the Macro menu, select Visual Basic Editor.

<span id="_Ref479072065" class="anchor"></span>

> Figure : Micro Focus<sup>®</sup> Reflection (v16)—Open “Visual Basic” Editor in “Ribbon” Mode or “Classic” Mode

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/032.png)

12. To import the VB script into the .rdox session file, using the Microsoft<sup>®</sup> Visual Basic Editor (<u>Figure 3</u>):
1.  Right-click on the Project group with the Project area.
2.  Select Import File.

<span id="_Ref479072498" class="anchor"></span>Figure : Microsoft<sup>®</sup> Visual Basic Editor—Select File Menu Option

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/033.png)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/034.png) NOTE: The folder tree display in <u>Figure 3</u> can vary depending on whether or not you have toggled the folder view on or off.

13. Navigate to the location where you saved the XUSSOi-1.0p702_v16.bas file in [Step 1](#Step_1_v16_file_location) (e.g., C:\Temp\Patch-702\v16):
1.  Select the XUSSOi-1.0p702_v16.bas file.
2.  Select Open, as shown in <u>Figure 4</u>.

<span id="_Ref479072961" class="anchor"></span>

> Figure : Microsoft<sup>®</sup> Visual Basic Editor—Select XUSSOi-1.0p702_v16.bas File

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/035.png)

14. You should see the XUSSOi module listed under the “Project” project, as shown in <u>Figure 5</u>:

> <span id="_Ref479073130" class="anchor"></span>Figure : Microsoft<sup>®</sup> Visual Basic Editor—XUSSOi Module

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/036.png)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/037.png) NOTE: The folder tree display in <u>Figure 5</u> can vary depending on whether or not you have toggled the folder view on or off. Also, depending on the size of the project area of the editor window, scrolling may be required to see the newly imported module.

15. Select Save (blue disk icon) or select File and then Save from the menu, as shown in <u>Figure 6</u>:

> <span id="_Ref479073611" class="anchor"></span>Figure : Microsoft<sup>®</sup> Visual Basic Editor—Save Changes

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/038.png)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/039.png) NOTE: The folder tree display in <u>Figure 6</u> can vary depending on whether or not you have toggled the folder view on or off.

16. Close the Microsoft<sup>®</sup> Visual Basic Editor:
1.  Select File.
1.  Select Close and Return to Reflection.

> <span id="_Toc48043996" class="anchor"></span>Figure : Microsoft<sup>®</sup> Visual Basic Editor—Closing and Returning to Reflection

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/040.png)

#### Set Connection Action

This step sets the following Connection Action within the “Host Connections Settings” in Micro Focus<sup>®</sup> Reflection (v16):

"Run a macro or other action after the initial connection” action, which maps to the XUSSOi.XUSSOProcess VB subroutine.

Configure the terminal session .rdox file to trigger these events upon launching the session or when an open session is disconnected and reconnects, which forces the user to go through IAM and the RPC Broker’s 2-Factor Authentication.

To configure the Micro Focus<sup>®</sup> Reflection (v16) host settings connection action, do the following:

1.  Depending on the Micro Focus<sup>®</sup> Reflection mode in use, open the Connection Settings, as shown in <u>Figure 8</u>:
- “Ribbon” Mode—Under the Sessions tab, select the Host Connection Settings expansion button.
- “Classic” Mode—Under the Setup menu, select the View Settings menu option, then select the Configure Connection Settings link in the “Settings for VT” page.

> <span id="_Ref479074739" class="anchor"></span>Figure : Micro Focus<sup>®</sup> Reflection (v16)—Select “Host Connection Settings” in “Ribbon” or “Classic” Mode

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/041.png)

17. In the “Configure Connection Settings” form:
1.  Select the Connection Action option on the left menu.
2.  Select the Run a macro or other action after the initial connection checkbox, as shown in <u>Figure 9</u>:

> <span id="_Ref479074860" class="anchor"></span>Figure : Micro Focus<sup>®</sup> Reflection (v16)—“Configure Connection Settings” Form: Select “Connection Action” Event

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/042.png)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/043.png) NOTE: The first Connection Action checkbox, Run a macro or other action before the initial connection, does *<u>not</u>* need to change. Some .rdox file configurations may have this box checked or unchecked, and that setting can be left as is. Only the second Connection Action checkbox, Run a macro or other action after the initial connection, which is circled in RED (<u>Figure 9</u>), needs to change as per these instructions.

18. In the “Connection Action” form (<u>Figure 10</u>):
1.  Select the Select macro option.
2.  Select XUSSOi.XUSSOProcess VB macro.
3.  Select OK, as shown in <u>Figure 10</u>.

<span id="_Ref479074990" class="anchor"></span>

> Figure : Micro Focus<sup>®</sup> Reflection (v16)—“Connection Action” Form: “Select XUSSOi.XUSSOProcess” Macro

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/044.png)

19. When returned to the “Configure Connection Settings” form:
1.  Select the Run when reconnecting checkbox.
2.  Select OK, as shown in <u>Figure 11</u>.

> <span id="_Ref479075338" class="anchor"></span>Figure : Micro Focus<sup>®</sup> Reflection (v16)—Returned to the “Configure Connection Settings” Form: Select “Run when reconnecting”

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/045.png)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/046.png) NOTE: The first Connection Action checkbox, Run a macro or other action before the initial connection, does *<u>not</u>* need to change. Some .rdox file configurations may have this box checked or unchecked, and that setting can be left as is. Only the third Connection Action checkbox, Run when reconnecting, which is circled in RED (<u>Figure 11</u>), needs to change as per these instructions.

20. Select the “File” menu and then “Save”, as shown in <span class="mark"></span><u>Figure 12</u>, to save the Micro Focus<sup>®</sup> Reflection terminal session.

> <span id="_Ref485306870" class="anchor"></span>Figure : Micro Focus<sup>®</sup> Reflection (v16)—Save Terminal Session File

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/047.png)

21. Congratulations; you are done! The Micro focus<sup>®</sup> Reflection (v16) terminal session is now enabled for 2-Factor Authentication (2FA).  
      
    Repeat the configuration procedure for any remaining terminal sessions saved.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the installation of Kernel Patch XU\*8.0\*702 on the VistA M Server and within the Micro Focus<sup>®</sup> Reflection client software, do the following:

1.  VistA M Server:

Verify the installation using the KIDS Install File Print \[XPD PRINT INSTALL FILE\] option, located under the Utilities \[XPD UTILITY\] menu.

1.  At the “Select INSTALL NAME:” prompt, enter XU\*8.0\*702.
2.  Confirm that the STATUS field is “Install Completed”, as shown in <u>Figure 13</u>:

> <span id="_Ref33694226" class="anchor"></span>Figure : Verify the Kernel Patch XU\*8.0\*702 Installation was Completed on the VistA M Server (Excerpt)

Select Utilities Option: <span class="mark">INSTALL FILE PRINT</span>

Select INSTALL NAME: <span class="mark">XU\*8.0\*702 \<Enter\></span> <span class="mark">Install Completed</span> 4/04/19@08:10:34

=\> XU\*8\*702 TEST v1

DEVICE: HOME// <span class="mark">\<Enter\></span>

PACKAGE: XU\*8.0\*702 Apr 05, 2019 3:06 pm PAGE 1

COMPLETED ELAPSED

----------------------------------------------------------------------------

STATUS: <span class="mark">Install Completed</span> DATE LOADED: APR 4, 2019@08:09:32

INSTALLED BY: XUUSER,ONE

NATIONAL PACKAGE: KERNEL

INSTALL STARTED: MAR 20, 2019@08:10:34 08:10:34

ROUTINES: 08:10:34

…

2.  Terminal Emulator Software on the Client Workstation:

Micro Focus<sup>®</sup> Reflection (v16):

Verify the configuration information matches what is shown in the “<u>Set Connection Action</u>” section.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/048.png) CONGRATULATIONS: The installation of Kernel Patch XU\*8.0\*702 on the VistA M Server and client workstation is complete!

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 does *not* require any VistA M Server system configuration.

For client workstations, follow the configuration procedures listed in the “<u>Set Connection Action</u>” section.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 does *not* require any database tuning.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-Out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the back-out strategy for Kernel Patch XU\*8.0\*702, including the established time limits or other parameters that comprise the rationale for the strategy.

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from Veterans Health Administration (VHA) and Enterprise Program Management (EPMO). In the case of the initial release, a back-out would include removal of data, files, and routines. In the case of future patches and releases, the back-out strategy would be dependent on the contents of the released functionality and could include restoration of file definitions, routines or data.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include impact on production Veterans Health Information Systems and Technology Architecture (VistA) end-user client workstations and impact on Wide Area Network (WAN).

Kernel Patch XU\*8.0\*702 is server software that involves installation in the following environment:

Veterans Health Information Systems and Technology Architecture (VistA) M Servers

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for Kernel Patch XU\*8.0\*702. There are no resources or standards set for Kernel load testing, and a load testing environment is *not* available.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing (UAT) for the Kernel Patch XU\*8.0\*702 was performed by test sites and Software Quality Assurance (SQA) during the development and testing phase.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 VistA M Server back-out criteria follow existing VistA back-out procedures. There are additional back-out criteria for configuration updates made to the existing Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 VistA M Server back-out risks are the same risks established with existing VistA back-out procedures. There are additional back-out risks for configuration updates made to the existing Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with Veterans Health Administration (VHA), Office of Information and Technology (OIT), and Enterprise Program Management Office (EPMO) representatives.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 installation updates the following routine on the VistA M Servers:

^XUS

There are no other VistA M Server software updates.

To back-out Kernel Patch XU\*8.0\*702 in VistA, and back-out configuration updates to the Micro Focus<sup>®</sup> Reflection (v16) terminal emulator software, do the following (in any order):

1.  VistA M Server:
1.  Open the VistA MailMan message created during the “Backup a Transport Global” step of the patch installation process (i.e.,* Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*, Section 23.7.8, “Backing Up Transport Globals”).
2.  Follow the installation sequence (i.e.,* Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*, Section 23.7.1, “Installation Sequence”) to load and install a patch from a PackMan message. This installation restores the original (pre-patch) VistA routine.
3.  Terminal Emulator Software on the Client Workstation: Micro Focus<sup>®</sup> Reflection (v16)
1.  Remove/Delete the event from the Event Mapper and the XUSSOi macro that were enabled during the configuration process performed in the “<u>Set Connection Action</u>” section.
2.  Use a backup copy of the modified terminal session (.rdox) file to copy over the updated one to remove the changes done in the configuration process.

## Back-Out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the back-out of Kernel Patch XU\*8.0\*702, do the following:

1.  VistA M Server:

Verify that the last patch listed in line 2 of routine ^XUS is patch 659, and *not*702.

Select the First Line Routine Print option \[XU FIRST LINE PRINT\] to display the following:

> <span id="_Toc48044003" class="anchor"></span>Figure : Verifying Back-Out of Kernel Patch XU\*8.0\*702 on the VistA M Server

Select Routine Tools Option: <span class="mark">FIRST \<Enter\></span> Line Routine Print

PRINTS FIRST LINES

All Routines? No =\> <span class="mark">NO</span>

Routine: <span class="mark">XUS</span>

Routine: <span class="mark">\<Enter\></span>

1 routine

(A)lpha, (D)ate ,(P)atched, OR (S)ize ORDER: A// <span class="mark">\<Enter\></span>

Include line (2), Include lines 2&(3), (N)one: None//<span class="mark">2</span>

DEVICE: HOME// <span class="mark">\<Enter\></span> TELNET PORT Right Margin: 80// <span class="mark">\<Enter\></span>

FIRST LINE LIST UCI: VISTA,ROU 04/05/2019

XUS ;SFISC/STAFF - SIGNON ;09/22/15 09:25

;;8.0;KERNEL;\*\*16,26,49,59,149,180,265,337,419,434,584,<span class="mark">659</span>\*\*;Jul

10, 1995

1 ROUTINES

4.  Terminal Emulator Software on the Client Workstation: Micro Focus<sup>®</sup> Reflection (v16)

Attempt to make a client connection to VistA. If *not* prompted for 2-factor authentication (PIV and PIN), then you have successfully disabled/removed the macro.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data. This section includes the specific steps to roll back to the previous state of the data and platform settings, if required. It includes the order of restoration for multiple interdependent systems.

Kernel Patch XU\*8.0\*702 does *not* export any data, so no database rollback is required.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 does *not* export any data, so there are no rollback considerations required.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 does *not* export any data, so there are no rollback criteria required.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 does *not* export any data, so there are no rollback risks.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback *can* be authorized by system administrators once a problem has been identified. Office of Information and Technology (OIT) and Enterprise Program Management Office (EPMO) VistA Infrastructure (VI) Development Team should be informed immediately via a MailMan message sent to:

VA OIT PD Infrastructure Dev. & Doc. [*InfrastructureDevDoc@va.gov*](mailto:InfrastructureDevDoc@va.gov)

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 release does *not* export any data, so no rollback procedure is required.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section is not applicable. Kernel Patch XU\*8.0\*702 release does *not* export any data, so no rollback verification procedure is required.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation is a two-part process that includes component installation in the following environments:

- <u>VistA M Server</u>
- <u>Client Workstation</u>

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/049.png) REF: For detailed installation instructions, see the Patch XU\*8.0\*702 Patch Description (PD) on FORUM and the Patch XU\*8.0\*702 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG).

### VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install Kernel Patch XU\*8.0\*702 KIDS Build on the VistA M Server. Patch XU\*8.0\*702 adds code to the signon routine ^XUS to accept IAM SAML token for authentication using terminal emulator (roll-and-scroll) interface.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/050.png) REF: For patch install instructions, see the XU\*8.0\*702 Patch Description (PD) on FORUM.

### Client Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install the following components on all workstations:

- Micro Focus<sup>®</sup> Reflection (v16)—Terminal Emulator Software.
- .rdox File—Micro Focus<sup>®</sup> Reflection session file.
- Visual Basic (VB) Script—Used within Reflection, it calls the DLL and passes the SAML token to VistA.
- DLL—Performs the authentication with IAM and returns a SAML token.

The Visual Basic (VB) script and DLL enable Micro Focus Reflection 2-factor authentication into IAM, and using the received IAM SAML token to authenticate into VistA.

## DLL and .rdox Session Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*702 project team created the XUIAMSSOi.dll file. This DLL performs the authentication with Identity and Access Management (IAM) and returns a Security Assertion Mark-up Language (SAML) token. Associated with the DLL file is the Micro Focus<sup>®</sup> Reflection session file known as a .rdox file, which is configured to connect to VistA using IAM PIV 2FA.

### Phased Rollout of DLL and .rdox Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XUIAMSSOi.dll file *must* be pushed to all workstations; the Micro Focus Reflection .rdox file can be located on a centralized server.

#### DLL File

Client Tech will push out the XUIAMSSOi.dll file to all workstations. During the testing phase, Client Tech will push the XUIAMSSOi.dll file out to those workstations specified by test sites (e.g., ADPAC workstations). Upon national release, Client Tech will push the XUIAMSSOi.dll file out to *all* client workstations.

#### .RDOX File

The .rdox file is a configuration file with no set standard and can vary from region, VISN, facility, user group, and users. In addition, the .rdox file is hosted on a variety of platforms. Each functional group is responsible for updating the .rdox file baselines and redistributing them accordingly. Users will still be accessing Micro Focus<sup>®</sup> Reflection as they have prior to 2FA update. Information Technology Operations and Services (ITOPS) is responsible for communicating the upgrade as they implement the .rdox changes across the enterprise. The following is a list of ITOPS functional groups responsible for these changes:

- Client Desktop Work Station Support—SO IO PS ESL Client Technologies Division
- Citrix Virtual Desktop Support—SO IO PS ESL Back Office Citrix Division
- VistA Application Consolidated Server (VACS) support—SO IO HBMC FO Applications Division

### Verify Correct DLL File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users should first verify their workstation has the correct and latest XUIAMSSOi.dll file installed on their workstation, since an old DLL file (i.e., 2017 beta version from cancelled patch XU\*8.0\*681) may be lurking on some workstations.

<u>Figure 15</u> shows a screenshot of the metadata for the current and correct DLL. The current file was modified/built on 05/18/2020 and has an actual file version number of 8.0.702.3.

<span id="_Ref30054406" class="anchor"></span>Figure : XUIAMSSOi.dll File Properties Dialogue—Details Tab

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/051.png)

### Missing DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Client Tech pushes the XUIAMSSOi.dll file to *all* machines. If a machine is *not* turned on at the time of the push, the XUIAMSSOi.dll file will *not* be installed on the user’s machine.

If the XUIAMSSOi.dll file is *not* available when a user launches the (new) .rdox file, they will be alerted that the software *cannot* find the DLL file and then prompted for their Access/Verify codes. If the XUIAMSSOi.dll file is missing, the user receives an error message and should select End, then the ACCESS CODE prompt will be presented to login, as shown in <u>Figure 16</u>.

<span id="_Ref30054769" class="anchor"></span>Figure : Microsoft Visual Basic Error—Missing XUIAMSSOi.dll File

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/052.png)

## Micro Focus Connection Setting/Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses the scenario when your Micro Focus<sup>®</sup> Reflection session window keeps closing on time out. The “Leave disconnected” connection setting keeps the Micro Focus<sup>®</sup> Reflection session window open if you time out; you would just need to press Enter to get prompted to reconnect.

To prevent your Micro Focus<sup>®</sup> Reflection session window from closing on time-out, do the following:

1.  In Micro Focus<sup>®</sup> Reflection (v16), do the following:
1.  Select File.
3.  Select Settings.
4.  Select Host Connection.
5.  Select Configure Connection Settings.
22. Scroll down to the “Connection Options” section at the bottom of the screen.
23. Locate the “When Connection is Terminated:” box.
24. Change the setting to “Leave disconnected.”

> <span id="_Toc33624121" class="anchor"></span>Figure : Micro Focus Reflection—Connections Page (Sample)

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/053.png)

If you fail to change this setting, when your session disconnects, the session window does *not* stay open and you do not have the option to press Enter to reconnect.. It automatically closes and goes straight to the Reflection New Tab/Recent Documents, as shown in <u>Figure 18</u>:

> <span id="_Ref30060542" class="anchor"></span>Figure : Micro Focus Reflection—New Tab Page

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/054.png)

## New User Signon Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the scenario when a new user (brand new Access/Verify codes) attempts to use the IAM Link My Account webpage to provision their PIV card with a VistA system. The results are that you *cannot* link your PIV to a VistA account if the Verify code is NEW or EXPIRED. Technically, a new or expired Verify code is the same thing, since assigning a new Verify code to a user just presets the code’s expiration date back by several years; thus, forcing an entry of a new Verify code during the user’s first login.

To provision new users and link their PIV to VistA, do the following:

1.  <span id="provision_new_users_step_1" class="anchor"></span>Log onto VistA for the first time using assigned Access/Verify code pair:
1.  Use a PIV-enabled .rdox session file for Micro Focus<sup>®</sup> Reflection.
2.  Press CANCEL at the PIV card prompt.
3.  Press OK in the dialog that no SAML Token was received.
6.  Enter your initial Access/Verify codes provided and change your Verify code.
25. Use the IAM Link My Account website to provision your PIV card to the VistA system using your Access and Verify codes the user created in [Step 1](#provision_new_users_step_1).

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/055.png) REF: Follow the sample steps to provision your account in the “<u>Link My Account</u>” section.

26. Complete. Subsequent PIV logons to that VistA system would be functional and future Verify code expirations will be ignored when logging in using their PIV card.

### Verify Code Expiration Bypass

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA Kernel Patch XU\*8.0\*701 (released on 2/11/2020 and a compliance date of 2/18/2020) includes a logic fix to bypass the Verify code expiration check when successfully logged into VistA using PIV/SAML credentials. This allows Patch XU\*8.0\*702 and Micro Focus<sup>®</sup> Reflection to mimic the behavior of applications that use the Remote Procedure Call (RPC) Broker to connect to VistA (e.g., CPRS). The difference is that the RPC Broker applications do their connections through the Broker Transmission Control Protocol (TCP) port for communication, and with the Reflection method it is doing the communication through Secure Shell (SSH) and passing information to the VistA logon (XUS).

This Verify code expiration bypass also maintains the bypass if Active Directory (Username/Password) is used for SAML authentication by eliminating the check for Level of Assurance (LOA), since both Active Directory and PIV/PIN use STS SAML exchange for authentication and are both identified as SSO in the SAML certificate. The logic checks if the authentication contains “SSO,” which allows the logic to work for both authentication methods and the ability to bypass the Verify code expiration check.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/056.png) NOTE: Using the Active Directory credentials gives a credential Level of Assurance (LOA) a “2” rating, which is using typed codes for authentication as opposed to full 2-Factor Authentication (PIV Card and PIN), which would be a “3” rating for the LOA.

## Link My Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Micro Focus<sup>®</sup> Reflection users need to use Link My Account (LMA) for associating your Personal Identification Verification (PIV) credentials to your VistA credentials.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/057.png) NOTE: Users who do *not* have a PIV card or know their Personal Identification Number (PIN) number can cancel out of the PIV/PIN authentication process and choose to use either of the following authentication processes:

- Active Directory (AD) Username and Password—Possible if the user is logged into the workstation with AD Credentials and launching a 2FA configured .rdox session file.
- VistA Access/Verify code

From the Link My Account Summary Sheet site (VA Intranet site), follow the step-by-step instructions (see ServiceNow KB0013359 \[VA Intranet site\]) to link your Provisioning Account and VistA Account. For example, to link/bind your PIV credentials to your VistA account(s) using the Computerized Patient Record System (CPRS) application, do the following:

1.  Close all open applications and browser windows.
27. Open an Internet browser (e.g., Microsoft Internet Explorer) and navigate to the IAM Provisioning Service Link VistA to User task (VA Intranet site).
28. If you are *not* already logged into a Single Sign-On (SSO) application, the site prompts you to log in:
1.  Select the PIV card.
7.  Browse and select your authentication certificate from the displayed list. The certificate should read:

Issuer: Veterans Affairs User CA B1

8.  Enter your PIN.

> <span id="_Toc33624123" class="anchor"></span>Figure : PIV VA Single Signon Page

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/058.png)

If you receive the following errors after logging in, see the indicated knowledge article for resolution, and then continue to Step 4:

- Page Cannot Be Displayed: Verify the correct Internet Explorer settings, required by the VA for PIV use (see ServiceNow: KB0013570 \[VA Intranet site\]).
- You are in compatibility mode and certain features in the TK will not work as expected: Turn off compatibility view (see ServiceNow: KB0013476 \[VA Intranet site\]).
29. The “Link VistA User” page opens. If it does *not* open, select the Link VistA User menu option from the navigation links on the left of the page.

After selecting Link VistA User, the following message is displayed:

No VistA Stations Linked to your account in Provisioning

Users can ignore this message.

> <span id="_Toc33624124" class="anchor"></span>Figure : Ids VA Provisioning Services Page—Link VistA User

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/059.png)

30. Select a VistA instance:
1.  Move to the “User Account Request Information” section.
4.  From the Link Account drop-down menu, select a VistA Instance.

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/060.png) NOTE: The VistA Instance list is sorted by station number. If station ends in a letter or contains a letter, select the parent station for your division. For example, if your station is 576A or 576A5, select 576 station number.

TIP: To jump to a station on the list, type the station number. The selection jumps to that spot in the drop-down menu.

> <span id="_Toc33624125" class="anchor"></span>Figure : Ids VA Provisioning Services Page—Selecting VistA Instance

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/061.png)

31. Enter your VistA/CPRS Access code and Verify code for that VistA instance, and then select Submit.

> <span id="_Toc33624126" class="anchor"></span>Figure : Ids VA Provisioning Services Page—Entering VistA Access and Verify Code

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/062.png)

![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/063.png) NOTE: Access code may also be known as VistA or CPRS code, and Verify code may also be knowns as VistA or CPRS password. It is the same information entered to log into VistA and CPRS.

> <span id="_Toc33624127" class="anchor"></span>Figure : VistA Sign-On Dialogue

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/064.png)

32. Once you select Submit, if the Access/Verify code was accepted and successful, the application returns the following message:

Your Provisioning Account and VistA Account have been linked. Your user DUZ is (*XXXXX*) Linked with Sec ID: *XXXXXXXX*.

There may be a delay before the link is successful. If this happens, the application returns the message: Your request has been staged. You will receive an email once the linkage is complete. You can check back to see if the link is complete. Once the link is complete, you will see the connected instance as shown in <u>Figure 24</u>.

33. Verify the newly linked VistA account in the list of Instance Names.

> <span id="_Ref35863837" class="anchor"></span>Figure : Ids VA Provisioning Services Page—Verifying VistA Instance Selection

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/065.png)

34. If you have access to more than one VistA account, repeat Steps 5-7 until all VistA accounts have been linked.
35. Click Log off at the top right of the page to go to the IAM SSOi session page.

> <span id="_Toc33624129" class="anchor"></span>Figure : Ids VA Provisioning Services Page—Logout

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/066.png)

36. Click LOGOUT at the bottom of the page to close IAM SSOi session.

<span id="_Toc33624130" class="anchor"></span>Figure : IAM SSOi Session Page—Logout

> ![](xu-8-702-deployment-installation-back-out-and-rollback-guide-dibrg/067.png)

37. You have successfully linked your PIV credentials to your VistA account(s)! After linking your PIV to VistA credentials, you will select your certificate and enter your PIN to access Micro Focus Reflection.

## Technical Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For help in troubleshooting PIV IAM 2FA signon issues, please consult the following:

- PIV Issues—Contact your local PIV Office PIV Badge Office, Enterprise Service Desk (ESD) Support: 1-855-673-4357 (TTY 844-224-6186), or email [PIVHelpRequests@va.gov](mailto:PIVHelpRequests@va.gov).
- VistA account or Access/Verify Issues—Contact your local Information Technology (IT) support or Enterprise Service Desk (ESD) Support: 1-855-673-4357 (TTY 844-224-6186).
- Link my Account Issues—Contact the IAM Help Desk via Enterprise Service Desk (ESD):
- Phone: 1-855-673-4357.
- TTY (Hearing Impaired Only): 1-844-224-6186.

These lines are available 24 hours a day, 7 days a week.

- DLL Issues—If missing the XUIAMSSOi.dll file, send a ServiceNow (SNOW) ticket to the Client Tech REDACTEDCLIENTTECH.TRIAGE group.
- .rdox File Issues—Support entity depends on where the file is hosted:
- Client Desktop Work Stations Support—SO IO PS ESL Client Technologies Division:
- Technical Issues: Please submit ticket into Service Now (SNOW) and assign to your Client Tech SNOW support team or: REDACTEDClientTech.Triage
- Operational Questions: Can be emailed to [OIT ITOPS IO PS Client Tech Division Chiefs](mailto:OITITOPSSOIOPSESLClientTechnologiesDivisionChiefs@va.gov)
- Citrix Application Host Support—SO IO PS ESL Back Office Citrix Division:
- Technical Issues: Please submit ticket into Service Now (SNOW) and assign to REDACTEDBackOffice.Citrix
- Operational Questions: Can be emailed to OIT ITOPS IO PS ESL Back Office Citrix Leadership REDACTED
- VistA Application Consolidated Server (VACS; Gold Star) and/or Network Application Share Server Support—SO IO HBMC FO Applications Division:
- Technical issues Support: Please submit a Service Now (SNOW) ticket to the VAD Clinical SNOW support group (1, 2, 3, or 4) that coincides with your former region:
- IO.HBMC.FO.APP.VADKERNELassign1
- IO.HBMC.FO.APP.VADKERNELassign2
- IO.HBMC.FO.APP.VADKERNELassign3
- IO.HBMC.FO.APP.VADKERNELassign4
- Operational Questions: Can be emailed to: OIT ITOPS SO IO HBMC APP Vista Apps Supervisors; REDACTED

## Issues and Concerns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 11</u> lists any known Micro Focus<sup>®</sup> Reflection software limitations or issues with regard to PIV IAM 2FA:

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 30%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Issue</th>
<th>Resolution</th>
<th>Comments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Restart Session [XURELOG] Routine:</strong></p>
<p>In VistA roll-and-scroll, after signing in with 2FA, if you run the Restart Session [<strong>XURELOG</strong>] routine, it does <em>not</em> trigger you to sign in using 2FA. The only option is to re-sign in using Access/Verify (A/V) codes.</p></td>
<td>User <em>must</em> log out and log back in; restart your session.</td>
<td>Unfortunately, there is no automatic workaround for this issue. Once the user is logged into VistA, the Reflection macro is stopped and no longer listening to any triggers. It is only when the user is disconnected and reconnects, the macro starts up again. So, with something like <strong>XURELOG</strong> that logs off and on (but does <em>not</em> disconnect), only the A/V codes are available.</td>
</tr>
<tr class="even">
<td><p><strong>Mismatched .rdox and .ini Files (used with the INIHandler macro already in the field):</strong></p>
<p>Modifying and renaming a <strong>.rdox</strong> file without properly renaming the associated <strong>.ini</strong> file to match.</p></td>
<td>User <em>must</em> make sure the renamed <strong>.rdox</strong> file has a an associated <strong>.ini</strong> file with the same name.</td>
<td><p>If a standard <strong>.rdox</strong> file is being modified with the script and given a different name, then the associated <strong>.ini</strong> file that goes along with it needs to be copied and given the same name.</p>
<p>This should <em>not</em> be an issue if the modified <strong>.rdox</strong> file has the same name as the original <strong>.rdox</strong> file.</p>
<p>For example: If you were to modify the existing file <strong>FILE1.rdox</strong> and named the modified file <strong>FILE2.rdox</strong>; you would then need to copy the <strong>FILE1.ini</strong> and name the copy <strong>FILE2.ini</strong>, so both file names would still match and stay in synch.</p>
<p>Alternatively, if you first renamed the existing <strong>FILE1.rdox</strong> file to <strong>FILE1_old.rdox</strong> and named the modified file to <strong>FILE1.rdox</strong>, then you would <em>not</em> need to copy and rename the existing <strong>FILE1.ini</strong> file, since both names would still match and be in synch.</p></td>
</tr>
</tbody>
</table>

[^1]: Cron is a time-based job scheduler in Unix-like computer operating systems. People who set up and maintain software environments use cron to schedule jobs (commands or shell scripts) to run periodically at fixed times, dates, or intervals. It typically automates system maintenance or administration. These scripts are suitable for scheduling repetitive tasks: Wikipedia; <https://en.wikipedia.org/wiki/Cron>

[^2]: Dynamic Link Library (DLL) is a shared "library of executable functions or data that can be used by a Windows application. Typically, a DLL provides one or more particular functions and a program accesses the functions by creating either a static or dynamic link to the DLL. A static link remains constant during program execution while a dynamic link is created by the program as needed. DLLs can also contain just data. DLL files usually end with the extension .dll, .exe, .drv, or .fon.

    A DLL can be used by several applications at the same time. Some DLLs are provided with the Windows operating system and available for any Windows application. Other DLLs are written for a particular application and are loaded with the application." Webopedia “Dynamic Link Library (DLL)” term definition; Author: Vangie Beal;Website: <http://www.webopedia.com/TERM/D/DLL.html>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: XU*8*671 Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)

### Facility Specifics 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no facility-specific deployment or installation features of CTT&DM NDS patch XU\*8.0\*671.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No installation scripts are required for installation of CTT&DM NDS patch XU\*8.0\*671.
