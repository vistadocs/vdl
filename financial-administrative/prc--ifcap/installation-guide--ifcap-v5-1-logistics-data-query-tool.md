---
title: IFCAP Version 5.1 Logistics Data Query Tool Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: Logistics Data Query Tool
app_code: PRC
app_name: IFCAP
section: FIN
app_status: archive
pkg_ns: PRC
patch_ver: 5.1
patch_id: PRC*5.1
group_key: "PRC:PRC:5.1"
file_numbers: 
  - 200
security_keys: []
menu_options: 0
description: > Patch PRC\5.1\103 implements the VistA side of the Logistics Data Query Tool (or, more simply, the Query Tool). Made available with the patch is an InstallShield® executable for the graphical user interface (GUI) components of the Query Tool client. This document covers primarily the GUI component
audience: 
keywords: 
  - blockquote
  - strong
  - table
  - query
  - tool
  - contents
  - installation
  - class
  - version
  - guide
page_count: 0
word_count: 3712
section_count: 14
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2000
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP_Archive/ifcp5_1ldqt_installation_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/IFCAP_Archive/ifcp5_1ldqt_installation_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=263"
---

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/001.png)

Integrated Funds Distribution, Control Point Activity, Accounting and Procurement

> (IFCAP)

> Version 5.1

> October 2000

> Revised May 2007

> Logistics Data Query Tool

> INSTALLATION GUIDE

> Department of Veterans Affairs

> Office of Information and Technology (OI&T) Management, Enrollment, and Financial Systems

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
  - [![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/002.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/003.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/004.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/005.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/006.png)Online Documentation Available](#ifcap-version-5-1-logistics-data-query-tool-installation-guide002pngifcap-version-5-1-logistics-data-query-tool-installation-guide003pngifcap-version-5-1-logistics-data-query-tool-installation-guide004pngifcap-version-5-1-logistics-data-query-tool-installation-guide005pngifcap-version-5-1-logistics-data-query-tool-installation-guide006pngonline-documentation-available)
  - [About the Query Tool](#about-the-query-tool)
  - [Purpose of this Guide](#purpose-of-this-guide)
  - [Designated Query Tool Users](#designated-query-tool-users)
- [Deployment Overview](#deployment-overview)
  - [Software Retrieval](#software-retrieval)
  - [Required Access and Rights Needed](#required-access-and-rights-needed)
  - [Hardware and Operating Systems Requirements](#hardware-and-operating-systems-requirements)
    - [Software Requirements](#software-requirements)
    - [Workstation Hardware Requirements and Guidelines](#workstation-hardware-requirements-and-guidelines)
- [Pre-Installation Instructions and Preparation](#pre-installation-instructions-and-preparation)
  - [Database Information](#database-information)
- [Setting up a Query Tool User](#setting-up-a-query-tool-user)
  - [VistA Pre-Installation Notes](#vista-pre-installation-notes)
  - [VistA Installation Instructions](#vista-installation-instructions)
  - [The Remote Procedure Call Broker](#the-remote-procedure-call-broker)
    - [The RPC Broker](#the-rpc-broker)
    - [Ensuring RPC Broker Client Agent is Installed](#ensuring-rpc-broker-client-agent-is-installed)
    - [Ensure RPC Broker Client Agent Connection is Available](#ensure-rpc-broker-client-agent-connection-is-available)
    - [Server List](#server-list)
  - [Client Components Installation](#client-components-installation)
    - [Run InstallShield Executable](#run-installshield-executable)
    - [Verify Query Tool Client on Workstations](#verify-query-tool-client-on-workstations)
- [Installation Checklists](#installation-checklists)
- [Technical Information](#technical-information)
  - [![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/032.png)Directories and Files](#ifcap-version-5-1-logistics-data-query-tool-installation-guide032pngdirectories-and-files)
    - [Query Tool Application Files](#query-tool-application-files)
    - [RPC Broker Files](#rpc-broker-files)
> This guide documents Version 01 of the Logistics Data Query Tool Graphical User Interface (GUI) application. For future releases, information will be included here on changes and new features.
<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Date</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Revision</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Author(s)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>5/31/2007</p>
</blockquote></td>
<td><blockquote>
<p>01</p>
</blockquote></td>
<td><blockquote>
<p>Initial issue</p>
</blockquote></td>
<td><blockquote>
<p>REDACTED,</p>
<p>REDACTED, REDACTED</p>
</blockquote></td>
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
> Revision History
> THIS PAGE INTENTIONALLY LEFT BLANK

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PRC\*5.1\*103 implements the VistA side of the Logistics Data Query Tool (or, more simply, the Query Tool). Made available with the patch is an *InstallShield*® executable for the graphical user interface (GUI) components of the Query Tool client. This document covers primarily the GUI components of the Query Tool; installation instructions for the IFCAP patch itself are included in the FORUM patch release.

## ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/002.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/003.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/004.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/005.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/006.png)Online Documentation Available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## About the Query Tool

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Query Tool is a Windows software application that acts as a “front-end” to enable users to more easily find, display, and export VistA purchase order data. The Query Tool is a substitute for the VA FileMan utility program which has traditionally been employed to look directly at the MUMPS globals (files) which store VistA data. The Query Tool enables users to…

- Search for data and display data by a range of dates
- Sort and rearrange the view of the data; display the data in a custom view
- Export the data into a Microsoft® Excel® spreadsheet file

## Purpose of this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This Manual explains the fundamentals of how to install the GUI components of the Query Tool. Throughout this document, any references to “Guide,” “the Guide,” or “this Guide” should be interpreted to mean the *Logistics Data Query Tool Installation Guide* (this document).

## Designated Query Tool Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Specific users at each site or facility will be designated as Query Tool users by the Prosthetics and Clinical Logistics Office (PCLO). *Only designated individuals are permitted to use the Query Tool!* Neither the IFCAP option which permits the Query Tool to work, nor the GUI components of the Query Tool, should be made available to any individual not so designated.

> Introduction

> THIS PAGE INTENTIONALLY LEFT BLANK

# Deployment Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Software Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Patch PRC\*5.1\*103 is distributed via FORUM. This patch should be installed *before*

> attempting to install the GUI components of the Query Tool.

> Installation of the associated GUI client software, including the Query Tool executable, is accomplished via an *InstallShield*® executable. This executable, PRCLogisticsTools_v\*.exe (where \* is the version number), should be copied from an Anonymous.pub directory to a local shared drive at each site accessible by site IRM staff members or authorized users. “Authorized” Query Tool users are those persons specifically designated by the Prosthetics and Clinical Logistics Office (PCLO).

## Required Access and Rights Needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Programmer access is *not* required for setting up the VistA portion of the Query Tool. Anyone with access to the Kernel Installation & Distribution System \[XPD MAIN\] menu and the options Add a New User to the System \[XUSERNEW\] and Edit an Existing User \[XUSEREDIT\] option can install this patch in VistA and set up user access. Information Resources Management (IRM) personnel or other personnel setting up the GUI components must have administrator rights on the user’s workstation.

## Hardware and Operating Systems Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The VistA Remote Procedure Call (RPC) Broker Version 1.1 or higher must be properly installed and configured on the workstation (see 4.3 below)
- The current version of the RPC Broker is a 32-bit application; for this reason, the workstation must be running a 32-bit operating system (such as Microsoft Windows 95®, Windows 2000®, Windows NT®, or Windows XP®)
- Microsoft *Excel*® 97 or later version

### Workstation Hardware Requirements and Guidelines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The Query Tool runs on the standard hardware platforms used by Department of Veterans Affairs (VA) healthcare facilities.

> Deployment Overview

> THIS PAGE INTENTIONALLY LEFT BLANK

# Pre-Installation Instructions and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Database Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- There are no new VA FileMan globals. This application uses File \#19 (OPTION file). It extracts data from File \#442 (PO Data) and File \#664 (Prosthetics orders). It also uses a pointer to File \#441 (Item Master) to pick up the Short Description field and the NIF Item Number.
- No changes to file/global size are anticipated. This application sends data queries to VistA via the Remote Procedure Call (RPC) Broker and returns VistA data to the application.
- If the local symbol table partition size is less than two megabytes, store errors may result. This is particularly true if the user selects Item Detail – ITM as a custom data field (see the *Query Tool Manual*, Select Custom Data). In addition, retrieving orders with more than 40 or so items may result in a “hard crash” if the site’s symbol table partition size is inadequate. Current information indicates that a minimum partition size of 2 MB is required.
- ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/007.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/008.png)No new or additional data is stored or changed in VistA.
- There are no applicable relational tables or diagrams.

> Pre-Installation Instructions and Preparation

> THIS PAGE INTENTIONALLY LEFT BLANK

# Setting up a Query Tool User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please note that this is *not* an “all hands” installation; only individuals specifically identified by the PCLO (or designee) will be given access to the Query Tool.

> Setting up a user for the Query Tool involves actions on the VistA server and on the user’s workstation:

- Assigning the IFCAP B-type option PRCHL GUI
- Ensuring that the Remote Procedure Call (RPC) Broker Client Agent is installed and operational
- Running an *InstallShield*® executable to install the Query Tool software and related files
- Verifying with the user operation of the Query Tool

## VistA Pre-Installation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *See* Table 1 –Checklist: VistA Pre-Installation

## VistA Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to use the Query Tool and the RPC, users must have a B-type option assigned as one of their menu options. The Query Tool application will only run for those users who are allowed to activate it.

> This “B” type option is not invokable from a menu. B-type options are designed to be run only by the RPC Broker. Client/server applications like the Query Tool are a "B" (*i.e.*, Broker) type of option in the OPTION file (File \#19).

> *After* patch PRC\*5.1\*103 is installed, designated Query Tool users must have the client/server application option LOGISTICS DATA TOOL \[PRCHL GUI\] assigned to them via option Add a New User to the System \[XUSERNEW\] or Edit an Existing User \[XUSEREDIT\].

> This option should normally be added as a *secondary* menu option. Although the option can be installed on a primary menu, the established standard is that such options should be placed on a secondary menu. The option should be assigned as a primary menu option *only* if use of the Query Tool is to be the user’s only activity on this VistA system.

> Setting Up a Query Tool User

> *See* Table 2 –Checklist: Setting up Query Tool User in IFCAP

## The Remote Procedure Call Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Query Tool uses the Remote Procedure Call (RPC) protocol to communicate with a VistA server.

### The RPC Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The RPC Broker is “helper” software that allows a computer program to make remote procedure calls from one computer to another, via a network. The Broker establishes a common and consistent foundation for client/server applications written under the VistA umbrella. The Broker acts as a bridge connecting the client application front-end on the workstation (in this case, the Query Tool) to the M-based data and business rules on the server. It serves as the communications medium for messaging between VistA client/server applications. Upon receipt, the message is decoded, the requested remote procedure call is activated, and the results are returned to the calling application. Thus, the Broker helps bridge the gap between the traditionally proprietary VA software and other types of software.

> The RPC Broker includes:

- A common communications driver interface that handles the device-specific characteristics of the supported communications protocol.
- An interface component separate from the communications driver that interprets the message, executes the required code, and eventually returns data to the communications driver.
- A common file which all applications use to store the information on the queries to which they respond (*i.e.*, the REMOTE PROCEDURE file \[#8994\]).

### Ensuring RPC Broker Client Agent is Installed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Since this software is essential to the operation of the Query Tool, each user workstation must be checked to determine if the Broker client agent is installed and properly working.

> The RPC Broker Client Agent program (ClAgent.exe) runs in support of the single sign-on process (also called auto sign-on). This program automatically and continuously runs in the background on the client workstation, but may be closed or shut down by the user if resource availability is a problem.

> Setting Up a Query Tool User

> *See* Table 3 –Checklist: Ensure RPC Broker Client Agent Installed

### Ensure RPC Broker Client Agent Connection is Available

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the Client Agent (CA) is installed on the user workstation, the CA icon ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/009.png) will be displayed in the Windows System Tray if the Broker Client Agent is running.

> *See* Table 4 –Checklist: Verify Client Agent

![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/010.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/011.png)

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/012.png)Figure 4-1 Using Windows Task Manager to Check Client Agent

> If CA is not running, manually run the agent, then check to see if the icon appears in the system tray (Figure 4-2).

3.  Logistics Data Query Tool Installation Guide Version 01

> May 2007

> Setting Up a Query Tool User

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/013.png)Figure 4-2 Client Agent Icon in System Tray

> For more information about the connection(s), double-click the icon. You’ll see the pop- up dialog shown in Figure 4-3.

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/014.png)Figure 4-3 Client Agent Information Pop-Up

![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/015.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/016.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/017.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/018.png)

### Server List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use of the Query Tool also requires that the list of RPC Broker servers which the user is authorized to access be maintained on the workstation. The user must be able to reach at least one VistA server in order to use the Query Tool.

> In order for the Query Tool to connect to a VistA server, Broker information for that server must be available on the user’s workstation.

4.  Logistics Data Query Tool Installation Guide Version 01

> May 2007

> Setting Up a Query Tool User

> Invoke the application ServerList.exe on the workstation to define the Broker IP address and port for the VistA server(s) to be used. ServerList.exe is described in the RPC Broker *Systems Manual*.

> Both xwb1_1ws.exe and ServerList.exe, which are mentioned in the Broker System Manual, are distributed as part of the Broker.

> *See* Table 4 –Checklist: Verify Client Agent

## Client Components Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Once the PRCHL GUI option is assigned to the user and the RPC Broker Client Agent is properly installed, the Query Tool executable file should be installed on each Windows desktop where the Query Tool will be run.

### Run InstallShield Executable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation of the Query Tool application, as well as the online help file associated with the application, is handled by the *InstallShield* executable PRCLogisticsTools_v\*.exe (where \* is the version number), which will:

- Create the necessary folder on the user workstation: C:\Program Files\VISTA\IFCAP
- Install the Query Tool, Help File components, and required dynamic link libraries (DLLs) in the appropriate folders
- Create a shortcut icon on the user’s desktop

> The current version of PRCLogisticsTools_v\*.exe is available from your

> Anonymous.pub directory.

> *See* Table 6 –Checklist: Run InstallShield

5.  Logistics Data Query Tool Installation Guide Version 01

> May 2007

> Setting Up a Query Tool User

![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/019.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/020.png)

### Verify Query Tool Client on Workstations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you have configured the RPC broker client and installed the Delphi executable file (PRCLogisticsTools.exe) on the computer workstation, you should then follow the steps in Table 7 to verify that the Query Tool is working as expected. If possible, you should have the user go through these steps with you observing.

> *See* Table 7 –Checklist: Verify Query Tool Client on Workstations. It may also be desirable to have the *Logistics Data Query Tool User Manual* available; it shows the various screens, messages and pop-ups that may be encountered.

# Installation Checklists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following checklists cover the complete installation process. Refer to the explanatory sections noted in the “See” column if necessary. The “Step” numbers run consecutively throughout the series of checklists.

> Table 1 –Checklist: VistA Pre-Installation

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 78%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>1</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>File Backup.</strong> A backup of the transport global is recommended before installing the patch. No pre-installation reports are generated.</p>
</blockquote></td>
<td rowspan="5"><blockquote>
<p><strong>N/A</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>2</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Software Installation Time.</strong> The estimated installation time for the patch is under 15 minutes during off-peak hours.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>3</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Users on the System.</strong> Users can remain on the system during installation. Users who are assigned the <strong>PRCHL GUI</strong> option may be required to log off and then log back on again after the option is assigned.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>4</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Namespace.</strong> The Query Tool uses namespace <strong>PRCHL</strong>; verify this namespace is available.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>5</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>Patch Required.</strong> Patch <strong>PRC*5.1*103</strong> <em>must</em> be installed before attempting to install the Query Tool.</p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Table 2 –Checklist: Setting up Query Tool User in IFCAP

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 73%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>6</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Find, open and read the <strong>ReadMe.txt</strong> file for any updates to instructions or processes.</p>
</blockquote></td>
<td><blockquote>
<p><strong>N/A</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td rowspan="4"><blockquote>
<p><strong>7</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Ensure that each designated user of the Query Tool has been:</p>
</blockquote></td>
<td rowspan="4"><blockquote>
<p><strong>4.2</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>a</strong></p>
</blockquote></td>
<td><blockquote>
<p>Set up as a VistA user.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>b</strong></p>
</blockquote></td>
<td><blockquote>
<p>Granted access to one or more VistA servers.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>c</strong></p>
</blockquote></td>
<td><blockquote>
<p>Assigned an Access Code and a Verify Code.</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>8</strong></p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Place the IFCAP option <strong>PRCHL GUI</strong> on the user’s secondary menu. Note that this is a B-type option, designed to be run only by the RPC Broker; it cannot be run from the menu system. This option is set in the <strong>NEW PERSON</strong> file (<strong>File #200</strong>).</p>
<p>System Manager Menu (EVE)</p>
<p>User Management Menu (XUSER)</p>
<p>Edit an Existing User (XUSEREDIT) Select NEW PERSON NAME:</p>
<p>Select Secondary Menu Options (screen editor option) Enter PRCHL GUI</p>
<p>Save and Exit</p>
</blockquote></td>
<td><blockquote>
<p><strong>4.2</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Setting Up a Query Tool User

> Table 3 –Checklist: Ensure RPC Broker Client Agent Installed

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/021.png) ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/022.png)

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/023.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/024.png)Table 4 –Checklist: Verify Client Agent is Running

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 78%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>10</strong></p>
</blockquote></td>
<td><blockquote>
<p>Use the Windows Task Manager to verify that CA is running on the user’s workstation.</p>
<p>If CA is not running, manually run the agent, then check to see if the icon appears in the system tray (Figure 4-2).</p>
</blockquote></td>
<td><blockquote>
<p><strong>Figure 4-1</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>11</strong></p>
</blockquote></td>
<td><blockquote>
<p>Ensure that the Client Agent Icon appears in the System Tray.</p>
</blockquote></td>
<td><blockquote>
<p><strong>Figure 4-2</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>12</strong></p>
</blockquote></td>
<td><blockquote>
<p>Right-click the Client Agent Icon and select Show. If the Start Client with Windows box is checked, uncheck it unless the user specifically requires this startup option.</p>
</blockquote></td>
<td><blockquote>
<p><strong>Figure 4-3</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/025.png)Table 5 –Checklist: Install and Run ServerList

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 78%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>13</strong></p>
</blockquote></td>
<td><blockquote>
<p>On the workstation, define the RPC Broker server to be used by installing and executing <strong>ServerList.exe</strong>, which is described in the RPC Broker <strong>Systems Manual</strong> (available on the VDL). Both <strong>xwb1_1ws.exe</strong> and <strong>ServerList.exe</strong>, which are mentioned in the manual, are distributed as part of the RPC Broker.</p>
<p><em>See also</em> <a href="http://www.hardhats.org/cs/broker/docs/xwb1_1rn.html">http://www.hardhats.org/cs/broker/docs/xwb1_1rn.html</a> for more helpful information about installing and configuring <strong>ServerList.exe</strong>.</p>
</blockquote></td>
<td><blockquote>
<p><strong>4.3.4</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Setting Up a Query Tool User

> Table 6 –Checklist: Run InstallShield

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 78%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>14</strong></p>
</blockquote></td>
<td><blockquote>
<p>Find <strong>PRCLogisticsTools_v*.exe</strong> on your site shared drive and double-click it to run the <em>InstallShield</em> executable. Follow any instructions presented, and always accept any defaults offered.</p>
<p>If necessary, the program can be downloaded to the user workstation and run from that location.</p>
</blockquote></td>
<td><blockquote>
<p><strong>4.4.1</strong></p>
</blockquote></td>
<td></td>
</tr>
</tbody>
</table>

> Table 7 –Checklist: Verify Query Tool Client on Workstations

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 79%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>15</strong></p>
</blockquote></td>
<td><blockquote>
<p>Verify that the <strong>Logistics Data Query Tool</strong> shortcut icon exists on the user’s desktop.</p>
</blockquote></td>
<td><blockquote>
<p><strong>4.4.2</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>16</strong></p>
</blockquote></td>
<td><blockquote>
<p>Terminate any open VistA sign-on sessions. (Why? To make certain that the Query Tool can handle the sign-on.)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>17</strong></p>
</blockquote></td>
<td><blockquote>
<p>Double click on the shortcut to verify that the Query Tool activates.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>18</strong></p>
</blockquote></td>
<td><blockquote>
<p>From the Home Screen, click [ VISTA Sign-on ].</p>
<p>When the sign-on dialog appears (before actually signing-on) try to access the RPC Broker Help file by clicking [ Help ]. Exit the Help by closing the Help window. (Why? To make certain the RPC Broker Help is available.)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>19</strong></p>
</blockquote></td>
<td><blockquote>
<p>Have the user sign-on to at least one of the available VistA servers to confirm access and connectivity. (If no server appears to be available, see</p>
<p>4.3.4 above)</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>20</strong></p>
</blockquote></td>
<td><blockquote>
<p>After successful sign-on: From the Home Screen, have the user click</p>
<p>[ <u>L</u>ogistics Detail Display ] to activate the Query Tool Detail Display screen. A confidentiality warning will be displayed; the user should click [ OK ] to open the Detail Display screen. From the Detail Display screen, user should execute a query for a date range known to have data available. If expected data is displayed, the Query Tool is functioning correctly. If necessary, consult the <em>Logistics Data Query Tool User Manual</em> for information on how to do such queries.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>21</strong></p>
</blockquote></td>
<td><blockquote>
<p>From the Detail Display screen, with data displayed, have the user export data to <em>Excel</em>, by clicking [ E<u>x</u>cel ]. After the user chooses a drive/directory for use, <em>Excel</em> should open and display the same data that’s shown on the Detail Display screen. The <em>Excel</em> file will have a “.CSV” file extension, and the filename itself will represent the date range chosen.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>22</strong></p>
</blockquote></td>
<td><blockquote>
<p>From both Query Tool screens, have the user attempt to access the Help File by pressing &lt;F1&gt;. In a pop-up window, the user should see the Help</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 5-3 Logistics Data Query Tool Installation Guide Version 01

> May 2007

> Setting Up a Query Tool User

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 79%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Step</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>See</strong></p>
</blockquote></th>
<th><blockquote>
<p></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>File, with the caption Help Topics: PRCLogisticsTools. The user should click [ Cancel ] to close the Help File.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/026.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/027.png)

>  Once all the above steps are checked off, installation and verification is complete.

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/028.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/029.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/030.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/031.png)

## ![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/032.png)Directories and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Query Tool Application Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Query Tool application and its associated files are stored in the directory C:\Program Files\VISTA\IFCAP\\. This directory is created by the Query Tool *InstallShield* executable PRCLogisticsTools.exe. The files directly related to the Query Tool are:

> Table 8 - Query Tool Files

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Filename</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose/Explanation</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ReadMe.txt</strong></p>
</blockquote></td>
<td><blockquote>
<p>Includes any pertinent information not included in other documents or files (normally updates that could not be</p>
<p>included in other sources)</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PRCLogisticsTools.exe</strong></p>
</blockquote></td>
<td><blockquote>
<p>The compiled executable (program) file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PRCLogisticsTools.hlp</strong></p>
</blockquote></td>
<td><blockquote>
<p>The online help file</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>PRCLogisticsTools.cnt</strong></p>
</blockquote></td>
<td><blockquote>
<p>The online help “contents” file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>PRCLogisticsTools.gid</strong></p>
</blockquote></td>
<td><blockquote>
<p>The online help “index” file. This is the only file which can be safely deleted (the help system will rebuild it the next time it’s needed); under normal circumstances, however, there should not be any need to delete it.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>RoboEx32.dll</strong></p>
<p><strong>InetWH32.dll</strong></p>
</blockquote></td>
<td><blockquote>
<p>Dynamic link libraries needed for proper operation of the Help File.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Technical Information

![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/033.png)![](ifcap-version-5-1-logistics-data-query-tool-installation-guide/034.png)

### RPC Broker Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Other files may also be required to assist in setting up user workstations. The following applications should also be available in the C:\Program Files\VISTA\IFCAP\\ directory. If they are not, see 4.3.4 above for more information.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Filename</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose/Explanation</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>ServerList.exe</strong></p>
</blockquote></td>
<td><blockquote>
<p>The “Edit Broker Servers” program, needed to specify which servers are available to use in Query Tool</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>xwb1_1ws.exe</strong></p>
</blockquote></td>
<td><blockquote>
<p>Program needed to set up the RPC Broker Client on the workstation. <em>See</em></p>
<p><a href="http://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb1_1p40ig">http://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb1_1p40ig.</a></p>
<p>pdf.</p>
</blockquote></td>
</tr>
</tbody>
</table>