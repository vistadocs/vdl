---
title: XOBW*1*4 Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Installation, Back-Out, and Rollback Guide
app_code: XOBW
app_name: HealtheVet Web Services Client (HWSC)
section: GUI
app_status: active
pkg_ns: XOBW
patch_ver: 1
patch_id: XOBW*1*4
group_key: "XOBW:XOBW:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - installation
  - xobw
  - contents
  - patch
  - back
  - span
  - hwsc
  - vista
  - install
page_count: 0
word_count: 5990
section_count: 29
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2017
revision_count: 4
revision_newest: 12/05/2023
revision_oldest: 10/20/2016
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p4_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p4_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=180"
---

---
title: |
  <span id="_Toc186420068" class="anchor"></span>HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> 1.0  
  Patch XOBW\*1.0\*4

  Installation, Back-Out, and Rollback Guide
---

![](xobw-1-4-installation-back-out-and-rollback-guide/001.png)

May 2017

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

<span id="revision_history" class="anchor"></span>Revision History

| Date       | Revision | Description                                                                                                                                 | Author                                             |
|------------|----------|---------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------|
| 12/05/2023 | 1.3      | Updated for 508 compliance                                                                                                                  | Booz Allen Hamilton                                |
| 05/17/2017 | 1.2      | Added a new error section. Added Section <u>3.5.3</u>, “<u>Install Abort Error</u>,” as per feedback from install site, SQA and developers. | HealtheVet Web Services Client (HWSC) Project Team |
| 12/19/2016 | 1.1      | Corrected patch reference in Section <u>2.1</u>.                                                                                            | HealtheVet Web Services Client (HWSC) Project Team |
| 10/20/2016 | 1.0      | Initial document created for HWSC 1.0 Patch XOBW\*1.0\*4.                                                                                   | HealtheVet Web Services Client (HWSC) Project Team |

<span id="_Ref431821080" class="anchor"></span>Table : Documentation symbol descriptions

Table of Contents

<span id="_Toc482768749" class="anchor"></span>List of Figures

<span id="_Toc482768750" class="anchor"></span>List of Tables

[Table 1: Documentation symbol descriptions [vi](#_Ref431821080)](#_Ref431821080)

[Table 2: HWSC Documentation [6](#_Toc482768809)](#_Toc482768809)

<span id="orientation" class="anchor"></span>Orientation

How to Use this Manual

The Installation, Back-out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product.

Throughout this manual, advice and instructions are offered regarding the use of the HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> Patch XOBW\*1.0\*4 software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Information Resource Management (IRM)—System administrators and Capacity Management personnel at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation Disclaimer

This manual provides an overall explanation of using the HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> Patch XOBW\*1.0\*4 software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) Enterprise Program Management Office (EPMO) Intranet website.

![](xobw-1-4-installation-back-out-and-rollback-guide/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                                                                        | Description                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](xobw-1-4-installation-back-out-and-rollback-guide/003.png)                       | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](xobw-1-4-installation-back-out-and-rollback-guide/004.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Toc482768809" class="anchor"></span>Table : HWSC Documentation

- Descriptive text is presented in a proportional font (as represented by this font).
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xobw-1-4-installation-back-out-and-rollback-guide/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](xobw-1-4-installation-back-out-and-rollback-guide/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xobw-1-4-installation-back-out-and-rollback-guide/007.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). Use the List File Attributes option on the Data Dictionary Utilities menu in VA FileMan to print formatted data dictionaries.

![](xobw-1-4-installation-back-out-and-rollback-guide/008.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about HealtheVet Web Services Client (HWSC) should consult the following:

- *HWSC 1.0 Patch XOBW\*1.0\*4 Release Notes*
- *HWSC 1.0 Patch XOBW\*1.0\*4 Installation, Back-Out, and Rollback Guide* (this manual)
- *HWSC 1.0 Patch XOBW\*1.0\*4 Security Configuration Guide*
- *HWSC 1.0 Installation Guide*
- *HWSC 1.0 Systems Management Guide*
- *HWSC 1.0 Developer’s Guide*

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL): <http://www.va.gov/vdl/>

![](xobw-1-4-installation-back-out-and-rollback-guide/009.png) REF: See the [HealtheVet Web Services Client (HWSC) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=180).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

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
    - [VistA Programmer Access](#vista-programmer-access)
    - [Caché System Administration Account Access](#caché-system-administration-account-access)
    - [cacheexport.xsd File Permissions (System Administrator)](#cacheexportxsd-file-permissions-system-administrator)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Obtain and Extract Distribution Files](#obtain-and-extract-distribution-files)
    - [Software](#software)
    - [Documentation](#documentation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
- [Installation Procedure](#installation-procedure)
  - [Patch Installation Instructions](#patch-installation-instructions)
  - [Load and Install Distribution](#load-and-install-distribution)
  - [Post-Installation Instructions (System Administrator)](#post-installation-instructions-system-administrator)
    - [Create the “encryptonly” SSL/TLS Configuration File](#create-the-encryptonly-ssltls-configuration-file)
    - [Verify the “encryptonly” SSL Configuration File Exists](#verify-the-encryptonly-ssl-configuration-file-exists)
  - [Sample KIDS Installation](#sample-kids-installation)
  - [Troubleshoot Installation Errors / Review Install File](#troubleshoot-installation-errors-review-install-file)
    - [Caché Error 6301 cacheexport.xsd Document Could Not Be Opened](#caché-error-6301-cacheexportxsd-document-could-not-be-opened)
    - [Caché “\<PROTECT\>” Error](#caché-protect-error)
    - [Install Abort Error](#install-abort-error)
  - [Database Creation](#database-creation)
- [Implementation Procedure](#implementation-procedure)
  - [Database Tuning](#database-tuning)
  - [Verify Installation](#verify-installation)
- [Back-Out Plan](#back-out-plan)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure)
- [Rollback Plan](#rollback-plan)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure)
HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4 enables the use of Transport Layer Security/Secure Socket Layer (TLS/SSL) on OpenVMS systems.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to provide instructions for installing HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4.

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Coordinate with System Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers of the HWSC Patch XOBW\*1.0\*4 *must* coordinate with their respective system administration support group (e.g., Region Operation Center) to receive assistance in performing the complete installation.

Depending on your level of access it is expected that the work can be split as follows:

- The patch installer concentrates on performing tasks in the “<u>Load and Install Distribution</u>” section.
- The system administrator performs tasks in the following sections:
- <u>cacheexport.xsd File Permissions (System Administrator)</u>
- <u>Post-Installation Instructions (System Administrator)</u>

The following sections explain the need to coordinate with your system administrator. The result of your coordination determines which steps you can perform and which steps *must* be performed by the system administrator.

## VistA Environment, KIDS, and SSL/TLS Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers *must* coordinate with their system administrator to understand the number of nodes where Veterans Health Information Systems and Technology Architecture (VistA) is running and understand which nodes to which the installer has access. This applies to both VistA Test and Production accounts. The result of this coordination determines which node to access to install the HWSC Patch XOBW\*1.0\*4 Kernel Installation and Distribution System (KIDS) build.

VistA applications are hosted in a Caché environment that can contain a cluster of one or more computer nodes. The basic topology is split into a set of Front-End nodes and a set of Back-End nodes (database nodes). For a small site, a single computer node can serve as both. For larger sites, the number of Front-End and Back-End nodes can vary.

A traditional KIDS installation is performed *ONCE and ONLY* on a Back-End database node. Changes to the Back-End node are visible to all other nodes, except for SSL/TLS Configurations.

![](xobw-1-4-installation-back-out-and-rollback-guide/010.png) NOTE: The HWSC Patch XOBW\*1.0\*4 KIDS build includes both traditional components and non-traditional components, like the SSL/TLS configuration that is visible only to the node where the KIDS build was installed.

The HWSC Patch XOBW\*1.0\*4 KIDS build installation in the Back-End node will install or update the following components:

- Routines (visible to all nodes)
- Class xobw.WebServiceProxyFactory (visible to all nodes)
- Class xobw.WebServer (visible to all nodes)
- The "encrypt_only" Transport Layer Security (TLS/SSL) configuration (visible only to the node where the KIDS build is installed)

![](xobw-1-4-installation-back-out-and-rollback-guide/011.png) NOTE: The TLS/SSL configuration *must* be installed in all nodes, both front-end server nodes and database server nodes.  
  
REF: For more information, see the “<u>Post-Installation Instructions (System Administrator)</u>” section.

## Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installer needs to be familiar with the VistA environment and coordinate with a system administrator to be able to do the following:

- Obtain VistA software from FORUM and Secure File Transfer Protocol (SFTP) download sites (i.e., Product Support Anonymous Directories).
- Run a Kernel Installation and Distribution System (KIDS) installation.
- Use the VistA EVE menu.
- Log in through your Captive User VistA logon account or through your Programmer Support logon account:
- Captive User—Use this logon account when you log in directly to VistA using your Access and Verify code. It has a *non*-privileged %Developer role.
- Programmer Support—Use this logon account when you log in first to the operating system (OS) and then to VistA. It can have higher privileged roles, such as %All or %Manager.
- Execute commands in Programmer mode when given <u>VistA Programmer Access</u>.
- Execute commands in Programmer mode when given the %All or %Manager role (<u>Caché System Administration Account Access</u>).
- Understand VistA’s cluster of front-end and back-end (database) servers.

## Access Requirements—Privileges and Permissions Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers *must* coordinate with their system administrator to determine which level of access they have.

The following privileges and permissions to resources are required in order to install the HWSC Patch XOBW\*1.0\*4 KIDS build and Secure Socket Layer/Transport Layer Security (SSL/TLS) Configuration:

- VistA Programmer Access
- Caché System Administration Account Access
- cacheexport.xsd File Permissions

An installer with a Captive User logon account has only the Vista Programmer Access and requires the assistance of a system administrator. An installer with a Programmer Support login account has Caché System Administration Account Access.

### VistA Programmer Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers *must* have VistA Programmer Access for installing Patch XOBW\*1\*4 KIDS build.  
DUZ(0) = “@” is required.

![](xobw-1-4-installation-back-out-and-rollback-guide/012.png) NOTE: Installers with a Captive User account see a warning that the SSL/TLS configuration could *not* be completed and need to coordinate with their system administrator to complete it as described in the “<u>Post-Installation Instructions (System Administrator)</u>” section.

### Caché System Administration Account Access

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XOBW\*1\*4 KIDS also includes the Socket Layer/Transport Layer Security (SSL/TLS) Configuration installation step.

![](xobw-1-4-installation-back-out-and-rollback-guide/013.png) NOTE: Installers with a Captive User login account are *not* able to complete this step during the KIDS build installation and receive a warning, instructing them to obtain assistance from their system administrator to complete the last step of the KIDS build installation.  
  
REF: For more information, see the “<u>Post-Installation Instructions (System Administrator)</u>” section.

Installers with a Programmer Support account should have the following roles (i.e., greater than the %Developer role):

- %All
- %Manager

To confirm you have the appropriate Caché privileges, look at \$USERNAME and \$ROLES. For example:

\>W \$USERNAME

vha*xxxxxx*\>W \$ROLES

%All,%Developer

If you do *not* have one of the %All or %Manager roles, you *must* contact the system administrator for assistance.

![](xobw-1-4-installation-back-out-and-rollback-guide/014.png) NOTE: After successfully installing HWSC Patch XOBW\*1.0\*4, the elevated privileges are no longer necessary and should be removed.

### cacheexport.xsd File Permissions (System Administrator)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your site may already have the file permissions to an existing cacheexport.xsd file, which is used to parse XML files. To prevent file access errors (ERROR \#6301) on the database server, the system administrator *must* open access to the file cacheexport.xsd, as well as the directory containing it. Do the following:

1.  Navigate to the Caché install directory location for this Caché system.
2.  Locate the file cacheexport.xsd, typically in the “bin” subdirectory.
3.  Open up at least read access to everybody (world) to the directory containing cacheexport.xsd.
4.  Open up at least read access to everybody (world) to the cacheexport.xsd file itself.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *recommended* that sites take the following approach to installing HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4:

1.  Obtain the HWSC Patch XOBW\*1.0\*4 documentation.
2.  Obtain the HWSC Patch XOBW\*1.0\*4 from the Patch module on FORUM or through normal procedures.
3.  Install the software into a Test account.
4.  Install the software into a Production system.

The following minimum software tools are required on your VistA Server in order to install and use the HWSC software:

- VistA account running on InterSystems’ Caché for Linux, NT or OpenVMS.
- VistA accounts *must* contain the fully patched versions of the following packages:
- HWSC 1.0
- Kernel 8.0
- Kernel Toolkit 7.3
- MailMan 8.0
- VA FileMan 22.0 (or higher)

![](xobw-1-4-installation-back-out-and-rollback-guide/015.png) NOTE: These software packages *must* be properly installed and fully patched prior to installing HWSC Patch XOBW\*1.0\*4. Patches *must* be installed in published sequence. You can obtain all released VistA patches (including patch description and installation instructions), from the Patch module on FORUM or through normal procedures.

The HWSC Patch XOBW\*1.0\*4 patch can be installed with users on the system, since the installation only affects the HWSC options; however, it is *recommended* that it be installed during *non*-peak hours to minimize potential disruption to users. Installation of the patch itself should take approximately 5 minutes; however, the configuration process will take longer.

## Obtain and Extract Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC Patch XOBW\*1.0\*4 software distribution is contained in a KIDS PackMan message.

The KIDS PackMan message can be obtained from the Patch module on FORUM or through normal procedures.

Use KIDS to install the HWSC Patch XOBW\*1.0\*4 software.

### Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation for HealtheVet Web Services Client is available on the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/application.asp?appid=180>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories via Secure File Transfer Protocol (SFTP).

| File Name           | FTP Mode | Description                                         |
|---------------------|----------|-----------------------------------------------------|
| xobw_1_0_p4_ig.pdf  | Binary   | HWSC 1.0 Installation, Back-out, and Rollback Guide |
| xobw_1_0_p4_scg.pdf | Binary   | HWSC 1.0 Security Configuration Guide               |
| xobw_1_0_dg.pdf     | Binary   | HWSC 1.0 Developer’s Guide                          |
| xobw_1_0_sg.pdf     | Binary   | HWSC 1.0 Systems Management Guide                   |

VSM DocumentationVSM Documentation

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no installation scripts for HWSC Patch XOBW\*1.0\*4.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no cron scripts for the HWSC Patch XOBW\*1.0\*4.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a standard VistA patch installation. Use the Kernel Installation & Distribution System (KIDS) to install the HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4 software.

![](xobw-1-4-installation-back-out-and-rollback-guide/016.png) REF: Details regarding imported files, options, protocols, etc. can be found in the [*HWSC 1.0 Systems Management Guide*](http://www.va.gov/vdl/documents/HealtheVet/HealtheVet_Web_Services_Client/xobw1_0sg.pdf).

For VistA sites with a cluster of back-end database server nodes and front-end application server nodes, this patch should only be installed on the database server. The patch will do the following:

1.  Update routines that will be available on all nodes.
5.  Update the class xobw.WebServiceProxyFactory, which will be available on all nodes.
6.  Update the class xobw.WebServer, which will be available on all nodes.
7.  Create the Secure Socket Layer/Transport Layer Security (SSL/TLS) configuration “encrypt_only”. Visible only on the installed node. You need to make it available on all nodes in your cluster, see the “<u>Post-Installation Instructions (System Administrator)</u>” section.

## Load and Install Distribution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On configurations with a back-end database server and front-end application servers/commodity boxes, perform the following procedure:

1.  Log onto the database server.
2.  Choose the PackMan message containing this patch.
3.  Choose the INSTALL/CHECK MESSAGE PackMan option.
4.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL NAME enter the patch name XOBW\*1.0\*4:
1.  Backup a Transport Global—This option creates a backup message of any routines exported with this patch. It does not back up any other changes, such as DDs or templates.
2.  Compare Transport Global to Current System—This option allows you to view all changes that will be made when this patch is installed. It compares all components of this patch (e.g., routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global—This option allows you to ensure the integrity of the routines that are in the transport global.
5.  From the Installation Menu, select the Install Package(s) option. When prompted for the INSTALL NAME, enter XOBW\*1.0\*4.
6.  At the “Want KIDS to INHIBIT LOGONs during the install? NO//” prompt, enter NO.
7.  At the “Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//” prompt, enter NO.
8.  If prompted to “Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//”, enter NO.
9.  Enter the Device you want to print the Install messages. For example:

DEVICE: HOME// ;P-DEC NETWORK

Enter a “^” to abort the install.

![](xobw-1-4-installation-back-out-and-rollback-guide/017.png) NOTE: Do not queue the install, as the TaskMan process may not have the necessary privileges to perform the installation.

![](xobw-1-4-installation-back-out-and-rollback-guide/018.png) NOTE: Installers with a Captive User account will see a warning that the SSL/TLS configuration could *not* be completed and will need to coordinate with their system administrator to complete it as described in the “<u>Post-Installation Instructions (System Administrator)</u>” section.

## Post-Installation Instructions (System Administrator)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transport Layer Security (SSL/TLS) configuration *must* be installed on each of the nodes in the cluster.

The installer should coordinate with their respective system administration support group (e.g., Region Operation Center) to receive assistance in performing the complete installation as described below.

The system administrator should check that the SSL/TLS configuration has been installed in the node where HWSC Patch XOBW\*1.0\*4 was installed, which is a Back-end database node.

In general, the system administrator should check on all the nodes, front-end servers, and database servers that the SSL/TLS Configuration has been installed, using the following sections (in any order):

- <u>Create the “encrypt_only” SSL/TLS</u> Configuration File.
- <u>Verify the “encrypt_only” SSL Configuration</u> File Exists.

### Create the “encrypt_only” SSL/TLS Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new SSL/TLS Configuration file, “encrypt_only”, is installed if there is *not* already an existing “encrypt_only” configuration file.

To create the “encrypt_only” SSL/TLS configuration file, do the following:

1.  Log onto a node in the cluster.
8.  At the VistA programmer prompt, enter the following code:

> <span id="_Ref461627838" class="anchor"></span>Figure : Post-Installation Instructions—Create the “encrypt_only” SSL/TLS Configuration File

\><span class="mark">D SSLCONF^XOBWP004</span>

<span class="mark">o ‘encrypt_only’ SSL Config successfully installed</span>

Configuration Values

CAFile :

CAPath :

CRLFile :

CertificateFile :

CipherList : TLSv1:SSLv3:!ADH:!LOW:!EXP:@STRENGTH

Description : Patch XOBW\*1\*4

Enabled : 1

PrivateKeyFile :

PrivateKeyPassword :

PrivateKeyType : 2

Protocols : 2

Type : 0

VerifyDepth : 9

VerifyPeer : 0

![](xobw-1-4-installation-back-out-and-rollback-guide/019.png) CAUTION: If you see a “\<PROTECT\>” error (see Section <u>3.5.2</u>), you do *not* have the appropriate access requirements; see the “<u>Access Requirements—Privileges and Permissions Needed for</u> the Installation” section.

9.  When successful, you will see the following message:

> <span id="_Toc482768799" class="anchor"></span>Figure : Post-Installation Instructions—Confirmation of Successful Configuration File Creation

<span class="mark">o ‘encrypt_only’ SSL Config successfully installed</span>

10. Repeat Steps 1 - 3 for each node in the cluster.

### Verify the “encrypt_only” SSL Configuration File Exists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the “encrypt_only” SSL Config exists on a node, do the following:

1.  At the VistA programmer prompt, enter the following code:

D CHCKEXST^XOBWP004(“encrypt_only”)

11. If the “encrypt_only” SSL Config was successfully created, the configuration values are displayed, as shown in <u>Figure 3:</u>

> <span id="_Ref455984464" class="anchor"></span>Figure : Post-Installation Instructions—Verifying the “encrypt_only” SSL Configuration File Exists: Successful

\><span class="mark">D CHCKEXST^XOBWP004(“encrypt_only”)</span>

<span class="mark">Configuration Values</span>

CAFile :

CAPath :

CRLFile :

CertificateFile :

CipherList : TLSv1:SSLv3:!ADH:!LOW:!EXP:@STRENGTH

Description : Patch XOBW\*1\*4

Enabled : 1

PrivateKeyFile :

PrivateKeyPassword :

PrivateKeyType : 2

Protocols : 2

Type : 0

VerifyDepth : 9

VerifyPeer : 0

![](xobw-1-4-installation-back-out-and-rollback-guide/020.png) CAUTION: Make sure that you correctly spell the name of the configuration file, “encrypt_only”. If the configuration does *not* exist, then repeat the “<u>Create the “encrypt_only” SSL/TLS</u> Configuration File” section; making sure to correctly spell the name of the configuration file.  
  
If you see a “\<PROTECT\>” error (see Section <u>3.5.2</u>), you do *not* have the appropriate access requirements; see the “<u>Access Requirements—Privileges and Permissions Needed for</u> the Installation” section.

12. If the “encrypt_only” SSL Config was *not* successfully created, an error message is displayed, as shown in <u>Figure 4</u>:

> <span id="_Ref455984762" class="anchor"></span>Figure : Post-Installation Instructions—Verifying the “encrypt_only” SSL Configuration File Exists: Unsuccessful

\><span class="mark">D CHCKEXST^XOBWP004(“encrypt_only1”)</span>

<span class="mark">\>\>\>\> ‘encrypt_only’ SSL Config doesn’t exist.</span>

## Sample KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 5</u> is a sample HWSC Patch XOBW\*1.0\*4 KIDS install on a VMS system:

<span id="_Ref452993495" class="anchor"></span>Figure : Sample HWSC Patch XOBW\*1.0\*4 Installation on a VMS System

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation \<TEST ACCOUNT\> Option: <span class="mark">6 \<Enter\></span> Install Package(s)

Select INSTALL NAME: <span class="mark">XOBW\*1.0\*4 \<Enter\></span> Loaded from Distribution 7/8/16@11:28:50

=\> XOBW\*1\*4 TEST v7

This Distribution was loaded on Jul 08, 2016@11:28:50 with header of

XOBW\*1\*4 TEST v7

It consisted of the following Install(s):

XOBW\*1.0\*4

Checking Install for Package XOBW\*1.0\*4

Will first run the Environment Check Routine, XOBWP004

Install Questions for XOBW\*1.0\*4

Want KIDS to INHIBIT LOGONs during the install? NO// <span class="mark">\<Enter\></span>

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// <span class="mark">\<Enter\></span>

Enter the Device you want to print the Install messages.

You can queue the install by enter a ‘Q’ at the device prompt.

Enter a ‘^’ to abort the install.

DEVICE: HOME// <span class="mark">;P-DEC \<Enter\></span> NETWORK

Install Started for XOBW\*1.0\*4 :

Jun 14, 2016@09:51:06

Build Distribution Date: Jun 14, 2016

Installing Routines:...

Jun 14, 2016@09:51:06

Running Post-Install Routine: POST^XOBWP004.

Load started on 06/14/2016 09:51:06

Loading file /srv/vista/oak/user/hfs/xobw4.xml as xml

Imported class: xobw.WebServiceProxyFactory

Compiling class xobw.WebServiceProxyFactory

Compiling routine xobw.WebServiceProxyFactory.1

Load finished successfully.

o Support classes imported successfully.

Load started on 06/14/2016 09:51:06

Loading file /srv/vista/oak/user/hfs/xobw4b.xml as xml

Imported class: xobw.WebServer, compiling 2 classes, using 2 worker jobs

Compiling class xobw.WebServer

Compiling class xobw.WebServicesAuthorized

Compiling table xobw.WebServicesAuthorized

Compiling table xobw.WebServer

Compiling routine xobw.WebServer.1

Compiling routine xobw.WebServicesAuthorized.1

Load finished successfully.

o Support classes imported successfully.

o ‘encrypt_only’ SSL Config successfully installed.

Description: Patch XOBW\*1\*4

Updating Routine file......

Updating KIDS files.......

XOBW\*1.0\*4 Installed.

Jun 14, 2016@09:51:06

Not a production UCI

NO Install Message sent

## Troubleshoot Installation Errors / Review Install File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Review the contents of the install file and verify that no errors occurred. If an error did occur, check the following troubleshooting items to see if any match the error encountered.

If installation of HWSC PATCH XOBW\*1.0\*4 fails, the *recommended* action is to:

1.  Review the install logs.
13. Determine and address the cause of install failure.
14. Re-run the HWSC PATCH XOBW\*1.0\*4 installation.  
      
    The HWSC PATCH XOBW\*1.0\*4 installation can be re-run as many times as necessary until a successful installation is achieved.

Some common installation errors are listed below.

### Caché Error 6301 cacheexport.xsd Document Could Not Be Opened

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may encounter a Caché 6301 error as shown in <u>Figure 6</u>, specifically referring to “cacheexport.xsd”:

<span id="_Ref456763717" class="anchor"></span>Figure : Cache Error 6301 cacheexport.xsd: Primary Document Could Not Be Opened

Error: <u>ERROR \#6301: SAX XML Parser Error</u>: Line: 2 Offset: 125 An exception

occurred! Type:RuntimeException, Message:Warning: <u>The primary document entity could not be opened</u>. Id=\_\$1\$DISK:\[CACHESYS.ISC1.BIN\]<u>cacheexport.xsd</u> at line 0 offset 0

And/Or, an error referring to undeclared attributes and unknown elements could be displayed following a Caché 6301error, as shown in <u>Figure 7</u>:

<span id="_Ref456764412" class="anchor"></span>Figure : Undeclared Attributes and Unknown Elements

Line: 2 Offset: 125 An exception occurred! Type:RuntimeException, Message:Warning: The primary document entity could not be opened. Id=\$1\$DISK:\[CACHESYS.ISC1.BIN\]<u>cacheexport.xsd</u> at line 0 offset 0Line: 2 Offset: 125 Unknown element 'Export' while processing \$1\$DISK:\[CACHESYS.ISC1.MGR.TEMP\]568337052XWMf1.XML at line 2 offset 125

Line: 2 Offset: 125 Attribute 'generator' is not declared for element 'Export' while processing \$1\$DISK:\[CACHESYS.ISC1.MGR.TEMP\]568337052XWMf1.XML at line 2 offset 125

Line: 2 Offset: 125 Attribute 'version' is not declared for element 'Export' while processing \$1\$DISK:\[CACHESYS.ISC1.MGR.TEMP\]568337052XWMf1.XML at line 2 offset 125

Line: 2 Offset: 125 Attribute 'zv' is not declared for element 'Export' while processing \$1\$DISK:\[CACHESYS.ISC1.MGR.TEMP\]568337052XWMf1.XML at line 2 offset 125

Line: 2 Offset: 125 Attribute 'ts' is not declared for element 'Export' while processing \$1\$DISK:\[CACHESYS.ISC1.MGR.TEMP\]568337052XWMf1.XML at line 2 offset 125

Line: 3 Offset: 32 Unknown element 'Class' while processing \$1\$DISK:\[CACHESYS.ISC1.MGR.TEMP\]568337052XWMf1.XML at line 3 offset 32

To fix this issue, follow the instruction in the “<u>cacheexport.xsd File Permissions</u>” section.

### Caché “\<PROTECT\>” Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may encounter a protection error during the HWSC PATCH XOBW\*1.0\*4 KIDS installation or during the creation and verification of the SSL/TLS Configuration as shown in <u>Figure 8</u> and <u>Figure 9</u>:

<span id="_Ref456764040" class="anchor"></span>Figure : Cache “\<PROTECT\>” Error (1 of 2)

\><span class="mark">D SSLCONF^XOBWP004</span>

. . .

\<PROTECT\>EXISTS+6^XOBWP004 \*/srv/vista/oak/cache/oakr0ta01/mgr/

Or:

<span id="_Ref456764048" class="anchor"></span>Figure : Cache “\<PROTECT\>” Error (2 of 2)

\><span class="mark">D CHCKEXST^XOBWP004("encrypt_only")</span>

. . .

\<PROTECT\>EXISTS+6^XOBWP004 \*/srv/vista/oak/cache/oakr0ta01/mgr/

These errors indicate that you do not have the appropriate access requirements. For more information, see the “<u>Access Requirements—Privileges and Permissions Needed for</u> the Installation” section.

### Install Abort Error

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may encounter an “INSTALL ABORTED” error during the HWSC PATCH XOBW\*1.0\*4 KIDS installation, as shown in <u>Figure 10</u>:

<span id="_Ref482767608" class="anchor"></span>Figure : Install Abort Error

\*\*INSTALL ABORTED\*\* Patch XOBW\*1.0\*0 is Required to install this package!!

The explanation for this error is that your site's original installation of XOBW\*1.0\*0 might have left the PACKAGE (#9.4) file in an "inconsistent" state.

To correct the PACKAGE (#9.4) file, do the following:

1.  At a programmer prompt, set the following variables:

X="XOBW\*1.0\*0",Y=\$\$LKPKG^XPDUTL(\$P(X,"\*"))

15. Verify the value of the “Y” variable is *not* Zero (0):

W Y ;\<\<\<\<IF Y NOT ZERO CONTINUE DOING STEP \#3, AND \#4

16. Correct the PACKAGE (#9.4) file entry:

S ^DIC(9.4,Y,22,1,"PAH","B",0,1)=""

17. Verify that the PACKAGE (#9.4) file entry for HWSC PATCH XOBW\*1.0\*0 was successfully corrected at your site:

S XPDX="XOBW\*1.0\*0" W \$\$PATCH^XPDUTL(XPDX)  
1

The result is 1, which confirms that the PACKAGE (#9.4) file entry for HWSC PATCH XOBW\*1.0\*0 was successfully corrected. You *must* get a "1" to be sure that you can re-install patch XOBW\*1.0\*4.

18. Using KIDS, install HWSC PATCH XOBW\*1.0\*4.

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC Patch XOBW\*1.0\*4 installation does *not* create any databases. HWSC uses the existing VA FileMan database.

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special database tuning requirements for HWSC Patch XOBW\*1.0\*4.

## Verify Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To verify the installation, follow the procedures in the “<u>Verify the “encrypt_only” SSL Configuration</u> File Exists” section.

# Back-Out Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

In the case that a back-out of this release is required a patch needs to be created and deployed to all sites that have installed the original patch. In the case of an initial release this new patch would need to remove any existing data, remove Veterans Health Information Systems and Technology Architecture (VistA) files associated with the package and remove routines associated with this package. Contents of a back-out patch for future releases would be dependent on the functionality released at that time.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from Veterans Health Administration (VHA) and Enterprise Program Management (EPMO). In the case of the initial release a back-out would include removal of data, files and routines. In the case of future patches and releases the back-out strategy would be dependent on the contents of the released functionality and could include restoration of file definitions, routines or data.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out considerations would include impact on production VistA end-users and impact on Wide Area Network.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Not applicable for HWSC.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HWSC User Acceptance Testing (UAT) is performed during VistA patch testing at test sites.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC back-out criteria follow existing VistA back-out procedures.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC back-out risks are the same risks established with existing VistA back-out procedures.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with VHA and EPMO representatives.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC Patch XOBW\*1.0\*4 installation does not affect any existing VistA applications. If there is a need to back out to the previous state, you can back up the one routine being modified using the Kernel Installation and Distribution System (KIDS) Backup a Transport Global option \[XPD BACKUP\]. The ObjectScript classes and SSL/TLS Configuration would be returned to their previous state by the creation of a patch to replace the ObjectScript classes and remove the SSL/TLS Configuration.

# Rollback Plan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback pertains to data.

HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4 does not export any data.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. HWSC Patch XOBW\*1.0\*4 does not export any data.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. HWSC Patch XOBW\*1.0\*4 does not export any data.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. HWSC Patch XOBW\*1.0\*4 does not export any data.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Rollback *can* be authorized by system administrators once a problem has been identified. Enterprise Program Management Office (EPMO) should be informed immediately via a MailMan message sent to:

VA OIT PD Infrastructure Dev. & Doc. \<InfrastructureDevDoc@va.gov\>

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A. HWSC Patch XOBW\*1.0\*4 does not export any data.