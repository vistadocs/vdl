---
title: Electronic Signature (ESig) Version 1 Systems Management Guide
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: Systems Management Guide
app_code: XOBE
app_name: Electronic Signature (ESig)
section: GUI
app_status: active
pkg_ns: XOBE
patch_ver: 1
patch_id: XOBE*1
group_key: "XOBE:XOBE:1"
file_numbers: 
  - 200
security_keys: []
menu_options: 1
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - class
  - esig
  - contents
  - vista
  - signature
  - strong
  - electronic
  - even
  - java
page_count: 0
word_count: 4980
section_count: 24
table_count: 14
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Electronic_Signature/xobe_1_0sm.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Electronic_Signature/xobe_1_0sm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=171"
---

![](electronic-signature-esig-version-1-systems-management-guide/001.png)

Electronic Signature (ESig)

System Management Guide

November 2006

U.S. Department of Veterans Affairs

Health Systems Design & Development

Revision History

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 14%" />
<col style="width: 44%" />
<col style="width: 22%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Contacts</strong></td>
</tr>
<tr class="even">
<td>November 2006</td>
<td>1.0</td>
<td>Release</td>
<td rowspan="6"><p><strong>Project Manager and Analyst:</strong></p>
<p>REDACTED</p>
<p><strong>Developer:</strong></p>
<p>REDACTED</p>
<p><strong>Technical Writer:</strong></p>
<p>REDACTED</p></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Table of Contents

List of Figures

[Figure 1-1. ESig Architecture [2](#_Toc125274400)](#_Toc125274400)

List of Tables

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [ESig Overview](#esig-overview)
    - [VistALink 1.5 Dependency](#vistalink-15-dependency)
    - [Installation](#installation)
  - [Using this Guide](#using-this-guide)
    - [Purpose](#purpose)
    - [Audience](#audience)
    - [Text Conventions](#text-conventions)
  - [Additional Resources](#additional-resources)
    - [ESig Reference Materials](#esig-reference-materials)
    - [Online Technical Information](#online-technical-information)
- [VistA/M Information](#vistam-information)
  - [ESig 1.0 Installation](#esig-10-installation)
  - [Site Parameters](#site-parameters)
  - [Performance and Scalability](#performance-and-scalability)
  - [Exported Files](#exported-files)
  - [Global Translation, Journaling, and Protection](#global-translation-journaling-and-protection)
  - [VistA/M Server Routines](#vistam-server-routines)
    - [Routine Definitions](#routine-definitions)
    - [Routine Mapping](#routine-mapping)
    - [Menu Option](#menu-option)
  - [Exported Remote Procedures](#exported-remote-procedures)
  - [Callable Routines, Entry Points, and APIs](#callable-routines-entry-points-and-apis)
  - [External Relations](#external-relations)
    - [Software Requirements](#software-requirements)
    - [DBA Approvals and Integration Agreements (IAs)](#dba-approvals-and-integration-agreements-ias)
  - [Internal Relations](#internal-relations)
    - [Internal Relations](#internal-relations-1)
    - [Namespace](#namespace)
  - [Package-Wide Variables](#package-wide-variables)
- [ESig Security Features](#esig-security-features)
  - [VHA Directives, Policies, and Legal Requirements](#vha-directives-policies-and-legal-requirements)
  - [Mail Groups and Alerts](#mail-groups-and-alerts)
  - [Archiving and Purging](#archiving-and-purging)
  - [Contingency Planning](#contingency-planning)
  - [Interfacing](#interfacing)
  - [Menus](#menus)
  - [Security Keys](#security-keys)
  - [Files](#files)
  - [RPC Security](#rpc-security)
- [Glossary](#glossary)

## ESig Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As Health*<u>e</u>*Vet-VistA developers migrate VistA applications to modern technologies, interim solutions may be required until enterprise solutions are mature and stable. The Electronic Signature (ESig) service provides an interim solution for the use of electronic codes in place of wet signatures while Health*<u>e</u>*Vet-VistA’s security infrastructure and architecture are being defined. The service duplicates for Java applications (J2EE or J2SE) the Kernel 8.0 electronic signature functionality currently used by VistA/M applications.

ESig furnishes a standard, consistent set of APIs that Health*<u>e</u>*Vet -VistA developers can implement to provide users access to electronic signature data stored on VistA/M systems. ESig APIs make calls from Java applications to VistA/M systems to retrieve, validate, and store electronic signature codes and signature block information (name, title, office phone, etc.). Additional Java APIs provide encoding/decoding, hash, and checksum calculation utilities, but do not interact with the VistA/M system.

Applications that implement the ESig service must provide a user interface (UI) to prompt users for their secret codes when authorizing orders, prescriptions, financial transactions, or other business processes. Users may also need the UI to create or modify their code or signature block data.

### VistALink 1.5 Dependency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig requires the VistALink 1.5 service, which provides the transport layer enabling communication between a Java application and a VistA/M system.

The figure below shows ESig APIs communicating with VistA through VistALink 1.5. When a Health*<u>e</u>*Vet user signs on successfully, the connection from the application to VistA via VistALink is established. Consuming applications pass the VistaLinkConnection object to the ESig APIs that communicate with the VistA server.

![](electronic-signature-esig-version-1-systems-management-guide/002.png)

<span id="_Toc125274400" class="anchor"></span>Figure 1-1. ESig Architecture

### Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health*<u>e</u>*Vet ESig consists of three parts:

- An M package containing a routine, a Broker option, and a set of Remote Procedures for accessing electronic signature codes and related data in the Kernel’s NEW PERSON file
- A JAR file containing a set of Java APIs for passing and receiving electronic signature related information from M and for performing hashing, encryption, and decryption of strings. For ESig functionality to work, the ESig JAR file must be present on an application’s classpath.
- Sample Java Swing, client console, and JSP utility applications to test or verify installation and configuration of the ESig components. These are included in the ESig distribution.

Although ESig is a Health*<u>e</u>*Vet-VistA application, the only installation required is the KIDS build on the VistA/M server. Health*<u>e</u>*Vet-VistA applications requiring electronic signature functionality will include the ESig JAR file in their classpath. The JAR file contains APIs to perform ESig functions, including calling the VistA/M database.

Application developers and testers may want to deploy the sample ESig applications to client workstations (J2SE) or application servers (J2EE) to test the installation of the M server pieces. Instructions for deploying the sample applications are included in the *ESig 1.0 Developer Guide*.

## Using this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides technical reference data for the Health*<u>e</u>*Vet -VistA ESig 1.0 package, primarily on the M side. The *ESig 1.0 Installation Guide* presents instructions for the two administrative tasks required by ESig 1.0:

- Installing the ESig KIDS build on a VistA/M server
- Deploying the ESig sample applications on a BEA WebLogic application server and client workstation.

  Managing electronic signature code data is a Kernel function; for pertinent information see Chapter 4 (“Electronic Signature Codes”) of the *Kernel v8.0 Systems Manual*.

### Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is for the use of Health*<u>e</u>*Vet-VistA application developers, testing and quality-assurance personnel, Enterprise VistA Support (EVS) personnel, IRM staff, and data center M administrators. It focuses on the M environment and assumes that readers are familiar with the following:

- VistA/M computing environment
- VA FileMan data structures and terminology
- M programming language
- Microsoft Windows

### Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below summarizes specialized use of typographical styles in this document.

<span id="_Toc150655855" class="anchor"></span>Table 1-2. Text Conventions

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 42%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Convention</strong></th>
<th><strong>Explanation</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ALL CAPS</td>
<td>M file, routine, variable, field, menu, field, and security key names.</td>
<td><p>Developers should be assigned the XUPROGMODE security key.</p>
<p>The option [XOBE ESIG USER] may be added to the menu.</p></td>
</tr>
<tr class="even">
<td rowspan="3"><strong>Boldface</strong></td>
<td>Java file and directory names, particularly the first time they are mentioned in a passage.</td>
<td>Locate the <strong>javadoc</strong> folder and open your browser to the <strong>index.html</strong> file.</td>
</tr>
<tr class="odd">
<td>Java GUI buttons.</td>
<td>Press <strong>Enter</strong>.</td>
</tr>
<tr class="even">
<td>Used in M dialog examples to show user entries.</td>
<td>Enter a Host File: <strong>XOBE_1_.KID</strong></td>
</tr>
<tr class="odd">
<td>Courier font</td>
<td>Java class, method, or variable names</td>
<td>ESigConnectionException</td>
</tr>
<tr class="even">
<td rowspan="2">&lt;Angle brackets&gt;</td>
<td>M key entries.</td>
<td>&lt;Enter&gt;</td>
</tr>
<tr class="odd">
<td>In Java-related text, indicates information that is unknown or must be supplied by the user.</td>
<td>Locate the <strong>jaas.config</strong> file in the <strong>&lt;ESIG_SAMPLE_APP&gt;</strong> folder.</td>
</tr>
<tr class="even">
<td>“Quotation marks”</td>
<td>Verbatim user entries in Java-related instructions.</td>
<td>You should name the file “log4j.xml”.</td>
</tr>
</tbody>
</table>

The following symbols appear throughout the documentation to alert the reader to special information or conditions.

|                                                   |                                                                           |
|---------------------------------------------------|---------------------------------------------------------------------------|
| Symbol                                        | Description                                                           |
| ![](electronic-signature-esig-version-1-systems-management-guide/003.png) | Used to inform the reader of general information and reference material.  |
| ![](electronic-signature-esig-version-1-systems-management-guide/004.png) | Used to caution the reader to take special notice of critical information |

## Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ESig Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents are included in the ESig documentation set:

- *ESig 1.0 Installation Guide* – Prerequisites and instructions for installing the ESig KIDS build on a VistA/M server.
- *ESig 1.0 Developer Guide* – Detailed information about ESig APIs and exceptions, for developers intending to use ESig APIs in their applications. Includes instructions useful to developers, quality assurance, and testers, for deploying sample J2EE (application server) and J2SE (client server) applications. These sample applications test the ESig APIs used by the host application.
- *ESig 1.0 System Management Guide* – M-side system and security information.

Because ESig APIs communicate with VistA/M systems through VistALink and Kernel RPCs, the following documentation is highly recommended:

- VistALink 1.5 documentation: *Developer Guide*, *Installation Guide*, and *System Management Guide*.
- RPC documentation: *RPC Broker Getting Started with the Broker Development Kit (BDK, ) RPC Broker Developer's Guide* (i.e., BROKER.HLP, online help designed for programmers, distributed in the BDK)
- *Kernel v.8.0 Systems Manual*

ESig, VistALink, and RPC Broker documents are available on any of the Office of Information FTP directories as well as the VHA Document Library (VDL) at <http://www.va.gov/vdl/>.

### Online Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VistA/M Help

After the ESig KIDS build is installed on the VistA/M server, developers and system administrators can use the standard Kernel/FileMan utilities for printouts of the installed components.

VistA software has online help and commonly used system default prompts. In roll-and-scroll mode users are strongly encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA roll-and-scroll software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed.

> A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.

- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

#### VistA/M Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. To print formatted data dictionaries, refer to the VA FileMan v.22.0 Advanced User Manual at <http://www.va.gov/vdl>.

#### Javadocs

Java class and package documentation is included in the ESig distribution zip file. Locate the javadoc folder and open your browser to the index.html file.

|                                                   |                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-systems-management-guide/005.png) | To learn more about Javadoc files, refer to Sun’s Javadoc Tool Home Page at: <http://java.sun.com/j2se/javadoc/>. |

|                                                   |                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-systems-management-guide/006.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs of the information, products, or services on the Website. The VHA does not exercise any editorial control over the information you may find at these locations. |

# VistA/M Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ESig 1.0 Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *ESig 1.0 Installation Guide* provides detailed installation information. It also contains requirements and recommendations to configure ESig 1.0. This document (XOBE_1_OIG.PDF) is available on the Office of Information ANONYMOUS.SOFTWARE directories and the VHA Document Library (<http://www.va.gov/vdl>).

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no ESig 1.0 site parameters.

## Performance and Scalability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Current performance statistics are limited. However, preliminary testing results indicate that the processing time and resources consumed by ESig itself are minimal. ESig uses VistALink to communicate with the VistA/M server, and VistALink does not introduce any additional overhead to messages sent between the client and the VistA/M server.

## Exported Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No new files are exported to the VistA/M server for ESig 1.0 software. Applications using the ESig APIs will be responsible for deploying the libraries required for ESig to their BEA WebLogic application server(s).

## Global Translation, Journaling, and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig 1.0 software introduces no new globals on the VistA/M server. Translation, journaling, and protection are not applicable.

## VistA/M Server Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routine Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig distributes just one M routine:

> XOBESIG – This routine contains the code for the Remote Procedure Calls (RPCs) to retrieve and save electronic signature codes and related data on the VistA/M server.

### Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine mapping is at the discretion of the systems manager. ESig has no requirements for routine mapping.

### Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Name \[XOBE ESIG USER\]

> Menu Text Context for Electronic Signature Users

> Type Broker (Client / Server)

> Description This option is the user context that contains the RPCs used by ESig. Users of a HealtheVet application that calls ESig RPCs must have this option assigned to their VistA menu tree.

|                                                   |                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-systems-management-guide/007.png) | To bypass security for development purposes, developers should be assigned the XUPROGMODE security key*.* Holders of XUPROGMODE can run any VistA client / server application (regardless of menu trees) and access any RPC without regard to application context. |

|                                                   |                                                                                                                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-systems-management-guide/008.png) | To simplify maintenance, the option \[XOBE ESIG USER\] may be added to the Common \[XUCOMMAND\] menu on the VistA/M server to automatically give all users on that server access to the electronic signature remote procedures. |

## Exported Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig 1.0 distributes the remote procedures detailed in the table below.

<span id="_Toc58310991" class="anchor"></span>Table 2-1. ESig 1.0 Distributed Remote Procedures

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 30%" />
<col style="width: 26%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Remote Procedure</strong></td>
<td><strong>Description</strong></td>
<td><strong>Routine</strong></td>
<td><strong>Return Value Type</strong></td>
</tr>
<tr class="even">
<td><h6 id="xobe-esig-get-code" class="unnumbered">XOBE ESIG GET CODE</h6></td>
<td>Returns the electronic signature code for the user from the NEW PERSON file.</td>
<td>GETCODE^XOBESIG</td>
<td>Single Value</td>
</tr>
<tr class="odd">
<td><strong>XOBE ESIG GET DATA</strong></td>
<td>Returns the data for the electronic signature block-related fields from the NEW PERSON file.</td>
<td>GETDATA^XOBESIG</td>
<td>Array</td>
</tr>
<tr class="even">
<td><h6 id="xobe-esig-is-defined" class="unnumbered">XOBE ESIG IS DEFINED</h6></td>
<td>Returns whether the user currently has an electronic signature code defined. This RPC returns “0” if the electronic signature code is null; it returns “1” if the user’s electronic signature code is defined.</td>
<td>ISDEF^XOBESIG</td>
<td>Single Value</td>
</tr>
<tr class="odd">
<td><h6 id="xobe-esig-set-code" class="unnumbered">XOBE ESIG SET CODE</h6></td>
<td><h6 id="saves-the-users-electronic-signature-code-in-the-new-person-file." class="unnumbered">Saves the user's electronic signature code in the NEW PERSON file.</h6></td>
<td><h6 id="setcodexobesig" class="unnumbered">SETCODE^XOBESIG</h6></td>
<td><h6 id="single-value" class="unnumbered">Single Value</h6></td>
</tr>
<tr class="even">
<td><h6 id="xobe-esig-set-data" class="unnumbered">XOBE ESIG SET DATA</h6></td>
<td><h6 id="saves-the-electronic-signature-block-related-data-in-the-new-person-file." class="unnumbered">Saves the electronic signature block-related data in the NEW PERSON file.</h6></td>
<td><h6 id="setdataxobesig" class="unnumbered">SETDATA^XOBESIG</h6></td>
<td><h6 id="array" class="unnumbered">Array</h6></td>
</tr>
</tbody>
</table>

## Callable Routines, Entry Points, and APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig 1.0 does not provide any callable M routines. However, it does provide Java programming interfaces.

|                                                   |                                                                                                                                     |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-systems-management-guide/009.png) | For information on the ESig Java programming interfaces, see the “ESig APIs” chapter of the *Electronic Signature Developer Guide*. |

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig 1.0 relies on the VistA software listed in the table below.

<span id="_Toc58310992" class="anchor"></span>Table 2-2. Required VistA Software

|                |             |                       |
|----------------|-------------|-----------------------|
| Software   | Version | Patch Information |
| Kernel         | 8.0         | Fully patched         |
| Kernel Toolkit | 7.3         | Fully patched         |
| RPC Broker     | 1.1         | Fully patched         |
| VA FileMan     | 22.0        | Fully patched         |
| VistALink      | 1.5         | Fully patched         |

### DBA Approvals and Integration Agreements (IAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Database Administrator (DBA) maintains a list of Integration Agreements (IAs). IAs are mutual agreements between software developers that allow the use of internal entry points or other software-specific features that are not available to the general programming public.

#### Obtaining Integration Agreement Information

To obtain a current list of any IAs to which the ESig 1.0 software (XOBE) is a custodian:

1.  Sign on to the FORUM system REDACTED
2.  Go to the DBA menu \[DBA\].
3.  Select the Integration Agreements Menu option \[DBA IA ISC\].
4.  Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].
5.  Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].
6.  When this option prompts you for a package, enter ELECTRONIC SIGNATURE or XOBE.
7.  All current IAs to which the ESig software is a custodian will be listed.

To obtain detailed information on a specific integration agreement:

1.  Sign on to the FORUM system REDACTED
2.  Go to the DBA menu \[DBA\].
3.  Select the Integration Agreements Menu option \[DBA IA ISC\]
4.  Select the Inquire option \[DBA IA INQUIRY\].
5.  When prompted for "INTEGRATION REFERENCES," enter the specific integration agreement number of the IA you would like to display.
6.  The option will display the full text of the IA you requested.

To obtain the current list of IAs, if any, to which the ESig software is a subscriber:

1.  Sign on to the FORUM system REDACTED
2.  Go to the DBA menu \[DBA\].
3.  Select the Integration Agreements Menu option \[DBA IA ISC\].
4.  Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\]
5.  Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\]
6.  When prompted with "START WITH SUBSCRIBING PACKAGE," enter ELECTRONIC SIGNATURE (in uppercase). When prompted with "GO TO SUBSCRIBING PACKAGE," enter ELECTRONIC SIGNATURE (in uppercase).
7.  All current IAs to which the ESig software is a subscriber will be listed

#### ESig-Kernel Integration Agreement

The following is the integration agreement ESig has with Kernel to access fields in the New Person file:

4297 NAME: ELECTRONIC SIGNATURE-RELATED DATA IN THE NEW PERSON FILE

CUSTODIAL PACKAGE: KERNEL REDACTED

SUBSCRIBING PACKAGE: ELECTRONIC SIGNATURE REDACTED

USAGE: Private ENTERED: DEC 23,2003

STATUS: Active EXPIRES:

DURATION: Till Otherwise Agr VERSION:

FILE: 200 ROOT: VA(200,

DESCRIPTION: TYPE: File

Electronic Signature is a collection of Java APIs to validate, retrieve,

and save electronic signature codes and related data on the M server, as

well as APIs to encrypt and decrypt strings similar to the APIs provided

by the existing VA Kernel 8.0 electronic signature APIs.

The Java APIs provide HSD&D developers that are rehosting their

applications to a new Java environment a standardized method for migrating

their electronic signature functionality. It is hoped that this will

reduce duplication of effort, promote more efficient use of limited

development resources, and satisfy the VistA user's business needs.

This IA permits Electronic Signature to access electronic

signature-related data in the NEW PERSON file (#200) as listed in the

GLOBAL REFERENCE section of this Integration Agreement. All fields are

accessed via VA FileMan calls, such as \$\$GET1^DIQ and FILE^DIE, rather

than direct global reads.

^VA(200,

.132 OFFICE PHONE .13;2 Both R/W w/Fileman

.137 VOICE PAGER .13;7 Both R/W w/Fileman

.138 DIGITAL PAGER .13;8 Both R/W w/Fileman

1 INITIAL 0;2 Both R/W w/Fileman

20.2 SIGNATURE BLOCK PRIN 20;2 Both R/W w/Fileman

20.3 SIGNATURE BLOCK TITL 20;3 Both R/W w/Fileman

20.4 ELECTRONIC SIGNATURE 20;4 Both R/W w/Fileman

ROUTINE:

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No routines, files or options within the ESig product assume that the entry / exit logic of another option has already occurred.

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig has been assigned the XOBE namespace. The XOBE namespace is a member of the Foundations (XOB\*) product family.

## Package-Wide Variables 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig does not create any package-wide variables that have received Standards and Convention Committee (SACC) exemptions.

# ESig Security Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Electronic Signature security features are based on the following requirements:

- HeV applications authenticate their users.

> HeV applications are required to authorize and authenticate their users. Infrastructure tools such as KAAJEE (Kernel Authentication and Authorization for J2EE) and FatKAAT (rich-client Kernel Authentication and Authorization) are mandated for use in Health*<u>e</u>*Vet -VistA Web-based and rich-client applications, respectively.

- Users must have valid Access and Verify codes.
- Health*<u>e</u>*Vet -VistA applications must have a valid VistALink connection request.
- Any remote procedure call must be registered and valid for the application being executed.
- Users must have assigned to their VistA menu tree the Context for Electronic Signature Users \[XOBE ESIG USER\] “B”-type option.

## VHA Directives, Policies, and Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The pending *VHA Directive on Modifications to VistA and VistA Sensitive Software* prohibits modification of any part of the ESig software. There are no special legal requirements that pertain to the use of ESig. Distribution of ESig software is unrestricted.

## Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig does not make use of mail groups or alerts.

## Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig does not have any archiving or purging requirements or features.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is the responsibility of the using service to develop a local contingency plan for use in the event of application problems.

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please see the sections “[External Relations](#external-relations)” (VistA/M-server side) and “Required Java Software” (Java client side) in the Electronic Signature Developer Guide for a list of external packages required by ESig.

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no options of special note for Information Security Officers (ISOs) to view.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig requires no specific security keys. However, to bypass security for development purposes, we recommend client/server application developers be assigned the XUPROGMODE security key. All users assigned the XUPROGMODE security key can do the following:

- Run any VistA client/server application regardless of whether or not it is in their menu tree
- Access any RPC without regard to the application context

## Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig exports no files.

## RPC Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information regarding security enforced on RPCs, please visit the Infrastructure section of the VHA Document Library to access the *RPC Broker Systems Manual*:

> <http://www.va.gov/vdl/>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Access Code</td>
<td>A code, that along with the Verify code allows the Kernel to identify a user as authorized to gain access to a VistA system.</td>
</tr>
<tr class="even">
<td>API</td>
<td>Application Programming Interface. The set of public classes a package uses. Intended to prevent duplication of utilities and limit the number of callable entry points.</td>
</tr>
<tr class="odd">
<td>ASCII</td>
<td>American Standard Code for Information Interchange</td>
</tr>
<tr class="even">
<td>Authentication</td>
<td>Verification of a user’s identity.</td>
</tr>
<tr class="odd">
<td>Authorization</td>
<td>Checking the permissions of a user to allow or disallow the performance of some function.</td>
</tr>
<tr class="even">
<td>CCE</td>
<td>Computer Code Entry. A password/PIN technology for asserting electronic signature intent in a health-care environment. Computer Code Entry (CCE) is explicitly endorsed in existing medical records practice/regulation and is permitted by JCAHO IM7 standards.</td>
</tr>
<tr class="odd">
<td>Client</td>
<td>A single term used interchangeably to refer to a user, the workstation (e.g., PC), and the portion of the software that runs on the workstation.</td>
</tr>
<tr class="even">
<td>Data Dictionary</td>
<td>The structure of a file, table, or group of related information as defined for and by VA FileMan</td>
</tr>
<tr class="odd">
<td>Database Integration Agreement (DBIA)</td>
<td>A formal, documented understanding between two or more application packages that describes how data is shared or information is exchanged. The Database Administrator (DBA) maintains these agreements. Documented agreements are available via the DBIA menu on FORUM</td>
</tr>
<tr class="even">
<td>DBA</td>
<td>Data Base Administrator</td>
</tr>
<tr class="odd">
<td>Decrypt</td>
<td>To decipher, decode, or unlock encrypted or encoded messages/data to make them readable.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td><p>DUZ represents the internal entry number (IEN) for a user’s record in File #200, the New Person file and is designated as a system-wide variable in the VistA environment.</p>
<p>DUZ is used as a re-authentication mechanism.</p></td>
</tr>
<tr class="odd">
<td>EAR</td>
<td>Enterprise ARchive file.</td>
</tr>
<tr class="even">
<td>EJB</td>
<td>Enterprise Java Bean.</td>
</tr>
<tr class="odd">
<td>Electronic Signature</td>
<td>A secret, user-supplied PIN or code that is used to authorize business processes and is a legally binding equivalent of an individual’s handwritten signature. For the VA Kernel 8.0 an electronic signature must be 6-20 characters in length and can contain letters, numbers, and punctuation.</td>
</tr>
<tr class="even">
<td>Encrypt</td>
<td>To encode messages or data so that they are unreadable unless they are decoded.</td>
</tr>
<tr class="odd">
<td>ESig</td>
<td>Electronic Signature.</td>
</tr>
<tr class="even">
<td>EVS</td>
<td>Enterprise VistA Support</td>
</tr>
<tr class="odd">
<td>FOIA</td>
<td>Freedom of Information Act</td>
</tr>
<tr class="even">
<td>FTP</td>
<td>File Transfer Protocol</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphical User Interface. The graphical elements on the screen through which the user interacts with the computer.</td>
</tr>
<tr class="even">
<td>Hash</td>
<td>To encrypt data by substituting a shorter fixed-length value or key to represent the original. Hashing algorithms are one-way functions, so that it is not possible to decrypt the substitute values to generate the original data.</td>
</tr>
<tr class="odd">
<td>IP</td>
<td>Internet Protocol</td>
</tr>
<tr class="even">
<td>IRM</td>
<td>Information Resources Management. A service at each VAMC responsible for computer management and system security.</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td>Information Security Officer</td>
</tr>
<tr class="even">
<td>J2EE</td>
<td>Java <sup>TM</sup> 2 Platform, Enterprise Edition</td>
</tr>
<tr class="odd">
<td>J2SE</td>
<td>Java 2 Standard Edition</td>
</tr>
<tr class="even">
<td>JAAS</td>
<td>Java Authentication and Authorization Service</td>
</tr>
<tr class="odd">
<td>Javadoc</td>
<td>Javadoc is the tool from Sun Microsystems for generating API documentation in HTML format from doc comments in Java source code.</td>
</tr>
<tr class="even">
<td>JNDI</td>
<td>Java Naming Directory Interface</td>
</tr>
<tr class="odd">
<td>JSP</td>
<td>Java Server Page</td>
</tr>
<tr class="even">
<td>JVM</td>
<td>Java Virtual Machine</td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>VA Kernel 8.0 is a suite of VistA software that provides a standard and consistent user and programmer interface between application packages, the OS, and users.</td>
</tr>
<tr class="even">
<td>M</td>
<td>MUMPS</td>
</tr>
<tr class="odd">
<td>Option</td>
<td>A selectable software function: a menu item.</td>
</tr>
<tr class="even">
<td>PIN</td>
<td>Personal Identification Number</td>
</tr>
<tr class="odd">
<td>PKI</td>
<td>Public Key Infrastructure</td>
</tr>
<tr class="even">
<td>RPC</td>
<td>Remote Procedure Call</td>
</tr>
<tr class="odd">
<td>SAC</td>
<td>Standards and Conventions</td>
</tr>
<tr class="even">
<td>SACC</td>
<td>Standards and Conventions Committee</td>
</tr>
<tr class="odd">
<td>SDK</td>
<td>Java Software Development Kit. APIs and tools for developing applications.</td>
</tr>
<tr class="even">
<td>Signature Block</td>
<td>Data associated with an electronic signature user, stored in the New Person file. Signature block data consists of the user’s initials, printed name, title, office phone, voice pager, and digital pager.</td>
</tr>
<tr class="odd">
<td>TBD</td>
<td>To Be Determined</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td>Transmission Control Protocol / Internet Protocol</td>
</tr>
<tr class="odd">
<td>URL</td>
<td>Uniform Resource Locator</td>
</tr>
<tr class="even">
<td>User</td>
<td>This term generally refers to VA employees and volunteers with active records established in File #200, the New Person file, who are authorized to access a VistA system.</td>
</tr>
<tr class="odd">
<td>VA</td>
<td>Veterans Affairs</td>
</tr>
<tr class="even">
<td>VA ITSCAP</td>
<td>VA Information Technology Security Certification and Accreditation Program (VA Directive 6214)</td>
</tr>
<tr class="odd">
<td>VAMC</td>
<td>Department of Veterans Affairs Medical Center</td>
</tr>
<tr class="even">
<td>VAX</td>
<td>VAX (Virtual Address extension) is an established line of mid-range server computers from the Digital Equipment Corporation (DEC).</td>
</tr>
<tr class="odd">
<td>VHA</td>
<td>Veterans Health Administration</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture</td>
</tr>
<tr class="odd">
<td>VistA/M Server</td>
<td>The computer where the M data and the RPC Broker remote procedure calls (RPCs) reside.</td>
</tr>
<tr class="even">
<td>VistALink</td>
<td>A standardized, portable, and secure mechanism for establishing connections between Java (J2SE and J2EE) and VistA/M servers.</td>
</tr>
<tr class="odd">
<td>VMS</td>
<td>Virtual Machine System (operating system for VAX computers)</td>
</tr>
<tr class="even">
<td>WAN</td>
<td>Wide Area Network</td>
</tr>
<tr class="odd">
<td>WAR</td>
<td>Web ARchive</td>
</tr>
<tr class="even">
<td>WLS</td>
<td>WebLogic Server</td>
</tr>
<tr class="odd">
<td>XML</td>
<td>Extensible Markup Language</td>
</tr>
</tbody>
</table>
