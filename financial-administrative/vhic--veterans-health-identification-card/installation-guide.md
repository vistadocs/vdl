---
title: VISTA VIC 4.0 Patch Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Patch
app_code: VHIC
app_name: Veterans Health Identification Card
section: FIN
app_status: archive
pkg_ns: VHIC
patch_ver: 4.0
patch_id: VHIC*4.0
group_key: "VHIC:VHIC:4.0"
file_numbers: 
  - 18
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - server
  - table
  - mpif
  - strong
  - installation
  - contents
  - colgroup
  - thead
  - tbody
  - service
page_count: 0
word_count: 2580
section_count: 4
table_count: 6
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: May 2012
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/mpif_1_56ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Veteran_ID_Card_Archive/mpif_1_56ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=274"
---

> ![](vista-vic-4-0-patch-installation-guide/001.png)

VistA VIC 4.0/CAC

######### INSTALLATION GUIDE

MPIF\*1.0\*56

May 2012

Product Development

Table of Contents

# Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Pre-Installation Considerations](#pre-installation-considerations)
- [Minimum Required Packages](#minimum-required-packages)
- [Required Patches](#required-patches)
- [Software Retrieval](#software-retrieval)
- [Installation](#installation)
  - [Pre-Post Installation Overview](#pre-post-installation-overview)
  - [Installation Steps](#installation-steps)
    - [Installing the MPIF\1.0\56 Patch](#installing-the-mpif1056-patch)
  - [Post-Install/Setup Steps](#post-installsetup-steps)
    - [Set up the Web Server and Web Services](#set-up-the-web-server-and-web-services)
    - [Editing the Web Server and Assigning Web Services](#editing-the-web-server-and-assigning-web-services)
    - [Web Server and Web Services Post-Installation Check](#web-server-and-web-services-post-installation-check)
This Installation Guide explains how to install patch MPIF\*1.0\*56 software and set up the Web Server and Services necessary for the Veterans Health Information Systems and Technology Architecture (VistA) -to- Master Veteran Index (MVI) interface. The intended audience for this document is the Information Resources Management Service (IRMS) staff.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MPIF\*1.0\*56 provides the functionality needed to interface VHA VistA software to the MVI for Primary View (PV) lookup and data retrieval during registration of a patient using the new Veteran Identification Card (VIC 4.0) or Department of Defense’s Common Access Card (CAC).

MPIF software will provide the interface using Health*e*Vet Web Services (HWSC) to obtain initial patient information when a patient has never been treated at the local VA facility and their VIC 4.0 card is swiped or scanned or their CAC card is scanned during the registration process. This VistA-to-MVI interface will send and parse eXtensible Markup Language (XML) messages.

# Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** MPIF\* patches should NOT be installed on legacy systems to avoid issues with the legacy systems ending up as Treating Facilities.

# Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This MPIF patch can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and requires the following Department of Veterans Affairs (VA) software packages.

|                                        |                            |
|----------------------------------------|----------------------------|
| Package                            | Minimum Version Needed |
| Master Patient Index VistA (MPIF)      | 1.0                        |
| VA FileMan                             | 22.0                       |
| Kernel                                 | 8.0                        |
| Health*e*Vet Web Service Client (HWSC) | 1.0                        |

The above software must be installed for this patch to be installed.

# Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patches MPIF\*1.0\*54 and MPIF\*1.0\*55 must be installed prior to installation of MPIF\*1.0\*56.

# Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The files for this patch can be obtained from the ANONYMOUS.SOFTWARE directory at one of the OI Field Offices. The preferred method is to FTP the file from REDACTED., which will transmit the file from the first available server. Alternatively, sites may elect to retrieve the file from a specific OI Field Office.

OI FIELD OFFICE FTP ADDRESS DIRECTORY  
----------------------- ------------------------------------------ ------------------------  
Albany REDACTED anonymous.software  
Hines REDACTED anonymous.software  
Salt Lake City REDACTED anonymous.software

Below is a list of the files related to this patch that will need to be downloaded.

File Name Contents Retrieval (Format)  
------------------------- ------------------------ ---------------  
MPIF_1_56.ZIP Files indicated below: Binary  
- MPIF_1_56.KID KIDS Installation Build (KIDS)  
- PSIMWSEXECUTE.WSDL WSDL (XML)  
- MPIF_1_56IG.PDF Install Guide (PDF)

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Warning Installation Restrictions:                                                                                                                     | It is recommended both patches DG\*5.3\*857 and MPIF\*1.0\*56 be installed at the same time to ensure the functionality. There is no required install order between the two patches but their functionality does depend on each other being installed. Since the DG patch does affect ALL patient look-up processes at the site, we suggest it be installed after business hours. One should not Queue the Install for a later time because of the requirements of the WSDL file. Installation should take no longer than 10 minutes. |
|------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vista-vic-4-0-patch-installation-guide/002.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

## Pre-Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The installation steps are outlined below:

1.  Retrieve the ZIP file MPIF_1_56.zip and extract all of the files.
2.  Place the PSIMWSEXECUTE.WSDL file in the Default Directory for Host File System (HFS), as stated in the Kernel System Parameter (#8989.3) file, which is usually the USER\$:\[TEMP\] folder on the VistA server. If using an FTP utility to place the PSIMWSEXECUTE.WSDL file, please ensure that you have selected ASCII mode for the transfer.
3.  Place the MPIF_1_56.KID in an appropriate directory on the VistA server. If using an FTP utility to place the KIDS file, please ensure that you have selected ASCII mode for the transfer.
4.  Install the MPIF\*1.0\*56 patch. For additional information, please refer to Section *7.2.1 Installing the MPIF\*1.0\*56 Patch*.
5.  Set up the Web Server and Web Services. This will allow VistA to make the XML request to the MVI system. For additional information, please refer to Section *7.2.2 Set up the Web Server and Web Services*.

During the patch installation the environment check routine MPIFHWSC checks for the existence of the WSDL in the Kernel Default Directory. If it doesn’t exist, the install will not be permitted.

The POST-INIT routine POST^MPIFHWSC imports the WSDL file into the HWSC package.

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation includes two main steps:

- Installing the MPIF\*1.0\*56 Patch.
- Set up the Web Server and Web Services.

### Installing the MPIF\*1.0\*56 Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Start up KIDS. Select the Kernel Installation and Distribution System Menu \[XPD MAIN\] option.

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

2.  Select the Installation option.

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

3.  Select Load Distribution and enter the host file name.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select Installation Option: <strong>Load a Distribution</strong></p>
<p>Enter a Host File: <strong>USER$:[HFS]MPIF_1_56.KID</strong></p>
<p>KIDS Distribution saved on Jan 13, 2012@09:34:21</p>
<p>Comment: MPIF*1*56 VIC 4.0/CAC</p>
<p>This Distribution contains Transport Globals for the following Package(s):</p>
<p>Build MPIF*1.0*56</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  Answer YES to want to continue with load.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Want to Continue with Load? YES// <strong>YES</strong></p>
<p>Loading Distribution...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5.  Answer YES to want to RUN the environment check routine.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Build MPIF*1.0*56 has an Environmental Check Routine</p>
<p>Want to RUN the Environment Check Routine? YES// <strong>YES</strong> MPIF*1.0*56</p>
<p>Use INSTALL NAME: MPIF*1.0*56 to install this Distribution.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

6.  Install the package.

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

7.  Enter the package name.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select INSTALL NAME: <strong>MPIF*1.0*56</strong> Loaded from Distribution 1/23/11@12:19:53</p>
<p>=&gt; MPIF*1*56 VIC 4.0/CAC ;Created on Jan 13, 2012@09:34:21</p>
<p>This Distribution was loaded on Jan 13, 2012@12:19:53 with header of</p>
<p>MPIF*1*56 ;Created on Jan 13, 2012@09:34:21</p>
<p>It consisted of the following Install(s):</p>
<p>MPIF*1.0*56</p>
<p>Checking Install for Package MPIF*1.0*56</p>
<p>Will first run the Environment Check Routine, MPIFHWSC</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

8.  Answer NO to rebuild menu trees.

| Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<RET\> |
|--------------------------------------------------------------------------|

9.  Answer NO to not inhibit logons.

| Want KIDS to INHIBIT LOGONs during the install? NO// NO |
|-------------------------------------------------------------|

10. Answer NO to not disable scheduled, menu options and protocols.

| Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//NO |
|----------------------------------------------------------------------------|

11. Enter the device name you want to print the install messages.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Enter the Device you want to print the Install messages.</p>
<p>You can queue the install by enter a 'Q' at the device prompt.</p>
<p>Enter a '^' to abort the install.</p>
<p>DEVICE: HOME// COMPUTER ROOM</p>
<p>Install Started for MPIF*1.0*56 :</p>
<p>Aug 2, 2012@12:26:06</p>
<p>Build Distribution Date: Aug 2, 2012</p>
<p>Installing Routines:</p>
<p>Aug 2, 2012@12:26:06</p>
<p>Running Post-Install Routine: POST^MPIFHWSC</p>
<p>Compilation started on 08/02/2012 12:29:44 with qualifiers 'dk'</p>
<p>Compiling class MPIPSIM.PSIMWebServicePort</p>
<p>Compiling routine MPIPSIM.PSIMWebServicePort.1</p>
<p>Compiling class MPIPSIM.PSIMWebServicePort.execute</p>
<p>Compiling routine MPIPSIM.PSIMWebServicePort.execute.1</p>
<p>Compilation finished successfully in 3.073s.</p>
<p>o WEB SERVICE 'MPI_PSIM_EXECUTE' addition/update succeeded.</p>
<p>&gt;&gt;&gt; MPI_PSIM_EXECUTE entry added to WEB SERVICE file #18.02</p>
<p>- Be sure and set up the Web Server as in the post-install instructions!!</p>
<p>.</p>
<p>Updating Routine file...</p>
<p>Updating KIDS files...</p>
<p>MPIF*1.0*56 Installed.</p>
<p>Aug 2, 2012@12:26:06</p>
<p>Install Complete</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Receiving the above message during install indicates the installation of MPIF\*1.0\*56 is complete.

## Post-Install/Setup Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Set up the Web Server and Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Warning</strong></th>
<th rowspan="2"><p><strong>Setup Restrictions:</strong></p>
<p>Sites should NOT set up Web Services in their test account. The remaining setup instructions are for Production systems only. This patch should not be installed in legacy accounts.</p></th>
</tr>
<tr class="odd">
<th>![](vista-vic-4-0-patch-installation-guide/003.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

After patch MPIF\*1.0\*56 is installed, you must create the Web Server and Services to allow VistA to make the requests as follows:

1.  Enter or modify the Web Service entry in the WEB SERVICE (#18.02 ) file. This is done through the XOBW WEB SERVER MANAGER (Web Server Manager) menu option:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Server Manager</strong> Aug 02, 2012@12:44:41 Page: 1 of 1</u></p>
<p>HWSC Web Server Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Server Name IP Address or Domain Name:Port ____</u></p>
<p>Legend: *Enabled</p>
<p>AS Add Server TS (Test Server)</p>
<p>ES Edit Server WS Web Service Manager</p>
<p>DS Delete Server CK Check Web Service Availability</p>
<p>EP Expand Entry LK Lookup Key Manager</p>
<p>Select Action:Quit// <strong>WS</strong> Web Service Manager</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

2.  Select WS Web Service Manager.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Service Manager</strong> Aug 02, 2012@12:44:44 Page: 1 of 1</u></p>
<p>HWSC Web Service Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Service Name Type URL Context Root</u></p>
<p>1 MPI_PSIM_EXECUTE SOAP psim_webservice/PSIMWebService</p>
<p>Enter ?? for more actions</p>
<p>AS Add Service</p>
<p>ES Edit Service</p>
<p>DS Delete Service</p>
<p>EP Expand Entry</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  You should see the MPI_PSIM_EXECUTE in the list, there may be others previously setup on your system.

### Editing the Web Server and Assigning Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After verifying the Web Service is present as a result of the install, you must enter the Web Server and assign the Web Service to the server. In this case, the MPI_PSIM_EXECUTE server must be entered from the Web Server manager and Web services should be assigned as shown in the screens that follow.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Server Manager</strong> Jan 23, 2010@12:53:14 Page: 1 of 1</u></p>
<p>HWSC Web Server Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Server Name IP Address or Domain Name:Port______________</u></p>
<p>Legend: *Enabled</p>
<p>AS Add Server TS (Test Server)</p>
<p>ES Edit Server WS Web Service Manager</p>
<p>DS Delete Server CK Check Web Service Availability</p>
<p>EP Expand Entry LK Lookup Key Manager</p>
<p>Select Action:Quit// <strong>AS</strong> Add Server</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Select WEB SERVER NAME: MPI_PSIM_EXECUTE</p>
<p>Are you adding 'MPI_PSIM_EXECUTE' as a new WEB SERVER (the 1ST)? No// y (Yes)</p>
<p>NAME: MPI_PSIM_EXECUTE//</p>
<p>SERVER: REDACTED</p>
<p>PORT: 80//REDACTED</p>
<p>DEFAULT HTTP TIMEOUT: 30//</p>
<p>STATUS: E ENABLED</p>
<p>Security Credentials</p>
<p>====================</p>
<p>LOGIN REQUIRED: NO</p>
<p>Authorize Web Services</p>
<p>======================</p>
<p>Select WEB SERVICE: MPI_PSIM_EXECUTE</p>
<p>Are you adding 'MPI_PSIM_EXECUTE' as</p>
<p>a new AUTHORIZED WEB SERVICES (the 1ST for this WEB SERVER)? No// Y (Yes)</p>
<p>STATUS: E ENABLED</p>
<p>Select WEB SERVICE:</p></td>
</tr>
</tbody>
</table>

The MPI_PSIM_EXECUTE server has an Internet Protocol (IP) address and a port number. Be sure and enter the server name and port number exactly as provided to ensure communications.

Using the Web Server Manager option, check the setup of the MPI_PSIM_EXECUTE Web Server by entering EP (Expand Entry) and select the MPI_PSIM_EXECUTE server. The system should have the following data associated with it:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>===============================================================================</p>
<p>1 *MPI_PSIM_EXECUTE REDACTED:REDACTED</p>
<p>-------------------------------------------------------------------------------</p>
<p>NAME: MPI_PSIM_EXECUTE PORT: REDACTED</p>
<p>SERVER: REDACTED STATUS: ENABLED</p>
<p>DEFAULT HTTP TIMEOUT: 30 LOGIN REQUIRED: NO</p>
<p>WEB SERVICE: MPI_PSIM_EXECUTE STATUS: ENABLED</p>
<p>-------------------------------------------------------------------------------</p>
<p>Lookup keys associated with server:</p>
<p>&lt;No lookup keys associations&gt;</p>
<p>===============================================================================</p>
<p>Enter RETURN to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
</tbody>
</table>

The name of the server, MPI_PSIM_EXECUTE, and its respective service, MPI_PSIM_EXECUTE, must remain static. These names are used in the interface code to access the correct Web server and services.

### Web Server and Web Services Post-Installation Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After successfully setting up the Web Server and Web Services, the user can test the communication by selecting the CK--Check Web Service Availability option as shown in the next two screens:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Server Manager</strong> May 04, 2012@15:52:55 Page: 1 of 1</u></p>
<p>HWSC Web Server Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Server Name IP Address or Domain Name:Port</u></p>
<p>1 *MPI_PSIM_EXECUTE REDACTED:REDACTED</p>
<p>Legend: *Enabled</p>
<p>AS Add Server TS (Test Server)</p>
<p>ES Edit Server WS Web Service Manager</p>
<p>DS Delete Server CK Check Web Service Availability</p>
<p>EP Expand Entry LK Lookup Key Manager</p>
<p>Select Action:Quit// <strong>CK</strong> Check Web Service Availability</p>
<p>Select Web Server: (1-1): <strong>1...</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Service Availability</strong> May 04, 2012@15:53:53 Page: 1 of 1</u></p>
<p>Web Server:</p>
<p>1 *MPI_PSIM_EXECUTE REDACTED:REDACTED</p>
<p>_____________________________________________________________________________</p>
<p>1 MPI_PSIM_EXECUTE is available</p>
<p>Enter ?? for more actions</p>
<p>Actions</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>