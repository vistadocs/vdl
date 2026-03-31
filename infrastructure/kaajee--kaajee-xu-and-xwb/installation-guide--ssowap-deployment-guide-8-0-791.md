---
title: KAAJEE SSOWAP Deployment Guide (8.0*791)
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: KAAJEE
app_name: KAAJEE (XU and XWB)
section: INF
app_status: active
pkg_ns: 
patch_ver: 8.0
patch_id: 
group_key: "KAAJEE::8.0"
file_numbers: 
  - 18
  - 200
security_keys: []
menu_options: 5
description: The Kernel Authentication and Authorization for Java (2) Enterprise Edition (KAAJEE) software was developed by Common Services Security Program. It was further supplemented by the implementation of the SSOi 2-Factor Authentication (2FA) Authorization requirement, producing a new Single Sign-On Web A
audience: 
keywords: 
  - class
  - kaajee
  - strong
  - application
  - login
  - error
  - table
  - software
  - server
  - security
page_count: 0
word_count: 22775
section_count: 7
table_count: 107
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: April 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/KAAJEE/kaajee_ssowap_8_791_depg_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/KAAJEE/kaajee_ssowap_8_791_depg_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=151"
---

![](kaajee-ssowap-deployment-guide-8-0-791/001.png)

KERNEL AUTHENTICATION & AUTHORIZATION FOR J2EESingle Sign-On Web Application Plugin(KAAJEE SSOWAP) VERSION 8.791FOR WEBLOGIC (WL) VERSIONS 12.2 AND HIGHERDEPLOYMENT GUIDE

April 2024

Office of Information and Technology

Product Development

*This page is left blank intentionally.*

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this manual. Revisions to the documentation are based on patches and new versions released to the field.

<span id="_Toc202862995" class="anchor"></span>Table i. Documentation revision history

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 53%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>04/2024</td>
<td>XU-*8*791</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>03/2022</td>
<td>XU*8*749 -Updated documentation for the WL 12.2 release</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>08/2020</td>
<td>Updated documentation to split KAAJEE SSPI, KAAJEE Classic and KAAJEE SSOWAP</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>07/2018</td>
<td>Software and documentation for KAAJEE 1.2.x.x, referencing VistALink 1.6 and WebLogic 10.3.6 and higher.</td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="odd">
<td>03/2011</td>
<td><p>Software and documentation for KAAJEE 1.1.0.007 and KAAJEE Security Service Provider Interface (SSPI) 1.1.0.002, referencing VistALink 1.6 and WebLogic 9.2 and higher.</p>
<p><strong>Software Version: 1.1.0.007</strong></p>
<p><strong>Security Service Provider Interface (SSPI) Version: 1.1.0.002</strong></p>
<p><strong>Kernel Patch: XU*8.0*504</strong></p></td>
<td><mark>Redacted</mark></td>
</tr>
<tr class="even">
<td>05/2006</td>
<td><p>Initial software and documentation for Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) 1.0.0.019 and KAAJEE SSPIs 1.0.0.010, referencing VistALink 1.5 and WebLogic 8.1 (SP4 or higher).</p>
<p><strong>Software Version: 1.0.0.019</strong></p>
<p><strong>SSPI Version 1.0.0.010</strong></p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/002.png) <strong>REF:</strong> For a description of the current KAAJEE software version numbering scheme, please review the readme.txt file distributed with the KAAJEE software.</p></td>
<td><mark>Redacted</mark></td>
</tr>
</tbody>
</table>

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

|                                                                                                                       |                                                                                                                                                                                            |
|-----------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/003.png) | NOTE: Kernel is the designated custodial software application for KAAJEE; however, KAAJEE comprises multiple patches and software releases from several HealtheVet-VistA applications. |

Contents

> [1. Declare Groups (weblogic.xml file) [4-3](#declare-groups-weblogic.xml-file)](#declare-groups-weblogic.xml-file)

> [2. Create VistA M Server J2EE Security Keys Corresponding to WebLogic Group Names [4-4](#create-vista-m-server-j2ee-security-keys-corresponding-to-weblogic-group-names)](#create-vista-m-server-j2ee-security-keys-corresponding-to-weblogic-group-names)

> [6. Protect Resources in Your J2EE Application [4-7](#protect-resources-in-your-j2ee-application)](#protect-resources-in-your-j2ee-application)

> [7. Administer Users [4-8](#administer-users)](#administer-users)

*This page is left blank intentionally.*

### Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*This page is left blank intentionally.*

### Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Deployment Guide is intended for use in conjunction with the Kernel Authorization and Authentication for J2EE (KAAJEE) software. It outlines the details of KAAJEE-related software and gives guidelines on how the software is used within Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA).

The intended audience of this manual is all key stakeholders. The primary stakeholder is Common Services. Additional stakeholders include:

- Health*<u>e</u>*Vet-VistA application developers of Web-based applications in the WebLogic Application Server environment.
- Information Resource Management (IRM) and Information Security Officers (ISOs) at Veterans Affairs Medical Centers (VAMCs) responsible for computer management and system security.
- Enterprise Product Support (EPS).
- VAMC personnel who will be using Health*<u>e</u>*Vet-VistA Web-based applications running in the WebLogic Application Server environment.

How to Use this Manual

This manual is divided into three major parts:

- User Guide—Provides general overview of the KAAJEE sub project.
- Developers Guide—Provides step-by-step instructions for Health*<u>e</u>*Vet-VistA developers to follow and Application Program Interfaces (APIs) to use when writing Web-based applications incorporating the KAAJEE authorization and authentication functionality.
- Systems Management Guide—Provides implementation, maintenance, and security overview for IRM and ISO personnel.

Throughout this manual, advice and instructions are offered regarding the use of KAAJEE software and the functionality it provides for Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA) software products.

There are no special legal requirements involved in the use of KAAJEE-related software.

This manual uses several methods to highlight different aspects of the material:

- Various symbols/terms are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols/terms:

<span id="_Ref345831418" class="anchor"></span>

Table ii. Documentation symbol/term descriptions

| Symbol                                                                                                            | Description                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/004.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](kaajee-ssowap-deployment-guide-8-0-791/005.png)     | CAUTION or DISCLAIMER: Used to inform the reader to take special notice of critical information.                |

- Descriptive text is presented in a proportional font (as represented by this font).
- "Snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts and some software code reserved/key words will be bold typeface type.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/006.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- Java software code, variables, and file/folder names can be written in lower or mixed case.
- All uppercase is reserved for the representation of Mumps (M) code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistALink—VistA M Server and Application Server software
- Linux (i.e., Red Hat Enterprise ES 6.0 or higher) or Microsoft Windows environment
- Java Programming languageJava 2 Standard Edition (J2SE) Java Development Kit (JDK, a.k.a. Java Software Development Kit \[SDK\])
- WebLogic 10.3.6 and higher—Application servers
- Oracle Database 11*g*—Database (e.g., Security Service Provider Interface \[SSPI\] or Standard Data Services \[SDS\] 18.0 (or higher) database/tables)
- Oracle SQL\*Plus Software 9.2.0.1.0 (or higher)

This manual provides an overall explanation of the installation procedures and functionality provided by the software; however, no attempt is made to explain how the overall HealtheVet-VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the VA Intranet for a general orientation to HealtheVet-VistA the:

> http://vista.med.va.gov/

Reference Materials

Readers who wish to learn more about KAAJEE should consult the following:

- *Kernel Authentication & Authorization for J2EE (KAAJEE) Installation Guide*
- *Kernel Authentication & Authorization for J2EE (KAAJEE) Deployment Guide*, this manual
- KAAJEE Web site:

> http://vista.med.va.gov/kernel/kaajee/index.asp

- *Kernel Systems Management Guide*
- *VistALink Installation Guide*
- *VistALink System Management Guide*
- *VistALink Developer Guide*

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/007.png)</td>
<td><p><strong>REF:</strong> For more information on VistALink, please refer to the following Web address:</p>
<blockquote>
<p>http://www.va.gov/vdl/application.asp?appid=163</p>
</blockquote></td>
</tr>
</tbody>
</table>

Health*<u>e</u>*Vet-VistA documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/008.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following Web address:</p>
<blockquote>
<p>http://vista.med.va.gov/iss/acrobat/index.asp</p>
</blockquote></td>
</tr>
</tbody>
</table>

Health*<u>e</u>*Vet-VistA documentation can be downloaded from the Veterans Health Affairs (VHA) Software Document Library (VDL) Web site:

> <http://www.va.gov/vdl/>

Health*<u>e</u>*Vet-VistA documentation and software can also be downloaded from the Enterprise Product Support (EPS) anonymous directories at the various Office of Information Field Offices (OIFOs) noted below:

- Preferred Method download.vista.med.va.gov

This method transmits the files from the first available File Transfer Protocol (FTP) server.

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/009.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# User Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Revision History](#revision-history)
    - [Figures](#figures)
    - [Tables](#tables)
    - [Orientation](#orientation)
- [User Guide](#user-guide)
  - [KAAJEE SSOWAP Overview](#kaajee-ssowap-overview)
- [Developer's Guide](#developers-guide)
  - [KAAJEE Installation Instructions for Developers](#kaajee-installation-instructions-for-developers)
    - [Confirm/Obtain Developer Workstation Distribution Files (recommended)](#confirmobtain-developer-workstation-distribution-files-recommended)
    - [Create a KAAJEE Staging Folder (required)](#create-a-kaajee-staging-folder-required)
    - [Unzip/Explode KAAJEE Software (required)](#unzipexplode-kaajee-software-required)
    - [Review/Use KAAJEE Files for Web-based Applications (recommended)](#reviewuse-kaajee-files-for-web-based-applications-recommended)
  - [Integrating KAAJEE SSOWAP with an Application](#integrating-kaajee-ssowap-with-an-application)
    - [Assumptions When Implementing KAAJEE](#assumptions-when-implementing-kaajee)
    - [Software Requirements/Dependencies](#software-requirementsdependencies)
    - [Web-based Application Procedures to Implement KAAJEE](#web-based-application-procedures-to-implement-kaajee)
  - [Software Product Security](#software-product-security)
  - [Cactus Testing with KAAJEE SSOWAP](#cactus-testing-with-kaajee-ssowap)
  - [Troubleshooting](#troubleshooting)
    - [Glossary](#glossary)
    - [Appendix A—Sample Deployment Descriptors](#appendix-asample-deployment-descriptors)
    - [Appendix B—Mapping WebLogic Group Names with J2EE Security Role Names](#appendix-bmapping-weblogic-group-names-with-j2ee-security-role-names)
    - [Index](#index)
This is the User Guide section of this supplemental documentation for Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE). It is intended for use in conjunction with the KAAJEE software. It details the user-related KAAJEE documentation (e.g., overview of the KAAJEE sub-project), management of KAAJEE-related software, etc.).
*This page is left blank intentionally.*

## KAAJEE SSOWAP Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Kernel Authentication and Authorization for Java (2) Enterprise Edition (KAAJEE) software was developed by Common Services Security Program. It was further supplemented by the implementation of the SSOi 2-Factor Authentication (2FA) Authorization requirement, producing a new Single Sign-On Web Application Plugin component – SSOWAP – which is part of this distribution. For ease of reference and understanding, references related to a specific functionality of the A/V codes validation version of KAAJEE is refered to as KAAJEE Classic.

Kernel is the designated custodial software application for KAAJEE; however, KAAJEE comprises multiple software and patches from several HealtheVet-VistA applications.

KAAJEE addresses the Authentication and Authorization (AA) needs of HealtheVet-VistA Web-based applications in the Java 2 Platforms, Enterprise Edition (J2EE) environment. Over the long term, the Department of Veterans Affairs (VA) will provide Authentication and Authorization (AA) services to end-users enterprise wide; however, in the interim period, the Office of Information (OI) has a choice to make as to which AA mechanism(s) would be the most effective. This applies both to the needs of the applications themselves, as well as in anticipation of an expected migration to the future AA solution.

Most major J2EE application servers (e.g., WebLogic 12.2 and higher and Oracle's 11*g*) allow enterprises to override the default source of AA and replace it with custom, enterprise-specific sources for AA.

.

KAAJEE SSOWAP depends on the Personal Identification Verification (PIV) authentication by the Identity and Access Management (IAM) services, it then proceeds to authenticate provided data against a (Secure Token Service (STS) web service, followed by calling the Kernel authentication routine at the selected VistA M Server. If the user has been properly authenticated against a VistA M Server, SSOWAP dynamically creates a temporary username and password and populates this into a Structured Query Language (SQL) database via custom Security Service Provider Interfaces (SSPIs). This username and password is needed for the second level/phase/pass authentication for the J2EE container.

|                                                                                                                |                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/010.png) | REF: For more information on SSPIs and the overall KAAJEE-related AA process please refer to the "Error! Not a valid bookmark self-reference." topic in this documentation. |

Currently, Kernel maintains the primary VistA and HealtheVet-VistA user store (i.e., NEW PERSON file \[#200\]), which provides both Authentication and Authorization (AA) services for all VistA and HealtheVet-VistA applications. By leveraging Kernel, KAAJEE authenticates and authorizes J2EE Web users by using Kernel's AA capabilities.

Some potential advantages to employing Kernel as the AA source include the following:

- Provides a single point of user management for existing and new HealtheVet-VistA applications.
- Allows the use of an existing credential—the Access and Verify code for Authentication and Authorization, rather than introducing a new security credential.
- Eliminates the need to maintain a mapping from WebLogic accounts to VistA M Server Kernel accounts.
- Avoids an additional user store, which simplifies the migration to the future AA solution.
- Partitions user authorizations by Veterans Health Administration (VHA) site.

Some potential KAAJEE strategy limitations due to employing Kernel as the AA source include the following:

- Kernel user accounts are not currently VA-wide; instead, they are facility-specific.
- Users *must* have an active VistA M Server Kernel account on some VistA system. Not all users fit this requirement (e.g., Veterans Affairs Central Office \[VACO\] users).
- This strategy introduces a dependency on the M system's availability, to perform virtually any function in a J2EE application.
- Correlating a user at one VA facility with the same user at a different VA facility is not supported, given the current lack of an enterprise-wide VA person identifier (e.g., VA-wide Person Identifier \[VPID\]).

|                                                                                                                |                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/011.png) | REF: KAAJEE Classic does *not* currently use the Department of Veterans Affairs Personal Identification (VPID), since this field is not currently populated enterprise-wide. |

The KAAJEE software provides a Kernel-based Authentication and Authorization (AA) service for all HealtheVet-VistA Web-based applications in the J2EE/WebLogic environment.

KAAJEE is designed to run on the WebLogic 12.26 and higher.

This manual discusses in more detail the major software modules that, together, provide for KAAJEE functionality and how to deploy KAAJEE-enabled J2EE Form-based Authentication framework and the Security Service Provider Interfaces (SSPIs).

#### Features

KAAJEE SSOWAP provides the following high-level features and functionality:

- Prompts users to enter their site of choice when they attempt to access a protected application resource for the first time during a user session.
- Validates the obtained STS certificate against the M system/division selected by the user at logon.

> Ddisplays a list of M systems, by division, against which an end-user can log in.

- Returns all VistA M Server J2EE security keys and uses these as the basis for authorization decisions, as each security key is cached as a WebLogic group name. The KAAJEE SSPIs currently use an external Oracle 11*g* database to store this information for later authentication.  
  >   
  > KAAJEE roles are defined by the list of roles in the web.xml file, VistA M Server J2EE security keys, and WebLogic group names found in your application's weblogic.xml file.

|                                                                                                                |                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/012.png) | REF: For more information on groups and roles, please refer to Chapter 4, "Role Design/Setup/Administration," in this manual. |

- (optional) Maps J2EE security role names with security key role names. Through \<security-role-assignment\> tags (e.g., in weblogic.xml) the actual J2EE security role names can be different than the security key role names. This mapping is optional, because if the same names are used throughout, no \<security-role-assignment\> tags are required.

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/013.png) | REF: For a sample spreadsheet showing a mapping between WebLogic group names (i.e., principals) with J2EE security role names, please refer to "Appendix B—Mapping WebLogic Group Names with J2EE Security Role Names" in this manual. |

- Transforms valid Access and Verify codes into a J2EE-compatible username (e.g., "kaaj_DUZ_8888~CMPSYS_523") and password, and submits the information to the J2EE container. It then passes the submitted information to the KAAJEE SSPIs, which validate the username and makes that username the current user.

> Application developers can use the HttpServletRequest.getRemoteUser servlet method to return demographic data, such as the KAAJEE-created username (e.g., "kaaj_DUZ_8888~CMPSYS_523").

|                                                                                                                |                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/014.png) | REF: For more information on formatting J2EE usernames, please refer to the "J2EE Username Format" topic in Chapter 7, "Programming Guidelines," in this manual. |

- Calls the KAAJEE SSPIs when the J2EE container checks user roles, which checks the role cache for the given user, created at user login. This allows user authorizations to be managed on the VistA M Server, and yet have fast response time in the J2EE application.
- Provides user demographics information, which includes the selected Division at login, <u>user VPID</u>, user number (or DUZ), and user Name, all which are available to the application after login via the Session object (cookie).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/015.png)</td>
<td><p><strong>REF:</strong> For more information on the user demographics provided, please refer to the following:</p>
<ul>
<li><blockquote>
<p>"LoginUserInfoVO Object" topic in Chapter 7, "Programming Guidelines," in this manual.</p>
</blockquote></li>
<li><blockquote>
<p>VistALink and the Health<em><u>e</u></em>Vet-VistA documentation can be downloaded from the VHA Software Document Library (VDL) Web site:</p>
</blockquote></li>
</ul>
<blockquote>
<p><a href="http://www.va.gov/vdl/">http://www.va.gov/vdl/</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

- Uses the SIGN-ON LOG file (#3.081) on the VistA M Server (i.e., the same M system used for user authentication) to track user logons and logoffs.

|                                                                                                                |                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/016.png) | REF: For more information on the SIGN-ON LOG file (#3.081), please refer to the *Kernel Systems Management Guide*. |

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/017.png)</td>
<td><p>J2EE container-managed enforcement of security, both programmatic and declarative, is fully enabled with KAAJEE.</p>
<p>Deployment of KAAJEE for a given J2EE application requires the KAAJEE components to be integrated with the application, because the J2EE servlet specification requires J2EE Form-based Authentication to run within the scope of the application using it.</p></td>
</tr>
</tbody>
</table>

#### KAAJEE SSOWAP 2FA Login Process Flow Overview

<span id="_Toc167811455" class="anchor"></span>Figure 1‑1 KAAJEE SSOWAP & J2EE Web-based application process overview diagram

![](kaajee-ssowap-deployment-guide-8-0-791/018.png)

#### Using Industry Standard Form-based Authentication

Figure 1‑2 shows what happens if you specify *form-based authentication*, in which you can customize the login screen and error pages that an HyperText Transfer Protocol (HTTP) browser presents to the end user.

<span id="_Ref206311385" class="anchor"></span>Figure 1‑2. Industry Standard for Form-Based Authentication overview

![](kaajee-ssowap-deployment-guide-8-0-791/019.png)

With form-based authentication, the following things occur:

- A client requests access to a protected resource.
- If the client is unauthenticated, the server redirects the client to a login page.
- The client submits the login form to the server.
- If the login succeeds, the server redirects the client to the resource. If the login fails, the client is redirected to an error page. [^1]

#### Using Industry Standard Form-based Authentication

Figure 1‑2 shows what happens if you specify *form-based authentication*, in which you can customize the login screen and error pages that a HyperText Transfer Protocol (HTTP) browser presents to the end user.

<span id="_Toc51575220" class="anchor"></span>Figure 1‑3. Industry Standard for Form-Based Authentication overview

![](kaajee-ssowap-deployment-guide-8-0-791/020.png)

With form-based authentication, the following things occur:

- A client requests access to a protected resource.
- If the client is unauthenticated, the server redirects the client to a login page.
- The client submits the login form to the server.
- If the login succeeds, the server redirects the client to the resource. If the login fails, the client is redirected to an error page. [^2]

#### KAAJEE SSOWAP Use of Form-based Authentication

Form-based authentication is not particularly secure. In form-based authentication, the content of the user dialog box is sent as plain text, and the target server is not authenticated. This form of authentication can expose your usernames and passwords unless all connections are over Secure Sockets Layer (SSL). If someone can intercept the transmission, the username and password information can easily be decoded.

The J2EE servlet specification provides at least two means for Web-based applications to query for end-user authentication credentials:

- Hyper Text Transport Protocol (HTTP) Basic Authentication
- J2EE Form-based Authentication

KAAJEE employs J2EE Form-based Authentication for the J2EE Web-based authentication process as part of the larger security framework. VistALink provides connectivity between KAAJEE and the VistA M Server.

J2EE Form-based Authentication works as follows:

1.  The user on the client uses a Web browser to access a Web-based application's protected resource (URL).
2.  The J2EE Application Server (container) detects that the user is not in an authenticated user session and redirects the user to the J2EE Form-based Authentication Web login page specified in the \<login-config\> tag in the web.xml deployment descriptor.

|                                                                                                                |                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/021.png) | NOTE: The container remembers the URL the user originally requested. |

3.  The user on the client submits their username and password (i.e., Access and Verify codes) via the KAAJEE Authentication and Authorization (AA) Web login form.

> a\. The Web login page's responsibility is to collect user credentials (username and password) and calls the WebLogic ServletAuthentication.authenticate API.

> b\. The WebLogic ServletAuthentication.authenticate API passes those credentials to the WebLogic Custom Security Authentication Providers.

4.  J2EE Application Server authenticates the user:
    1.  Success:

> i\. If the WebLogic Custom Security Authentication Providers authenticates the user, an authenticated session is established.

2.  Failure:

> i\. If the WebLogic Custom Security Authentication Providers fails to authenticate the user, an authenticated session is *not* established.

5.  Upon return to the ServletAuthentication.authenticate API, a flag is set identifying if the user has been authentication. KAAJEE checks this flag to determine where to redirect the user; either to the target application page, or to the login error page.

There *cannot* be login buttons that point directly to the login page. Only an attempt to access a protected resource (as opposed to the login page) triggers the J2EE Form-based Authentication process.

Authentication (i.e., challenging the end-user for Access and Verify codes by prompting them with the logon Web form) is triggered when an end-user attempts to access a protected Web page in the application:

> The container will force the user to authenticate by submitting the login form only when required (for example, when an unauthenticated user tries to access a protected resource). This is termed lazy authentication and means that users who never attempt to access a protected resource will never be forced to authenticate. Once authenticated, a user will never be challenged again within a session. The user identity will be carried through to calls to other components of the application. Therefore, there is no need for user code behind protected resources to check that authentication has occurred.[^3]

#### Container Security Detecting Authorization Failures

Success or failure of the J2EE Application Server authorization for the user is defined as follows:

1.  Success:

> i\. If the container security detects that the user has the roll needed to access the requested page, the container permits access to that page.

2.  Failure:

> i\. Upon failure, the container either displays a general 403 error page or redirects the user to a specified error page identified in web.xml for 403 errors.

Generally, form-based authentication would handle both authentication and authorization. KAAJEE only implements the user interface part of form-based authentication. The back-end security check is replaced with the ServletAuthentication.authenticate API. Therefore, all authorization failures are handled solely by container security. As such all users who are not authorized to access the targeted page after login will receive an http '403' error. To provide a more user-friendly error message, KAAJEE now distributes a 'loginerror403.jsp' file. The consuming application may use this page or another of their choosing. To use this page, add an '\<error-page\>' entry in web.xml similar to the one listed below:

\<error-page\>

\<error-code\>403\</error-code\>

\<location\>/login/loginerror403.jsp\</location\>

\</error-page\>

#### KAAJEE SSOWAP J2EE Web-based Application Login Page

KAAJEE SSOWAP provides the official HealtheVet VistA J2EE Web-based application login page (i.e., login.jsp) to collect the end-user's choice of instition under which the user logs in. Kernel on the VistA M Server uses that information to authenticate the end-user and sign them onto VistA. A sample of the KAAJEE SSOWAP Web login page is displayed below:

<span id="_Toc108603785" class="anchor"></span>

Figure 1‑4. Sample KAAJEE SSOWAP Web login page (i.e., login.jsp)

![](kaajee-ssowap-deployment-guide-8-0-791/022.png)

|                                                                                                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/023.png) | CAUTION: As per the Software Engineering Process Group/Software Quality Assurance (SEPG/SQA) Standard Operating Procedure (SOP) 192-039—Interface Control Registration and Approval (effective 01/29/01, see <span class="mark">REDACTED</span>), application programmers developing HealtheVet VistA J2EE Web-based applications that are KAAJEE-enabled *must* use the KAAJEE login Web page (i.e., login.jsp) as delivered (see Figure 1‑4). Developers *must not* customize the login Web page or alter the KAAJEE software code in any way. |

|                                                                                                     |                                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/024.png) | CAUTION: In a domain consisting of an Administration Server and several Managed Servers, the Administration Server *must* always be running, as new logins through KAAJEE will *not* succeed while the Administration Server is down. |

The KAAJEE SSOWAP Web login page:

- Complies with Section 508 of the Rehabilitation Act Amendments of 1998.
- Provides a consistent look-and-feel across all HealtheVet VistA J2EE Web-based applications that are KAAJEE-enabled.

As you can see from Figure 1‑4, the introductory text (i.e., system announcement message) is displayed in the top portion of the Web login page and is preceded by the "System Announcements:" label.

Following the Introductory text, the name of the application to which you are signing on is displayed after the "Log on for:" label. Applications pass in the name of their application. In this example (Figure 1‑4), the application name is SSOi Web Application Plugin (SWAP) 2FA release.

#### Session Expiration Dialog Box Warning End-Users of Session Time Out

In compliance with Section 508, during login label are the specific KAAJEE displays a warning to the end-user entries used in alerting when there is only 30 seconds remaining in their session.

<span id="_Toc167811459" class="anchor"></span>Figure 1‑5 Session Will Expire

> ![](kaajee-ssowap-deployment-guide-8-0-791/025.png)

In order to log into the Web-based application, which is described in the topic that follows (i.e., Login Procedures for J2EE Web-based Applications) KAAJEE provides this warning using JavaScript. Therefore, KAAJEE distributes a login.js file, which is exported as part of the login\javascript\\ folder.

|                                                                                                                |                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/026.png) | REF: For more information on distribution of the login.js file, please refer to "Section 508 Compliance Addresses Session Timeouts" topic in section titled "5. Import KAAJEE Login Folder" of this manual. |

#### Login Procedures for J2EE Web-based Applications with KAAJEE SSOWAP

To log into VistA from a J2EE Web-based application, do the following:

> 1\. (Required) Navigate to the application URL, communicated to you by the release coordinator.

> 2\. Enter you PIV PIN at the prompt.

> 4\. (required) Select the appropriate Station Name/Number from the Institution dropdown list or accept the default value displayed.

> 5\. (required) Click on (press) the Proceed button or press the \<Enter\> key. After the authentication process successfully completes on the VistA M Server, the requested application protected Web page will be displayed.

|                                                                                                                |                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/027.png) | NOTE: The asterisks located next to the Sort by Station Number/Sort by Station Name radio buttons and the Institution dropdown box indicate that both the Station Name/Number sort order preference. |

#### <table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/028.png)</td>
<td><strong>REF:</strong> For information on common login-related error messages, please refer to the "Common Login-related Error Messages" topic in Chapter 10, "Troubleshooting," in this manual.<br />
<br />
For a list of other login-related error messages, please refer to the "Symptoms and Possible Solutions" topic in Chapter 7 in the <em>VistALink System Administration Guide</em>.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/029.png) | REF: For more information on the Kernel signon process and related error messages, please refer to the "Signon/Security" section in the *Kernel Systems Management Guide*. |

# Developer's Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Developer's Guide section of this supplemental documentation for Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE). It is intended for use in conjunction with the KAAJEE software. It details the developer-related KAAJEE documentation (e.g., developer procedures needed to incorporate the KAAJEE authorization and authentication functionality into Web-based applications, APIs exported with KAAJEE, etc.).

*This page is left blank intentionally.*

## KAAJEE Installation Instructions for Developers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Dependencies: Preliminary Considerations for Developer Workstation Requirements

The following minimum hardware, software tools, and documentation are required by developers when developing J2EE Web-based applications that are Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE)-enabled:

<span id="_Ref204792543" class="anchor"></span>Table 2‑1. Developer minimum hardware and software tools/utilities required for KAAJEE-enabled application development

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Minimum Hardware/Software Requirement</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Workstation Hardware</td>
<td>80x86-based client or server workstation.</td>
</tr>
<tr class="even">
<td>Operating System</td>
<td><p>One of the following 32-bit operating systems:</p>
<ul>
<li><blockquote>
<p>Linux (i.e., Red Hat Enterprise ES 8.0)</p>
</blockquote></li>
<li><blockquote>
<p>Microsoft Windows XP Service Pack 3</p>
</blockquote></li>
<li><blockquote>
<p>Microsoft Windows 11</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Development-related Software</td>
<td><p>The following development-related software is required in order to develop J2EE Web-based applications that utilize KAAJEE functionality:</p>
<ul>
<li><blockquote>
<p>KAAJEE Software (see <strong>Error! Not a valid bookmark self-reference.</strong>)—Software used to KAAJEE-enable Web-based applications.</p>
</blockquote></li>
<li><blockquote>
<p>Java 2 Standard Edition (J2SE) Java Development Kit (JDK)—COTS software for development of J2EE Web-based applications that are KAAJEE-enabled. The JDK should include Java Runtime Environment (JRE) and other developer tools to write Java code.</p>
</blockquote></li>
<li><blockquote>
<p>HealtheVet-VistA Web-based Software Applications (e.g., Blind Rehab, Patient Advocate Tracking System [PATS], Veterans Personal Finance System [VPFS])—Web-based software <em>must</em> be available to the end-user/developer.</p>
</blockquote></li>
<li><blockquote>
<p>Internet Browser (e.g., Microsoft Internet Explorer 6.0 or higher)—Commercial-Off-The-Shelf (COTS) software. Internet browser software <em>must</em> be available to the end-user on the client workstation.</p>
</blockquote></li>
<li><blockquote>
<p>Oracle SQL*Plus (9.2.0.1.0 or higher)—COTS software for configuring SSPI SQL or Standard Data Services (SDS) tables on an Oracle 10<em>g</em> database.</p>
</blockquote></li>
</ul>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/030.png) <strong>REF:</strong> For more information on configuring files and integrating KAAJEE with Web-based software applications, please refer to Chapter 4, "Integrating KAAJEE with an Application," in this manual.</p></td>
</tr>
<tr class="even">
<td><p>Network Communications Software/Capability</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/031.png) <strong>REF:</strong> For more information on telecommunications support, please visit the VHA Communication Services Office (CSO) Home Page:</p>
<blockquote>
<p>http://vaww.va.gov/cso/</p>
</blockquote></td>
<td><p>All developer workstations <em>must</em> have the following network communications software and capability:</p>
<ul>
<li><blockquote>
<p>Networked client/server workstations running Microsoft's native TCP/IP stack.</p>
</blockquote></li>
</ul>
<blockquote>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/032.png) <strong>NOTE:</strong> Currently, only Winsock compliant TCP/IP protocol is supported on the LAN or remotely as Point-to-Point Protocol (PPP) or Serial Line Internet Protocol (SLIP). You <em>must</em> use RAS (Remote Access Service) or Dialup Networking to connect to the server using PPP or SLIP. For the setup of RAS or Dialup Networking, please refer to the appropriate operating system's documentation.</p>
</blockquote>
<ul>
<li><blockquote>
<p>Connectivity with the VistA M Server (i.e., VA Wide Area Network [WAN] connectivity). Run PING.EXE to test the connectivity.</p>
</blockquote></li>
<li><blockquote>
<p>Capability to log onto the NT network using a unique NT Logon ID.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

#### Dependencies: KAAJEE and VistALink Software

The following table shows the dependency relationships between the current version of KAAJEE, SSPIs, and VistALink software:

<span id="_Toc99793280" class="anchor"></span>Table 2‑2. Dependencies——KAAJEE, SSPIs, and VistALink software

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 24%" />
<col style="width: 26%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3"><strong>Developer-related Software</strong></th>
<th colspan="2"><strong>Application Server Software</strong></th>
</tr>
<tr class="odd">
<th><strong>Software</strong></th>
<th><strong>Version</strong></th>
<th><strong>KAAJEE SSOWAP Software<br />
Release/Distribution</strong></th>
<th><strong>KAAJEE SSPI Software<br />
Release/Distribution</strong></th>
<th><strong>VistALink Software Release/Distribution</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KAAJEE SSOWAP</td>
<td>8.791</td>
<td>XU_8.791.ZIP</td>
<td>XU_8.781.zip</td>
<td>VistALink 1.6.7</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/033.png) | REF: For a list of VistALink dependent VistA M Server patches, please refer to the *VistALink Installation Guide*. |

#### Dependencies: KAAJEE-Related Software Applications/Modules

<span id="_Toc202863005" class="anchor"></span>Table 2‑3. Dependencies—KAAJEE SSOWAP-related software applications/modules

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Module</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WebLogic 12.2 and higher Application Server<br />
(running)</td>
<td><p>WebLogic 12.2 and higher servers use security provider packages that allow a J2EE application running in WebLogic 12.2 and higher to draw its Authentication and Authorization from Kernel on the VistA M Server.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/034.png) <strong>NOTE:</strong> A J2EE standard for pluggable authentication for J2EE servers is underway<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>, but won't be finalized until J2EE 1.5.</p></td>
</tr>
<tr class="even">
<td>VistALink 1.6.7</td>
<td>The Application Server <em>must</em> also have the VistALink software deployed and running. VistALink provides connectivity between KAAJEE and the VistA M Server.</td>
</tr>
<tr class="odd">
<td>Standard Data Services (SDS) 19.0 (or higher)</td>
<td>KAAJEE makes internal API calls to the SDS Database/Tables located on an Oracle 11<em>g</em> database.</td>
</tr>
<tr class="even">
<td>Log4j2 libraries, log4j configuration file</td>
<td>KAAJEE SSOWAP employs log4j2 API for logging management and output</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>JSR-196, http://www.jcp.org/en/jsr/detail?id=196.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

#### KAAJEE SSOWAP Installation Instructions

The following instructions are only required for those workstations to be used by developers to develop KAAJEE-enabled HealtheVet-VistA Web-based software applications running on a WebLogic Application Server.

|                                                                                                                |                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/035.png) | REF: For Developer Workstation platform requirements, please refer to the "Dependencies: Preliminary Considerations for Developer Workstation Requirements" topic in this chapter. |

### Confirm/Obtain Developer Workstation Distribution Files *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following files are needed to install the KAAJEE developer-related software:

<span id="_Toc167811505" class="anchor"></span>Table 2‑4. Dependencies—KAAJEE-related software documentation

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KAAJEE_SSOWAP_8_791_RN.PDF</td>
<td><blockquote>
<p><strong>Release Notes</strong> (manual). List of new features in the KAAJEE SSOWAP distribution</p>
</blockquote></td>
</tr>
<tr class="even">
<td>KAAJEE_SSOWAP_8_791_DEPG.PDF</td>
<td><blockquote>
<p><strong>Deployment Guide</strong> (manual). Outlines the details of KAAJEE-related software and gives guidelines on how the software is used within Health<em><u>e</u></em>Vet-Veterans Health Information Systems and Technology Architecture. It contains the User Manual, Programmer Manual, and Technical Manual information for KAAJEE.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>XU_8_791.ZIP</td>
<td><blockquote>
<p><strong>KAAJEE Distribution File</strong> (jar files). This Zip file contains the KAAJEE software for development of Health<em><u>e</u></em>Vet-VistA Web-based applications requiring Authentication and Authorization against Kernel on the VistA M Server via KAAJEE.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/036.png)</td>
<td><p><strong>REF:</strong> For the KAAJEE software release, all distribution files, unless otherwise noted, are available for download from the Enterprise Product Support (EPS) anonymous directories:</p>
<ul>
<li><blockquote>
<p>Preferred Method download.vista.med.va.gov</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

### Create a KAAJEE Staging Folder *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create a KAAJEE Staging Folder on your developer workstation. This will be referred to as the \<STAGING_FOLDER\> alias for the rest of the instructions.

### Unzip/Explode KAAJEE Software *(required)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Unzip/Explode the XU_8_791.ZIP software distribution file in the \<STAGING_FOLDER\>.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/037.png)</td>
<td><p><strong>NOTE:</strong> KAAJEE makes internal API calls to the Standard Data Services (SDS) Database/Tables 19.0 (or higher) located on an Oracle 19c database. SDS is responsible for maintaining this database and related tables.</p>
<p>KAAJEE Classic distributes SDS 19.0 client jar files as part of the Sample Web Application. If you deploy the both the KAAJEE Sample Web Application and your own Web-based application on the same WebLogic Application Server domain instance and intend to use a different version of SDS, those client jar files will need to be swapped out for the appropriate version of the SDS client jar files. Otherwise, there may be a conflict if both applications reference the same JNDI tree.</p></td>
</tr>
</tbody>
</table>

### Review/Use KAAJEE Files for Web-based Applications *(recommended)*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To build your HealtheVet-VistA J2EE Web-based applications that are KAAJEE-enabled, you need to configure and include the kaajee ssowap jar file located in the following directory:

> \<STAGING_FOLDER\>\ssowap-8.0.791.jar

> Each HealtheVet-VistA Web-based application requiring Authentication and Authorization against Kernel on the VistA M Server should use the standard KAAJEE Web login page, which is available with the login.jsp file located in the following KAAJEE archive:

> \<STAGING_FOLDER\>\ssowap-8.0.791.war

|                                                                                                                   |                                                                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/038.png) | CAUTION: Consuming applications should *not* provide a direct link to the login.jsp file. Otherwise, users could get a login error message when they click on that link. |

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/039.png)</td>
<td><p><strong>REF:</strong> For more information on this login error message, please refer to the "</p>
<p>Error: You navigated inappropriately to this page" topic in Chapter 10, "Troubleshooting," in this manual.</p></td>
</tr>
</tbody>
</table>

> Review the sample descriptor files located in the following KAAJEE archive:

> \<STAGING_FOLDER\>\\ ssowap-8.0.791.war

> Use these sample descriptor files as templates for your Web-based applications.

|                                                                                                                |                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/040.png) | REF: For more information on configuring files and integrating KAAJEE with Web-based software applications, please refer to Chapter 4, "Integrating KAAJEE SSOWAP with an Application," in this manual. |

> For example:

<span id="_Toc204421605" class="anchor"></span>Figure 2‑1. Sample application weblogic.xml file (e.g., KAAJEE Sample Web Application)

\<?xml version="1.0" encoding="UTF-8"?\>

\<weblogic-web-app xmlns="http://www.bea.com/ns/weblogic/10" xmlns:wls="http://www.bea.com/ns/weblogic/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd http://www.bea.com/ns/weblogic/10 http://www.bea.com/ns/weblogic/103/weblogic-web-app.xsd"\>

\<run-as-role-assignment\>

\<role-name\>adminuserrole\</role-name\>

\<run-as-principal-name\>SSOWAP_USER\</run-as-principal-name\>

\</run-as-role-assignment\>

\<security-role-assignment\>

\<role-name\>SSOWAP_APP_ROLE\</role-name\>

\<principal-name\>PRPF_LEAD_PFC\</principal-name\>

\</security-role-assignment\>

\<session-descriptor\>

\<cookie-name\>ssowapJSESSIONID\</cookie-name\>

\</session-descriptor\>

\<context-root\>swap\</context-root\>

\</weblogic-web-app\>

> In this sample application weblogic.xml file, the developers use KAAJEE Sample Web Application-related VistA M Server J2EE security keys and role names.

> The \<session-descriptor\> tag contains the \<session-param\> tag, which defines attributes for Hyper Text Transport Protocol (HTTP) sessions, as shown in Table 2‑1.

> The WebLogic Application Server defines the session cookie name. If it is not set by the user, it defaults to JSESSIONID. KAAJEE needs to set the session cookie name. You can set this to a more specific name for your application. For example:

- KAAJEE SSOWAP: ssowapJSESSIONID
- ApplicationOne: applicationoneJSESSIONID
- ApplicationTwo: applicationtwoJSESSIONID

> For KAAJEE SSOWAP to execute correctly, it needs to have a \<run-as\> tag, which causes it to run as an Admin user, as shown below:

<span id="_Toc202863008" class="anchor"></span>Figure 2‑2. Sample excerpt from a web.xml file—Using the run-as tag

> \<servlet\>

> \<servlet-name\>LoginController\</servlet-name\>

> \<servlet-class\>gov.va.med.authentication.kernel.ssowap.LoginController\</servlet-class\>

> \<init-param\>

> \<param-name\>debugFlag\</param-name\>

> \<param-value\>True\</param-value\>

> \</init-param\>

> \<run-as\>

> \<role-name\>adminuserrole\</role-name\>

> \</run-as\>

> \</servlet\>

> Make sure that the application context name is in the kaajeeConfig.xml file, as shown below:

<span id="_Toc99332741" class="anchor"></span>Figure 2‑3. Sample \<context-root-name\> tag found in the kaajeeConfig.xml file

\<context-root-name\>/ssowapSampleApp\</context-root-name\>

|                                                                                                                   |                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/041.png) | Congratulations! You have now completed the installation of KAAJEE-related software on the developer workstation. |

*This page is left blank intentionally.*

## Integrating KAAJEE SSOWAP with an Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter describes how application developers can modify their HealtheVet-VistA Web-based applications to integrate Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) 1.2.0.xxx for Authentication and Authorization to the VistA M Server.

This chapter discusses the following topics:

- Assumptions When Implementing KAAJEE
- Software Requirements
- Web-based Application Procedures to Implement KAAJEE

### Assumptions When Implementing KAAJEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following assumptions are made regarding application developers and HealtheVet-VistA J2EE Web-based applications when implementing KAAJEE (Iteration 1):

- Developer Training—It is assumed that developers have J2EE experience, including the following skills:
- Writing Servlets
- Configuring J2EE Deployment Descriptors
- Deploying Java-based applications
- Configuring WebLogic 10.3.6 and higher -specific Deployment Descriptors
- Configuring/Using Oracle 11*g* database (e.g., Security Service Provider Interface \[SSPI\])
- Configuring/Using Log4J
- Implementing the security plug-in for WebLogic 10.3.6 and higher by using custom Security Service Provider Interfaces (SSPIs)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/042.png)</td>
<td><p><strong>REF:</strong> Information about implementing the security plug-in and SSPIs for WebLogic 10.3.6 and higher can be found at the following references:</p>
<ul>
<li><blockquote>
<p><em>Kernel Authentication &amp; Authorization for J2EE (KAAJEE) Installation Guide</em></p>
</blockquote></li>
<li><blockquote>
<p>WebLogic Documentation at the following Website:</p>
</blockquote></li>
<li><blockquote>
<p><u>http://www.oracle.com/webfolder/technetwork/tutorials/obe/fmw/wls/12c/12c_poster/poster.html#</u>Applications using JMX to communicate to the WebLogic SSPIs at the following Website:</p>
</blockquote></li>
</ul>
<blockquote>
<p>https://docs.oracle.com/middleware/1212/wls/index.html</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Software Requirements/Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to KAAJEE-enable a Web-based application, developers require the following software:

<span id="_Toc204421608" class="anchor"></span>Table 3‑1. Dependencies—KAAJEE software requirements for development

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 31%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Category</strong></th>
<th><strong>Software</strong></th>
<th><strong>Version/Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="2">Developer Workstation</td>
<td><p>Java Integrated Development Environment (IDE)</p>
<p>Java 2 Standard Edition (J2SE) Java Development Kit (JDK)</p></td>
<td><p>Any version. Developer software installed on the workstation used for developing HealtheVet-VistA J2EE Web-based applications.</p>
<p>The JDK should include a Java Runtime Environment (JRE) and other developer tools to write Java code.</p></td>
</tr>
<tr class="even">
<td>KAAJEE SSOWAP</td>
<td>Version 8.791. Developer software installed on the workstation used for developing, running, and testing HealtheVet-VistA KAAJEE-enabled J2EE Web-based applications (see <strong>Error! Not a valid bookmark self-reference</strong>.).</td>
</tr>
<tr class="odd">
<td rowspan="3">Application Server</td>
<td>WebLogic</td>
<td>Version 12.2 and higher</td>
</tr>
<tr class="even">
<td>KAAJEE SSPIs</td>
<td>Version 8.781.</td>
</tr>
<tr class="odd">
<td>VistALink</td>
<td>Version 1.6. Developer's software is installed on WebLogic 12.2 and higher application servers used by the developer's application.</td>
</tr>
<tr class="even">
<td rowspan="2">Database</td>
<td>Oracle Database</td>
<td>Version 19c or higher (e.g., Security Service Provider Interface [SSPI])</td>
</tr>
<tr class="odd">
<td>SDS Tables</td>
<td><p>Version 19.0 or higher.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/043.png) <strong>NOTE:</strong> KAAJEE works with SDS 18.0 or higher; however, KAAJEE 1.2.0.008 distributes SDS 18.0 client jar files as part of the Sample Web Application. If you deploy both the KAAJEE Sample Web Application and your own Web-based application on the same WebLogic Application Server domain instance and intend to use a different version of SDS, those client jar files will need to be swapped out for the appropriate version of the SDS client jar files. Otherwise, There may be a conflict if both applications reference the same JNDI tree.</p></td>
</tr>
<tr class="even">
<td>VistA M Server</td>
<td>Kernel</td>
<td>Version 8.x, fully patched (see <strong>Error! Not a valid bookmark self-reference</strong>.).</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/044.png) | NOTE: Kernel is the designated custodial software application for KAAJEE; however, KAAJEE comprises multiple patches and software releases from several HealtheVet-VistA applications. |

|                                                                                                                |                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/045.png) | REF: For the specific KAAJEE software and VistA M Server patches required for the implementation of KAAJEE, please refer to Error! Not a valid bookmark self-reference. in the "Error! Not a valid bookmark self-reference." Chapter 1 in this manual. |

### Web-based Application Procedures to Implement KAAJEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Use of VistALink to Authenticate Users Based on Configured Station Numbers

> KAAJEE makes use of VistALink to authenticate a user against a specific M system, based on configured station numbers. KAAJEE relies on VistALink during the following steps:

> a\. Obtain the Java Naming and Directory Interface (JNDI) name of the VistALink connector pool (i.e., standard that provides a unified interface to multiple naming and directory services), based on the Station Number of the institution the user selects in the applications' Web login page. VistALink's institution mapping facility is used to return the JNDI name of the appropriate connector (and therefore destination M system) based on station number. The list of allowed authenticating Station Numbers is defined in the server-side deployment descriptor (i.e., kaajeeConfig.xml file).

> b\. Make Remote Procedure Calls (RPC) calls over the selected VistALink connector to the corresponding M system, to check the user's credentials (i.e., Access and Verify codes). The VistALink connector whose JNDI name was obtained in Step \#1a above is used.

> KAAJEE depends on institution mapping being set up for your VistALink connectors. J2EE Web-based application developers *must* set up connectors at every site they intend to support KAAJEE logins.

|                                                                                                                |                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/046.png) | REF: For more information on VistALink, please consult the VistALink documentation. |

#### Access VA Standard Data Services (SDS) Tables

> VA Standard Data Services (SDS) has created and maintains standardized tables in an Oracle 10*g* database (e.g., VA Institutions). These tables *must* be accessible to your Web-based application. The minimum version required is 18.0. KAAJEE uses the read-only Institution API and the data in the SDS Institution table to do the following:

- Retrieve institution display names.
- Retrieve child institutions.
- Verify if divisions share the same VistA M Server provider instance.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/047.png) | NOTE: KAAJEE works with SDS 18.0 or higher; however, KAAJEE 1.2.0.xxx distributes Standard Data Service (SDS) 18.0 client jar files as part of the Sample Web Application. If you deploy the both the KAAJEE Sample Web Application and your own Web-based application on the same WebLogic Application Server domain instance and intend to use a different version of SDS, those client jar files will need to be swapped out for the appropriate version of the SDS client jar files. Otherwise, there may be a conflict if both applications reference the same JNDI tree. |

> Therefore, the following are required:

- A Connection Pool and a Data Source needs to be created on the application server to point to the Oracle 11*g* database housing the SDS tables.

> To configure the SDS tables for a J2EE DataSource, please refer to the "Configuring for a J2EE DataSource" topic in the *SDS API Installation Guide*.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/048.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the SDS APIs, please refer to the <em>SDS API Installation Guide</em>. The SDS documentation is included in the SDS software distribution ZIP files, which are available for download at the following Website:</p>
<blockquote>
<p>http://vaww.sts.infoshare.va.gov/STS_SDS/Project%20Artifacts/Forms/AllItems.aspx</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Import KAAJEE SSOWAP Jar File

> The following jar file is present in the STAGING_FOLDER\>\\

<span id="_Ref78765853" class="anchor"></span>Table 3‑2. KAAJEE jar distribution file

|                   |                                 |
|-------------------|---------------------------------|
| Jar File Name | Description                 |
| ssowap-8.791.jar  | The KAAJEE SSOWAP java classes. |

> To import this library into your development environment, add this jar to the compiler paths of your Integrated Development Environment (IDE), ANT configuration, and/or anywhere else in your development environment that needs to know classpaths.

<span id="_Toc98223568" class="anchor"></span>Table 3‑3. Jar files and classpath defined for KAAJEE-enabled Web-based applications

| Classpath    | Description                           |
|------------------|-------------------------------------------|
| ssowap-8.791.jar | KAAJEE SSOWAP developer-related software. |

> The ssowap-8.791.jar file *must* be distributed in your application's Enterprise Archive (.ear) file with an application-level classloader.

> When you are ready to deploy/distribute your application, perform the following steps:

> a\. (required) Package the ssowap-8.791.jar (see Table 3‑2) in your application's ear file (e.g., in a "../APP-INF/lib" folder descendent from the root level of your application's ear file), along with its depencies (see below)

> b\. (required) Ensure that ssowap-8.791.jar is *not* located in a deeper level of the classloader hierarchy than that of an application, *anywhere* on the application server. Otherwise, the singletons will be instantiated with settings inappropriate for your application, and the KAAJEE security system will function inappropriately for your application.

#### Import Other Dependent Jar Files

> KAAJEE-enabled Web-based applications also have dependencies on the following jar files:

<span id="_Ref83460728" class="anchor"></span>Table 3‑4. Other required dependent jar files for KAAJEE-enabled Web-based applications

| log4j-api-2.17.1.jar    | A “PROVIDED” dependency, deployed as Shared Library                     |
|-----------------------------|-----------------------------------------------------------------------------|
| log4j-core-2.17.1.jar   | A “PROVIDED” dependency, deployed as Shared Library                     |
| vha-stddata-client-19.0.jar | (included) Two Standard Data Services (SDS) jar files (as of Version 19.0). |
| vha-stddata-basic-19.0.jar  |                                                                             |

> To import these libraries into your development environment, add all jars to the compiler paths of your IDE, ANT configuration, and/or anywhere else in your development environment that needs to know classpaths.

> Once you install VistALink on a WebLogic Application Server, both VistALink and Log4J libraries are available on a classloader that is parent to all other applications; therefore, you do not need to export these jar files in your application.

> You do, however, need to export the SDS jar files. Because they are used by the ssowap-8.791.jar, they need to be loaded via an application-level classloader in order for the consumed plugin to have visibility to them.

> Thus, when you deploy/distribute your application it is recommended that you distribute both SDS jar files

#### Import KAAJEE Login Folder

> The following files are present in the "login\\ folder contained in the

> \<STAGING_FOLDER\>\\ ssowap-8.0.791.war\\

<span id="_Toc83538904" class="anchor"></span>Table 3‑5. KAAJEE login folder files

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 33%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Directory</strong></th>
<th><strong>File Name</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>..login\</td>
<td>login.jsp</td>
<td><p>Login Web page for authentication. This is the Login Web page where users enter their Access and Verify codes and choose an Institution from a dropdown list.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/049.png) CAUTION: Consuming applications should <em>not</em> provide a direct link to the login.jsp file. Otherwise, users could get a login error message when they click on that link, see the description for navigatonerrordisplay.jsp in this table.</p></td>
</tr>
<tr class="even">
<td>..login\</td>
<td>loginCookieInfo.htm</td>
<td>Login persistent cookie information.</td>
</tr>
<tr class="odd">
<td>..login\</td>
<td>loginerror.jsp</td>
<td>J2EE Form-based Authentication error Web page for failure to authenticate J2EE Application Server login credentials.</td>
</tr>
<tr class="even">
<td>..login\</td>
<td>Loginerror403.jsp</td>
<td>KAAJEE authorization error Web page.</td>
</tr>
<tr class="odd">
<td>..login\</td>
<td>loginerrordisplay.jsp</td>
<td><p>Login error display Web page for failure to authenticate VistA M Server login credentials.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/050.png) <strong>REF:</strong> For more information on these types of errors, please refer to Chapter 10, "Troubleshooting," in this manual.</p></td>
</tr>
<tr class="even">
<td>..login\</td>
<td>navigatonerrordisplay.jsp</td>
<td><p>Error display Web page displayed after a user successfully logs into a Web application and then presses the browser <strong>Back</strong> button to get back to the KAAJEE Web login page.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/051.png) <strong>REF:</strong> For more information on this error, please refer to the "</p>
<p>Error: You navigated inappropriately to this page" topic in Chapter 10, "Troubleshooting," in this manual.</p></td>
</tr>
<tr class="odd">
<td>..login\</td>
<td>SessionTimeout.jsp</td>
<td>Login session timeout Web page.</td>
</tr>
<tr class="even">
<td>..login\images\</td>
<td>HealtheVetVistaSmallBlue.jpg</td>
<td>HealtheVet-VistA small blue logo image file.</td>
</tr>
<tr class="odd">
<td>..login\images\</td>
<td>HealtheVetVistaSmallWhite.jpg</td>
<td>HealtheVet-VistA small white logo image file.</td>
</tr>
<tr class="even">
<td>..login\javascript\</td>
<td>login.js</td>
<td><p>This JavaScript file supports functions associated with code for the KAAJEE login.jsp file. For example:</p>
<ul>
<li><blockquote>
<p>Sorting of Institutions.</p>
</blockquote></li>
<li><blockquote>
<p>Enabling/Disabling of components as part of login parameter passing.</p>
</blockquote></li>
<li><blockquote>
<p>Helper function for the Section 508 Alert dialog timeout box.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

> Import the entire "login\\ folder, including the folder itself, into your Web-based application. These files *must* be brought into your J2EE Web-based application, and distributed with it, because by the J2EE standard, any pages that are used in J2EE Form-based Authentication *must* run in the same context as the Web-based application:

|                                                                                                                |                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/052.png) | REF: For more information on how to configure your web.xml file for the login folder, please refer to "5. Configure Web-based Application for J2EE Form-based Authentication" topic in Chapter 4, "Role Design/Setup/Administration," in this manual. |

#### Section 508 Compliance Addresses Session Timeouts

> To address Section 508 compliance regarding session timeouts, KAAJEE displays an alert dialogue box warning the end-user logging in how much time remains before the session expires. This warning is displayed 30 seconds prior to the expiration of the login user's session. To provide this warning, KAAJEE utilizes JavaScript. Therefore, KAAJEE distributes a login.js file, which is exported as part of the login\javascript\\ folder.

#### Set Up KAAJEE Configuration File

> KAAJEE relies on a configuration file (i.e., kaajeeConfig.xml file) to read in all administrator-configurable settings.

> You can use the kaajeeConfig.xml file that is distributed with the KAAJEE software or you can create a KAAJEE configuration file in your J2EE Web-based application and export it along with your Web-based application.

|                                                                                                                |                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/053.png) | REF: For a sample kaajeeConfig.xml file, please refer to Figure 5‑2 in Chapter 6, "KAAJEE SSOWAP Configuration File," in this manual. |

> If you create a new KAAJEE configuration file, do the following:

> a\. (required) Create an empty XML file within your Web-based application's context root (e.g., in the WEB-INF folder). The developer can choose any name for this XML file.

> b\. (required) Set the top-level tag for the file to \<kaajee-config\>. For example:

<span id="_Toc83538907" class="anchor"></span>Figure 3‑1. Sample empty KAAJEE configuration file

> \<?xml version="1.0" encoding="UTF-8"?\>

> \<kaajee-config xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="kaajeeConfig.xsd"\>

> \</kaajee-config\>

> c\. (required) Configure the file created in the previous step (i.e., Step \#6b) by following guidelines in Chapter 6, "KAAJEE SSOWAP Configuration File," in this manual. At a minimum, the following tags *must* be configured (see Table 5‑1):

- \<kaajee-config\>.
- \<login-station-numbers\> (controls the login Web page's Institution dropdown list).
- \<context-root-name\>.

|                                                                                                                |                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/054.png) | NOTE: For every login Station Number you enter here, you also need to use VistALink's Institution Mapping to associate that login Station Number with a VistALink connector. |

|                                                                                                                   |                                                                                                                        |
|-------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/055.png) | WARNING: The context root must have a minimum of four characters following the forward slash (e.g., /kaajeeSampleApp). |

|                                                                                                                |                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/056.png) | REF: For more details, please refer to Chapter 6, "KAAJEE SSOWAP Configuration File," in this manual. |

#### Configure KAAJEE Initialization Servlet (web.xml file)

> You can place the KAAJEE configuration file anywhere within your Web-based application's context root. KAAJEE provides an initialization servlet to initialize KAAJEE.

> The classname of the servlet is:

> gov.va.med.authentication.kernel.InitKaajeeServlet

> This servlet in the web.xml file is used to:

- Pass the location and name of the KAAJEE configuration file (see Figure 3‑2) as a servlet parameter named:

> kaajee-config-file-location

- Control the sequence of startup using the \<load-on-startup\> tag.

> For example:

<span id="_Toc83538908" class="anchor"></span>Figure 3‑2. Sample excerpt of the KAAJEE web.xml file—Initialization servlet

> \<servlet\>

> \<servlet-name\>KaajeeInit\</servlet-name\>

> \<servlet-class\>gov.va.med.authentication.kernel.ssowap.InitKaajeeServlet\</servlet-class\>

> \<init-param\>

> \<param-name\>kaajee-config-file-location\</param-name\>

> \<param-value\>/WEB-INF/kaajeeConfig.xml\</param-value\>

> \</init-param\>

> \<load-on-startup\>3\</load-on-startup\>

> \</servlet\>

|                                                                                                                |                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/057.png) | REF: For a sample web.xml file, please refer to "Appendix A—Sample Deployment Descriptors" in this manual. |

#### Configure KAAJEE LoginController Servlet (web.xml file)

> The kaajee-1.2.0.xxx.jar file includes one servlet that you *must* configure in your J2EE Web-based application's web.xml file. This servlet is referenced by the Web forms in the \login folder.

> The servlet *must* be mapped to the url-pattern "/LoginController".

> Configure the servlet in your application's web.xml file, as shown below:

<span id="_Toc83538909" class="anchor"></span>Figure 3‑3. Sample excerpt of the KAAJEE web.xml file—LoginController servlet configuration

> \<servlet\>

> \<servlet-name\>LoginController\</servlet-name\>

> \<servlet-class\>gov.va.med.authentication.kernel.ssowap.LoginController\</servlet-class\>

> \<run-as\>

> \<role-name\>adminuserrole\</role-name\>

> \</run-as\>

> \</servlet\>

> \<servlet-mapping\>

> \<servlet-name\>LoginController\</servlet-name\>

> \<url-pattern\>/LoginController\</url-pattern\>

> \</servlet-mapping\>

#### Configure KAAJEE Listeners (web.xml file)

> KAAJEE has two similar listeners, both of which perform logout actions for a user. Both of these listeners are available in case one listener does not work with a specific container/platform (e.g., WebLogic, Oracle 10*g*, etc.):

<span id="_Ref134001208" class="anchor"></span>Table 3‑6. KAAJEE listeners

| Listener                   | Description                                                                                                                                                                               |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| KaajeeSessionAttributeListener | The KaajeeSessionAttributeListener listens for specific (individual) session attributes that are targeted for removal, which signals a user session ending, and performs user logout actions. |
| KaajeeHttpSessionListener      | The KaajeeHttpSessionListener listens for session destruction. It is looking for the whole session being destroyed and performs user logout actions.                                          |

> KAAJEE uses two different approaches to configure the listeners for future compatibility. While an HttpSessionAttributeListener method would be expected to be the way to retrieve the value of an attribute (in the case of the LoginUserInfoVO object) as a user session is destroyed[^4], the HttpSessionListener's sessionDestroyed method is used to provide this functionality.

> Configure these listeners in your application's web.xml file as follows (listeners in bold typeface):

<span id="_Toc167811466" class="anchor"></span>Figure 3‑4 Sample excerpt of the KAAJEE web.xml file—Listener configuration

\<listener\>

\<listener-class\>

gov.va.med.authentication.kernel.ssowap.KaajeeSessionAttributeListener

\</listener-class\>

\</listener\>

\<listener\>

\<listener-class\>

gov.va.med.authentication.kernel.ssowap.KaajeeHttpSessionListener

\</listener-class\>

\</listener\>

#### Design/Set Up Application Roles

> Some preparation is required to correctly set up application roles. The following areas are involved:

- WebLogic group mappings (weblogic.xml).

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/058.png) | REF: For a sample spreadsheet showing a mapping between WebLogic group names (i.e., principals) with J2EE security role names, please refer to "Appendix B—Mapping WebLogic Group Names with J2EE Security Role Names" in this manual. |

- VistA M Server J2EE security keys (correspond to WebLogic server group names).
- J2EE security role declarations (web.xml and weblogic.xml).
- Security constraints using J2EE security role and group names (weblogic.xml).

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/059.png) | REF: For more detailed role configuration instructions, please refer to Chapter 5, "Role Design/Setup/Administration," in this manual. |

#### Configure Log4J Logging for KAAJEE

> KAAJEE uses Log4J to log error and debugging information. It is strongly recommended that you configure your application to use Log4J (in addition to any other logging system your application is using) in order to gain access to the error and debugging information produced by KAAJEE.

> Configure Log4J logging so that KAAJEE error and/or debug messages are logged to the same file used by *all* J2EE-based applications running in the same domain on the application server. This assists users on the application server to monitor and troubleshoot KAAJEE and all other J2EE-based applications in one place.

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/060.png) | REF: For specific directions on setting up logging for KAAJEE, please refer to the "Log4J2 Configuration" section in Chapter 8, "Implementation and Maintenance," in the Implementation and Maintenance section of this documentation. |

#### Protect KAAJEE SSOWAP Web Pages

> At this point, your application is configured with KAAJEE, but has *not* yet been configured to protect any Web pages using KAAJEE. To authenticate and authorize users with KAAJEE, you need to protect the Web pages in your application by configuring J2EE Form-based Authentication in your application's web.xml file.

> Once you protect your application Web pages, KAAJEE is activated. When a user tries to access a protected Web page, if all is configured correctly, the user is redirected to the KAAJEE Web login page for Authentication and Authorization.

|                                                                                                                |                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/061.png) | REF: For information on setting up KAAJEE to protect Web pages, please refer to Chapter 4, "Role Design/Setup/Administration," in this manual. |

#### Kernel Authentication & Authorization for J2EE (KAAJEE) 1.2.0 is Single Sign-On/User Context (SSO/UC) enabled via the implementation of the CCOW user context. CCOW or Clinical Context Object Workgroup is an HL7 standard protocol designed to enable disparate applications to synchronize in real-time, and at the user-interface level. It is vendor independent and allows applications to present information at the desktop and/or portal level in a unified way. Applications that incorporate this functionality offer their users the convenience of only having to present their credentials (Access/Verify codes) once via their first signon to the SSO/UC/CCOW enabled application. Subsequent applications selected by the user, which are also SSO/UC/CCOW enabled, will not prompt the user for their credentials.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/062.png)</td>
<td><p><strong>RE</strong>F: For more information on CCOW and Single Signon/User Context (SSO/UC), refer to the Single Sign-On/User Context (SSO/UC) Deployment Guide (Kernel Patch XU*8.0*337), located on the VHA Software Document Library at the following address:</p>
<p><a href="http://www.va.gov/vdl/application.asp?appid=162">http://www.va.gov/vdl/application.asp?appid=162</a></p></td>
</tr>
</tbody>
</table>

#### Enabling Your KAAJEE SSOWAP Application

To enable your KAAJEE application, in addition to the elements required by KAAJEE, you must do the following:

1.  Modify your application’s web.xml to include the necessary elements described in the following section.
2.  Ensure your application contains a folder called ‘applets’ that contains the WebJ2Applets.jar library.
3.  Ensure that your application contains the WebJContextor.jar library.
4.  Ensure that clients of your application have the required Sentillion desktop components as described in the Single Sign-On/User Context (SSO/UC) Deployment Guide.

#### KAAJEE Sample Application with SSO/UC

For example, the sample application that comes with your distribution can be SSO/UC enabled by replacing the following web.xml file:

> \<STAGING_FOLDER\>\kaajee-1.2.0.xxx\samples\exploded\kaajeeSampleApp-1.2.0.xxxEAR\kaajeeSampleApp.war\WEB-INF\web.xml

With the following web.xml file:

> \<STAGING_FOLDER\>\kaajee-1.2.0.xxx\samples\sso-ccow\web.xml

You will then need to (re)deploy the sample application.

#### SSO/UC Elements in web.xml

Table 3‑7 lists the elements that need to be added to your web.xml file. You can find the actual elements in the file named sso-elements.txt where you can cut and paste them in your application’s web.xml file. This file can be found in your distribution, in the following directory:

> \<STAGING_FOLDER\>\kaajee-1.2.0.xxx\samples\sso-ccow\sso-elements.txt

<span id="_Ref206317550" class="anchor"></span>Table 3‑7. web.xml elements needed for SSO/UC/CCOW enabled KAAJEE Sample Application

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Category</strong></th>
<th><strong>Element</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Filters</strong></td>
<td><p>ContextInitializerFilter and its corresponding filter-mapping</p>
<p>ContextWriterFilter and its corresponding filter-mapping</p></td>
</tr>
<tr class="even">
<td><strong>Listener</strong></td>
<td>CcowHttpSessionListener</td>
</tr>
<tr class="odd">
<td><strong>Servlet</strong></td>
<td>ContextParticipantServlet and its corresponding servlet-mapping</td>
</tr>
</tbody>
</table>

Figure 3‑5 provides the contents of file sso-elements.tx which contains the elements listed in Table 3‑7.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/063.png)</td>
<td><p>ATTENTION: The order of placement of these elements is critical when building of your web.xml file. You can see the ordering of these elements in the web.xml file found in the following directory:</p>
<p>&lt;STAGING_FOLDER&gt;\kaajee-1.2.0.xxx\samples\sso-ccow\web.xml</p></td>
</tr>
</tbody>
</table>

Figure 3‑5 shows the web.xml element implementations needed for SSO/UC/CCOW enabled KAAJEE SampleWebApp:

<span id="_Ref206318736" class="anchor"></span>Figure 3‑5. web.xml element implementations needed for SSO/UC/CCOW enabled KAAJEE SampleWebApp

\

- XUS KAAJEE GET USER VIA PROXY

#### Exported Options

The following menu options are exported with KAAJEE (listed alphabetically):

<span id="_Hlt200359295" class="anchor"></span>

Table 7‑3. KAAJEE exported options

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th><strong>Option Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUCOMMAND</td>
<td><blockquote>
<p>This menu option is used to link the XUS KAAJEE WEB LOGON option. As all authenticated users have access to XUCOMMAND, this linkage enables all users to have access to all RPCs listed under the XUS KAAJEE LOGON "B"-type option.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>XUS KAAJEE WEB LOGON</td>
<td><blockquote>
<p>This "B"-type option contains references to the following RPCs in its "RPC" multiple:</p>
</blockquote>
<ul>
<li><blockquote>
<p>XUS ALLKEYS</p>
</blockquote></li>
<li><blockquote>
<p>XUS KAAJEE GET USER INFO</p>
</blockquote></li>
<li><blockquote>
<p>XUS KAAJEE LOGOUT</p>
</blockquote></li>
<li><blockquote>
<p>XUS KAAJEE GET CCOW TOKEN</p>
</blockquote></li>
</ul>
<p>This option has no effect on those RPCs as such; however, having this option assigned allows KAAJEE to call these RPCs on behalf of the end-user.</p></td>
</tr>
<tr class="odd">
<td>XUS KAAJE PROXY LOGON</td>
<td><blockquote>
<p>This "B"-type option contains references to the following RPC in its "RPC" multiple:</p>
</blockquote>
<ul>
<li><blockquote>
<p>XUS KAAJEE GET USER VIA PROXY</p>
</blockquote></li>
</ul>
<blockquote>
<p>This option has no effect on those RPCs as such; however, having this option assigned allows KAAJEE to call these RPCs on behalf of the end-user.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/103.png) | REF: For more information on KAAJEE-related RPCs, please refer to the "Remote Procedure Calls (RPCs)" topic in this chapter. |

#### Archiving and Purging

There are *no* special archiving, purging, or journaling instructions for KAAJEE.

|                                                                                                                |                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/104.png) | REF: For more information regarding the KAAJEE SSPI tables, please refer to the *KAAJEE Installation Guide*. |

#### Callable Routines

There are *no* callable VistA M Server routines exported with KAAJEE.

#### External Relations

#### HealtheVet-VistA Software Requirements

KAAJEE relies on the following HealtheVet-VistA software to run effectively (listed alphabetically):

<span id="_Hlt200359277" class="anchor"></span>

Table 7‑4. External Relations—Health*<u>e</u>*Vet-VistA software

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Software</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td>8.0</td>
<td>Server software—Fully patched.</td>
</tr>
<tr class="even">
<td>Kernel Toolkit</td>
<td>7.3</td>
<td>Server software—Fully patched.</td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td>1.1</td>
<td>Client/Server software—Fully patched.</td>
</tr>
<tr class="even">
<td>Standard Data Services (SDS)</td>
<td>18.0<br />
(or higher)</td>
<td><p>Oracle 11<em>g</em> Database and Software—Fully patched. Contains Institution-related data tables accessed via supported APIs created by SDS.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/105.png) <strong>NOTE:</strong> KAAJEE works with SDS 19.0 or higher; however, XU_8_749 distributes SDS 19.0 client jar files as part of the Sample Web Application. If you deploy the both the KAAJEE Sample Web Application and your own Web-based application on the same WebLogic Application Server domain instance and intend to use a different version of SDS, those client jar files will need to be swapped out for the appropriate version of the SDS client jar files. Otherwise, There may be a conflict if both applications reference the same JNDI tree.</p></td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>22.2</td>
<td>Server software—Fully patched.</td>
</tr>
<tr class="even">
<td>VistALink</td>
<td>1.6.1</td>
<td>Client/Server software—Fully patched.</td>
</tr>
</tbody>
</table>

#### COTS Software Requirements

The KAAJEE authorization and authentication software interface with the following Commercial-Off-The-Shelf (COTS) software products in order to run effectively (listed alphabetically):

<span id="_Hlt200359261" class="anchor"></span>

Table 7‑5. External Relations—COTS software

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 17%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Software</strong></th>
<th><strong>Version</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>WebLogic</td>
<td>12.2</td>
<td>Application server software—Fully patched.</td>
</tr>
<tr class="even">
<td>Java IDE (e.g., MyEclipse/<br />
Eclipse)</td>
<td>Any</td>
<td>Developer workstation software—The Java Integrated Development Environment (IDE) is used when developing J2EE Web-based applications that are KAAJEE-enabled.</td>
</tr>
<tr class="odd">
<td>Java 2 Standard Edition (J2SE) Java Development Kit (JDK, e.g., Sun Microsystems')</td>
<td>Java 8</td>
<td>Developer workstation software—Fully patched. The JDK is used when developing J2EE Web-based applications that are KAAJEE-enabled. The JDK should include Java Runtime Environment (JRE) and other developer tools to write Java code.</td>
</tr>
<tr class="even">
<td>Sentillion Web Software Development Kit (SDK)</td>
<td>TBD</td>
<td>Developer workstation software—The SDK is used when developing CCOW-aware and KAAJEE-enabled applications.</td>
</tr>
<tr class="odd">
<td>Sentillion Web Software Development Kit (SDK)</td>
<td>TBD</td>
<td>Developer Client Workstation software—The SDK is used when developing CCOW-aware and FatKAAT-enabled applications.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/106.png) | NOTE: There are *no* other COTS (*non*-VA) products embedded in or requiring special interfaces by this version of KAAJEE, other than those provided by the underlying operating systems. |

#### DBA Approvals and Database Integration Agreements

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are not available to the general programming public. These IAs are listed on FORUM.

KAAJEE is *not* dependent on any IAs; however, Kernel is the custodial package of KAAJEE Integration Agreement (IA) \#4851.

To obtain the current list of IAs, if any, to which the Kernel (KAAJEE-related) software is a custodian:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the Database Administrator (DBA) menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].

> 5\. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].

> 6\. When this option prompts you for a package, enter XXXX—Where XXXX equals: XU or Kernel.

> 7\. All current IAs to which the software is a custodian are listed.

To obtain detailed information on a specific integration agreement:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Inquire option \[DBA IA INQUIRY\].

> 5\. When prompted for "INTEGRATION REFERENCES," enter the specific integration agreement number of the IA you would like to display.

> 6\. The option then lists the full text of the IA you requested.

To obtain the current list of IAs, if any, to which the Kernel (KAAJEE-related) software is a subscriber:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\].

> 5\. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].

> 6\. When prompted with "START WITH SUBSCRIBING PACKAGE," enter XXXX (in uppercase). When prompted with "GO TO SUBSCRIBING PACKAGE," enter XXXX (in uppercase)—Where "XXXX" equals: XU.

> 7\. All current IAs to which the software is a subscriber are listed.

#### Internal Relations

#### Relationship of KAAJEE with the VistA M Server

#### Namespace

KAAJEE consists of VistA M Server patches that have been assigned to the following namespaces (listed alphabetically):

- XU—Kernel
- XWB—RPC Broker

In order to develop J2EE Web-based applications so that they can be authorized and authenticated against Kernel, VistALink 1.6 software *must* be installed on the application server as well as Kernel 8.0 (fully patched).

VistALink 1.6 software (i.e., XOBS 1.5; fully patched) *must* be installed on the developer workstation and the application server.

#### Software-wide and Key Variables

KAAJEE does *not* employ the use of software-wide or key variables on the VistA M Server.

#### SACC Exemptions

KAAJEE does *not* have any Programming Standards and Conventions (SAC) exemptions.

*This page is left blank intentionally.*

## Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Security Management

There are *no* special legal requirements involved in the use of Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE).

#### Mail Groups, Alerts, and Bulletins

#### Mail Groups

KAAJEE does *not* create or utilize any specific mail groups.

#### Alerts

KAAJEE does *not* make use of alerts.

#### Bulletins

KAAJEE does *not* make use of bulletins.

#### Auditing—Log Monitoring

#### Log4J Log

In test, developers use this log during Web application development as a debugging tool. It can provide detailed context for application failures. It is a complimentary tool for testing applications.

In production, the Enterprise Management Center (EMC) and/or Application Server Administrators should monitor this log. If a problem is detected and developers or the administrators are unable to resolve it, the user should call the National Help Desk and file a Remedy ticket.

#### M-side Log

This event log records VistA M Server-related errors. Information Resource Management (IRM) should monitor this log for any errors related to KAAJEE and take appropriate actions to remedy the error.

#### Sign-On Log

This event log records all users that sign onto the VistA M Server via Kernel in the SIGN-ON LOG file (#3.081). IRM should monitor this log. IRM should check for unusual activity (e.g., unusual amount of activity for a given user). If there is an unusual amount of activity for a particular user, IRM should further investigate by contacting the user in question and taking appropriate action as deemed appropriate.

#### Failed Access Attempts Log

This event log records users that fail to enter a valid Access/Verify code pair. IRM should monitor this log. IRM should check for unusual activity (e.g., unusual amount of activity for a given user). If there is an unusual amount of activity for a particular user, IRM should further investigate by contacting the user in question and taking appropriate action as deemed appropriate.

#### Remote Access/Transmissions

For every user logon, Web browser applications on the client workstation transmit/receive data using Hyper Text Transport Protocol (HTTP) to communicate with KAAJEE-enabled applications deployed on the application server.

|                                                                                                                |                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/107.png) | NOTE: HTTP rides over Transmission Control Protocol/Internet Protocol (TCP/IP) in the payload packet. |

On the application server, KAAJEE-enabled Web-based applications call the KAAJEE login/authentication component, which then calls VistALink using APIs. VistALink uses Transmission Control Protocol/Internet Protocol (TCP/IP) to transmit data to and receive data from VistA M Servers.

The KAAJEE SSPIs on the application server use Java Database Connector (JDBC) to query the remote security store database (e.g., Oracle), which holds the temporary username and password. KAAJEE also uses the SDS APIs to query tables on the remote national SDS database.

After authentication, applications can optionally make subsequent VistALink calls to run any RPCs authorized to the authenticated user.

#### Interfaces

The KAAJEE and KAAJEE SSPIs software interfaces with the following VA software:

- VistALink 1.6
- Standard Data Services (SDS) tables 19.0 (or higher).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/108.png)</td>
<td><p><strong>NOTE:</strong> KAAJEE works with SDS 19.0 or higher; If you deploy the both the KAAJEE Sample Web Application and your own Web-based application on the same WebLogic Application Server domain instance and intend to use a different version of SDS, those client jar files will need to be swapped out for the appropriate version of the SDS client jar files. Otherwise, There may be a conflict if both applications reference the same JNDI tree.address:</p>
<p>http://vaww.sts.infoshare.va.gov/STS_SDS/Project%20Artifacts/Forms/AllItems.aspx</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/109.png)</td>
<td><p><strong>REF:</strong> For more information on Common Services and SDS tables, please visit the following Website:</p>
<blockquote>
<p>http://vaww.sts.infoshare.va.gov/STS_SDS/Project%20Artifacts/Forms/AllItems.aspx</p>
</blockquote></td>
</tr>
</tbody>
</table>

KAAJEE Classic and KAAJEE SSPIs interfaces with the following *non*-VA Commercial-Off-The-Shelf (COTS) products/software:

- Oracle or Caché databases.
- WebLogic 12.2 and higher Application Servers

|                                                                                                                |                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/110.png) | NOTE: There are *no* other COTS (*non*-VA) products embedded in or requiring special interfaces by this version of KAAJEE, other than those provided by the underlying operating systems. |

#### Electronic Signatures

There are *no* electronic signatures used within KAAJEE 1.2.0.xxx.

#### Security Keys

The following VistA M Server security key is exported with KAAJEE 1.2.0.xxx:

<span id="_Ref236561832" class="anchor"></span>Table 8‑1. KAAJEE exported security keys

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Security Key</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUKAAJEE_SAMPLE</td>
<td><blockquote>
<p>This security key is exported with Kernel Patch XU*8.0*504. This security key is required in order to access the KAAJEE Sample Web Application exported with KAAJEE. First, an initial authentication occurs against a VistA M Server (i.e., Access and Verify codes). Then, if the login user passes this phase, the XUKAAJEE_SAMPLE VistA M security key is used to create a J2EE group/principal of the same name on the J2EE Application Server, if not already created. In addition, the login user will be assigned membership to this group on the J2EE Application Server during the login session. This membership is necessary as the authorization aspect of container security. It validates the role-based access by the membership of the associated group/principal.</p>
<p>The XUKAAJEE_SAMPLE security key must be assigned to users on the VistA M Server to authorize their access to the protected page of the KAAJEE sample Web application.</p>
</blockquote></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/111.png) | NOTE: KAAJEE calls the XUS ALLKEYS RPC to return all VistA M Server J2EE security keys; however, there are *no* new KAAJEE-specific VistA M Server security keys exported with this version of KAAJEE. |

#### File Security

There are *no* new file or field security changes associated with KAAJEE.

#### Contingency Planning

All sites should develop a local contingency plan to be used in the event of software/hardware problems in a production (live) environment. The contingency plan *must* identify the procedure for maintaining functionality provided by this software in the event of system outage.

#### Official Policies

There are *no* special legal requirements involved in the use of KAAJEE.

Distribution of KAAJEE is unrestricted.

As per the Software Engineering Process Group/Software Quality Assurance (SEPG/SQA) Standard Operating Procedure (SOP) 192-039—Interface Control Registration and Approval (effective 01/29/01), application programmers *must* not alter any Health*<u>e</u>*Vet VistA Class I software code.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/112.png)</td>
<td><p><strong>REF:</strong> For more information on SOP 192-039—Interface Control Registration and Approval, please refer to the following Website:</p>
<blockquote>
<p>http://vista.med.va.gov/SEPG_lib/Standard%20Operating%20Procedures/192-039%20Interface%20Control%20Registration%20and%20Approval.htm</p>
</blockquote></td>
</tr>
</tbody>
</table>

*This page is left blank intentionally.*

## Cactus Testing with KAAJEE SSOWAP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Cactus is a simple test framework for unit testing server-side Java code (servlets, Enterprise JavaBeans \[EJBs\], tag libs, filters, etc.).[^7] Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) supports testing with the Cactus container-based unit testing tool. It is possible that other container-based unit testing tools could be supported as well, but Cactus is the one that is the basis of developing KAAJEE's unit test support.

|                                                                                                                |                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/113.png) | NOTE: This chapter assumes that the reader has a basic understanding of the Jakarta Cactus unit testing tool. |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/114.png)</td>
<td><p><strong>REF:</strong> For more information on the Cactus testing tool, please visit the Jakarta Cactus Website at the following Website:</p>
<blockquote>
<p><a href="http://jakarta.apache.org/cactus/">http://jakarta.apache.org/cactus/</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Enabling Cactus Unit Test Support

To enable Cactus unit test support, do the following:

> 1\. Switch from FORM to BASIC authentication. For example, In your J2EE Web-based application's web.xml, code as follows:

<span id="_Toc204421644" class="anchor"></span>Figure 9‑1. Switching from FORM to BASIC in web.xml example

\<login-config\>

\<auth-method\>BASIC\</auth-method\>

\<form-login-config\>

\<form-login-page\>/login/login.jsp\</form-login-page\>

\<form-error-page\>login/loginerror.jsp\</form-error-page\>

\</form-login-config\> --\>

\</login-config\>

> 2\. Turn on Cactus Support in the KAAJEE configuration file, set the following tag to "true" (case sensitive):

\<cactus-insecure-mode enabled="true" /\>

|                                                                                                                   |                                                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/115.png) | This mode should *never* be enabled on a production system. It defaults to "false" unless enable is specifically set to "true" (case sensitive). |

> Essentially, this switch turns the "one-time login token" to a "many-time login token," allowing the re-use of login credentials over repeated Cactus unit tests.

> 3\. Add the normal required Cactus configuration information into your application's web.xml.

#### Using Cactus in a KAAJEE-Secured Application

There are probably several approaches to obtaining a login credential on your Cactus test client side, to use to login on the container side. Essentially:

- Start with a valid-for-login Access code, Verify code and Division.
- Pass these, on the container side, to the LoginController.getFormsAuthCredentialsForCactus().
- The return value (for valid login credentials) is an object that contains valid j_username and j_password values.

#### How do you do this?

One approach is:

> 1\. Configure both secured and unsecured Cactus test redirector servlets in your Web-based application's web.xml deployment descriptor.

> 2\. Create one Cactus test in your test suite that uses an unsecured ServletRedirector Cactus test redirector servlet. This application will gather a set of login credentials from the server.

- The beginXXX, testXXX and endXXX methods should be, sequentially in your test class source code, the first set of tests. Cactus/JUnit appear to follow source code order when sequencing test execution.
- This unsecured Cactus test should start with the Access code, Verify code, and Division. These could be hard-coded into the test class, or could be kept in a client-side configuration file, read on the client during the beginXXX method, and passed to the server-side testXXX method as session attributes.
- In the server-side testXXX method, call the KAAJEE LoginController class's static getFormsAuthCredentialsForCactus method to obtain a valid j_username and j_password value. These are returned in a KAAJEE CactusFormsAuthCredentialVO object.
- In the server-side testXXX method, you could also obtain and cache the LoginUserInfoVO object. The getFormsAuthCredentialsForCactus will put this into the testXXX method's session object if you pass that as a parameter. You need to store this somewhere on the server so you can retrieve it in subsequent testXXX methods; the example below stores it in a static class variable in the server-side version of the test class.
- Using the toString() method of the CactusFormsAuthCredentialVO object, write the credentials to the Web page output, using the servlet's PrintWriter.
- Back on the client in the endXXX method, instantiate a new CactusFormsAuthCredentialVO object, using the complete Web response as input. The CactusFormsAuthCredentialVO class can instantiate itself by looking for its own "toString" output in any given string.
- On the client side, again in the endXXX method, store these values (the CactusFormsAuthCredentialVO object provides a valid j_username and j_password) in a static class variable in the test class.

> 3\. If you are caching the LoginUserInfoVO object in the server instance of the test class, you could add code in the setUp() method (executed before every testXXX method) to put the LoginUserInfoVO object back into session, for use as needed by each testXXX method.

> 4\. For the rest of the Cactus tests in the test class, use the secured ServletRedirector (specify in the beginXXX method), and pass the credentials using a Cactus BasicAuthentication object. The testXXX methods should all run in the server context created by the login of the secure ServletRedirector.

This approach has been tested for ServletTestCase. While it should work for JspTestCase, it has not been tested.

#### Cactus ServletTestCase Example

<span id="_Toc202863047" class="anchor"></span>Figure 9‑2. Cactus ServletTestCase example

> package gov.va.med.authentication.kernel.samples;

> import java.io.IOException;

> import java.io.PrintWriter;

> import gov.va.med.authentication.kernel.CactusFormsAuthCredentialVO;

> import gov.va.med.authentication.kernel.KaajeeLoginException;

> import gov.va.med.authentication.kernel.LoginController;

> import gov.va.med.authentication.kernel.LoginUserInfoVO;

> import junit.framework.Test;

> import junit.framework.TestSuite;

> import org.apache.cactus.ServletTestCase;

> import org.apache.cactus.WebRequest;

> import org.apache.cactus.WebResponse;

> import org.apache.cactus.client.authentication.BasicAuthentication;

> publicclass TestSampleApp extends ServletTestCase {

> /\*\*

> \* Access code, Verify code, Division to transform

> \* into a valid j_username, j_password

> \*/

privatestaticfinal String userAccessCode = "good!@#\$1";

privatestaticfinal String userVerifyCode = "good!@#\$2";

privatestaticfinal String userDivision = "631";

> /\*\*

> \* To store the login credentials on the client side

> \*/

> privatestatic CactusFormsAuthCredentialVO clientCredentials;

> /\*\*

> \* To store the userInfo session object on the server side

> \* (problematic if multiple tests are running simultaneously)

> \*/

> privatestatic LoginUserInfoVO serverUserInfo;

> public TestSampleApp(String theName) {

super(theName);

}

publicstatic Test suite() {

> TestSuite testSuite = new TestSuite(TestSampleApp.class);

return testSuite;

}

> /\*\*

> \* Runs on SERVER, before every test.

> \*/

publicvoid setUp() {

> // put login user info object back into session, if

> // already cached in the static class variable.

> if (serverUserInfo!= null) {

> session.setAttribute(LoginUserInfoVO.SESSION_KEY, serverUserInfo);

}

}

> /\*\*

> \* Runs on SERVER, after every test.

> \*/

publicvoid tearDown() {

}

> /\*\*

> \* Runs on CLIENT. Communicates with server-side test execution via

> \* WebRequest. This test should use a \_unsecured\_ Cactus redirector.

> \*/

> publicvoid beginGetServerCredentials(WebRequest webRequest) {

> // use unsecured test director (depends on web.xml configuration)

> webRequest.setRedirectorName("ServletRedirector");

}

> /\*\*

> \* Runs on SERVER. Gets the j_username and j_password login

> \* credentials, and returns to client by writing to the servlet output.

> \*/

> publicvoid testGetServerCredentials() {

try {

> PrintWriter out = response.getWriter();

> // call KAAJEE to get valid j_username/j_password credentials

> // based on a/v code, division

> CactusFormsAuthCredentialVO serverCredentials =

> LoginController.getFormsAuthCredentialsForCactus(

userDivision,

> userAccessCode,

> userVerifyCode,

session);

> // return credentials to client via servlet output

> out.println("testGetServerCredentials credentials: " +

> serverCredentials.toString());

> // get LoginUserInfoVO from session; save in static

> // class variable in server side test class (not OK

> // if multiple tests are running simultaneously)

> serverUserInfo = (LoginUserInfoVO)

> session.getAttribute(LoginUserInfoVO.SESSION_KEY);

> } catch (KaajeeLoginException e) {

> //

> } catch (IOException e) {

> //

}

}

> /\*\*

> \* Runs on CLIENT. Stores login credentials returned from server

> \* in static class variable (client-side).

> \*/

> publicvoid endGetServerCredentials(WebResponse webResponse) {

> System.out.println(webResponse.getText());

> // parse, store login credentials returned from server

> clientCredentials = new

> CactusFormsAuthCredentialVO(webResponse.getText());

}

> /\*\*

> \* Runs on CLIENT. This test should use a \_secure\_ Cactus redirector,

> \* using credentials gathered by earlier test run.

> \*/

> publicvoid beginSecureLogin(WebRequest webRequest) {

> // use secured test director (depends on web.xml configuration)

> webRequest.setRedirectorName("ServletRedirectorSecure");

> // use credentials obtained previously to login

> webRequest.setAuthentication(

> new BasicAuthentication(clientCredentials.getJUsername(),

> clientCredentials.getJPassword()));

}

> /\*\*

> \* Runs on SERVER.

> \*/

> publicvoid testSecureLogin() {

> // test should be running in the KAAJEE-created container

> // security context of the KAAJEE-logged-in ServletRedirectSecure.

> //

> // Now run any tests you need, in the KAAJEE

try {

> PrintWriter out = response.getWriter();

> // display security context info

> out.println("getRemoteUser: " + request.getRemoteUser());

> } catch (IOException e) {

> //

}

}

> /\*\*

> \* Runs on CLIENT.

> \*/

> publicvoid endSecureLogin(WebResponse webResponse) {

> System.out.println(webResponse.getText());

}

> }

#### Other Approaches *Not* Recommended

It would be possible to insert a valid j_username and j_password directly into the kaajeeweblogontoken table. Reasons not to do this include:

- The LoginUserInfoVO object will not be created.
- The proper DUZ for the given Access and Verify code is guaranteed when obtained from the LoginUserInfoVO object.
- Going through the full process of translating an Access/Verify code at runtime into a login credential assures that there are no problems (login-wise) with the M account being connected to.
- The tables are purged at every server restart, destroying the credential.
- Inserting malformed credentials into the table may cause login problems.

Another approach is to use the LoginController's getFormsAuthCredentialsForCactus method to get a valid credential once, store this credential on the client, and re-use between tests. This approach has the most of the same drawbacks as the first alternate method described above.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Common Login-related Error Messages

This chapter describes some of the common Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) and VistALink-related error messages that users might encounter during the Authentication and Authorization process of KAAJEE-enabled applications. For each error message listed, we include the cause and suggest possible resolutions to correct the error. All KAAJEE/VistALink error messages are displayed in an HTML format (i.e., Web page) in any of the following template files:

- loginerror.jsp
- loginerror403.jsp
- loginerrordisplay.jsp
- navigatonerrordisplay.jsp

These files are located in the following directory:

> \<STAGING_FOLDER\>\XUS_8_695\ssowapSampleApp\login\\

The following error messages are discussed in this chapter:

- Error: You are not authorized to view this page
- Error: Forms authentication login failed
- Error: You navigated inappropriately to this page
- Error: Could not get a connection from connector pool
- Error:
- Error: Login failed due to too many invalid signon attempts
- Error:
- Error:
- Error: Logins are disabled on the M system
- Error! Not a valid bookmark self-reference.
- Error: Institution/division you selected for login is not valid for your M user account
- Error! Not a valid bookmark self-reference.

|                                                                                                                |                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/116.png) | NOTE: The error messages discussed in this chapter are *not* listed in any particular order. |

#### Error: You are not authorized to view this page

Message:

<span id="_Hlt200359194" class="anchor"></span>

Figure 10‑1. Error—Forbidden message: You are not authorized to view this page

You are not authorized to view this page

You might not have permission to view this directory or page using the credentials you supplied.

If you believe you should be able to view this directory or page, please try to contact the Website by using any e-mail address or phone number that may be listed on the localhost:8888 home page.

You can click <u>Search</u> to look for information on the Internet.

HTTP Error 403 – Forbidden  
Internet Explorer

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user attempts to access a protected resource, and instead of being prompted for their login credentials, they are immediately given a Hyper Text Transport Protocol (HTTP) Error 403 (not authorized) error (Figure 10‑1).</p>
<p>Some possible reasons that the authorization may have failed:</p>
<ul>
<li><blockquote>
<p>Lack of Proper Security Keys—The end-user's account does not have the VistA M Server J2EE security keys matching the role required for this page.</p>
</blockquote></li>
<li><blockquote>
<p>Error Retrieving User Roles—Some other error prevented proper retrieval of user roles during the login process.</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td><p>For the following situations, the user <em>must</em> contact IRM or the System Administrator for assistance:</p>
<ul>
<li><blockquote>
<p>Lack of Proper Security Keys—Get the necessary VistA M Server J2EE security keys assigned.</p>
</blockquote></li>
<li><blockquote>
<p>Error Retrieving User Roles—Check the log4J logs for any errors.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

#### Error: Forms authentication login failed

Message:

<span id="_Ref108600557" class="anchor"></span>Figure 10‑2. Error—Forms authentication login failed

Forms authentication login failed.

<u>Try login again.</u>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 86%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user enters their Access and Verify codes and presses the <strong>Login</strong> button. No obvious error is returned, but the user is sent to the loginerror.jsp error page (error message template) that states a generic message: "Forms authentication login failed." (Figure 10‑2).</p>
<p>The user was redirected by KAAJEE to the login error page. KAAJEE expects to find the loginerror.jsp in the /login folder of the application context root.</p>
<p>Some possible reasons that the authentication may have failed:</p>
<ul>
<li><blockquote>
<p>WebLogic Configuration Problem—The WebLogic Custom Security Authentication Providers are not configured correctly.</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td><p>For the following situations, the user <em>must</em> contact IRM or the System Administrator for assistance:</p>
<ul>
<li><blockquote>
<p>WebLogic Configuration Problem—If you have Log4J configured to log the gov.va.med.authentication.kernel package for DEBUG level messages, examine the Log4J log files for output from the class UserManagerImp. If no such output is present, the WebLogic Custom Security Authentication Providers are probably <em>not</em> configured correctly in weblogic.xml, or the application did not deploy correctly.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

#### Error: You navigated inappropriately to this page

Message:

<span id="_Toc204421648" class="anchor"></span>Figure 10‑3. Error—You navigated inappropriately to this page

You navigated inappropriately to this page.

The login process should only be invoked via the consuming application by using your original bookmark, shortcut or URL destination

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th>After successfully logging into the Web application, the user presses the browser <strong>Back</strong> button until they reach the level of the KAAJEE Web login page. This message is displayed by the navigatonerrordisplay.jsp.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td><blockquote>
<p>Because the user is already successfully logged into the Web application, they should just press the browser <strong>Forward</strong> button to get back to the desired Web application page.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Error: Could not get a connection from connector pool

Message:

<span id="_Hlt200359166" class="anchor"></span>

Figure 10‑4. Error—Could not get a connection from connector pool

There was a login error detected by the login system:

Error processing login credentials: Could not get a connection from connector pool for institution 'nnn'.

<u>Try login again.</u>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user enters their Access and Verify codes and presses the <strong>Login</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑4).</p>
<p>In this case, the descriptive error message stated that the system could not get a connection from the connector pool for the institution selected by the user.</p>
<p>Several possible reasons for this failure include:</p>
<ul>
<li><blockquote>
<p>No Institution mapping is configured to associate Station Number <strong>nnn</strong> (e.g., 662) with a JNDI name of a connector.</p>
</blockquote></li>
<li><blockquote>
<p>No connector exists for the mapped JNDI name returned by VistALink's Institution Mapping.</p>
</blockquote></li>
<li><blockquote>
<p>The VistA M Server to which the connector is connecting is down.</p>
</blockquote></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td>The user <em>must</em> contact IRM or the Systems Administrator for assistance. A review of the log files for both the application and the connector should further narrow down the exact cause of the failure.</td>
</tr>
</tbody>
</table>

#### Error: Error retrieving user information

Message:

<span id="_Hlt200359155" class="anchor"></span>

Figure 10‑5. Error—Error retrieving user information

There was a login error detected by the login system:

Error processing login credentials: Error retrieving user information.; Root cause exception: gov.va.med.foundations.rpc.RpcFaultException: Fault Code: 'Server'; Fault String: 'Internal Application Error'; Fault Actor: 'XUS KAAJEE GET USER INFO'; Code: '182301'; Type: 'XUS KAAJEE GET USER INFO'; Message: 'No valid DUZ found. \[Security Type: AV\]\[Access code does not match a NP entry.''

<u>Try login again.</u>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user enters their Access and Verify codes and presses the <strong>Login</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑5).</p>
<p>In this case, the descriptive error message stated that the system could not find a valid DUZ for the user. The Access code entered by the user was not found in the NEW PERSON file (#200).</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td>The user <em>must</em> contact IRM or the Systems Administrator to verify that the user is allowed access to the VistA M Server account in question and then grant the user appropriate access.</td>
</tr>
</tbody>
</table>

#### Error: User provisioning information is not available

Message:

<span id="_Ref111256294" class="anchor"></span>Figure 10‑6. Error—“VistA

![](kaajee-ssowap-deployment-guide-8-0-791/117.png)

| Cause:      | The user arrives at the application’s login page and gets presented the “VistAIDError” control.                                                   |
|-----------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Resolution: | The user *must* exercise the Link My Account functionality in order to get granted appropriate orivusuing information from the IAM/STS services.. |

#### Error: Login failed due to too many invalid signon attempts

Message:

<span id="_Hlt200359136" class="anchor"></span>

Figure 10‑7. Error—Login failed due to too many invalid logon attempts

#### There was a login error detected by the login system:

Error processing login credentials :: Could not get a connection from connector pool for institution '442'.; Root cause exception: gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: Could not perform Logon; Root cause exception: gov.va.med.vistalink.security.m.SecurityTooManyInvalidLoginAttemptsFaultException: Fault Code: 'Server'; Fault String: 'Logon Failed'; Fault Actor: ''; Code: '183005'; Type: ''; Message: 'Logon failure: 'Device/IP address is locked due to too many invalid signon attempts.''

Try login again.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user picks an institution and presses the <strong>Proceed</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑7).</p>
<p>The underlying <strong>Connector Proxy</strong> account’s Verify code is most likely expired, which has exceeded the allowed number of login attempts to the VistA M Server.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td>The user <em>must</em> contact IRM or the System Administrator for assistance.</td>
</tr>
</tbody>
</table>

#### Error: Certificate expired

Message:

<span id="_Ref111258407" class="anchor"></span>Figure 10‑8. Error—Your 2-way auth SSL certificate has expired

![](kaajee-ssowap-deployment-guide-8-0-791/118.png)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user enters picks a station number from the drop-down list and presses the <strong>Proceed</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑8).</p>
<p>Several possible reasons for this failure include:</p>
<ul>
<li><p>The certificate on the WebLogic side has expired.</p></li>
<li><p>One of the intermediary, root chain certificates has expired.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td>Update the certificate on the application server side and communicate securely to the STS team.</td>
</tr>
</tbody>
</table>

#### Error: Unable to sign on, “Try using your Access/Verify code” error

Message:

<span id="_Hlt200359113" class="anchor"></span>

Figure 10‑9. Error— Unable to sign on using Identity and Access Management STS token. Try using your Access/Verify codes:

There was a login error detected by the login system:

Unable to sign on using Identity and Access Management STS token. Try using your Access/Verify codes.

<u>Try login again.</u>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user selectes an institution and presses the <strong>Proceed</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑9).</p>
<p>Several possible reasons for this failure include:</p>
<ul>
<li><p>The SecID values in VistA and STS provisioning down’t match</p></li>
<li><p>Timezone difference (mismatch between the certificate issuing authority and the VistA).</p></li>
<li><p>The user is not allowed access to the VistA M Server in question.</p></li>
<li><p>The user was not set up correctly on the VistA M Server in question.</p></li>
</ul>
<p>For security reasons, the system does <em>not</em> specify the exact reason for an error.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td><p>The user should open a ticket with the IAM in reagrds to the Link My Account functionality for the production environments or inspect/confirm the values on the STS and VistA side for the lower environments.</p>
<p>If the error persists, the user <em>must</em> contact IRM or the System Administrator to verify that the user is allowed access to the VistA M Server account in question, inspect the presense and value of a SecID field and then grant the user appropriate access.</p></td>
</tr>
</tbody>
</table>

#### Error: Logins are disabled on the M system

Message:

<span id="_Hlt200359103" class="anchor"></span>

Figure 10‑10.  Error—Logins are disabled on the M system

There was a login error detected by the login system:

Logins are disabled on the M system.

<u>Try login again.</u>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user picks the station from the drop-down list and presses the <strong>Proceed</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑10).</p>
<p>IRM or the System Administrator has disabled logins on the VistA M Server. Logins are sometimes disabled in order to install new software or perform system maintenance.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td>The user should wait and try to log into the VistA M Server at a later time. If the user feels the time period to log back into the system is excessive, the user should contact IRM or the System Administrator for assistance.</td>
</tr>
</tbody>
</table>

#### Error: Institution/division you selected for login is not valid for your M user account

Message:

<span id="_Hlt200359079" class="anchor"></span>

Figure 10‑11. Error—Institution/division you selected for login is not valid for your M user account

There was a login error detected by the login system:

Institution/division you selected for login is not valid for your M user account; could not log you  
on.

Please contact your site manager for assistance.

More details below:

<u>Try login again.</u>

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Cause:</strong></th>
<th><p>The user selects and institution and presses the <strong>Proceed</strong> button. The user is then redirected to the loginerrordisplay.jsp error page (error message template) with a descriptive error message displayed (Figure 10‑11).</p>
<p>Several possible reasons for this failure include:</p>
<ul>
<li><p>The user does not have the selected Institution/Division entry in the DIVISION Multiple field (#16) in the NEW PERSON file (#200) entry.</p></li>
<li><p>The SDS tables could <em>not</em> validate the Division selected.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Resolution:</strong></td>
<td>The user <em>must</em> contact IRM or the System Administrator to verify that the user is allowed access to the Institution/Division in question and then grant the user appropriate access.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/119.png) | REF: For a list of other login-related error messages, please refer to the "Symptoms and Possible Solutions" topic in the VistALink *System Administration Guide*. |

|                                                                                                                |                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/120.png) | REF: For more information on the Kernel signon process and related error messages, please refer to the "Signon/Security" section in the *Kernel Systems Management Guide*. |

*This page is left blank intentionally.*

### Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Term Definition
<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 67%" />
</colgroup>
<tbody>
<tr class="odd">
<td>AA</td>
<td>Authentication and Authorization</td>
</tr>
<tr class="even">
<td>AAC</td>
<td>Formerly the Austin Automation Center. Renamed to the Austin Information Technology Center (AITC)</td>
</tr>
<tr class="odd">
<td>AAIP</td>
<td><p>Authentication and Authorization Infrastructure Program (terminated, see <a href="http://vaww.vista.med.va.gov/iss/acronyms/p-acronyms.asp#piv">PIV</a> or refer to <a href="http://vaww.vista.med.va.gov/iss/acronyms/o-acronyms.asp#ocis">OCIS</a>)</p>
<p>The Office of Human Resources and Administration is currently managing the Personal Identity Verification (<a href="http://vaww.vista.med.va.gov/iss/acronyms/p-acronyms.asp#piv">PIV</a>) project with the assistance of the Office of Security and Law Enforcement and the Office of Cyber and Information Security (OCIS). This program replaces the Authentication and Authorization Infrastructure Project (AAIP) that OCIS formally managed and has since terminated. VA will issue a Directive that will mandate use of the <a href="http://vaww.vista.med.va.gov/iss/acronyms/f-acronyms.asp#fips">FIPS</a> 201 processes and preparing a series of Handbooks (Identity Proofing, Issuance, and Privacy) to describe specific implementation roles, responsibilities, and processes as defined in <a href="http://vaww.vista.med.va.gov/iss/acronyms/f-acronyms.asp#fips">FIPS</a> 201. The <a href="http://vaww.vista.med.va.gov/iss/acronyms/p-acronyms.asp#piv">PIV</a> Program Office is working with the three Administrations to ensure all business, systems and policy requirements are adequately addressed and making a concerted effort to coordinate an enterprise-wide approach for identity and access management. Of specific interest is the need to coordinate the various requirements for identity and access management.</p></td>
</tr>
<tr class="even">
<td>Access Code</td>
<td>A password used by the Kernel system to identify the user. It is used with the verify code.</td>
</tr>
<tr class="odd">
<td>Adapter</td>
<td>Another term for resource adapter or connector.</td>
</tr>
<tr class="even">
<td>Administration Server</td>
<td>Each WebLogic server domain must have one server instance that acts as the administration server. This server is used to configure all other server instances in the domain.</td>
</tr>
<tr class="odd">
<td>AITC</td>
<td>Austin Information Technology Center</td>
</tr>
<tr class="even">
<td>Alias</td>
<td>An alternative filename.</td>
</tr>
<tr class="odd">
<td>Alpha/VMS</td>
<td><p>Alpha: Hewlett Packard computer system</p>
<p>VMS: Virtual Memory System</p></td>
</tr>
<tr class="even">
<td>Anonymous Software Directories</td>
<td>M directories where VHA application and patch zip files are placed for distribution.</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Program Interface</td>
</tr>
<tr class="even">
<td>Application Proxy User</td>
<td>A Kernel user account designed for use by an application rather than an end-user.</td>
</tr>
<tr class="odd">
<td>Application Server</td>
<td>Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</td>
</tr>
<tr class="even">
<td>ASTM</td>
<td>American Society for Testing and Materials</td>
</tr>
<tr class="odd">
<td>Authentication</td>
<td>Verifying the identity of the end-user.</td>
</tr>
<tr class="even">
<td>Authorization</td>
<td>Granting or denying user access or permission to perform a function.</td>
</tr>
<tr class="odd">
<td>Base Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a standalone adapter that is completely set up. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters). The deployer only needs to modify a subset of the linked adapters’ deployment descriptor settings. Note: This mechanism is no longer supported in WebLogic 9 and later for J2CA 1.5 adapters (e.g., VistALink 1.6).</td>
</tr>
<tr class="even">
<td>Caché</td>
<td>Caché is an M environment, a product of InterSystems Corp.</td>
</tr>
<tr class="odd">
<td>Cache/VMS</td>
<td><p>Cache: InterSystems Caché object database that runs SQL</p>
<p>VMS: Virtual Memory System</p></td>
</tr>
<tr class="even">
<td>CCI</td>
<td>Common Client Interface</td>
</tr>
<tr class="odd">
<td>CCOW</td>
<td><p>A standard defining the use of a technique called "context management," providing the clinician with a unified view on information held in separate and disparate healthcare applications that refer to the same patient, encounter or user. </p>
<p>Formerly Clinical Context Object Workgroup, now known as the CCOW Technical Committee. CCOW is an end-user-focused standard that complements HL7's traditional emphasis on data interchange and enterprise workflow. Using a technique known as context management, the clinical user's experience is one of interacting with a single system, when in fact he or she may be using multiple, independent applications from many different systems, each via its native user interface. By synchronizing and coordinating applications so that they automatically follow the user's context, the CCOW Standard serves as the basis for ensuring secure and consistent access to patient information from heterogeneous sources. The benefits include applications that are easier to use, increased utilization of electronically available information, and an increase in patient safety. Further, CCOW support for secure context management provides a healthcare standards basis for addressing HIPAA requirements. For example, CCOW enables the deployment of highly secure single sign-on solutions.</p></td>
</tr>
<tr class="even">
<td>Classpath</td>
<td>The path searched by the JVM for class definitions. The class path may be set by a command-line argument to the JVM or via an environment variable.</td>
</tr>
<tr class="odd">
<td>Client</td>
<td>Can refer to both the client workstation and the client portion of the program running on the workstation.</td>
</tr>
<tr class="even">
<td>Connection Factory</td>
<td>A J2CA class for creating connections on request.</td>
</tr>
<tr class="odd">
<td>Connection Pool</td>
<td>A cached store of connection objects that can be available on demand and reused, increasing performance and scalability. VistALink uses connection pooling when running on a J2EE server.</td>
</tr>
<tr class="even">
<td>Connector</td>
<td>A system-level driver that integrates J2EE application servers with Enterprise Information Systems (EIS). VistALink is a J2EE connector module designed to connect to Java applications with VistA/M systems. The term is used interchangeably with connector module, adapter, adapter module, and resource adapter.</td>
</tr>
<tr class="odd">
<td>Connector Proxy User</td>
<td>For security purposes, each instance of a J2EE connector must be granted access to the M server it connects to. This is done via a Kernel user account set up on the M system. This provides initial authentication for the app server and establishes a trusted connection. The M system manager must set up the connector user account and communicate the access code, verify code and listener IP address and port to the J2EE system manager.</td>
</tr>
<tr class="even">
<td>COTS</td>
<td>Commercial, Off-The-Shelf</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td>Computerized Patient Record System</td>
</tr>
<tr class="even">
<td>CSV</td>
<td>Comma-Separated Values format</td>
</tr>
<tr class="odd">
<td>DBF</td>
<td>Database file format underlying many database applications (originally dBase)</td>
</tr>
<tr class="even">
<td>DBMS</td>
<td>Database Management System</td>
</tr>
<tr class="odd">
<td>DCL</td>
<td>Digital Command Language. An interactive command and scripting language for VMS.</td>
</tr>
<tr class="even">
<td>Division</td>
<td>Division is an Institution in the INSTITUTION file (#4) that is identified via a unique Station Number. Divisions are "sub"-divisions or child sites within an integrated set of facilities, whose computing is hosted on the computer system of the primary facility. The parent-child relationship between a division and a primary facility is maintained by the ASSOCIATIONS multiple field (#14) in the INSTITUTION file (#4). A sub-division may be a medical center, clinic, or nursing home. The primary facility is also a division of itself. Clinics and nursing homes are often sub-divisions. The Station Number for child sites is 5 characters, the first 3 of which are the 3 numbers of the parent facility. For example, Livermore, CA is a medical center that is a child of Palo Alto, CA. Its Station Number is 640A4.</td>
</tr>
<tr class="odd">
<td>DSM</td>
<td>Digital Standard MUMPS. An M environment, a product of InterSystems Corp.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td>A local variable holding a number that identifies the signed-on user. The number is the Internal Entry Number (IEN) of the user’s record in the NEW PERSON file (file #200)</td>
</tr>
<tr class="odd">
<td>EAR (file)</td>
<td><em>Enterprise ARchive</em> file (.ear extension). This file has the same format as a regular .jar file. An ear file is like a zip file packaged for J2EE application deployment. The .ear file contains everything necessary to deploy an enterprise application on an application server. An ear file can contain 1-n Web modules. It contains at least one .war (Web Archive) file which contains the Web component of the application as well as the .jar (Java Archive) file. In addition, there are some deployment descriptor files in XML.<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
</tr>
<tr class="even">
<td>EIS</td>
<td>Enterprise Information System</td>
</tr>
<tr class="odd">
<td>EJB</td>
<td>Enterprise JavaBeans. Enterprise JavaBeans (EJB) technology is the server-side component architecture for the Java 2 Platform, Enterprise Edition (J2EE) platform. EJB technology enables rapid and simplified development of distributed, transactional, secure and portable applications based on Java technology.<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a></td>
</tr>
<tr class="even">
<td>EPHI</td>
<td><p>The HealtheVet-VistA architecture is a services-based architecture. Applications are constructed in tiers with distinct user interface, middle, and data tiers. Two types of services will exist:</p>
<p>Core Services—Infrastructure and data.</p>
<p>Application Services—A single logical authoritative source of data.Electronic Protected Health Information</p></td>
</tr>
<tr class="odd">
<td>FatKAAT</td>
<td>Fat-Client (i.e. Rich client) Kernel Authentication and Authorization</td>
</tr>
<tr class="even">
<td>FDA</td>
<td>FileMan Data Array</td>
</tr>
<tr class="odd">
<td>File #18</td>
<td>System file #18 was the precursor to the KERNEL SYSTEMS PARAMETERS file, and is now obsolete. It uses the same number space that is now assigned to VistALink. Therefore, file #18 must be deleted before VistALink can be installed.</td>
</tr>
<tr class="even">
<td>Global</td>
<td>A multi-dimensional data storage structure -- the mechanism for persistent data storage in a MUMPS database.</td>
</tr>
<tr class="odd">
<td>Health<em>e</em>vet-VistA</td>
<td><p>The Health<em>e</em>Vet-VistA architecture is a services-based architecture. Applications are constructed in tiers with distinct user interface, middle, and data tiers. Two types of services will exist:</p>
<ul>
<li><p>Core Services—Infrastructure and data.</p></li>
<li><p>Application Services—A single logical authoritative source of data.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>HIPAA</td>
<td>Health Insurance Portability and Accountability Act</td>
</tr>
<tr class="odd">
<td>HL7</td>
<td>Health Level 7</td>
</tr>
<tr class="even">
<td>HTTP</td>
<td>HyperText Transport Protocol</td>
</tr>
<tr class="odd">
<td>HTTP Session Object</td>
<td>Hyper Text Transport Protocol (HTTP) Session Objects are used like cookies to maintain states as Web pages are considered stateless rather than stateful.</td>
</tr>
<tr class="even">
<td>IDE</td>
<td>Integrated development environment. A suite of software tools to support writing software.</td>
</tr>
<tr class="odd">
<td>Institution</td>
<td>A Department of Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA). There are a wide variety of facility types in the INSTITUTION file, including medical centers, clinics, domiciliaries, administrative centers, Veterans Integrated Service Networks (VISNs), and so forth.</td>
</tr>
<tr class="even">
<td>Institution Mapping</td>
<td>The VistALink 1.6 release includes a small utility that administrators can use to associate station numbers with JNDI names, and which allows runtime code to retrieve the a VistALink connection factory based on station number.</td>
</tr>
<tr class="odd">
<td>IP</td>
<td>Internet Protocol</td>
</tr>
<tr class="even">
<td>ISO</td>
<td>Information Security Officer</td>
</tr>
<tr class="odd">
<td>J2CA</td>
<td>J2EE Connector Architecture. J2CA is a framework for integrating J2EE-compliant application servers with Enterprise Information Systems, such as the VHA’s VistA/M systems. It is the framework for J2EE connector modules that plug into J2EE application servers, such as the VistALink adapter.</td>
</tr>
<tr class="even">
<td>J2EE</td>
<td>The Java 2 Platform, Enterprise Edition (J2EE) is an environment for developing and deploying enterprise applications. The J2EE platform consists of a set of services, APIs, and protocols that provide the functionality for developing multi-tiered, Web-based applications. A J2EE Connector Architecture specification for building adapters to connect J2EE systems to non-J2EE enterprise information systems.</td>
</tr>
<tr class="odd">
<td>J2SE</td>
<td>Java 2 Standard Edition. Sun Microsystem’s programming platform based on the Java programming language. It is the blueprint for building Java applications, and includes the Java Development Kit (JDK) and Java Runtime Environment (JRE).</td>
</tr>
<tr class="even">
<td>JAAS</td>
<td>Java Authentication and Authorization Service. JAAS is a pluggable Java framework for user authentication and authorization, enabling services to authenticate and enforce access controls upon users.</td>
</tr>
<tr class="odd">
<td>JAR file</td>
<td>Java archive file. It is a file format based on the ZIP file format, used to aggregate many files into one.</td>
</tr>
<tr class="even">
<td>JAVA</td>
<td>Java is a programming language. It can be used to complete applications that may run on a single computer or be distributed among servers and clients in a network.</td>
</tr>
<tr class="odd">
<td>Java Library</td>
<td>A library of Java classes usually distributed in JAR format.</td>
</tr>
<tr class="even">
<td>JavaBeans</td>
<td>JavaBeans expose methods, properties, and events, which can then be accessed by other components or scripts. JavaBeans are commonly mistaken for design patterns as they both use similar conventions (e.g., both use Setter and Getter methods). A JavaBean is a reusable component that can be used in any Java application development environment. JavaBeans are dropped into an application container, such as a form, and can perform functions ranging from a simple animation to complex calculations.<a href="#fn3" class="footnote-ref" id="fnref3" role="doc-noteref"><sup>3</sup></a></td>
</tr>
<tr class="odd">
<td>Javadoc</td>
<td>Javadoc is a tool for generating API documentation in HTML format from doc comments in source code. Documentation produced with this tool is typically called Javadoc.</td>
</tr>
<tr class="even">
<td>JBoss</td>
<td>JBoss is a free software / open source Java EE-based application server.</td>
</tr>
<tr class="odd">
<td>JCA CCI</td>
<td>J2EE Connector Architecture Common Client Interface</td>
</tr>
<tr class="even">
<td>JDBC</td>
<td>Java Database Connector. JDBC technology is an API (included in both J2SE and J2EE releases) that provides cross-DBMS connectivity to a wide range of SQL databases and access to other tabular data sources, such as spreadsheets or flat files. With a JDBC technology-enabled driver, you can connect all corporate data even in a heterogeneous environment.<a href="#fn4" class="footnote-ref" id="fnref4" role="doc-noteref"><sup>4</sup></a></td>
</tr>
<tr class="odd">
<td>JDK</td>
<td>Java Development Kit. A set of programming tools for developing Java applications.</td>
</tr>
<tr class="even">
<td>JMX</td>
<td>Java Management eXtensions. A java specification for building manageability into java applications, including J2EE-based ones.</td>
</tr>
<tr class="odd">
<td>JNDI</td>
<td>Java Naming and Directory Interface. A protocol to a set of APIs for multiple naming and directory services.</td>
</tr>
<tr class="even">
<td>JRE</td>
<td>The <em>Java Runtime Environment</em> consists of the Java virtual machine, the Java platform core classes, and supporting files. JRE is bundled with the JDK but also available packaged separately.</td>
</tr>
<tr class="odd">
<td>JSP</td>
<td>Java Server Pages. A language for building web interfaces for interacting with web applications.</td>
</tr>
<tr class="even">
<td>JSP</td>
<td><em>Java Server Pages.</em></td>
</tr>
<tr class="odd">
<td>JVM</td>
<td>Java Virtual Machine. The JVM interprets compiled Java binary code (byte code) for specific computer hardware.</td>
</tr>
<tr class="even">
<td>KAAJEE</td>
<td>Kernel Authentication and Authorization for Java 2 Enterprise Edition</td>
</tr>
<tr class="odd">
<td>KaajeeVistaLinkConnection<br />
Spec</td>
<td><p>KAAJEE currently maintains this VistALink class and uses it to connect to the VistA M Server. This class extends VistaLinkConnectionSpecImpl. In other words, it inherits from the VistALink class VistaLinkConnectionSpecImpl. KAAJEE has added additional code in order to handle the IP address.</p>
<p>![](kaajee-ssowap-deployment-guide-8-0-791/121.png) NOTE: In the future, VistALink may incorporate and maintain this code.</p></td>
</tr>
<tr class="even">
<td>KERNEL</td>
<td>A facility is multidivisional if it supports one or more divisions. HealtheVet-VistA applications are required to be multidivisional-aware. Thus, it <em>must</em> be designed to work correctly at a multi-divisional facility.Set of VistA software routines that function as an intermediary between the host operating system and the VistA application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.</td>
</tr>
<tr class="odd">
<td>KIDS</td>
<td>Oracle 9i (or higher version) is a relational database that supports the Structured Query Language (SQL), now an industry standard. Currently, it is used to store the KAAJEE SSPIs.Kernel Installation and Distribution System. The VistA/M module for exporting new VistA software packages.</td>
</tr>
<tr class="even">
<td>LDAP</td>
<td>Acronym for Lightweight Directory Access Protocol. LDAP is an open protocol that permits applications running on various platforms to access information from directories hosted by any type of server.</td>
</tr>
<tr class="odd">
<td>Linked Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a standalone adapter that is completely set up. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters). The deployer only needs to modify a subset of linked adapters’ deployment descriptor settings. Note: This mechanism is no longer supported in WebLogic 9 and later for J2CA 1.5 adapters (e.g., VistALink 1.6).</td>
</tr>
<tr class="even">
<td>Linux</td>
<td>An <a href="http://www.webopedia.com/TERM/L/open_source.html">open-source</a> <a href="http://www.webopedia.com/TERM/L/operating_system.html">operating system</a> that runs on various types of hardware <a href="http://www.webopedia.com/TERM/L/platform.html">platforms</a>. HealtheVet-VistA servers use both Linux and Windows operating systems.</td>
</tr>
<tr class="odd">
<td>Listener</td>
<td>A socket routine that runs continuously at a specified port to field incoming requests. It sends requests to a front controller for processing. The controller returns its response to the client through the same port. The listener creates a separate thread for each request, so it can accept and forward requests from multiple clients concurrently.</td>
</tr>
<tr class="even">
<td>log4J Utility</td>
<td>An open-source logging package distributed under the Apache Software license. Reviewing log files produced at runtime can be helpful in debugging and troubleshooting.</td>
</tr>
<tr class="odd">
<td>logger</td>
<td>In log4j, a logger is a named entry in a hierarchy of loggers. The names in the hierarchy typically follow Java package naming conventions. Application code can select a particular logger by name to write output to, and administrators can configure where a particular named logger’s output is sent.</td>
</tr>
<tr class="even">
<td>M (MUMPS)</td>
<td>Massachusetts General Hospital Utility Multi-programming System, abbreviated M. M is a high-level procedural programming computer language, especially helpful for manipulating textual data.</td>
</tr>
<tr class="odd">
<td>Managed Server</td>
<td>A server instance in a WebLogic domain that is not an administration server, i.e., not used to configure all other server instances in the domain.</td>
</tr>
<tr class="even">
<td>MBeans</td>
<td>In the Java programming language, an MBean (managed bean) is a Java object that represents a manageable resource, such as an application, a service, a component, or a device. MBeans must be concrete Java classes.</td>
</tr>
<tr class="odd">
<td>Messaging</td>
<td>A framework for one application to asynchronously deliver data to another application, typically using a queuing mechanism.</td>
</tr>
<tr class="even">
<td>Multidivisional</td>
<td>A facility is multidivisional if it supports one or more divisions. Health<em><u>e</u></em>Vet-VistA applications are required to be multidivisional-aware. Thus, it <em>must</em> be designed to work correctly at a multi-divisional facility.</td>
</tr>
<tr class="odd">
<td>Multiple</td>
<td>A VA FileMan data type that allows more than one value for a single entry.</td>
</tr>
<tr class="even">
<td>Namespace</td>
<td>A unique 2-4 character prefix for each VistA package. The DBA assigns this character string for developers to use in naming a package’s routines, options, and other elements. The namespace includes a number space, a pre-defined range of numbers that package files must stay within.</td>
</tr>
<tr class="odd">
<td>NEW PERSON (#200) FILE</td>
<td>A VistA file that contains data on employees, users, practitioners, etc. of the VA.</td>
</tr>
<tr class="even">
<td>NIST</td>
<td>National Institute for Standards and Technology</td>
</tr>
<tr class="odd">
<td>OCIS</td>
<td>Office of Cyber and Information Security</td>
</tr>
<tr class="even">
<td>OI</td>
<td>Office of Information</td>
</tr>
<tr class="odd">
<td>OI&amp;T</td>
<td>Office of Information &amp; Technology</td>
</tr>
<tr class="even">
<td>ORACLE 10<em>g</em></td>
<td>Oracle is a relational database that supports the Structured Query Language (SQL), now an industry standard.</td>
</tr>
<tr class="odd">
<td>OS</td>
<td>Operating System</td>
</tr>
<tr class="even">
<td>OS&amp;LE</td>
<td>Office of Security and Law Enforcement</td>
</tr>
<tr class="odd">
<td>Patch</td>
<td>An update to a VistA software package that contains an enhancement or bug fix. Patches can include code updates, documentation updates, and information updates. Patches are applied to the programs on M systems by IRM services.</td>
</tr>
<tr class="even">
<td>PHI</td>
<td>Protected Health Information</td>
</tr>
<tr class="odd">
<td>PIV</td>
<td>Personal Identity Verification</td>
</tr>
<tr class="even">
<td>Primary Facility</td>
<td>Primary facilities, also called Parent Facilities, are always medical centers, and they have a three-digit Station Number. a primary facility may be a standalone medical center, or it may be the parent facility of an integrated set of facilities, often called a healthcare network. For example, Palo Alto, CA is the headquarters of the Palo Alto Healthcare Network (HCN). Its Station Number is 640. An integrated set of facilities always falls within the boundary of a VISN.</td>
</tr>
<tr class="odd">
<td>Production</td>
<td>A system on which <em>some</em> production (i.e., "live" data) is stored, accessed, and/or updated.</td>
</tr>
<tr class="even">
<td>ra.xml</td>
<td>ra.xml is the standard J2EE deployment descriptor for J2CA connectors. It describes connector-related attributes and its deployment properties using a standard DTD (Document Type Definition) from Sun.</td>
</tr>
<tr class="odd">
<td>Re-authentication</td>
<td>When using a J2CA connector, the process of switching the security context of the connector from the original application connector "user" to the actual end-user. This is done by the calling application supplying a proper set of user credentials.</td>
</tr>
<tr class="even">
<td>Resource Adapter</td>
<td>J2EE resource adapter modules are system-level drivers that integrate J2EE application servers with Enterprise Information Systems (EIS). This term is used interchangeably with resource adapter and connector.</td>
</tr>
<tr class="odd">
<td>RM</td>
<td>Requirements Management</td>
</tr>
<tr class="even">
<td>Routine</td>
<td>A program or sequence of computer instructions that may have some general or frequent use. M routines are groups of program lines that are saved, loaded, and called as a single unit with a specific name.</td>
</tr>
<tr class="odd">
<td>RPC</td>
<td>Remote Procedure Call. A defined call to M code that runs on an M server. A client application, through the RPC Broker, can make a call to the M server and execute an RPC on the M server. Through this mechanism a client application can send data to an M server, execute code on an M server, or retrieve data from an M server</td>
</tr>
<tr class="even">
<td>RPC Broker</td>
<td>The RPC Broker is a client/server system within VistA. It establishes a common and consistent framework for client-server applications to communicate and exchange data with VistA/M servers.</td>
</tr>
<tr class="odd">
<td>RPC Security</td>
<td>All RPCs are secured with an RPC context (a "B"-type option). An end-user executing an RPC must have the "B"-type option associated with the RPC in the user’s menu tree. Otherwise an exception is thrown.</td>
</tr>
<tr class="even">
<td>S&amp;OCS</td>
<td>Security &amp; Other Common Services</td>
</tr>
<tr class="odd">
<td>SAD</td>
<td>Software Architecture Document</td>
</tr>
<tr class="even">
<td>SDD</td>
<td>Software Design Document</td>
</tr>
<tr class="odd">
<td>SE&amp;I</td>
<td>Software Engineering &amp; Integration</td>
</tr>
<tr class="even">
<td>Servlet</td>
<td>A Java program that resides on a server and executes requests from client web pages.</td>
</tr>
<tr class="odd">
<td>Singleton</td>
<td>"An object that cannot be instantiated. A singleton can be created, but it can't be instantiated by developers—meaning that the singleton class has control over how it is created. The restriction on the singleton is that there can be only one instance of a singleton created by the Java Virtual Machine (JVM)."<a href="#fn5" class="footnote-ref" id="fnref5" role="doc-noteref"><sup>5</sup></a></td>
</tr>
<tr class="even">
<td>Socket</td>
<td>An operating system object that connects application requests to network protocols.</td>
</tr>
<tr class="odd">
<td>SPI</td>
<td>J2CA service provider interface Service-Level Contract</td>
</tr>
<tr class="even">
<td>SRS</td>
<td>Software Requirements Specification</td>
</tr>
<tr class="odd">
<td>SSL</td>
<td>Secure Socket Layer. A low-level protocol that enables secure communications between a server and a browser. It provides communication privacy.</td>
</tr>
<tr class="even">
<td>SSO/UC</td>
<td>Single Sign-On/User Context</td>
</tr>
<tr class="odd">
<td>SSPI</td>
<td>Security Service Provider Interface</td>
</tr>
<tr class="even">
<td>STATION NUMBER</td>
<td>A Station Number uniquely identifies every VA primary facility and division; however, entries for some facility types do not have Station Numbers. Station Numbers are stored in Field #99 in the VistA M Server INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td>TCP/IP</td>
<td>Transmission Control Protocol (TCP) and the Internet Protocol (IP)</td>
</tr>
<tr class="even">
<td>Term</td>
<td>Definition</td>
</tr>
<tr class="odd">
<td>TEST</td>
<td>A system on which <em>no</em> production (i.e., "live" data) is stored, accessed, and/or updated.</td>
</tr>
<tr class="even">
<td>TREEMAPS</td>
<td>TreeMaps are like name/value pairs. They are sorted by the keys. There are other types of maps as well (e.g., map, hashmap, hashtable, collection, etc.). TreeMaps have a Put and a Get method; therefore, you can use the Put method and pass in a key and an object. An object can be like any object (e.g., value object).</td>
</tr>
<tr class="odd">
<td>TRM</td>
<td>The Technical Reference Model</td>
</tr>
<tr class="even">
<td>TXT</td>
<td>Text file format</td>
</tr>
<tr class="odd">
<td>UI</td>
<td>User Interface</td>
</tr>
<tr class="even">
<td>UML</td>
<td>Unified Modeling Language is a standardized specification language for object modeling.</td>
</tr>
<tr class="odd">
<td>URL</td>
<td>Uniform Resource Locator</td>
</tr>
<tr class="even">
<td>User Provisioning</td>
<td>User account management—Create, modify, and delete user accounts and privileges (e.g., definition by roles and rules) for access to computer system resources. Enterprises typically use user provisioning to manage internal user access.<a href="#fn6" class="footnote-ref" id="fnref6" role="doc-noteref"><sup>6</sup></a></td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Department of Veterans Affairs</td>
</tr>
<tr class="even">
<td>VACO</td>
<td>Veterans Affairs Central Office</td>
</tr>
<tr class="odd">
<td>Value Object</td>
<td>Value Objects (VO) allow programs to store values for different elements where they can be extracted later using a method. They follow certain design patterns.</td>
</tr>
<tr class="even">
<td>Verify Code</td>
<td>A password used in tandem with the access code to provide secure user access. The Kernel’s Sign-on/Security system uses the verify code to validate the user's identity.</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Veterans Integrated Service Network(s)</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture. The VHA’s portfolio of M-based application software used by all VA medical centers and associated facilities.</td>
</tr>
<tr class="even">
<td>VistALink (VL)</td>
<td>VistaLink is a runtime and development tool providing connection and data conversion between Java and M applications in client-server and n-tier architectures, to which this document describes the architecture and design.</td>
</tr>
<tr class="odd">
<td>VistALink Libraries</td>
<td>Classes written specifically for VistALink.</td>
</tr>
<tr class="even">
<td>VMS</td>
<td>Virtual Memory System. An operating system, originally designed by DEC (now owned by Hewlett-Packard), that operates on the VAX and Alpha architectures.</td>
</tr>
<tr class="odd">
<td>VPFS</td>
<td>Veterans Personal Finance System. The re-hosted Integrated Patient Funds (IPF) software (a.k.a. Personal Funds of Patients [PFOP]) that is written in J2EE and planned to run on a centralized system. A Web browser front-end will be used for the user interface.</td>
</tr>
<tr class="even">
<td>VPID</td>
<td>VA Person Identifier. A new enterprise-level identifier uniquely identifying VA ‘persons’ across the entire VA domain.</td>
</tr>
<tr class="odd">
<td>WAR (file)</td>
<td>Web ARchive file (.war extension). Web Modules are packaged in .war files. A war file does not need to contain jsps and/or html content. A war file can be deployed by itself.</td>
</tr>
<tr class="even">
<td>WebLogic</td>
<td>WebLogic is a J2EE Platform application server.</td>
</tr>
<tr class="odd">
<td>WebSphere</td>
<td>WebSphere Application Server (WAS) is and IBM application server.</td>
</tr>
<tr class="even">
<td>WLU</td>
<td>WebLogic Server Upgrade project</td>
</tr>
<tr class="odd">
<td>XLS</td>
<td>Microsoft Office XL worksheet and workbook file format</td>
</tr>
<tr class="even">
<td>XML</td>
<td>Extensible Markup Language</td>
</tr>
<tr class="odd">
<td>XmlBeans</td>
<td>XMLBeans is a Java-to-XML binding framework which is part of the Apache Software Foundation XML project.</td>
</tr>
<tr class="even">
<td>XOB Namespace</td>
<td>The VistALink namespace. All VistALink programs and their elements begin with the characters "XOB."</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>Derived from a question (What's an .ear file) posed by John Zukowski and defined by Mobushir Hingorjo on 3/6/00 (modified 8/4/00) and available on the following Web page: <u>http://www.jguru.com/faq/view.jsp?EID=21097.</u><a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>Definition from the following Sun Microsystems WebWeb site: <u>http://java.sun.com/products/ejb/.</u><a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn3"><p>Definition of JavaBean from the following Glossary Web site: <u>http://www.orafaq.com/glossary/faqglosj.htm,</u> 7/17/04, Revision 2.1; Author: Frank Naudé.<a href="#fnref3" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn4"><p>Definition from the following Sun Microsystems WebWeb site: <u>http://java.sun.com/products/jdbc/.</u><a href="#fnref4" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn5"><p>Definition taken from the "Java Coffee Break" Web site: <a href="http://www.javacoffeebreak.com/articles/designpatterns/">http://www.javacoffeebreak.com/articles/designpatterns/</a><a href="#fnref5" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn6"><p>Definition taken from the following Web site: <a href="http://www.biu.ac.il/Computing/security/glossary%20of%20useful%20terms.htm">http://www.biu.ac.il/Computing/security/glossary%20of%20useful%20terms.htm</a> (based on www. Gartner.com)<a href="#fnref6" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kaajee-ssowap-deployment-guide-8-0-791/122.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the Glossary Web page at the following Web address:</p>
<blockquote>
<p>http://vaww.vista.med.va.gov/iss/glossary.asp</p>
</blockquote>
<p>For a comprehensive list of acronyms, please visit the Acronyms Web site at the following Web address:</p>
<blockquote>
<p>http://vaww.vista.med.va.gov/iss/acronyms/index.asp</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Appendix A—Sample Deployment Descriptors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/123.png) | REF: For a sample of the kaajeeConfig.xml file, please refer to Figure 5‑2 in chapter 6, "KAAJEE SSOWAP Configuration File," in this manual. |

application.xml

<span id="_Toc167811497" class="anchor"></span>Figure A-1. Sample KAAJEE Deployment Descriptor: application.xml file (e.g., KAAJEE sample application)

\<?xml version="1.0" encoding="UTF-8"?\>

\<!DOCTYPE application PUBLIC "-//Sun Microsystems, Inc.//DTD J2EE Application 1.3//EN" "http://java.sun.com/dtd/application_1_3.dtd"\>

\<application\>

\<display-name\>ssowapSampleEar\</display-name\>

\<module\>

\<web\>

\<web-uri\> ssowap-8.0.791.war\</web-uri\>

\<context-root\>/ssowapSampleApp\</context-root\>

\</web\>

\</module\>

\</application\>

Application developers would customize this sample descriptor for their use by replacing the following information with information specific to their application:

- \<display-name\> Tag—Replace "KaajeeSampleEar" ear file name with the name of your application ear file.
- \<web-uri\> Tag—Replace "kaajeeSampleApp.war" war file name with the name of your application war file.
- \<context-root\> Tag—Replace "/kaajeeSampleApp" root directory with the name of your application root directory.

web.xml

<span id="figure_a_4" class="anchor"></span>Figure A-2. Sample KAAJEE Deployment Descriptor: web.xml file (e.g., PATS application)

\<?xml version='1.0' encoding='UTF-8'?\>

\<web-app xmlns="http://java.sun.com/xml/ns/javaee"

xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

xsi:schemaLocation="http://java.sun.com/xml/ns/javaee

http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"

version="2.5"\>

\<listener\>

\<listener-class\>

gov.va.med.authentication.kernel.ssowap.KaajeeSessionAttributeListener

\</listener-class\>

\</listener\>

\<listener\>

\<listener-class\>

gov.va.med.authentication.kernel.ssowap.KaajeeHttpSessionListener

\</listener-class\>

\</listener\>

\<servlet\>

\<servlet-name\>SampleAppInit\</servlet-name\>

\<servlet-class\>gov.va.med.authentication.kernel.ssowap.samples.InitSampleAppServlet\</servlet-class\>

\<load-on-startup\>1\</load-on-startup\>

\</servlet\>

\<servlet\>

\<servlet-name\>KaajeeInit\</servlet-name\>

\<servlet-class\>gov.va.med.authentication.kernel.ssowap.InitKaajeeServlet\</servlet-class\>

\<init-param\>

\<param-name\>kaajee-config-file-location\</param-name\>

\<param-value\>/WEB-INF/kaajeeConfig.xml\</param-value\>

\</init-param\>

\<load-on-startup\>3\</load-on-startup\>

\</servlet\>

\<servlet\>

\<servlet-name\>LoginController\</servlet-name\>

\<servlet-class\>gov.va.med.authentication.kernel.ssowap.LoginController\</servlet-class\>

\<init-param\>

\<param-name\>debugFlag\</param-name\>

\<param-value\>True\</param-value\>

\</init-param\>

\<run-as\>

\<role-name\>adminuserrole\</role-name\>

\</run-as\>

\</servlet\>

\<servlet-mapping\>

\<servlet-name\>LoginController\</servlet-name\>

\<url-pattern\>/LoginController\</url-pattern\>

\</servlet-mapping\>

\<session-config\>

\<session-timeout\>7\</session-timeout\>

\</session-config\>

\<error-page\>

\<error-code\>403\</error-code\>

\<location\>/login/loginerror403.jsp\</location\>

\</error-page\>

\<error-page\>

\<error-code\>404\</error-code\>

\<location\>/AppErrorPage.jsp\</location\>

\</error-page\>

\<security-constraint\>

\<web-resource-collection\>

\<web-resource-name\>SSOWAP Login Page\</web-resource-name\>

\<url-pattern\>/login/\*\</url-pattern\>

\<http-method\>GET\</http-method\>

\<http-method\>POST\</http-method\>

\</web-resource-collection\>

\<user-data-constraint\>

\

- \<url-pattern\> Tag—Replace "/AppHelloWorld.jsp" security constraint URL with your application's security constraint URL.
- \<role-name\> Tag—Replace "XUKAAJEE_SAMPLE_ROLE" security constraint role name with your application's security constraint role name.
- \<user-data-constraint\>  
  > \<transport-guarantee\> Tag—Replace "NONE" with "CONFIDENTIAL" to put your page in SSL.

|                                                                                                                |                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/124.png) | NOTE: For the KAAJEE Login Page, use 'CONFIDENTIAL' when possible. |

- \<security-role\> Tag (multiple):
- \<description\> Tag—Replace/add all security role descriptions (e.g., "KERNEL KAAJEE Sample role") with your application's security role descriptions.
- \<role-name\> Tag—Replace/add all security role names (e.g., "XUKAAJEE_SAMPLE_ROLE") with your application's security role names.

weblogic.xml

The BEA weblogic.xml file is used to map security role names (i.e., \<security-role\> element entries in the web.xml file) to users and/or groups (i.e., principals); KAAJEE only uses groups. The WebLogic Application Server will only allow mapped security roles access to protected URL resources.

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/125.png) | REF: For a sample spreadsheet showing a mapping between WebLogic group names (i.e., principals) with J2EE security role names, please refer to "Appendix B—Mapping WebLogic Group Names with J2EE Security Role Names" in this manual. |

<span id="_Toc167811499" class="anchor"></span>Figure A-3. Sample KAAJEE Deployment Descriptor: weblogic.xml file (e.g., KAAJEE Sample Web Application)

\<?xml version="1.0" encoding="UTF-8"?\>

\<weblogic-web-app xmlns="http://www.bea.com/ns/weblogic/10" xmlns:wls="http://www.bea.com/ns/weblogic/10" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/web-app_2_4.xsd http://www.bea.com/ns/weblogic/10 http://www.bea.com/ns/weblogic/103/weblogic-web-app.xsd"\>

\<run-as-role-assignment\>

\<role-name\>adminuserrole\</role-name\>

\<run-as-principal-name\>SSOWAP_USER\</run-as-principal-name\>

\</run-as-role-assignment\>

\<security-role-assignment\>

\<role-name\>XUKAAJEE_SAMPLE_ROLE\</role-name\>

\<principal-name\>XUKAAJEE_SAMPLE\</principal-name\>

\</security-role-assignment\>

\<session-descriptor\>

\<cookie-name\>ssowapJSESSIONID\</cookie-name\>

\</session-descriptor\>

\<context-root\>swap\</context-root\>

\</weblogic-web-app\>

Application developers would customize this sample descriptor for their use by replacing the following information with information specific to their application:

- \<security-role-assignment\> Tag:
- \<role-name\> Tag—Replace "XUKAAJEE_SAMPLE_ROLE" security role assignment role name with your application's security role assignment role name.
- \<principal-name\> Tag—Replace "XUKAAJEE_SAMPLE" security role assignment principal name with your application's security role assignment principal name.
- \<session-param\> Tag:
- \<param-value\> Tag—Replace "ssowapJSESSIONID" security param value with your application's param value.

|                                                                                                                |                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/126.png) | NOTE: Creating the weblogic.xml deployment descriptor is optional. If you do not include this file, or include the file but do not include mappings for all security roles, all security roles without mappings will default to any user or group whose name matches the role name.[^8] |

### Appendix B—Mapping WebLogic Group Names with J2EE Security Role Names

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table supersedes the role_mapping_worksheet.xls as delivered with XU_8_749. The role_mapping_worksheet.xls Microsoft Excel spreadsheet is located in the following directory:

> \<STAGING_FOLDER\>\kaajee-1.2.0.xxx\dd_examples

<span id="_Hlt200358995" class="anchor"></span>

Table B-1. Sample spreadsheet showing a mapping between WebLogic group names and J2EE security role names

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Security Key Name</strong></th>
<th><strong>WebLogic Group Name<br />
</strong><em>(via WebLogic Console)</em></th>
<th><strong>&lt;security-role-assignment&gt;<br />
subelement &lt;principal-name&gt;<br />
(i.e., group name)<br />
<br />
From: WebLogic group name...<br />
</strong><em>(weblogic.xml)</em></th>
<th><strong>&lt;security-role-assignment&gt;<br />
subelement &lt;role-name&gt;<br />
<br />
...To: J2EE security role name<br />
</strong><em>(weblogic.xml)</em></th>
<th><strong>J2EE &lt;security-role&gt;<br />
role-name<br />
</strong><em>(web.xml, ejb-jar.xml, application.xml)</em></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="3"><strong>&lt;--------------- (WebLogic Group Names [a.k.a. Principals]) --------------&gt;</strong></td>
<td colspan="2"><strong>&lt;---------------- (J2EE Security Role Names) -------------------&gt;</strong></td>
</tr>
<tr class="even">
<td>DG-CLERK</td>
<td>DG-CLERK</td>
<td>DG-CLERK</td>
<td>CLERK</td>
<td>CLERK</td>
</tr>
<tr class="odd">
<td>DG-SUPERVISOR</td>
<td>DG-SUPERVISOR</td>
<td>DG-SUPERVISOR</td>
<td>SUPER</td>
<td>SUPER</td>
</tr>
<tr class="even">
<td>DG-ADMIN</td>
<td>DG-ADMIN</td>
<td>DG-ADMIN</td>
<td>ADMIN</td>
<td>ADMIN</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kaajee-ssowap-deployment-guide-8-0-791/127.png) | NOTE: The \<security-role-assignment\> elements in the weblogic.xml file are not needed when the \<role-name\> element and the \<principal-name\> element are the same. By default, WebLogic automatically creates a group of the same name if no mapping is defined in weblogic.xml. |

### Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A
Ability for the User to Switch Divisions, 7-10
Access Code
Not Valid (Error Message), 11-8
Access VA Standard Data Services (SDS) Tables, 4-3
Acronyms
Home Page Web Address, Glossary, 13
ACTIVE by Custodial Package Option, 8-14
Administer
Roles, 5-6
Users, 5-6
Adobe
Home Page Web Address, xv
Adobe Acrobat Quick Guide
Home Page Web Address, xv
Alerts, 9-1
All Divisions at the Login Division's Computing Facility, 7-11
Announcement Text, Sample, 6-4
Apache
Jakarta Cactus
Website, 10-1
Jakarta Project
Home Page Web Address, 4-7
APIs
Institution getVistaProvider(), 7-1, 7-2
APP PROXY ALLOWED Field (#.11), 8-11
Appendix A—Sample Deployment Descriptors, A, 1
Appendix B—Mapping WebLogic Group Names with J2EE Security Role Names
B, 1
Application Involvement in User/Role Management, 7-1
Application Servers
WebLogic, 1-2, 3-3, 4-1, 4-2, 9-3
application.xml File, A, 1
Archiving, 8-12
ASIS Documents
Log4j Guidelines Website, 8-6
Assumptions
About the Reader, xiv
When Implementing KAAJEE, 4-1
Auditing
Log Monitoring, 9-1
Authentication
J2EE Form-based, 1-8
J2EE Form-based Authentication, 1-8
J2EE Web-based Applications, 1-10
Authorization failed for your user account on the M system (Error Message), 11-6
B
Broker
Namespace, 8-15
Bulletins, 9-1
C
Cactus Testing
Enabling Cactus Unit Test Support, 10-1
KAAJEE, 10-1
Other Approaches Not Recommended, 10-6
ServletTestCase Example, 10-4
Using Cactus in a KAAJEE-Secured Application, 10-2
Callable Routines, 8-12
CCOW, 8-13
Functionality Enabled, 4-15
classloader, 4-6, 4-7
Common Login-related Error Messages, 11-1
Configuration File, 6-1
Elements, 6-1
Configuring
KAAJEE
Configuration File, 4-9, 4-10, 4-11, 6-5
Initialization Servlet (web.xml), 4-10
Listeners (web.xml), 4-12
LoginController Servlet (web.xml), 4-11
KAAJEE Login Server Requirements, 8-4
kaajeeConfig.xml File, 3-9, 4-9, 6-1, 7-11
Log4J, 8-5
Logging for KAAJEE, 4-13
Login Division, 1-2, 2-1, 7-11
SDS Tables, 4-4
Security Provider, 1-6
web.xml File, 4-11, 4-13
Web-based Application for J2EE Form-based Authentication, 5-4
Connections, 9-2
ConnectionSpec
VistALink Connection Specs for Subsequent VistALink Calls, 7-10
VistaLinkDuzConnectionSpec, 7-10
Connector Pool, 7-10
Constructor Summary
LoginUserInfoVO Object, 7-3
VistaDivisionVO Object, 7-9
Constructors
LoginUserInfoVO(), 7-3
VistaDivisionVO(), 7-9
Container-enforced Security Interfaces, J2EE, 7-1
Contents, v
Contingency Planning, 9-4
Cookie
Information, 1-17
COTS Software Requirements, 8-13
Could not
Get a connection from connector pool (Error Message), 11-4
Match you with your M account (Error Message), 11-9
Create VistA M Server J2EE security keys Corresponding to WebLogic Group Names, 5-3
Custodial Package Menu, 8-14
D
DBA Approvals and Integration Agreements, 8-14
DBA IA CUSTODIAL MENU, 8-14
DBA IA CUSTODIAL Option, 8-14
DBA IA INQUIRY Option, 8-14
DBA IA ISC Menu, 8-14
DBA IA SUBSCRIBER MENU, 8-14
DBA IA SUBSCRIBER Option, 8-14
DBA Menu, 8-14
Declare
Groups (weblogic.xml file), 5-2
J2EE Security Role Names, 5-3
Default Division
Providing Helper Function for User's Default Division Enhancement, 2-1
Delete
KAAJEE SSPI Tables, 8-4
Dependencies
KAAJEE, 1-4
KAAJEE and VistALink, 3-2
Software, 4-2
Deployment Descriptors
application.xml File, A, 1
Samples, A, 1
web.xml File
A, 1, 4
weblogic.xml File
A, 4
Design/Set Up Application Roles, 4-13
Developer
KAAJEE Installation, 3-1
Workstation
Platform Requirements, 3-1
Developer's Guide, II-1
DIEDIT Option, 5-3
DIVISION Multiple Field (#16), 7-11, 11-10
Divisions
From a User's New Person File, 7-11
Providing Helper Function for User's Default Division Enhancement, 2-1
Switching
All Divisions at the Login Division's Computing Facility, 7-11
Divisions from a User's New Person File, 7-11
Providing the Ability for the User to Switch Divisions, 7-10
Documentation
Revisions, iii
E
ear File, 4-6, 4-7, 5-3
Glossary, 4
Electronic Signatures, 9-3
Enabling
Cactus Unit Test Support, 10-1
Enforce Failed Login Attempt Limit Issue, 2-1
Enhancements
KAAJEE, 2-1
Providing Helper Function for User's Default Division, 2-1
Enter or Edit File Entries Option, 5-3
Enter/Edit Kernel Site Parameters Option, 8-2
EPS Anonymous Directories, 3-4
Error logging on or retrieving user information (Error Message), 11-11
Error retrieving user information (Error Message), 11-5
Errors
Authorization failed for your user account on the M system, 11-6
Could not
Get a connection from connector pool, 11-4
Match you with your M account, 11-9
Error logging on or retrieving user information, 11-11
Error retrieving user information, 11-5
Forms authentication login failed, 11-2
Institution/division you selected for login is not valid for your M user account, 11-10
Login failed due to too many invalid logon attempts, 11-7
Login-related, 11-1
Logins are disabled on the M system, 11-9
Not a valid ACCESS CODE/VERIFY CODE pair, 11-8
You are not authorized to view this page, 11-2, 11-3
Your verify code has expired or needs changing, 11-7
EVS Anonymous Directories, xv
Examples
KAAJEE Configuration File, 6-5
Exemptions
SAC, 8-15
Exported Options, 8-11
External Relations, 8-12
F
Failed
Access Attempts Log, 8-8, 9-2
Login Attempt Limit, Enforcement Issue, 2-1
FatKAAT
Download Home Page Web Address, 3-4
Features
KAAJEE, 1-2
Fields
APP PROXY ALLOWED (#.11), 8-11
DIVISION Multiple (#16), 7-11, 11-10
LoginUserInfoVO Object, 7-3
SEND TO J2EE (#.05), 5-3, 8-8, 8-10
SESSION_KEY, 7-3
Figures and Tables, ix
FileMan File Protection, 9-4
Files
application.xml, A, 1
Configuration File Elements, 6-1
ear, 4-6, 4-7, 5-3
Glossary, 4
HealtheVetVistaSmallBlue.jpg, 4-9
HealtheVetVistaSmallWhite.jpg, 4-9
INSTITUTION (#4), 7-5, 7-9
Glossary, 3, 5, 11
j2ee.jar, 4-6
jaxen-full.jar, 4-6
jdbc.properties, 4-4, 4-5
KAAJEE
Configuration, 4-9, 4-10, 4-11, 10-1
Example, 6-5
Distribution Zip, 4-5, 4-8
Jar, 4-5
kaajee-1.0.0.019.jar, 3-6, 4-5, 4-6, 4-7, 4-11
kaajeeConfig.xml, 3-9, 4-9, 6-1, 7-11
KERNEL SYSTEM PARAMETERS (#8989.3), 7-2, 7-5, 8-2
Log4J, 4-6
log4j-1.2.8.jar, 4-6
login.jsp, 4-8
loginCookieInfo.htm, 4-8
loginerror.jsp, 4-8
loginerrordisplay.jsp, 4-8
logout.jsp, 7-11
NAME COMPONENTS (#20), 7-4, 7-5
navigationerrordisplay.jsp, 4-8
NEW PERSON (#200), 6-3, 7-1, 7-2, 7-4, 7-5, 7-10, 7-11, 8-11, 11-10
REMOTE PROCEDURE (#8994), 8-10
saxpath.jar, 4-6
SDS jar, 4-7
Security, 9-4
SECURITY KEY (#19.1), 5-3, 8-8, 8-10
SessionTimeout.jsp, 4-9
SIGN-ON LOG (#3.081), 1-3, 7-11, 8-8, 8-9, 9-2
vha-stddata-basic-13.0.jar, 4-5, 4-7
vha-stddata-client-13.0.jar, 4-5, 4-7
war, 5-3
Glossary, 4, 12
web.xml, 1-2, 4-11, 4-13, 4-14, 5-1, 7-1, 10-1, 10-2, 11-3
A, 1, 4
weblogic.jar, 4-6
weblogic.xml, 1-2, 1-3, 3-8, 4-13, 5-1, 5-2, 5-3, 7-1, 8-10, 11-3
A, 4
Files and Fields, 8-10, 8-11
Formats
J2EE Username, 7-1
Forms authentication login failed (Error Message), 11-2
Functionality
CCOW Functionality Enabled, 4-15
Future Enhancements
KAAJEE, 2-1
Providing Helper Function for User's Default Division, 2-1
Purge KAAJEE SSPI Tables at System Startup, 2-2
Support Change Verify Code, 2-1
G
getIsDefault Method, 7-9
getLoginDivisionVistaProviderDivisions() Method, 7-4, 7-11
getLoginStationNumber() Method, 7-4
getName Method, 7-9
getNumber Method, 7-9
getPermittedNewPersonFileDivisions() Method, 7-4, 7-11
getUserDegree() Method, 7-4
getUserDuz() Method, 7-4
getUserFirstName() Method, 7-5
getUserLastName() Method, 7-5
getUserMiddleName() Method, 7-5
getUserName01() Method, 7-5
getUserNameDisplay() Method, 7-5
getUserParentAdministrativeFacilityStationNumber() Method, 7-5
getUserParentComputerSystemStationNumber() Method, 7-5
getUserPrefix() Method, 7-5
getUserSuffix() Method, 7-5
Globals
Mapping, 8-10
Translation, 8-10
Glossary, 1
Home Page Web Address, Glossary, 13
gov.va.med.authentication.kernel Package, 11-3
Grant Special Group to All Authenticated Users (Magic Role), 5-5
Groups, 1-2, 4-13, 5-3, 5-5, 8-10
Declare, 5-2
Guidelines
Programming, 7-1
H
HealtheVet-VistA Software Requirements, 8-12
HealtheVetVistaSmallBlue.jpg File, 4-9
HealtheVetVistaSmallWhite.jpg File, 4-9
Home Pages
Acronyms Home Page Web Address, Glossary, 13
Adobe Acrobat Quick Guide Web Address, xv
Adobe Home Page Web Address, xv
Apache
Jakarta Cactus Website, 10-1
Jakarta Project Web Address, 4-7
ASIS Documents
Log4j Guidelines Website, 8-6
FatKAAT
Download Home Page Web Address, 3-4
Glossary Home Page Web Address, Glossary, 13
KAAJEE
Home Page Web Address, xv
Kernel
RPCs Website, 8-10
SDS Home Page Web Address, 4-5, 9-3
SDS Website, 4-4, 4-5, 7-1, 9-3
SOP 192-039 Website, 9-5
VHA CSO Website, 3-2
VHA Software Document Library (VDL)
Home Page Web Address, xv, 1-3
IFR Home Page Web Address, 8-3
VistALink
Website, xv
VistALink Home Page Web Address, 8-6
WebLogic
Documentation Website, 1-6, 4-1
How to
Use this Manual, xiii
HTTP, 1-8, 3-8, 7-2, 9-2, 11-2
Session Object, 7-2
HttpSessionAttributeListener method, 4-12
HttpSessionListener's sessionDestroyed Method, 4-12
Hyper Text Transport Protocol (HTTP), 1-8, 3-8, 7-2, 9-2, 11-2
I
Images
HealtheVetVistaSmallBlue.jpg, 4-9
HealtheVetVistaSmallWhite.jpg, 4-9
Implementation and Maintenance (J2EE Site), 8-1
Import
KAAJEE Jar Files, 4-5
KAAJEE Login Folder, 4-8
Other Dependent Jar Files, 4-6
Inquire Option, 8-14
Installation
KAAJEE Developer Instructions, 3-1
KAAJEE Virgin Installation, 3-3
INSTITUTION File (#4), 7-5, 7-9
Glossary, 3, 5, 11
Institution getVistaProvider() API, 7-1, 7-2
Institution.getVistaProvider Method, 7-11
Institution/division you selected for login is not valid for your M user account (Error Message), 11-10
Instructions
Installing KAAJEE for Development, 3-1
KAAJEE Virgin Installation, 3-3
Integrating KAAJEE with an Application, 4-1
Integration Agreements, 8-14
Integration Agreements Menu Option, 8-14
Interfaces, 9-3
Internal Relations, 8-15
Introduction
KAAJEE, 1-1
Introductory Text
Suggested System Announcement Text, 6-4
isCallerInRole Method, 7-1
Issues
Enforce Failed Login Attempt Limit, 2-1
Outstanding, 2-1
KAAJEE, 2-1
isUserInRole Method, 5-1, 7-1
J
J2EE
Container-enforced Security Interfaces, 7-1
Form-based Authentication, 1-8
Username Format, 7-1
Web-based Application Authentication Login Page, 1-10
j2ee.jar File, 4-6
Java Server Page Web Page Sample, 7-6
JavaBean Example
VistaDivisionVO Object, 7-9
jaxen-full.jar File, 4-6
jdbc.properties File, 4-4, 4-5
JNDI, 6-1, 7-10, 11-4
Journaling
Globals, 8-10
JSP Web Page Sample, 7-6
K
KAAJEE
Cactus Testing, 10-1
Configuration File, 4-9, 4-10, 4-11, 6-1, 10-1
Elements, 6-1
Example, 6-5
Dependencies, 4-2
Distribution Zip File, 4-5, 4-8
Features, 1-2
Future Enhancements, 2-1
Home Page Web Address, xv
Installation
Developers, 3-1
Virgin Installation, 3-3
Interfaces, 9-3
Introduction, 1-1
Listeners, 4-12, 7-11
Namespace, 8-1, 8-15
Outstanding Issues, 2-1
Overview, 1-1
Remote Access/Transmissions, 9-2
Software
Dependencies for Consuming Applications, 1-4
Requirements, 4-2
SSPI Tables
Deleting Entries, 8-4
Troubleshooting, 11-1
VistA M Server Patch Dependencies, 1-4
VistALink Dependencies, 3-2
kaajee-1.0.0.019.jar File, 3-6, 4-5, 4-6, 4-7, 4-11
kaajeeConfig.xml File, 3-9, 4-9, 6-1, 7-11
KaajeeHttpSessionListener Listener, 4-12
KaajeeSessionAttributeListener Listener, 4-12
KAAJEEWEBLOGONTOKEN Table, 10-6
Kernel
Namespace, 8-15
Patches
XU\*8.0\*451, 1-4, 9-4
RPC Website, 8-10
KERNEL SYSTEM PARAMETERS File (#8989.3), 7-2, 7-5, 8-2
Key Variables, 8-15
Keys, xiv, 9-4
VistA M Server J2EE security keys, 1-2, 3-8, 4-13, 5-1, 5-2, 5-3, 5-5, 5-6, 8-8, 9-4, 11-2
VistA M Server J2EE Security Keys, 5-3
VistA M Server Security Keys, 5-6
XUKAAJEE_SAMPLE, 9-4
L
Listeners
KAAJEE, 4-12, 7-11
KaajeeHttpSessionListener, 4-12
KaajeeSessionAttributeListener, 4-12
Log4J, 4-1, 4-7, 4-13, 11-3
Configuration, 8-5
File, 4-6
Log, 8-6, 9-1, 11-3
log4j-1.2.8.jar File, 4-6
Logging Utility, Apache Jakarta Project, 4-6
Login
Attempt Limit, Enforcement of Failed Attempts Issue, 2-1
Error Messages, 11-1
Parameter Passing for J2EE Web-based Applications, 1-13
Persistent Cookie Information, 1-17
Procedures for J2EE Web-based Applications, 1-12
Screen
J2EE Web-based Application Authentication, 1-10
Login failed due to too many invalid logon attempts (Error Message), 11-7
login.jsp, 4-8
loginCookieInfo.htm File, 4-8
loginerror.jsp File, 4-8
loginerrordisplay.jsp File, 4-8
Logins
KAAJEE Login Server Requirements, 8-4
Logins are disabled on the M system (Error Message), 11-9
LoginUserInfoVO Object, 2-1, 4-12, 6-3, 7-2, 7-10, 7-11, 10-2, 10-3, 10-6
Constructor Summary, 7-3
Field Summary, 7-3
Methods, 7-5, 7-8
LoginUserInfoVO() Constructor, 7-3
LoginUserInfoVO.SESSION_KEY String, 7-2
logout.jsp File, 7-11
Logouts, 7-11
KAAJEE, 8-9
Logs
Failed Access Attempts, 8-8, 9-2
Log4J, 8-6, 9-1
Monitoring, 8-6, 9-1
M-side, 8-8, 9-1
Sign-On, 8-8, 9-2
M
Magic Role, 5-5
Mail Groups, 9-1
Maintenance and Implementation (J2EE), 8-1
Mapping
Globals, 8-10
J2EE Security Role Names to WebLogic Group Names (weblogic.xml), 5-3
MBeanMaker Utility, 1-6
Menus
Custodial Package Menu, 8-14
DBA, 8-14
DBA IA CUSTODIAL MENU, 8-14
DBA IA ISC, 8-14
DBA IA SUBSCRIBER MENU, 8-14
DBA Option, 8-14
Integration Agreements Menu, 8-14
Subscriber Package Menu, 8-14
XUCOMMAND, 5-6, 8-11
Messages
Authorization failed for your user account on the M system, 11-6
Could not
Get a connection from connector pool, 11-4
Match you with your M account, 11-9
Error logging on or retrieving user information, 11-11
Error retrieving user information, 11-5
Forms authentication login failed, 11-2
Institution/division you selected for login is not valid for your M user account, 11-10
Login failed due to too many invalid logon attempts, 11-7
Logins are disabled on the M system, 11-9
Not a valid ACCESS CODE/VERIFY CODE pair, 11-8
You are not authorized to view this page, 11-2, 11-3
Your verify code has expired or needs changing, 11-7
Methods
getIsDefault(), 7-9
getLoginDivisionVistaProviderDivisions(), 7-4, 7-11
getLoginStationNumber(), 7-4
getName(), 7-9
getNumber(), 7-9
getPermittedNewPersonFileDivisions(), 7-4, 7-11
getUserDegree(), 7-4
getUserDuz(), 7-4
getUserFirstName(), 7-5
getUserLastName(), 7-5
getUserMiddleName(), 7-5
getUserName01(), 7-5
getUserNameDisplay(), 7-5
getUserParentAdministrativeFacilityStationNumber(), 7-5
getUserParentComputerSystemStationNumber(), 7-5
getUserPrefix(), 7-5
getUserSuffix(), 7-5
HttpSessionAttributeListener, 4-12
HttpSessionListener's sessionDestroyed, 4-12
Institution.getVistaProvider, 7-11
isCallerInRole, 7-1
isUserInRole, 5-1, 7-1
LoginUserInfoVO Object, 7-5, 7-8
toString()
LoginUserInfoVO Object, 7-5
VistaDivisionVO Object, 7-9
VistaDivisionVO Object, 7-9
Monitoring
Logs, 8-6, 9-1
M-side Log, 8-8, 9-1
N
NAME COMPONENTS File (#20), 7-4, 7-5
Namespace
KAAJEE, 8-1, 8-15
navigationerrordisplay.jsp File, 4-8
NEW PERSON File (#200), 6-3, 7-1, 7-2, 7-4, 7-5, 7-10, 7-11, 8-11, 11-10
Not a valid ACCESS CODE/VERIFY CODE pair (Error Message), 11-8
O
Objects
LoginUserInfoVO, 2-1, 4-12, 6-3, 7-2, 7-10, 7-11, 10-2, 10-3, 10-6
Constructor Summary, 7-3
Field Summary, 7-3
Methods, 7-5, 7-8
Value, 7-2
VistaDivisionVO, 7-8
Constructor Summary, 7-9
JavaBean Example, 7-9
Methods, 7-9
Official Policies, 9-4
Options
ACTIVE by Custodial Package, 8-14
Custodial Package Menu, 8-14
DBA, 8-14
DBA IA CUSTODIAL, 8-14
DBA IA CUSTODIAL MENU, 8-14
DBA IA INQUIRY, 8-14
DBA IA ISC, 8-14
DBA IA SUBSCRIBER MENU, 8-14
DBA IA SUBSCRIBER Option, 8-14
DBA Option, 8-14
DIEDIT, 5-3
Enter or Edit File Entries, 5-3
Enter/Edit Kernel Site Parameters, 8-2
Exported, 8-11
Inquire, 8-14
Integration Agreements Menu, 8-14
Print ACTIVE by Subscribing Package, 8-14
Subscriber Package Menu, 8-14
XUCOMMAND, 5-6, 8-11
XUS KAAJEE WEB LOGON, 5-6, 8-11
XUSITEPARM, 8-2
Orientation, xiii
Other Approaches Not Recommended
Cactus Testing, 10-6
Outstanding Issues, 2-1
KAAJEE, 2-1
Overview
KAAJEE, 1-1
P
Packages
gov.va.med.authentication.kernel, 11-3
Page not authorized (Error Message), 11-2, 11-3
Parameter Passing
Login, 1-13
Patches
KAAJEE, 1-4
Revisions, iv
XU\*8.0\*451, 1-4, 9-4
Persistent Cookie
Information, 1-17
Policies, Official, 9-4
Preliminary Considerations
Developer Workstation Requirements, 3-1
Principals, 1-6, 5-1, 4
Print ACTIVE by Subscribing Package Option, 8-14
Procedures
Login, 1-12
Paramter Passing, 1-13
Logouts, 7-11
Signon, 1-12
Parameter Passing, 1-13
Web-based Application Procedures to Implement KAAJEE, 4-3
Programming Guidelines, 7-1
Protecting
Globals, 8-10
KAAJEE Web Pages, 4-14
Resources in Your J2EE Application, 5-5
Purging, 8-12
KAAJEE SSPI Tables at System Startup, 2-2
R
Reader
Assumptions About the, xiv
Reference Materials, xv
Relations of KAAJEE-related Software
External, 8-12
Internal, 8-15
VistA M Server, 8-15
Remote Access/Transmissions, 9-2
Connections, 9-2
Remote Procedure Calls (RPCs), 8-8
REMOTE PROCEDURE File (#8994), 8-10
Revision History, iii
Documentation, iii
Patches, iv
Roles
Administering, 5-6
Application Involvement in User/Role Management, 7-1
Design/Setup/Administration, 5-1
Magic Role, 5-5
Routines
Callable, 8-12
RPC Broker
Namespace, 8-15
RPCs, 8-8
Kernel RPC Website, 8-10
XUS ALLKEYS, 8-8
XUS CCOW VAULT PARAM, 8-11
XUS FATKAAT SERVERINFO, 8-11
XUS KAAJEE GET USER INFO, 8-8
XUS KAAJEE LOGOUT, 7-11, 8-9
S
SAC Exemptions, 8-15
saxpath.jar File, 4-6
SDS
Home Page Web Address, 4-5, 9-3
jar Files, 4-7
Website, 4-4, 4-5, 7-1, 9-3
Security, 9-1
Files, 9-4
Keys, xiv, 9-4
VistA M Server J2EE security keys, 1-2, 3-8, 4-13, 5-1, 5-2, 5-3, 5-5, 5-6, 8-8, 9-4, 11-2
VistA M Server J2EE Security Keys, 5-3
VistA M Server Security Keys, 5-6
Management, 9-1
SECURITY KEY File (#19.1), 5-3, 8-8, 8-10
Security Keys
XUKAAJEE_SAMPLE, 9-4
Security Service Provider Interfaces (SSPI), 1-5
SEND TO J2EE Field (#.05), 5-3, 8-8, 8-10
ServletTestCase Example
Cactus Testing, 10-4
SESSION_KEY Field, 7-3
SessionTimeout.jsp File, 4-9
Set Up
KAAJEE Configuration File, 4-9
Signatures, Electronic, 9-3
Signon
Parameter Passing for J2EE Web-based Applications, 1-13
Procedures for J2EE Web-based Applications, 1-12
SIGN-ON LOG File (#3.081), 1-3, 7-11, 8-8, 8-9, 9-2
singletons, 4-6
Software
Dependencies, 4-2
KAAJEE and VistALink, 3-2
KAAJEE Dependencies, 1-4
KAAJEE Software Dependencies for Consuming Applications, 1-4
Product Security, 9-1
Requirements, 4-2
COTS, 8-13
HealtheVet-VistA, 8-12
Variables, 8-15
XOBS V. 1.5 (VistALink), 8-15
SOP 192-039
Website, 9-5
SSPI, 1-5
Standard Data Services (SDS) Institution Utilities, 7-11
Strings
LoginUserInfoVO.SESSION_KEY, 7-2
Subscriber Package Menu Option, 8-14
Suggested System Announcement Text, 6-4
Support for
Change Verify Code, 2-1
Switching Divisions
Providing the Ability for the User to Switch Divisions, 7-10
System Announcement Text, Sample, 6-4
Systems Management Guide, III-1
T
Table of Contents, v
Tables
Deleting KAAJEE SSPI Table Entries, 8-4
KAAJEEWEBLOGONTOKEN, 10-6
Tables and Figures, ix
Testing
Cactus Testing for KAAJEE, 10-1
There was a login error detected by the login system
Authorization failed for your user account on the M system (Error Message), 11-6
Could not
Get a connection from connector pool (Error Message), 11-4
match you with your M account (Error Message), 11-9
Error logging on or retrieving user information (Error Message), 11-11
Error retrieving user information (Error Message), 11-5
Institution/division you selected for login is not valid for your M user account (Error Message), 11-10
Login failed due to too many invalid logon attempts (Error Message), 11-7
Logins are disabled on the M system (Error Message), 11-9
Not a valid ACCESS CODE/VERIFY CODE pair (Error Message), 11-8
Your verify code has expired or needs changing (Error Message), 11-7
toString Method
VistaDivisionVO Object, 7-9
toString() Method
LoginUserInfoVO Object, 7-5
Translation
Globals, 8-10
Troubleshooting
Authorization failed for your user account on the M system, 11-6
Could not
Get a connection from connector pool, 11-4
Match you with your M account, 11-9
Error logging on or retrieving user information, 11-11
Error retrieving user information, 11-5
Forms authentication login failed, 11-2
Institution/division you selected for login is not valid for your M user account, 11-10
KAAJEE, 11-1
Login failed due to too many invalid logon attempts, 11-7
Logins are disabled on the M system, 11-9
Not a valid ACCESS CODE/VERIFY CODE pair, 11-8
You are not authorized to view this page, 11-2, 11-3
Your verify code has expired or needs changing, 11-7
U
URLs
Acronyms Home Page Web Address, Glossary, 13
Adobe Acrobat Quick Guide Web Address, xv
Adobe Home Page Web Address, xv
Apache
Jakarta Cactus Website, 10-1
Jakarta Project Web Address, 4-7
ASIS Documents
Log4j Guidelines Website, 8-6
FatKAAT
Download Home Page Web Address, 3-4
Glossary Home Page Web Address, Glossary, 13
KAAJEE
Home Page Web Address, xv
Kernel
RPCs Website, 8-10
SDS Home Page Web Address, 4-5, 9-3
SDS Website, 4-4, 4-5, 7-1, 9-3
SOP 192-039
Website, 9-5
VHA CSO Website, 3-2
VHA Software Document Library (VDL)
Home Page Web Address, xv, 1-3
IFR Home Page Web Address, 8-3
VistALink Home Page Web Address, 8-6
WebLogic
Documentation Website, 1-6, 4-1
Use of VistALink to Authenticate Users Based on Configured Station Numbers, 4-3
User Guide, I-1
Username
J2EE Format, 7-1
Users
Administering, 5-6
Application Involvement in User/Role Management, 7-1
Using Cactus in a KAAJEE-Secured Application, 10-2
Utilities
Logging Utility, Apache Jakarta Project, 4-6
MBeanMaker, 1-6
Standard Data Services (SDS) Institution Utilities, 7-11
V
VA FileMan File Protection, 9-4
Value Object, 7-2
Variables
Key, 8-15
Software-wide, 8-15
Verify Code
Expired (Error Message), 11-7
Not Valid (Error Message), 11-8
VHA CSO
Website, 3-2
VHA Software Document Library (VDL)
Home Page Web Address, xv, 1-3
IFR Home Page Web Address, 8-3
vha-stddata-basic-13.0.jar File, 4-5, 4-7
vha-stddata-client-13.0.jar File, 4-5, 4-7
VistA M Server
J2EE security keys, 1-2, 3-8, 4-13, 5-1, 5-2, 5-3, 5-5, 5-6, 8-8, 9-4, 11-2
J2EE Security Keys, 5-3
Security Keys, 5-6
VistaDivisionVO Object, 7-8
Constructor Summary, 7-9
JavaBean Example, 7-9
Methods, 7-9
VistaDivisionVO() Constructor, 7-9
VistALink
Connection Specs for Subsequent VistALink Calls, 7-10
Connector Pool, 7-10
VistaLinkDuzConnectionSpec, 7-10
XOBS V. 1.5, 8-15
VistALink Home Page Web Address, xv, 8-6
VistaLinkDuzConnectionSpec, 7-10
VistALink's Institution Mapping, 4-10, 6-1, 11-4
VPID, 1-2, 7-2, 7-10
W
war File, 5-3
Glossary, 4, 12
Web Pages
Acronyms Home Page Web Address, Glossary, 13
Adobe Acrobat Quick Guide Web Address, xv
Adobe Home Page Web Address, xv
Apache
Jakarta Cactus Website, 10-1
Jakarta Project Home Page Web Address, 4-7
ASIS Documents
Log4j Guidelines Website, 8-6
FatKAAT
Download Home Page Web Address, 3-4
Glossary Home Page Web Address, Glossary, 13
KAAJEE
Home Page Web Address, xv
Kernel
RPC Website, 8-10
SDS Home Page Web Address, 4-5, 9-3
SDS Website, 4-4, 4-5, 7-1, 9-3
SOP 192-039 Website, 9-5
VHA CSO Website, 3-2
VHA Software Document Library (VDL)
Home Page Web Address, xv, 1-3
IFR Home Page Web Address, 8-3
VistALink
Website, xv
VistALink Home Page Web Address, 8-6
WebLogic
Documentation Website, 1-6, 4-1
web.xml File, 1-2, 4-11, 4-13, 4-14, 5-1, 7-1, 10-1, 10-2, 11-3
A, 1, 4
Web-based
Application Procedures to Implement KAAJEE, 4-3
Authentication, 1-10
WebLogic
Application Server, 1-2, 3-3, 4-1, 4-2, 9-3
Documentation
Website, 1-6
Documentation Website, 4-1
KAAJEE Login Server Requirements, 8-4
weblogic.jar, 4-6
weblogic.xml File, 1-2, 1-3, 3-8, 4-13, 5-1, 5-2, 5-3, 7-1, 8-10, 11-3
A, 4
X
XML
application.xml File, A, 1
web.xml File
A, 1, 4
weblogic.xml File
A, 4
XUCOMMAND Menu, 5-6, 8-11
XUKAAJEE_SAMPLE Security Key, 9-4
XUS ALLKEYS RPC, 8-8
XUS CCOW VAULT PARAM RPC, 8-11
XUS FATKAAT SERVERINFO RPC, 8-11
XUS KAAJEE GET USER INFO RPC, 8-8
XUS KAAJEE LOGOUT RPC, 7-11, 8-9
XUS KAAJEE WEB LOGON Option, 5-6, 8-11
XUSITEPARM Option, 8-2
Y
You are not authorized to view this page (Error Message), 11-2, 11-3
Your verify code has expired or needs changing (Error Message), 11-7
[^1]: http://java.sun.com/j2ee/1.4/docs/tutorial/doc/Security5.html
[^2]: http://java.sun.com/j2ee/1.4/docs/tutorial/doc/Security5.html
[^3]:
[^4]: Hall, Marty, *More Servlets and Java Server Pages*, 2002, pg. 523.
[^5]: See <https://vaww.ocis.va.gov/portal/server.pt>?.
[^6]: Definition of JavaBean from the following Glossary WebWeb site: <u>http://www.orafaq.com/glossary/faqglosj.htm,</u> 7/17/04, Revision 2.1; Author: Frank Naudé.
[^7]: "The Apache Jakarta Project;" Overview of Cactus WebWeb site: <http://jakarta.apache.org/cactus/>, last updated 2/15/05.
[^8]: Excerpt taken from the WebLogic Server™ Programming WebLogic Security Guide, Page 2-12; downloaded from the BEA Website: [www.bea.com](http://www.bea.com).Web site
