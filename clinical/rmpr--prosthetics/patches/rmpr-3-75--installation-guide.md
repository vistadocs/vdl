---
title: RMPR*3*75 Prosthetics VistA Suite (GUI) Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Prosthetics VistA Suite (GUI)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*75
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 1
description: "<table> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 81%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td><h5 id=\\"introduction\\">Introduction</h5></td> <td><blockquote> <p>With Patch RMPR375, Prosthetics offers the <strong>Create Lab Work Order (OWL)</strong> feature, which offers lab work or"
audience: 
keywords: 
  - blockquote
  - strong
  - table
  - style
  - colgroup
  - width
  - tbody
  - installation
  - prosthetics
  - vista
page_count: 0
word_count: 3890
section_count: 5
table_count: 7
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_75ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_75ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [Overview](#overview)
  - [Preinstallation](#preinstallation)
  - [## Client Installation](#client-installation)
  - [Post Installation](#post-installation)
![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/001.png)
Prosthetics VistA SuiteInstallation GuideVersion 3.0 (GUI Version)January 2005
for Patch RMPR\*3.0\*75
Health System Design and Development
Provider Systems
Revision History
|                                                |              |                                    |
|------------------------------------------------|--------------|------------------------------------|
| Description                                | Date     | Author                         |
| Prosthetics VistA Suite (GUI) V. 3.0 released. | January 2005 |                                    |
| RMPR\*3.0\*75 released                         | May 2007     | <span class="mark">REDACTED</span> |
|                                                |              |                                    |
|                                                |              |                                    |
|                                                |              |                                    |
|                                                |              |                                    |
|                                                |              |                                    |
Table of Contents
Overview [1](#overview)
Preinstallation [3](#preinstallation)
Uninstalling a Previous Version of the Prosthetics Suite [3](#uninstalling-a-previous-version-of-the-prosthetics-suite)
Installing the RPC Broker [4](#installing-the-rpc-broker)
Downloading the Installation File [5](#downloading-the-installation-file)
Extracting the Installation File [6](#extracting-the-installation-file)
Client Installation [7](#client-installation)
Installing the GUI Application [7](#installing-the-gui-application)
Post Installation [13](#post-installation)
Setting Up the Hosts File [13](#setting-up-the-hosts-file)
Running the Prosthetics VistA Suite [16](#running-the-prosthetics-vista-suite)
Uninstalling the Prosthetics VistA Suite [17](#uninstalling-the-prosthetics-vista-suite)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>With Patch RMPR*3*75, Prosthetics offers the <strong>Create Lab Work Order (OWL)</strong> feature, which offers lab work ordering functionality in a windows-based environment. This <em><strong>Prosthetics VistA Suite (GUI)</strong></em> <em><strong>Installation Guide</strong></em> will help IRM and users to download and install the GUI portion of the patch. See the patch description for the instructions for the VistA portion of the patch. The following is a list of documentation on the <a href="http://www.va.gov/vdl/">VistA Document Library (VDL)</a> for Prosthetics graphical user interface (GUI) applications::</p>
</blockquote>
<ul>
<li><blockquote>
<p>Delayed Order Report (DOR) (GUI) Installation Guide</p>
</blockquote></li>
<li><blockquote>
<p>Delayed Order Report (DOR) (GUI) User Manual</p>
</blockquote></li>
<li><blockquote>
<p>NPPD Detail Display (GUI) Installation Guide</p>
</blockquote></li>
<li><blockquote>
<p>Prosthetics VistA Suite (GUI) User Manual</p>
</blockquote></li>
<li><blockquote>
<p>Prosthetics VistA Suite (GUI) Installation Guide (i.e., the manual you are currently reading.)</p>
</blockquote></li>
</ul>
<ul>
<li><p>View Billing Information (GUI) User Manual</p></li>
</ul>
<blockquote>
<p><strong>Note:</strong> The Prosthetics Main Menu (GUI) User Manual is no longer a separate manual. It has been combined with the Prosthetics Application Suite User Manual (GUI).</p>
<p>The <strong>Prosthetics Main Menu</strong> window allows you to access all GUI applications for Prosthetics.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="important-note-to-irm">IMPORTANT NOTE to IRM</h5></td>
<td><blockquote>
<p>RMPR_3_75.EXE, the full VistA suite, is typically installed on each Prosthetic user’s computer. For sites which prefer their users to connect to the VistA Suite over the network, RMPR_3_75.EXE may be installed on a server that has a user environment set up.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Preinstallation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Uninstalling a Previous Version of the Prosthetics Suite

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="important-remove-previous-vista-prosthetics-suite-installations">IMPORTANT: Remove previous VistA Prosthetics Suite installations</h5></td>
<td><blockquote>
<p>You <strong>must</strong> first uninstall an existing VistA Prosthetics suite installation.</p>
<p>To do this, go to the <strong>Control Panel</strong> <strong>Add or Remove Programs</strong> option and select the Prosthetics VistA suite item. Click the <strong>Add/Remove</strong> button and follow the prompts to uninstall the Prosthetics suite.</p>
<p>This remainder of this section of the Installation Guide contains a fully-detailed workflow for uninstalling a previous Prosthetics suite. If you are installing the Prosthetics VistA Suite for the first time, or don’t require detailed uninstall instructions, you can skip to the next section—Installing the RPC Broker.</p>
<p>If you already have the RPC Broker installed, you don’t need to reinstall it. If that’s the case, you may skip to the following section—Downloading the Installation File.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="detailed-uninstall-workflow">Detailed uninstall workflow</h5></td>
<td><blockquote>
<p>This workflow is based on the Windows XP operating system (OS). If you are using a different OS, some screens and item names may vary.</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Click the Windows <strong>Start</strong> button.</p>
</blockquote></li>
<li><blockquote>
<p>Move your mouse pointer over <strong>Settings</strong> to expose <strong>Control Panel</strong> to expand its menu, then select <strong>Add or Remove Programs</strong>. The Add or Remove Programs window displays a list of currently installed programs.<br />
<br />
<strong>Note:</strong> Depending on your preferred Windows menu style, you may not see Settings. If that is the case, simply click Control Panel.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Prosthetics Vista Suite</strong> from the list. That will display the Add/Remove button.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Change/Remove</strong> button. A progress window displays for a few seconds while the system prepares to make changes.</p>
</blockquote></li>
<li><blockquote>
<p>A confirmation popup asks, “Do you want to completely remove the selected application and all of its components?” Click <strong>OK</strong> to proceed with the uninstall.</p>
</blockquote></li>
<li><blockquote>
<p>Another progress window displays for a few seconds, then the <strong>Maintenance Complete</strong> window displays. Click <strong>Finish</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Close the Add or Remove Programs window.</p>
</blockquote></li>
</ol>
<blockquote>
<p>The previous version of the Prosthetics VistA Suite is now uninstalled. Since you were already a Prosthetics VistA Suite user, you probably already have the RPC Broker installed. If that’s the case, you may skip to the following section—Downloading the Installation File. If not, continue with the next section to install the RPC Broker,</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Installing the RPC Broker

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rpc-broker">RPC Broker </h5></td>
<td><blockquote>
<p>The assumption is made that the user’s PC has the required RPC Broker Client Workstation set up. If this is not the case, the user should first install this software.</p>
<p>The installation is beyond the scope of this installation guide, but the RPC Broker files and installation instructions can be found on the VA’s RPC Broker web page: <mark>REDACTED</mark>.</p>
<p>These files must be installed before running the GUI application.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Downloading the Installation File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="anonymous-directory">Anonymous directory</h5></td>
<td><blockquote>
<p>The file for this patch can be obtained from the ANONYMOUS.SOFTWARE directory at one of the OI Field Offices. The preferred method is to FTP the file from DOWNLOAD.VISTA.MED.VA.GOV, which will transmit the file from the first available server.</p>
<p>Alternatively, you may elect to retrieve the file from a specific OI Field Office. The documentation can be read via the Adobe Acrobat Reader browser program. The .EXE file is binary file and must be transferred using binary file transfer tools.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="download-steps">Download steps</h5></td>
<td><blockquote>
<p>To begin the install process and unzip the files, follow these steps:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>From the ANONYMOUS.SOFTWARE Directory, download the file <strong>RMPR_3_75.EXE</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Make a note of the file location.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="warning-wrong-filename"><u>Warning</u>: Wrong filename</h5></td>
<td><blockquote>
<p><strong>Warning:</strong> If the filename of the file you download is <strong>RMPR_3_75.EXE;1</strong> then you <strong>must</strong> rename it to <strong>RMPR_3_75.EXE</strong> so that the filename does not have “<strong>;1</strong>” at the end of it.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><h5 id="section"></h5></td>
<td><blockquote>
<p>To change the filename, right click the <strong>RMPR_3_75.EXE;1</strong>, file and select the <strong>Rename</strong> option. Then delete the <strong>“;1”</strong> from the filename and press <strong>[ENTER]</strong>.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Extracting the Installation File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="default-location-of-extracted-files-is-cpros">Default location of extracted files is C:\PROS\</h5></td>
<td><blockquote>
<p>The file <strong>RMPR_3_75.EXE</strong> is a zip file that contains the setup files needed for the automated installation. For setup purposes, the files will unzip to the following folder:</p>
<p>C:\PROS\</p>
<p>As an alternative to extracting these files to every client computer, IRM staff can unzip this file to a shared folder (directory) on a network server and then run the installation “SETUP.EXE” remotely.</p>
<p><strong><u>Recommendation</u>:</strong> Do not change the file folder, as future patches will need to overwrite these files.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="unzip-steps">Unzip steps </h5></td>
<td><ol type="1">
<li><blockquote>
<p>Double click the installation file <strong>RMPR_3_75.EXE</strong>. The WinZip Self-Extractor dialog displays.</p>
</blockquote></li>
</ol>
<blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/002.png)</p>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Click the <strong>Unzip</strong> button (as shown above). A successful message displays when the unzip process has completed.</p>
</blockquote></li>
</ol>
<blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/003.png)</p>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>Click <strong>OK</strong> to close the confirmation popup.</p>
</blockquote></li>
<li><blockquote>
<p>The <strong>WinZip Self-Extractor</strong> dialog box continues to display (as shown above). Click the <strong>Close</strong> button.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

## ## Client Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Installing the GUI Application

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="automatic-wizard">Automatic Wizard</h5></td>
<td><blockquote>
<p>Once you have extracted the files onto your C: drive, you can perform an installation using the automatic wizard that is provided. This feature combines several steps to make installation easy.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="install-steps">Install steps </h5></td>
<td><blockquote>
<p>To begin the installation, follow these steps:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Double-click the <strong>My Computer</strong> icon on your desktop. The Windows Explorer view displays.</p>
</blockquote></li>
<li><blockquote>
<p>Double click the <strong>C:</strong> drive in your Windows Explorer view.</p>
</blockquote></li>
<li><blockquote>
<p>Double click the <strong>PROS</strong> folder to display the setup files.</p>
</blockquote></li>
<li><blockquote>
<p>Double click the <strong>Setup.exe</strong> file in the <strong>C:\PROS</strong> folder.</p>
</blockquote></li>
<li><blockquote>
<p>The <strong>Install Shield Wizard</strong> begins and displays the download process.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-2"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/004.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-3"></h5></td>
<td><ol start="6" type="1">
<li><blockquote>
<p>Click the <strong>Next</strong> button on the first window of the <strong>Install Shield Wizard</strong> for the GUI application.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-4"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/005.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-5"></h5></td>
<td><ol start="7" type="1">
<li><blockquote>
<p>Click the <strong>Yes</strong> button on the License Agreement if you agree to the terms of the license.<br />
<br />
<strong>Note:</strong> If you choose <strong>No</strong>, the setup will automatically close.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-6"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/006.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-7"></h5></td>
<td><ol start="8" type="1">
<li><blockquote>
<p>Click the <strong>Next</strong> button on the <strong>Choose Destination Location</strong> window.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Recommendation:</strong> The destination folder <strong>C:\Program Files\Vista\PROS</strong> has been established in accordance with VA policy so as not to conflict with other VA programs. It is recommended that you do NOT change this portion of the path.</p>
</blockquote>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-8"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/007.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-9"></h5></td>
<td></td>
</tr>
<tr class="even">
<td><h5 id="section-10"></h5></td>
<td></td>
</tr>
<tr class="odd">
<td><h5 id="section-11"></h5></td>
<td></td>
</tr>
<tr class="even">
<td><h5 id="section-12"></h5></td>
<td><ol start="9" type="1">
<li><blockquote>
<p>Click <strong>OK</strong> on the confirmation box. Notice that it states that the PROS folder was created.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-13"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/008.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-14"></h5></td>
<td><ol start="10" type="1">
<li><blockquote>
<p>Click the <strong>Next</strong> button on the <strong>Start Copying Files</strong> dialog box.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-15"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/009.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-16"></h5></td>
<td><ol start="11" type="1">
<li><blockquote>
<p>Click the <strong>Finish</strong> button on the <strong>InstallShield Wizard Complete</strong> window.</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-17"></h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/010.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="section-18"></h5></td>
<td><blockquote>
<p>Setup is almost complete. The final step of the installation is to set up your Hosts file. Proceed to the next section.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Post Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Setting Up the Hosts File 

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="hosts-file">HOSTS file</h5></td>
<td><blockquote>
<p>A link must be established between the client and the server via the PC’s Hosts file and the PC’s Windows Registry. The Windows 2000/XP Hosts file (no extension) is located in the following directory:</p>
<p>C:\WINDOWS\system32\drivers\etc</p>
<p>If the Hosts file does not exist, it must be created. (There may be a sample Hosts file named hosts.sam already in place.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="note">NOTE</h5></td>
<td><blockquote>
<p><strong>Note:</strong> If you create the file with Notepad, Notepad automatically adds a .txt extension.</p>
<p>To remove the extension, use Explorer to rename the file from Hosts.txt to Hosts</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="caution">CAUTION</h5></td>
<td><blockquote>
<p>If the Hosts file already exists, do not delete anything.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="sample-hosts-file-viewed-in-notepad">Sample HOSTS file viewed in Notepad</h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/011.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="simple-hosts-file-update">Simple Hosts file update</h5></td>
<td><blockquote>
<p><strong>If the user needs to access only one GUI server and the server port is 9200</strong>, then add a line to the Hosts file as shown in the example above using the IP address provided by the server administrator.</p>
<p><strong>Note:</strong> There must be at least one space between the address and the name. There can be no spaces in the name itself. After you’ve updated the Hosts file and saved it, make sure the file still does not have an extension. If it does, remove it.</p>
<p><strong>If the server port is not 9200 and/or if the user needs to access multiple GUI servers,</strong> then you must run the ServerList utility described below.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="hosts-file-update-using-the-serverlist-utility">Hosts file update using the ServerList utility</h5></td>
<td><blockquote>
<p>Follow these instructions for updating the Hosts file in conjunction with the ServerList utility.</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Add the GUI server IP addresses and names to the Hosts file:</p>
</blockquote>
<ul>
<li><p>BrokerServer1 (Use any names you like.)</p></li>
<li><blockquote>
<p>BrokerServer2</p>
</blockquote></li>
</ul></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Notes:</strong> There must be at least one space between the address and the name. There can be no spaces in the name itself.</p>
</blockquote>
<blockquote>
<p>After you’ve updated the Hosts file and saved it, make sure the file still does not have an extension. If it does, remove it.</p>
</blockquote>
</blockquote>
<ol start="2" type="1">
<li><blockquote>
<p>Run the ServerList Utility (ServerList.exe), which is installed in the following folder:</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p>C:\Program Files\Vista\PROS</p>
</blockquote>
<p>The left windowpane of the ServerList utility shows those servers that have been set up as Host Servers in the HOSTS file.</p>
<blockquote>
<p>The right windowpane shows those servers that have been set up as Broker servers.</p>
</blockquote>
</blockquote>
<ol start="3" type="1">
<li><blockquote>
<p>To enable a Broker server, double-click on the name in the left window to move it to the right window, and then enter the corresponding server port number.</p>
</blockquote></li>
</ol>
<blockquote>
<blockquote>
<p><strong>Note:</strong> The order of the names in the right list is the order they will be displayed in the drop-down box when starting the GUI feature. If only one server is listed on the right, then you won’t see the drop-down box – it will automatically select that server as the default).</p>
</blockquote>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="del-column">“Del” column</h5></td>
<td><blockquote>
<p>A left-click in the “<strong>Del</strong>” column marks and un-marks server for deletion. See the following ServerList screen for an example.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="serverlist">ServerList</h5></td>
<td><blockquote>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/012.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Running the Prosthetics VistA Suite

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="installation-complete">Installation Complete</h5></td>
<td><blockquote>
<p>The application is now installed in <strong>C:\Program Files\Vista\PROS</strong>. An icon named <strong>Prosthetics Vista Suite</strong> has been placed on your desktop. It looks like a medicine bag, as shown below.</p>
<p>![](rmpr-3-75-prosthetics-vista-suite-gui-installation-guide/013.png)</p>
<p>Double-click the icon to run the application. The application can also be run in the following way:</p>
<p><strong>Start All Programs Prosthetics Vista Suite</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Uninstalling the Prosthetics VistA Suite

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="uninstall-procedure">Uninstall procedure</h5></td>
<td><blockquote>
<p>To uninstall the application, do the following:</p>
</blockquote>
<ol type="1">
<li><blockquote>
<p>Click the Windows <strong>Start</strong> button.</p>
</blockquote></li>
<li><blockquote>
<p>Move your mouse pointer over <strong>Settings</strong> to expose <strong>Control Panel</strong> to expand its menu, then select <strong>Add or Remove Programs</strong>. The Add or Remove Programs window displays a list of currently installed programs.<br />
<br />
<strong>Note:</strong> Depending on your preferred Windows menu style, you may not see Settings. If that is the case, simply click Control Panel.</p>
</blockquote></li>
<li><blockquote>
<p>Click <strong>Prosthetics Vista Suite</strong> from the list. That will display the Change/Remove button.</p>
</blockquote></li>
<li><blockquote>
<p>Click the <strong>Change/Remove</strong> button. A progress window displays for a few seconds while the system prepares to make changes.</p>
</blockquote></li>
<li><blockquote>
<p>A confirmation popup asks, “Do you want to completely remove the selected application and all of its components?” Click <strong>OK</strong> to proceed with the uninstall.</p>
</blockquote></li>
<li><blockquote>
<p>Another progress window displays for a few seconds, then the <strong>Maintenance Complete</strong> window displays. Click <strong>Finish</strong>.</p>
</blockquote></li>
<li><blockquote>
<p>Close the <strong>Add or Remove Programs</strong> window.</p>
</blockquote></li>
<li><blockquote>
<p>To complete the full removal, the setup files will need to be deleted from the file location you selected (usually C:\PROS).</p>
</blockquote></li>
</ol></td>
</tr>
</tbody>
</table>