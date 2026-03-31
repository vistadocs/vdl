---
title: MAG*3*201 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: archive
pkg_ns: MAG
patch_ver: 3
patch_id: MAG*3*201
group_key: "MAG:MAG:3"
file_numbers: []
security_keys: []
menu_options: 0
description: > This document explains how to install the VistA Imaging Exchange (VIX) service. Please review the install checklist in Appendix A prior to starting the install and reference throughout.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - installation
  - table
  - contents
  - class
  - guide
  - mark
  - server
  - service
  - blockquote
  - verify
page_count: 0
word_count: 7618
section_count: 22
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: February 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag3_0p201_vix_installation_guide_20190201_16.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys_Archive/mag3_0p201_vix_installation_guide_20190201_16.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=413"
---

---
title: |
  Image Viewer Version 3.0

  Deployment, Installation, Back-out, and Rollback Plan
---

![](mag-3-201-installation-guide/001.png)

> Version 28.0 MAG\*3.0\*201

## Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Office of Information and Technology (OI&T)

> Property of the US Government

> MAG\*3.0\*201 Deployment, Installation, Back-out, and Rollback Plan February 2019 i

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development group.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Product Development Department of Veterans Affairs Internet: <span class="mark">REDACTED</span>

> VA intranet: <span class="mark">REDACTED</span>

> Revision History

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Rev</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Oct 14 2011</td>
<td>1</td>
<td>Created for MAG*3.0*104. WPR complete Aug 31; labeled for release Oct 14. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>May 07 2012</td>
<td>2</td>
<td>Updated for MAG*3.0*122. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 25 2013</td>
<td>3</td>
<td>Updated for MAG*3.0*034/116/118, MAG*3.0*119, MAG*3.0*127, MAG*3.0*129. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>September 09</p>
<p>2013</p></td>
<td>4</td>
<td>Updated for MAG*3.0*130, <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>May 10 2016</td>
<td>5</td>
<td>Updated for MAG*3.0*162, <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>February 14</p>
<p>2017</p></td>
<td>6</td>
<td>Updated for MAG 3.0*170, <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>March 24</p>
<p>2017</p></td>
<td>7</td>
<td>Date updates<mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>April 27 2017</td>
<td>8</td>
<td>Updated port information <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>July 05 2017</td>
<td>9</td>
<td>MAG*3.0*170 Installer Updates <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>July 26 2017</td>
<td>10</td>
<td>MAG*3.0*170 Updates <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>August 01</p>
<p>2017</p></td>
<td>11</td>
<td>MAG*3.0*177 Updates <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>October 03</p>
<p>2017</p></td>
<td>12</td>
<td>MAG*3.0*177 Updates <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>October 25</p>
<p>2017</p></td>
<td>13</td>
<td>MAG*3.0*185 Updates. <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>November 14</p>
<p>2017</p></td>
<td>14</td>
<td>Incorporated comments from reviewers regarding MAG*3.0*185. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><p>December 5</p>
<p>2017</p></td>
<td>15</td>
<td>Updated MAG*3.0*185 build numbers. <mark>REDACTED</mark>.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Rev</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>January 11</p>
<p>2018</p></td>
<td>16</td>
<td>Additional MAG*3.0*185 updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="even">
<td><p>January 25</p>
<p>2018</p></td>
<td>17</td>
<td>Additional MAG*3.0*185 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="odd">
<td><p>January 26</p>
<p>2018</p></td>
<td>18</td>
<td>Updated for MAG*3.0*197. <mark>REDACTED</mark> .</td>
</tr>
<tr class="even">
<td><p>March 13</p>
<p>2018</p></td>
<td>19</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="odd">
<td>May 25 2018</td>
<td>20</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="even">
<td>June 21 2018</td>
<td>21</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="odd">
<td>July 6 2018</td>
<td>22</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="even">
<td>July 26 2018</td>
<td>23</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="odd">
<td><p>August 14</p>
<p>2018</p></td>
<td>24</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="even">
<td><p>August 21</p>
<p>2018</p></td>
<td>25</td>
<td>Additional MAG*3.0*197 Updates. <mark>REDACTED</mark> .</td>
</tr>
<tr class="odd">
<td><p>September 27</p>
<p>2018</p></td>
<td>26</td>
<td>Updated for MAG*3.0*197 <mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><p>November 19</p>
<p>2018</p></td>
<td>27</td>
<td>Updated for MAG*3.0*201</td>
</tr>
<tr class="odd">
<td><p>February 1</p>
<p>2019</p></td>
<td>28</td>
<td>Updated for MAG*3.0 201 T9</td>
</tr>
</tbody>
</table>

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Department of Veterans Affairs](#department-of-veterans-affairs)
- [Contents](#contents)
- [Introduction](#introduction)
  - [Intended Audience](#intended-audience)
  - [Terms of Use](#terms-of-use)
  - [Document Conventions](#document-conventions)
  - [Related Information](#related-information)
- [Installing a New VIX](#installing-a-new-vix)
  - [Preparing for a New VIX Installation](#preparing-for-a-new-vix-installation)
  - [New VIX Installation – Standalone Server](#new-vix-installation-standalone-server)
    - [Choose Start \| All Programs \| VistA Imaging Programs \| VIX Installation Service Wizard.](#choose-start-all-programs-vista-imaging-programs-vix-installation-service-wizard)
    - [Next.](#next)
    - [Create.](#create)
  - [Verifying Installation Is Complete](#verifying-installation-is-complete)
  - [Activating a New VIX](#activating-a-new-vix)
    - [To register the VIX](#to-register-the-vix)
- [Updating an Existing VIX](#updating-an-existing-vix)
  - [Preparing for a VIX Update](#preparing-for-a-vix-update)
    - [RESTART the VIX server before proceeding (User MUST restart the server after uninstalling SQL software).](#restart-the-vix-server-before-proceeding-user-must-restart-the-server-after-uninstalling-sql-software)
  - [Performing a VIX Update – Standalone Server](#performing-a-vix-update-standalone-server)
  - [In the Specify the Release of Information (ROI) Configuration, do the following:](#in-the-specify-the-release-of-information-roi-configuration-do-the-following)
- [Post-installation](#post-installation)
  - [McAfee Exclusions](#mcafee-exclusions)
  - [Verifying VIX Operations](#verifying-vix-operations)
  - [Access to http://\<FQDN\>:8080/Vix/secure/VixLog.jsp](#access-to-httpfqdn8080vixsecurevixlogjsp)
  - [Using the VIX Installation Wizard to Reconfigure the VIX](#using-the-vix-installation-wizard-to-reconfigure-the-vix)
- [Troubleshooting](#troubleshooting)
  - [Resuming an Interrupted VIX Installation](#resuming-an-interrupted-vix-installation)
    - [Click Start \| All Programs \| VistA Imaging Programs \| VIX Installation Wizard.](#click-start-all-programs-vista-imaging-programs-vix-installation-wizard)
  - [VIX Support](#vix-support)
- [Back Out/Uninstall](#back-outuninstall)
  - [Back Out/Uninstall Scenarios](#back-outuninstall-scenarios)
    - [Choose Start \| All Programs \| VistA Imaging Programs \| VIX Installation Service Wizard.](#choose-start-all-programs-vista-imaging-programs-vix-installation-service-wizard-1)
  - [Uninstalling the VIX](#uninstalling-the-vix)
    - [Uninstall a program.](#uninstall-a-program)
- [Appendix A: VIX Install Checklist](#appendix-a-vix-install-checklist)
  - [VIX Install Checklist](#vix-install-checklist)
MAG\*3.0\*201 Deployment, Installation, Back-out, and Rollback Plan

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document explains how to install the VistA Imaging Exchange (VIX) service. Please review the install checklist in Appendix A prior to starting the install and reference throughout.

## Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>This document is intended for VA staff responsible for managing a local VIX.</u>

> <u>This document presumes a working knowledge of the VistA environment, VistA Imaging</u> <u>components and workflow, and Windows administration.</u>

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VIX is a component of VistA Imaging and is regulated as a medical device by the Food and Drug Administration (FDA). Use of the VIX is subject to the following provisions:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](mag-3-201-installation-guide/002.png)</p>
</blockquote></th>
<th><blockquote>
<p>The FDA classifies VistA Imaging, and the VIX (as a component of VistA Imaging) as a medical device. Unauthorized modifications to VistA Imaging, including the VIX, such as the installation of unapproved software, will adulterate the medical device. The use of an adulterated medical device violates US federal law (21CFR820).</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](mag-3-201-installation-guide/003.png)</p>
</blockquote></td>
<td><blockquote>
<p>Because software distribution/inventory management tools can install inappropriate or unapproved software without a local administrator’s knowledge, sites must exclude the VIX server from such systems.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Document Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This document uses the following conventions:

- Controls, options, and button names are shown in Bold.
- A vertical bar is used to separate successive menu choices. For example: “Click

> File \| Open” means: “Click the File menu; then click the Open option.”

- Keyboard key names are shown in bold and in brackets.
- Sample output is shown in monospace.
- Important or required information is shown in a Note.
- ![](mag-3-201-installation-guide/004.png)Critical information is indicated by:

> Introduction

## Related Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In addition to this manual, the following document contains information about the VIX:

- [<u>VistA Image Exchange (VIX) Viewer Administrator’s Guide</u>](https://www.va.gov/vdl/application.asp?appid=105)

# Installing a New VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains how to implement a new VIX. The installation checklist in Appendix A, VIX Update Checklist, summarizes the process.

> Tip: If you are updating an existing VIX, see the [*Updating an Existing VIX*](#updating-an-existing-vix) section.

## Preparing for a New VIX Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Preparing to install a new VIX involves:

- Acquiring Installation Files
  - MAG3_0P201_VIX_Setup.msi and SQLEXPRESS_X64- 14_0_1000_169.ZIP found in the VIXSqlInstaller folder should be copied to a temporary folder on the desktop. (Download from SFTP site SOFTWARE folder if required)
  - If MAG 3.0\*197 VIX has been installed then the SQLexpress .zip file should have already been installed and came with SQL 2017. If not, remove any old SQL files from add/remove programs before proceeding with the install.
  - Note: please make sure you had scheduled a down-time of VIX service, it may take 1-2 hours to complete.
- Selecting and validating the server where the VIX will be installed
- Getting VIX component licenses
- Getting a VIX security certificate
- Port Setting
- Registry Update
- Tomcat User Permissions

> Specifics are covered in the following sections.

> <span id="_bookmark7" class="anchor"></span>Setting up VistA

> You must install the compatible KIDS package on the VistA system before installing the VIX server software. For information about how to install the KIDS package, see the patch description of the patch you are installing.

- If you are implementing a VIX for the first time, the MAG VIX ADMIN key, introduced in Patch MAG\*3.0\*83, must be assigned to the VistA accounts of administrators who need access to the VIX transaction log.
- While it is not required, it is recommended that sites run the MagDexter and MagKat utilities provided in patch MAG\*3.0\*98. Doing so populates DICOM series information for radiology exams acquired before the release of MAG\*3.0\*50. See the [*<u>VistA Imaging Storage Utilities Manual</u>*](https://www.va.gov/vdl/application.asp?appid=105) for details.

> <span id="_bookmark8" class="anchor"></span>Selecting and Validating the VIX Server

> The server where the VIX is installed must meet the FDA, hardware, and operating system/environmental requirements specified in the following sections.

> FDA Requirements

> The VIX is a component of VistA Imaging and is therefore regulated as a medical device by the Food and Drug Administration (FDA). Use of the VIX is subject to the terms of use listed in the introduction.

> Hardware Requirements

> Minimum VIX hardware requirements:

- Installation must be done on a 64bit OS machine.
- <u>The VIX servers will run on a minimum configuration of 2 CPUs, 4 gigabytes of RAM, and 200 gigabytes of disk space. However, during previous field testing, VIX performance was found to be less than optimal with image retrieval taking several minutes. Because of the slow performance with the minimum configuration, the following specifications are strongly recommended. If using minimum configurations, see Figure 2 below.</u>
- Strongly Recommended

o 4 CPUs and 8 gigabytes of RAM

- A dedicated local drive for the VIX cache
  - Strongly Recommended

> o 500 gigabytes of disk space

- A 1 gigabit Ethernet connection will need to be available for use by the VIX.

> ![](mag-3-201-installation-guide/005.png)

> *Figure 1: STRONGLY RECOMMENDED VIX Settings*

> ![](mag-3-201-installation-guide/006.png)

> Port Requirements

> *Figure 2: MINIMUM VIX Settings*

> On the server where the VIX is installed, verify that ports 343, 443, 8080, 8442, and 8443 are accessible to VA wide area network IP addresses (10.x.x.x).

> Operating System and Environment Requirements

> The VIX can run on:

- Minimum: Windows Server 2012 R2
- If you are installing on Windows Server 2012 R2
  - Verify that .Net 3.5 is enabled. It must be enabled for the VIX install.
  - .Net 4.5 framework should be installed on your server. If it isn’t installed, the installer will fail. To discover if you have the feature installed it should be present in *“Control Panel\Programs\Programs and Features”* as

> *“Microsoft .NET Framework 4.5.x”*.

- To remedy download and install the .Net 4.5 framework. (for convenience, a copy is placed on the FTP site)

> <span id="_bookmark9" class="anchor"></span>Getting VIX Component Licenses

> Two toolkits used by the VIX require third-party licenses.

> Laurel Bridge DCF Toolkit

> The Laurel Bridge DICOM Connectivity Framework (DCF) toolkit is a third-party toolkit used by the VIX to convert images to and from DICOM format.

> The VA has purchased an enterprise-wide license for this toolkit. To request site-specific serial numbers for this license, do the following:

1.  From the server where the VIX is installed, attempt to access the Laurel Bridge activation code server at <span class="mark">REDACTED</span>. (A login page will display if you can access the site.)

> ![](mag-3-201-installation-guide/007.png)If you cannot this access this site, enter a ticket and indicate that your site ACL (access control list) needs to be modified to access <span class="mark">REDACTED</span>.

2.  Contact the [<span class="mark">REDACTED</span>](mailto:VHAVILBLicenses@va.gov) mail group. They will provide a request form and instructions for completing the form.

> The serial number information provided will ultimately be used to generate an activation code (this is done during the VIX installation process). The activation code allows the Laurel Bridge DCF toolkit to be installed and used.

> The Laurel Bridge activation code is linked to the hardware of the server where the toolkit is installed. If you have to replace the licensed server, email the contacts listed previously to arrange to get the serial number(s) transferred as well.

> Aware JPEG2000 Toolkit License

> The Aware JPEG2000 toolkit is a third-party toolkit used for DICOM-to-JPEG2000 image conversion by the VIX.

> Sites that implement the VIX must purchase a one-time permanent license for the latest version of the Aware JPEG2000 toolkit from Aware for each server where the VIX is used

> IMPORTANT: Do not install the Aware JPEG2000 toolkit before you run the VIX installer. The VIX installer installs the version of the Aware JPEG2000 toolkit with which the VIX has been tested. If you install the Aware JPEG2000 toolkit before running the VIX installer, this will interfere with the installation process.

> <span id="_bookmark10" class="anchor"></span>Getting a VIX Security Certificate

> Each server that hosts the VIX must be issued a security certificate. To get security certificates, send an e-mail to [<span class="mark">REDACTED</span>](mailto:VHAVIVIXSETUP@VA.GOV) and include the following information:

- Fully Qualified Domain Name (FQDN) of the VIX server name
- Contact information for the primary and backup administrators of the VIX.

> Requests will typically be processed within five business days. After the request has been processed, the security certificate (one per server) will be securely transmitted to the requesting site POC for install on the site VIX.

> Each security certificate received will need to be copied to the local server where the VIX software is installed. The VIX installation wizard will prompt you for this certificate during the installation process.

> <span id="_bookmark11" class="anchor"></span>Java Version

> Before beginning the install, validate the specific patch description document for the current version of Java. If the server has a different version of Java than the required version specified in patch description, please uninstall the application.

> <span id="_bookmark12" class="anchor"></span>Port Setting

> Before beginning the install, the port range needs to be set. Follow the steps below: This step is for enabling MUSE which is not currently supported in JLV (future capability).

1.  Start \| Search CMD \| Open Command Prompt
2.  Run the following command: NetSh INT IPV4 SET DynamicPort TCP Start=1025 num=64511
3.  Verify the command successfully went through by running the following command: NetSh INT IPV4 Show DynamicPort TCP
4.  If step 2 was successful, results from step 3 should look like:

> Protocol tcp Dynamic Port Range

> Start Port: 1025 Number of Ports: 64511

5.  If results do not look like this, repeat step 2 to ensure there are no typing errors.

> <span id="_bookmark13" class="anchor"></span>Registry Update

> Before beginning the install, the client TCP/IP socket connection timeout value must be adjusted to be between 30 and 240.

1.  <span id="_bookmark14" class="anchor"></span>Start \| Search regedit \| Open Registry Editor
2.  Browse to the following key in the registry and select: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters
3.  Search for the following registry value: TcpTimedWaitDelay.

> If this value is not there, click on the Edit menu, click New, DWORD Value, and then add “TcpTimedWaitDelay” to reduce the length of time that a connection stays in the TIME_WAIT state when the connection is being closed. While a connection is in the TIME_WAIT state, the socket pair cannot be reused:

4.  Right click on the “TcpTimedWaitDelay” registry value and click “’Modify”. Then click “Decimal” and ensure the value is between 30 and 240.
5.  Close Registry Editor.

> <span id="_bookmark15" class="anchor"></span>Tomcat User Permissions

> Due to the VA group policy restriction or rules, there is an issue found while the VIX installer wizard is setting file system access rules - i.e. error denying

> access to apachetomcat account to c:\\..

> If it occurs, please check/verify the Access control of VIX service account \[apachetomcat\] for the following folders, must have the Modify & Write access rights (Allow access must be checked) -

- C:\Program Files\Apache Software Foundation\Tomcat 8.0\\
- C:\Program Files\java\Jre...
- C:\DCF_Run Time_x64
- C:\Vixconfig

> Right-click on the Folder, select 'Properties' - 'Security' - 'Edit'

> Otherwise, the Tomcat8 or VIX service(s) may experience some start-up, or slowness issues.

![](mag-3-201-installation-guide/008.png)

> ![](mag-3-201-installation-guide/009.png)

## New VIX Installation – Standalone Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the following steps to install a VIX on a standalone server for the first time. Installation should take less than 30 minutes if all preparation steps in previous sections are complete.

> Note Only perform the steps in this section if you are installing the VIX on a single server.

> <span id="_bookmark17" class="anchor"></span>Preparing Passwords, Activating Components, and Staging Files

> Before starting the VIX installation process on a standalone server, do the following:

> 1\. Verify that .NET 3.5 features and .NET 4.5 features are enabled. If Windows needs to download files, accept.

> ![](mag-3-201-installation-guide/010.png)

2.  Prepare a password to be used for the Apache Tomcat administrator account that will be created as part of the VIX installation process.
    - This account will be rarely used; it only needs to be secured properly.
    - The password is case-sensitive and only alphanumeric characters are allowed.
3.  Prepare a password for the Windows account that will be created as part of the VIX installation process.
    - This Windows account, which will be named “apachetomcat” when it is created by the VIX installer, is used to run the VIX in the Tomcat environment. This account is limited to only the functions it needs to run the VIX.
    - The password is case sensitive, must contain at least eight characters, and must contain at least one capital letter and one number.
4.  Set up a service account in VistA for ROI periodic processing with the MAG DICOM VISA secondary menu option and the OR CPRS GUI CHART secondary menu option. The service account may be the same service account as the one the DICOM Gateway and the HDIG use. The credentials are required for the VIX to process ROI disclosure requests periodically, in the background and to purge completed requests.
5.  Determine the email address or addresses for notification about invalid ROI periodic processing credentials. The VIX will send an email notification to the email address or addresses, if the ROI periodic processing credentials are invalid or have expired.

> You must specify this address when you install the VIX. You can set up a new email account for this purpose or use an existing one.

6.  Copy the VIX security certificate to the primary drive (usually the C drive) of the server where the VIX will be installed.
7.  To minimize downtime and speed up the P201 VIX installation, stop the following VIX services first: (if these are already present on new VIX server).

> For Server 2012 R2 (Server Manager – Tools – Component Services – Services (Local), or Task Manager – Services – Open Services)

- Apache Tomcat
- SQL Server (SQLEXPRESS), SQL Server CEIP (SQLEXPRESS), SQL Server VSS Writer
- Listener Tool
- VIX Render Service
- VIX Viewer Service

> Always use the Window ‘Task Manager’ to monitor the processing tasks as needed.

> Standalone Server Installation

> VIX installation involves running two processes back-to-back. The first short process installs the VIX Installation Wizard. The second, longer process involves using the VIX Installation Wizard to install the actual VIX.

> Note: These steps presume that you have already obtained a serial number for the Laurel Bridge DCF toolkit. These steps also presume the VIX can access the Laurel Bridge license server via the internet.

> To install the VIX on a standalone server

1.  Use an administrator-level account to log on to the standalone server where the VIX will be installed.
2.  Copy the latest VIX installer (MAG3_0P201_VIX_Setup.msi) and the VIXSqlInstaller folder SQLEXPRESS_X64-14_0_1000_169.ZIP) to a temporary folder on the desktop.
3.  Do the following to prepare the VIX Installation Wizard:
    1.  Double-click the VIX set-up MAG3_0P\<number\>\_VIX_Setup.msi file.
1.  When the Welcome page displays, click Next.
2.  When the Confirm Installation page displays, click Next.
3.  When the Installation Complete screen displays, click Close.

### Choose Start \| All Programs \| VistA Imaging Programs \| VIX Installation Service Wizard.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  Run selected program as administrator.

![](mag-3-201-installation-guide/011.png)

5.  When the Welcome page for the VIX installation wizard displays, click Next.
6.  In the Site Number field of the Specify the VA site... page, enter the STATION NUMBER (field (#99) in the INSTITUTION file (#4)) of your site. Then, click Lookup Server Addresses.
7.  Verify that the site-related information retrieved by the lookup is correct. Then, click

### Next.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Note: The VIX server hostname will be blank and the port number will be 0; these values are populated automatically once the VIX is registered with the VistA site service.

8.  When the Install the VIX Prerequisites page displays, verify that the icons for the first two items on the page are ![](mag-3-201-installation-guide/012.png) .
- \<account\> has Administrator role – This line will indicate if an administrative account is being used. If not, cancel the installation and restart it using a Windows administrator account.
- Current operating system – This line will indicate if the proper operating system is present. If a non-supported operating system is identified, the installation cannot continue.
9.  On the same page, check the line that indicates the state of the Java Runtime environment. If ![](mag-3-201-installation-guide/013.png) is shown, do the following:
    1.  Click Install.
    2.  Wait until the status icon the Java Runtime Environment changes to ![](mag-3-201-installation-guide/014.png) . (This install of Java will take longer than previous versions and may take several minutes to complete)
10. On the same page, check the line that indicates the state of the Apache Tomcat installation. If ![](mag-3-201-installation-guide/015.png) is shown, do the following:
    1.  Click Install.
    2.  In the dialog box that displays, enter and confirm the Apache Tomcat password that you prepared as described in [<u>Preparing Passwords, Activating Components,</u> <u>and Staging Files</u>](#_bookmark17) previously. Then, click OK.
    3.  Wait until the status icon for Apache Tomcat changes to ![](mag-3-201-installation-guide/016.png) . (This install of Tomcat will take longer than previous versions and may take several minutes to complete)
11. On the same page, check the line that indicates the state of the Laurel Bridge toolkit. If ![](mag-3-201-installation-guide/017.png) is shown, do the following:
    1.  Click the Install button next to the Laurel Bridge item. After a brief delay, the Activate DCF License window will open.

> Tip: The Network Activation tab will be selected automatically, and about half of the boxes in the window will be pre-populated.

2.  Enter all of the following information in the Network Activation tab:

> Note: The Activate button will be disabled if any of the following boxes are left blank.

- Product Serial Number – the new Laurel Bridge DCF serial number (include dashes).
- Site – the name of your site.
- CPUs – the number of CPUs on the server hosting the VIX.
- Contact name and Contact email – the administrator of your local VistA Imaging system.
3.  Near the bottom of the window, click Activate. After a brief delay, the Status

> box will display a green “Success” message.

4.  Click Exit with success. The Activate DCF License window will close and the updated Laurel Bridge toolkit will be installed (installation will only take a second or two).
12. On the same page, check the line that indicates the state of the service account. If ![](mag-3-201-installation-guide/018.png) is shown, do the following:
    1.  Click Create.
    2.  In the dialog box that displays, enter the Windows service account password that you prepared [<u>Preparing Passwords, Activating Components, and Staging Files</u>](#_bookmark17) previously. Then, click OK.
    3.  Wait until the status icon for the service account changes to ![](mag-3-201-installation-guide/019.png) .
13. On the same page, check the line that indicates the state of VIX security certificate. If ![](mag-3-201-installation-guide/020.png) is shown, do the following:
    1.  Click Install.
    2.  In the dialog box that displays, click Select.
    3.  Specify the location of the security certificate setup file received from the national VistA Imaging team. Then, click OK.
14. Check the line that indicates VIX/Viewer Render Services. If ![](mag-3-201-installation-guide/021.png) is shown, do the following.
    1.  Click Install

![](mag-3-201-installation-guide/022.png)

2.  Click Configure Viewer/Render

![](mag-3-201-installation-guide/023.png)![](mag-3-201-installation-guide/024.png)

3.  Verify the following settings:
1)  Verify the viewer port is set to 343.
2)  Verify Site Service host name is set to localhost.
3)  Verify Site Service port is set to 8080.
4)  Verify VIX Service host name is set to localhost.
5)  Verify instance name is .\\ SQLEXPRESS
    1.  Edit image cache directory drive to the dedicated VIX cache drive. (For example, "E:\VIXRenderCache")
    2.  If setting values were modified click the Save Configuration button in the top right corner.
    3.  Click OK
    4.  If prompted to install the SQL server, click OK and select the SQLEXPRESS_X64-14_0_1000_169.ZIP file from the “VIXSqlInstaller” folder in the temporary folder on the desktop. (Depending on your system, this step may take up to twenty minutes)

![](mag-3-201-installation-guide/025.png)

![](mag-3-201-installation-guide/026.png)

15. In the Install the VIX Prerequisites page, confirm that all the icons are ![](mag-3-201-installation-guide/027.png) . Then, click Next.
16. In the Specify the location page, select the drive where you want the VIX configuration files to reside. Then, click Create.
- In most cases, you should use the same drive for the VIX configuration files and for the VIX cache.
17. In the same page, select the drive where the VIX cache will be located. Then, click

### Create.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

18. Click Next.
- Select the “C:\\ drive for VixConfig folder and the appropriate VIXCache drive for your site (E: is shown in the example below). Click each Create button to create the folders.

![](mag-3-201-installation-guide/028.png)

- Click Next.
- In the Specify the Release of Information (ROI) Configuration, do the following:
  - Specify the access and verify codes for the account with the ROI periodic processing credentials. The VIX uses this account for periodic processing of ROI disclosure requests. The account must be valid VistA credentials with the DICOM VISA \[MAG DICOM VISA\] secondary menu option and the CPRSChart version

> 1.0.31.116 \[OR CPRS GUI CHART\] secondary menu option. The credentials can be the credentials of the same service account that the DICOM Gateway and the HDIG use.

- Specify the email address that gets notifications for invalid ROI periodic processing credentials. The VIX sends an email notification to the address or addresses specified in this field if the ROI periodic processing credentials are expired or invalid. You can enter several addresses, separated by a comma.

> ![](mag-3-201-installation-guide/029.png)

- Click Validate.

> The VIX installation program checks the information. If it detects an error, it displays a tooltip with information about the error. When it validates the configuration, Next becomes available.

- In the Configure Local DoD connection page, do one of the following:
  - If your site has no local network connection to a DoD facility, click Next (this will be the case at most VA sites)
  - If your site has a local network connection to a DoD facility, enter connection information for the DoD’s PACS Integrator server. After entering the connection information, click Validate to test the connection. Then, click Next.

> ![](mag-3-201-installation-guide/030.png)

- On the Install the VIX page, click Install. (The information in this page is saved in C:\Program Files (x86)\VistA\Imaging\VixInstaller for future reference or troubleshooting.) This will start the installation process. It will also start the Tomcat and Viewer/Render services.

> ![](mag-3-201-installation-guide/031.png)

> ![](mag-3-201-installation-guide/032.png)

- When installation is complete, click Finish to exit the wizard.
- The VIX will start automatically, but cannot be used until it is activated and registered with the VistA Site Service. See the next section for details.

## Verifying Installation Is Complete

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After you have run the VIX Installation Wizard, verify that your installation is complete. Follow these steps:

1.  Go to the VIX homepage: http://\<FQDN of VIX server\>:8080/
2.  The current version is listed in the format XX.XXX.X.X. The first two digits represent Version 3.0 of the VistA Imaging system and do not change. The next three

> digits are the number of the latest patch that has affected the VIX. This patch number should match the number of the VIX component you have most recently installed.

![](mag-3-201-installation-guide/033.png)

3.  ![](mag-3-201-installation-guide/034.png)Verify VIX viewer and VIX render services are running.
4.  Verify the listener tool is running.

![](mag-3-201-installation-guide/035.png)

5.  Verify that you have 10 Hydra IX and 10 Hydra VistA Worker threads running:

![](mag-3-201-installation-guide/036.png)

## Activating a New VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the VIX is installed, it will be inactive until it is registered with the VistA Site Service. Clinical Display workstations and VistARad workstations use the site service to determine if local and remote VIX servers are available.

> After the VIX is registered in the site service, the VIX will begin to be actively used, both by clinicians at your site as well as by remote VA sites for access to locally stored images.

> Note: Do not register the VIX with the site service until after it is installed. Registering the VIX before it is installed will cause errors and timeout issues for Clinical Display users.

### To register the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Gather the following information:

> Primary contact name, phone, and email:

> Backup contact name, phone, and email:

> Site name:

> STATION NUMBER (field \#99) from INSTITUTION file (#4):

> Network Name defined for Imaging Resources group:

2.  Enter a National ticket to Clin 3 for site service update.
    - Paste the lines in the preceding step into the ticket.
    - Include “Add VIX server to Site Service database”
3.  You will be notified, typically within five business days, when the site service registration is complete.
4.  See [*<u>Verifying VIX Operations</u>*](#verifying-vix-operations)

# Updating an Existing VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains how to update an existing VIX server. An installation checklist that summarizes this process can be found in [<u>Appendix A</u>](#appendix-a-vix-install-checklist), VIX Update Checklist.

## Preparing for a VIX Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Preparing for a VIX update involves:

- Acquiring Installation Files
  - MAG3_0P201_VIX_Setup.msi and SQLEXPRESS_X64-14_0_1000_169.ZIP found in the VIXSqlInstaller folder should be copied to a temporary folder on the desktop.
  - Copy the MAG3_0P185_VIX_Setup.msi (or P177) for the backup plan if it is not already on the same VIX server.
  - Note: please ensure down time has been scheduled to install the VIX service. The installation may take 1-2 hours to complete.
- Verify the MAG\*3.0\*201 VistA KIDs package has been installed.
- Schedule 1 – 2 hours for the downtime and notify users of the impact of the VIX update.
- Tip: Aware licenses (used for DICOM-to-JPEG2000 conversion on the VIX) established for older VIX systems will automatically carry over to new VIX systems.
- Tip: VIX-specific account passwords and security key assignments established for older VIX systems will automatically carry over to new VIX systems.
- Port Setting
- Registry Update
- Uninstall Prior Version of SQL (If older than current patch version)
- Stop VIX Services (Apache Tomcat, VIXViewer, and VIXRender)
- Check Tomcat Permissions (Ensure the Apache Tomcat account is in the local users group. If it does not exist, add it.)

> Hardware Requirements

> Minimum VIX hardware requirements:

- Installation must be done on a 64bit OS machine.
- The VIX servers will run on a minimum configuration of 2 CPUs, 4 gigabytes of RAM, and 200 gigabytes of disk space. However, during previous field testing, VIX performance was found to be less than optimal with image retrieval taking several minutes. Because of the slow performance with the minimum configuration, the following specifications are strongly recommended. If using minimum configurations, see Figure 2 below.
- Strongly Recommended

o 4 CPUs and 8 gigabytes of RAM

- A dedicated local drive for the VIX cache
  - Strongly Recommended

> o 500 gigabytes of disk space

- A 1 gigabit Ethernet connection will need to be available for use by the VIX.

![](mag-3-201-installation-guide/037.png)

> *Figure 3: STRONGLY RECOMMENDED VIX Settings*

> ![](mag-3-201-installation-guide/038.png)

> *Figure 4: MINIMUM VIX Settings*

> <span id="_bookmark22" class="anchor"></span>VistA Software Dependencies

> The VIX server software requires that a compatible Imaging KIDS package be installed on VistA. For details about the compatible KIDS package and installing it, see the patch description of the specific patch.

> <span id="_bookmark23" class="anchor"></span>Scheduling Downtime and Impact of a VIX Update

> You will need to schedule downtime with appropriate personnel for the duration of the VIX installation.

> Note: If a VIX is installed on a standalone (dedicated) server, the DICOM image acquisition is not impacted and can continue.

> While the VIX server is being updated, VIX assisted functions will not be available. The following table summarizes how a VIX outage will affect clinicians:

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Clinical Group</strong></th>
<th><strong>Impact</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Local Clinical Display users</td>
<td><p>DoD images will not be accessible for the duration of the VIX shutdown.</p>
<p>Remote VA images may be temporarily inaccessible. Clinical Display will attempt to revert to pre-VIX remote image views, but users may have to disconnect from and reconnect to remote sites, or in some cases, restart Clinical Display.</p>
<p>Clinicians may notice longer retrieval times for remote images for the duration of the VIX shutdown.</p>
<p>After the VIX is restarted, restart Clinical Display to make sure that Clinical Display is no longer using pre-VIX remote image views for remote sites.</p></td>
</tr>
<tr class="even">
<td>Local VistARad users</td>
<td>Remote exam data and monitored exam lists will not be available. For additional information, refer to the documentation for VistARad.</td>
</tr>
<tr class="odd">
<td>Remote VA or DoD clinicians requesting your site’s images</td>
<td><p>Remote clinicians may experience transitory application errors if the VIX is shut down while it is in the middle of processing a request; the clinician may have to repeat the request.</p>
<p>Remote VA clinicians issuing new requests may notice longer retrieval times for the duration of the VIX shutdown.</p>
<p>Remote DoD clinicians will not be able to retrieve locally stored images for the duration of the VIX shutdown.</p></td>
</tr>
<tr class="even">
<td>Local DICOM Importer users</td>
<td>The DICOM importer client will be unable to log into VistA and process imports for the duration that the VIX is down.</td>
</tr>
<tr class="odd">
<td>VIX image viewer/JLV users</td>
<td>Clinical users of JLV will not be able to access images or artifacts using the VIX image viewer.</td>
</tr>
</tbody>
</table>

> <span id="_bookmark24" class="anchor"></span>Java Version

> Before beginning the install, validate the specific patch description document for the current version of Java. If the server has a different version of Java than the required version specified in patch description, please uninstall the application.

> For example: P201 is using Java 8 Update: 1.80_171

> ![](mag-3-201-installation-guide/039.png)

> <span id="_bookmark25" class="anchor"></span>Port Setting

> Before beginning the install, the port range needs to be set. Follow the steps below:

1.  Start \| Search CMD \| Open Command Prompt
2.  Run the following command: NetSh INT IPV4 SET DynamicPort TCP Start=1025 num=64511
3.  Verify the command successfully went through by running the following command: NetSh INT IPV4 Show DynamicPort TCP
4.  If step 2 was successful, results from step 3 should look like:

> Protocol tcp Dynamic Port Range

> Start Port: 1025 Number of Ports: 64511

5.  If results do not look like this, repeat step 2 to ensure there are no typing errors.
    - This step is for enabling MUSE which is not currently supported in JLV (future capability).

> <span id="_bookmark26" class="anchor"></span>Registry Update

> Before beginning the install, the client TCP/IP socket connection timeout value must be adjusted to be between 30 and 240.

1.  Start \| Search regedit \| Open Registry Editor
2.  Browse to the following key in the registry and select: HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters
3.  Search for the following registry value: TcpTimedWaitDelay.

> If this value is not there, click on the Edit menu, click New, DWORD Value, and then add “TcpTimedWaitDelay” to reduce the length of time that a connection stays in the TIME_WAIT state when the connection is being closed. While a connection is in the TIME_WAIT state, the socket pair cannot be reused:

4.  Right click on the “TcpTimedWaitDelay” registry value and click “’Modify”. Then click “Decimal” and ensure the value is between 30 and 240.
5.  Close Registry Editor.

> <span id="_bookmark27" class="anchor"></span>Uninstall Prior Version of SQL (If older than current patch version)

1.  Stop Apachetomcat Service (if already running).
2.  Uninstall all or any old MS-SQL programs (Control Panel – Program – Program and Feature – Uninstall)
3.  Uninstall previous versions of Java.
4.  Remove prior Tomcat software other than Tomcat 8.0 (i.e.: 6.0)
5.  Remove/Delete the folder C:\Program Files\Microsoft SQL Server (include data files if it exists)

### RESTART the VIX server before proceeding (User MUST restart the server after uninstalling SQL software).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For example:

> ![](mag-3-201-installation-guide/040.png)

> <span id="_bookmark28" class="anchor"></span>Stop VIX Services (Apache Tomcat, VIX Viewer, and VIXRender) before P201 VIX upgrade

> To speed up the installation process, please stop the following services:

> For Server 2012 R2 (Server Manager – Tools – Component Services – Services (Local), or Task Manager – Services – Open Services)

- Apache Tomcat
- Listener Tool
- VIX Render
- VIX Viewer

![](mag-3-201-installation-guide/041.png)

- Always use the ‘Task Manager’ Window to monitor the processing tasks as needed.

> For example: ‘Details’ tab of Task Manager shows all running services, e.g.: Hydra.VistA.Worker for VIX Viewer, Hydra.IX.Worker for VIX Render, …etc. After stopping the service, they will be off the service details Running list.

![](mag-3-201-installation-guide/042.png)

> <span id="_bookmark29" class="anchor"></span>Check Tomcat Permissions (Ensure the Apache Tomcat account is in the local users group. If it does not exist, add it.)

> Due to the VA group policy restriction or rules, there may be an issue found while the VIX installer wizard is setting file system access rules - i.e. error denying

> access to apachetomcat account to c:\\ (Ensure the Apache Tomcat account is in the

> local users group. If it does not exist, add it.)

> If this occurs, please check/verify the Access control of VIX service account \[apachetomcat\] for the following folders, must have the Modify & Write access (Allow access must be checked) -

- C:\Program Files\Apache Software Foundation\Tomcat 8.0\\
- C:\Program Files\java\Jre1.8.0_171
- C:\DCF_Run Time_x64 (Check advanced special permissions in the C:\DCF_runtime x64\\ folder with “delete subfolder and file”)
- C:\Vixconfig

> Right-click on the Folder, select 'Properties' - 'Security' - 'Edit'

## Performing a VIX Update – Standalone Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use the following steps to update a VIX on a standalone server.

> Note: These steps presume that you have already obtained a new Laurel Bridge DCF toolkit serial number. These steps also presume the VIX can access the Laurel Bridge license server via the internet.

1.  Use an administrator-level account to log on to the standalone server where the VIX will be installed.
2.  Copy the VIX installation files (MAG3_0P201_VIX_Setup.msi and SQLEXPRESS_X64-14_0_1000_169.ZIP (if SQL 2017 is not already present on your VIX) found in the VIXSqlInstaller folder to a local folder on the server.
3.  Go into Control Panel/Programs/Programs and Features and remove prior VIX Service Installation Wizard.
4.  To Install the VIX Installation Wizard, perform the following steps:
    1.  Double-click the VIX installation file.
    2.  When the Welcome page displays, click Next.
    3.  When the Confirm Installation page displays, click Next.
    4.  When the Installation Complete screen displays, click Close.
5.  Choose Start \| All Programs \| VistA Imaging Programs \| VIX Installation Service Wizard. (Right-click and run as administrator)
6.  Run selected program as administrator.

![](mag-3-201-installation-guide/043.png)

7.  When the Welcome page displays, click Next. Then, when you are prompted to do so, uninstall the pre-existing VIX software. (If it is not already stopped, the wizard will gracefully stop the VIX service before performing the uninstall.)
8.  When the Uninstall is complete message displays near the top of the page, click Next.

![](mag-3-201-installation-guide/044.png)

9.  In the Site Number field of the Specify the VA Site... page, verify that the Site Number box shows your STATION NUMBER (field \#99) in the INSTITUTION file (#4).
10. Confirm the connection by clicking Lookup Server Address. Then click Next.
11. In the VIX Prerequisites page:
- Check the line that indicates the state of the Java Runtime environment. If ![](mag-3-201-installation-guide/045.png) is shown, do the following:
  - Click Install.
  - Wait until the status icon the Java Runtime Environment changes to ![](mag-3-201-installation-guide/046.png) . (This install of Java will take longer than previous versions and may take several minutes to complete)
- Check the line that indicates the state of the Apache Tomcat installation. If ![](mag-3-201-installation-guide/047.png) is shown, do the following:
  - Click Install.
  - In the dialog box that displays, enter and confirm the Apache Tomcat password that you prepared as described in [<u>Preparing Passwords,</u> <u>Activating Components, and Staging Files</u>](#_bookmark17) previously. Then, click OK.
  - Wait until the status icon for Apache Tomcat changes to ![](mag-3-201-installation-guide/048.png) . (This install of Tomcat will take longer than previous versions and may take several minutes to complete)
12. On the same page, check the line that indicates the state of the service account. If ![](mag-3-201-installation-guide/049.png) is shown, do the following:

> o Click Assign.

> ![](mag-3-201-installation-guide/050.png)

- If your service user did not change, click Yes. If you need to reassign the password, click No.
- If you answered No, in the dialog box that displays, enter the Windows service account password that you prepared [<u>Preparing Passwords,</u> <u>Activating Components, and Staging Files</u>](#_bookmark17) previously. Then, click OK.
- Wait until the status icon for the service account changes to ![](mag-3-201-installation-guide/051.png) .

> ![](mag-3-201-installation-guide/052.png)

13. Check the line that indicates VIX/Viewer Render Services.
    1.  If ![](mag-3-201-installation-guide/053.png) is shown, click Install. If ![](mag-3-201-installation-guide/054.png) is shown, click Reinstall.
    2.  Click Configure Viewer/Render

![](mag-3-201-installation-guide/055.png)

3.  Verify the following settings:
    1.  Verify the viewer port is set to 343.
    2.  Verify Site Service host name is set to localhost.
    3.  Verify Site Service port is set to 8080.
    4.  Verify VIX Service host name is set to localhost.
    5.  Verify instance name is .\\ SQLEXPRESS
4.  Edit image cache directory drive to the dedicated VIX cache drive. (For example, "E:\VIXRenderCache")
5.  If setting values were modified click the Save Configuration button in the top right corner. (The Save Configuration button will not activate unless configuration changes were actually made)
6.  Click OK
7.  If prompted to install the SQL server, click OK and select the SQLEXPRESS_X64- 14_0_1000_169.ZIP found in the “VIXSqlInstaller” folder in the temporary folder on the desktop. (Depending on your system, this step may take up to twenty minutes)

![](mag-3-201-installation-guide/056.png)

> ![](mag-3-201-installation-guide/057.png)

8.  After SQL 2017 install and BEFORE initializing VIX, clean up the VIX Render Cache folders. For example: If VIX cache is on D: drive \VixCache, select all VIX cache folders \[CTRL A\] then Delete \[CTRL D\]. Do the same with D:\VIXRenderCache (or your site selected cache drive).

![](mag-3-201-installation-guide/058.png)

9.  Click Next to continue.
10. Select the “C:\\ drive for VixConfig folder and the dedicated VIX cache drive for VixCache folder. (For example, “E:\VIXCache”) Click each Create button to confirm and create the folders.

## In the Specify the Release of Information (ROI) Configuration, do the following:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Specify the access and verify codes for the account with the ROI periodic processing credentials. The VIX uses this account for periodic processing of ROI disclosure requests. The account must be valid VistA credentials with the MAG DICOM VISA secondary menu option and the OR CPRS GUI CHART secondary menu option. The credentials can be the credentials of the same service account that the DICOM Gateway and the HDIG use.
- Specify the email address that gets notifications for invalid ROI periodic processing credentials. The VIX sends an email notification to the address or addresses specified in this field if the ROI periodic processing credentials are expired or invalid. You can enter several addresses, separated by a comma.

> ![](mag-3-201-installation-guide/059.png)

14. Click Validate.

> The VIX installation program checks the information. If it detects an error, it displays a tooltip with information about the error. When it validates the configuration, Next becomes available.

15. In the Configure Local DoD connection page, do one of the following:
- If your site has no local network connection to a DoD facility, click Next (this will be the case at most VA sites)
- If your site has a local network connection to a DoD facility, enter connection information for the DoD’s PACS Integrator server. After entering the connection information, click Validate to test the connection. Then, click Next.

> ![](mag-3-201-installation-guide/060.png)

16. ![](mag-3-201-installation-guide/061.png)On the Install the VIX page, click Install. (The information in this page is saved in C:\Program Files (x86)\VistA\Imaging\VixInstaller for future reference or troubleshooting.) This will start the installation process. It will also start the Tomcat and Viewer/Render services.
17. The VIX will start automatically when installation is complete.
18. Click Finish. The VIX Installation Wizard will close.

![](mag-3-201-installation-guide/062.png)

19. Confirm Hydra IX and Hydra VistA Worker threads (10 each):

> ![](mag-3-201-installation-guide/063.png)

20. Continue to [*<u>Verifying VIX Operations</u>*](#verifying-vix-operations)

# Post-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## McAfee Exclusions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Exclude the following directories using McAfee On Access Scan Properties (Make sure to exclude subfolders as well):

1.  C:\Program Files\Apache Software Foundation\Tomcat 8.0\logs
2.  C:\Program Files\VistA\Imaging\VIX.Render.Service\log
3.  C:\Program Files\VistA\Imaging\VIX.Viewer.Service\log
4.  C:\VixConfig\logs
5.  \<cache drive\>:\VixCache
6.  \<cache drive\>:\VIXRenderCache
7.  Disable jar file scanning as per P197 instructions on folders - C:\Program Files\Apache Software Foundation\Tomcat 8.0\lib C:\Program Files\Java\jre1.8.0_171\lib

![](mag-3-201-installation-guide/064.png)

![](mag-3-201-installation-guide/065.png)

## Verifying VIX Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After a new VIX is installed and is registered with the Image Exchange Service, Clinical Display (MAG\*3.0\*93 or later) and VistARad (MAG\*3.0\*90 or later) workstations will automatically start using the VIX.

- Clinical Display will begin sending requests for remote data to the VIX immediately. No configuration changes are required for Clinical Display to start using the VIX.
- VistARad will need some local configuration changes to enable some of its VIX- supported capabilities; refer to the VistARad documentation for details.

> <span id="_bookmark34" class="anchor"></span>Verifying Access to the VIX Transaction Log

> VIX administrators can use the VIX transaction log to monitor VIX activities. If the transaction log can be accessed, the VIX is running.

> To access the transaction log, you will need:

- A VistA account that has the MAG VIX ADMIN security key assigned to it (while the log is a Web page, the VIX uses a VistA account to secure the log).

## Access to http://\<FQDN\>:8080/Vix/secure/VixLog.jsp

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> (Where \<FQDN\> is either the fully qualified domain name of the server the VIX is installed on.)

> If you cannot access the transaction log, verify that the VIX service is running.

> If the VIX is running but you cannot access the transaction log, ensure that port 8080 on the VIX server is not blocked. Possible culprits of a blocked port include antivirus firewalls and modifications to ACLs (Access Control Lists).

> For detailed information about the contents of the transaction log, refer to the [*<u>VIX Viewer</u>*](https://www.va.gov/vdl/application.asp?appid=105)

> [*<u>Administrator’s Guide.</u>*](https://www.va.gov/vdl/application.asp?appid=105)

> You can also spot-check individual remote images to see if they were delivered via the VIX as described in this section.

> <span id="_bookmark35" class="anchor"></span>Spot-checking VIX Image Delivery

1.  On the Clinical Display workstation, select a patient with remote images.
2.  If it is not visible already, display the Abstracts area to display an abstract for one of the remote images.
3.  Right-click the abstract for the remote image and open the Image Information window.
4.  In the Image Information window, check the IEN (Internal Entry Number) value. If the value starts with “urn”, the remote image was retrieved by the VIX.
5.  Go to the VIX homepage: http://\<FQDN of VIX server\>:8080/
6.  The current version is listed in the format XX.XXX.X.X. The first two digits represent Version 3.0 of the VistA Imaging system and do not change. The next three digits are the number of the latest patch that has affected the VIX. This patch number should match the number of the VIX component you have most recently installed.

![](mag-3-201-installation-guide/066.png)

7.  Verify VIX Viewer and VIX Render services are running.

![](mag-3-201-installation-guide/067.png)

8.  Verify listener tool is running.

![](mag-3-201-installation-guide/068.png)

9.  If this is a new installation of the VIX, please go back to [<u>Post-Installation Steps</u>](#post-installation).

## Using the VIX Installation Wizard to Reconfigure the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will need to re-execute the VIX Installation wizard if you need to:

- Change the drive where the VixCache or VixConfig folders are located. It is recommended that these folders reside on the same shared drive.
- Change the VIX configuration to use a different local VistA host name or port number.

> Using the VIX Installation wizard is broadly similar to the steps for updating a VIX, except the process is much faster since no actual software is being installed.

> Note: The following steps that new cache location is set up and/or that the local VistA database connection change has already been made.

> Tip: Changing a VIX cache location or local connection information should take about 5 minutes.

> <span id="_bookmark37" class="anchor"></span>Reconfiguring a VIX – Standalone Server

1.  Review the information in the [*Scheduling Downtime and Impact of a VIX Update*](#_bookmark23)

> section, and schedule downtime and notify appropriate groups of the downtime.

2.  Log in as an administrator on the server where the VIX is installed and choose Start \| All Programs \| VistA Imaging Programs \| VIX Installation Service Wizard.

![](mag-3-201-installation-guide/069.png)

3.  Click Next until the Specify the VA Site... page displays.
4.  In this page, verify that the Site Number box shows your STATION NUMBER (field (#99) in the INSTITUTION file (#4)). Then, click Lookup Server Address.
5.  Verify that the correct hostname and port number for the local VistA system is displayed. Then, click Next.
6.  When the Install the VIX Prerequisites page displays, click Next. (All prerequisites are installed already).
7.  In the Specify the location... page, do one of the following:
    - If you are changing the location of the VIX cache and configuration files, select the new drive for each (the same drive should be used). Then, click Create. Then, click Next.
    - If you are NOT changing the location of the VIX cache and configuration files, click Next.
8.  In the Specify the Release of Information (ROI) Configuration, do the following:
    - If you want to change any of the values, enter the new values. If you are changing the email address or addresses for invalid ROI periodic processing credentials notification, click Validate. If you do not want to change any of the values on this page, skip this step.
    - Click Next.
9.  In the Configure local DoD connection page, click Next.
10. In the Install the VIX page, click Install.
11. Wait until the installation is complete and click Finish. The VIX will restart automatically.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Resuming an Interrupted VIX Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you have had to interrupt or cancel an in-progress VIX installation, you can resume the installation.

> Note: If you re-run MAG3_0P\<number\>\_VIX_Setup.msi, you are repeating the installation of the VIX Installation Wizard software, not the installation of the VIX itself. If you do this, click Cancel, choose Yes when prompted for confirmation, and then exit the installer. Then restart the VIX installation.

> <span id="_bookmark40" class="anchor"></span>Resuming Installation (single server VIX)

1.  Log onto the VIX server as an administrator.

### Click Start \| All Programs \| VistA Imaging Programs \| VIX Installation Wizard.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](mag-3-201-installation-guide/070.png)

2.  Follow the steps for a first-time standalone VIX installation or for updating a standalone VIX.

## VIX Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you encounter problems installing the VIX please call the National Service Desk at 1- 855-673-4357.

# Back Out/Uninstall

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Back Out/Uninstall Scenarios

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The information in this section addresses three possible cases that involve uninstalling a VIX:

- Troubleshooting
- Relocation onto a different server
- Decommission

> Each of these scenarios is outlined in the following sections.

> <span id="_bookmark44" class="anchor"></span>Uninstall/Restore as part of Troubleshooting

> If you need to remove and then immediately reinstall the VIX on the same server for troubleshooting purposes, you will need to do the following:

1.  Locate the product serial number for the Laurel Bridge software that is bundled with the VIX. This number is in the license paperwork that was provided by [<span class="mark">REDACTED</span>](mailto:VHAVILBLicenses@va.gov) when the VIX was set up.
2.  Note: You will need to re-enter this serial number as a part of the VIX installation process.

### Choose Start \| All Programs \| VistA Imaging Programs \| VIX Installation Service Wizard.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  When the Welcome page displays, verify that the screen displays “This wizard will guide you through the installation of the Vista Imaging Patch 201 VIX and click Next.
4.  Then, when you are prompted to do so, click Uninstall version 30.201.xxx. (The wizard will gracefully stop the VIX service before performing the uninstall.)
5.  Go to the Control Panel, choose Add/Remove Programs, and remove the MAG\*3.0\*201 VIX installer.
6.  Re-execute the VIX installation as if for a new standalone VIX, see [*<u>New VIX</u><u>Installation - Standalone Server</u>*](#_bookmark14) section.

> <span id="_bookmark45" class="anchor"></span>Relocating a VIX onto a New Server

> If you need to remove all traces of the VIX from the old server and set up the VIX on a new server, you will need to do the following:

1.  Contact the [<span class="mark">REDACTED</span>](mailto:VHAVILBLicenses@va.gov) mail group and arrange to have the existing Laurel Bridge DCF toolkit licenses transferred to a new server.
2.  Validate the new server where the VIX will be installed as described in the [*Selectingand Validating the VIX Server*](#_bookmark8) section.
3.  Manually remove the VIX as described in the [*Uninstalling the VIX*](#uninstalling-the-vix) section below.
4.  Re-execute the VIX installation as if for a new standalone VIX, see [*<u>New VIX</u><u>Installation – Standalone Server</u>*](#_bookmark14) section.

> <span id="_bookmark46" class="anchor"></span>Decommissioning a VIX

> If a VIX to be completely decommissioned and not replaced by another VIX, do the following:

1.  Notify the [<span class="mark">REDACTED</span>](mailto:VHAVILBLicenses@va.gov) mail group that the Laurel Bridge license seats used by your site are no longer being used.
2.  Contact [<span class="mark">REDACTED</span>](mailto:VHAVIVIXSETUP@VA.GOV) mail group to have the VIX security certificates retired and the VIX removed from the site service.
3.  Manually remove the VIX as described in the [*Uninstalling the VIX*](#uninstalling-the-vix) section below.
4.  In VistA, remove the MAG VIX ADMIN security key from the accounts that have this key assigned.

## Uninstalling the VIX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following steps explain how to completely remove a VIX and all its supporting components (toolkits, runtime environments, etc.) from the server where the VIX is installed.

> ![](mag-3-201-installation-guide/071.png)These steps will completely remove the VIX and permanently delete the VIX cache.

> Depending on the VIX server configuration and operating system, the specifics of removing the VIX will vary, but the general process is as follows:

1)  Stop the VIX service.
2)  Remove VIX-related applications, accounts, directories, and variables

> These steps do not require a server reboot, and can be performed while the rest of the Imaging system is active.

> <span id="_bookmark48" class="anchor"></span>Stopping the VIX service

> The steps for stopping the VIX service vary based on operating system.

> <span id="_bookmark49" class="anchor"></span>Remove VIX-related applications, accounts, directories, and variables

> After stopping (and/or removing) the VIX service as described in the previous sections, you will need to remove VIX software and settings.

> These steps presume you are already logged in as an administrator on the server where the VIX service used to reside.

> These steps cover all supported VIX configurations.

1.  Use Windows Explorer to navigate to the drive where the VIX Cache is located, and delete the following folders:

> \<shared drive letter\>\VixCache

> \<shared drive letter\>\VixConfig

2.  Use Windows Explorer to delete the following directories: C:\\ DCF_RunTime

> C:\Program Files\Java\jre1.8.0_171

3.  If you are removing the VIX permanently, also delete the following folders:

> ![](mag-3-201-installation-guide/072.png)SKIP THIS STEP if you are uninstalling and reinstalling the VIX on the same server for troubleshooting purposes. If you delete these folders, you will need to recreate the VIX configuration and request new VIX security certificates.

> \<shared drive letter\>\VixConfig C:\VixCertStore

4.  Open the window used to remove programs.
    - On Windows click Start \| Control Panel. Under the Programs item, click

### Uninstall a program.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Remove these three programs (no reboot required): Apache Tomcat 8.0.52

> Java (TM) 1.8.0. Update 171 VIX Service Installation Wizard

5.  In Windows Explorer, right-click the Local Disk (C:) folder, select Properties. Then, select the Security tab.
6.  Select the apachetomcat user and click Remove.
7.  Click OK to close the Properties dialog box, and click Yes when are asked if you want to continue.

> Note: If one or more “Error applying security” messages display, click Continue

> until they are all closed.

8.  Open the Computer Management/Server Manager window.
    - On Windows, right-click Computer on the desktop. Then, click Manage.
9.  In the tree on the left side of the window, navigate to Users.
    - On Windows, go to Server Manager/Configuration/ Local Users and Groups/Users.
10. In the right side of the window, right-click the apachetomcat user, click Delete, and click Yes when you are asked for confirmation.
11. Open the System Properties dialog box.
    - On Windows, right-click Computer on the desktop. Then, click Properties. Then on the left side of the System window, click Advanced system settings.
12. In the Advanced tab, click Environment Variables.
13. In the System variables list near the bottom of the dialog, delete the following variables:

<table>
<colgroup>
<col style="width: 47%" />
<col style="width: 52%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>CATALINA_HOME DCF_BIN DCF_CFG DCF_CLASSES DCF_LIB DCF_LOG DCF_PLATFORM DCF_ROOT DCF_TMP</p>
<p>DCF_USER_BIN</p>
</blockquote></th>
<th><blockquote>
<p>DCF_USER_CLASSES DCF_USER_LIB DCF_USER_ROOT LD_LIBRARY_PATH OMNI_BIN OMNI_LIB OMNI_ROOT</p>
<p>vixcache vixconfig</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

14. In the System variables list, select the Path system variable. Then, click Edit.
15. In the Variable value box, delete the following substrings: C:\DCF (if present)

> C:\DCF_Runtime\bin C:\DCF_Runtime\lib

> C:\Program Files\Java\jre1.8.0_xx\bin

> Note It is recommended that after deleting each substring you delete any extra semicolon characters.

16. After removing the substrings, click OK. Then click OK twice more to close the Environment Variables and System Properties dialog boxes.
17. If the VIX is installed on a standalone server, VIX removal is complete.

# Appendix A: VIX Install Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The checklist on this page summarizes the VIX installation process.

## VIX Install Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 54%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><strong>Requirement</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Action</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>☐</td>
<td>Install patch MAG*3.0*201 KIDS MAG3_0P201.KID in VistA</td>
<td><blockquote>
<p>See Patch Description Document</p>
</blockquote></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Verify VIX server/VM meets minimum hardware specifications</td>
<td><blockquote>
<p>Allocate more CPU cores/RAM as needed to meet minimum or recommended specifications</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Verify Microsoft Visual C++ 2010 Redistributable Package (x64) is installed</td>
<td><blockquote>
<p>Install Microsoft Visual C++ 2010 Redistributable Package (x64) if required. (Download from SFTP site)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Verify .NET 3.5 is installed and enabled</td>
<td><blockquote>
<p>Install and enable .NET 3.5 if required</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Verify .NET 4.5 is installed and enabled</td>
<td><blockquote>
<p>Install and enable .NET 4.5 if required (Download from SFTP site)</p>
</blockquote></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Verify you have the VIXSqlInstaller folder or zip file SQLExpress_x64-14.0.1000.169 (for P177 VIX site skip P197 VIX)</td>
<td><blockquote>
<p>Download from SFTP site if required</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Initiate the installation of the VIX MAG3_0P201_VIX_Setup.msi</td>
<td><blockquote>
<p>See Installation Guide</p>
</blockquote></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Verify if install is complete</td>
<td><blockquote>
<p>See Installation Guide</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Verify that VIX is running</td>
<td><blockquote>
<p>See Installation Guide</p>
</blockquote></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Verify that VIX Viewer and VIX render services started</td>
<td><blockquote>
<p>Verify in window services console</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Verify Listener Tool service is running</td>
<td><blockquote>
<p>Verify in window services console</p>
</blockquote></td>
</tr>
<tr class="even">
<td>☐</td>
<td>Verify that McAfee Exclusions are updated</td>
<td><blockquote>
<p>See Installation Guide</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>☐</td>
<td>Request Site Service update to your facility if needed</td>
<td><blockquote>
<p>Enter in national ticket requesting CLIN3 to</p>
<p>update your site service entry to include the new viewer. (Port 343)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 54%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>☐</th>
<th>Verify that images can be viewed via zero-footprint Image Viewer.</th>
<th><blockquote>
<p>Verify JLV or other application utilizing zero footprint viewer. If unable to view an image, enter a support ticket for</p>
<p>assistance.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>