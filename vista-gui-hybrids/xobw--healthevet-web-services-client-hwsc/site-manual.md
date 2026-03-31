---
title: HealtheVet Web Services Client (HWSC) Version 1 Systems Management Guide
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: Systems Management Guide
app_code: XOBW
app_name: HealtheVet Web Services Client (HWSC)
section: GUI
app_status: active
pkg_ns: XOBW
patch_ver: 1
patch_id: XOBW*1
group_key: "XOBW:XOBW:1"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - server
  - class
  - hwsc
  - table
  - service
  - span
  - services
  - manager
  - contents
  - certificate
page_count: 0
word_count: 6053
section_count: 9
table_count: 6
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw1_0sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw1_0sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=180"
---

---
title: |
  <span id="_Toc89057903" class="anchor"></span>HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> 1.0

  Systems Management Guide
---

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/001.png)

October 2016

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

<span id="_Toc456020163" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref455581318" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 43%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>10/20/2016</td>
<td>2.0</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Added the “<a href="#_Toc338740692">Orientation</a>” section.</p></li>
<li><p>Updated the “<u>Introduction</u>” section.</p></li>
<li><p>Updated the “<u>Using the Web Server Manager</u>” section for Patch XOBW*1.0*4.</p></li>
<li><p>Updated the “<u>Using SSL/TLS and Certificate-Based Authentication with HWSC</u>” section for Patch XOBW*1.0*4.</p></li>
<li><p>Converted Word document to .docx format.</p></li>
<li><p>Reformatted document to follow latest documentation standards and formatting rules. Also, formatted document for online presentation vs. print presentation (i.e., for double-sided printing). These changes include:</p></li>
</ul>
<ul>
<li><p>Revised section page setup.</p></li>
<li><p>Removed section headers.</p></li>
<li><p>Revised document footers.</p></li>
<li><p>Removed blank pages between sections.</p></li>
<li><p>Revised all heading style formatting.</p></li>
</ul>
<ul>
<li><p>Updated organizational references (e.g., “Product Development [PD]” to “Enterprise Program Management Office [EPMO]”).</p></li>
<li><p>Redacted document for the following information:</p></li>
</ul>
<ul>
<li><p>Names (replaced with role and initials).</p></li>
<li><p>Production IP addresses and ports.</p></li>
<li><p>VA Intranet websites.</p></li>
<li><p>Server geographic locations and node names.</p></li>
</ul></td>
<td>HealtheVet Web Services Client (HWSC) Project Team</td>
</tr>
<tr class="even">
<td>02/--/2011</td>
<td>1.0</td>
<td>HWSC Version 1.0 Initial release</td>
<td><p>Product Development Services Security Program HWSC development team.</p>
<ul>
<li><blockquote>
<p><mark>REDACTED</mark>.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref455581318" class="anchor"></span>Table : Documentation Symbol Descriptions

Table of Contents

<span id="_Toc456020164" class="anchor"></span>List of Figures

<span id="_Toc456020165" class="anchor"></span>List of Tables

# <span id="_Toc338740692" class="anchor"></span>Orientation


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [<span id="Toc338740692" class="anchor"></span>Orientation](#span-idtoc338740692-classanchorspanorientation)
- [Introduction](#introduction)
  - [HWSC Overview](#hwsc-overview)
    - [HWSC Features](#hwsc-features)
- [HWSC Management Functions](#hwsc-management-functions)
  - [Using the Web Server Manager](#using-the-web-server-manager)
  - [Using Web Service Manager](#using-web-service-manager)
  - [Using the Lookup Key Manager](#using-the-lookup-key-manager)
- [Security](#security)
  - [Using SSL/TLS and Certificate-Based Authentication with HWSC](#using-ssltls-and-certificate-based-authentication-with-hwsc)
  - [Securing a Web Service Using HTTP Basic Authentication](#securing-a-web-service-using-http-basic-authentication)
- [Troubleshooting](#troubleshooting)
  - [HWSC Availability Checking](#hwsc-availability-checking)
  - [Runtime Errors Due to Configuration Issues](#runtime-errors-due-to-configuration-issues)
    - [Caché Error \#5005: Cannot Open File](#caché-error-5005-cannot-open-file)
    - [zDelete Errors](#zdelete-errors)
- [# Appendix A—HWSC Error Codes](#appendix-ahwsc-error-codes)
How to Use this Manual
Throughout this manual, advice and instructions are offered regarding the use of the HealtheVet Web Services Client (HWSC) software and the functionality it provides for Veterans Information Systems and Technology Architecture (VistA).
Intended Audience
The intended audience of this manual is the following stakeholders:
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS)—Personnel who support Kernel-related products.
Disclaimers
Software Disclaimer
This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/002.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
Per VHA Directive 2004-038, this routine should not be modified
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).
Documentation Disclaimer
This manual provides an overall explanation of using Kernel; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) Enterprise Program Management Office (EPMO) Intranet Website.
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/004.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.
Documentation Conventions
This manual uses several methods to highlight different aspects of the material:
- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:
| Symbol                                                                                                                            | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/005.png)       | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/006.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |
<span id="_Ref455740092" class="anchor"></span>Table : Web Server Manager Actions
- Descriptive text is presented in a proportional font (as represented by this font).
- “Snapshots” of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and can be enclosed within a box.
- User’s responses to online prompts are boldface and (optionally) highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is boldface and (optionally) highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.
- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/008.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (i.e., CamelCase).
How to Obtain Technical Information Online
Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/009.png) NOTE: Methods of obtaining specific technical information online are indicated where applicable under the appropriate section.  
REF: See the *Kernel Technical Manual* for further information.
Help at Prompts
VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.
Obtaining Data Dictionary Listings
Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option \[DILIST\] on the Data Dictionary Utilities menu \[DI DDU\] in VA FileMan to print formatted data dictionaries.
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/010.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section in the *VA FileMan Advanced User Manual*.
Assumptions
This manual is written with the assumption that the reader is familiar with the following:
- VistA computing environment:
- Kernel 8.0—VistA M Server software
- Remote Procedure Call (RPC) Broker 1.1—VistA M Server software
- VA FileMan 22.0 (and higher) data structures and terminology—VistA M Server software
- VistALink 1.6—VistA M Server and Application Server software
- Linux or Microsoft<sup>®</sup> Windows environment
- Java Programming language:
- Java Integrated Development Environment (IDE)
- J2SE<sup>TM</sup> Development Kit (JDK)
- Java Authentication and Authorization Services (JAAS) programming
- M programming language
- WebLogic 9.2 or 10.x Application Server
Reference Materials
Readers who wish to learn more about HWSC should consult the following:
- *HWSC 1.0 Installation Guide*
- *HWSC 1.0 Systems Management Guide* (this manual)
- *HWSC 1.0 Developer’s Guide*
- *HWSC 1.0 Patch XOBW\*1.0\*4 Release Notes*
- *HWSC 1.0 Patch XOBW\*1.0\*4 Installation, Back-Out, and Rollback Guide*
- *HWSC 1.0 Patch XOBW\*1.0\*4 Security Configuration Guide*
VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>
VistA documentation can be downloaded from the VA Software Document Library (VDL): <http://www.va.gov/vdl/>
![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/011.png) REF: HWSC manuals are located on the VDL at: <http://www.va.gov/vdl/application.asp?appid=180>
VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HWSC Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HealtheVet Web Services Client (HWSC) uses Caché’s Web services client to invoke Web service methods on external servers and retrieve results. It provides helper methods and classes to improve the use of the Web service client in Veterans Health Information Systems and Technology Architecture (VistA).

### HWSC Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HWSC acts as an adjunct to the Web services client functionality provided in Caché, by:

- Leveraging Caché's platform-provided Web services client capabilities.
- Adding a file and user interface (UI) to manage the set of external Web server endpoints (IP, port, etc.)
- Adding a file and UI to register and manage the set of external Web services.
- Providing runtime application programming interface (API) to invoke a specific Web service on a specific Web server.
- Providing a runtime API to facilitate error processing in a VistA environment.
- Providing a deployment API to install/register a Web service proxy from a Web Services Description Language (WSDL) file.
- Providing a management UI including the ability to “ping” (test) a given Web service/server combination from VistA M.
- Supporting both Simple Object Access Protocol (SOAP)- and Representational State Transfer (REST)-style Web services.
- Fostering consistent implementation of VistA M Web service consumers.

# HWSC Management Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HealtheVet Web Services Client (HWSC) provides several management screens allowing you to create and manage the Web server and Web service information needed by VistA applications to consume external Web services. The management screens are:

- Web Server Manager
- Web Service Manager
- Lookup Key Manager

## Using the Web Server Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the XOBW WEB SERVER MANAGER option to call up the HWSC Web Server Manager. You should use this tool to enter Web server information.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/012.png) NOTE: Programmer access (DUZ(0)= “@”) is required to use this option.

<span id="_Toc456020184" class="anchor"></span>Figure : Using the XOBW WEB SERVER MANAGER Option

Web Server Manager Apr 18, 2007@16:07:54 Page: 1 of 1

HWSC Web Server Manager

Version: 1.0 Build: xx

ID Web Server Name IP Address or Domain Name:Port

1 \*Oakland Test Server1 vhaisxsysa.vha.med.va.gov:7111

2 \*Oakland Test Server2 vhaisxsysb.vha.med.va.gov:7112

3 \*Oakland Test Server3 vhaisxsysc.vha.med.va.gov:7113

4 \*Oakland Test Server4 vhaisxsysd.vha.med.va.gov:7114

Legend: \*Enabled

AS Add Server TS Test Server

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit//

<u>Table 2</u> summarizes the actions available in the Web Server Manager.

<table>
<caption><p><span id="_Ref455741133" class="anchor"></span>Table : Web Server Fields</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AS (Add Server)</td>
<td>Add a new entry in the WEB SERVER file (18.12).</td>
</tr>
<tr class="even">
<td>DS (Delete Server)</td>
<td>Delete an entry from the WEB SERVER file (18.12).</td>
</tr>
<tr class="odd">
<td>ES (Edit Server)</td>
<td>Edit an entry in the WEB SERVER file (18.12).</td>
</tr>
<tr class="even">
<td>EP (Expand Entry)</td>
<td>View all information about a particular entry in the WEB SERVER file (18.12).</td>
</tr>
<tr class="odd">
<td>TS (Test Server)</td>
<td><p>If the XOBT sample application is installed, it runs some of its tags to call sample external Web services. Disabled if the sample application (XOBT) is <em>not</em> installed.</p>
<p>![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/013.png) <strong>REF:</strong> For more information on the XOBT sample, see the <em>HWSC 1.0 Developer’s Guide</em>.</p></td>
</tr>
<tr class="even">
<td>WS (Web Service Manager)</td>
<td>Invoke the Web Service Manager screen.</td>
</tr>
<tr class="odd">
<td>CK (Check Web Service Availability)</td>
<td>Check availability for each Web service authorized/assigned to the Web server.</td>
</tr>
<tr class="even">
<td>LK (Lookup Key Manager)</td>
<td>Invoke the Lookup Key Manager screen.</td>
</tr>
</tbody>
</table>

<span id="_Ref455741133" class="anchor"></span>Table : Web Server Fields

When you add or edit a Web server, you are prompted for the information shown in <u>Table 3</u>.

| Field                | Description                                                                                                                                        |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Name                 | Name to identify the Web server entry. The name *must* be 3-30 characters in length.                                                               |
| Server               | The full domain name (for DNS) or IP address of the Web service server.                                                                            |
| Port                 | The TCP/IP port of Web service server.                                                                                                             |
| Default Http Timeout | A default http timeout to use for outgoing requests made to this server. The default value is 30.                                                  |
| Status               | Select either ENABLED or DISABLED.                                                                                                                 |
|                      | Security Credentials                                                                                                                           |
| Login Required?      | If a login is required, enter YES (allows editing of username and password).                                                                   |
| Username             | Name of the authorized user in the security realm on the Web server.                                                                               |
| Edit Password?       | Enter “Y” if you wish to change the password; otherwise, “N”.                                                                              |
|                      | SSL Setup                                                                                                                                      |
| SSL Enabled          | Determines whether SSL/TLS is enabled for the Web server.                                                                                          |
| SSL Configuration    | Name of Caché SSL configuration to use for this Web server.                                                                                        |
| SSL Port             | SSL port number to use for this Web server.                                                                                                        |
|                      | Authorize Web Services                                                                                                                         |
| Select Web Service   | Select one of the Web services listed, or enter a new one. A Web service *must* be “authorized” by entering here, to be used with this Web server. |
| Status               | Select ENABLED or DISABLED.                                                                                                                        |

<span id="_Ref455740705" class="anchor"></span>Table : Web Service Manager Actions

## Using Web Service Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Web Service Manager to enter or modify information for Web services that M applications access.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/014.png) NOTE: VistA applications that install Web service clients will probably automatically create Web service entries for the external Web services they are accessing.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/015.png) NOTE: Programmer access (DUZ(0)= “@”) is required to use this option.

To display the Web Service Manager, select the WS action in the Web Server Manager (see “[Using the Web Server Manager](#using-the-web-server-manager)”). In addition to adding a new service, you can edit or delete a previous entry, or display complete information previously entered for a particular service.

<span id="_Toc456020185" class="anchor"></span>Figure : Using Web Service Manager

Web Service Manager May 09, 2007@14:27:19 Page: 1 of 1

HWSC Web Service Manager

Version: 1.0 Build: xx

ID Web Service Name Type URL Context Root

1 XOBT TESTER REST SERVICE REST hwscrestservice

2 XOBT TESTER WEB SERVICE SOAP hwscwebservices/TesterWebService

Enter ?? for more actions

AS Add Service

ES Edit Service

DS Delete Service

EP Expand Entry

Select Action:Quit//

<u>Table 4</u> summarizes the actions available in the Web Service Manager.

| Action              | Description                                                                    |
|---------------------|--------------------------------------------------------------------------------|
| AS (Add Service)    | Add a new entry to the WEB SERVICE file (18.02).                               |
| DS (Delete Service) | Delete an entry from the WEB SERVICE file (18.02).                             |
| ES (Edit Service)   | Edit an entry in the WEB SERVICE file (18.02).                                 |
| EP (Expand Entry)   | View all information about a particular entry in the WEB SERVICE file (18.02). |

<span id="_Ref455741081" class="anchor"></span>Table : Web Service Fields

There are two types of Web services supported by HWSC:

- Representational State Transfer (REST)
- Simple Object Access Protocol (SOAP)

When you register a new Web service, you are prompted for slightly different information depending on the type, as shown in <u>Table 5</u>.

| Service Type | Field                 | Description                                                                                                                         |
|--------------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| REST     | Name                  | Name to identify the Web service entry. The name *must* be *non*-numeric, 3-30 characters long, and starting *without* punctuation. |
|              | Date Registered       | Date the entry was registered (created).                                                                                            |
|              | Service Type          | Choose REST.                                                                                                                    |
|              | Context Root          | The context root of the Web service.                                                                                                |
|              | Availability Resource | A “resource” to append to the context root to create a URL that can be used to check if the Web service is available.               |
| SOAP     | Name                  | Name to identify the Web service entry. The name *must* be *non*-numeric, 3-30 characters long, and starting *without* punctuation. |
|              | Date Registered       | Date the entry was registered (created).                                                                                            |
|              | Service Type          | Choose SOAP.                                                                                                                    |
|              | Proxy Class Name      | Name of the Caché Object class that is the Web service client proxy, as created by the Caché WSDL compiler.                         |
|              | Context Root          | The context root of the Web service.                                                                                                |
|              | Availability Resource | A “resource” to append to the context root to create a URL that can be used to check if the Web service is available.               |

<span id="_Ref455741798" class="anchor"></span>Table : Lookup Key Manager Actions

## Using the Lookup Key Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Lookup Key Manager is a tool for sites to use to associate a mnemonic name with a particular server. Applications use the mnemonic at runtime to retrieve the Web server.

<span id="_Toc456020186" class="anchor"></span>Figure : Using the Lookup Key Manager

Lookup Key Manager Apr 20, 2007@12:52:21 Page: 1 of 1

HWSC Web Server Lookup Key Manager

Version: 1.0 Build: xx

Filters: Key = \<no filter\> Server = \<no filter\>

ID Lookup Key Name \[Sorted By\] Web Server Name

1 XOBZ DEMO SERVER Oakland Test Server3

2 XOBZ ID SERVER Oakland Test Server1

3 XOBZ MESSAGE SERVER Oakland Test Server1

4 XOBZ PATIENT SERVER Oakland Test Server2

Enter ?? for more actions

AK Add Key SS Switch Sort

EK Edit Key FK Filter Key

DK Delete Key FS Filter Server

EP Expand Entry

Select Action:Quit//

<u>Table 6</u> summarizes the actions available in the Lookup Key Manager.

<table>
<caption><p><span id="_Ref455742051" class="anchor"></span>Table : Lookup Key Manager Fields</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Action</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AK (Add Key)</td>
<td>Add a new entry to the WEB SERVER LOOKUP KEY file (18.13).</td>
</tr>
<tr class="even">
<td>DK (Delete Key)</td>
<td>Delete an entry from the WEB SERVER LOOKUP KEY file (18.13).</td>
</tr>
<tr class="odd">
<td>EK (Edit Key)</td>
<td>Edit an entry in the WEB SERVER LOOKUP KEY file (18.13).</td>
</tr>
<tr class="even">
<td>EP (Expand Entry)</td>
<td>View all information about a particular entry in the WEB SERVER LOOKUP KEY (18.13).</td>
</tr>
<tr class="odd">
<td>FK (Filter Key)</td>
<td>Limit the list of lookup keys displayed by the key manager. The user specifies text to be used as a filter against the beginning characters of the key values. Only matching keys are listed. This protocol is also used to clear a key filter if one is currently being applied.</td>
</tr>
<tr class="even">
<td>FS (Filter Server)</td>
<td><p>Limit the list of Web server entries displayed by the key manager. The user specifies text to be used as a filter against the beginning characters of the key values. Only matching keys are listed.</p>
<p>This protocol is also used to clear a server filter if one is currently being applied.</p></td>
</tr>
<tr class="odd">
<td>SS (Switch Sort)</td>
<td>Switch sorting between “key” and “server” in the list of Web server lookup keys.</td>
</tr>
</tbody>
</table>

<span id="_Ref455742051" class="anchor"></span>Table : Lookup Key Manager Fields

When you enter a new lookup key, you are prompted for the information shown in <u>Table 7</u>.

| Field                      | Description                                                                                           |
|----------------------------|-------------------------------------------------------------------------------------------------------|
| Key Name                   | The name for the lookup key *must* be 3-30 characters in length.                                      |
| Brief Description          | The description *must* be 2-50 characters in length.                                                  |
| Associated Web Server Name | The WEB SERVER NAME with which to associate this key. Lookups made on the key return this Web server. |

<span id="_Ref455751322" class="anchor"></span>Table : HWSC Error Codes

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using SSL/TLS and Certificate-Based Authentication with HWSC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HealtheVet Web Services Client (HWSC) HyperText Transfer Protocol (HTTP) connections can be secured with Secure Socket Layer/Transport Layer Security (SSL/TLS). Doing so makes those connections much more secure, by encrypting the authentication handshake as well as the message contents.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/016.png) REF: For more information about using SSL/TLS (on Windows or Linux systems), contact the Help Desk and file a support ticket with the HWSC Product Support team.

In addition, HWSC supports two authentication mechanisms:

- HTTP Basic authentication
- Certificate-based authentication

As of Patch XOBW\*1.0\*4, HWSC enabled the use of Secure Socket Layer/Transport Layer Security (SSL/TLS) encryption and certificate-based authentication on OpenVMS systems. This allows VistA applications to make Hypertext Transfer Protocol (Secure) HTTP(S) connections from VistA to remote HTTP(S) servers. HWSC uses a Caché library that makes HTTP or HTTPS requests.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/017.png) REF: For more information and configuration setup instructions, see the *HWSC 1.0 Patch XOBW\*1.0\*4 Security Configuration Guide*.

## Securing a Web Service Using HTTP Basic Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To use HTTP Basic Authentication (with or without SSL/TLS), some setup is required. The J2EE and M server administrators need to perform the necessary steps for HTTP Basic Authentication:

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/018.png) REF: For more information and configuration setup instructions, see the *HWSC 1.0 Patch XOBW\*1.0\*4 Security Configuration Guide*.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HWSC Availability Checking

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Web Server Manager “Check Availability” action is probably the best tool to troubleshoot Web services problems. It is one way to test the validity of the Web server and Web service configuration; it lists all authorized/assigned Web services and tests each one individually.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/019.png) REF: For more information, see the “Supporting HWSC Availability Checking” section in the *HWSC 1.0 Developer’s Guide*.

Assuming that the Web service entry is set up with a valid “Availability Resource,” this option connects to the URL composed of the server, port, context root, and availability resource, and reports any errors encountered. Some examples are provided below for a few error types.

<span id="_Toc456020187" class="anchor"></span>Figure : Unsuccessful Availability Check—Listener Down

Web Service Availability May 18, 2007@11:46:56 Page: 1 of 1

Web Server:

4 \*VHAISXSYSA vhaisxsysa:7111

1 Unable to retrieve '?wsdl' for XOBT TESTER WEB SERVICE

o ERROR \#6059: Unable to open TCP/IP socket to server vhaisxsysa:7111

<span id="_Toc456020188" class="anchor"></span>Figure : Unsuccessful Availability Check—Authorization Failure; HTTP Error Code 401

Web Service Availability May 18, 2007@11:54:12 Page: 1 of 1

Web Server:

13 \* VHAISXSYSB vhaisxsysb:7111

1 Unable to retrieve '?wsdl' for XOBT TESTER WEB SERVICE

o HTTP Response Status Code: 401

2 Unable to retrieve '/available' for XOBT TESTER REST SERVICE

o HTTP Response Status Code: 401

<span id="_Toc456020189" class="anchor"></span>Figure : Successful Availability Check

Web Service Availability May 18, 2007@11:49:08 Page: 1 of 1

Web Server:

5 \*VHAISXSYSC vhaisxsysc:7111

1 XOBT TESTER WEB SERVICE is available

2 XOBT TESTER REST SERVICE is available

## Runtime Errors Due to Configuration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Caché Error \#5005: Cannot Open File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On VMS systems, the VMS accounts used by end-users *must* have RWED access to the directory used by Caché for creating temporary files. Otherwise, calls to external Web services made in a given end-user's process can fail. Runtime errors can be of the form:

- Cannot open file “WREK2XEPAXY.stream”  
    
  Or:
- ERROR \#5005: Cannot open file “TRMUAJZVAQT.stream”

Where “WREK2XEPAXY.stream” and “TRMUAJZVAQT.stream” are examples of randomly assigned temporary file names used by Caché.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/020.png) REF: For detailed information on how to address this issue, see the “Pre-Installation Preparation” section in the *HWSC 1.0 Installation Guide*.

### zDelete Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On VMS systems, VMS accounts used for end-user processes need to have adequate VMS process parameters (quotas). If VMS process parameters are *not* set to at least the minimum values *recommended* by InterSystems, calls to external Web services made in a given end-user's process can fail. Error messages can include the phrase:

"Error: *\<FUNCTION\>*zDelete^%ooLibrary.File.1"

This error is usually caused (at a lower level) by a VMS process quota exceeded error.

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/021.png) REF: For detailed information on how to address this issue, see the “Pre-Installation Preparation” section in the *HWSC 1.0 Installation Guide*.

# # Appendix A—HWSC Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Error code entries are contained in the DIALOG file (#.84). <u>Table 8</u> lists the dialog entries used in the HWSC software:

| Dialog Number | Short Description                     |
|---------------|---------------------------------------|
| 186001        | (reserved for future use)             |
| 186002        | Web Server Disabled                   |
| 186003        | Web Service not registered to server  |
| 186004        | Web Service disabled for Web server   |
| 186005        | Web Server not defined                |
| 186006        | Web Service not defined               |
| 186007        | Web Service is wrong type.            |
| 186008        | Invalid Server Lookup Key             |
| 186009        | Server Lookup Key Missing Association |

<span id="_Toc158103768" class="anchor"></span>

Glossary

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AA</td>
<td>Authentication and Authorization.</td>
</tr>
<tr class="even">
<td>Business Delegate</td>
<td>A business delegate acts as a representative of the client components and is responsible for hiding the underlying implementation details of the business service. It knows how to look up and access the business services.</td>
</tr>
<tr class="odd">
<td>Certificate Authority (CA)</td>
<td><p>"A certificate authority (CA) is an entity that creates and then 'signs' a document or file containing the name of a user and his public key. Anyone can verify that the file was signed by no one other than the CA by using the public key of the CA. By trusting the CA, one can develop trust in a user's public key.</p>
<p>The trust in the certification authority's public key can be obtained recursively. One can have a certificate containing the certification authority's public key signed by a superior certification authority (Root CA) that he already trusts. Ultimately, one need only trust the public keys of a small number of top-level certification authorities. Through a chain of certificates (Sub CAs), trust in a large number of users' signatures can be established.</p>
<p>A broader application of digital certification includes not only name and public key but also other information. Such a combination, together with a signature, forms an extended certificate. The other information may include, for example, electronic-mail address, authorization to sign documents of a given value, or authorization to sign other certificates."<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></p>
<p>Currently, the Department of Veterans Affairs (VA) uses VeriSign, Inc. as the Certificate Authority (CA).</p></td>
</tr>
<tr class="even">
<td>Cryptography</td>
<td>The system or method used to write or decipher messages in code (see "Encryption" and "Decryption").</td>
</tr>
<tr class="odd">
<td>CSR</td>
<td>Certificate Signing Request.</td>
</tr>
<tr class="even">
<td>Decryption</td>
<td>Using a secret key to unscramble data or messages previously encrypted with a cipher or code so that they are readable. In some cases, encryption algorithms are one directional (i.e., they only encode and the resulting data cannot be unscrambled).</td>
</tr>
<tr class="odd">
<td>Encryption</td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases, encryption algorithms are one directional (i.e., they only encode and the resulting data cannot be unscrambled).</td>
</tr>
<tr class="even">
<td>HTTP Protocol</td>
<td>Hyper Text Transfer Protocol is the underlying protocol used by the World Wide Web. HTTP defines how messages are formatted and transmitted, and what actions Web servers and browsers should take in response to various commands.</td>
</tr>
<tr class="odd">
<td>HWSC</td>
<td>Health<u>e</u>Vet Web Services Client is a support framework that offers VistA/M applications real-time, synchronous client access to n-tier (J2EE) Web services through the supplied M-based and Caché APIs.</td>
</tr>
<tr class="even">
<td>Intermediate CA</td>
<td>Intermediate Certificate Authority. Currently, the Department of Veterans Affairs (VA) uses VeriSign, Inc. as the Certificate Authority (CA). VeriSign requires the use of a CA Intermediate Certificate. The CA Intermediate Certificate is used to sign the peer's (server) certificate. This provides another level of validation-managed PKI for SSL.</td>
</tr>
<tr class="odd">
<td>J2EE</td>
<td>The Java 2 Platform, Enterprise Edition (J2EE) defines the standard for developing multi-tier enterprise applications. J2EE defines components that function independently, that can be deployed on servers, and that can be invoked by remote clients. The J2EE platform is a set of standard technologies and is not itself a language. The current J2EE platform is version 1.4.</td>
</tr>
<tr class="even">
<td>PKI</td>
<td><p>Public Key Infrastructure technology adds the following security services to an electronic ordering system:</p>
<ul>
<li><p>Confidentiality—only authorized persons have access to data.</p></li>
<li><p>Authentication—establishes who is sending/receiving data.</p></li>
<li><p>Integrity—the data has not been altered in transmission.</p></li>
<li><p><em>Non</em>-repudiation—parties to a transaction cannot convincingly deny having participated in the transaction.<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></p></li>
</ul></td>
</tr>
<tr class="odd">
<td>Private Certificate</td>
<td>This is the certificate that contains both the user's public and private keys. This certificate resides on a smart card.</td>
</tr>
<tr class="even">
<td>Public Certificate</td>
<td>This is the certificate that contains the user's public key. This certificate resides in a file or database.</td>
</tr>
<tr class="odd">
<td>REST</td>
<td>Representational State Transfer (REST) is an architectural style for simplified Web services, based on accessing resources via HTTP.</td>
</tr>
<tr class="even">
<td>Root CA</td>
<td><p>Root Certificate Authority. In cryptography and computer security, a root certificate is an unsigned public key certificate, or a self-signed certificate, and is part of a public key infrastructure scheme. The most common commercial variety is based on the ITU-T X.509 standard. Normally an X.509 certificate includes a digital signature from a Certificate Authority (CA), which vouches for correctness of the data contained in a certificate. Root certificates are implicitly trusted.</p>
<p>Currently, the Department of Veterans Affairs (VA) uses VeriSign, Inc. as the Certificate Authority (CA).</p></td>
</tr>
<tr class="odd">
<td>Service Facade</td>
<td>The Service Façade acts as the server-side bridge between the Business Delegate and the capability. The Service Façade is responsible for taking a request from the delegate and doing any translation necessary to invoke the capability and provide the response to the delegate.</td>
</tr>
<tr class="even">
<td>Servlet Container</td>
<td><p>A servlet is managed by a servlet container (formerly referred to as servlet engine.) The servlet container is responsible for loading and instantiating the servlets and then calling <a href="http://www.adp-gmbh.ch/java/servlets/interface.html#init">init()</a>. When a request is received by the servlet container, it decides what servlet to call in accordance with a configuration file. A famous example of a servlet container is <a href="http://jakarta.apache.org/tomcat/">Tomcat</a>.</p>
<p>The servlet Container calls the servlet's <a href="http://www.adp-gmbh.ch/java/servlets/interface.html#service">service()</a> method and passes an instance of ServletRequest and ServletResponse. Depending on the <a href="http://www.adp-gmbh.ch/web/http/methods.html">request's method</a> (mostly GET and POST), service calls doGet() or doPost(). These passed instances can be used by the servlet to find out who the remote user is, if and what <a href="http://www.adp-gmbh.ch/web/http/methods.html#post">HTTP POST</a> parameters have been set and other characteristics.</p>
<p>Together with the Web server (or application server) the servlet container provides the HTTP interface to the world.</p>
<p>It is also possible for a servlet container to run standalone (without Web server), or to even run on a host other than the Web server. <a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></p></td>
</tr>
<tr class="odd">
<td>Signed Certificate</td>
<td>The Signed Certificate (a.k.a. self-signed certificate) is the peer's (server) digital certificate. Currently, the Department of Veterans Affairs (VA) uses VeriSign, Inc. as the Certificate Authority (CA) to sign (validate) digital certificates. VeriSign, Inc. requires the use of CA Root and Intermediate Certificates. The Subject and Issuer have the same content when signed by VeriSign; the issuer has VeriSign's content.</td>
</tr>
<tr class="even">
<td>SOAP</td>
<td>Simple Object Access Protocol (SOAP) is a protocol for exchanging structured information over a network, often via HTTP.</td>
</tr>
<tr class="odd">
<td>SSL</td>
<td>Secure Socket Layer. A low-level protocol that enables secure communications between a server and a browser. It provides communication privacy.</td>
</tr>
<tr class="even">
<td>TLS</td>
<td>Transport Layer Security. Transport Layer Security (TLS) and its predecessor, Secure Sockets Layer (SSL), are cryptographic protocols which provide secure communications on the Internet for such things as Web browsing, e-mail, Internet faxing, instant messaging and other data transfers. There are slight differences between SSL 3.0 and TLS 1.0, but the protocol remains substantially the same.</td>
</tr>
<tr class="odd">
<td>Web Service</td>
<td>A Web resource meant to be consumed over a network via HTTP, by an autonomous program.</td>
</tr>
<tr class="even">
<td>WebLogic</td>
<td>An Oracle<sup>®</sup> product; WebLogic Server 8.1, 9.2, and 10.x is a J2EE- v1.3-certified application server for developing and deploying J2EE enterprise applications.</td>
</tr>
<tr class="odd">
<td>WSDL</td>
<td><p>Web Services Definition Language. “WSDL is an <a href="http://en.wikipedia.org/wiki/XML">XML</a>-based service description on how to communicate using <a href="http://en.wikipedia.org/wiki/Web_services">Web services</a>. The WSDL defines services as collections of network endpoints, or ports. WSDL specification provides an <a href="http://en.wikipedia.org/wiki/XML">XML</a> <a href="http://en.wikipedia.org/wiki/Format">format</a> for documents for this purpose.</p>
<p>The abstract definition of ports and messages is separated from their concrete use or instance, allowing the reuse of these definitions. A port is defined by associating a network address with a reusable binding, and a collection of ports define a service. Messages are abstract descriptions of the data being exchanged, and port types are abstract collections of supported operations. The concrete protocol and data format specifications for a particular port type constitutes a reusable binding, where the messages and operations are then bound to a concrete network protocol and message format. In this way, WSDL describes the public interface to the Web service.</p>
<p>WSDL is often used in combination with <a href="http://en.wikipedia.org/wiki/SOAP">SOAP</a> and <a href="http://en.wikipedia.org/wiki/XML_Schema">XML Schema</a> to provide Web services over the <a href="http://en.wikipedia.org/wiki/Internet">Internet</a>. A client program connecting to a Web service can read the WSDL to determine what functions are available on the server. Any special <a href="http://en.wikipedia.org/wiki/Datatypes">datatypes</a> used are embedded in the WSDL file in the form of XML Schema. The client can then use SOAP to actually call one of the functions listed in the WSDL.”<a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></p></td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>DEA website (<a href="http://www.deadiversion.usdoj.gov/ecomm/csos/archive/conops.pdf">http://www.deadiversion.usdoj.gov/ecomm/csos/archive/conops.pdf</a>): “Public Key Infrastructure Analysis Concept of Operations,” Section 3.4.3 “Public Key - The I in PKI.”<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>DEA Web site (<a href="http://www.deadiversion.usdoj.gov/ecomm/csos/archive/conops.pdf">http://www.deadiversion.usdoj.gov/ecomm/csos/archive/conops.pdf</a>): “Public Key Infrastructure Analysis Concept of Operations,” Section 3.3 “Security.”<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>From the <em>ADP –Analyse, Design &amp; Programing GmbH</em> website:</p>
<p><a href="http://www.adp-gmbh.ch/java/servlets/container.html">http://www.adp-gmbh.ch/java/servlets/container.html</a><a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p><a href="http://en.wikipedia.org/wiki/Web_Services_Description_Language">http://en.wikipedia.org/wiki/Web_Services_Description_Language</a><a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

![](healthevet-web-services-client-hwsc-version-1-systems-management-guide/022.png) REF: For a list of commonly used terms and definitions, see the OI&T Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.