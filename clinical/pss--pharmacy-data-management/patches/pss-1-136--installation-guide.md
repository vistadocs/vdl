---
title: PSS*1*136 Installation Guide- VistA to MOCHA Version 1 Interface
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: VistA to MOCHA Version 1 Interface
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*136
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - table
  - strong
  - server
  - colgroup
  - thead
  - tbody
  - services
  - check
  - vendor
  - database
page_count: 0
word_count: 4835
section_count: 6
table_count: 13
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_ig_r0411.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_ig_r0411.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

> ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/001.png)

VistA to MOCHA v1.0 Interface

######### INSTALLATION GUIDE

PSS\*1.0\*136

April 2011

Product Development

######### Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

| Date | Revised Pages | Patch Number | Description                 |
|----------|-------------------|------------------|---------------------------------|
| 04/11    | N/A               | PSS\*1\*136      | Initial Version for PSS\*1\*136 |
|          |                   |                  |                                 |

*(This page included for two-sided copying.)*

Table of Contents

*(This page included for two-sided copying.)*

# Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Purpose](#purpose)
- [Scope](#scope)
- [Pre-Installation Considerations](#pre-installation-considerations)
- [Minimum Required Packages](#minimum-required-packages)
- [Required Patches](#required-patches)
- [Installation](#installation)
  - [Pre-Post Installation Overview](#pre-post-installation-overview)
  - [Installation Steps](#installation-steps)
    - [Installing the PSS\1.0\136](#installing-the-pss10136)
    - [Setup the Web Server and Web Services](#setup-the-web-server-and-web-services)
- [Editing the Web Server and Assigning Web Services](#editing-the-web-server-and-assigning-web-services)
- [Web Server and Web Services Post-Installation Check](#web-server-and-web-services-post-installation-check)
- [Check Vendor Database Link](#check-vendor-database-link)
- [PEPS Services Menu and Options](#peps-services-menu-and-options)
  - [Check PEPS Services Setup](#check-peps-services-setup)
  - [Check Vendor Database Link](#check-vendor-database-link-1)
  - [Enable/Disable Vendor Database Link](#enabledisable-vendor-database-link)
- [Appendix A- Ensure Adequate Access to \[MGR.TEMP\], \[BIN\] and cacheexport.xsd (Temporary Change)](#appendix-a-ensure-adequate-access-to-mgrtemp-bin-and-cacheexportxsd-temporary-change)
The purpose of this Installation Guide is to provide an explanation of how to install Interface software and set up the Web Server and Services necessary for the Veterans Health Information Systems and Technology Architecture (VistA) -to- Medication Order Check Healthcare Application (MOCHA) v1.0 interface. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files required for drug selection through Pharmacy and Computerized Patient Record System (CPRS).

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSS\*1.0\*136 provides the functionality needed to prepare for the release of MOCHA v1.0, which will expand the current Pharmacy Order Checking system in addition to facilitating the switch from using the data stored in VistA to using data from a commercial database system for these order checks.

MOCHA v1.0 will interface existing VistA Pharmacy applications with a drug information database from a third-party vendor. This VistA-to-MOCHA v1.0 interface will parse incoming eXtensible Markup Language (XML) messages.

# Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MOCHA V1.0 will be rolled out in a phased implementation. Your site will be notified of your implementation date. Do not attempt to start this installation without the implementation team’s knowledge.

The initial setup of the Oracle Database, Operating System (OS) Cache, WebLogic framework, and the FDB Drug Information Framework (DIF) tables has been done. This pre-installation setup was done centrally, as the servers will not reside at the local sites.

# Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This PDM patch can only be run with a standard Massachusetts General Hospital Utility Multi-Programming System (MUMPS) operating system and requires the following Department of Veterans Affairs (VA) software packages.

|                                        |                            |
|----------------------------------------|----------------------------|
| Package                            | Minimum Version Needed |
| Pharmacy Data Management (PDM)         | 1.0                        |
| VA FileMan                             | 22.0                       |
| Kernel                                 | 8.0                        |
| Health*e*Vet Web Service Client (HWSC) | 1.0                        |
| VistA Link                             | 1.5                        |

The above software must be installed for this patch to be completely functional.

# Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*147 must be installed prior to installation of PSS\*1.0\*136.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA to MOCHA v1.0 interface consists of the standard Kernel Installation and Distribution system (KIDS) patch PSS\*1.0\*136 and the XML file PSSPRE_1_0.XML. (The XML file includes a Cache object that parses incoming XML responses.) These are both bundled in the zip file PSS_1_136.zip. The software will be distributed in a controlled release. Sites will be notified by the Implementation Team where to retrieve the software during their implementation phase.

The two components contained in the zip file are named:

- PRE_I_3_INTERFACE_BUILD.KID
- PSSPRE_1_0.XML

These files should be unzipped before placing them in the proper directories.

The software will be distributed in a controlled release. Sites will be notified by the Implementation Team how to retrieve the software during their implementation phase.

| Warning Installation Restrictions:            | Pharmacy users do not need to be off the system. If this patch is being installed for the first time, the only installation restriction is that it should NOT be installed when Pharmacy Data Management options are being used. It is also recommended that it should be installed during Non-Peak hours for CPRS, Inpatient Medications and Outpatient Pharmacy. One should not Queue the Install for a later time because there is user/installer interaction required during the installation. Installation should take no longer than 30 minutes. |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/002.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## Pre-Post Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Note:</strong></th>
<th rowspan="2"><p>Before continuing, these two steps must be performed:</p>
<ol type="1">
<li><p>Locate the cacheexport.xsd file on the VistA server. Both the file and the folder in which it resides <strong><u>MUST</u></strong> have world: read and execute (W:RE) access rights. If the permissions are not set this way, the installation will error. Instructions for setting permissions are found in Appendix A. (<strong><u>This requires Systems Administrator Privileges</u></strong>)</p></li>
<li><p>Ensure that XOBW 1.0 (HWSC v.1) has been installed on your system.</p></li>
</ol></th>
</tr>
<tr class="odd">
<th>![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/003.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The installation steps are outlined below:

1.  Retrieve the ZIP file PSS_1_136.zip as instructed by the Implementation Team, and extract all of the files.
2.  Place the PSSPRE_1_0.XML file in the Default Directory for Host File System (HFS), as stated in the Kernel Site Parameter file, which is usually the USER\$:\[TEMP\] folder on the VistA server. If using an FTP utility to place the PSSPRE_1_0.XML file, please ensure that you have selected BINARY mode for the transfer.
3.  Place the PRE_I_3_INTERFACE_BUILD.KID in an appropriate directory on the VistA server. If using an FTP utility to place the KIDS file, please ensure that you have selected ASCII mode for the transfer.
4.  Install the PSS\*1.0\*136 patch. For additional information, please refer to section *6.2.1 Installing the PSS\*1.0\*136*.
5.  Set up the Web Server and Web Services. This will allow VistA to make the XML request to Pharmacy Enterprise Product system (PEPS). For additional information, please refer to section *6.2.2 Setup the Web Server and Web Services*.

During the patch installation the environment check routine PSSHRENV checks for the existence of the mail group G.PSS ORDER CHECKS. If it doesn’t exist, the routine prompts the user for a mail group organizer and creates the mail group.

The POST-INIT routine PSSHRPST imports the pharmacy class file (PSSPRE_1_0.XML). A message is sent to the G.PSS ORDER CHECK mail group that the Installation of Patch PSS\*1.0\*136 has successfully completed.

## Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation steps include two main steps:

- Installing the PSS\*1.0\*136 Patch.
- Set up the Web Server and Web Services (assuming the XOBW 1.0 is already installed on the system).

### Installing the PSS\*1.0\*136

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Startup KIDS. Select the Kernel Installation and Distribution System Menu \[XPD MAIN\] option.

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
<p>Enter a Host File: <strong>USER$:[HFS]PRE_I_3_INTERFACE_BUILD.KID</strong></p>
<p>KIDS Distribution saved on Jan 13, 2011@09:34:21</p>
<p>Comment: Interface Package</p>
<p>This Distribution contains Transport Globals for the following Package(s):</p>
<p>Build PSS*1.0*136 has been loaded before, here is when:</p>
<p>. . .</p>
<p>. . .</p>
<p>. . .</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

4.  Answer YES to OK to continue with load.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OK to continue with Load? NO// <strong>YES</strong></p>
<p>Distribution OK!</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5.  Answer YES to want to continue with load.

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

6.  Answer YES to want to RUN the environment check routine.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Build PSS*1.0*136 has an Environmental Check Routine</p>
<p>Want to RUN the Environment Check Routine? YES// <strong>YES</strong> PSS*1.0*136</p>
<p>Use INSTALL NAME: PSS*1.0*136 to install this Distribution.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

7.  Install the package.

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

8.  Enter the package name.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select INSTALL NAME: <strong>PSS*1.0*136</strong> Loaded from Distribution 1/23/11@12:19:53</p>
<p>=&gt; Interface Package ;Created on Jan 13, 2011@09:34:21</p>
<p>This Distribution was loaded on Oct 28, 2010@12:19:53 with header of</p>
<p>Interface Package Test 11 ;Created on Jan 13, 2011@09:34:21</p>
<p>It consisted of the following Install(s):</p>
<p>PSS*1.0*136</p>
<p>Checking Install for Package PSS*1.0*136</p>
<p>Will first run the Environment Check Routine, PSSHRENV</p>
<p>Install Questions for PSS*1.0*136</p>
<p>Incoming Files:</p>
<p>59.73 VENDOR DISABLE/ENABLE</p>
<p>Note: You already have the 'VENDOR DISABLE/ENABLE' File.</p>
<p>59.74 VENDOR INTERFACE DATA</p>
<p>Note: You already have the 'VENDOR INTERFACE DATA' File.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

9.  Answer NO to rebuild menu trees.

| Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// \<RET\> |
|--------------------------------------------------------------------------|

10. Answer NO to not inhibit logons.

| Want KIDS to INHIBIT LOGONs during the install? NO// NO |
|-------------------------------------------------------------|

11. Answer NO to not disable scheduled, menu options and protocols.

| Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//NO |
|----------------------------------------------------------------------------|

12. Enter the device name you want to print the install messages.

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
<p>. . .</p>
<p>. . .</p>
<p>. . .</p>
<p>Install Completed</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

13. Check MailMan for installation completion message.

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
<p>You have 1 new message. (Last arrival: 06/29/09@14:30)</p>
<p>Select Installation Option: <strong>mailMan Menu</strong></p>
<p>VA MailMan 8.0 service for DOE.JOHN@PRECACHE.FO-BIRM.MED.VA.GOV</p>
<p>You last used MailMan: 1/23/11@11:35</p>
<p>You have 1 new message.</p>
<p>NML New Messages and Responses</p>
<p>RML Read/Manage Messages</p>
<p>SML Send a Message</p>
<p>Query/Search for Messages</p>
<p>AML Become a Surrogate (SHARED,MAIL or Other)</p>
<p>Personal Preferences ...</p>
<p>Other MailMan Functions ...</p>
<p>Help (User/Group Info., etc.) ...</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

14. Check for the “PSS\*1.0\*136 INSTALLATION COMPLETE” message.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select MailMan Menu Option: <strong>NML</strong> New Messages and Responses</p>
<p>Subj: PSS*1.0*136 Installation Complete [#95986] 1/23/11@12:22 1 line</p>
<p>From: PACKAGE PSS*1.0*136 INSTALL In 'IN' basket. Page 1 *New*</p>
<p>--------------------------------------------------------------------</p>
<p>Installation of Patch PSS*1.0*136 has been successfully completed!</p>
<p>Enter message action (in IN basket): Ignore//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Receiving the above message indicates the installation of PSS\*1.0\*136 is complete.

### Setup the Web Server and Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After patch PSS\*1.0\*136 is installed, you must modify or create the Web Server and Services to allow VistA to make the requests as follows:

1.  Enter or modify the Web Service entry in the Web Services file. This is done through the XOBW WEB SERVER MANAGER (Web Server Manager):

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Server Manager</strong> Jan 23, 2011@12:44:41 Page: 1 of 1</u></p>
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
<th><p><u><strong>Web Service Manager</strong> Jan 23, 2011@12:27:23 Page: 1 of 1</u></p>
<p>HWSC Web Service Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Service Name Type URL Context Root____________________</u></p>
<p><u>Enter ?? for more actions_______________________________________</u></p>
<p>AS Add Service</p>
<p>ES Edit Service</p>
<p>DS Delete Service</p>
<p>EP Expand Entry</p>
<p>Select Action:Quit// <strong>AS</strong> Add Service</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

3.  Select AS and enter the Web Services needed.
4.  Enter the data for ORDER_CHECKS as shown here:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select WEB SERVICE NAME: ORDER_CHECKS</p>
<p>Are you adding 'ORDER_CHECKS' as a new WEB SERVICE (the 1ST)? No// <strong>Y</strong> (Yes)</p>
<p>NAME: ORDER_CHECKS//</p>
<p>DATE REGISTERED: <strong>N</strong> (Jan 23, 2011@12:49:27)</p>
<p>TYPE: <strong>REST</strong> REST</p>
<p>CONTEXT ROOT: <strong>/MOCHA/</strong></p>
<p>AVAILABILITY RESOURCE: <strong>ordercheck</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

5.  Once the data for ORDER_CHECKS is done, enter the data for DRUG_INFO as shown here:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select WEB SERVICE NAME: DRUG_INFO</p>
<p>Are you adding 'DRUG_INFO' as a new WEB SERVICE (the 2nd)? No// <strong>Y</strong> (Yes)</p>
<p>NAME: DRUG_INFO//</p>
<p>DATE REGISTERED: <strong>N</strong> (Jan 23, 2011@12:49:27)</p>
<p>TYPE: <strong>REST</strong> REST</p>
<p>CONTEXT ROOT: <strong>/MOCHA/</strong></p>
<p>AVAILABILITY RESOURCE: <strong>druginfo</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

When completed, the two Web Services will appear as shown below:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Service Manager</strong> Jan 28, 2011@12:53:12 Page: 1 of 1</u></p>
<p>HWSC Web Service Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Service Name Type URL Context Root____________________</u></p>
<p>1 DRUG_INFO REST /MOCHA/</p>
<p>2 ORDER_CHECKS REST /MOCHA/</p>
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

Both ORDER_CHECKS and DRUG_INFO must be entered exactly as shown above.

# Editing the Web Server and Assigning Web Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After building the Web Services you must enter or edit the Web Server and assign the Web Services to the server. In this case, the PEPS server must be entered from the Web Server manager and Web services should be assigned as shown in the screens that follow.

| Note:                                         | The server and port number will be provided to you by the Implementation Team. |
|---------------------------------------------------|--------------------------------------------------------------------------------|
| ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/004.png) |                                                                                |

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
<td><p>Select WEB SERVER NAME: PEPS</p>
<p>Are you adding 'PEPS' as a new WEB SERVER (the 1ST)? No// y (Yes)</p>
<p>NAME: PEPS//</p>
<p>SERVER: 10.4.232.15 (or r02ausapp80.r02. <mark>REDACTED</mark>)</p>
<p>PORT: 80// 7003</p>
<p>DEFAULT HTTP TIMEOUT: 30//</p>
<p>STATUS: E ENABLED</p>
<p>Security Credentials</p>
<p>====================</p>
<p>LOGIN REQUIRED:</p>
<p>Authorize Web Services</p>
<p>======================</p>
<p>Select WEB SERVICE: ORDER_CHECKS</p>
<p>Are you adding 'ORDER_CHECKS' as</p>
<p>a new AUTHORIZED WEB SERVICES (the 1ST for this WEB SERVER)? No// Y (Yes)</p>
<p>STATUS: E ENABLED</p>
<p>Select WEB SERVICE: DRUG_INFO</p>
<p>Are you adding 'DRUG_INFO' as</p>
<p>a new AUTHORIZED WEB SERVICES (the 2ND for this WEB SERVER)? No// Y (Yes)</p>
<p>STATUS: E ENABLED</p>
<p>Select WEB SERVICE:</p></td>
</tr>
</tbody>
</table>

The PEPS server has an Internet Protocol (IP) address and a port number. The information may also be provided in the form of a Fully Qualified Domain Name (FQDN) and port number. If the Implementation Team supplies you with a FQDN, use this in place of the IP address. These numbers may be different depending on the server VistA is connecting to. All other data remains the same. The Server and Port numbers in the example above are just examples, and each site will be provided these numbers by the Implementation Team.

Using the Web Server Manager option, check the setup of the PEPS Web Server by entering EP (Expand Entry) and select the PEPS server. The system should have the following data associated with it:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>===============================================================================</p>
<p>1 *PEPS 10.4.232.15:7003</p>
<p>-------------------------------------------------------------------------------</p>
<p>NAME: PEPS PORT: 7003</p>
<p>SERVER: 10.4.232.15 STATUS: ENABLED</p>
<p>DEFAULT HTTP TIMEOUT: 30 LOGIN REQUIRED: NO</p>
<p>WEB SERVICE: ORDER_CHECKS STATUS: ENABLED</p>
<p>WEB SERVICE: DRUG_INFO STATUS: ENABLED</p>
<p>-------------------------------------------------------------------------------</p>
<p>Lookup keys associated with server:</p>
<p>&lt;No lookup keys associations&gt;</p>
<p>===============================================================================</p>
<p>Enter RETURN to continue or '^' to exit:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

The name of the server, PEPS, and its respective services, DRUG_INFO and ORDER_CHECKS, must remain static. These names are used in the interface code to access the correct Web server and services. As stated previously, the only data elements that should change are the IP address or the port number.

# Web Server and Web Services Post-Installation Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After successfully setting up the Web Server and Web Services, the user can test the communication by selecting the CK--Check Web Service Availability option as shown in the next two screens:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><u><strong>Web Server Manager</strong> Jan 23, 2011@13:10:51 Page: 1 of 1</u></p>
<p>HWSC Web Server Manager</p>
<p>Version: 1.0 Build: 31</p>
<p><u>ID Web Server Name IP Address or Domain Name:Port</u></p>
<p>1 *PEPS 10.4.232.15:7003</p>
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
<th><p><u><strong>Web Service Availability</strong> Oct 28, 2010@13:11:04 Page: 1 of 1</u></p>
<p>Web Server:</p>
<p>1 *PEPS 10.4.232.15:7003</p>
<p><u>_____________________________________________________________________________</u></p>
<p>1 ORDER_CHECKS is available</p>
<p>2 DRUG_INFO is available</p>
<p>Enter ?? for more actions</p>
<p>Actions</p>
<p>Select Action:Quit//</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# Check Vendor Database Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Run the *PEPS Services Option Menu* \[PSS PEPS SERVICES\] option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Check Vendor Database Link</p>
<p>Check PEPS Services Setup</p>
<p>Select PEPS Services Option: <strong>Check Vendor Database Link</strong></p>
<p>Database Version: 6</p>
<p>Build Version: 3.2</p>
<p>Issue Date: 1/23/2011</p>
<p>Custom Database Version: 6</p>
<p>Custom Build Version: 3.2</p>
<p>Custom Issue Date: 1/13/2011</p>
<p>Connected to Vendor database successfully @Jan 23, 2011@14:18</p>
<p>Press Return to Continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If you get the message “Connected to Vendor database successfully …” it means the connection was successful.

# PEPS Services Menu and Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the PEPS Services menu. This menu contains the following options:

To get the list of this menu, select *PEPS Services Option Menu* \[PSS PEPS SERVICES\] option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Check Vendor Database Link</p>
<p>Check PEPS Services Setup</p>
<p>Select PEPS Services Option:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

This section also describes the *Enable/Disable Vendor Database Link* option that is exported as a standalone menu option.

## Check PEPS Services Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS PEPS SERVICES\]

This option provides the ability to check and validate that the link to the vendor interface used for enhanced order checking is enabled and operational. It also provides the ability to execute various order checks against the vendor database to ensure that the database is installed and reachable.

To check the PEPS services setup, select the *PEPS Services Option Menu*.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Check Vendor Database Link</p>
<p>Check PEPS Services Setup</p>
<p>Schedule/Reschedule Check PEPS Interface</p>
<p>Select PEPS Services Option: <strong>Check PEPS Services Setup</strong></p>
<p>Checking Vendor Database Connection...OK</p>
<p>Press Return to Continue:</p>
<p>Performing Drug-Drug Interaction Order Check for ASPIRIN 325MG TAB and WARFARIN</p>
<p>10MG TAB...OK</p>
<p>Significant Drug Interaction: The concurrent use of anticoagulants and</p>
<p>salicylates may result in increased INR values and increase the risk of</p>
<p>bleeding.</p>
<p>Press Return to Continue:</p>
<p>Performing Duplicate Therapy Order Check for CIMETIDINE 300MG TAB and</p>
<p>RANITIDINE 150MG TAB...OK</p>
<p>Therapeutic Duplication with CIMETIDINE 300MG TAB and RANITIDINE 150MG TAB</p>
<p>Duplicate Therapy Class(es): Peptic Ulcer Agents,Histamine-2 Receptor</p>
<p>Antagonists (H2 Antagonists)</p>
<p>Press Return to Continue:</p>
<p>Performing Dosing Order Check for ACETAMINOPHEN 500MG TAB - 3000MG Q4H...OK</p>
<p>Single dose amount of 3000 MILLIGRAMS exceeds the maximum single dose mount</p>
<p>of 1000 MILLIGRAMS.</p>
<p>Total dose amount of 18000 MILLIGRAMS/DAY exceeds the dosing range of 320</p>
<p>MILLIGRAMS/DAY to 4000 MILLIGRAMS/DAY.</p>
<p>Press Return to Continue:</p>
<p>Performing Custom Drug-Drug Interaction Order Check for CLARITHROMYCIN 250MG</p>
<p>TAB and DIAZEPAM 5MG TAB...OK</p>
<p>Significant Drug Interaction: Serum concentrations of certain</p>
<p>benzodiazepines may be increased enhancing their pharmacological effects.</p>
<p>Press Return to Continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Check Vendor Database Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows the user to check if the FDB link is up and running or unreachable.

To check the link, select *PEPS Services Option Menu* \[PSS PEPS SERVICES\] option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Check Vendor Database Link</p>
<p>Check PEPS Services Setup</p>
<p>Schedule/Reschedule Check PEPS Interface</p>
<p>Select PEPS Services Option: <strong>Check Vendor Database Link</strong></p>
<p>Database Version: 6</p>
<p>Build Version: 3.2</p>
<p>Issue Date: 1/13/2011</p>
<p>Custom Database Version: 6</p>
<p>Custom Build Version: 3.2</p>
<p>Custom Issue Date: 1/23/2011</p>
<p>Connected to Vendor database successfully @JAN 23, 2011@14:12</p>
<p>Press Return to Continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

If you get the message “Connected to Vendor database successfully …” it means the connection to the vendor database was successful.

## Enable/Disable Vendor Database Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[PSS ENABLE/DISABLE DB LINK\]

This option provides the ability to disable/enable the link to the vendor interface used for enhanced order checking. When disabled, NO drug-drug interaction, duplicate therapy or dosing order checks will be performed in Pharmacy or in the Computerized Patient Record System (CPRS). NOTE: No dosing order checks will be performed until MOCHA V2.0 is released.

After enabling or disabling the link, user name, date/time of when the links were disabled or enabled is recorded in the VENDOR DISABLE/ENABLE file (#59.74). The content of this file may be viewed using FileMan’s *INQUIRE TO FILE ENTRIES* option.

To enable the link, select *PEPS Enable/Disable Vendor Database Link*.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: <strong>PSS ENABLE/DISABLE DB LINK</strong> Enable/Disable Vendor Database Link</p>
<p>Enable/Disable Vendor Database Link</p>
<p>WARNING! The connection to the Vendor database is currently DISABLED.</p>
<p>NO Drug-Drug Interactions,Duplicate Therapy, or Dosing Order Checks</p>
<p>will be performed while the connection is disabled!!!</p>
<p>Do you wish to ENABLE the Vendor database connection? YES// <strong>YES</strong></p>
<p>Vendor database connection enabled.</p>
<p>Connected to Vendor database successfully.</p>
<p>Press Return to Continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

To disable the link, select *PEPS Enable/Disable Vendor Database Link*

\[PSS ENABLE/DISABLE DB LINK\] option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Select OPTION NAME: <strong>PSS ENABLE/DISABLE DB LINK</strong> Enable/Disable Vendor Database Link</p>
<p>Enable/Disable Vendor Database Link</p>
<p>The connection to the Vendor database is currently ENABLED.</p>
<p>Do you wish to DISABLE the connection to the Vendor database? NO// <strong>YES</strong></p>
<p>NO Drug-Drug Interactions,Duplicate Therapy, or Dosing Order Checks</p>
<p>will be performed while the connection is disabled!!!</p>
<p>Are you sure you want to DISABLE the connection to the Vendor Database? NO//<strong>YES</strong></p>
<p>Vendor database connection DISABLED.</p>
<p>REMEMBER to ENABLE the Vendor database connection AFTER task completed.</p>
<p>Press Return to Continue:</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

*(This page included for two-sided copying.)*

# Appendix A- Ensure Adequate Access to \[MGR.TEMP\], \[BIN\] and cacheexport.xsd (Temporary Change)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requires: System Administrator Privileges

During the installation and on each system in your configuration, ensure that the corresponding subdirectories \[MGR.TEMP\] and \[BIN\] beneath the Caché install directory, as well as the file cachexport.xsd in the \[BIN\] folder, have adequate protections for loading Caché Objects from an XML file.

| Note:                                         | For a Linux installation, the equivalent subdirectories would be mgr/temp and bin in the corresponding Caché install directory. The equivalent access permission in Linux for W:RWED and W:RE would be Other RWX and Other RW. |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/005.png) |                                                                                                                                                                                                                                |

Follow these steps to apply the necessary protections:

1.  Identify the location of the Caché install directory for your configuration. You can find this location by using the following Caché command from your corresponding OS command line:

> \$ ccontrol list

> . . .

> Configuration ' BOIR1TSVR' (default)

> directory: \_\$1\$DGA2:\[CACHESYS.BOIR1TSVR\]

> versionid: 5.2.3.710.0.8574

> conf file: BOIR1TSVR.cpf (SuperServer port = 19722)

> status: running, since Wed Jul 28 18:03:54 2010

> . . .

2.  Identify the location of the TEMP directory (within the Caché install directory) by logging into the M account-- the account you plan to install in -- and then executing the following command:

> DEVMOU\> write \##class(%SYS.System).TempDirectory() \<RET\>

> Depending on your system, the name of the location may look like this:

> \_DSA158:\[CACHESYS.BOIR1TSVR.MGR.TEMP\]

| Note:                                         | On Caché 2008.2.5 or higher systems, the directory returned by the function above may be the same directory you've already designated as the system temp folder with ^%SYS("TempDir"), rather than a directory under the Caché install folder. |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/006.png) |                                                                                                                                                                                                                                                |

3.  Ensure that the designated TEMP subdirectory has World RWED protection. If not, record the original setting, and then set it to World RWED protection.
4.  Examine the protection settings of the BIN directory (a peer to/at the same level as the MGR directory), e.g.,

> \_DSA158:\[CACHESYS.BOIR1TSVR.BIN\]

> Ensure that the BIN directory has at least W:RE (world: read execute). If not, record the original setting, and set it to World RE protection.

| Note:                                         | On Caché 2008.2.5 or higher systems, this may already be accessible to at least W:RE access, e.g., via an ACL setting on VMS systems. |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/007.png) |                                                                                                                                       |

5.  In the BIN directory, examine the protection setting on the file cacheexport.xsd. Ensure that this file has at least W:RE (world: read execute) protection. If not, record the original setting, and set it to World RE protection.

| Note:                                         | On Caché 2008.2.5 or higher systems, this may already be accessible to at least W:RE access, e.g., via an ACL setting on VMS systems. |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](pss-1-136-installation-guide-vista-to-mocha-version-1-interface/008.png) |                                                                                                                                       |

6.  Repeat steps 1-5 on all the Caché boxes/instances in your configuration
7.  Continue with the rest of the installation.
8.  Restore any VMS-level protection settings that were altered in the Caché install directory.