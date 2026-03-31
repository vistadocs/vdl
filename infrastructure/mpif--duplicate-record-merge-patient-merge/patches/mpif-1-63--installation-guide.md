---
title: MPI MPIF*1*63 Installation, Back-Out, and Rollback Guide
doc_type: DIBR
doc_label: Deployment, Installation, Back-Out, and Rollback Guide
doc_layer: patch
doc_subject: Installation, Back-Out, and Rollback Guide
app_code: MPIF
app_name: Master Patient Index
section: INF
app_status: active
pkg_ns: MPIF
patch_ver: 1
patch_id: MPIF*1*63
group_key: "MPIF:MPIF:1"
file_numbers: 
  - 18
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - contents
  - installation
  - back
  - patch
  - mpif
  - colgroup
  - thead
  - tbody
  - install
page_count: 0
word_count: 4409
section_count: 24
table_count: 9
figure_count: 3
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/mpif_1_63_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Master_Patient_Index_(MPI)/mpif_1_63_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=16"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Master Patient Index (MPI)

  Patch MPIF\*1.0\*63

  Installation, Back-Out, and Rollback Guide
---

![](mpi-mpif-1-63-installation-back-out-and-rollback-guide/001.png)

November 2016

Office of Information and Technology (OI&T)

Revision History

| Date     | Revision | Description                                            | Author                                              |
|----------|----------|--------------------------------------------------------|-----------------------------------------------------|
| Nov 2016 | 1.0      | Initial document created for MPIF Patch MPIF\*1.0\*63. | Identity Services Project/Master Veteran Index Team |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
    - [Pre-Post Installation Overview](#pre-post-installation-overview)
    - [Minimum Required Packages](#minimum-required-packages)
  - [Download and Extract Files](#download-and-extract-files)
    - [Required Patches](#required-patches)
    - [Software Retrieval](#software-retrieval)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
    - [Access Requirements—Privileges and Permissions](#access-requirementsprivileges-and-permissions)
    - [Skills](#skills)
- [Installation Procedure](#installation-procedure)
  - [Installing Patch MPIF\1.0\63](#installing-patch-mpif1063)
- [Post-Installation/Implementation Procedure](#post-installationimplementation-procedure)
  - [Web Server and Web Services Post-Installation Check](#web-server-and-web-services-post-installation-check)
  - [Monitoring Error Trap for Errors](#monitoring-error-trap-for-errors)
  - [System Configuration](#system-configuration)
  - [Database Tuning](#database-tuning)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-out Strategy](#back-out-strategy)
  - [Back-out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-out Criteria](#back-out-criteria)
  - [Back-out Risks](#back-out-risks)
  - [Authority for Back-out](#authority-for-back-out)
  - [Back-out Procedure](#back-out-procedure-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
The Installation, Back-Out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for Patch MPIF\*1.0\*63, as managed through the Master Patient Index Patch project.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide an explanation of how to install patch MPIF\*1.0\*63 software and set up the secure Web Server and Services necessary for the Veterans Health Information Systems and Technology Architecture (VistA) -to- Master Veteran Index (MVI) interface. The intended audience for this document is the Information Resources Management Service (IRMS) staff.

## Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MPIF\*1.0\*63 addresses the Web Application Security Assessment (WASA) findings related to the passing of Personal Identifiable Information (PII) through Hypertext Transport Protocol (HTTP) communication by moving to support Hypertext Transport Protocol <u>Secure</u> (HTTPS) communications to the Person Service Identity Management (PSIM) system. The VistA system implements the VistA HealtheVet Web Services Client (HWSC) framework through Simple Object Access Protocol (SOAP) Web Services when communicating with the PSIM system.

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](mpi-mpif-1-63-installation-back-out-and-rollback-guide/002.png) | ALERT: MPIF\* patches should NOT be installed on legacy systems to avoid issues with the legacy systems ending up as Treating Facilities. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pre-Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation steps are outlined below:

1.  Retrieve the VISTAWEBSERVICE.WSDL file.
2.  Place the VISTAWEBSERVICE.WSDL file in the Default Directory for Host File System (HFS), as stated in the PRIMARY HFS DIRECTORY field (#320) in the KERNEL SYSTEM PARAMETERS file (#8989.3), which is usually the USER\$:\[TEMP\] folder on the VistA server. If using an SFTP utility to place the VISTAWEBSERVICE.WSDL file, please ensure that you have selected ASCII mode for the transfer.

| ![](mpi-mpif-1-63-installation-back-out-and-rollback-guide/003.png) | ALERT: VistA Linux system users must ensure that the Web Services Description Language (WSDL) file copied/stored in the Default HFS Directory is in <u>uppercase</u> (Name and Extension). The environment check process will not find the VISTAWEBSERVICE.WSDL file if it is in lower or mixed case as Linux is a case sensitive operating system, causing the installation process to abort. |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

3.  Confirm that XOBW\*1.0\*4 was installed and all the instructions for setup have been completed, specifically Sections 3.3. and 3.3.3. *Verify the “encrypt_only” SSL Configuration File Exists.*

To perform this check you’ll need to:

- Coordinate with your site’s respective system administration group (e.g. Region Operation Center) to receive assistance in performing the SSL Configuration verification check described as follows:
  - Ask the system administrator to check that the SSL/TLS configuration has been installed in all nodes.
  - Ask the system administrator (with a Programmer Support account) to perform the verification check, assuming they have one of the following roles (e.g. greater than %Developer role):
    - %All
    - %Manager

> Example of determining Roles currently held:

> \>W \$ROLES

> \>%All,%Developer

To check if the "encrypt_only" SSL Configuration exists on that node, enter the following code at the programmer prompt:

> \>D CHCKEXST^XOBWP004("encrypt_only")

> Configuration Values

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

If you get something similar to the above displayed where Protocols is equal to ‘2’ then you are good to go and can proceed with installing patch MPIF\*1.0\*63.

If you get the following, then you’ll need to go back to the XOBW\*1.0\*4 patch instructions and complete the setup before proceeding with the installation of patch MPIF\*1.0\*63.

> \>D CHCKEXST^XOBWP004("encrypt_only")

> \>\>\>\> 'encrypt_only' SSL Config doesn't exist.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr class="header">
<th>![](mpi-mpif-1-63-installation-back-out-and-rollback-guide/004.png)</th>
<th><p><strong>ALERT:</strong> However, if you get an error resembling the following, then you’ll need to contact your Cache System Administrator to request %Manager or %All roles or you could request that the Cache System Manager install this patch.</p>
<p>.S $NAMESPACE="%SYS" ;Change namespace, revert back upon "Q"</p>
<p>  ^</p>
<p>&lt;PROTECT&gt;EXISTS+6^XOBWP004 */srv/vista/isa/cache/isar2tsvr/mgr/</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  Install the MPIF\*1.0\*63 patch. For additional information, please refer to Section 3.1 Installing the MPIF\*1.0\*63 patch.

During the patch installation the environment check routine MPIFWSC checks for the existence of the WSDL file in the Kernel Default Directory. If it doesn’t exist, the install will NOT be permitted.

The POST-INIT routine POST^MPIFWSC imports the WSDL file into the WEB SERVICE file (#18.02) and programmatically creates the WEB SERVER file (#18.12) entry to support the transfer of PII information using HTTPS communications to PSIM. In addition, the “TWO” file entry will be automatically created in the MPI ICN BUILD MANAGEMENT file (#984.8), which will allow determination of the communication protocol (HTTP or HTTPS) to use when communicating with PSIM.

### Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This MPIF patch can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and requires the following Department of Veterans Affairs (VA) software packages.

|                                   |                            |
|-----------------------------------|----------------------------|
| Package                       | Minimum Version Needed |
| Master Patient Index VistA (MPIF) | 1.0                        |
| VA FileMan                        | 22.0                       |
| Kernel                            | 8.0                        |
| Web Service Client (XOBW)         | 1.0                        |

The above software must be installed for this patch to be installed and fully patched.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches MPIF\*1.0\*61 and XOBW\*1.0\*4 must be installed prior to installation of MPIF\*1.0\*63.

### Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The files for this patch can be obtained from the ANONYMOUS.SOFTWARE directory at one of the OI Field Offices. The preferred method is to SFTP the file from REDACTED, which will transmit the file from the first available server. Alternatively, sites may elect to retrieve the file from a specific OI Field Office.

| Oi Field Office | Address | Directory      |
|---------------------|-------------|--------------------|
| Albany              | REDACTED    | anonymous.software |
| Hines               | REDACTED    | anonymous.software |
| Salt Lake City      | REDACTED    | anonymous.software |

ANONYMOUS.SOFTWARE Software Retrieval directories.

The following is a list of the files related to this patch that will need to be downloaded.

| File Name        | Contents  | Retrieval (Format) |
|----------------------|---------------|------------------------|
| VISTAWEBSERVICE.WSDL | WSDL          | ASCII                  |
| MPIF_1_63.PDF        | Install Guide | Binary                 |

Patch information

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Access Requirements—Privileges and Permissions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installers *must* have the following privilege and permission in order to install the MPI Patch MPIF\*1.0\*63:

> Programmer Access: DUZ(0)=”@” is required for installing the Patch MPIF\*1.0\*63.

> Privileged Cache Account Role: %Manager or %All is required to perform the SSL/TLS check step.

> File Access: Required to move/copy the VISTAWEBSERVICE.WSDL file into the Default Directory on the system.

### Skills

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installer needs to know how to do the following:

- Obtain VistA software from FORUM and Secure File Transfer Protocol (SFTP) download sites.
- Run a Kernel Installation & Distribution System (KIDS) installation.
- Use the VistA EVE menu.
- Navigate VMS/UNIX directories.
- Transfer files using Secure File Transfer Protocol (SFTP).
- Use Web Services Options.
- Interpret information in the VistA KERNEL error trap.

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 85%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](mpi-mpif-1-63-installation-back-out-and-rollback-guide/005.png)</p>
</blockquote></th>
<th><strong>WARNING – INSTALLATION RESTRICTIONS:</strong> Do NOT use the Production Web Server account settings when prompted during installation of the MPIF*1.0*63 patch in your Test Account, as this may send test patient information to the production MVI and PSIM systems. <em><mark>Please use the Test Web Server</mark></em> account settings when prompted, as responses are required to complete installation of the patch on the system. Installation should not be queued and it should take no longer than 2 minutes to complete.</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Installing Patch MPIF\*1.0\*63

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the step-by-step instructions for installing all components of VistA Patch MPIF\*1.0\*63.

1.  Choose the PackMan message containing this patch.
5.  Choose the INSTALL/CHECK MESSAGE PackMan option.

The Environment Check routine will automatically execute to verify the availability of the WSDL file.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MPIF*1.0*63</p>
<p>Will first run the Environment Check Routine, MPIFWSC</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Error message displayed if WSDL file is not available:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>MPIF*1.0*63</p>
<p>Will first run the Environment Check Routine, MPIFWSC</p>
<p> WSDL file VISTAWEBSERVICE.WSDL not found in USER$:[TEMP].</p>
<p>You will need that prior to install.</p>
<p>MPIF*1.0*63 Build will not be installed</p>
<p>Jun 02, 2016@10:40:52</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> *NOTE: VISTAWEBSERVICE.WSDL must be available in the Default Directory of the HFS before installation can be continued.*

6.  Confirm that XOBW\*1.0\*4 was installed and all the instructions for setup have been completed, specifically Sections 3.3. and 3.3.3. *Verify the “encrypt_only” SSL Configuration File Exists.*

To perform this check you’ll need to:

- Coordinate with your site’s respective system administration group (e.g. Region Operation Center) to receive assistance in performing the SSL Configuration verification check described as follows:
  - Ask the system administrator to check that the SSL/TLS configuration has been installed in all nodes.
  - Ask the system administrator (with a Programmer Support account) to perform the verification check, assuming they have one of the following roles (e.g. greater than %Developer role):
    - %All
    - %Manager

> Example of determining Roles currently held:

> \>W \$ROLES

> \>%All,%Developer

To check if the "encrypt_only" SSL Configuration exists on that node, enter the following code at the programmer prompt:

> \>D CHCKEXST^XOBWP004("encrypt_only")

> Configuration Values

> CAFile :

> CAPath :

> CRLFile :

> CertificateFile :

> CipherList : TLSv1:SSLv3:!ADH:!LOW:!EXP:@STRENGTH

> Description : Patch XOBW\*1\*4

> Enabled : 1

> PrivateKeyFile :

> PrivateKeyPassword :

> PrivateKeyType : 2

> Protocols : 4

> Type : 0

> VerifyDepth : 9

> VerifyPeer : 0

If you get the above displayed then you are good to go and can proceed with installing patch MPIF\*1.0\*63.

If you get the following, then you’ll need to go back to the XOBW\*1.0\*4 patch instructions and complete the setup before proceeding with the installation of patch MPIF\*1.0\*63.

> \>D CHCKEXST^XOBWP004("encrypt_only")

> \>\>\>\> 'encrypt_only' SSL Config doesn't exist.

However, if you get an error resembling the following, then you’ll need to contact your Cache System Administrator to request %Manager or %All roles or you could request that the Cache System Manager install this patch.

> .S \$NAMESPACE="%SYS" ;Change namespace, revert back upon "Q"

>   ^

> \<PROTECT\>EXISTS+6^XOBWP004 \*/srv/vista/isa/cache/isar2tsvr/mgr/

7.  From the Kernel Installation and Distribution System Menu, select the Installation Menu. From this menu, you may elect to use the following options. When prompted for the INSTALL enter the patch number (i.e. MPIF\*1.0\*63):
1.  Backup a Transport Global – This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DDs or templates.
2.  Compare Transport Global to Current System – This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DDs, templates, etc.).
3.  Verify Checksums in Transport Global – This option will allow you to ensure the integrity of the routines that are in the transport global.
8.  Startup KIDS. Select the Kernel Installation and Distribution System Menu \[XPD MAIN\] option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Edits and Distribution ...</p>
<p>Utilities ...</p>
<p>Installation ...</p>
<p>Patch Monitor Main Menu ...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

9.  Select the Installation option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Kernel Installation &amp; Distribution System Option: Installation</p>
<p>1 Load a Distribution</p>
<p>2 Verify Checksums in Transport Global</p>
<p>3 Print Transport Global</p>
<p>4 Compare Transport Global to Current System</p>
<p>5 Backup a Transport Global</p>
<p>6 Install Package(s)</p>
<p>Restart Install of Package(s)</p>
<p>Unload a Distribution</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

10. Install the package.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>1 Load a Distribution</p>
<p>2 Verify Checksums in Transport Global</p>
<p>3 Print Transport Global</p>
<p>4 Compare Transport Global to Current System</p>
<p>5 Backup a Transport Global</p>
<p>6 Install Package(s)</p>
<p>Restart Install of Package(s)</p>
<p>Unload a Distribution</p>
<p>Select Installation Option: <strong>Install Package(s)</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

11. Enter the package name.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select INSTALL NAME: <strong>MPIF*1.0*63 &lt;Enter&gt;</strong> Loaded from Distribution 6/24/16@15:04:39</p>
<p>=&gt; MPIF*1*63 TEST v2</p>
<p>This Distribution was loaded on Jun 24, 2016@15:04:39 with header of</p>
<p>MPIF*1*63 TEST v2</p>
<p>It consisted of the following Install(s):</p>
<p>MPIF*1.0*63</p>
<p>Checking Install for Package MPIF*1.0*63</p>
<p>Will first run the Environment Check Routine, MPIFWSC</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

12. Answer the Install Questions. (\*\*Required to continue\*\*)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Install Questions for MPIF*1.0*63</p>
<p>Enter the PORT Number for the MPINEWPSIMEXECUTE web service: (1-99999):</p>
<p>Enter the name of the server for MPINEWPSIMEXECUTE:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Production Account Settings:

> Port Number: 8957

> Server Name: REDACTED

> Test Account Settings:

> Port Number: 999

> Server Name: TEST.NOT.APPLICABLE

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th>![](mpi-mpif-1-63-installation-back-out-and-rollback-guide/006.png)</th>
<th><p><strong>ALERT</strong>: Do NOT use the Production Account Settings in your test account as this may send test patient information to the MVI and PSIM production systems.</p>
<p><strong>ALERT:</strong> Test Account Settings are only provided so that users can test the installation of the patch in their Test Account prior to installing into Production.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

13. Answer NO to not inhibit logons.

| Want KIDS to INHIBIT LOGONs during the install? NO// NO |
|-------------------------------------------------------------|

14. Answer NO to not disable scheduled, menu options and protocols.

| Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//NO |
|----------------------------------------------------------------------------|

15. Enter the device name you want to print the install messages.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter the Device you want to print the Install messages.</p>
<p>You SHOULD NOT queue the installation.</p>
<p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME//</p>
<p>Install Started for MPIF*1.0*63 :</p>
<p>Jun 24, 2016@15:09:43</p>
<p>Build Distribution Date: Jun 24, 2016</p>
<p>Installing Routines:...</p>
<p>Jun 24, 2016@15:09:43</p>
<p>Installing PACKAGE COMPONENTS:</p>
<p>Installing REMOTE PROCEDURE..</p>
<p>Jun 24, 2016@15:09:43</p>
<p>Running Post-Install Routine: POSTINIT^MPIFWSC.</p>
<p>Compilation started on 06/24/2016 15:09:44 with qualifiers 'dk'</p>
<p>Compiling class MPIPSIM.VistAWebServicePort</p>
<p>Compiling routine MPIPSIM.VistAWebServicePort.1</p>
<p>Compiling class MPIPSIM.VistAWebServicePort.execute</p>
<p>Compiling routine MPIPSIM.VistAWebServicePort.execute.1</p>
<p>Compilation finished successfully in 4.156s.</p>
<p>o WEB SERVICE 'MPI_PSIM_NEW EXECUTE' addition/update succeeded.</p>
<p>&gt;&gt;&gt; MPI_PSIM_NEW EXECUTE entry added to WEB SERVICE file #18.02</p>
<p>&gt;&gt;&gt; Adding TWO entry to the MPI ICN BUILD MANAGEMENT (#984.8) file &lt;&lt;&lt;</p>
<p>Updating Routine file......</p>
<p>Updating KIDS files.......</p>
<p>MPIF*1.0*63 Installed.</p>
<p>Jun 24, 2016@15:09:47</p>
<p>Install Complete</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Receiving the above message during install indicates the installation of MPIF\*1.0\*63 is complete.

13. Using FileMan (FM), confirm that the Web Service and Web Server entries were setup correctly.

> \>D P^DI

> VA FileMan 22.0

> Select OPTION: INQUIRE TO FILE ENTRIES

> OUTPUT FROM WHAT FILE: WEB SERVER// \<Enter\> WEB SERVER

> Select WEB SERVER NAME: MPI_PSIM_NEW EXECUTE

> ANOTHER ONE: \<Enter\>

> STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

> Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computes

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NAME: MPI_PSIM_NEW EXECUTE</p>
<p>SERVER: REDACTED</p>
<p>STATUS: ENABLED DEFAULT HTTP TIMEOUT: 30</p>
<p>LOGIN REQUIRED: YES</p>
<p>SSL ENABLED: TRUE</p>
<p>SSL CONFIGURATION: encrypt_only SSL PORT: 8957</p>
<p>WEB SERVICE: MPI_PSIM_NEW EXECUTE STATUS: ENABLED</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Select WEB SERVER NAME: \<Enter\>

> Select OPTION: INQUIRE TO FILE ENTRIES

> OUTPUT FROM WHAT FILE: WEB SERVER// \<Enter\> WEB SERVICE (3 entries)

> Select WEB SERVICE NAME: MPI_PSIM_NEW EXECUTE

> ANOTHER ONE: \<Enter\>

> STANDARD CAPTIONED OUTPUT? Yes// \<Enter\> (Yes)

> Include COMPUTED fields: (N/Y/R/B): NO// \<Enter\> - No record number (IEN), no Computed Fields

> *NOTE: Check the WEB SERVICE listing to confirm that there is information for the WSDL. If there is no WSDL information for the entry then the patch did not install correctly and will need to be re-installed.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>NAME: MPI_PSIM_NEW EXECUTE TYPE: SOAP</p>
<p>DATE REGISTERED: JUN 22, 2016@08:48:15</p>
<p>PROXY CLASS NAME: MPIPSIM.VistAWebServicePort</p>
<p>CONTEXT ROOT: psim_webservice/VistAWebService</p>
<p>AVAILABILITY RESOURCE: ?wsdl</p>
<p>WSDL: &lt;?xml version="1.0" encoding="UTF-8"?&gt; &lt;definitions xmlns:tns="VISTA"</p>
<p>xmlns:wsr="http://www.openuri.org/2002/10/soap/reliability/" xmlns:mime="http:/</p>
<p>/schemas.xmlsoap.org/wsdl/mime/"</p>
<p>xmlns:soap12="http://schemas.xmlsoap.org/wsdl/soap12/" xmlns:http="http://schem</p>
<p>as.xmlsoap.org/wsdl/http/"</p>
<p>xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:soap12enc="http</p>
<p>://www.w3.org/2003/05/soap-encoding"</p>
<p>xmlns:conv="http://www.openuri.org/2002/04/wsdl/conversation/" xmlns:soap="http</p>
<p>://schemas.xmlsoap.org/wsdl/soap/"</p>
<p>xmlns:s="http://www.w3.org/2001/XMLSchema" xmlns="http://schemas.xmlsoap.org/ws</p>
<p>dl/" targetNamespace="VISTA"&gt;</p>
<p>&lt;message name="execute"&gt;</p>
<p>&lt;part xmlns:partns="http://www.w3.org/2001/XMLSchema" name="requestXML"</p>
<p>type="partns:string"&gt;</p>
<p>&lt;/part&gt;</p>
<p>&lt;/message&gt;</p>
<p>&lt;message name="executeResponse"&gt;</p>
<p>&lt;part xmlns:partns="http://www.w3.org/2001/XMLSchema" name="responseXML</p>
<p>" type="partns:string"&gt;</p>
<p>&lt;/part&gt;</p>
<p>&lt;/message&gt;</p>
<p>&lt;portType name="VistAWebServicePort"&gt;</p>
<p>&lt;operation name="execute"&gt;</p>
<p>&lt;input message="tns:execute"&gt;</p>
<p>&lt;/input&gt;</p>
<p>&lt;output message="tns:executeResponse"&gt;</p>
<p>&lt;/output&gt;</p>
<p>&lt;/operation&gt;</p>
<p>&lt;/portType&gt;</p>
<p>&lt;binding type="tns:VistAWebServicePort" name="VistAWebServicePort"&gt;</p>
<p>&lt;soap:binding style="rpc" transport="http://schemas.xmlsoap.org/soap/ht</p>
<p>tp" /&gt;</p>
<p>&lt;operation name="execute"&gt;</p>
<p>&lt;soap:operation style="rpc" soapAction="" /&gt;</p>
<p>&lt;input&gt;</p>
<p>&lt;soap:body use="encoded" namespace="VISTA" encodingStyle="http:</p>
<p>//schemas.xmlsoap.org/soap/encoding/" /&gt;</p>
<p>&lt;/input&gt;</p>
<p>&lt;output&gt;</p>
<p>&lt;soap:body use="encoded" namespace="VISTA" encodingStyle="http:</p>
<p>//schemas.xmlsoap.org/soap/encoding/" /&gt;</p>
<p>&lt;/output&gt;</p>
<p>&lt;/operation&gt;</p>
<p>&lt;/binding&gt;</p>
<p>&lt;service name="VistAWebService"&gt;</p>
<p>&lt;port name="VistAWebServicePort" binding="tns:VistAWebServicePort"&gt;</p>
<p>&lt;soap:address location="http://REDACTED:81</p>
<p>10/psim_webservice/VistAWebService" /&gt;</p>
<p>&lt;/port&gt;</p>
<p>&lt;/service&gt; &lt;/definitions&gt;</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Post-Installation/Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Web Server and Web Services Post-Installation Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After successfully installing patch MPIF\*1.0\*63 in Production, which will setup the Web Server and Web Service entries, the user can test the communication by selecting the CK--Check Web Service Availability option as shown in the next two screens, as follows.

*NOTE: This is accomplished through the XOBW WEB SERVER MANAGER (Web Server Manager) menu option. Production accounts will most likely have significantly more Web Server entries than shown below.*

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong><u>Web Server Manager Jun 24, 2016@09:37:36 Page: 1 of 1</u></strong></p>
<p>HWSC Web Server Manager</p>
<p>Version: 1.0 Build: 31</p>
<p>ID Web Server Name IP Address or Domain Name:Port</p>
<p>1 *MPI_PSIM_EXECUTE address:port</p>
<p>2 *MPI_PSIM_NEW EXECUTE REDACTED 8957 <em>(SSL)</em></p>
<p>Legend: *Enabled</p>
<p>AS Add Server TS (Test Server)</p>
<p>ES Edit Server WS Web Service Manager</p>
<p>DS Delete Server CK Check Web Service Availability</p>
<p>EP Expand Entry LK Lookup Key Manager</p>
<p>Select Action:Quit// <strong><u>CK</u> &lt;Enter&gt;</strong> Check Web Service Availability</p>
<p>Select Web Server: (1-4): <strong><u>2</u>...</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<caption>Production Account Display</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Service Availability</strong> Jun 24, 2016@09:37:37</u></p>
<p>Web Server:</p>
<p>2 *MPI_PSIM_NEW EXECUTE REDACTED:8957</p>
<p>_____________________________________________________________________________</p>
<p>1 Unable to retrieve '?wsdl' for MPI_PSIM_NEW EXECUTE</p>
<p>o HTTP Response Status Code: 401</p>
<p>Enter ?? for more actions</p>
<p>Actions</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Production Account Display

Figure 1. Production Account Display (Service Availability Check failed)

*NOTE: If you see the “HTTP Response Status Code: 401” that will indicate that the username and password have not been configured yet. MPI staff will update the username and password remotely once we have confirmed that the patch was successfully installed. Then Information Resource Management (IRM) will be asked to check the web service again and they should now see that the service is available.*

If IRM executes the *<u>Check Web Service Availability</u>* option above in their TEST account, they will see the following error as the TCP/IP address/Port account settings entered for the TEST account during patch installation do NOT actually point (nor should they) to a valid system to connect to.

<table>
<caption>Production Account Display</caption>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Service Availability</strong> Jun 24, 2016@09:37:37</u></p>
<p>Web Server:</p>
<p>2 *MPI_PSIM_NEW EXECUTE TEST.NOT.APPLICABLE:999</p>
<p>_____________________________________________________________________________</p>
<p>1 Unable to retrieve '?wsdl' for MPI_PSIM_NEW EXECUTE</p>
<p>o ERROR #6059: Unable to open TCP/IP socket to server TEST.NOT.APPLICABLE:999</p>
<p>Enter ?? for more actions</p>
<p>Actions</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Production Account Display

Figure 2. Test Account Display (Service Availability Check failed)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Service Availability</strong> Jun 24, 2016@12:03:21 Page: 1 of 1</u> Web Server:</p>
<p>2 *MPI_PSIM_EXECUTE REDACTED:8957</p>
<p>_____________________________________________________________________________</p>
<p>1 MPI_PSIM_NEW EXECUTE is available</p>
<p>Enter ?? for more actions</p>
<p>Actions</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Figure 3. Service Availability Check Success

## Monitoring Error Trap for Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After MPI has remotely configured and switched your site over to using the secure (SSL/TLS) connection, sites may see the following similar error in their error trap if the XOBW\*1.0\*4 patch was not completely installed on all nodes.

> \<ZSOAP\>zInvokeClient+203^%SOAP.WebClient.###:##:##  ROU:<u>NODEXXX</u>   \####

Specific details of the error can be found in the XOBEOARR variable when researching the specifics of the error as shown below:

> XOBEOARR("text",1)=ERROR \#6085: Unable to write to socket with SSL/TLS configuration 'enc

> XOBEOARR("text",2)=rypt_only', error reported 'SSL/TLS configuration 'encrypt_only' is no

> XOBEOARR("text",3)=t activated.'

If you are seeing errors similar to this, then SSL/TLS configuration that was supposed to occur during installation of patch XOBW\*1.0\*4 may not have been configured on one or more front-end or back-end nodes. The initial error above will indicate the current node the error occurred on (i.e., NODEXXX), but there could be other nodes where installation also did not occur.

From the XOBW\*1.0\*4 installation guide, the following command (assuming the user has the appropriate privileges) can be run on a specific node to see if SSL/TLS has been installed.

> \>D CHCKEXST^XOBWP004("encrypt_only")

> \>\>\>\>  'encrypt_only' SSL Config doesn't exist.

Once confirmed that SSL/TLS has NOT been configured on the front-end and/or back-end node, the user can (again assuming they have the appropriate privileges) execute the following command to install SSL/TLS on that node:

> \>D SSLCONF^XOBWP004

> o ‘encrypt_only’ SSL Config successfully installed

> Configuration Values

> CAFile :

> CAPath :

> CRLFile :

> CertificateFile :

> CipherList : TLSv1:SSLv3:!ADH:!LOW:!EXP:@STRENGTH

> Description : Patch XOBW\*1\*4

> Enabled : 1

> PrivateKeyFile :

> PrivateKeyPassword :

> PrivateKeyType : 2

> Protocols : 2

> Type : 0

> VerifyDepth : 9

> VerifyPeer : 0

Additional information if needed on XOBW\*1.0\*4 can be found in the installation guide XOBW_1_0_P4_IG.(pdf/doc).

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“Back-Out” pertains to a return to the last known good operational state of the software and appropriate platform settings.

The back-out procedure for Patch MPIF\*1.0\*63 is to restore the routines back to the previous state, using the back-up message created during installation. Communications will automatically revert to the existing HTTP communication link as before once the routine is restored.

## Back-out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The need for a back-out would be determined by all affected organizations. This would primarily include representatives from Veterans Health Administration (VHA) and Enterprise Program Management (EPMO). In the case of the initial release a back-out would include the restoration of a routine. In the case of future patches and releases the back-out strategy would be dependent on the contents of the released.

## Back-out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None. The system changes were minimal and the routine changes are used based upon a parameter that allows either the HTTP or HTTPS communication to be utilized. The parameter can easily be returned to allow HTTP communication.

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MPIF User Acceptance Testing (UAT) is performed in a near-production environment and verified by the Healthcare Identity Management team (HC IdM).

## Back-out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPIF back-out criteria follow existing VistA back-out procedures.

## Back-out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPIF back-out risks are the same risks established with existing VistA back-out procedures. However, they are considered minimal as the software will continue to use the existing/original HTTP communication link.

## Authority for Back-out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for the need of back-out would reside with VHA and EPMO representatives.

## Back-out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPIF back-out procedure would consist of restoring the original routine using the back-up message created during the patch installation.

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MPIF\*1.0\*63 patch does not export any data so there is no rollback procedure required.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A.