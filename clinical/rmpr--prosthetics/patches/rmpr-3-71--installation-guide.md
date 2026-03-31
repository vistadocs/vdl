---
title: RMPR*3*71 NPPD Detail Display (GUI) Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: NPPD Detail Display (GUI)
app_code: RMPR
app_name: Prosthetics
section: CLI
app_status: active
pkg_ns: RMPR
patch_ver: 3
patch_id: RMPR*3*71
group_key: "RMPR:RMPR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Patch RMPR\3\71 Installation Guide](#patch-rmpr371-installation-guide) ![](rmpr-3-71-nppd-detail-display-gui-installation-guide/001.png) PROSTHETICS NPPD DETAIL DISPLAYPATCH RMPR\3\71INSTALLATION GUIDE
audience: 
keywords: 
  - table
  - colgroup
  - style
  - width
  - tbody
  - blockquote
  - strong
  - class
  - installation
  - continued
page_count: 0
word_count: 2813
section_count: 2
table_count: 16
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_71ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Prothestics/rmpr_3_71ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=96"
---

## Table of Contents

  - [Patch RMPR\3\71 Installation Guide](#patch-rmpr371-installation-guide)
![](rmpr-3-71-nppd-detail-display-gui-installation-guide/001.png)
PROSTHETICS NPPD DETAIL DISPLAYPATCH RMPR\*3\*71INSTALLATION GUIDE

#### Version 3.0

January 2003
V*IST*A System Design and Development
Table of Contents
Patch RMPR\*3\*71 Installation Guide [1](#patch-rmpr371-installation-guide)
Client Installation [1](#client-installation)
Extract the file [4](#extract-the-file)
Install the NPPD File [7](#install-the-nppd-file)

## Patch RMPR\*3\*71 Installation Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Client Installation

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="introduction">Introduction</h5></td>
<td><blockquote>
<p>With Patch RMPR*3*71, Prosthetics offers the <strong>NPPD Detail Display</strong> feature, which is the first GUI windows-based functionality available to users. This <em><strong>Installation Guide</strong></em> will help IRM and users to download this patch.</p>
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
<td><h5 id="rpc-broker">RPC Broker </h5></td>
<td><blockquote>
<p>The assumption is made that the user’s PC has the required RPC Broker Client Workstation set up. If this is not the case, the user should first install this software. The installation is beyond the scope of this installation guide, but the RPC Broker files and installation instructions can be found on the VA’s RPC Broker web page. These files must be installed before running the <strong>NPPD Detail Display</strong> GUI application.</p>
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
<td><h5 id="hosts-file">HOSTS file</h5></td>
<td><blockquote>
<p>A link must be established between the client and the server via the PC’s Hosts file and the PC’s Windows Registry. The Hosts file (no extension) is in the following:</p>
<p>C:\Windows for Windows 95 or 98</p>
<p>C:\WinNt\System32\Drivers\Etc for Windows NT 4</p>
<p>If the Hosts file does not exist, it must be created. (There may be a hosts.sam sample file already in place.) Note that if you create the file with Notepad, Notepad automatically adds a .txt extension. To remove the extension, use Explorer to rename it, leaving off the .txt.</p>
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
<td><h5 id="steps">Steps</h5></td>
<td><blockquote>
<p>If the Hosts file already exists, do not delete anything. Follow these instructions for updating the Hosts file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>1</td>
<td><p>If the user needs to access only one <strong>NPPD Detail Display</strong> GUI server, and the ServerPort is 9200, then add a line to the Hosts file, as shown in the example (on the next page) using the IP address provided by the server administrator. (There must be at least one space between the address and the name. There can be no spaces in the name itself.)</p>
<p>Continue to the next page.</p></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="notepad-sample-hosts-file">Notepad – sample HOSTS file</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/002.png)</p>
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
<td><h5 id="steps-continued">Steps (continued)</h5></td>
<td><blockquote>
<p>Continue to follow these instructions for updating the Hosts file (if the Hosts file already exists.)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>2</td>
<td>If the user needs to access only <strong>one</strong> <strong>NPPD Detail Display</strong> GUI Server and the ServerPort is <strong><u>not</u></strong> 9200, then add one line to the Hosts file as shown in scenario 1 above, and run the ServerList utility described in scenario 3 below, or use the command line parameters shown in the next section.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>If the user needs to access multiple <strong>NPPD Detail Display</strong> GUI Servers and/or the ServerPort is NOT 9200, and the <strong>NPPD Detail Display</strong> GUI Server names to the Hosts file:</p>
<ul>
<li><p>152.111.222.333 BrokerServer1 (The names can be anything you<br />
like.)</p></li>
<li><p>152.111.222.444 BrokerServer2</p></li>
</ul></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="multiple-servers">Multiple servers</h5></td>
<td><blockquote>
<p>Then run the ServerList Utility, installed in the <strong>C:\Program Files\Vista\PROS</strong> file of the GUI install package.</p>
</blockquote>
<ul>
<li><p>The left windowpane of the ServerList utility shows those servers that have been set up as Host Servers in the HOSTS file.</p></li>
<li><p>The right windowpane shows those servers that have been set up as BrokerServers.</p></li>
</ul></td>
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
<td><h5 id="steps-1">Steps </h5></td>
<td><blockquote>
<p>Continue to follow these instructions for updating the Hosts file.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>To enable a BrokerServer, double-click on the name in the left window to move it to the right window, and then enter the corresponding ServerPort number.</p>
<p><strong>Note:</strong> The order of the names in the right list is the order they will be displayed in the drop-down box when starting the <strong>NPPD Detail Display</strong> GUI feature. If only one server is listed on the right, then you won’t see the drop down box – it will automatically select that server as the default).</p>
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
<p>A left-click in the “<strong>Del</strong>” column marks and un-marks server for deletion. See the following ServerList screen print for an example.</p>
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
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/003.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Extract the file

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
<td><h5 id="steps-2">Steps</h5></td>
<td><blockquote>
<p>To begin the install process and unzip the files, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                    |
|------|--------------------------------------------------------------------|
| Step | Action                                                             |
| 1    | From the Anonymous Directory, download the file RMPR_3_71.EXE. |
| 2    | Double click the RMPR_3_71.exe icon.                           |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="wrong-filename">Wrong filename</h5></td>
<td><blockquote>
<p>If the filename is <strong>RMPR_3_71.exe;1 (see first file in picture below)</strong> when you try to download it, then you <strong>must</strong> rename it to <strong>RMPR_3_71.exe</strong> so that the filename does not have an “<strong>;1</strong>” in it.</p>
<p><strong>Note:</strong> See next page for renaming instructions.</p>
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
<td><h5 id="wrong-filename-with-1-extension">Wrong filename with “;1” extension</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/004.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rename-the-file">Rename the file</h5></td>
<td><blockquote>
<p>To change the filename, right click on <strong>RMPR_3_71.exe;1</strong>, and select <strong>Rename.</strong> Then delete the <strong>“;1”</strong> from the filename. See picture below of correct filename.</p>
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
<td><h5 id="rename-option">Rename option</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/005.png)</p>
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
<td><h5 id="rmrp_3_71">RMRP_3_71</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/006.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="unzipping-files">Unzipping files</h5></td>
<td><blockquote>
<p>The file RMPR_3_71.EXE is a zip file that contains the “setup” files needed for the automated installation. The files will unzip to the C:\PROS folder for setup purposes. As an alternative to extracting these files to every client computer, IRM staff can unzip this file to a shared folder (directory) on a network server and then run the installation “SETUP.EXE” remotely.</p>
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
<td><h5 id="winzip-dialog-box">WinZip dialog box</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/007.png)</p>
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
<td><h5 id="steps-continued-1">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to unzip the files, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                           |
|------|-------------------------------------------------------------------------------------------|
| Step | Action                                                                                    |
| 3    | In the WinZip Self-Extractor dialog box, click the Unzip button (as shown above). |
| 4    | A successful message box displays when the unzip process has completed. (See below.)      |
| 5    | Click the OK button on the WinZip Self-Extractor confirmation box.                |
| 6    | The WinZip Self-Extractor dialog box continues to display (as shown above).           |
| 7    | Click the Close button.                                                               |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="successful-message-box">Successful message box</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/008.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Install the NPPD File

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="automatic-wizard">Automatic Wizard</h5></td>
<td><blockquote>
<p>Once you have extracted the files onto your c-drive, you can perform an installation using an automatic wizard that is provided for you. This feature has combined several steps to make installation easy.</p>
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
<td><h5 id="steps-3">Steps</h5></td>
<td><blockquote>
<p>To begin the installation, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                      |
|------|----------------------------------------------------------------------|
| Step | Action                                                               |
| 1    | Open the My Computer icon on your desktop by double clicking it. |
| 2    | Double click the C-drive in your Windows Explorer view.          |
| 3    | Double click the folder that contains the files: PROS.           |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="windows-explorer">Windows Explorer</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/009.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-2">Steps (continued)</h5></td>
<td><blockquote>
<p>To run the installation program, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Step | Action                                                                                             |
| 4    | Double click the Setup.exe file in the C\\PROS folder shown on your Windows Explorer view. |

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="windows-explorer-1">Windows Explorer</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/010.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-3">Steps (continued)</h5></td>
<td><blockquote>
<p>To run the wizard for the <strong>NPPD Detail Display</strong> installation, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                                 |
|------|-----------------------------------------------------------------------------------------------------------------|
| Step | Action                                                                                                          |
| 5    | Click the Next button on the first window of the Install Shield Wizard for the NPPD Detail Display. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="nppd-detail-display-setup">NPPD Detail Display Setup</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/011.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-4">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue the installation, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<tbody>
<tr class="odd">
<td>Step</td>
<td>Action</td>
</tr>
<tr class="even">
<td>6</td>
<td><p>Click the <strong>Yes</strong> button on the License Agreement if you agree to the terms of the license.</p>
<p><strong>Note:</strong> If you choose <strong>No</strong>, the setup will automatically close.</p></td>
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
<td><h5 id="license-agreement">License Agreement</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/012.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="recommendation">Recommendation</h5></td>
<td><blockquote>
<p>The destination folder <strong>“\Program Files\Vista\PROS”</strong> has been established by VA policy so as not to conflict with other VA programs. It is recommended that you do NOT change this portion of the path.</p>
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
<td><h5 id="steps-continued-5">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue the installation, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                                    |
|------|----------------------------------------------------------------------------------------------------|
| Step | Action                                                                                             |
| 7    | Click the Next button on the Destination Location dialog box.                              |
| 8    | Click OK on the confirmation box. Notice that it states that the PROS file folder was created. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="file-destination-location">File Destination Location</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/013.png)</p>
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
<td><h5 id="confirmation-message">Confirmation message</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/014.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-6">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue the installation, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                   |
|------|-------------------------------------------------------------------|
| Step | Action                                                            |
| 9    | Click the Next button on the Start Copy Files dialog box. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="start-copying-files">Start Copying Files</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/015.png)</p>
</blockquote></td>
</tr>
</tbody>
</table>

Continued on next page

, Continued

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="steps-continued-7">Steps (continued)</h5></td>
<td><blockquote>
<p>To continue to install the Prosthetics feature onto your desktop, follow these steps:</p>
</blockquote></td>
</tr>
</tbody>
</table>

|      |                                                                                             |
|------|---------------------------------------------------------------------------------------------|
| Step | Action                                                                                      |
| 10   | The Install Shield Wizard will be complete with this step. Click the Finish button. |

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="install-shield-wizard">Install Shield Wizard</h5></td>
<td><blockquote>
<p>![](rmpr-3-71-nppd-detail-display-gui-installation-guide/016.png)</p>
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
<td><h5 id="installation-complete">Installation Complete</h5></td>
<td><blockquote>
<p>The application is now installed on C:\Program Files\Vista\PROS. An icon has been placed on your desktop to run the application NPPD Detail Display. The application can also be run from <strong>Start</strong> <strong>Programs</strong> <strong>NPPD Detail Display</strong>.</p>
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
<td><h5 id="uninstall-procedures">Uninstall procedures</h5></td>
<td><blockquote>
<p>To uninstall the application, go to the <strong>Control Panel</strong> <strong>Add/Remove Programs</strong> option and select the <strong>NPPD Detail Display</strong> item. Click the <strong>REMOVE</strong> button and the program will automatically uninstall. To complete the full removal, the setup files will need to be deleted from the file location you selected.</p>
</blockquote></td>
</tr>
</tbody>
</table>