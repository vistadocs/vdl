---
title: Vitals Version 5 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: GMRV
app_name: Vitals/Measurements
section: CLI
app_status: active
pkg_ns: GMRV
patch_ver: 5
patch_id: GMRV*5
group_key: "GMRV:GMRV:5"
file_numbers: []
security_keys: []
menu_options: 0
description: - In the Package (#9.4) file, this application is known as Gen. Med. Rec. - Vitals. The package namespaces are GMRV and GMV. Version 5 is exporting only GMV namespaced code which provides a GUI interface. The existing roll’n’scroll options (i.e., GMRV namespace) still exist, but are not sent out wit
audience: 
keywords: 
  - blockquote
  - installation
  - class
  - vitals
  - mark
  - table
  - guide
  - server
  - style
  - width
page_count: 0
word_count: 2408
section_count: 7
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/vitl5_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vitals_Measurements/vitl5_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=107"
---

> ![](vitals-version-5-installation-guide/001.png)

VITALS/MEASUREMENTS INSTALLATION GUIDE

> Version 5.0

> October 2002

> Department of Veterans Affairs

> V*IST*A System Design & Development

> Revision History

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1/16/2002</td>
<td>5.1</td>
<td>Added Revision History</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>2/6/2002</td>
<td>5.2</td>
<td>Update install guide</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>2/13/2002</td>
<td>5.3</td>
<td><p>The following sections were updated: Overview</p>
<blockquote>
<p>Example - Vitals Server Installation Post Initialization Tasks</p>
<p>File Security</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/6/2002</td>
<td>5.4</td>
<td><p>The following sections were updated: Disk Storage</p>
<blockquote>
<p>Example - Vitals Server Installation</p>
<p>Post Installation Tasks</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/13/2002</td>
<td>5.5</td>
<td><p>The following sections were updated: Overview</p>
<blockquote>
<p>Example - Vitals Server Installation</p>
<p>Post Initialization Tasks</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/14/2002</td>
<td>5.6</td>
<td><p>Took out screen capture of setup screen in install shield example as instructed by</p>
<p>David.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>5/15/2002</td>
<td>5.7</td>
<td><p>Took out screen capture of self-extracting zip file, and changed Setup.exe to Vitals.exe as instructed by</p>
<p>David.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>5/21/2002</td>
<td>5.8</td>
<td><p>Added <mark>REDACTED</mark>changes to the Install</p>
<p>Guide.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>6/21/2002</td>
<td>5.9</td>
<td><p>Added <mark>REDACTED</mark>changes to the Install</p>
<p>Guide.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>9/10/2002</td>
<td>6.0</td>
<td><p>Added <mark>REDACTED</mark>changes to the Install</p>
<p>Guide for T31.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/19/2002</td>
<td>6.1</td>
<td>Changed release date to October 2002.</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>10/17/2002</td>
<td>6.2</td>
<td><p>Added <mark>REDACTED</mark>changes to the Install</p>
<p>Guide for T32.</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>10/23/2002</td>
<td>6.3</td>
<td><p>Added <mark>REDACTED</mark> changes to the Install</p>
<p>Guide for T32.</p></td>
<td><mark>REDACTED</mark></td>
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

# Installation Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Installation Guide](#installation-guide)
  - [Overview](#overview)
  - [Vitals/Measurements V. 5.0 Installation (M Server)](#vitalsmeasurements-v-50-installation-m-server)
    - [Installation Instructions:](#installation-instructions)
    - [M Server Installation – Example Screen Listing](#m-server-installation-example-screen-listing)
  - [Vitals/Measurements V. 5.0 Installation (Client Installation)](#vitalsmeasurements-v-50-installation-client-installation)
  - [Post Installation Tasks on the M Server](#post-installation-tasks-on-the-m-server)
  - [Customizing the Client Installation](#customizing-the-client-installation)
  - [Server Based Installation](#server-based-installation)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- In the Package (#9.4) file, this application is known as Gen. Med. Rec. - Vitals. The package namespaces are GMRV and GMV. Version 5 is exporting only GMV namespaced code which provides a GUI interface. The existing roll’n’scroll options (i.e., GMRV namespace) still exist, but are not sent out with Version 5. The roll’n’scroll and GUI versions can both be used.

> Contents of this package can be found in the V*IST*A Documentation Library (VDL).

> The Vitals/Measurements package is comprised of two parts, the M Server and the Client workstation. This guide addresses both the installation of the KIDS build on the M Server and the executable on the workstation.

> The post installation routine GMVXPST deletes 4 obsolete data dictionary fields and any data that may remain. It does not send a mail message when done. The post installation should take no longer than 10 minutes to complete. It also updates the Parameters (#8989.5) file with the current version of executable files and the weblink for the Vitals/Measurements package.

- Requirements for M Server installation:

> The M Server (disk) storage requirements for this package are:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 55%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><u>Globals</u></th>
<th><blockquote>
<p><u>Type of Data</u></p>
</blockquote></th>
<th><u>Size</u></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DDs</td>
<td><blockquote>
<p>Data Dictionaries</p>
</blockquote></td>
<td>40 k</td>
</tr>
<tr class="even">
<td>GMR</td>
<td><blockquote>
<p>Patient data for the Text Generator, Vitals/Measurements,</p>
<p>Intake and Output, Adverse Reaction Tracking and Consult/ Request Tracking Modules</p>
</blockquote></td>
<td><p>25-75 k/</p>
<p>patient</p></td>
</tr>
<tr class="odd">
<td>GMRD</td>
<td><blockquote>
<p>Static data for the Text Generator, Vitals/Measurements and Intake and Output Modules</p>
</blockquote></td>
<td>10 k depending on the global efficiency</td>
</tr>
</tbody>
</table>

> Installation Guide

> The following packages and patches must be installed and fully patched for the installation environment for Version 5.0 of the Vitals/Measurements package on the M Server:

1.  VA FileMan V. 22 or greater
2.  Kernel V. 8.0 or greater
3.  Kernel Toolkit V. 7.3 or greater
4.  Kernel RPC Broker V. 1.1 or greater
5.  PIMS V. 5.3 or greater
6.  Intake and Output V. 4.0
7.  Health Summary V. 2.7 or greater
8.  Nursing V. 4.0 or greater
- Requirements for V*IST*A Client installation: The client (disk) storage requirements are:

> <u>Type of Data</u> <u>Size</u>

> Application (user) 1356.5 k Application (manager) 811.5 k

> Help Files (user) 460 k Help Files (manager) 175.678 k

> The following describes the installation environment for the Vitals/Measurements package on the V*IST*A client workstation:

1.  Workstations must be running under Windows NT (V4 or later) or Windows 2000.
2.  The workstation must be connected to the local area network.
3.  Twelve (12) megabytes of available disc space is needed to run the program.
4.  RPC Broker Workstation can be installed (Optional).

<span id="_bookmark1" class="anchor"></span>Installation Guide

## Vitals/Measurements V. 5.0 Installation (M Server)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The server installation must be done before the client installation.Pre-installation instructions:

1.  Coordinate the installation with the CAC, package ADPAC and IRMS.
2.  If not already on system, create, place, and set the journaling option for the globals ^GMR and ^GMRD on the volume set.

### Installation Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> INSTALLATION FILES:

> The following software and documentation files are released as parts of Vitals 5.0

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 49%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>File Name</th>
<th><blockquote>
<p>Contents</p>
</blockquote></th>
<th>Retrieval Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VITL5.KID</td>
<td><blockquote>
<p>Vitals 5.0 M code</p>
</blockquote></td>
<td>ASCII</td>
</tr>
<tr class="even">
<td><blockquote>
<p>NUR*4*37</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>GMRY*4*5</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VITL5_IG.PDF</td>
<td><blockquote>
<p>Vitals 5.0 Installation Guide</p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>VITL5_RN.PDF</td>
<td><blockquote>
<p>Vitals 5.0 Release Notes</p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>VITL5_TM.PDF</td>
<td><blockquote>
<p>Vitals 5.0 Technical</p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>VITL5_UM.PDF</td>
<td><blockquote>
<p>Vitals 5.0 User Manual</p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="even">
<td>VITL5.EXE</td>
<td><blockquote>
<p>Vitals 5.0 Executable</p>
</blockquote></td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>VITL5_SRC.xxx</td>
<td><blockquote>
<p>Vitals 5.0 GUI Source Code</p>
</blockquote></td>
<td>Binary</td>
</tr>
</tbody>
</table>

> Note: The NUR\*4\*37 KIDS build contains one routine, NURAPI. The GMRY\*4\*5 KIDS build contains only one routine, GMRYAPI. Both routines contain utilities used by the Vitals/Measurements package.

> The files listed above may be obtained via FTP. The preferred method is to FTP the files from: <span class="mark">REDACTED</span> This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| CIO FIELD OFFICE                   |     | FTP ADDRESS                        |     | DIRECTORY                          |
|------------------------------------|-----|------------------------------------|-----|------------------------------------|
| <span class="mark">REDACTED</span> |     | <span class="mark">REDACTED</span> |     | <span class="mark">REDACTED</span> |

> Installation Guide

> Users should copy the VITL5.KID file to an area where it can be loaded into the M account by the KIDS utility. Also, the VITL5.EXE file should be copied into a sharable directory where it can be reached for the client installation.

> INSTALLATION:

1.  Users may remain on the system at the time of installation. The software should be installed when use of the Vitals software is minimal.
2.  On the V*IST*A system, set the variables DUZ and DUZ(0) by executing the command D

> ^XUP. Verify DUZ(0) = @.

3.  Mapping is not recommended for any Vitals routines.
4.  Use the Kernel Installation & Distribution System menu \[XPD MAIN\] and select Installation and then Load a Distribution. When prompted to enter a host file, enter VITL5.kid.
5.  From this menu, run the option Verify Checksums in Transport global to verify that all routines have the correct checksum.
6.  Use the KIDS installation menu option \[XPD MAIN\] and select Installation and then Install Package(s) and select the package GEN. MED. REC. – VITALS. Refer to the following Installation example in this manual for additional information.

<span id="_bookmark2" class="anchor"></span>Installation Guide

### M Server Installation – Example Screen Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \> D ^XUP

> Setting up programmer environment Terminal Type set to: C-VT100

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> KIDS Installation ...

> Select Kernel Installation & Distribution System Option: INSTALLation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation

> Option:

> 1 Load a Distribution

> Enter a Host File: VITL5.KID

> KIDS Distribution saved on Feb 06, 2002@11:03:08 Comment: VITALS v5, NUR\*4\*37 and GMRY\*4\*5

> This Distribution contains Transport Globals for the following Package(s): GEN. MED. REC. - VITALS 5.0

> NUR\*4.0\*37 GMRY\*4.0\*5

> Distribution OK!

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Build GEN. MED. REC. - VITALS 5.0 has an Enviromental Check Routine Want to RUN the Environment Check Routine? YES// \<RET\>

> GEN. MED. REC. - VITALS 5.0

> Will first run the Environment Check Routine, GMVXENV

> NUR\*4.0\*37 GMRY\*4.0\*5

> Use INSTALL NAME: GEN. MED. REC. - VITALS 5.0 to install this Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Installation Guide

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: GEN. MED. REC. - VITALS 5.0 Loaded from

> Distribution 2/6/02@11:11:36

> =\> VITALS v5, NUR\*4\*37 and GMRY\*4\*5 ;Created on Feb 06, 2002@11:03:08

> This Distribution was loaded on Feb 06, 2002@11:11:36 with header of VITALS v5, NUR\*4\*37 and GMRY\*4\*5 ;Created on Feb 06, 2002@11:03:08 It consisted of the following Install(s):

> GEN. MED. REC. - VITALS 5.0 NUR\*4.0\*37 GMRY\*4.0\*5

> Checking Install for Package GEN. MED. REC. - VITALS 5.0 Will first run the Environment Check Routine, GMVXENV

> Install Questions for GEN. MED. REC. - VITALS 5.0 Incoming Files:

> 120.5 GMRV VITAL MEASUREMENT

> Note: You already have the 'GMRV VITAL MEASUREMENT' File.

51. GMRV VITAL TYPE (including data) Note: You already have the 'GMRV VITAL TYPE' File. Data will NOT be added.
52. GMRV VITAL QUALIFIER (including data) Note: You already have the 'GMRV VITAL QUALIFIER' File. Data will NOT be added.
53. GMRV VITAL CATEGORY (including data) Note: You already have the 'GMRV VITAL CATEGORY' File. Data will NOT be added.

> 120.57 GMRV VITALS PARAMETERS (including data) Note: You already have the 'GMRV VITALS PARAMETERS' File. Data will NOT be added.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

> NOTE: The decision to rebuild menus is left up to each facility, ‘No’ was used for this example. Please follow whatever policy your facility uses for rebuilding menus when installing software.

> Checking Install for Package NUR\*4.0\*37 Install Questions for NUR\*4.0\*37

> Checking Install for Package GMRY\*4.0\*5 Install Questions for GMRY\*4.0\*5

Installation Guide

> Want KIDS to INHIBIT LOGONs during the install? YES// NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// \<RET\> TELNET

> Install Started for GEN. MED. REC. - VITALS 5.0 : Feb 06, 2002@11:12:20

> Build Distribution Date: Feb 06, 2002 Installing Routines:

> Feb 06, 2002@11:12:27

> Installing Data Dictionaries:

> Feb 06, 2002@11:12:30

> Installing Data:

> Feb 06, 2002@11:12:30

> Installing PACKAGE COMPONENTS: Installing SECURITY KEY Installing REMOTE PROCEDURE Installing OPTION

> Feb 06, 2002@11:12:34

> Installing PARAMETER DEFINITION

> Feb 06, 2002@11:12:36

> Running Post-Install Routine: ^GMVXPST Updating system parameters.

> Will queue data cleanup as a background job. Task \#: 330472

> Updating Routine file... Updating KIDS files...

> GEN. MED. REC. - VITALS 5.0 Installed.

> Feb 06, 2002@11:12:38

> Not a production UCI

> NO Install Message sent

> Install Started for NUR\*4.0\*37 :

> Feb 06, 2002@11:12:38

> Build Distribution Date: Feb 06, 2002 Installing Routines:

> Feb 06, 2002@11:12:38

> Installation Guide

> Updating Routine file... Updating KIDS files...

> NUR\*4.0\*37 Installed.

> Feb 06, 2002@11:12:39

> Not a production UCI

> NO Install Message sent

> GMRY\*4.0\*5

> Install Started for GMRY\*4.0\*5 :

> Feb 06, 2002@11:12:39

> Build Distribution Date: Feb 06, 2002 Installing Routines:

> Feb 06, 2002@11:12:39

> Updating Routine file... Updating KIDS files...

> GMRY\*4.0\*5 Installed.

> Feb 06, 2002@11:12:39

> Not a production UCI

> NO Install Message sent

> +------------------------------------------------------------+ 100% ¦ 25 50 75 ¦ Complete +------------------------------------------------------------+

> Install Completed

<span id="_bookmark3" class="anchor"></span>Installation Guide

## Vitals/Measurements V. 5.0 Installation (Client Installation)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Vitals application utilizes the RPC Broker connection to the V*IST*A server for operation. Before installing the application, insure that the workstation has connectivity to the required server via the RPC Broker. For help in setting up the RPC Broker on the workstation refer to the Kernel RPC Broker documentation.

> Run VITL5.exe from the sharable directory where you placed it, and follow the installation steps that will be presented to the user.

![](vitals-version-5-installation-guide/002.png)

> Fig. 1

1.  Your first screen is a welcome screen. Press the Next button to begin the installation process of Vitals/Measurements (Fig. 1).
2.  You will then see an Extracting Files window and then another Install Shield window.

> Installation Guide

3.  When the extracting process completes, you will see the following welcome screen (Fig. 2):

![](vitals-version-5-installation-guide/003.png)

> Fig. 2

Installation Guide

![](vitals-version-5-installation-guide/004.png)

> Fig. 3

4.  Select the location (i.e., Destination Folder in Fig. 3) on the client where the application is to be installed. By default the installation will be placed in the system directory of:

> C:\Program Files\Vista\Vitals\\

> It is recommended that you use this default as it is in compliance with the GUI SACC guidelines for the location of GUI application installations. The application will operate correctly if placed elsewhere on the client workstation but this is not recommended. Use Browse button to select another destination folder or directory.

> Installation Guide

![](vitals-version-5-installation-guide/005.png)

> Fig. 4

5.  Select the setup you prefer by clicking on it and then clicking the Next button (Fig. 4).

> Clinician only installs Vitals, Vitals Manager is not installed.

> Manager installs both the Vitals and Vitals Manager applications.

> Clinical Application Coordinators, package coordinators, and Information Resource Management Service (IRMS) staff should get the Manager setup.

> Clinical staff should get the Clinician setup.

Installation Guide

6.  The Install wizard will now start copying files upon verification of the settings (Fig. 5).

![](vitals-version-5-installation-guide/006.png)

> Fig. 5

> Installation Guide

![](vitals-version-5-installation-guide/007.png)

> Fig. 6

7.  Once all steps are completed the installation will begin and show the progress as it installs (Fig. 6). If the installation files are located on the client PC, the install screen should complete in less than one minute. Server and network connectivity for installations over the network may cause the installation time to increase.

Installation Guide

![](vitals-version-5-installation-guide/008.png)

> Fig. 7

8.  Upon completion of the installation this screen will be presented to the user and the installation can be finalized by pressing the Finish button (Fig. 7).

> <span id="_bookmark4" class="anchor"></span>Installation Guide

## Post Installation Tasks on the M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  There is one security key in this application, it is GMV MANAGER. This new key controls access to the Vitals Manager module. This key should be assigned to the package coordinator.
2.  There are no routines to be mapped in the Vitals/Measurements software as of this release.
3.  All users should be assigned the GMV V/M GUI option.
4.  Verify that the following globals are journaled and place them in the UCI translation table for each CPU: ^GMR and ^GMRD.
5.  Verify that the file security is correct for the following files:

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th>NUMBER</th>
<th>NAME</th>
<th></th>
<th><blockquote>
<p>GLOBAL NAME</p>
</blockquote></th>
<th><blockquote>
<p>DD ACC</p>
</blockquote></th>
<th><blockquote>
<p>RD ACC</p>
</blockquote></th>
<th><blockquote>
<p>WR ACC</p>
</blockquote></th>
<th><blockquote>
<p>DEL ACC</p>
</blockquote></th>
<th><blockquote>
<p>LAY AUD</p>
<p>ACC ACC</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>120.5</td>
<td>GMRV</td>
<td>VITAL MEASUREMENT</td>
<td><blockquote>
<p>^GMR(120.5,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>120.51</td>
<td>GMRV</td>
<td>VITAL TYPE</td>
<td><blockquote>
<p>^GMRD(120.51,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>120.52</td>
<td>GMRV</td>
<td>VITAL QUALIFIER</td>
<td><blockquote>
<p>^GMRD(120.52,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="even">
<td>120.53</td>
<td>GMRV</td>
<td>VITAL CATEGORY</td>
<td><blockquote>
<p>^GMRD(120.53,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>120.57</td>
<td>GMRV</td>
<td>VITALS PARAMETERS</td>
<td><blockquote>
<p>^GMRD(120.57,</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
<td><blockquote>
<p>@</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_bookmark5" class="anchor"></span>Installation Guide

## Customizing the Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The client installation by default installs and builds the icons and program folder items without any command line switches. Vitals/Measurements utilizes the ServerList utility of the RPC Broker for selecting a server to connect to if it is configured on the client workstation.

> Instructions for configuration and utilization of the ServerList utility can be found in the RPC Broker documentation located on the VDL. If the ServerList utility has not been configured on the client, the applications by default will attempt to connect to the server identified in the users HOSTS file as BROKERSERVER on Listener Port 9200. Adding command line parameters to the shortcuts as shown below by right clicking the appropriate Vitals/Measurements application icon and selecting the Properties menu item can easily override these parameters.

![](vitals-version-5-installation-guide/009.png)

> Fig. 8

> The above (Fig. 8) is a standard properties view of the Vitals icon as displayed when right clicking the icon. Select the Shortcut tab to proceed with customization.

> Installation Guide

![](vitals-version-5-installation-guide/010.png)

> Fig. 9

> This example (Fig. 9) will attempt to connect the application to the server identified in your HOSTS file as *yourserver* and will use listener port 9200.

> Vitals/Measurements V. 5.0 command line parameters available from the command prompt or within Windows shortcut definitions are:

> Vitals.exe \[/server=*servername*\] \[/port=*listenerport*\]

> \[/tempdir=*temporarydirectory*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\] \[/brokertimeout=*seconds*\]

> VitalsManager.exe \[/server=*servername*\] \[/port=*listenerport*\] \[/helpdir=*helpdirectory*\] \[/debug={on\|off}\] \[/brokertimeout=*seconds*\]

Installation Guide

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 54%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Switches</strong></th>
<th><strong>Description</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>/server</td>
<td><p>Specifies an alternate server to connect to. The server must be defined in the clients hosts. file.</p>
<p>Default Hosts. file locations: NT 4.0/W2K =</p>
<p>c:\winnt\system32\drivers\etc\hosts. Windows 9x = c:\windows\hosts.</p>
<p>Default = BROKERSERVER</p></td>
<td>/server=vista</td>
</tr>
<tr class="even">
<td>/port</td>
<td><p>Specifies an alternate listener port on the selected server. This is the TCP/IP port that the broker is running on V<em>IST</em>A server.</p>
<p>Default = 9200</p></td>
<td>/port=9200</td>
</tr>
<tr class="odd">
<td>/tempdir</td>
<td><p>Location accessible to the client workstation and current user for storage of temporary scratch files.</p>
<p>Default = <em>application_directory</em>\temp</p></td>
<td>/tempdir=C:\temp</td>
</tr>
<tr class="even">
<td>/helpdir</td>
<td><p>Location of the Vitals/Measurements windows help files.</p>
<p>Default = <em>application_directory</em>\help</p></td>
<td>/helpdir=C: \help</td>
</tr>
<tr class="odd">
<td>/debug</td>
<td><p>Set the debug mode for both the RPC Broker and the Vitals/Measurements application.</p>
<p>Default = Off.</p></td>
<td>/debug=On</td>
</tr>
<tr class="even">
<td>/brokertimeout</td>
<td><p>Overrides the timeout for the RPC Broker when executing a Remote Procedure.</p>
<p>Default = 30.</p></td>
<td>/brokertimeout=60</td>
</tr>
<tr class="odd">
<td>/nonsharedbroker</td>
<td><p>Force application to use nonshared version of RPC</p>
<p>Broker</p></td>
<td>/nonsharedbroker</td>
</tr>
</tbody>
</table>

> <span id="_bookmark6" class="anchor"></span>Installation Guide

## Server Based Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Vitals/Measurements package may be installed on a shared server and accessed via shortcuts on the user’s desktop to minimize the impact of patching and installation. To do this simply perform a complete install of the application on a workstation and verify that the installation is working. Next, copy all files and sub directories from the target directory (default C:\Program Files\vista\Vitals\\’) to the shared server. On each individual workstation all that needs to be done is the creation of a shortcut pointing to the Vitals.exe and/or VitalsManager.exe applications on the server. These shortcuts can be customized as shown above in the Customizing the Client Installation section. This allows for updates to occur on the single copy of the application on the server and does not require IRM going to each individual workstation to apply updates. As the VA moves towards utilizing Microsoft SMS, Vitals/Measurements will be updated to support this method of client installation.

> List of all files that need to be copied to the server share for server based installations: C:\Program Files\vista\Vitals\Vitals.exe

> C:\Program Files\vista\Vitals\VitalsManager.exe C:\Program Files\vista\Vitals\Help\Vitals.hlp C:\Program Files\vista\Vitals\Help\Vitals.cnt C:\Program Files\vista\Vitals\Help\VitalsManager.hlp C:\Program Files\vista\Vitals\Help\VitalsManager.cnt C:\Program Files\vista\Vitals\Help\Roboex32.dll