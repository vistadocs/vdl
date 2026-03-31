---
title: XWB*1.1*35 and XWB*1.1*44 TCP/IP Supplement
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: and XWB*1.1*44 TCP/IP Supplement
app_code: XWB
app_name: Remote Procedure Call (RPC) Broker
section: INF
app_status: active
pkg_ns: XWB
patch_ver: 1.1
patch_id: XWB*1.1*35
group_key: "XWB:XWB:1.1"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <caption><p><span id=\\"_Ref111129761\\" class=\\"anchor\\"></span>Table 1: Documentation Symbol Descriptions</p></caption> <colgroup> <col style=\\"width: 14%\\" /> <col style=\\"width: 51%\\" /> <col style=\\"width: 34%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th>Date</th> <th>Description</th> <th>Autho"
audience: 
keywords: 
  - broker
  - service
  - tcpip
  - account
  - span
  - openvms
  - table
  - contents
  - access
  - cach
page_count: 0
word_count: 6633
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: January 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb1_1P44um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb1_1P44um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=23"
---

---
title: |
  RPC Broker 1.1

  TCP/IP Supplement:

  Patch XWB\*1.1\*35  
  Patch XWB\*1.1\*44
---

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/001.png)

Patch XWB\*1.1\*35 Original: January 2005

Patch XWB\*1.1\*44 Updated: December 2005

Revised: August 2022

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Development, Security, and Operations (DSO)

<span id="_Toc209429662" class="anchor"></span>Revision History

Document Revisions

<table>
<caption><p><span id="_Ref111129761" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 51%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/23/2022</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated document to follow current documentation standards and style guidelines.</p></li>
<li><p>Updates all styles and formatting.</p></li>
<li><p>Verified document is Section 508 conformant.</p></li>
<li><p>No changes to the overall content structure (e.g., multiple M environments), since that was the system design at the time of the original patch release.</p></li>
</ul></td>
<td>VistA Infrastructure Shared Services (VISS) Development Team</td>
</tr>
<tr class="even">
<td>11/30/2005</td>
<td>Patch XWB*1.1*44: Updated the <strong>XWBSERVER_START.COM</strong> file in <a href="#_bookmark19"><u>Figure 4</u>,</a> replacing the pipe command with individual commands to avoid a MAX SUB-PROCESS LIMIT.</td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>03/31/2005</td>
<td><p>Updates:</p>
<ul>
<li><p>Changed user (UAF) and directory names to <strong>VISTATCPSVC</strong>.</p></li>
<li><p>Updated the <strong>XWBSERVICE_START.COM</strong> to include <strong>$ csession</strong> examples in the Caché section for Test and Production accounts and for Production Data Centers.</p></li>
</ul></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>03/29/2005</td>
<td><p>Change the following:</p>
<ul>
<li><p><strong>UAF</strong> entry from <strong>VISTATCPSVC</strong> to <strong>BROKER</strong>.</p></li>
<li><p><strong>Directory</strong> from <strong>VISTATCPSVC</strong> to <strong>RPCSERVER</strong>.</p></li>
</ul></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>03/25/2005</td>
<td>Included a "<strong>_UAF&gt; /batch -</strong>" command line in the example showing the creation of the VMS User in <u>Figure 2</u>.</td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>03/10/2005</td>
<td>Edited the command lines beginning with <strong>CCONTROL</strong> to <strong>CSESSION</strong> in "<u>Figure 4</u>" to prevent the spawning of a sub-session.</td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>01/2005</td>
<td>Initial <em>RPC Broker 1.1 Patch XWB*1.1*35: TCP/IP Supplement</em> document.</td>
<td>RPC Broker Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref111129761" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the National Patch Module (NPM) on FORUM.

Table of Contents

<span id="_Toc112158760" class="anchor"></span>List of Figures

<span id="_Toc112158761" class="anchor"></span>List of Tables

[Table 1: Documentation Symbol Descriptions [vi](#_Ref111129761)](#_Ref111129761)

[Table 2: Terms and Definitions [20](#_Toc112158748)](#_Toc112158748)

<span id="_Toc111187559" class="anchor"></span>Orientation

This is the Veterans Health Information Systems and Technology Architecture (VistA) Remote Procedure Call (RPC) Broker Transmission Control Protocol/Internet Protocol (TCP/IP) Supplement exported with Patch XWB\*1.1\*35. This supplement uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                         | Description                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/002.png) | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/003.png)                                                              | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Toc112158748" class="anchor"></span>Table : Terms and Definitions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666.”
- Patient and user names are formatted as follows:
- \[Application Name\]PATIENT,\[N\]
- \[Application Name\]USER,\[N\]

Where “*\[Application Name\]*” is defined in the Approved Application Abbreviations document and “*\[N\]*” represents the first name as a number spelled out and incremented with each new entry.

For example, in RPC Broker (XWB) test patient names would be documented as follows:

XWBPATIENT,ONE; XWBPATIENT,TWO; XWBPATIENT,14, etc.

For example, in RPC Broker (XWB) test user names would be documented as follows:

XWBUSER,ONE; XWBUSER,TWO; XWBUSER,14, etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are in boldface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is in boldface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are in boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/004.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in the Toolbar to navigate back and forth in the Word document when selecting hyperlinks within the document.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/005.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/006.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.  
  
REF: For further information, see the *RPC Broker Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/007.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- Remote Procedure Call (RPC) Broker—VistA Client/Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language
- Open Virtual Memory System (OpenVMS)
- M operating systems:
- Caché on NT
- Caché on OpenVMS
- Digital Standard MUMPS (DSM) for OpenVMS
- GT.M on Linux or GT.M on OpenVMS

References

Readers who wish to learn more about RPC Broker should consult the following:

- Patch XWB\*1.1\*35 and XWB\*1.1\*44 Patch Descriptions (PDs) located in the National Patch Module on FORUM―Includes Installation Instructions.
- RPC Broker Release Notes
- RPC Broker Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)
- RPC Broker Systems Management Guide
- RPC Broker Technical Manual
- RPC Broker User Guide
- *RPC Broker Developer’s Guide*—This document provides an overview of development with the RPC Broker.
- RPC Broker VA Intranet website.  
    
  This site provides announcements, additional information (e.g., Frequently Asked Questions \[FAQs\], advisories), documentation links, archives of older documentation and software downloads.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: <http://www.va.gov/vdl/>

The RPC Broker documentation is located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=23>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
  - [Managing TCP/IP Services](#managing-tcpip-services)
  - [RPC Broker Service](#rpc-broker-service)
- [Multi-Threaded Service for Caché on NT](#multi-threaded-service-for-caché-on-nt)
  - [Setting Up a Multi-Threaded Service](#setting-up-a-multi-threaded-service)
  - [Starting and Stopping the Listening Service](#starting-and-stopping-the-listening-service)
- [TCPIP (UCX) Multi-Threaded Service on OpenVMS](#tcpip-ucx-multi-threaded-service-on-openvms)
  - [Set Up OpenVMS User Account](#set-up-openvms-user-account)
  - [Set Up Home Directory for the RPC Broker Handler Account](#set-up-home-directory-for-the-rpc-broker-handler-account)
  - [Create a DCL Login Command Procedure for the RPC Broker Handler](#create-a-dcl-login-command-procedure-for-the-rpc-broker-handler)
  - [Set Up and Enable the TCPIP Service](#set-up-and-enable-the-tcpip-service)
    - [Create a TCP/IP Service](#create-a-tcpip-service)
  - [Access Control List (ACL) Issues](#access-control-list-acl-issues)
  - [How to Control the Number of Log Files Created by TCPIP](#how-to-control-the-number-of-log-files-created-by-tcpip)
  - [Starting and Stopping the Service](#starting-and-stopping-the-service)
  - [Starting and Stopping the Service Cluster-Wide](#starting-and-stopping-the-service-cluster-wide)
- [Migration Considerations](#migration-considerations)
  - [DSM/VMS to Caché/VMS](#dsmvms-to-cachévms)
    - [Disable Any RPC BROKER Service(s)](#disable-any-rpc-broker-services)
  - [Caché/NT to Caché/VMS](#cachént-to-cachévms)
- [Glossary](#glossary)
- [Index](#index)
A Service Request (RPC Broker—Firewall Issue, service request \#20021001) was made for an enhancement to the RPC Broker that will allow local sites the ability to control the range of ports used in connecting to joint and/or contracting facilities. As a security measure, participating sites or joint facilities (i.e., Department of Defense \[DoD\] and universities) have firewalls set up to prevent intrusion. Lack of access to clinics outside the firewall is preventing session connections from thin clients to Computerized Patient Record System (CPRS). With the use of the Remote Procedure Call (RPC) Broker, which enables clients to communicate and exchange data over the network, sites could minimize security risks by controlling the range of available ports that would be open for connection.
In response to this request to operate with firewalls and other network security measures, the RPC Broker is eliminating the callback portion of the system. The Broker was changed to work more like other Transmission Control Protocol/Internet Protocol (TCP/IP) programs. This is the RPC Broker TCP/IP Supplement. It outlines the details of the work involved in setting up and managing RPC Broker TCP/IP services for all currently supported M operating systems.
This documentation is intended for use in conjunction with RPC Broker Patch XWB\*1.1\*35. Patch XWB\*1.1\*35 sets the groundwork for the next Broker Patch XWB\*1.1\*36, which implements a new Broker Developer Kit (BDK). This will allow VistA developer's access to this new RPC Broker server side TCP/IP service through the Broker client. Existing RPC Broker applications will work with this new server-side code, which will eventually replace the current Broker listener, XWBTCPL.
The intended audience for this documentation is VistA developers and VA facility system administrators.

## Managing TCP/IP Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker uses a TCP/IP service to "listen" on a particular port for incoming TCP/IP connections from other systems. Listeners are necessary whenever RPC Broker Clients need to initiate a connection to the VistA system over TCP/IP.

## RPC Broker Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TCPIP service is only available for the OpenVMS operating systems:

- Caché on OpenVMS.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/008.png) REF: For more information, see the "<u>TCPIP (UCX) Multi-Threaded Service on OpenVMS</u>" section.

- DSM for OpenVMS.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/009.png) REF: For more information, see the "<u>TCPIP (UCX) Multi-Threaded Service on OpenVMS</u>" section.

- GT.M on OpenVMS.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/010.png) REF: For more information, see the "<u>TCPIP (UCX) Multi-Threaded Service on OpenVMS</u>" section.

- GT.M on Linux.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/011.png) NOTE: No documentation is available for GT.M on Linux at this time.

# Multi-Threaded Service for Caché on NT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Windows NT operating system (OS) does *not* provide an equivalent service to OpenVMSTCPIP service. Kernel Patch XU\*8\*78, released in April of 1998, provides a way to provide a multi-threaded service for TCP/IP messaging for Caché on NT systems.

## Setting Up a Multi-Threaded Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set up a multi-threaded service, do the following:

1.  Define an entry for it in the RPC BROKER SITE PARAMETERS (#8994.1) file.
2.  Set or change the value of the TYPE OF LISTENER (#.5) field to "New Style" in File \#8994.1.
3.  Use the TaskMan Schedule/Unschedule Options \[XUTM SCHEDULE\] option to verify that XWB LISTENER STARTER is scheduled. You are then presented with the “Edit Option Schedule” ScreenMan form. Enter the value "STARTUP" in the SPECIAL QUEUEING field.

## Starting and Stopping the Listening Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start and stop the listening service, do the following:

- START SERVICE—To start a service outside of scheduling it through TaskMan, enter the following through programmer mode:

DO RESTART^XWBTCP

Or

JOB ZISTCP^XWBTCPM1(port#)

- STOP SERVICE—To stop the listener, enter the following through programmer mode:

DO STOPALL^XWBTCP

# TCPIP (UCX) Multi-Threaded Service on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multi-threaded listeners are implemented using OpenVMS's TCPIP (aka Digital TCPIP services for OpenVMS, formerly known as UCX). The TCPIP service uses a cluster-wide database. The TCPIP multi-threaded service on OpenVMS permits multiple TCPIP clients to connect and run as concurrent processes up to the limits established by the system. TCPIP listens on a particular port and launches the specified RPC Broker handler process for each client connection.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/012.png) The following names, found in a typical RPC Broker Handler process, are referenced throughout this chapter:

- BROKER―OpenVMS account name for TCPIP RPC Broker handler.
- \[RPCSERVER\]―Name of home directory.
- XWBSERVER_START.COM―Name of template DCL command procedure.

For the TCPIP RPC Broker handler process, you need to create the following:

- OpenVMS account.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/013.png) REF: For more information, see the "<u>Set Up OpenVMS User Account</u>" section.

- Home directory.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/014.png) REF: For more information, see the "<u>Set Up Home Directory for the RPC Broker Handler Account</u>" section.

- Digital Command Language (DCL) login command procedure.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/015.png) REF: For more information, see the "<u>Create a DCL Login Command Procedure for the RPC Broker Handler</u>" section.

## Set Up OpenVMS User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The easiest way to configure an OpenVMS account for the RPC Broker handler is to use a current account, like VA MailMan or Health Level Seven (HL7), and adjust its parameters. The other way is to create a new OpenVMS account for the RPC Broker handler. The following steps illustrate how to do this:

1.  Determine an unused UIC:

Determine an unused User Identification Code (UIC). This is selected from the same UIC group as other DSM or Caché for OpenVMS accounts, depending on which version of M you are using.

2.  Create a BROKER account with the unused UIC:

Use the OpenVMS Authorize Utility to create a BROKER account with the unused UIC.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/016.png) CAUTION: You *must* be running from a system administrator account to set up an OpenVMS user account.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/017.png) CAUTION: Since the TCPIP is node-specific, make sure you set up the TCPIP service for each node on which you want the service to run.

The following two examples illustrate different ways to set up an OpenVMS User account to execute the RPC service COM file:

1.  Copy your existing XMINET (TCP/IP MailMan) account to a new account with an unused UIC. <u>Figure 1</u> contains the recommended settings and assumes you already have an XMINET account on OpenVMS.

> <span id="_Ref111192036" class="anchor"></span>Figure 1: Copy XMINET (TCP/IP MailMan) Account to a New Account with an Unused UIC

\$ MCR AUTHORIZE

UAF\> COPY XMINET BROKER/UIC=\[51,45\]/DEVICE=USER\$/DIRECTORY=RPCSERVER

%UAF-I-COPMSG, user record copied

%UAF-W-DEFPWD, copied or renamed records must receive new password

%UAF-I-RDBADDMSGU, identifier BROKER value \[000051,000045\] added to rights database

UAF\>

2.  Create the new BROKER VMS account. <u>Figure 2</u> illustrates how to create an OpenVMS User account from scratch with the recommended settings. You *must* adhere to minimum account quota recommendations from the AXP/VMS Technical Support Team.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/018.png) REF: For more information on recommended account quotas, see the [AXP/VMS Technical Support Team](http://vaww.va.gov/custsvc/cssupp/axp/default.asp) website.

> <span id="_Ref38264753" class="anchor"></span>Figure 2: Create an OpenVMS User from Scratch

\$ MC AUTHORIZE

UAF\> ADD BROKER /UIC=\[51,45\]/OWNER="\<cache\>or\<DSM\>" -\_UAF\> /DEVICE=USER\$/DIRECTORY=\[RPCSERVER\] -\_UAF\> /NOACCESS/NETWORK/FLAGS=(DISCTLY,RESTRICTED,NODISUSER) -\_UAF\> /PRIV=(NETMBX,TMPMBX) –\_UAF\> /batch -\_UAF\> /DEF=(NETMBX,TMPMBX)/LGICMD=NL:

%UAF-I-ADDMSG, user record successfully added

%UAF-I-RDBADDMSGU, identifier BROKER value \[000051,000045\] added to rights database

UAF\>

3.  Verify Account Settings:

Verify the settings for your new BROKER account or the account you are going to use. Now you want to see what the parameters look like. <u>Figure 3</u> contains the settings for your new BROKER account. Verify that your settings are the same as they appear in <u>Figure 3</u>; or if they are different, verify that the impact of the different settings is acceptable for your system.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/019.png) REF: The example in <u>Figure 3</u> assumes that you have just completed the steps illustrated in either <u>Figure 1</u> or <u>Figure 2</u>.

> <span id="_Ref38265295" class="anchor"></span>Figure 3: Verify the Settings for the New BROKER Account

\$ MCR AUTHORIZE

UAF\> SHOW BROKER

Username: BROKER Owner: (DSM or Cache)

Account: UIC: \[51,45\] (\[BROKER\])

CLI: DCL Tables: DCLTABLES

Default: USER\$:\[RPCSERVER\]

LGICMD: NL:

Flags: DisCtlY Restricted

Primary days: Mon Tue Wed Thu Fri

Secondary days: Sat Sun

Primary 000000000011111111112222 Secondary 000000000011111111112222

Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

Network: \##### Full access \###### \##### Full access \######

Batch: \##### Full access \###### \##### Full access \######

Local: ----- No access ------ ----- No access ------

Dialup: ----- No access ------ ----- No access ------

Remote: ----- No access ------ ----- No access ------

Expiration: (none) Pwdminimum: 6 Login Fails: 0

Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

Last Login: (none) (interactive), (none) (non-interactive)

Maxjobs: 0 Fillm: 600 Bytlm: 200000

Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

Maxdetach: 0 BIOlm: 600 JTquota: 8192

Prclm: 2 DIOlm: 2048 WSdef: 2048

Prio: 4 ASTlm: 4096 WSquo: 4096

Queprio: 0 TQElm: 50 WSextent: 65535

CPU: (none) Enqlm: 4096 Pgflquo: 200000

Authorized Privileges:

NETMBX TMPMBX

Default Privileges:

NETMBX TMPMBX

UAF\> EXIT

%UAF-I-DONEMSG, system authorization file modified

%UAF-I-RDBDONEMSG, rights database modified

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/020.png) CAUTION: As a security precaution, make sure that the DisCtlY and Restricted flags are set.

## Set Up Home Directory for the RPC Broker Handler Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to create a home directory for the RPC Broker handler account. This directory will house the DCL command procedures, which are executed whenever a client connects. Make sure that the owner of the directory is the BROKER account.

For example, to create a home directory named \[RPCSERVER\] with ownership of BROKER:

\$ CREATE/DIR USER\$:\[RPCSERVER\]/OWNER=BROKER

## Create a DCL Login Command Procedure for the RPC Broker Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure in the home directory for the handler account. Make sure the command procedure file is owned by the RPC Broker handler account.

Copy the sample COM file: XWBSERVER_START.COM, from any VistA anonymous directory. Create a local copy to edit, you will need one file for each TCP/IP service (port). All nodes of the cluster share the same COM file.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/021.png) NOTE: Make sure that you do *not* have a current XWBSERVER_START.COM file being used by the M2M Broker Service. XWBSERVER_START.COM is a template file. Make a copy to edit for each service you setup. You want to give the service a name that helps make the link with the account and port that it uses.

\$COPY XWBSERVER_START.COM VAH9200.COM

Edit your local copy of the COM file as follows:

1.  Adjust the command line (environment, UCI, and volume set) to match your system. In the command line section of the COM file for each vendor, there are parameters in the angle brackets (\< \>) that need to be replaced with the correct values for your site. Example, for DSM, copy the following sample line, keeping in mind to replace the *\<dsmmgr\>*, *\<vah\>*, and *\<rou\>* with the correct values for your site:

"DSM/ENV=*\<dsmmgr\>*/UCI=*\<vah\>*/VOL=*\<rou\>*/data="''dev'" DSM^XWBTCPM"

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/022.png) REF: For the specific changes that need to be made for Caché or GT.M, see <u>Figure 4</u>.

4.  If you are running DSM and access control is enabled, ensure that the BROKER account has access to this UCI, volume set, and routine.

You can run the same TCPIP service processes on multiple nodes. This depends on your sites configuration and needs. For instance, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate, permitting the listening process to continue uninterrupted if one node stops. This requires that the RPC BROKER TCPIP service be enabled on all nodes in the cluster. For this reason, it is *recommended* that you enable the RPC BROKER TCPIP service on most or all of the nodes in the cluster.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/023.png) REF: For more information on DSM and access control, see the "<u>Access Control List (ACL) Issues</u>" section.

> <span id="_Ref38335570" class="anchor"></span>Figure 4: Sample DCL Command Procedure

\$!XWBSERVER_start.COM - for incoming tcp connect requests

\$! Revision History:

\$! Patch XWB\*1.1\*35

\$! Add code to get remote IP address.

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ say :== write sys\$output

\$! Purge at end

\$ set prot=(s:rwed,o:rwed,g:rwe,w:rwe)/default

\$!

\$ dev=f\$trnlnm("sys\$net") !This is our MBX device

\$ NODE=F\$EDIT(F\$GETSYI("SCSNODE"),"COLLAPSE,TRIM") !Node Name

\$!

\$ say "Opening " + dev !This can be viewed in the log file

\$!

\$! With TCPIP Services for OpenVMS 5.3 ECO \#2 or higher,

\$! the below section can be removed.

\$!

\$! Check status of the BG device before going to VistA

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''dev'","STS")

\$ if cnt .eq. 100

\$ then

\$ say "Could not open ''dev' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ say "Stat: ''stat' Cnt:''cnt' Dev: ''dev' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ endif

\$ endif

\$! End of TCPIP Services for OpenVMS 5.3 ECO \#2 or higher, removal

\$!

\$!-------------------------------------------------------------

\$ bg == f\$extract(1,f\$locate(":",dev)-1,dev)

\$ pid = f\$getjpi("","PID")

\$ assign /user pipe1\_'pid'.tmp sys\$output

\$ TCPIP SHOW DEVICE 'bg'

\$ search pipe1\_'pid'.tmp 'bg' /output=pipe2\_'pid'.tmp

\$ open/error=err_exit/end=err_exit host pipe2\_'pid'.tmp

\$ read host line

\$ close host

\$ delete /noconfirm /nolog pipe1\_'pid'.tmp;\*,pipe2\_'pid'.tmp;\*

\$ port = f\$edit(f\$extract(24,5,line),"TRIM")

\$ ip = f\$edit(f\$extract(55,15,line),"TRIM")

\$!

\$ define VistA\$IP "''ip'"

\$!-------------------------------------------------------------

\$ say "''dev' from host ''ip' is now ready for use."

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is enabled,

\$! \*\*that this account has access to this uci,vol & routine.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$! anything in \<x\> needs to be replaced including the \<\> with local data

\$!-------------------------------------------------------------

\$! for DSM

\$! dsm/env=\<dsmmgr\>/uci=\<vah\>/vol=\<rou\>/data="''dev'" DSM^XWBTCPM

\$!-------------------------------------------------------------

\$! for Cache

\$! Edit only one of the three ‘csession’ lines below.

\$!

\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$!

\$! \#1 -- For Test Accounts

\$! if the configname is not the same as the node name, usually a test

\$! account, edit/use the ‘csession’ line below

\$! Remove the comment character ‘!’ from the beginning of the line.

\$! Replace \<PREFIX\>, including the \<\>, with the proper Test account

\$! prefix.

\$! Usually this is T or TST

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is TST for a Test account.

\$!

\$! an Example -- \$ csession "T''NODE'" "-U" "TST" "CACHEVMS^XWBTCPM"

\$!

\$! csession "\<PREFIX\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XWBTCPM"

\$!

\$! \#2 -- For most Production Accounts.

\$! OR if your configname is the same as your node name, usually a non-data

\$! center production site, edit/use the ‘cesssion’ line below.

\$! Remove the comment character ‘!’ from the beginning of the line.

\$! Replace \<namespace\>, including the \<\> with the correct namespace,

\$! Usually the namespace is "VAH" for production.

\$!

\$! an Example -- \$ csession "''NODE'" "-U" "VAH" "CACHEVMS^XWBTCPM"

\$!

\$! csession "''NODE'" "-U" "\<namespace\>" "CACHEVMS^XWBTCPM"

\$!

\$! \#3 -- for Data-Center Production Accounts

\$! OR, for a production Data Center site, edit/use the ‘csession’ line below.

\$! Remove the comment character ‘!’ from the beginning of the line.

\$! Replace \<NSP\>, including the \<\>, with the proper site prefix.

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is the same as the value used for NSP.

\$!

\$! an Example -- \$ csession "BRX''NODE'" "-U" "BRX" "CACHEVMS^XWBTCPM"

\$!

\$! csession "\<NSP\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XWBTCPM"

\$!\$!-------------------------------------------------------------

\$! for GT.M

\$! assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$! Depending on how your command files are set up, you may need to

\$! run the GT.M profile file.

\$! @\<user\$:\[gtmmgr\]\>gtmprofile.com

\$! forfoo="\$" + f\$parse("user\$:\[gtmmgr.r\]ZFOO.exe")

\$! forfoo GTMUCX^XWBTCPM("''dev'")

\$!

\$!

\$ exit:

\$ purge/keep=100 sys\$login:\*.log !Purge log files only

\$ logout/brief

## Set Up and Enable the TCPIP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After you have done the following:

- Created the RPC Broker account.
- Created the TCPIP service to listen for connections.
- Launched the RPC Broker handler.

Do the following three steps:

1.  Select the OpenVMS nodes upon which to run the service.

Designate the nodes on which you want to run the resulting M jobs to handle incoming RPC Broker connections. You will need to set up the TCPIP service on each node that you want the service to run.

5.  Select the port upon which the new service should listen.

This will be the port you are currently using for the Broker listener.

6.  Specify the user account and command file name (see the "<u>Set Up OpenVMS User Account</u>" section) invoked when a connection is received.

### Create a TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/024.png) CAUTION: Prior to setting up the TCP/IP service in Production, it is *recommended* that you create a test TCP/IP service that uses a different port to listen on, which sends connections into an M Test account. This test TCP/IP service can use the same OpenVMS account and directory that the Production TCP/IP uses. However, it is *recommended* that you create a different DCL command file (e.g., TST9900.COM) for the UCI and port for the Test account.

The steps to set up a TCP/IP service for the RPC Broker are listed as follows:

1.  Set up the RPC BROKER TCP/IP service.

Since the TCP/IP service database is cluster-wide, sign onto one node in the Production cluster and create the service.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/025.png) CAUTION: The LIMIT *must* be set high enough to allow access for all your CPRS and other RPC Broker users that you want to run on that node.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/026.png) NOTE: You will need to provide unique names on each node for each account, because all files will be located in a common directory. Each RPC service on a node *must* have a unique name. The TCPIP service is named VAH9200 for the purposes of this documentation only.

> <span id="_Toc98293285" class="anchor"></span>Figure 5: Set Up the VAH9200 TCPIP Service

\$ TCPIP

TCPIP\> SET SERVICE VAH9200/USER=BROKER/PROC=VAH9200/PORT=9200-

TCPIP\> /PROTOCOL=TCP/REJECT=MESSAGE="#Signon Limit Reached#" –

TCPIP\> /LOG=ADDRESS/LIMIT=500/FILE=VAH9200.COM

TCPIP\> SHO SERVICE VAH9200/FULL

Service: VAH9200

State: Disabled

Port: 9200 Protocol: TCP Address: 0.0.0.0

User_name: BROKER Process: VAH9200

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/027.png) NOTE: Set the port number to match the port number in use by your site.

7.  Enable and set boot status for the RPC BROKER TCP/IP service on every node where you need to run the service.

On the same node:

> <span id="_Toc98293286" class="anchor"></span>Figure 6: Enable and Set Boot Status for the RPC BROKER TCPIP Service

TCPIP\> ENABLE SERVICE VAH9200

TCPIP\> SET CONFIG ENABLE SERVICE VAH9200

TCPIP\> SHO SERVICE/FULL VAH9200

Service: VAH9200

State: Enabled

Port: 9200 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: BROKER Process: VAH9200

Limit: 500 Active: 0 Peak: 0

File: VAH9200.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: \#Signon Limit Reached#

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, VAH9200, MPI, TELNET, XMINETMM

TCPIP\> EXIT

## Access Control List (ACL) Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some sites use DSM's ACL feature, which controls access explicitly to each OpenVMS account needing to enter that specific DSM environment. If your site is using ACL, you should set up the BROKER account with PROGRAMMER access, then specify the Volume set and UCI name that the BROKER user account has authorization to access. Ensure that the OpenVMS BROKER account:

- Prohibits the following logins:
- Batch
- Local
- Dialup
- Remote
- Allows only Network logins.

<u>Figure 7</u> is an example of setting this level of access for a BROKER account:

<span id="_Ref40772606" class="anchor"></span>Figure 7: Access Control List (ACL) for BROKER

\$ <span class="mark">DSM/ENV=\<dsmmgr\>/MAN ^ACL</span>

Environment Access Utilities

<span class="mark">1. ADD/MODIFY USER</span> (ADD^ACL)

2\. DELETE USER (DELETE^ACL)

3\. MODIFY ACTIVE AUTHORIZATIONS (^ACLSET)

4\. PRINT AUTHORIZED USERS (PRINT^ACL)

Select Option \> <span class="mark">1 \<Enter\></span> ADD/MODIFY USER

OpenVMS User Name: \> <span class="mark">BROKER</span>

ACCESS MODE VOL UCI ROUTINE

----------- --- --- -------

No access rights for this user.

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> <span class="mark">P</span>

Volume set name: \> <span class="mark">ROU</span>

UCI: \> <span class="mark">VAH</span>

UCI: \> <span class="mark">\<Enter\></span>

Volume set name: \> <span class="mark">\<Enter\></span>

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> <span class="mark">\<Enter\></span>

USER ACCESS MODE VOL UCI ROUTINE

---- ----------- --- --- -------

BROKER PROGRAMMER ROU VAH

OK to file? \<Y\> <span class="mark">\<Enter\></span>

OpenVMS User Name: \> <span class="mark">\<Enter\></span>

OK to activate changes now? \<Y\> <span class="mark">\<Enter\></span>

Creating access authorization file: SYS\$SYSDEVICE:\[DSMMGR\]DSM\$ACCESS.DAT.

## How to Control the Number of Log Files Created by TCPIP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TCPIP service automatically creates log files in the RPCSERVER directory named VAH9200.LOG;*xxx* (where "*xxx*" is a file version number).

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/028.png) NOTE: TCPIP does this, and it *cannot* be prevented.

The XWBSERVER_START.COM template file purges extra log files as part of its running. New versions of the log file are created until that file version number reaches the maximum number of 32767. This can be used to limit the number of log files by explicitly setting the log file to the highest version number (32767) on the VAH9200.LOG file. This results in the VAH9200.LOG file being renamed to VAH9200.LOG;32767, and no further versions of this log file are created. If a system manager needs to see the log file contents of new connections, they can rename that file to a lower version, such as VAH9200.LOG;32760, and let new log files be created.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/029.png) CAUTION: It is *recommended* that you *not* limit the number of versions of the log file until you know that your VAH9200 service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

## Starting and Stopping the Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because this is a TCPIP service, use TCPIP to enable and disable it, as shown in <u>Figure 8</u>:

<span id="_Ref40773039" class="anchor"></span>Figure 8: Start and Stop the TCPIP Service

TCPIP\> <span class="mark">ENABLE SERVICE VAH9200</span>

TCPIP\> <span class="mark">DISABLE SERVICE VAH9200</span>

## Starting and Stopping the Service Cluster-Wide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the OpenVMS command SYSMAN to run the TCPIP command on each member of the cluster, as shown in <u>Figure 9</u>:

<span id="_Ref40773273" class="anchor"></span>Figure 9: Start and Stop the TCPIP Service Cluster-Wide

ISFVA2\$ <span class="mark">MC SYSMAN</span>

SYSMAN\> <span class="mark">SET ENV/CLU</span>

%SYSMAN-I-ENV, current command environment:

Clusterwide on local cluster

Username SYSTEM will be used on nonlocal nodes

SYSMAN\> DO TCPIP ENABLE SERVICE VAH9200

# Migration Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section addresses issues and considerations involved in moving from the platforms listed below, to Caché/VMS:

- Migrating from DSM/VMS to Caché/VMS as documented in the "<u>DSM/VMS to Caché/VMS</u>" section.
- Migrating from Caché/NT to Caché/VMS involves only one step related to the NT platform prior to migrating to Caché/VMS. This is documented in the "<u>Caché/NT to Caché/VMS</u>" section.

## DSM/VMS to Caché/VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site is running DSM/VMS and you are migrating to Caché/VMS, it is *recommended* that you read these instructions to make the necessary VMS configuration changes.

![](xwb-1-1-35-and-xwb-1-1-44-tcp-ip-supplement/030.png) NOTE: These changes *must only* be done after shutting down DSM and prior to migrating to Caché/VMS.

### Disable Any RPC BROKER Service(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To disable RPC BROKER services, do the following:

1.  Disable all user access:

Check the existing BROKER user and ensure that the User Identification Code (UIC) is correct for Caché/VMS.

8.  Modify the existing VAH9200.COM file to start Caché in place of DSM.
9.  You are now ready to migrate to Caché. Perform the necessary steps for migration including any backups, disk conversions, and the shutdown of DSM.
10. After the migration is complete and Caché is activated for use, remember to enable the RPC BROKER service.

## Caché/NT to Caché/VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site is running Caché/NT and you are migrating to Caché/VMS , follow these instructions to remove the multi-threaded service and create the TCPIP service:

1.  Remove the entry for it in the RPC BROKER SITE PARAMETERS (#8994.1) file.
11. Use TaskMan’s Schedule/Unschedule Options \[XUTM SCHEDULE\] option to remove the XWB LISTENER STARTER option from the schedule.
12. Follow the instructions documented in the “<u>TCPIP (UCX) Multi-Threaded Service on OpenVMS</u>” section.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Term                                    | Definition                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-----------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL                                 | Access Control List.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DCL                                 | Digital Command Language.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DEPARTMENT OF VETERANS AFFAIRS (VA) | The Department of Veterans Affairs, formerly called the Veterans Administration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| DHCP                                | Decentralized Hospital Computer Program of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA) is the former name for Veterans Health Information Systems and Technology Architecture (VistA). VistA software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M and, via the Kernel, runs on all major M implementations regardless of vendor. VistA is composed of packages that undergo a verification process to ensure conformity with namespacing and other VistA standards and conventions. |
| FIELD                               | In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file's data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.                                                                                                                                                                                                                            |
| FILE                                | Set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| FILE MANAGER (VA FILEMAN)           | VistA's Database Management System (DBMS). The central component of Kernel that defines the way standard VistA files are structured and manipulated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| KERNEL                              | Kernel is VistA software that functions as an intermediary between the host operating system and other VistA software applications (e.g., Laboratory, Pharmacy, IFCAP, etc.). Kernel provides a standard and consistent user and programmer interface between software applications and the underlying M implementation.                                                                                                                                                                                                                                                                                                  |
| MENU                                | List of choices for computing activity. A menu is a type of option designed to identify a series of items (other options) for presentation to the user for selection. When displayed, menu-type options are preceded by the word "Select" and followed by the word "option" as in Select Menu Management option: (the menu's select prompt).                                                                                                                                                                                                                                                                              |
| MENU SYSTEM                         | The overall Menu Manager logic as it functions within the Kernel framework.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| OPTION                              | An entry in the OPTION file (#19). As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by TaskMan.                                                                                                                                                                                                                                                                                                                                                             |
| PROMPT                              | The computer interacts with the user by issuing questions called prompts, to which the user issues a response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ROUTINE                             | Program or a sequence of instructions called by a program that may have some general or frequent use. M routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.                                                                                                                                                                                                                                                                                                                                                                                                   |
| RPC Broker Clients                  | Any Windows application that makes use of the RPC Broker to do the connection with the VistA system.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TCP/IP                              | Transmission Control Protocol/Internet Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| TCPIP                               | Digital TCPIP services for OpenVMS, this used to be called UCX. TCPIP permits multiple TCPIP clients to connect and run as concurrent processes up to the limits established by the system. TCPIP listens on a particular port and launches the specified RPC Broker handler process for each client connection.                                                                                                                                                                                                                                                                                              |
| VA FILEMAN                          | Set of programs used to enter, maintain, access, and manipulate a database management system consisting of files. A software application of online computer routines written in the M language, which can be used as a standalone database system or as a set of application utilities. In either form, such routines can be used to define, enter, edit, and retrieve information from a set of computer stored files.                                                                                                                                                                                                   |
| VistA                               | Veterans Health Information Systems and Technology Architecture (VistA) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). VistA software, developed by the VA, is used to support clinical and administrative functions at VHA sites nationwide. Server-side code is written in M, and, via Kernel, runs on all major M implementations regardless of vendor. VistA is composed of software that undergoes a quality assurance process to ensure conformity with namespacing and other VistA standards and conventions.                                               |

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Access Control List (ACL) Issues
Allow only Network Logins 15
authorization access 15
PROGRAMMER access 15
setting level of access for RPCSERVER account 16
accounts
MailMan TCP (XMINET) 5
OpenVMS RPC Broker handler 4
RPC BROKER 8
RPC Broker handler 8
RPCSERVER 5
Assumptions viii
AXP/VMS Technical Support Team 6
B
Broker Patch XWB\*1.1\*35 1
Broker Patch XWB\*1.1\*36 1
C
Caché command line 8
Caché on NT, Multi-threaded Service for
set up service 3
starting and stopping service 3
Callout Boxes vii
Captive flag 7
COM file
XWBSERVER_START.COM 4, 8
D
Data Dictionary
Data Dictionary Utilities Menu viii
Listings viii
DCL command procedure
TCPIP (UCX) Multi-threaded Service for Cache on OpenVMS 4
DI DDU Menu viii
DILIST Option viii
directories
DCL command procedure 8
RPC Broker handler account 8
RPCSERVER 8
setup 8
TCPIP (UCX) Multi-threaded Service for Cache on OpenVMS 4
directory, home 4, 8
DisCtlY flag 7
Documentation
Revisions ii
Symbols vi
Documentation Navigation vii
DSM command line 8
DSM's ACL (Access Control List) feature
Allow only Network Logins 15
authorization access 15
PROGRAMMER access 15
setting level of access for RPCSERVER account 16
F
field, TYPE OF LISTENER (#.5) 3
Firewall Issue Request \#20021001 1
flags
Captive 7
DisCtlY 7
Restricted 7
G
Glossary 19
H
Help
At Prompts viii
Online viii
Question Marks viii
History
Revisions ii
home directory 4
DCL command procedure 8
RPC Broker handler account 8
RPCSERVER 8
set up 4, 8
Home Pages
Adobe Website ix
RPC Broker Website ix
VA Software Document Library (VDL) Website ix
RPC Broker ix
How to
Obtain Technical Information Online viii
I
Introduction 1
L
List File Attributes Option viii
log files 16
M
MailMan TCP account (XMINET) 5
Managing TCP/IP Services, Introduction 1
Menus
Data Dictionary Utilities viii
DI DDU viii
Migration Considerations
Caché/NT to Caché/VMS 18
disable any RPC BROKER service(s) 18
disable users 18
DSM/VMS to Caché/VMS 18
User Identification Code 18
Multi-threaded Service for Caché on NT
RPC BROKER SITE PARAMETERS file (#8994.1) 3
set up 3
SPECIAL QUEUEING STARTUP 3
starting and stopping service 3
TaskMan 3
TYPE OF LISTENER field (#.5) 3
N
network security 1
O
Obtaining
Data Dictionary Listings viii
Online
Documentation viii
Technical Information, How to Obtain viii
OpenVMS account
TCPIP (UCX) Multi-threaded Service for Cache on OpenVMS 4
OpenVMS Nodes 12
OpenVMS RPC Broker handler account 4
OpenVMS User Account, Set Up
Captive flag 5
DisCtlY flag 5
Restricted flag 5
RPCSERVER 6
XMINET 6
Options
Data Dictionary Utilities viii
DI DDU viii
DILIST viii
List File Attributes viii
Orientation vi
P
Product Support (PS)
Anonymous Directories ix
PS
Anonymous Directories ix
Q
Question Mark Help viii
R
Restricted flag 7
Revision History
Documentation ii
Revision History ii
RPC Broker
Website ix
RPC Broker handler account
DCL command procedure 8
RPC Broker Service 1
RPC BROKER SITE PARAMETERS file (#8994.1)
TYPE OF LISTENER field (#.5) 3
RPC BROKER TCPIP service
set up 13
RPCSERVER 5
RPCSERVER account 16
S
security, network 1
Service Request \#20021001 1
Set Up OpenVMS User Account
Captive flag 5
Restricted flag 5
RPCSERVER 6
XMINET 6
starting and stopping service
DO RESTART^XWBTCP 3
DO STOPALL^XWBTCP 3
Multi-threaded Service for Caché on NT 3
TCPIP (UCX) Multi-threaded Service for Cache on OpenVMS 17
Support
Anonymous Directories ix
Symbols
Found in the Documentation vi
T
TaskMan 3
TCP/IP Listeners
TCPIP (UCX) Multi-threaded Service for Cache on OpenVMS 4
TCPIP (UCX) Cluster Wide
starting and stopping service 17
TCPIP (UCX) Multi-threaded Service for Cache on OpenVMS
home directory 8
starting and stopping service 17
TCP/IP Listeners 4
TCPIP service
set up 13
set up and enable 12
TCPIP Service
Multi-threaded for Caché on NT 3
TYPE OF LISTENER field (#.5) 3
U
unique naming conventions
RPC service 13
URLs
Adobe Website ix
AXP/VMS Technical Support Team 6
RPC Broker documentation 4
RPC Broker Website ix
VA Software Document Library (VDL) Website ix
RPC Broker ix
User Account, Set Up OpenVMS
Captive flag 5
DisCtlY flag 5
Restricted flag 5
RPCSERVER 6
XMINET 6
V
VA Software Document Library (VDL)
Website ix
RPC Broker ix
VAH9200 TCPIP
log files 16
W
Web sites
AXP/VMS Technical Support Team 6
RPC Broker documentation 4
Websites
Adobe Website ix
RPC Broker ix
VA Software Document Library (VDL) Website ix
RPC Broker ix
X
XWBSERVER_START.COM 4, 8
