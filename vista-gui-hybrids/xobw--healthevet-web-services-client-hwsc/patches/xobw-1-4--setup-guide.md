---
title: XOBW*1*4 Security Configuration Guide
doc_type: CFG
doc_label: Configuration Guide
doc_layer: patch
doc_subject: Security
app_code: XOBW
app_name: HealtheVet Web Services Client (HWSC)
section: GUI
app_status: active
pkg_ns: XOBW
patch_ver: 1
patch_id: XOBW*1*4
group_key: "XOBW:XOBW:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - security
  - configuration
  - server
  - table
  - contents
  - client
  - xobw
  - authentication
  - vista
  - guide
page_count: 0
word_count: 4842
section_count: 16
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2017
revision_count: 2
revision_newest: 02/15/2017
revision_oldest: 10/20/2016
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p4_scg.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p4_scg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=180"
---

---
title: |
  HealtheVet Web Services Client (HWSC) 1.0  
  Patch XOBW\*1.0\*4

  Security Configuration Guide
---

![](xobw-1-4-security-configuration-guide/001.png)

February 2017

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

<span id="_Toc455656205" class="anchor"></span>Revision History

| Date       | Version | Description                                                                            | Author                                             |
|------------|---------|----------------------------------------------------------------------------------------|----------------------------------------------------|
| 02/15/2017 | 1.1     | Corrected <u>Figure 3</u> to reflect the SSLv3 check box is checked.                   | HealtheVet Web Services Client (HWSC) Project Team |
| 10/20/2016 | 1.0     | Initial document created for HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4. | HealtheVet Web Services Client (HWSC) Project Team |

Table : Documentation symbol descriptions

Table of Contents

<span id="_Toc455656206" class="anchor"></span>List of Figures

<span id="_Toc453151200" class="anchor"></span>Orientation

How to Use this Manual

The Security Configuration Guide defines the ordered, technical steps required to configure the product.

Throughout this manual, advice and instructions are offered regarding the use of the HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> Patch XOBW\*1.0\*4 software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Information Resource Management (IRM)—System administrators and Capacity Management personnel at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation Disclaimer

This manual provides an overall explanation of using the HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> Patch XOBW\*1.0\*4 software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) Enterprise Program Management Office (EPMO) Intranet Website.

![](xobw-1-4-security-configuration-guide/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](xobw-1-4-security-configuration-guide/003.png)         | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](xobw-1-4-security-configuration-guide/004.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

- Descriptive text is presented in a proportional font (as represented by this font).
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xobw-1-4-security-configuration-guide/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](xobw-1-4-security-configuration-guide/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

You can now use these Back and Forward command buttons in the Toolbar to navigate back and forth in the Word document when selecting hyperlinks within the document.

![](xobw-1-4-security-configuration-guide/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xobw-1-4-security-configuration-guide/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). Use the List File Attributes option on the Data Dictionary Utilities menu in VA FileMan to print formatted data dictionaries.

![](xobw-1-4-security-configuration-guide/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about HealtheVet Web Services Client (HWSC) should consult the following:

- *HWSC 1.0 Patch XOBW\*1.0 \*4 Release Notes*
- *HWSC 1.0 Patch XOBW\*1.0 \*4 Installation, Back-Out, and Rollback Guide*
- *HWSC 1.0 Patch XOBW\*1.0 \*4 Security Configuration Guide* (this manual)
- *HWSC 1.0 Installation Guide*
- *HWSC 1.0 Systems Management Guide*
- *HWSC 1.0 Developer’s Guide*

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL): <http://www.va.gov/vdl/>

![](xobw-1-4-security-configuration-guide/010.png) REF: See the [HealtheVet Web Services Client (HWSC) manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=180).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Background](#background)
    - [Current Functionality](#current-functionality)
    - [Proposed Functionality](#proposed-functionality)
  - [Purpose](#purpose)
  - [Transport Layer Security Concepts](#transport-layer-security-concepts)
  - [HTTP Basic Authentication](#http-basic-authentication)
  - [Web Service Security](#web-service-security)
  - [VistA Environment](#vista-environment)
  - [SSL/TLS Configuration in VistA](#ssltls-configuration-in-vista)
  - [Configuration Recommendations](#configuration-recommendations)
- [Encryption-Only Setup](#encryption-only-setup)
  - [Server-Side](#server-side)
  - [Client-Side](#client-side)
  - [Potential Errors](#potential-errors)
- [HTTP Basic Authentication Configuration](#http-basic-authentication-configuration)
  - [Server-Side](#server-side-1)
    - [Security Realm Configuration](#security-realm-configuration)
    - [Create Security Realms Group](#create-security-realms-group)
    - [web.xml File Configuration](#webxml-file-configuration)
    - [weblogic.xml File Configuration](#weblogicxml-file-configuration)
  - [Client-Side](#client-side-1)
    - [Web Server File (#18.12) Configuration](#web-server-file-1812-configuration)
- [Client Certificate Authentication Configuration](#client-certificate-authentication-configuration)
  - [Server-Side](#server-side-2)
    - [Security Realm Configuration](#security-realm-configuration-1)
    - [SSL Client Behavior Configuration](#ssl-client-behavior-configuration)
    - [web.xml File Configuration](#webxml-file-configuration-1)
    - [Edit the Authentication Method](#edit-the-authentication-method)
    - [weblogic.xml File Configuration](#weblogicxml-file-configuration-1)
  - [Client-Side](#client-side-2)
    - [SSL/TLS Configuration](#ssltls-configuration)
    - [VistA Client Private Key and Certificate](#vista-client-private-key-and-certificate)
    - [Testing the SSL/TLS Configuration](#testing-the-ssltls-configuration)
HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4 enables the use of Secure Socket Layer/Transport Layer Security (SSL/TLS) on OpenVMS systems.

## Background

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HWSC software allows Veterans Health Information Systems and Technology Architecture (VistA) applications to make Hypertext Transfer Protocol (Secure) HTTP(S) connections from Veterans Health Information Systems and Technology Architecture (VistA) to remote HTTP(S) servers. HWSC uses a Caché library that makes HTTP or HTTPS requests.

On the initial deployment of HWSC (seven years ago), it was decided to disable the use of HTTPS secure connections from VistA due to a memory leak issue with VMS. The remote servers are capable of hosting their servers using HTTPS; however, due to this issue they are hosting them as HTTP.

### Current Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HWSC with SSL/TLS (HTTPS) works with other operating systems (i.e., Linux and Windows), but applications like Master Patient Index (MPI) have been forced to use HWSC *without* SSL/TLS (HTTPS). <u>Figure 1</u> illustrates the current connection pathway using HTTP.

<span id="_Ref450831270" class="anchor"></span>Figure : HWSC HTTP Connection—Current Functionality

![](xobw-1-4-security-configuration-guide/011.png)

### Proposed Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Enabling SSL/TLS on OpenVMS systems allows applications to use SSL/TLS consistently throughout the VA system. <u>Figure 2</u> illustrates the proposed connection pathway using HTTPS.

<span id="_Ref450831012" class="anchor"></span>Figure : HWSC and with HTTPS Connection—Proposed Functionality

![](xobw-1-4-security-configuration-guide/012.png)

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this guide is to describe the configuration setup needed by VistA applications when using HWSC as a Web service client to secure its communication.

Since the proper configuration of a Web service client depends on the configuration of the corresponding remote Web service, minimal instructions are also provided for Web services hosted in a Java EE application server (WebLogic).

The configuration instructions are written for the following environments:

- Client-Side—Describes configuration instructions for HWSC-based VistA applications.
- Server-Side—Describes configuration instructions for typical systems currently in use at the VA (WebLogic Java EE application server).

It is *recommended* that VistA system administrators focus on the “Client-Side” sections and system administrators who manage Java EE applications (e.g., Oracle<sup>®</sup> WebLogic) focus on the “Server-Side” sections.

## Transport Layer Security Concepts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transport Layer Security (TLS) protocol allows applications to communicate across a network in a secure manner that prevents eavesdropping, tampering, and message forgery. It can be used for securing (by encryption) communication between network clients and network servers; and for authentication of the network client, network server, or both.

TLS authentication can use public key infrastructure (PKI) certificates to identify network clients and network servers.

This configuration guide provides instructions on setting up encrypted connections with or without certificates for authenticating network clients. The instructions can be extended if an application opts to also authenticate the network server (mutual authentication). A configuration that does *not* use certificates for authentication is called an encryption-only configuration.

## HTTP Basic Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authentication of network clients can also be achieved at the Network Application Layer, as is done in the HTTP protocol with HTTP Basic Authentication. This requires the use of a username and password credentials to be set up by the network server and its network clients. The use of HTTP Basic Authentication *must* encrypt its communication to protect the credentials. It is *recommended* that applications using HTTP Basic Authentication also configure their applications with encryption-only configuration.

This configuration guide provides instructions on setting up HTTP Basic Authentication for authenticating network clients.

## Web Service Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although there is a standard Web Service Security (WS-Security) for Simple Object Access Protocol (SOAP) Web services, at the time that the HWSC software was developed and released, the implementation of WS-Security in Caché was *not* fully implemented. Also, HWSC is used for implementing Representational State Transfer (REST)-based Web service clients for which WS-Security is *not* used.

![](xobw-1-4-security-configuration-guide/013.png) REF: For alternatives to WS-Security, see the “<u>Configuration Recommendations</u>” section.

## VistA Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA applications are hosted in a Caché environment that may contain a cluster of one or more computer nodes. The basic topology is split into a set of Front-End nodes and a set of Back-End nodes (database nodes). For a small site, a single computer node may serve as both. For larger sites, the number of Front-End and Back-End nodes can vary.

## SSL/TLS Configuration in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main configuration artifact in a Caché system is an SSL/TLS configuration that VistA applications need to reference in their code.

## Configuration Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *recommended* that the following configurations be chosen, in order of complexity:

1.  Encryption-Only (see the “<u>Encryption-Only Setup</u>” section) with HTTP Basic Authentication (see the “<u>HTTP Basic Authentication Configuration</u>” section).  
      
    Or:
2.  Client Certificate Authentication (see the “<u>HTTP Basic Authentication Configuration</u>” section).

# Encryption-Only Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server-Side

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions are written for Oracle<sup>®</sup> WebLogic (WL) 8.1 to 10.3.6 Application Server.

![](xobw-1-4-security-configuration-guide/014.png) NOTE: Other versions should have a similar path to the configuration.

Set up a WL server to use default settings for /Secure Socket Layer (SSL):

1.  In the WebLogic Admin Console, navigate to:

Servers *\<myserver\>* Configuration-General

The *\<myserver\>* name depends on your installation.

2.  Check the SSL Listen Port Enabled option.
3.  In the same page, enter a port number in the SSL Listen Port text field (e.g., 7002).
4.  Save the changes.
5.  Restart the server.
6.  Ensure that the SSL listen port is now active.

## Client-Side

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions are written for Caché 2014.1.3 M Server.

![](xobw-1-4-security-configuration-guide/015.png) NOTE: Patch XOBW\*1.0\*4 installs an SSL/TLS configuration named “encrypt_only” in all nodes of a Caché system. You can use the Caché System Management Portal to view the SSL/TLS configuration in the node where the Management Portal is hosted.

You can view and test the SSL/TLS configuration by using the Caché System Management Portal.

1.  Locate the SSL/TLS configuration in the Caché System Management Portal.

System Administration Security SSL/TLS Configuration

7.  From the list of SSL/TLS configurations, select the “encrypt_only” choice by clicking the edit link.

> <span id="_Ref474921228" class="anchor"></span>Figure : Encryption-Only Setup—SSL/TLS configuration: Client-Side

> ![](xobw-1-4-security-configuration-guide/016.png)

8.  Select the Test button to start testing the SSL/TLS configuration. You are prompted for the following information:
- Test server host name or IP address—This is the server-side server configured in the “<u>Server-Side</u>” section. For example:

> <span id="_Toc455656245" class="anchor"></span>Figure : Encryption-Only Setup—SSL/TLS Configuration Test: Server Host Name or IP Address

> ![](xobw-1-4-security-configuration-guide/017.png)

- Test server port—This is the SSL port configured on the server-side server configured in the “<u>Server-Side</u>” section. For example:

> <span id="_Toc455656246" class="anchor"></span>Figure : Encryption-Only Setup—SSL/TLS Configuration Test: Server Port

> ![](xobw-1-4-security-configuration-guide/018.png)

9.  You should see the following or similar information:

> <span id="_Toc455656247" class="anchor"></span>Figure : Encryption-Only Setup—SSL/TLS configuration Test: Sample Results

> ![](xobw-1-4-security-configuration-guide/019.png)

10. You are now ready, and can reference the “encrypt_only” SSL configuration in your WEB SERVER entry:

> <span id="_Toc455656248" class="anchor"></span>Figure : Encryption-Only Setup—SSL/TLS configuration Test: encrypt_only WEB SERVER Entry

> SSL ENABLED: TRUE

> SSL CONFIGURATION: encrypt_only

> SSL PORT: 7002

## Potential Errors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may encounter errors while testing the configuration. Some of the errors are listed below:

1.  Ensure to enter the correct remote server host name or IP address.
11. Ensure to enter the correct remote server port number.
12. Ensure that your server and client systems are up to date with their use of SSL/TLS libraries.

![](xobw-1-4-security-configuration-guide/020.png) NOTE: In testing it was found that a Veterans Health Information Systems and Technology Architecture (VistA) system running on Linux could *not* establish an SSL session with an older WebLogic Application Server.

# HTTP Basic Authentication Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server-Side

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enable the Web Services application to use Hypertext Transfer Protocol (HTTP) Basic Authentication you *must* have the following elements defined on the Java EE Application Server:

- A Security Realm User.
- A Security Realm Group.
- web.xml for the Web Services application.
- weblogic.xml for the Web Services application.

This allows a Veterans Health Information Systems and Technology Architecture (VistA) M Server Client to be registered in the JAVA EE Application Server hosting the Web Services application.

### Security Realm Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a user and group in the default security realm.

### Create Security Realms Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a security realms group that is given the role and privilege to invoke Web Services in the JAVA EE Application Server (e.g., XOBW_Server_Proxies).

#### Create Security Realms User

Create the user that is mapped to the username and password submitted by the client:

- USER—The name of the user to be mapped to the username in the security realm (e.g., wsuser)
- PASSWORD—The user's password to be mapped to the password in the security realm (e.g., changeit). The password *must* be kept secret and shared only to those clients allowed to invoke your Web Service.

![](xobw-1-4-security-configuration-guide/021.png) NOTE: Coordinate with the person responsible for the VistA M Server Client—they need to know the values to be used as username and password in their implementation of HTTP Basic Authentication.

#### Assign User to the Security Realms Group

Assign the user created (e.g., wsuser) to the security realms group (e.g., XOBW_Server_Proxies).

### web.xml File Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Configure the Web Services application’s web.xml file in order to use HTTP Basic Authentication.

#### Edit the Authentication Method

Edit the \<auth-method\> tag under the \<login-config\> tag in the web.xml file. For HTTP Basic Authentication, use BASIC as the authentication method, as shown in <u>Figure 8</u>:

<span id="_Ref450742026" class="anchor"></span>Figure : Application Server—Edit the web.xml file to use BASIC authentication method

\<login-config\>

\<auth-method\>BASIC\</auth-method\>

\</login-config\>

#### Define Web Services Security Roles and Constraints

Edit the following tags in the web.xml file:

- Edit the \<role-name\> tag under the \<auth-constraint\> tag under the \<security constraint\> tag to reference your Web Services security role.
- Edit the \<role-name\> tag under the \<security-role\> tag to reference your Web Services security role.

For example, use XOBW_Server_Proxies as the Web Services security role:

<span id="_Toc455656250" class="anchor"></span>Figure : Application Server—Edit the web.xml file to define security roles and constraints

\<security-constraint\>

. . .

\<web-resource-collection\>

. .

\</web-resource-collection\>

\<auth-constraint\>

\<description\>These are the roles who have access\</description\>

\<role-name\>XOBW_Server_Proxies\</role-name\>

\</auth-constraint\>

. . .

\</security-constraint

\<security-role\>

\<role-name\>XOBW_Server_Proxies\</role-name\>

\</security-role\>

### weblogic.xml File Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Configure the application's weblogic.xml file in order to use HTTP Basic Authentication.

#### Define Web Services Security Roles to be Mapped to the Security Realm's Principal

Define any security roles that *must* be mapped to the Oracle WebLogic JAVA EE Application Server security realm's Principal. For example, use XOBW_Server_Proxies as the group (Principal):

<span id="_Toc455656251" class="anchor"></span>Figure : Application Server—Defining security roles mapped to security realm's principal in the weblogic.xml file

\<security-role-assignment\>

\<role-name\>XOBW_Server_Proxies\</role-name\>

\<principal-name\>XOBW_Server_Proxies\</principal-name\>

\</security-role-assignment\>

## Client-Side

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enable your VistA M Server Client to use HTTP Basic Authentication security, you *must* have an entry in the WEB SERVER file (#18.12)

### Web Server File (#18.12) Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Follow the instructions in Section 2 in the [*HWSC Developer's Guide*](http://www.va.gov/vdl/documents/HealtheVet/HealtheVet_Web_Services_Client/xobw1_0dg.pdf) when creating an entry in the WEB SERVER file (#18.12). The following fields *must* be defined to enable HTTP Basic Authentication security:

- STATUS: ENABLED
- LOGIN REQUIRED: YES
- USERNAME: *\<wsuser\>*
- PASSWORD: *\<Hidden\>*

![](xobw-1-4-security-configuration-guide/022.png) NOTE: Username *\<wsuser\>* is just an example. You *must* obtain the values for the USERNAME and PASSWORD from the person responsible for the J2EE Application Server hosting the corresponding Web Service.

# Client Certificate Authentication Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server-Side

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enable the Web Services application to use Client Certificate Authentication you *must* have the following elements defined on the remote Web server. For example a Java EE Application Server (JEE):

A user that corresponds to the CN of the Caché system.

In a JEE server this corresponds to:

- Security Realm User for the Caché system
- Security Realm Group
- Security Realm DefaultIdentityAsserter
- SSL Configuration to require client certificates
- web.xml file for the Web Services application
- weblogic.xml file for the Web Services application

This allows a Veterans Health Information Systems and Technology Architecture (VistA) M Server Client to be registered in the remote server hosting the Web Services application.

Additional details for setting up the server-side are described in the sections that follow.

### Security Realm Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a user and group in the default security realm.

#### Create Security Realms Group

Create a security realms group that is given the role and privilege to invoke Web Services in the JAVA EE Application Server (e.g., XOBW_Server_Proxies).

#### Create Security Realms User

Create the user that is mapped to the CN of the client certificate (e.g., a1.fo-oakland.med.va.gov)

- USER—The Domain Name Service (DNS) name of the host server (e.g., a1.fo-oakland.med.va.gov)
- PASSWORD—The password can be anything the user chooses, since it is never shared with anyone, not even the client user.

![](xobw-1-4-security-configuration-guide/023.png) NOTE: Coordinate with the person responsible for the VistA Caché Server Client, they can give you their signed public key digital certificate for you to look at it, or you can ask them for the contents of the Common Name (CN) field.

#### Assign User to the Security Realms Group

Assign the user created (e.g., a1.fo-oakland.med.va.gov) to the security realms group (e.g., XOBW_Server_Proxies).

#### Edit Security Realm DefaultIdentityAsserter

Add and edit the security realm's DefaultIdentityAsserter properties with the following values:

- Types: X.509
- Default User Name Mapper: Enable
- Default User Name Mapper Attribute Type: CN
- Default User Name Mapper Attribute Delimiter: (Leave Blank)

### SSL Client Behavior Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make sure that your JEE Application Server is already enabled for SSL connectivity. For Client Certificate Authentication to work, the Two Way Client Cert Behavior property *must* be set to "Client Certs Requested And Enforced," which is the most restrictive.

### web.xml File Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Configure the Web Services application’s web.xml file in order to use Client Certificate Authentication.

### Edit the Authentication Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Edit the \<auth-method\> tag under the \<login-config\> tag in the web.xml file. For Client Certificate Authentication, use BASIC as the authentication method, as shown in <u>Figure 11</u>:

<span id="_Ref450743194" class="anchor"></span>Figure : Application Server—Edit the web.xml file to use CLIENT-CERT authentication method

\<login-config\>

\<auth-method\>CLIENT-CERT\</auth-method\>

\</login-config\>

#### Define Web Services Security Roles and Constraints

Edit the following tags in the web.xml file:

- Edit the \<role-name\> tag under the \<auth-constraint\> tag under the \<security constraint\> tag to reference your Web Services security role.
- Edit the \<role-name\> tag under the \<security-role\> tag to reference your Web Services security role.

For example, use XOBW_Server_Proxies as the Web Services security role:

<span id="_Toc455656253" class="anchor"></span>Figure : Application Server—Edit the web.xml file to define security roles and constraints

\<security-constraint\>

. . .

\<web-resource-collection\>

. .

\</web-resource-collection\>

\<auth-constraint\>

\<description\>These are the roles who have access\</description\>

\<role-name\>XOBW_Server_Proxies\</role-name\>

\</auth-constraint\>

. . .

\</security-constraint

\<security-role\>

\<role-name\>XOBW_Server_Proxies\</role-name\>

\</security-role\>

### weblogic.xml File Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Configure the application's weblogic.xml file in order to use Client Certificate Authentication.

#### Define Web Services Security Roles to be Mapped to the Security Realm's Principal

Define any security roles that *must* be mapped to the Oracle WebLogic JAVA EE Application Server security realm's Principal. For example, use XOBW_Server_Proxies as the group (Principal):

<span id="_Toc455656254" class="anchor"></span>Figure : Application Server—Defining security roles mapped to security realm's principal in the weblogic.xml file

\<security-role-assignment\>

\<role-name\>XOBW_Server_Proxies\</role-name\>

\<principal-name\>XOBW_Server_Proxies\</principal-name\>

\</security-role-assignment\>

## Client-Side

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions are written for Caché version 2014.1.3 or later.

### SSL/TLS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your VistA system administrator needs to create an SSL/TLS configuration in the Caché System Management Portal similar to the example in <u>Figure 14</u>. Also, in systems that have more than one node, the configuration needs to be created in all nodes.

<span id="_Ref455655729" class="anchor"></span>Figure : Client Certificate Authentication Configuration—SSL/TLS Configuration

![](xobw-1-4-security-configuration-guide/024.png)

The SSL/TLS Configuration requires two files: The Caché system’s identity certificate; and the corresponding Caché system’s private key. Your Caché system is identified by its CN value in the certificate. Make note of it.

![](xobw-1-4-security-configuration-guide/025.png) NOTE: Typical system certificates are issued for the purpose of identifying a server, your Caché system is used as the client; therefore, make sure that you request your certificate for the purpose of client as well.

### VistA Client Private Key and Certificate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create the necessary private key file and corresponding digital certificate from the VA’s site:

1.  To start the VA PKI SSL request process, browse to the following location:

http://vaww.pki.va.gov/ssltls/

![](xobw-1-4-security-configuration-guide/026.png) REF: Be sure to read the “Request Process” section on that Web page.

13. Obtain a digital certificate for your VistA server and the corresponding private key; these files are used as the client certificate and the client private key respectively.
14. Make a note of the CN field value in the certificate. In this example, the CN is defined for a VistA server identified as follows:

CN=a1.fo-oakland.med.va.gov

![](xobw-1-4-security-configuration-guide/027.png) NOTE: This name is used by the remote Web service server to identify a trusted system (user).

15. Place the two files in the Caché system.
16. Edit the SSL/TLS configuration file and browse to their location and select them.
17. Save your SSL/TLS configuration.

### Testing the SSL/TLS Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xobw-1-4-security-configuration-guide/028.png) NOTE: To perform this test, you need to know the server-side’s host name or IP address and the port listening for SSL/TLS connections.

1.  Select the Test button to start testing the SSL/TLS configuration. You are prompted for the following information:
- Test server host name or IP address—This is the server-side server configured in the “<u>Server-Side</u>” section. For example:

> <span id="_Toc455656256" class="anchor"></span>Figure : Client Certificate Authentication Configuration—Testing the SSL/TLS Configuration server host name or IP address

> ![](xobw-1-4-security-configuration-guide/029.png)

- Test server port—This is the SSL port configured on the server-side server configured in the “<u>Server-Side</u>” section. For example:

> <span id="_Toc455656257" class="anchor"></span>Figure : Client Certificate Authentication Configuration—Testing the SSL/TLS Configuration server port

> ![](xobw-1-4-security-configuration-guide/030.png)

18. You should see the following similar information:

> <span id="_Toc455656258" class="anchor"></span>Figure : Client Certificate Authentication Configuration—Sample Results

> ![](xobw-1-4-security-configuration-guide/031.png)

19. You are now ready, and can reference the “client_authentication” SSL/TLS configuration in your WEB SERVER entry.

To enable your VistA M Server Client to use Client Certificate Authentication security, you *must* follow the instructions in Section 3 in the [*HWSC System Management Guide*](http://www.va.gov/vdl/documents/HealtheVet/HealtheVet_Web_Services_Client/xobw1_0sg.pdf). Also, define the configuration elements via an entry in the WEB SERVER file (#18.12) with values for the following fields:

- SSL ENABLED: TRUE
- SSL CONFIGURATION: SSL/TLS configuration (e.g., client_authentication).
- SSL PORT: Server’s SSL/TLS port number (e.g., 7002).