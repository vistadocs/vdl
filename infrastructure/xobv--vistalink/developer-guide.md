---
title: VistALink Version 1.6 Developer Guide
doc_type: DG
doc_label: Developer Guide
doc_layer: anchor
doc_subject: null
app_code: XOBV
app_name: VistALink
section: INF
app_status: active
pkg_ns: XOBV
patch_ver: 1.6
patch_id: XOBV*1.6
group_key: XOBV:XOBV:1.6
file_numbers:
- '18'
- '200'
- '200.02'
- '217'
- '8989.3'
- '8994'
security_keys: []
menu_options: 2
description: Product Development Services Security Program VistALink development team. Albany, NY
audience: ''
keywords: []
page_count: 0
word_count: 20542
section_count: 39
table_count: 51
figure_count: 0
appendix_count: 1
has_toc: false
is_stub: false
pub_date: July 2020
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_dg.docx
pdf_url: https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_dg.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=163
audit_applied: '2026-05-31'
master_source: VistALink Version 1.6 Developer Guide
master_pub_date: July 2020
consolidated_from: 3 versions
prior_versions:
- VistALink Version 1.5 Developer Guide
- VistaLink Version 1.6.7 Developer Guide
consolidated_title: vistalink developer guide
---

![](vistalink-version-1-6-developer-guide/001.png)

VISTALINKDEVELOPER GUIDE

July 2020

Office of Information and Technology

Product Development

## ## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 46%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>07/2020</td>
<td>XOBV*1.6*5 – VistALink Version 1.6.1</td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/24/19</td>
<td>XOBVS*1.6*4 N/A changes</td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/2010</td>
<td>VistALink Version 1.6 release.</td>
<td><blockquote>
<p>Product Development Services Security Program VistALink development team.</p>
<p>Albany, NY OIFO:</p>
</blockquote>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul>
<blockquote>
<p>Bay Pines, FL OIFO:</p>
</blockquote>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul>
<blockquote>
<p>Oakland, CA OIFO:</p>
</blockquote>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>05/2006</td>
<td>Initial VistALink Version 1.5 release.</td>
<td><p>REDACTED, technical writer</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc280220364" class="anchor"></span>Table i. Revision History

Contents

## Tables and Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*This page is left blank intentionally.*

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Developer Guide is intended for use in conjunction with the VistALink software. It outlines the details of VistALink-related software and gives guidelines on how the software is used within Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA).

The intended audience of this manual is all key stakeholders. The primary stakeholder is the Product Development Security Program team. Additional stakeholders include:

- Health*<u>e</u>*Vet-VistA application developers of Web-based applications in the WebLogic 10.3.6 and 12.1.2 Application Server environments.
- Information Resource Management (IRM) and Information Security Officers (ISOs) at Veterans Affairs Medical Centers (VAMCs) responsible for computer management and system security.
- Product Support.
- VA facility personnel who will be using Health*<u>e</u>*Vet-VistA Web-based applications running in the WebLogic 10.3.6 and 12.1.2 Application Server environment.

Document Overview

This manual's intended audience includes server administrators and IRM Information Technology (IT) specialists at Veteran's Affairs (VA) facilities, as well as developers of Java applications requiring communication with VistA/Mumps (M).

Generally, the installation and maintenance instructions presented here assume the use of Windows as the client operating system. Where appropriate, separate steps are displayed for Linux.

### Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term *resource adapter* is often shortened in this guide to "adapter*,*" and is also used interchangeably with the term *connector*.

### Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File names and directory names are set off from other text using bold font (e.g., config.xml). Bold is also used to indicate Graphical User Interface (GUI) elements, such as tab, field, and button names (e.g., "press Delete").

All caps are used to indicate M routine and option names (e.g., XMINET). All caps used inside angle brackets indicate file names to be supplied by the user. Example:

> \<JAVA_HOME\>\bin\java -Dlog4j.configurationFile=file:///c:/localConfigs/mylog4j2.xml

Names for Java objects, methods, and variables are indicated by Courier font. Snapshots of computer displays also appear in Courier, surrounded by a border:

Select Installation Option: LOAD a Distribution

Enter a Host File: XOB_1_5.KID

In these examples, the response that the user enters at a prompt appears in bold font:

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\> TELNET PORT

Boldface text is also used in code and deployment descriptor samples to indicate lines of interest, discussed in the preceding text:

\<?xml version="1.0"?\>

\<weblogic-connector xmlns="http://www.bea.com/ns/weblogic/90" xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance xsi:schemaLocation="http://www.bea.com/ns/weblogic/90 http://www.bea.com/ns/weblogic/90/weblogic-ra.xsd"\>

\

- *VistALink 1.6 Developer Guide* (this manual): Contains detailed information about workstation setup, re-authentication, institution mapping, executing requests, VistALink exceptions, Foundations Library utilities, and other topics pertaining to writing code that uses VistALink.
- *VistALink 1.6 Release Notes*: Lists all new features included in each VistALink 1.6 release.

VistALink 1.6 end-user documentation can be downloaded from the VA Software Document Library (VDL) Web site at:

> <u><http://www.va.gov/vdl/application.asp?appid=163></u>

VistALink 1.6 end-user documentation and software can be downloaded from any of the anonymous.software directory on the Office of Information Field Office (OIFO) File Transfer Protocol (FTP) download sites::

- Albany OIFO [REDACTED](ftp://ftp.fo-albany.med.va.gov)
- Hines OIFO [REDACTED](ftp://ftp.fo-hines.med.va.gov)
- Salt Lake City OIFO [REDACTED](ftp://ftp.fo-slc.med.va.gov)
- Preferred Method REDACTED

The documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

SSO/UC Project (CCOW-Enabled Logins)

VistALink implements CCOW-enabled functionality for client/server end-user logins. For more information on how to use VistALink for CCOW-enabled client/server logins, see the Single Sign-On/User Context (SSO/UC) documentation, on the Veterans Document Library (VDL):

> [<u>http://www.va.gov/vdl/application.asp?appid=162</u>](http://www.va.gov/vdl/application.asp?appid=162)

Oracle (formerly known as BEA) Systems

At the current time, VistALink 1.6 has been tested and is supported on Oracle WebLogic Server 10.3.6 and 12.1.2. WebLogic product documentation can be found at the following website:

> [<u>http://edocs.bea.com/</u>](http://edocs.bea.com/)

|                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/004.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [## Revision History](#revision-history)
  - [Tables and Figures](#tables-and-figures)
  - [Orientation](#orientation)
    - [Terminology](#terminology)
    - [Text Conventions](#text-conventions)
- [Introduction](#introduction)
  - [About this Guide](#about-this-guide)
  - [WebLogic Updates Project](#weblogic-updates-project)
  - [About J2EE Connectors](#about-j2ee-connectors)
  - [Public VistALink APIs Documentation](#public-vistalink-apis-documentation)
  - [Sample Applications for J2EE Server](#sample-applications-for-j2ee-server)
  - [Deprecated VistALink APIs](#deprecated-vistalink-apis)
- [Developer Workstation Setup](#developer-workstation-setup)
  - [J2EE Development](#j2ee-development)
    - [IDE](#ide)
    - [J2EE Runtime](#j2ee-runtime)
  - [J2SE Development](#j2se-development)
    - [IDE](#ide-1)
    - [J2SE Runtime](#j2se-runtime)
- [How to Use VistALink in J2EE Applications](#how-to-use-vistalink-in-j2ee-applications)
  - [Using Station Number and Division](#using-station-number-and-division)
    - [System Locator: Institution-Connector Mapping](#system-locator-institution-connector-mapping)
    - [Multidivision-Aware Application Code: ConnectionSpec Credentials](#multidivision-aware-application-code-connectionspec-credentials)
    - [Example](#example)
  - [Request Cycle](#request-cycle)
    - [Retrieving the Connection Factory](#retrieving-the-connection-factory)
    - [Instantiating a Connection Spec for Re-authentication](#instantiating-a-connection-spec-for-re-authentication)
    - [Getting a Connection (Connection Spec)](#getting-a-connection-connection-spec)
    - [Executing a Request](#executing-a-request)
    - [Closing the Connection](#closing-the-connection)
    - [Complete Request Cycle](#complete-request-cycle)
    - [Connectivity Failures and Retry Strategies](#connectivity-failures-and-retry-strategies)
  - [More about Re-authentication](#more-about-re-authentication)
    - [Overview](#overview)
    - [Connection Specification Classes](#connection-specification-classes)
    - [Institution/Division Rules for Re-authentication](#institutiondivision-rules-for-re-authentication)
    - [Application Proxy User](#application-proxy-user)
  - [Timeouts](#timeouts)
    - [Socket-Level Forced Timeout](#socket-level-forced-timeout)
    - [Graceful (Request-Level) Timeout](#graceful-request-level-timeout)
  - [Institution Mapping](#institution-mapping)
    - [How to Configure Mappings](#how-to-configure-mappings)
    - [How to View the Currently Loaded Mappings](#how-to-view-the-currently-loaded-mappings)
    - [Retrieving Mappings for Applications](#retrieving-mappings-for-applications)
    - [Subdivisions](#subdivisions)
  - [VistALink Java API Reference](#vistalink-java-api-reference)
- [Executing Requests](#executing-requests)
  - [Remote Procedure Calls](#remote-procedure-calls)
    - [RPC Security ("B"-Type Option)](#rpc-security-b-type-option)
    - [RPCs for Use by Application Proxy Users](#rpcs-for-use-by-application-proxy-users)
  - [Request Processing](#request-processing)
    - [Get an RpcRequest Object: RpcRequestFactory Class](#get-an-rpcrequest-object-rpcrequestfactory-class)
    - [Set RpcRequest Parameters: "Explicit" Style](#set-rpcrequest-parameters-explicit-style)
    - [Set RpcRequest Parameters: "setParams" Style](#set-rpcrequest-parameters-setparams-style)
    - [Specifying Indices for List-Type RPC Parameters](#specifying-indices-for-list-type-rpc-parameters)
    - [Other Useful RpcRequest Methods](#other-useful-rpcrequest-methods)
  - [Response Processing](#response-processing)
    - [RpcResponse Class](#rpcresponse-class)
    - [Request/Response Example](#requestresponse-example)
    - [Parsing RPC Results](#parsing-rpc-results)
    - [XML Responses](#xml-responses)
  - [How to Write RPCs](#how-to-write-rpcs)
    - [Write Stateless RPCs Whenever Possible](#write-stateless-rpcs-whenever-possible)
    - [When State is Needed](#when-state-is-needed)
    - [Pitfalls of Using of \$JOB in Stateful RPCs](#pitfalls-of-using-of-job-in-stateful-rpcs)
    - [Pitfalls of Global Locking in Stateful RPCs](#pitfalls-of-global-locking-in-stateful-rpcs)
- [VistALink Exception Reference](#vistalink-exception-reference)
  - [Exception Nesting Changes Since VistALink 1.5](#exception-nesting-changes-since-vistalink-15)
  - [VistALink Exception Hierarchy](#vistalink-exception-hierarchy)
    - [Common FoundationsExceptionInterface](#common-foundationsexceptioninterface)
    - [VistaLinkResourceException](#vistalinkresourceexception)
    - [FoundationsException](#foundationsexception)
    - [VistaLinkFaultException](#vistalinkfaultexception)
- [Foundations Library Utilities](#foundations-library-utilities)
  - [Encryption: gov.va.med.crypto](#encryption-govvamedcrypto)
  - [J2EE Environment: gov.va.med.environment](#j2ee-environment-govvamedenvironment)
    - [Environment.isProduction()](#environmentisproduction)
    - [Environment.getServerType()](#environmentgetservertype)
  - [Network: gov.va.med.net](#network-govvamednet)
  - [Audit Timer: gov.va.med.monitor.time](#audit-timer-govvamedmonitortime)
    - [Sample Code](#sample-code)
  - [Exception: gov.va.med.exception](#exception-govvamedexception)
    - [ExceptionUtils Class](#exceptionutils-class)
  - [XML: gov.va.med.xml](#xml-govvamedxml)
    - [XmlUtilities Class](#xmlutilities-class)
- [How to Use VistALink in J2SE Applications](#how-to-use-vistalink-in-j2se-applications)
  - [Authenticating and Connecting to VistA in Client-Server Mode](#authenticating-and-connecting-to-vista-in-client-server-mode)
    - [JAAS Overview](#jaas-overview)
  - [VistALink JAAS Implementation](#vistalink-jaas-implementation)
    - [VistaLoginModule](#vistaloginmodule)
    - [JAAS Login Configuration Overview](#jaas-login-configuration-overview)
    - [VistALink-Specific JAAS Login Configuration](#vistalink-specific-jaas-login-configuration)
    - [Passing the JAAS Login Configuration(s) to Your JVM](#passing-the-jaas-login-configurations-to-your-jvm)
    - [Selecting the JAAS Configuration From an Application](#selecting-the-jaas-configuration-from-an-application)
    - [Selecting a VistaLoginModule Callback Handler](#selecting-a-vistaloginmodule-callback-handler)
    - [Benefits of Passing Parent Application Frame to Callback Handler](#benefits-of-passing-parent-application-frame-to-callback-handler)
  - [Putting the Pieces Together: VistALink JAAS Login](#putting-the-pieces-together-vistalink-jaas-login)
    - [Logging in to VistA](#logging-in-to-vista)
  - [After Successfully Logging In](#after-successfully-logging-in)
    - [Retrieving the VistaKernelPrincipal](#retrieving-the-vistakernelprincipal)
    - [Retrieving the Authenticated Connection From the Principal](#retrieving-the-authenticated-connection-from-the-principal)
    - [Retrieving User Demographic Information](#retrieving-user-demographic-information)
    - [Executing RPCs](#executing-rpcs)
    - [Timeouts](#timeouts-1)
    - [Logging Out](#logging-out)
  - [Catching Login Exceptions](#catching-login-exceptions)
    - [VistaLoginModule Exception Hierarchy](#vistaloginmodule-exception-hierarchy)
  - [CCOW Login Functionality](#ccow-login-functionality)
  - [Unit Testing and VistALink](#unit-testing-and-vistalink)
  - [Appendix A: Pluggable Institution Rules](#appendix-a-pluggable-institution-rules)
  - [Glossary](#glossary)

## About this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is a guide to developing applications that utilize VistALink 1.6. The VistALink 1.6 resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet Java applications and VistA/Mumps (M) servers, in both client-server and n-tier environments. It allows Remote Procedure Calls (RPCs) to execute on the VistA/M system and return results to the Java enterprise system.

VistALink consists of Java-side adapter libraries and an M-side listener. The adapter libraries use the J2EE Connector Architecture (J2CA 1.5) specification to integrate Java applications with legacy systems. The M listener process receives and processes requests from client applications.

The term *resource adapter* is often shortened in this guide to *adapter,* and is also used interchangeably with the term *connector*.

## WebLogic Updates Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In support of the Department of Veterans Affairs Information Technology Application Modernization effort, the three applications VistALink, Fat-client Kernel Authentication and Authorization (v), and Kernel Authentication and Authorization for the Java 2 Enterprise Edition (KAAJEE) have been developed. Based on the direction of the Technical Review Model (TRM) and to support applications that upgrade to the new WebLogic Server versions 10.3.6 and 12.1.2, this project is required. The scope of the project is to upgrade these three applications to work with the WebLogic Server versions 10.3.6 and 12.1.2.

The previous VistALink version (1.5) that was released in June of 2006, provided project developers with J2EE and Java Platform, Standard Edition (J2SE) application connectivity to VistA/M servers. It was designed specifically for J2EE 1.3 application servers (e.g., WebLogic 8.1).

## About J2EE Connectors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6 implements a resource adapter that is fully compliant with the J2EE Connector Architecture Specification 1.5. VistALink is accessed programmatically through the interfaces specified in the J2EE Connector Architecture specification.

|                                                                                                                |                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/005.png) | REF: For more information about J2EE Connectors, see the book *J2EE Connector Architecture and Enterprise Application Integration*, by Sharma, Stearns, and Ng (Addison-Wesley Professional). Also see the JCA 1.5 Connector Specification and the J2EE 1.4 standard. |

## Public VistALink APIs Documentation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink 1.6 distribution zip file supplies full Javadoc Application Program Interface (API) reference documentation in the /javadoc folder. The VistALink Javadoc describes the various Java classes that make up the public VistALink programming API. These APIs may be used under the conditions listed in the Javadoc documentation. VistALink classes that are not documented in the VistALink Javadoc are not part of the supported VistALink API.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-developer-guide/006.png)</td>
<td><p><strong>REF:</strong> For more information about the Javadoc documentation format, please see</p>
<p><a href="http://java.sun.com/j2se/javadoc/"><u>http://java.sun.com/j2se/javadoc/</u></a>.</p></td>
</tr>
</tbody>
</table>

## Sample Applications for J2EE Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the J2EE Developer Samples for examples of how to use VistALink with a J2EE server. The Developer Samples are supplied in the VistALink 1.6 distribution zip file for both J2EE and J2SE modes.

## Deprecated VistALink APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The list of deprecated APIs in VistALink 1.6 is:

- gov.va.med.exception.FoundationsExceptionInterface (and implementers):
  - getFullStackTrace() method
  - getNestedException() method
- gov.va.med.exception.FoundationsException (and descendants):
  - getFullStackTrace() method
  - getNestedException() method
- gov.va.med.vistalink.adapter.cci.VistaLinkResourceException (and descendants):
  - getFullStackTrace() method
  - getNestedException() method
- gov.va.med.vistalink.security.VistaLoginModuleException (and descendants):
  - getFullStackTrace() method
  - getNestedException() method
- gov.va.med.exception.ExceptionUtils:
  - String getFullStackTrace() method
  - Throwable getNestedExceptionByClass() method
    - gov.va.med.xml.XmlUtilities:
  - String convertXmlToStr() method
  - Document getDocumentForXmlString() method
  - Document getDocumentForXmlInputStream() method
  - Attr getAttr() method
  - Node getNode() method
  - String XML_HEADER field

# Developer Workstation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## J2EE Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following libraries should be on the project classpath of your J2EE project in your integrated development environment (IDE), when developing modules using VistALink J2EE connectors:

- vljConnector-1.6.1.x.jar
- vljFoundationsLib-1.6.1.x.jar
- A J2EE 1.4 library (e.g., j2ee.jar, weblogic.jar, MyEclipseIDE's j2ee library, etc.)

The vlj\* library jars are provided in the /app-j2ee/shared-lib folder of the distribution zip file.

### J2EE Runtime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At runtime, additional libraries are required for your J2EE environment. See the *VistALink 1.6 Installation Guide* and the *VistALink 1.6 System Management Guide* for more information on setting up VistALink connectors in a J2EE container.

## J2SE Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IDE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following libraries need to be on the project classpath of your J2SE project in your IDE, when developing modules using VistALink client/server connectivity:

- vljConnector-1.6.1.x.jar
- vljFoundationsLib-1.6.1.x.jar
- vljSecurity-1.6.1.x.jar
- A jar containing J2EE 1.4 ResourceException classes (to meet this need,  
  geronimo-j2ee-connector_1.5_spec-1.0.1.jar is provided in VistALink distribution)

The vlj\* library jars and geronimo jar are provided in the /samples-J2SE folder of the VistALink 1.6 distribution file.

### J2SE Runtime

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At runtime, these additional jar files are required for your J2SE application to launch and run:

- log4j-core-2.x.x.jar
- log4j-api-2.x.x.jar
- A jar containing J2EE 1.4 ResourceException classes (to meet this need,  
  geronimo-j2ee-connector_1.5_spec-1.0.1.jar is provided in VistALink distribution)

These additional jars can also be found in the /samples-J2SE folder of the VistALink 1.6 distribution file.

# How to Use VistALink in J2EE Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using Station Number and Division

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink asks application code to provide Veteran's Health Affairs (VHA) institution station numbers in two situations, for different purposes: system location and multi-division awareness. Because these two modes of use are separate, the meaning of *station number* (also referred to as institution and division) is "overloaded." The two modes are described in the sections below.

### System Locator: Institution-Connector Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application code must provide a station number/division to retrieve a connector The Java Naming and Directory Interface (JNDI) name from VistALink's institution-mapping Application Programming Interface (API). Lacking anything better, station numbers are used as a location designator for a particular M system.

Each VistALink connector has a primaryStation attribute, configured by the J2EE administrator. The configured value should exactly match the DEFAULT INSTITUTION value in corresponding M system's KERNEL SYSTEM PARAMETERS file (#8989.3). VistALink uses primaryStation to confirm that a connector is accessing the correct M system: if the two values don't match, connections are rejected.

The primaryStation attribute is also the mapping source between station numbers and connector JNDI names. A VA-specific implementation of business rules around station numbers governs how the institution mapping API – getJndiConnectorNameForInstitution (division) in InstitutionMappingDelegate – matches a requested division with a given connector's primary station.

The mapping API can be passed either a primary station or a subdivision (a primary station number appended with a suffix such as 'A' or '9' (9 is a special case, representing a nursing home subdivision). Some examples of how the VA rules work for matching subdivisions with primary station numbers are as follows:

| Division (Institution Mapping API argument) | Maps to Primary Station |
|-------------------------------------------------|-----------------------------|
| 631                                             | 631                         |
| 631A                                            | 631                         |
| 6319                                            | 631                         |
| 639                                             | 639                         |
| 639A                                            | 639                         |
| 6399                                            | 639                         |

<span id="_Toc280220365" class="anchor"></span>Table 3‑1. VA Institution Mapping Rules Examples

The primary station for a connector (and for an M system) is almost always all-numeric (e.g., "523"). The main exception is 200-series station numbers, which are only allocated to Austin Information Technology Center (AITC) systems.

### Multidivision-Aware Application Code: ConnectionSpec Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Application code must also use the station number to create a connection spec, which it then uses to obtain a VistALink connection. When application code executes a remote procedure call (RPC), the division specified in the connection spec is passed to M to populate the variable User Number, or *DUZ(2)* on the M system. On M systems, setting the proper value for *DUZ(2)* makes applications multidivision-aware, to give the right view of the data. On merged systems, for example, an end-user might only see the set of patients matching the station number specified in their DUZ(2) (e.g., "523B").

Only one value can be set into *DUZ(2)* at a time. So, if you construct a connection spec (e.g., "connSpec = new VistaLinkVpidConnectionSpec(division, vpid)") and pass in "523B", VistALink sets DUZ(2) on the M side to "523B". RPCs are then executed under that setting (if it is granted as a permissible subdivision to the end-user.).

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a merged site, where an end-user has access to "631A" but not to "631", the institution mapping lookup for "631A" will return the connector whose primaryStation attribute is "631". If you create a connection spec and connection to execute an RPC and specify "631A", this value will be set into DUZ(2) on the M side. The RPC will execute with multi-division awareness, i.e., that the current institution is "631A".

## Request Cycle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using a J2CA connector such as VistALink in a J2EE environment to execute requests (RPCs) involves the following sequence of steps:

> 1\. Retrieve a particular VistALink connector's connection factory from JNDI

> 2\. Instantiate a ConnectionSpec to use for re-authentication over the connection

> 3\. Get a connection from the connection factory

> 4\. Execute a request over the connection

> 5\. Close the connection.

These steps are discussed in more detail in the sections below.

### Retrieving the Connection Factory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To retrieve a connection factory from JNDI, you need to know the JNDI name of the connection factory. Each VistALink connector going to a different destination will have a different JNDI name. For this example, assume that the JNDI name of the connection factory is "vlj/testconnector."

To retrieve the connection factory, make the following calls to JNDI:

String division="523A"; // ordinarily get from KAAJEE, FatKAAT, etc.

Context ic = new InitialContext();

String jndiName = InstitutionMappingDelegate.

getJndiConnectorNameForInstitution(division);

// cast JNDI object to VistaLinkConnectionFactory

VistaLinkConnectionFactory cf = (VistaLinkConnectionFactory) ic.lookup(jndiName);

Note that the object retrieved from the JNDI must be cast to the VistaLinkConnectionFactory class.

If your application hard-codes JNDI connection factory names, you may want to use the J2EE resource-ref mechanism to loosely couple a hard-coded JNDI name in your application source code to an administrator-modifiable mapping in your application deployment descriptors.

More likely, however, in a VA environment, your application would retrieve JNDI connection factory names *dynamically,* based on VA facility station number. See the "Institution Mapping" section later in this chapter, which describes how to connect to a particular VA site by getting the JNDI name for a connector's connection factory.

### Instantiating a Connection Spec for Re-authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before retrieving a connection from the connection factory object, you need to instantiate a connection spec. The connection spec is used to pass re-authentication information to the connection, identifying the user to run the request under on the target VistA M system. (For a complete discussion of VistALink's re-authentication mechanism, see "[More about Re-authentication](#more-about-re-authentication)" below, as well as the titled "Security" in the *VistALink System Management Guide*.)

The following connection specs are provided with VistALink for general application use:

- VistaLinkVpidConnectionSpec(division, vpid)
- VistaLinkDuzConnectionSpec(division, duz)
- VistaLinkAppProxyConnectionSpec(division, appProxyName)

To instantiate a VistaLinkVpidConnectionSpec, for example:

String vpid = "0000002987654321V654321000000";

VistaLinkVpidConnectionSpec connSpec = new

VistaLinkVpidConnectionSpec(division, vpid);

|                                                                                                                |                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/007.png) | REF: For more information on connection specs, see the section "[Connection Specification Classes](#connection-specification-classes)" in this document. |

### Getting a Connection (Connection Spec)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following code retrieves a VistALink connection from a given connection factory:

VistaLinkConnection myConnection = null;

// cast connection factory getConnection to VistaLinkConnection

myConnection = (VistaLinkConnection) cf.getConnection(connSpec);

myConnection.setTimeOut(10000); // set request timeout to 10 seconds

Every connection has a default timeout, which is the time the J2EE side of the connection waits for a response from the M system when executing an RPC. You can manually increase the timeout if you expect the RPCs to take a long time (as in the example above).

### Executing a Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have a connection, you can execute a request over the connection. In general, the steps to execute a request are:

1.  Create an RpcRequest object
2.  Set the RpcRequest name of the RPC to execute (RpcRequest.setRpcName)
3.  Set the type of request transmission format to use (we recommend proprietary in all cases, rather than eXtensible Markup Language (XML).
4.  Assert an RpcRequest authorization context (RpcRequest.setRpcContext)
5.  Set request parameters (if the request has any)
6.  Execute the request
7.  Process the results.

For example:

RpcRequest vReq = RpcRequestFactory.getRpcRequest();

vReq.setRpcName("XOBV TEST PING");

vReq.setUseProprietaryMessageFormat(true);

vReq.setRpcContext("XOBV VISTALINK TESTER");

RpcResponse vResp = myConnection.executeRPC(vReq);

String results = vResp.getResults();

More complete information on setting up a request, passing parameters to the request, and processing the response, is provided in the "[Executing Requests](#executing-requests)" section.

### Closing the Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The final step in executing a request is to close the connection. Doing this does not close the physical connection in J2EE; instead, it returns the connection to the connection pool it came from, for possible re-use on a subsequent request.

It is strongly recommended that you close the connection in a final block surrounding all of the code, beginning at getConnection(). Otherwise, errors will result in leaked connections that have not been returned to the pool, possibly causing the pool to run out of available connections for other callers.

### Complete Request Cycle

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example shows the complete request cycle, including closing the connection.

VistaLinkConnection myConnection = null;

String results = null;

String division="523A"; // ordinarily get from KAAJEE, FatKAAT, etc.

String vpid = "0000002987654321V654321000000"; // ditto

try {

Context ic = new InitialContext();

String jndiName = InstitutionMappingDelegate.

getJndiConnectorNameForInstitution(division);

VistaLinkConnectionFactory cf = (VistaLinkConnectionFactory)  
ic.lookup(jndiName);

VistaLinkVpidConnectionSpec connSpec = new

VistaLinkVpidConnectionSpec(division, vpid);

myConnection = (VistaLinkConnection) cf.getConnection(connSpec);

myConnection.setTimeOut(10000); // set 10 second socket timeout

RpcRequest vReq = RpcRequestFactory.getRpcRequest();

vReq.setUseProprietaryMessageFormat(true);

vReq.setRpcName("XOBV TEST PING");

vReq.setRpcContext("XOBV VISTALINK TESTER");

RpcResponse vResp = myConnection.executeRPC(vReq);

results = vResp.getResults();

} catch (VistaLinkFaultException e) {

// ...

} catch (NamingException e) {

// ...

} catch (ResourceException e) {

// ...

} catch (FoundationsException e) {

// ...

} finally {

if (myConnection != null) {

try {

myConnection.close();

} catch (ResourceException e) {

// ...

}

}

}

### Connectivity Failures and Retry Strategies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During an executeRPC()call, connectivity to the VistA system can fail due a network failure or anything else that breaks connectivity. The request's implementation of the VistaLinkRequestRetryStrategy interface determines whether VistALink automatically retries the request or not.

Connectivity can fail at any point while executing the original request. If it does, most or all of the work of the original request may have been performed already. You should take this into account when considering what retry strategy to use for your requests -- for example, whether a RPC retry could potentially add a second instance of a particular entry to a file.

By default, the implementation class VistaLinkRequestRetryStrategyAllow is set as the retry strategy for a request. Its single method, execute(), returns "true," causing VistALink to attempt to obtain a new connection and retry the request, exactly once.

In addition to VistaLinkRequestRetryStrategyAllow, an additional implementation class, VistaLinkRequestRetryStrategyDeny, is supplied. Its single method, execute(), returns "false." You can use this class in cases where you never want the request to be retried.

You can also supply your own implementation class for the VistaLinkRequestRetryStrategy interface that uses its own logic to determine whether to return "true" or "false" to allow or deny the retry attempt.

For example:

RpcRequest vReq = RpcRequestFactory.getRpcRequest();

vReq.setRpcName("XOBV TEST PING");

vReq.setRpcContext("XOBV VISTALINK TESTER");

vReq.setRetryStrategy(new VistaLinkRequestRetryStrategyDeny());

RpcResponse vResp = myConnection.executeRPC(vReq);

String results = vResp.getResults();

## More about Re-authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a connection is used by an *application*, VistALink uses re-authentication for the following reasons:

- The connection proxy user used by the adapter to connect to M should not have privileges
- Most RPCs need to run in the context of specific end-users.

Re-authentication is a lightweight security context switch from the application server adapter's user identity to the actual end-user identity.

The architecture of VistALink assumes that the identity of the end-user has already been authenticated (verified) by the calling application. Therefore, VistALink does not attempt to authenticate the end-user's identity. Instead, the re-authentication process matches the end-user identity already established by the calling application with a matching VistA New Person file entry.

When retrieving a VistALink connection from a connection factory, the application supplies end-user credentials as part of the connection specification. These credentials are used to switch security context on the M side, to re-authenticate the connection. This re-authentication process establishes the correct end-user environment on the M server (VPID, DUZ, etc) for the duration of the connection's use.

### Connection Specification Classes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To link identities, the application selects one of the following connection specifications to retrieve a connection:

| Connection Specification class | Required Credentials                                                             |
|------------------------------------|--------------------------------------------------------------------------------------|
| VistaLinkDuzConnectionSpec         | Division; known DUZ value of a specific end-user (to be deprecated in favor of VPID) |
| VistaLinkVpidConnectionSpec        | Division; known VPID value of a specific end-user                                    |
| VistaLinkAppProxyConnectionSpec    | Division; name of a user of the special user type "Application Proxy"                |

<span id="_Toc135039345" class="anchor"></span>Table 3‑2. Connection Specification Classes

VA Person ID (VPID) is the connection specification expected to be used in most production scenarios. Whatever end-user authentication mechanism is used by a Health*<u>e</u>*Vet-VistA application, the application should be able to obtain the VPID for a given end-user as an output from the authentication process. During RPC execution, when the end-user is authenticated, the J2EE application can use the VPID as a way to identify the end-user to any VistA M system.

|                                                                                                                |                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/008.png) | NOTE: Kernel patch XU\*8.0\*309 is required to support the VPID connection specification on M-VistA systems. |

DUZ (DuzConnectionSpec) is the primary re-authentication mechanism until the VPID infrastructure is fully rolled out. At that point DuzConnectionSpec will be deprecated, and VpidConnectionSpec will be the primary mechanism. In both cases, it is expected that the login will have been performed already through a Veterans Health Affairs (VHA)-approved authentication mechanism, and that the authentication mechanism will make the DUZ or VPID available for use by the application.

The Application Proxy connection specification is designed to be used in cases where the RPC should run on the Kernel/M system under the identity of an application, rather than an end-user.

### Institution/Division Rules for Re-authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For every connection spec, a division must be passed: the division parameter is mandatory. This requirement ensures that the division requested for a connection on behalf of a user matches the division under which the user's request is executed on the M system. It also helps to ensure that RPCs are not executed on the wrong M system.

All applications should already be multidivision-aware, so the VistALink requirement that an application know the end-user's division should be no additional burden to applications. This value is set by Kernel into DUZ(2) for the re-authenticated end-user.

The value to pass for the division parameter for any connection specification is the division station number, e.g., "523" or "523BZ". This is the value found in field 99 (Station Number) of the corresponding entry in the Institution File on the M system.

The following applies to user-based connection specs (VistaLinkVpidConnectionSpec and VistaLinkDuzConnectionSpec) on the M side:

- If the end-user's DIVISION (#200.02) multiple of their New Person file entry is empty, the division passed in with the connection spec must be the station number of the division set into the DEFAULT INSTITUTION (#217) field of the KERNEL SYSTEM PARAMETERS (#8989.3) file entry for the site.
- If an end-user has one or more divisions specified in the DIVISION (#200.02) multiple of their New Person file entry, the division passed in with the connection spec must be the station number for one of the divisions present in that multiple.

For the VistaLinkApplicationProxyConnectionSpec, the division must be a division supported on the computing system being connected to. In both cases, if the division passed does not meet the conditions above, re-authentication fails, and a SecurityDivisionDeterminationFaultException is returned to the calling application.

### Application Proxy User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel patch XU\*8.0\*361 provides the following public API for application proxy user support:

- CREATE(NAME,FMAC,OPT) ;Create an APPLICATION PROXY user<u>  
  </u>For a description of this API, see the Kernel Programmer Manual on the Kernel API Web site (http://vista.med.va.gov/kernel/apis/index.shtml) or the VistA Document Library ([<u>http://www.va.gov/vdl/application.asp?appid=10</u>](http://www.va.gov/vdl/application.asp?appid=10) ).

VistALink uses patch 361 functionality to implement a new re-authentication connection spec, VistaLinkAppProxyConnectionSpec. With this, re-authentication can be performed using an application proxy account on the M system, rather than under an end-user account.

The Application Proxy connection specification is expected to be used in either of the following special situations:

- The J2EE end-user does not have a user account on the M system on which an RPC is to be executed – i.e., when a service uses VistALink from an Enterprise Java Beans (EJB) (when an end-user is not practical)
- It is not appropriate for the RPC to execute under the identity of a particular end-user

To use the Application Proxy connection, you should understand the following:

- VistaLinkAppProxyConnectionSpec(String division, String appProxyName) is the constructor for the new connection spec.
- Kernel patch XU\*8\*361 supports the new functionality.
- SecurityIdentityDeterminationFaultException is thrown if re-authentication fails.
- For the division, you can specify any division that is valid for the site. Division checking is done against what is a valid division for the site, not against user-specific division settings.

> If your functionality is not multi-divisional, you can use "primary station" for the M system. This is the station number in the DEFAULT INSTITUTION field (#217) of the KERNEL SYSTEM PARAMETERS file (#8989.3) in the M account in question.

|                                                                                                                |                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/009.png) | NOTE: According to Infrastructure & Security Services, a valid division for a Kernel/M site is currently any division whose numeric M value (e.g., when "plussed") (1) equals the DEFAULT INSTITUTION station number, and (2) is not marked inactive in the Institution file at the site. |

- A "tester" application proxy user is distributed with VistALink, and added to the New Person file during the installation post-init. The proxy user is named XOBVTESTER,APPLICATION PROXY.
- The VistALink sample Web application demonstrates the use of all connection specs, including VistaLinkAppProxyConnectionSpec. The sample application makes use of the XOBVTESTER,APPLICATION PROXY user created during the VistALink installation post-init.

The M example of adding an application proxy user is shown below. In this case, the proxy name is passed into the function; no FileMan access code is added to the user; and the \[XOBV VISTALINK TESTER\] B-type option is added to the secondary menu of the proxy user:

ADDPROXY(XOBANAME) ; add application proxy if not present

; depends on XU\*8\*361

NEW XOBID

;

SET XOBID=\$\$CREATE^XUSAP(XOBANAME,"","XOBV VISTALINK TESTER","")

IF (+XOBID)\>0 DO

. ; actions if successfully added

IF (+XOBID)=0 DO

. ; actions if proxy user was already present

IF (+XOBID)\<0 DO

. ; actions if error – could not add user for some reason

QUIT

#### J2EE Application Proxy Usage Example

StringBuffer results = new StringBuffer();

String appProxyName = "XOBVTESTER,APPLICATION PROXY";

String division="11000"; // ordinarily get from KAAJEE, FatKAAT, etc.

try {

VistaLinkConnectionSpec connSpec = new

VistaLinkAppProxyConnectionSpec(division, appProxyName);

String jndiName = InstitutionMappingDelegate.

getJndiConnectorNameForInstitution(division);

Context ic = new InitialContext();

VistaLinkConnectionFactory cf = (VistaLinkConnectionFactory)

ic.lookup(jndiName);

VistaLinkConnection myConnection = (VistaLinkConnection)

cf.getConnection(connSpec);

RpcRequest vReq = RpcRequestFactory.getRpcRequest();

vReq.setUseProprietaryMessageFormat(true);

vReq.setRpcContext("XOBV VISTALINK TESTER");

vReq.setRpcName("XOBV TEST PING");

RpcResponse vResp = myConnection.executeRPC(vReq);

results.append("\<p\>" + rpcName + " Results: \<b\>" +

vResp.getResults() + "\</b\>");

} catch (Exception e) {

// ...

} finally {

if (myConnection != null) {

try {

myConnection.close();

} catch (ResourceException e) {

//...

}

}

}

<span id="_Appendix_C__Deploying_Multiple_Vist" class="anchor"></span>

## Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Socket-Level Forced Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A simple socket timeout capability is provided so that the Java side of the connection can simply time out the M side of the connection if an RPC is taking too long to execute. If the timeout is reached, the socket will drop the connection to M. On the M side, the RPC will terminate ungracefully.

For RPCs that are known to be long-running, you may want to use the socket timeout in conjunction with a graceful RPC timeout. Set the socket timeout slightly longer than you set the graceful RPC-based request-level timeout. (See the "[Graceful (Request-Level) Timeout](#_Graceful_(Request-Level)_Timeout)" section below for more information about how to implement graceful timeouts.)

#### Setting Socket-Level Timeouts

The socket-level timeout can be set in two ways:

- On the connection object, the setTimeOut() method will set a socket timeout, in milliseconds, that will be used for all RPCs executed over the connection. For example:

// set timeout for all requests sent over this connection to 10 seconds

myConnection.setTimeOut(10000);

- On the RPC request, the socket timeout can be set for a single request:

// set request timeout to 10 seconds, for this request only

myRpcRequest.setTimeOut(10000);

#### Default Socket-Level Timeout

All connectors are configured with a default socket timeout, so that if a request takes infinitely long to complete, a socket timeout will eventually always be triggered.

Administrators can selectively configure (tune) the default socket timeout for each connector, depending on the WAN performance and system performance for reaching any given M system. The default timeout is set in the gov.va.med.vistalink.connectorConfig.xml file. (See the section "Connector Settings," in the *VistALink 1.6 System Management Guide*.)

#### Changing Socket Timeout as a Multiple of Default Timeout

If you are going to programmatically adjust the timeout, you may want to obtain the current timeout for the connector first, multiply it by a factor, and then set the new timeout. This takes advantage of any tuning the administrators may have done for a particular connector.

Example:

// increase timeout by a factor of two

int timeout = myConnection.getTimeOut();

myConnection.setTimeOut(timeout\*2);

<span id="_Graceful_(Request-Level)_Timeout" class="anchor"></span>

### Graceful (Request-Level) Timeout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to using a socket timeout, the calling Java application can also pass a graceful timeout value to the RPC it is going to execute. To implement a graceful timeout, the RPC code that is executing must check whether it has timed out against this timeout value. A set of M APIs is provided for applications to check whether their RPC has timed out, based on the value passed by the calling application with the request.

Implementing a graceful timeout requires a delicate synchronization process between the graceful timeout, the socket timeout, and the RPC execution on the M side. Therefore, the graceful timeout is only recommended if your application needs more than what the socket timeout provides.

To implement a graceful timeout:

1.  Java-side: The calling application sets the request level RpcClientTimeout property, with RpcRequest.setRpcClientTimeOut(numberOfSeconds).
2.  Java-side: Make sure the current connection-level socket timeout (in milliseconds) evaluates to a longer period than the graceful timeout (in seconds). Otherwise the socket may timeout anyway before the graceful timeout is reached. For example, if you set RpcRequest.setRpcClientTimeOut(10), you could do myConnection.setTimeOut(15000), i.e., 15 seconds.
3.  M-side RPC: The RPC code should periodically check (e.g., if code is executing an iterative loop) if the RPC has exceeded the client timeout by calling \$\$STOP^XOBVLIB(). Return values from \$\$STOP^XOBVLIB are: "1" (application should stop processing, timeout has been exceeded) or "0" (continue processing).
4.  Java-side: The calling application can catch the RpcTimeOutFaultException in the try/catch code surrounding its RPC execute call. If the calling application catches this exception when executing an RPC, it means the M-side RPC checked STOP^XOBVLIB, was notified that a timeout had occurred, and did not reset the timeout value.

|                                                                                                                |                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/010.png) | NOTE: If the RPC continues processing without resetting the timeout after receiving a timeout indicator from \$\$STOP^XOBVLIB, the RPC may complete, but VistALink will return an RpcTimeOutFaultException to the client. |

#### STOP^XOBVLIB()

Used by the application to determine if processing should stop.

Input variables: (none)

Output variables: Return value. "1" is an indicator to stop processing; "0" is an indicator to

continue processing. I "1" is returned, and internal "timed out" indicator is also set.

|                                                                                                                 |                                                                                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/011.png) | NOTE: If you call STOP^XOBVLIB and it returns 1, a fault will be returned to the calling Java application. This will happen even if your RPC code completes, unless you call SETTO^XOBVLIB to increase the timeout and then call STOP^XOBVLIB to clear the "timed out" indicator based on the higher timeout value. |

#### \$\$GETTO^XOBVLIB()

Get the current timeout value (default = 300 seconds). An application would call this to obtain the current timeout value.

Output Variable: Return value, which is the timeout value, if it exists (in seconds), or the default of 300 seconds.

#### \$\$SETTO^XOBVLIB()

Override the current "graceful" timeout setting received from the client via RpcRequest.setRpcClientTimeout(int) or the default.

It is suggested that you call STOP^XOBVLIB immediately after resetting the timeout value, in order to reset the current timeout indicator based on the new timeout value.

Input Variable: TO. TO is the RPC timeout value in seconds. This is always the total number of seconds since the RPC began; it is not an increment from the current time.

Output Variable: Return value. The function sets the RPC timeout value (in seconds) and returns a "1" to indicate value successfully reset or 0 if not successful.

For example, if the M-side RPC wants "more time" after getting a "1" from \$\$STOP^XOBVLIB, it can use the \$\$SETTTO call to do so. However, this is risky, because the socket-level timeout may time out the connection anyway, particularly if the calling application set the socket-level timeout just higher than it set the graceful RPC timeout.

To add "more time" (though it risks running into a socket-level timeout), an RPC could get the current timeout value (\$\$GETTO^XOBVLIB), increase it, and then reset the higher value with \$\$SETTO^XOBVLIB. It should also call \$\$STOP^XOBVLIB immediately after calling \$\$SETTO, in order to reset the "timed out" indicator based on the new value. \$\$STOP needs to be called again because the new \$SETTO value may not have been large enough. The timeout check is always calculated from the start of the RPC, not the reset.

#### Java and M Code RPC Timeout Call Examples

Java-side example:

// increase socket timeout by a factor of two and

// use the original socket timeout as RPC client timeout

int timeout = myConnection.getTimeOut();

myConnection.setTimeOut(timeout\*5);

myConnection.setRpcClientTimeOut(timeout/1000);

M/VistA-side example:

...

F S IEN=\$O(ARR(IEN)) Q:IEN="" DO I \$\$STOP^XOBVLIB() DO CLEANUP QUIT

. DO PROCESS(IEN)

...

## Institution Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health*<u>e</u>*Vet-VistA applications need to be able to dynamically retrieve connectors to various VistA systems. The connecting systems to will change over time, so hard-coding of connector references is out of the question.

VistALink provides an Institution Mapping facility so that administrators deploying VistALink connectors can map each connector to a specific VHA institution, using that institution's station number. Health*<u>e</u>*Vet-VistA applications can then retrieve the JNDI name for a connector to a particular institution, using the institution mapping facility. This utility is in the gov.va.med.vistalink.institution package.

There is no requirement to use this utility to use VistALink. The utility merely provides a way for administrators to associate station numbers with JNDI names, and for runtime code to retrieve the mapping.

### How to Configure Mappings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each connector is configured in a file named gov.va.med.vistalink.connectorConfig.xml. Each connector's settings are stored in a unique \<connector\> element in that file. The station number and JNDI name it maps to are both XML attributes of the \<connector\> element.

Refer to the *VistALink 1.6 Installation Guide* and the *VistALink System Management Guide* for a complete description of how to configure VistALink's institution mappings for each VistALink connector.

### How to View the Currently Loaded Mappings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can view the currently loaded institution mappings for a given server using the VistALink administration console. Refer to the *VistALink 1.6 System Management Guide* for a complete description of the VistALink administration console.

### Retrieving Mappings for Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A static method, getJndiConnectorNameForInstitution, is provided in the class gov.va.med.vistalink.institution.InstitutionMappingDelegate. This class provides application access to the institution mappings. For example:

String stationNumber = 500;

String jndiConnectorName = null;

try {  
jndiConnectorName =

InstitutionMappingDelegate.getJndiConnectorNameForInstitution(

stationNumber);  
} catch (InstitutionMappingNotFoundException e) {  
// take some action  
} catch (InstitutionMapNotInitializedException e) {  
// take some action  
}

### Subdivisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When retrieving the JNDI name for a particular station number, you should pass the exact subdivision you are working with to the getJndiConnectorNameForInstitution() call (e.g., "523A", "523B", or "523"). This API determines the correct connector associated with a given station number, even if the station number parameter passed to it is a subdivision (usually *but not always* signified by the presence of alpha characters after the numeric portion of the station number).

## VistALink Java API Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a complete reference to all of the Java-side VistALink interfaces, classes, methods and exceptions, please see the Javadoc API documentation provided in the VistALink 1.6 distribution file.

This page is left blank intentionally.

# Executing Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Remote Procedure Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A remote procedure call (RPC) is a defined call to M code that runs on an M server. Through the RPC Broker, a client application can make a call to the M server and execute an RPC on the M server. This is the mechanism through which a client application can:

- Send data to an M server
- Execute code on an M server
- Retrieve data from an M server

An RPC can take optional parameters to do a task and then return either a single value or an array to the client application.

|                                                                                                                |                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/012.png) | REF: For detailed information on RPCs, please refer to *Getting Started With the Broker Development Kit (BDK)* and/or the *RPC Broker Technical Manual*. You can find both publications at [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/). |

### RPC Security ("B"-Type Option)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All RPCs are secured with an RPC context (a "B"-type option). The end-user on whose behalf an RPC is executed must have the "B"-type option associated with the RPC in their menu tree. Otherwise an exception is thrown.

|                                                                                                                |                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/013.png) | REF: For more information on RPC security, see *Getting Started with the BDK, Chapter 3 (Extract): RPC Overview*, which is bundled in the /rpc-doc folder of the VistALink distribution, as the file xwb1_1p13dg-rpc_extract.pdf. |

### RPCs for Use by Application Proxy Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPCs must be explicitly marked as supporting execution by an application proxy user, in order to be used by one. The new field APP PROXY ALLOWED (#.11) in the REMOTE PROCEDURE file (#8994) must be marked "YES." RPCs should only be marked for application proxy use if:

- The business logic behind the RPC is valid when the DUZ represents an application proxy user (rather than end-user)
- The application expects to be executed by an application proxy user.

## Request Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

During interactions with M from Java, developers use the RpcRequest object. The RpcRequest object encapsulates the data that will be sent to M to execute an interaction, i.e. the RPC name, RPC parameters, and RPC context. The RpcRequest object is constructed using the RpcRequestFactory object. The RPC parameters are accessed through the RpcRequest objects via the clearParams(), getParams() and setParams() methods.

### Get an RpcRequest Object: RpcRequestFactory Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RpcRequest class represents a request from Java to M. As the transport format, it permits the use of either XML or a proprietary format. The proprietary format is the default and is recommended because it is faster. This class also exposes methods for specifying Rpc Name, Rpc Context and the parameters used by M to execute the RPC.

The RpcRequestFactory class is responsible for creating instances of RpcRequest. In order to create an RpcRequest, the developer must call the static getRpcRequest method on this class. In the example shown below, getRpcRequest is overloaded with three declarations:

> <span class="mark">publicstatic RpcRequest getRpcRequest() throws FoundationsException</span>

This method is used to create a default RpcRequest with no specified Rpc Name or Rpc Context. You must specify the Rpc Context and the Rpc Name on the RpcRequest object before you can use this object in an interaction. Refer to javadoc on RpcRequest for more information:

> <span class="mark">publicstatic RpcRequest getRpcRequest(String rpcContext)</span> <span class="mark">throws FoundationsException</span>

This method is used to create a RpcRequest with the specified Rpc Context. You must specify the Rpc Name on the RpcRequest object before you can use this object in an interaction.

> <span class="mark">publicstatic RpcRequest getRpcRequest(String rpcContext, String rpcName)</span> <span class="mark">throws FoundationsException</span>

Refer to the Javadocs on RpcRequest for more information.

This method is used to create a RpcRequest with the specified Rpc Context and the Rpc Name. You may still specify another Rpc Context and Rpc Name on this object. Refer to the JavaDocs on RpcRequest for more information.

#### getRpcRequest() Example 

<span class="mark">RpcRequest vReq = null;</span>

<span class="mark">//The Rpc Context</span>

<span class="mark">String rpcContext = "XOBV VISTALINK TESTER";</span>

<span class="mark">//The Rpc to call</span>

<span class="mark">String rpcName = "XWB GET VARIABLE VALUE";</span>

<span class="mark"></span>

<span class="mark">// Construct the request object</span><span class="mark">try{</span>

<span class="mark">vReq = RpcRequestFactory.getRpcRequest(rpcContext, rpcName);</span>

} catch(FoundationsException e) {// process exception as needed}

### Set RpcRequest Parameters: "Explicit" Style

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two ways of passing RPC parameters to an RpcRequest object. For convenience, the first method is referred to as "explicit" style, the second method as "setParams" style.

In explicit style, the method of passing RPC parameters corresponds very closely to the underlying RPC parameters. The RPC Broker has three input parameter types for RPC calls. These map to VistALink RpcRequestParam parameter types as follows:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 29%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>RPC parameter type</strong></th>
<th><strong>VistALink RpcRequestParam type</strong></th>
<th><strong>Java value type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Literal</td>
<td>"string"</td>
<td><strong>String</strong></td>
</tr>
<tr class="even">
<td>Reference</td>
<td>"ref"</td>
<td><strong>String</strong></td>
</tr>
<tr class="odd">
<td>List</td>
<td>"array"</td>
<td><p><strong>List</strong> (Specify array indices yourself; supports non-integer, negative, or multi-level indices)</p>
<p><strong>Map</strong> or <strong>Set</strong> (index automatically generated as a single-level, integer, sequence)</p></td>
</tr>
</tbody>
</table>

To pass parameters into an RpcRequest, you should retrieve the RpcRequest's mutable RpcRequestParam object, accessible by RpcRequest.getParams(). Then, call setParam() on that object to define each RPC parameter:

> void setParam(int position, String type, Object value)

The parameters to this call are:

- position: the expected RPC parameter list position where the RPC expects to see the RPC parameter
- type: can be "string", "ref" or "array" (to match the expected RPC parameter type)
- value: an object that is the value of the RPC parameter. For "string" or "ref" types, the object should be a string. For "array" types, the object should implement the Map, List or Set interface.

#### Literal RPC Parameter Example

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">vReq.getParams().setParam(1, "string", "I am a string");</span>

#### Reference RPC Parameter Example

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">vReq.getParams().setParam(1, "ref", "DTIME");</span>

#### List RPC Parameter Example:

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList nums = new ArrayList();</span>

<span class="mark">nums.add("3");</span>

<span class="mark">nums.add("5");</span>

<span class="mark">nums.add("4");</span>

<span class="mark">nums.add("1");</span>

<span class="mark">nums.add("7");</span>

<span class="mark">nums.add("8");</span>

<span class="mark">nums.add("2");</span>

<span class="mark">nums.add("6");</span>

<span class="mark">nums.add("9");</span>

<span class="mark">vReq.getParams().setParam(1, "array", nums);</span>

#### Combination RPC Parameter Example:

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList nums = new ArrayList();</span>

<span class="mark">nums.add("3");</span>

<span class="mark">nums.add("5");</span>

<span class="mark">nums.add("4");</span>

<span class="mark">nums.add("1");</span>

<span class="mark">nums.add("7");</span>

<span class="mark">nums.add("8");</span>

<span class="mark">nums.add("2");</span>

<span class="mark">nums.add("6");</span>

<span class="mark">nums.add("9");</span>

<span class="mark">vReq.getParams().setParam(1, "array", nums);</span>

<span class="mark">vReq.getParams().setParam(2, "string", "I am a string");</span>

<span class="mark">vReq.getParams().setParam(3, "ref", "DTIME");</span>

### Set RpcRequest Parameters: "setParams" Style

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A second style of passing RPC parameters for an RPC into an RpcRequest object is called the "setParams" style. This method offers a small amount of abstraction from the underlying RPC, although parameters still must correspond directly to what is expected by the RPC being invoked.

With the setParams style, you create an object that implements the List interface and holds each of the parameters as an object entry in the list. Add each parameter to the List as an object value, and then use RpcRequest.setParams(List) to pass the RPC parameters to the request.

The RpcRequest object processes the List internally extracting the RPC parameter characteristics for the request as follows:

- position: Determined by the order each object was added to the List. The first object added becomes the first RPC parameter, the second becomes the second, and so forth.
- type:
- If an object found in the List is a String, it is passed as an RPC literal parameter.
- If an object found in the List implements the Map, List, or Set interfaces, it is passed as an RPC List parameter.
- If an object found in the List is an instance of the special RpcReferenceType class, it is passed as an RPC reference parameter.
- value: The value for the RPC parameter is simply the object added to the List for each parameter.

#### Literal RPC Parameter Example:

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList params = new ArrayList();</span>

<span class="mark">params.add("I am a string");</span>

<span class="mark">vReq.setParams(params);</span>

#### Reference RPC Parameter Example:

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList params = new ArrayList();</span>

<span class="mark">params.add(new RpcReferenceType("DTIME"));</span>

<span class="mark">vReq.setParams(params);</span>

#### List RPC Parameter Example:

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList params = new ArrayList();</span>

<span class="mark">ArrayList nums = new ArrayList();</span>

<span class="mark">nums.add("3");</span>

<span class="mark">nums.add("5");</span>

<span class="mark">nums.add("4");</span>

<span class="mark">nums.add("1");</span>

<span class="mark">nums.add("7");</span>

<span class="mark">nums.add("8");</span>

<span class="mark">nums.add("2");</span>

<span class="mark">nums.add("6");</span>

<span class="mark">nums.add("9");</span>

<span class="mark">params.add(nums);</span>

<span class="mark">vReq.setParams(params);</span>

#### Combination RPC Parameter Example:

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList params = new ArrayList();</span>

<span class="mark">ArrayList nums = new ArrayList();</span>

<span class="mark">nums.add("3");</span>

<span class="mark">nums.add("5");</span>

<span class="mark">nums.add("4");</span>

<span class="mark">nums.add("1");</span>

<span class="mark">nums.add("7");</span>

<span class="mark">nums.add("8");</span>

<span class="mark">nums.add("2");</span>

<span class="mark">nums.add("6");</span>

<span class="mark">nums.add("9");</span>

<span class="mark">params.add(nums);</span>

<span class="mark">params.add("I am a string");</span>

<span class="mark">params.add(new RpcReferenceType("DTIME"));</span>

<span class="mark">vReq.setParams(params);</span>

### Specifying Indices for List-Type RPC Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

List-type RPC parameter values can be passed to VistALink in Java objects that implement the List, Set, or Map interfaces.

If you pass List-type parameter values in an object that implements List or Set (but not Map), the array index is automatically generated for you, as a single-level, integer, sequential index starting at "1." (The array becomes the array subscript level in M for the data.) This can be convenient if the array index is not significant for your RPC.

However, if you need any of the following features in your array when it is passed to M, use an object that implements Map (such as HashMap) instead:

- Negative index values
- Non-sequential index values
- Control over the index start point
- Non-integer index values
- Multi-level indices (\>1 subscript level in M)

For each entry added to the Map object, the key becomes the M subscript, and the value becomes the M value.

To pass a multi-level subscript, use the RpcRequest.buildMultipleMSubscriptKey() method to generated the HashMap key.

#### List RPC Parameter Example (Explicit Index)

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList params = new ArrayList();</span>

<span class="mark">HashMap hm = new HashMap();</span>

<span class="mark">hm.add(".11", "0");</span>

<span class="mark">hm.add("1202", "23");</span>

<span class="mark">hm.add("1205", "595");</span>

<span class="mark">hm.add("time", "NOW");</span>

<span class="mark">params.add(hm);</span>

<span class="mark">vReq.setParams(params);</span>

#### List RPC Parameter Example (Explicit Multi-Level Index)

<span class="mark">RpcRequest vReq = RpcRequestFactory.getRpcRequest();</span>

<span class="mark">ArrayList params = new ArrayList();</span>

<span class="mark">HashMap hm = new HashMap();</span>

<span class="mark">hm.put(RpcRequest.buildMultipleMSubscriptKey("\\FRUIT\\,1"), "Apple");</span>

<span class="mark">hm.put(RpcRequest.buildMultipleMSubscriptKey("\\FRUIT\\,2"), "Orange");</span>

<span class="mark">hm.put(RpcRequest.buildMultipleMSubscriptKey("\\FRUIT\\,3"), "Pear");</span>

<span class="mark">hm.put(RpcRequest.buildMultipleMSubscriptKey("\\FRUIT\\,4"), "'nana");</span>

<span class="mark">params.add(hm);</span>

<span class="mark">vReq.setParams(params);</span>

### Other Useful RpcRequest Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">For a complete list of other available RpcRequest methods, please see the Javadoc for RpcRequest.</span>

#### Clear Previous Request Parameters

<span class="mark">If you are re-using a request object for additional requests, the RpcRequest.clearParams method is provided so that you can clear any existing parameters. You should call this method before attempting to set RPC parameters for subsequent requests:</span>

<span class="mark">//clear the params</span>

<span class="mark">vReq.clearParams();</span>

#### Set the Message Format (Proprietary or XML)

<span class="mark">VistALink's XML message format is based on the XML standard.</span> As the transport format, it permits the use of either XML or a proprietary format. <span class="mark">RpcRequest</span> defaults to the proprietary format because it is faster.

<span class="mark">//Set the request to use the propietary message format</span>

<span class="mark">vReq.setUseProprietaryMessageFormat(true);</span>

<span class="mark">//Set the request to use the XML message format</span>

<span class="mark">vReq.setUseProprietaryMessageFormat(false);</span>

#### Set the RPC Context

<span class="mark">If you are re-using a request object for additional requests, you can change the RPC Context with this method:</span>

<span class="mark">private static final String RPCCONTEXT = "XOBV VISTALINK TESTER";</span>

<span class="mark">vReq.setRpcContext(RPCCONTEXT);</span>

#### Set the RPC Name

<span class="mark">If you are re-using a request object for additional requests, you can change the RPC Name with this method:</span>

> <span class="mark">vReq.setRpcName("XOBV TEST NOT IN CONTEXT");</span>

#### Set the RPC Client Timeout

<span class="mark">This method sets a "graceful" timeout period that is made available to the RPC code on the M system. It is up to the M code to honor the timeout period, however. The value sent defaults to 600 seconds. You can change this value by calling the setRpcClientTimeOut method:</span>

<span class="mark">private static final int TIMEOUT = 300;</span>

<span class="mark">vReq.setRpcClientTimeOut(TIMEOUT);</span>

|                                                                                                                |                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/014.png) | <span class="mark">REF: For more information on the different kinds of timeouts, see the "</span>[<span class="mark"></span>Timeouts](#_Appendix_C__Deploying_Multiple_Vist)<span class="mark">" section.</span> |

## Response Processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">Once you have set up RpcRequest, you can execute an RPC interaction on the VistALinkConnection object, using the RpcRequest object. Doing this returns an RpcResponse object. RpcResponse is a value object that provides information about the response returned from M.</span>

### RpcResponse Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">The RpcResponse class is a value object that provides information about the response returned from M. The RpcResponse object exposes methods to retrieve the results, results type, and an org.w3c.dom.document object that contains the results, if the results are in XML format.</span>

### Request/Response Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">//request and response objects</span>

<span class="mark">RpcRequest vReq = null;</span>

<span class="mark">RpcResponse vResp = null;</span>

<span class="mark"></span>

<span class="mark">//The Rpc Context</span>

<span class="mark">String rpcContext = "XOBV VISTALINK TESTER";</span>

<span class="mark">//The Rpc to call</span>

<span class="mark">String rpcName = "XOBV TEST STRING";</span>

<span class="mark"></span>

<span class="mark">//Construct the request object</span>

<span class="mark">try {</span>

<span class="mark">vReq = RpcRequestFactory.getRpcRequest(rpcContext, rpcName);</span>

} catch(FoundationsException e) {

// process exception as needed

}

<span class="mark">//clear the params</span>

<span class="mark">vReq.clearParams();</span>

<span class="mark"></span>

<span class="mark">//Set the params</span>

<span class="mark">vReq.getParams(). setParam(1, "string", "This is a test string!");</span>

<span class="mark">//Set the request to use the proprietary message format</span>

<span class="mark">vReq.setUseProprietaryMessageFormat(true);</span>

<span class="mark">//Execute the Rpc and construct the response with the</span><span class="mark">//RpcResponseFactory</span><span class="mark">try {</span>

<span class="mark">vResp = vistaLinkConnection.executeRPC(vReq);</span>

<span class="mark">} catch(VistaLinkFaultException e) {</span>

// process exception as needed

<span class="mark">} catch(FoundationsException e) {</span>

// process exception as needed

<span class="mark">}</span>

<span class="mark"></span>

<span class="mark">//Display the response</span>

<span class="mark">System.out.println(vResp.getResults());</span>

### Parsing RPC Results

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All results from RPCs are returned as a single string from RpcResponse.getResults().

The RPC Broker defines five return types for RPCs (at the time of the current VistALink release). The mapping between these return types and the single string returned through VistALink are as follows:

| RPC Return Type | VistALink Result String Format                                                                  |
|---------------------|-----------------------------------------------------------------------------------------------------|
| Single Value        | As-is                                                                                               |
| Global Instance     | As-is                                                                                               |
| Array               | All array nodes concatenated sequentially, with each delimited by linefeed (ASCII 10) character     |
| Global Array        | All array nodes concatenated sequentially, with each delimited by linefeed (ASCII 10) character     |
| Word Processing     | Each word processing "line" concatenated sequentially, separated by a linefeed (ASCII 10) character |

<span id="_Toc135039346" class="anchor"></span>Table 4‑1. Mapping RPC Return Types to VistALink Result String Format

One easy way to parse array-type results concatenated with line feeds is with the Java string tokenizer. For example:

<span class="mark">StringTokenizer st = new StringTokenizer(vResp.getResults(), "\n");</span>

<span class="mark">int cnt = st.countTokens();</span>

<span class="mark">for (int i = 0; i \< cnt; i++) {</span>

<span class="mark">system.out.println("Result node " + i + ": " + st.nextToken());</span>

<span class="mark">}</span>

|                                                                                                             |                                                                                                                  |
|-------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/015.png) | In JDK 1.5 and forward, Sun deprecates StringTokenizer in favor of the split() function in java.lang.String. |

### XML Responses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some newer RPCs may choose to return their results as an XML document. The RpcResponse class provides two helper methods to turn the normal results string into an XML document. If you expect the results from an RPC to be an XML document, you can call RpcResponse.isXmlResponse to confirm if the response is in XML format, and RpcResponse.getResultsDocument to convert the result string into an XML document:

<span class="mark">//</span>Get a org.w3c.dom.document object that contains the results if set

<span class="mark">if (vReq.isXmlResponse()) {</span>

<span class="mark">org.w3c.dom.document xmlDoc = null;</span>

<span class="mark">try{</span>

<span class="mark">xmlDoc = vResp.getResultsDocument());</span>

<span class="mark">}catch(RpcResponseTypeIsNotXmlException e){</span>

<span class="mark">// process exception as needed</span>

<span class="mark">}catch(FoundationsException e){</span>

<span class="mark">// process exception as needed</span>

<span class="mark">}</span>

<span class="mark">}</span>

## How to Write RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For guidelines on how to write RPC Broker RPCs, please refer to the extract *Getting Started With The BDK Chapter 3 (Extract): RPC Overview* from the *RPC Broker* manual, bundled in the /rpc-doc folder of the VistALink distribution. Some special considerations apply to writing RPCs in the new modes supported by VistALink, including n-tier. These are discussed in the sections below.

### Write Stateless RPCs Whenever Possible

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When writing new RPCs to execute in an n-tier environment, we recommend making them stateless whenever possible. "Stateless" means that each RPC execution is standalone: when a sequence of RPCs is executed, there is no state maintained on the M system between RPC executions. This way, if you need to use an RPC from one sequence of RPCs in another sequence, your code will be more flexible.

The two main M-side state mechanisms traditionally used in RPCs -- \$J (as a temporary storage index) and global locking -- are both problematic in an n-tier environment. In the n-tier model, there is no guarantee that your requests will execute in the same M job partition. Middle-tier code will be retrieving and returning VistALink connections to a connection pool across a number of client-tier accesses, and because connections are not "dedicated" to a single user session, the underlying M partition may be a different one each time, with a different \$J.

### When State is Needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you do need to maintain state on the M system between RPC invocations, the two approaches discussed in the sections below are recommended. They are more compatible with the n-tier model.

#### Session ID as Temporary Storage Index

Rather than using \$J for a temporary storage index, we recommend that you implement a session ID, guaranteed to be unique on the M system, to index storage on the M system, and that you maintain the session ID state on the middle tier. You can then use the session ID between middle-tier invocations on a variety of connections with different underlying \$Js and still be able to consistently retrieve your indexed temporary data from the M system.

|                                                                                                                |                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/016.png) | NOTE: Kernel may provide a new API for middle tiers to obtain a guaranteed unique M system session identifier to index temporary storage locations. |

#### FileMan-Based Lock File

An alternative to the M LOCK command is to implement a FileMan-based lock file mechanism to synchronize locking across requests, connections, and middle-tier accesses. Note that a lock file needs to be used in all application code that needs to honor the lock – whether "roll & scroll," client-server, or n-tier.

You will probably also need APIs for locking and unlocking. Locks should probably be unlocked automatically after a period of time (e.g., lost connection) or based on some state change or event in the application session.

### Pitfalls of Using of \$JOB in Stateful RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When running RPCs in an n-tier model, there is no guarantee that all your requests will execute in the same M job partition. Your middle tier will be retrieving and returning VistALink connections to a connection pool across client-tier accesses, and each connection retrieved from the connection pool may have a different \$J.

If you have an RPC sequence that shares data across RPCs using temporary M storage indexed by \$J, the RPC sequence must be performed over the same connection (or else \$J will change). In n-tier mode, this means the RPC sequence must be executed over one connection before closing it (returning it to the connection pool).

Another \$J-related issue can occur even if you execute an RPC sequence over a single connection. The default VistaLinkRequestRetryStrategy implementation allows a request to be retried. If you use it and connectivity fails, the request will be retried on a new connection, and therefore using a new \$J. So if your RPCs communicate by leaving values on the M system indexed by \$J, you should consider using VistaLinkRequestRetryStrategyDeny for those requests.

### Pitfalls of Global Locking in Stateful RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When running RPCs in an n-tier model, locking global nodes across RPCs presents the same issues as when using \$J across RPCs. In particular, you cannot lock data in an RPC over one connection and unlock data in a different connection. Also, if the M partition that sets a lock exits, the M operating system automatically clears the lock. Therefore locking can only be used safely within a single RPC, or within an RPC sequence that will be executed over a single connection.

As with \$J, another locking-related issue can occur if network connectivity fails and your request is retried (which would be over a different connection). Therefore you should consider using VistaLinkRequestRetryStrategyDeny for requests that depend on locking across RPCs: if connectivity fails and a request is retried, the request will be retried over a new connection that does not own the lock. (The lock may be released anyway, since the previous partition will probably exit as a consequence of the network connectivity failure).

# VistALink Exception Reference

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink, like any other Java application, uses exceptions to indicate various error conditions that can occur during execution. VistALink throws only checked exceptions.

## Exception Nesting Changes Since VistALink 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous versions of VistALink were designed to work with Java version 1.3, which did not support nested exceptions. As a result, nested exception capability was built into all VistALink exception classes. Now that Java version 1.4 and above support nested exceptions "out of the box", VistaLink's nested exception facilities are deprecated, the classes themselves have been internally redirected to store nested exceptions using Java's nested exception functionality instead.

Any code that is using VistALink's deprecated nested exception facilities should switch to the standard Java nested exception facilities. In particular:

- Any code using the getNestedException() method of any VistALink-provided exception (defined, and now deprecated, in FoundationsExceptionInterface) should switch to the JRE-provided Throwable.getCause() method instead.
- Any code using the getFullStackTrace() method of any VistALink-provided exception should switch to the JRE-provided Throwable.getStackTrace() instead.

## VistALink Exception Hierarchy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink security modules and the VistALink resource adapter modules often throw more exceptions more specific than what is declared to be thrown.

Because VistALink implements various Java specifications (e.g., Java Authentication and Authorization Service (JAAS) and J2EE Connectors), each Java specification dictates usage of a specific base exception class. To be able to work with all types of exceptions, VistALink also defines one unifying exception interface: gov.va.med.exception.FoundationsExceptionInterface.

For example, where the JAAS specification requires a LoginException to be thrown, methods in the VistaLinkLoginModule may throw VistaLoginModuleException (which subclasses LoginException and implements FoundationsExceptionInterface) or an even more specific exception like VistaLoginModuleNoJobSlotsAvailableException.<span id="_VistALink_Exception_Hierarchy" class="anchor"></span>

### Common FoundationsExceptionInterface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

gov.va.med.exception.FoundationsExceptionInterface is defined to be able to have common interface for all types of VistALink exceptions. Implementation of this interface allows gov.va.med.exception.ExceptionUtils to work exceptions, no matter what they inherit from.

FoundationsExceptionInterface

│

├ FoundationsException (extends java.lang.Exception)

│ │

│ ├ InstitutionMapNotInitializedException

│ ├ InstitutionMappingNotFoundException

│ ├ RpcResponseTypeIsNotXmlException

│ ├ VistaKernelHashCountLimitExceededException

│ │

│ ├ VistaLinkFaultException

│ │ │

│ │ ├ LoginsDisabledFaultException

│ │ ├ NoJobSlotsAvailableFaultException

│ │ ├ RpcFaultException

│ │ │ ├ NoRpcContextFaultException

│ │ │ ├ RpcNotInContextFaultException

│ │ │ └ RpcTimeOutFaultException

│ │ │ └ RpcNotOkForProxyUseException

│ │ │

│ │ └ SecurityFaultException

│ │ ├ SecurityAccessVerifyCodePairInvalidException

│ │ ├ SecurityConnectionProxyException

│ │ ├ SecurityDivisionDeterminationFaultException

│ │ ├ SecurityIdentityDeterminationFaultException

│ │ ├ SecurityIPLockedFaultException

│ │ ├ SecurityPrimaryStationMismatchException

│ │ ├ SecurityProductionMismatchException

│ │ ├ SecurityTooManyInvalidLoginAttemptsFaultException

│ │ ├ SecurityUserAuthorizationException

│ │ └ SecurityUserVerifyCodeException

│ │

│ └ VistaSocketException

│ │

│ ├ VistaLinkSocketAlreadyClosedException

│ └ VistaSocketTimeOutException

│

├ VistaLinkResourceException (extends

│ │ javax.resource.ResourceException)

│ ├ ConnectionHandlesExceededException

│ ├ HeartBeatFailedException

│ │ └ HeartBeatInitializationFailedException

│ └ VistaLinkSocketClosedException

│

└ VistaLoginModuleException (extends

│ javax.security.auth.login.LoginException)

├ VistaLoginModuleIPLockedException

├ VistaLoginModuleLoginsDisabledException

├ VistaLoginModuleNoJobSlotsAvailableException

├ VistaLoginModuleNoPathToListenerException

├ VistaLoginModuleTooManyInvalidAttemptsException

├ VistaLoginModuleUserCancelledException

└ VistaLoginModuleUserTimedOutException

<span id="_Ref230542163" class="anchor"></span>Figure 5‑1. VistALink Exception Hierarchy

### VistaLinkResourceException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

J2EE Connectors requires adapter methods to throw javax.resource.ResourceException.

VistALink implements gov.va.med.vistalink.adapter.cci.VistaLinkResourceException that extends javax.resource.ResourceException. VistaLinkResourceException is thrown from all J2EE Connectors required methods as well as any custom method in VistALink that implements connection management interfaces.

VistaLinkResourceException more specific exception subclasses include (see [Figure 5‑1. VistALink Exception Hierarchy](#_VistALink_Exception_Hierarchy)):

- ConnectionHandlesExceededException
- VistaLinkSocketClosedException
- HeartBeatFailedException
- HeartBeatInteractionFailedException.

### FoundationsException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The J2EE Connector Architecture specification defines optional record and interaction management interfaces that are not implemented in VistALink. Instead, VistALink uses VistaLinkConnection::executeRPC(), VistaLinkConnection::executeInteration() and classes in gov.va.med.vistalink.adapter.record package to implement interaction and record management. These methods are not governed by the J2EE Connector Architecture specification. Hence VistALink uses gov.va.med.exception.FoundationsException and its subclasses in these methods.

### VistaLinkFaultException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink communications with M can produce exceptions that originate from the Java code side. In that case, VistaLinkResourceException and FoundationsException will be thrown (described above).

VistALink communications with M can also produce exceptions that originate from the M side. In those cases a Fault message is sent back to VistALink from M. Fault messages are parsed and gov.va.med.vistalink.adapter.record.VistaLinkFaultException that extends FoundationsException are constructed to be thrown in those cases.

VistaLinkFaultException will have all the information that is sent back from the M side to Java, including: faultCode, faultString, faultActor, errorCode, errorType and errorMessage.

VistaLinkFaultException more specific exception subclasses include (see Figure 5‑1. VistALink Exception Hierarchy):

- NoJobSlotsAvailableFaultException
- LoginsDisabledFaultException
- SecurityFaultException (contain more specific subclasses)
- RpcFaultException (contain more specific subclasses)

# Foundations Library Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Java APIs discussed in this chapter are the Foundations Library utilities. They are provided in vljFoundationsLib-1.6.1.x.jar.

## Encryption: gov.va.med.crypto

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistaKernelHash utility class implements a two-way hash via two static methods, encrypt and decrypt. These provide the encoding and obfuscation algorithms used by the RPC Broker and Kernel to encode and decode data strings.

Using these algorithms makes it harder to sniff the contents of text sent over the network. This is not, however, encryption-class encoding, nor does it protect against replay attacks of un-decoded strings. As a two-way hash, this algorithm should not be considered an implication or achievement of any particular security level beyond obfuscation.

Example (encoding):

String encodedString =

VistaKernelHash.encrypt("some text to encode", true);

The second parameter is useful if the text is to be passed in a CDATA section of an XML message. If this parameter is set to true, the returned encoded strings will contain neither "\]\]\>" nor "\<\![CDATA\[". Otherwise, it is possible a returned encoding may contain those character sequences. If, in a reasonable number of tries, an encoded string cannot be created without these CDATA boundaries, an exception is thrown of type VistaKernelHashCountLimitExceededException.

Example (decoding):

String decodedString =

VistaKernelHash.decrypt(encodedString);

## J2EE Environment: gov.va.med.environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Environment.isProduction()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returns whether or not the administrator has configured the J2EE server to be "production" in a VA-medical-center sense, i.e., the system is operating on production VA data. The source of the setting is the gov.va.med.environment.production JVM argument passed to the J2EE server upon startup. A setting of "true" designates the server as a production server; any other value (including not passing the JVM argument at all) marks the server as a non-VA production server.

Returns: true if the server is a VA production server, false if not.

### Environment.getServerType()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Returns the J2EE server type. The source of the setting is the gov.va.med.environment.servertype JVM argument passed to the J2EE server upon startup. If the JVM argument is not present, auto-detects for WebLogic only, and otherwise defaults to return UNKNOWN if auto-detection fails.

Returns: ServerType: JBOSS \| ORACLE \| SUN_RI_13 \| UNKNOWN \| WEBLOGIC \| WEBSPHERE \| TOMCAT \| J2SE

Example:

if (Environment.getServerType().equals(ServerType.WEBLOGIC)) {

// execute weblogic-specific code

}

## Network: gov.va.med.net

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following classes provide basic socket-based network functionality:

- SocketManager: Represents a socket that can be used to communicate with IP end points.
- VistaSocketException: Represents an exception thrown during read/write operations on a socket
- VistaSocketTimeOutException: Represents an exception identifying a timeout has occurred during read/write operations.

|                                                                                                                |                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/017.png) | REF: For more information on gov.va.med.net classes, see the Javadoc documentation provided in the VistALink distribution file. |

## Audit Timer: gov.va.med.monitor.time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink uses gov.va.med.monitor.time.AuditTimer to capture and log information on the length of execution for VistALink interactions using lo4j-logging capabilities. Special logger gov.va.med.vistalink.adapter.spi.VistaSocketConnection.AuditLog is used to output this information. Applications can use AuditTimer independently if they want to report timer information for various processing requests.

Two types of constructors can be used to construct the AuditTimer instance:

- For public AuditTimer(), default logger gov.va.med.monitor.time.AuditTimer is used.
- For public AuditTimer(Logger logger), an application-specific logger is used.

AuditTimer logs milliseconds elapsed between start() and stop() calls. The number of elapsed milliseconds can be retrieved using getTimeElapsedMillis().

Logging can be done using either log() method:

- public void log()
- public void log(String message): Since the logger can be passed into the constructor and the output pattern for a specific logger can be configured using the log4j configuration file, there should be no need to pass info message. Instead, different loggers should be used.

### Sample Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">import gov.va.med.monitor.time.AuditTimer;</span>

<span class="mark">publicclass AuditTimerTest {</span>

<span class="mark">privatestatic AuditTimer timer = null;</span>

<span class="mark">privatestatic Logger auditLogger = Logger.getLogger(AuditTimerTest.class.getName() + ".AuditLog");</span>

<span class="mark">publicstaticvoid main(String\[\] args) {</span>

<span class="mark"> // Initialize Log4j configuration</span>

<span class="mark"> DOMConfigurator.configureAndWatch("props/log4j2Config.xml",10000);</span>

<span class="mark"> timer = new AuditTimer(auditLogger);</span>

<span class="mark"> //</span> Start timer

<span class="mark"> timer.start();</span>

<span class="mark"> //</span> ... perform your operations

<span class="mark"> //</span> Stop timer

<span class="mark"> timer.stop();</span>

<span class="mark"> //</span> Log elapsed time information

<span class="mark"> timer.log();</span>

<span class="mark"> //</span> Get time elapsed if not for logging purposes

<span class="mark"> long timeElapsed = timer.getTimeElapsedMillis();</span>

<span class="mark">}</span>

<span class="mark">}</span>

The following is a snippet from the log4j configuration file:

\<Appenders\>

\<Console name="Console" target="SYSTEM_OUT"\>

\<PatternLayout pattern="%d{HH:mm:ss.SSS} \[%t\] %-5level %logger{36} - %msg%n"/\>

\</Console\>

\</Appenders\>

\<Logger name="<span class="mark">gov.va.med.vistalink.utilities.test.AuditTimerTest.AuditLog</span>" level="all" additivity="false"\>

\<AppenderRef ref="Console"/\>

\</Logger\>

## Exception: gov.va.med.exception

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ExceptionUtils Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/018.png) | NOTE: Use of this class (ExceptionUtils) has been deprecated, due to inclusion of nested exceptions in Java 1.4 and greater. |

All APIs in the gov.va.med.exception.ExceptionUtils class have been deprecated:

- String getFullStackTrace() method
- Throwable getNestedExceptionByClass() method

## XML: gov.va.med.xml 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### XmlUtilities Class

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/019.png) | NOTE: Use of this class (XmlUtilities) has been deprecated, due to the high level of XML support in Java 1.4 and greater. However, documentation has been left in place for reference. |

This class contains a number of static utility methods to help developers work with XML documents, nodes, attributes and strings. These utilities are XML-parser independent.

The tables below describe the VistALink utility methods and variables.

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 44%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Static Method Signature</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>String convertXmlToStr(Document doc)</td>
<td>Converts a DOM document to a string</td>
</tr>
<tr class="odd">
<td><p>Document getDocumentForXmlString(</p>
<p>String xml)</p></td>
<td>Returns an XML DOM Document for the specified String</td>
</tr>
<tr class="even">
<td><p>Document getDocumentForXmlInputStream(</p>
<p>InputStream xml)</p></td>
<td>Returns an XML DOM Document for the specified InputStream</td>
</tr>
<tr class="odd">
<td>Attr getAttr(Node node, String attrName)</td>
<td>Returns the Attribute with the given attrName at node</td>
</tr>
<tr class="even">
<td>Node getNode(String xpathStr, Node node)</td>
<td>Returns the first node at the specified XPath location<span id="_Toc193784594" class="anchor"></span></td>
</tr>
</tbody>
</table>

Table 6‑1. VistALink Utility Methods

|                            |                                                                                                                                                                                                                                            |
|----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Static Final Variables | Description                                                                                                                                                                                                                            |
| String XML_HEADER          | Represents the default header used for all xml documents that communicate with an M server via VistALink. It is important to use this header as this keeps the client and M server in sync.<span id="_Toc193784603" class="anchor"></span> |

Table 6‑2. VistALink Utility Variables

# How to Use VistALink in J2SE Applications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using VistALink to build J2SE client/M server applications is very similar to using VistALink in J2EE. The main differences are in the areas of authentication and obtaining a connection. Sample J2SE applications are provided in the VistALink distribution file, in the samples-J2SE folder.

## Authenticating and Connecting to VistA in Client-Server Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In J2EE, applications retrieve and return VistALink connections to a connection pool. In J2SE mode, however, VistALink establishes a direct, persistent connection on behalf of the J2SE application to the M server. Unless the server is shut down, this connection remains open until closed by the client.

The high-level steps to establish a VistALink connection to M in J2SE mode are:

1.  Provide server configuration information to VistALink (IP address and port of the M VistALink listener to connect to)
2.  Authenticate the end-user over the connection
3.  Execute RPCs
4.  Close the connection (log out)

VistALink uses the Java Authentication and Authorization Service (JAAS) framework for steps 1, 2 and 4 above.

|                                                                                                                |                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/020.png) | REF: For information on step 3, see the section "[Executing Requests](#executing-requests)." |

### JAAS Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Java Authentication and Authorization Service (JAAS) is a Java pluggable framework for user authentication and authorization. "Pluggability" means that different security modules (e.g., authentication modules) can be added or "plugged in" to an application without recompiling the application. VistALink uses the JAAS framework to authenticate end-users to an M/Kernel system, via the users' customary Kernel access and verify codes.

A JAAS-compliant login module contains all of the logic required to authenticate a user to a given system. The login module class does not itself, however, include the user interface to gather authentication credentials (e.g., access and verify codes) from the end-user. Instead, a set of JAAS-compliant callbacks, along with a JAAS-compliant callback handler, are used to de-couple the user interface from the login module. VistALink provides a JAAS-compatible login module and JAAS-compliant callbacks and callback handlers to perform a VistA login.

Although the JAAS framework also provides authorization capabilities, VistALink uses JAAS for authentication only. VistALink does not make any use of the permission/authorization portions of the JAAS specification at this time.

## VistALink JAAS Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistaLoginModule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink provides a single JAAS-compliant login module class, VistaLoginModule. As a developer, you do not use this class directly because your application does the following:

- Specifies which login module to use, via a JAAS configuration file
- Creates a LoginContext instance, and passes it a supported callback handler instance to collect user input
1.  Invokes the login method of the LoginContext class to initiate the login process for the configured login module

#### Section 508 Considerations

The VistaLoginModule UI has undergone section 508 testing and been approved. A button on the main login screen, "Section 508 Information", documents this.

The login module inherits color and font settings from the parent application. For that reason, we suggest that your code invoke the login module's login() method after first:

1.  Setting the Swing look-and-feel to the System look-and-feel classname, and
2.  Calling the Swing updateComponentTreeUI method

### JAAS Login Configuration Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, VistALink uses the default JAAS configuration reader to load login configurations. The default JAAS configuration reader class loads login configurations from a JAAS configuration file, which it expects to be in a predefined format.

One or more configuration entries are defined in the JAAS configuration file. The configuration file itself can have any name, and can be located anywhere. Each entry in the JAAS configuration file defines a particular login configuration. Generically, the format of this file is as follows:

ConfigurationName {  
ModuleClass Flag ModuleOptions;  
};

ConfigurationName {  
ModuleClass Flag ModuleOptions;  
};

### VistALink-Specific JAAS Login Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of the JAAS configuration file format needed specifically for VistALink:

<span class="mark">Test {</span>

<span class="mark">gov.va.med.vistalink.security.VistaLoginModule requisite</span>

<span class="mark">gov.va.med.vistalink.security.ServerAddressKey="10.21.1.185"</span>

<span class="mark">gov.va.med.vistalink.security.ServerPortKey="18000";</span>

<span class="mark">};</span>

<span class="mark">Production {</span>

<span class="mark">gov.va.med.vistalink.security.VistaLoginModule requisite</span>

<span class="mark">gov.va.med.vistalink.security.ServerAddressKey="10.21.1.85"</span>

<span class="mark">gov.va.med.vistalink.security.ServerPortKey="8000";</span>

<span class="mark">};</span>

This example defines two login configurations, one named "Test" and one named "Production." An application uses this name (Test or Production) as the index to retrieve a particular configuration from the JAAS configuration file.

To configure a VistALink login to a VistA system, configure a single login module per login configuration entry, within each entry's {braces}, as follows:

1.  Name the VistALink login module class, including package name:

gov.va.med.vistalink.security.vistalink.VistaLoginModule

2.  Follow with a flag indicating what action to take if login fails. For VistALink, use requisite.
3.  Follow with options for the VistALink login module. There are two options that must be set, in "name=value" format:

gov.va.med.vistalink.security.vistalink.ServerAddressKey

gov.va.med.vistalink.security.vistalink.ServerPortKey

Use quotes around the server address and server port values.

4.  Before the closing brace, end with a semicolon.
5.  Follow the closing brace with a semicolon.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-developer-guide/021.png)</td>
<td><p><strong>REF:</strong> For more information about the JAAS configuration file format expected by the default JAAS configuration file reader class, see:</p>
<p><a href="http://java.sun.com/j2se/1.4.1/docs/guide/security/jgss/tutorials/LoginConfigFile.html%20"><u>http://java.sun.com/j2se/1.4.1/docs/guide/security/jgss/tutorials/LoginConfigFile.html</u></a></p></td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/022.png) | NOTE: It is possible to define your own JAAS configuration reader class, instead of using the default class. If you do this, you are still responsible for providing the package/name of the VistaLoginModule class, the JAAS requisite flag, and the two options required by the VistaLoginModule. |

### Passing the JAAS Login Configuration(s) to Your JVM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The JAAS Login Configuration needs to be passed to the Java Virtual Machine (JVM) (and hence to your application). The JAAS configuration can be passed in two ways:

- With the javax.security.auth.login.Configuration Java virtual machine (JVM) argument when launching your application, e.g.:  
  >   
  > java -Djava.security.auth.login.config=jaas.config MyApp
- In the Java security properties file.

In most cases it is preferable to use the JVM argument, since it allows the setting to be application-specific rather than machine-wide.

### Selecting the JAAS Configuration From an Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once your application is running, it should select a specific configuration. In order to allow local administration of JAAS configuration files, you should, in most cases, provide a command-line parameter to allow local administrators to pass a particular JAAS configuration into your application. For example:

java -Djava.security.auth.login.config=jaas.conf MyApp Production

### Selecting a VistaLoginModule Callback Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to decouple the user interface for logon from the login module, the JAAS standard allows login modules such as VistaLoginModule to supply different callback handlers. VistALink supplies two callback handler classes, one for an interactive logon, and one for non-interactive unit testing:

- CallbackHandlerSwingCCOW: for production application use. Performs single-signon if credentials are already present in CCOW user context. Otherwise, collects access code, verify code, division and "change verify code" input via a set of Swing dialogs; stores single sign-on credentials in CCOW user context for subsequent application use.
- CallbackHandlerSwing: for production application use. Collects access code, verify code, division and "change verify code" input via a set of Swing dialogs.
- CallbackHandlerUnitTest: for unit testing only (not production use). Access code, verify code, division are passed as parameters to the class constructor, resulting in a "silent" login suitable for (non-interactive) unit testing. The "change verify code" functionality is not supported.

Your code will need to instantiate one of these callback handlers as part of the JAAS VistALink login. Your code will then need to pass the instantiated callback handler as a parameter to create a JAAS login context (see "[Putting the Pieces Together: VistALink JAAS Login](#_Putting_the_Pieces_Together: VistAL)," below.

### Benefits of Passing Parent Application Frame to Callback Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When constructing/instantiating a VistALink callback handler, one of the arguments is a reference to the (java.awt.)Frame of the parent application. We recommend that the calling application have created a Frame or descendant for itself prior to invoking login. Benefits to passing the calling application's defined Frame to the VistALink callback handler's constructor include:

- If, during a login to your application, the user temporarily grants focus to another application, and then returns (either by choosing the application in Alt-Tab, or by clicking the application icon in the taskbar), the application window and login dialog are made visible with the login on top, and the login dialog is granted focus.
- If the login dialog has focus but the app window is visible beneath it on the screen, and the user attempts to switch focus to the app window (from the login dialog), the login dialog flashes and keeps focus
- If the login dialog has focus and the user clicks on the application's taskbar icon, the login dialog keeps focus

If the parent application's Frame is not passed, focus issues do not work as above which is problematic given that the login is a modal dialog.

## Putting the Pieces Together: VistALink JAAS Login

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Logging in to VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example login. If application execution succeeds through the try block, the user has successfully logged in to the specified VistA listener.

<span class="mark">// variable holding LoginContext should have application scope</span>

<span class="mark">// since it will be needed to log out, later on</span>

<span class="mark">private LoginContext loginContext = null;</span>

<span class="mark">try {</span>

<span class="mark">// create the callback handler</span> to use to collect user input

<span class="mark">// pass current Frame as parameter</span>

<span class="mark">CallbackHandlerSwing cbhSwing = new CallbackHandlerSwing(myFrame);</span>

<span class="mark">// create the LoginContext</span> to control the login process;

// pass the JAAS configuration to connect to, and the callback

// handler (jaasConfigName value could be passed in from command

// line)

<span class="mark">loginContext = new LoginContext(jaasConfigName, cbhSwing);</span>

<span class="mark">// login to server</span> through the LoginContext

<span class="mark">loginContext.login();</span>

<span class="mark">} catch (VistaLoginModuleException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(), "Login error",</span>

<span class="mark">JOptionPane.ERROR_MESSAGE);</span>

<span class="mark">} catch (LoginException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(), "Login error",</span>

<span class="mark">JOptionPane.ERROR_MESSAGE);</span>

}

## After Successfully Logging In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Retrieving the VistaKernelPrincipal

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The JAAS subject is available from the JAAS LoginContext class after a successful login.

It contains a JAAS principal (user entity), which holds:

- Demographic information about the logged-in user
- The authenticated VistALink connection object

The following code shows how to retrieve the Kernel principal after a successful login:

<span class="mark">// variable holding Kernel principal may need application scope</span>

<span class="mark">// since it will be needed for RPC execution</span>

<span class="mark">private VistaKernelPrincipalImpl userPrincipal = null;</span>

// . . . login code

<span class="mark">// get the Kernel principal</span> after logon

try {

<span class="mark">userPrincipal = VistaKernelPrincipalImpl.getKernelPrincipal(</span>

<span class="mark">loginContext.getSubject());</span>

<span class="mark">} catch (FoundationsException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(), "Login error",</span>

<span class="mark">JOptionPane.ERROR_MESSAGE);</span>

<span class="mark">}</span>

In the future, it is conceivable that *more than one principal* could be contained in the JAAS subject after login, if multiple login modules are used. This might happen when a compound login has been configured, requiring several logins to complete, e.g., one for a Kernel M system and one for a separate health data repository.

Only one \*Kernel\* principal should ever be returned, however. Use the getKernelPrincipal helper method in the VistaKernelPrincipalImpl class to retrieve the single Kernel principal.

### Retrieving the Authenticated Connection From the Principal 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To execute RPCs, you need to retrieve the authenticated connection. The authenticated connection object over which you make requests is stored in the Kernel principal, and can be retrieved with the getAuthenticatedConnection method.

Once a successful login has been completed, you should retrieve the associated authenticated connection from the Kernel principal. This connection is "logged in" to the M system under the end-user's identity. You can then use it to execute requests such as RPCs on behalf of the end-user.

|                                                                                                                |                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/023.png) | REF: For more information on executing requests, see the chapter of this manual titled "Executing Requests." An example of successful login appears below. |

VistaLinkConnection myConnection =

userPrincipal.getAuthenticatedConnection();

// . . . now you can execute requests

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/024.png) | REF: For information on how to use the VistaLinkConnection object to execute requests, see the section "[Executing RPCs](#executing-rpcs)," below. |

### Retrieving User Demographic Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following predefined static KEY\* strings to retrieve user demographic values via the Kernel principal's getUserDemographicValue method. For example:

// get the DUZ

String duz = this.userPrincipal.getUserDemographicValue(

VistaKernelPrincipalImpl.KEY_DUZ);

// get the name

String name = userPrincipal.getUserDemographicValue(

VistaKernelPrincipalImpl.KEY_NAME_DISPLAY);

The table below shows a complete set of returned demographics information and keys.

| Key                     | Value                     |
|-----------------------------|-------------------------------|
| KEY_DIVISION_IEN            | Login division station IEN    |
| KEY_DIVISION_STATION_NAME   | Login division station name   |
| KEY_DIVISION_STATION_NUMBER | Login division station number |
| KEY_DTIME                   | User timeout value            |
| KEY_DUZ                     | DUZ                           |
| KEY_LANGUAGE                | User language                 |
| KEY_NAME_DEGREE             | User degree                   |
| KEY_NAME_FAMILYLAST         | Name component family-last    |
| KEY_NAME_GIVENFIRST         | Name component given-first    |
| KEY_NAME_MIDDLE             | Name component middle         |
| KEY_NAME_NEWPERSON01        | New Person .01 Field name     |
| KEY_NAME_PREFIX             | Name component prefix         |
| KEY_NAME_SUFFIX             | Name component suffix         |
| KEY_SERVICE_SECTION         | User service/section          |
| KEY_NAME_DISPLAY            | Concatenated standard name    |
| KEY_TITLE                   | User title                    |

<span id="_Toc135039349" class="anchor"></span>Table 7‑1. Demographics Keys and Values

### Executing RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have a VistaLinkConnection connection object to work with, you can execute requests in exactly the same fashion as for VistALink's J2EE mode.

|                                                                                                                |                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/025.png) | REF: For more information, see chapter 4 of this document, "[Executing Requests](#executing-requests)." The entire chapter is valid for J2SE mode. |

### Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information on timeouts for RPC execution, see the "Timeouts" section of this document titled "Using VistALink in J2EE." Most of the information there on timeouts is also valid for the J2SE mode.

There is one significant difference to be aware of when a timeout occurs for a J2SE VistALink connection, however. Once a timeout occurs, the single authenticated connection to the M system is now rendered unusable. In order to perform any more actions on the M system, the client application will need to re-invoke the entire login process, in order to log in the end user again and get to the point where a validated, authenticated connection is once again available over which to execute RPC requests.

As such, for client/server applications, it is best to set the longest timeout value that can be tolerated within the context of the RPC itself as well as the specific end-user functionality being executed.

### Logging Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your application should *always* call the logout method of the JAAS LoginContext class to log out of VistA before exiting. This ensures that proper Kernel cleanup (e.g., of the ^TMP global) occurs on the M server to which the user was connected.

#### Logging Out of Swing Applications

In a Swing application, the application should always call the LoginContext's logout method when the application is shut down. There are a number of ways an application can be shut down: The user closes the application window, the application is terminated from the Windows control panel, etc.

A good way to catch all of these shutdown cases is to implement a WindowAdapter as a window listener in the application, and provide an implementation of its windowClosing method that calls the LoginContext's logout method.

For example:

<span class="mark">// loginContext has been defined earlier, with application scope</span>

<span class="mark">// add event listener to log out when window closes</span>

<span class="mark">frame.addWindowListener(new WindowAdapter() {</span>

<span class="mark">public void windowClosing(WindowEvent e) {</span>

<span class="mark">mylogout();</span>

<span class="mark">System.exit(0);</span>

<span class="mark">}</span>

<span class="mark">});</span>

<span class="mark">// Method called from event handler to perform logout</span>

<span class="mark">private void mylogout() {</span>

<span class="mark">// Kernel logout</span>

<span class="mark">if (this.userPrincipal != null) {</span>

<span class="mark">try {</span>

<span class="mark">loginContext.logout();</span>

<span class="mark">} catch (LoginException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(),</span>

<span class="mark">"Logout error", JOptionPane.ERROR_MESSAGE);</span>

<span class="mark">}</span>

<span class="mark">}</span>

}

## Catching Login Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LoginContext login() and logout() methods only throw exceptions that derive from LoginException. So at a minimum, when executing the login or logout methods of a LoginContext object, your application needs a try/catch block to catch LoginException.

### VistaLoginModule Exception Hierarchy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

JAAS requires LoginModules to throw javax.security.auth.login.LoginException from JAAS classes implementation methods. So the VistALink login module throws exceptions of type gov.va.med.vistalink.security.vistalink.VistaLoginModuleException, which extends javax.security.auth.login.LoginException.

The VistaLink login module provides more granular exceptions from VistaLoginModuleException, so that your application can optionally filter exceptions at a finer level of granularity. This means that your application can detect and implement specific processing for login exception types that might be of interest.

| Exception                                   | Description                                                                                        |
|-------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| VistaLoginModuleException                       | Like a LoginException, but may contain nested exception(s) that were the cause for the LoginException. |
| VistaLoginModuleLoginsDisabledException         | Logins are disabled on the M server.                                                                   |
| VistaLoginModuleNoJobSlotsAvailableException    | Job slot maximum has been exceeded on M server.                                                        |
| VistaLoginModuleNoPathToListenerException       | No reachable listener was found on the path represented by the specified IP address and Port.          |
| VistaLoginModuleTooManyInvalidAttemptsException | The user tried to login too many times with invalid credentials.                                       |
| VistaLoginModuleUserCancelledException          | The user cancelled the login.                                                                          |
| VistaLoginModuleUserTimedOutException           | The user timed out of the login.                                                                       |

<span id="_Toc280220372" class="anchor"></span>Table 7‑2. VistALink Login Exceptions

For example, if your application is interested in whether the IP and port specified were "bad" (at least at the time the login was attempted), you can trap for the VistaLoginModuleNoPathToListener exception, in addition to the standard LoginException. Example:

<span class="mark">try {</span>

<span class="mark">// create the callback handler to use to collect user input</span>

<span class="mark">CallbackHandlerSwing cbhSwing = new CallbackHandlerSwing(myFrame);</span>

<span class="mark">// create the LoginContext to control the login process.</span>

<span class="mark">loginContext = new LoginContext(serverAlias, cbhSwing);</span>

<span class="mark">// login to server through the LoginContext</span>

<span class="mark">loginContext.login();</span>

<span class="mark">} catch (VistaLoginModuleLoginsDisabledException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(</span>

<span class="mark">null,</span>

<span class="mark">"Logins are disabled; try later.",</span>

<span class="mark">"Login error",</span>

<span class="mark">JOptionPane.ERROR_MESSAGE);</span>

<span class="mark">} catch (LoginException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(), "Login error",</span>

<span class="mark">JOptionPane.ERROR_MESSAGE);</span>

}

## CCOW Login Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink's client/server logins support Clinical Context Object Workgroup (CCOW)-based single sign-on, based on the work in the Single Sign-On/User Context (SSO/UC) Project. For more information on CCOW-enabling the logins of client/server applications, please the documentation for the SSO/UC project (available on the VDL).

## Unit Testing and VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The login user interface collects end-user information, including the access and verify code and division number. It is separate from the logic that implements login, because of the pluggable JAAS architecture. The user interface is contained in a JAAS-compliant set of callbacks, and the login logic is contained in a JAAS-compliant login module. Therefore, the JAAS framework makes it straightforward to implement alternative user interfaces for login.

VistALink provides an alternative callback handler that implements a "silent" (non-interactive) login suitable for unit testing purposes. This silent login is not suitable for any production environment. Your application passes the access and verify code, and (optionally) division to silently log in your application. Changing the verify code is not supported with this callback handler.

For example:

// Connection info

String cfgName = "Production";

// signon credentials for unit test callback handler

String accessCode = "asdf.123";

String verifyCode = "asdf.456";

String division = "";

<span class="mark">try {</span>

// create the "unit test" callbackhandler for JAAS login

CallbackHandlerUnitTest cbhUnitTest =new CallbackHandlerUnitTest(accessCode, verifyCode, division);

// create the JAAS LoginContext for login

lc = new LoginContext(cfgName, cbhUnitTest);

// login to server

lc.login();

<span class="mark">}</span> catch <span class="mark">(VistaLoginModuleException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(), "Login error",</span>

<span class="mark">JOptionPane.ERROR_MESSAGE);</span>

<span class="mark">} catch (LoginException e) {</span>

<span class="mark">JOptionPane.showMessageDialog(null, e.getMessage(), "Login error", JOptionPane.ERROR_MESSAGE);</span>

<span class="mark">}</span>

## Appendix A: Pluggable Institution Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/026.png) | NOTE: This section is of interest primarily to non-VA users of VistALink. |

J2EE Applications using VistALink need the ability to select the resource adapter (connector) to execute a remote procedure call (RPC) on a given M system. To retrieve the appropriate VistALink adapter, the application needs to know what JNDI name the adapter they're interested in is registered under.

VistALink's institution mapping provides a way for J2EE applications to obtain the JNDI name of a VistALink adapter based on station number (the institution, station, and division number are the pieces of information an application is likely to have to identify an M system it wants to connect to.)

With VistALink's institution mapping, J2EE applications should not have to hard-code connector JNDI names; in most cases they should get the appropriate connector using a station number.

The VA-specific implementation of institution mapping rules (gov.va.med.vistalink.institution.PrimaryStationRulesVHA) makes several VA-specific assumptions, in particular:

- Legal station numbers in VA can be 3 digits or 5+ digits with one exception (see nursing homes below).
- For station numbers assigned to the Austin Information Technology Center (AITC) only: If a station number has an alpha suffix, e.g. "200A", the numeric portion must be "200"
- For nursing homes: If a numeric station number is 4 digits, the 4th digit must be a "9"

To replace these rules with a different rule implementation, you can provide a new implementation of the rules interface (gov.va.med.vistalink.institution.IPrimaryStationRules). To do that:

- A new implementation of the IPrimaryStationRules interface must be provided, and
- The package/classname of the new implementation must be passed in a -D JVM argument, "gov.va.med.vistalink.primary-station-rules-class". E.g., -Dgov.va.med.vistalink.primary-station-rules-class=org.test.PrimaryStationRulesTest

For an example of an implementation of institution mapping rules, you can examine the source code for the PrimaryStationRulesVHA class. Also, documentation for the interface is provided in the javadoc distributed with VistALink.

|                                                                                                                |                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-developer-guide/027.png) | REF: For more information on activating a non-VA-specific institution rules class, see the *System Management Guide*. |

This page is left blank intentionally.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>AAC</th>
<th>Formerly the Austin Automation Center. Renamed to the Austin Information Technology Center (AITC)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Access Code</td>
<td>A password used by the Kernel system to identify the user. It is used with the verify code.</td>
</tr>
<tr class="even">
<td>Adapter</td>
<td>Another term for <em>resource adapter</em> or <em>connector.</em></td>
</tr>
<tr class="odd">
<td>Administration Server</td>
<td>Each WebLogic server domain must have one server instance that acts as the administration server. This server is used to configure all other server instances in the domain.</td>
</tr>
<tr class="even">
<td>AITC</td>
<td><em>Austin Information Technology Center</em></td>
</tr>
<tr class="odd">
<td>Alias</td>
<td>An alternative filename.</td>
</tr>
<tr class="even">
<td>Alpha/VMS</td>
<td><p>Alpha: Hewlett Packard computer system</p>
<p>VMS: <em>Virtual Memory System</em></p></td>
</tr>
<tr class="odd">
<td>Anonymous Software Directories</td>
<td>M directories where VHA application and patch zip files are placed for distribution.</td>
</tr>
<tr class="even">
<td>API</td>
<td><em>Application Program Interface</em></td>
</tr>
<tr class="odd">
<td>Application Proxy User</td>
<td>A Kernel user account designed for use by an application rather than an end-user.</td>
</tr>
<tr class="even">
<td>Application Server</td>
<td>Software/hardware for handling complex interactions between users, business logic, and databases in transaction-based, multi-tier applications. Application servers, also known as app servers, provide increased availability and higher performance.</td>
</tr>
<tr class="odd">
<td>ASTM</td>
<td><em>American Society for Testing and Materials</em></td>
</tr>
<tr class="even">
<td>Authentication</td>
<td>Verifying the identity of the end-user.</td>
</tr>
<tr class="odd">
<td>Authorization</td>
<td>Granting or denying user access or permission to perform a function.</td>
</tr>
<tr class="even">
<td>Base Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a standalone adapter that is completely set up. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters). The deployer only needs to modify a subset of the linked adapters' deployment descriptor settings.</td>
</tr>
<tr class="odd">
<td>BEA WebLogic</td>
<td>BEA WebLogic is a J2EE Platform application server. Oracle has acquired BEA Systems, Inc. From here forward it will be referred to as Oracle.</td>
</tr>
<tr class="even">
<td>Caché</td>
<td>Caché is an M environment, a product of InterSystems Corp.</td>
</tr>
<tr class="odd">
<td>Cache/VMS</td>
<td><p>Cache: InterSystems Caché object database that runs SQL</p>
<p>VMS: <em>Virtual Memory System</em></p></td>
</tr>
<tr class="even">
<td>CCI</td>
<td>Common Client Interface</td>
</tr>
<tr class="odd">
<td>CCOW</td>
<td>A standard defining the use of a technique called "context management," providing the clinician with a unified view on information held in separate and disparate healthcare applications that refer to the same patient, encounter or user. </td>
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
<td>A cached store of connection objects that can be available on demand and reused, increasing performance and scalability. VistALink 1.6 uses connection pooling.</td>
</tr>
<tr class="even">
<td>Connector</td>
<td>A system-level driver that integrates J2EE application servers with Enterprise Information Systems (EIS). VistALink is a J2EE connector module designed to connect to Java applications with VistA/M systems. The term is used interchangeably with <em>connector module</em>, adapter, <em>adapter module</em>, and <em>resource adapter</em>.</td>
</tr>
<tr class="odd">
<td>Connector Proxy User</td>
<td>For security purposes, each instance of a J2EE connector must be granted access to the M server it connects to. This is done via a Kernel user account set up on the M system. This provides initial authentication for the app server and establishes a trusted connection. The M system manager must set up the connector user account and communicate the access code, verify code and listener IP address and port to the J2EE system manager.</td>
</tr>
<tr class="even">
<td>COTS</td>
<td><em>Commercial, Off-The-Shelf</em></td>
</tr>
<tr class="odd">
<td>CSV</td>
<td><em>Comma-Separated Values</em> format</td>
</tr>
<tr class="even">
<td>DBF</td>
<td>Database file format underlying many database applications (originally dBase)</td>
</tr>
<tr class="odd">
<td>DCL</td>
<td><em>Digital Command Language</em>. An interactive command and scripting language for VMS.</td>
</tr>
<tr class="even">
<td>Division</td>
<td>VHA sites are also called <em>institutions</em>. Each institution has a <em>station number</em> associated with it. Occasionally a single institution is made up of multiple sites, known as <em>divisions</em>. To make a connection, VistALink needs a station number from the end-user's New Person entry in the Kernel Site Parameters file. It looks first for a division station number and if it can't find one, uses the station number associated with default institution.</td>
</tr>
<tr class="odd">
<td>DSM</td>
<td><em>Digital Standard MUMPS.</em> An M environment, a product of InterSystems Corp.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td>A local variable holding a number that identifies the signed-on user. The number is the Internal Entry Number (IEN) of the user's record in the NEW PERSON file (file #200)</td>
</tr>
<tr class="odd">
<td>EAR file</td>
<td><em>Enterprise archive</em> file. An enterprise application archive file that contains a J2EE application.</td>
</tr>
<tr class="even">
<td>EIS</td>
<td><em>Enterprise Information System</em></td>
</tr>
<tr class="odd">
<td>EPHI</td>
<td><em>Electronic Protected Health Information</em></td>
</tr>
<tr class="even">
<td>FatKAAT</td>
<td><em>Fat-Client (i.e. Rich client) Kernel Authentication and Authorization</em></td>
</tr>
<tr class="odd">
<td>FDA</td>
<td><em>FileMan Data Array</em></td>
</tr>
<tr class="even">
<td>File #18</td>
<td>System file #18 was the precursor to the KERNEL SYSTEMS PARAMETERS file, and is now obsolete. It uses the same number space that is now assigned to VistALink. Therefore, file #18 must be deleted before VistALink can be installed.</td>
</tr>
<tr class="odd">
<td>Global</td>
<td>A multi-dimensional data storage structure -- the mechanism for persistent data storage in a MUMPS database.</td>
</tr>
<tr class="even">
<td>Health<em><strong><u>e</u></strong></em>Vet-VistA</td>
<td>The VHA is converting its MUMPS-based VistA healthcare system to a new J2EE-based platform and application suite. The new system is known as Health<em><strong><u>e</u></strong></em>Vet-VistA.</td>
</tr>
<tr class="odd">
<td>HIPAA</td>
<td><em>Health Insurance Portability and Accountability Act</em></td>
</tr>
<tr class="even">
<td>IDE</td>
<td><em>Integrated development environment.</em> A suite of software tools to support writing software.</td>
</tr>
<tr class="odd">
<td>Institution</td>
<td>VHA sites are also called <em>institutions</em>. Each institution has a <em>station number</em> associated with it. Occasionally a single institution is made up of multiple sites, known as <em>divisions</em>. To make a connection, VistALink needs a station number from the end-user's New Person entry in the KERNEL SYSTEM PARAMETERS file (#8989.3). It looks first for a division station number and if it can't find one, uses the station number associated with default institution.</td>
</tr>
<tr class="even">
<td>Institution Mapping</td>
<td>The VistALink 1.6 release includes a small utility that administrators can use to associate station numbers with JNDI names, and which allows runtime code to retrieve the a VistALink connection factory based on station number.</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td><em>Information Security Officer</em></td>
</tr>
<tr class="even">
<td>J2CA</td>
<td><em>J2EE Connector Architecture</em>. J2CA is a framework for integrating J2EE-compliant application servers with Enterprise Information Systems, such as the VHA's VistA/M systems. It is the framework for J2EE connector modules that plug into J2EE application servers, such as the VistALink adapter.</td>
</tr>
<tr class="odd">
<td>J2EE</td>
<td>The <em>Java 2 Platform, Enterprise Edition (J2EE)</em> is an environment for developing and deploying enterprise applications. The J2EE platform consists of a set of services, APIs, and protocols that provide the functionality for developing multi-tiered, Web-based applications. A J2EE Connector Architecture specification for building adapters to connect J2EE systems to non-J2EE enterprise information systems.</td>
</tr>
<tr class="even">
<td>JAAS</td>
<td><em>Java Authentication and Authorization Service.</em> JAAS is a pluggable Java framework for user authentication and authorization, enabling services to authenticate and enforce access controls upon users.</td>
</tr>
<tr class="odd">
<td>JAR file</td>
<td><em>Java archive</em> file. It is a file format based on the ZIP file format, used to aggregate many files into one.</td>
</tr>
<tr class="even">
<td>Java Library</td>
<td>A library of Java classes usually distributed in JAR format.</td>
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
<td><em>J2EE Connector Architecture Common Client Interface</em></td>
</tr>
<tr class="even">
<td>JDK</td>
<td><em>Java Development Kit</em>. A set of programming tools for developing Java applications.</td>
</tr>
<tr class="odd">
<td>JMX</td>
<td><em>Java Management eXtensions</em>. A java specification for building manageability into java applications, including J2EE-based ones.</td>
</tr>
<tr class="even">
<td>JNDI</td>
<td><em>Java Naming and Directory Interface</em>. A protocol to a set of APIs for multiple naming and directory services.</td>
</tr>
<tr class="odd">
<td>JRE</td>
<td>The <em>Java Runtime Environment</em> consists of the Java virtual machine, the Java platform core classes, and supporting files. JRE is bundled with the JDK but also available packaged separately.</td>
</tr>
<tr class="even">
<td>JSP</td>
<td><em>Java Server Pages</em>. A language for building web interfaces for interacting with web applications.</td>
</tr>
<tr class="odd">
<td>JVM</td>
<td><em>Java Virtual Machine.</em> The JVM interprets compiled Java binary code (byte code) for specific computer hardware.</td>
</tr>
<tr class="even">
<td>KAAJEE</td>
<td><em>Kernel Authentication and Authorization for Java 2 Enterprise Edition</em></td>
</tr>
<tr class="odd">
<td>Kernel</td>
<td>Kernel functions as an intermediary between the host M operating system and VistA M applications. It consists of a standard user and program interface and a set of utilities for performing basic VA computer system tasks, e.g., Menu Manager, Task Manager, Device Handler, and security.</td>
</tr>
<tr class="even">
<td>KIDS</td>
<td><em>Kernel Installation and Distribution System</em>. The VistA/M module for exporting new VistA software packages.</td>
</tr>
<tr class="odd">
<td>LDAP</td>
<td>Acronym for <em>Lightweight Directory Access Protocol.</em> LDAP is an open protocol that permits applications running on various platforms to access information from directories hosted by any type of server.</td>
</tr>
<tr class="even">
<td>Linked Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a standalone adapter that is completely set up. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters). The deployer only needs to modify a subset of linked adapters' deployment descriptor settings.</td>
</tr>
<tr class="odd">
<td>Linux</td>
<td>An <a href="http://www.webopedia.com/TERM/L/open_source.html">open-source</a> <a href="http://www.webopedia.com/TERM/L/operating_system.html">operating system</a> that runs on various types of hardware <a href="http://www.webopedia.com/TERM/L/platform.html">platforms</a>. Health<em><strong><u>e</u></strong></em>Vet-VistA servers use both Linux and Windows operating systems.</td>
</tr>
<tr class="even">
<td>Listener</td>
<td>A socket routine that runs continuously at a specified port to field incoming requests. It sends requests to a front controller for processing. The controller returns its response to the client through the same port. The listener creates a separate thread for each request, so it can accept and forward requests from multiple clients concurrently.</td>
</tr>
<tr class="odd">
<td>log4J Utility</td>
<td>An open-source logging package distributed under the Apache Software license. Reviewing log files produced at runtime can be helpful in debugging and troubleshooting.</td>
</tr>
<tr class="even">
<td>logger</td>
<td>In log4j, a logger is a named entry in a hierarchy of loggers. The names in the hierarchy typically follow Java package naming conventions. Application code can select a particular logger by name to write output to, and administrators can configure where a particular named logger's output is sent.</td>
</tr>
<tr class="odd">
<td>M (MUMPS)</td>
<td><em>Massachusetts General Hospital Utility Multi-programming System</em>, abbreviated M. M is a high-level procedural programming computer language, especially helpful for manipulating textual data.</td>
</tr>
<tr class="even">
<td>Managed Server</td>
<td>A server instance in a WebLogic domain that is not an administration server, i.e., not used to configure all other server instances in the domain.</td>
</tr>
<tr class="odd">
<td>MBeans</td>
<td>In the Java programming language, an MBean (managed bean) is a Java object that represents a manageable resource, such as an application, a service, a component, or a device. MBeans must be concrete Java classes.</td>
</tr>
<tr class="even">
<td>Messaging</td>
<td>A framework for one application to asynchronously deliver data to another application, typically using a queuing mechanism.</td>
</tr>
<tr class="odd">
<td>Multiple</td>
<td>A VA FileMan data type that allows more than one value for a single entry.</td>
</tr>
<tr class="even">
<td>Namespace</td>
<td>A unique 2-4 character prefix for each VistA package. The DBA assigns this character string for developers to use in naming a package's routines, options, and other elements. The namespace includes a <em>number space</em>, a pre-defined range of numbers that package files must stay within.</td>
</tr>
<tr class="odd">
<td>New Person File</td>
<td>The New Person file contains information for all valid users on an M system.</td>
</tr>
<tr class="even">
<td>NIST</td>
<td><em>National Institute for Standards and Technology</em></td>
</tr>
<tr class="odd">
<td>OI</td>
<td><em>Office of Information</em></td>
</tr>
<tr class="even">
<td>Oracle WebLogic</td>
<td>Oracle WebLogic is a J2EE Platform application server. Oracle has acquired BEA Systems, Inc.</td>
</tr>
<tr class="odd">
<td>OS</td>
<td><em>Operating System</em></td>
</tr>
<tr class="even">
<td>Patch</td>
<td>An update to a VistA software package that contains an enhancement or bug fix. Patches can include code updates, documentation updates, and information updates. Patches are applied to the programs on M systems by IRM services.</td>
</tr>
<tr class="odd">
<td>PHI</td>
<td><em>Protected Health Information</em></td>
</tr>
<tr class="even">
<td>Plug-in</td>
<td>A component that can interact with or be added to an application without recompiling the application.</td>
</tr>
<tr class="odd">
<td>ra.xml</td>
<td>ra.xml is the standard J2EE deployment descriptor for J2CA connectors. It describes connector-related attributes and its deployment properties using a standard DTD (Document Type Definition) from Sun.</td>
</tr>
<tr class="even">
<td>Re-authentication</td>
<td>When using a J2CA connector, the process of switching the security context of the connector from the original application connector "user" to the actual end-user<em>.</em> This is done by the calling application supplying a proper set of user credentials.</td>
</tr>
<tr class="odd">
<td>Resource Adapter</td>
<td>J2EE resource adapter modules are system-level drivers that integrate J2EE application servers with Enterprise Information Systems (EIS). This term is used interchangeably with <em>resource adapter</em> and <em>connector</em>.</td>
</tr>
<tr class="even">
<td>RM</td>
<td><em>Requirements Management</em></td>
</tr>
<tr class="odd">
<td>Routine</td>
<td>A program or sequence of computer instructions that may have some general or frequent use. M routines are groups of program lines that are saved, loaded, and called as a single unit with a specific name.</td>
</tr>
<tr class="even">
<td>RPC</td>
<td><em>Remote Procedure Call</em>. A defined call to M code that runs on an M server. A client application, through the RPC Broker, can make a call to the M server and execute an RPC on the M server. Through this mechanism a client application can send data to an M server, execute code on an M server, or retrieve data from an M server</td>
</tr>
<tr class="odd">
<td>RPC Broker</td>
<td>The RPC Broker is a client/server system within VistA. It establishes a common and consistent framework for client-server applications to communicate and exchange data with VistA/M servers.</td>
</tr>
<tr class="even">
<td>RPC Security</td>
<td>All RPCs are secured with an RPC context (a "B"-type option). An end-user executing an RPC must have the "B"-type option associated with the RPC in the user's menu tree. Otherwise an exception is thrown.</td>
</tr>
<tr class="odd">
<td>SAD</td>
<td><em>Software Architecture Document</em></td>
</tr>
<tr class="even">
<td>SE&amp;I</td>
<td><em>Software Engineering &amp; Integration</em></td>
</tr>
<tr class="odd">
<td>Servlet</td>
<td>A Java program that resides on a server and executes requests from client web pages.</td>
</tr>
<tr class="even">
<td>Socket</td>
<td>An operating system object that connects application requests to network protocols.</td>
</tr>
<tr class="odd">
<td>SPI</td>
<td><em>J2CA service provider interface</em> Service-Level Contract</td>
</tr>
<tr class="even">
<td>SRS</td>
<td><em>Software Requirements Specification</em></td>
</tr>
<tr class="odd">
<td>SSH</td>
<td><a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>Secure Shell or SSH is a network protocol that allows data to be exchanged using a secure channel between two networked devices. Used primarily on Linux and Unix based systems to access shell accounts, SSH was designed as a replacement for Telnet and other insecure remote shells, which send information, notably passwords, in plaintext, leaving them open for interception. The encryption used by SSH provides confidentiality and integrity of data over an insecure network, such as the Internet.</td>
</tr>
<tr class="even">
<td>TCP/IP</td>
<td><em>Transmission Control Protocol (TCP) and the Internet Protocol (IP)</em></td>
</tr>
<tr class="odd">
<td>Term</td>
<td>Definition</td>
</tr>
<tr class="even">
<td>TXT</td>
<td><em>Text</em> file format</td>
</tr>
<tr class="odd">
<td>UML</td>
<td><em>Unified Modeling Language</em> is a standardized specification language for object modeling.</td>
</tr>
<tr class="even">
<td>VA</td>
<td><em>Department of Veterans Affairs</em></td>
</tr>
<tr class="odd">
<td>VACO</td>
<td><em>Veterans Affairs Central Office</em></td>
</tr>
<tr class="even">
<td>Verify Code</td>
<td>A password used in tandem with the access code to provide secure user access. The Kernel's Sign-on/Security system uses the verify code to validate the user's identity.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><em>Veterans Health Information Systems and Technology Architecture</em>. The VHA's portfolio of M-based application software used by all VA medical centers and associated facilities.</td>
</tr>
<tr class="even">
<td>VistALink Libraries</td>
<td>Classes written specifically for VistALink.</td>
</tr>
<tr class="odd">
<td>VL</td>
<td><em>VistaLink</em> is a runtime and development tool providing connection and data conversion between Java and M applications in client-server and n-tier architectures, to which this document describes the architecture and design.</td>
</tr>
<tr class="even">
<td>VMS</td>
<td><em>Virtual Memory System</em>. An operating system, originally designed by DEC (now owned by Hewlett-Packard), that operates on the VAX and Alpha architectures.</td>
</tr>
<tr class="odd">
<td>VPID</td>
<td><em>VA Person Identifier</em>. A new enterprise-level identifier uniquely identifying VA 'persons' across the entire VA domain.</td>
</tr>
<tr class="even">
<td>WAR file</td>
<td><em>Web archive</em> file. Contains the class files for servlets and JSPs.</td>
</tr>
<tr class="odd">
<td>WebLogic</td>
<td>WebLogic is a J2EE Platform application server.</td>
</tr>
<tr class="even">
<td>WebLogic Server</td>
<td>A J2EE application server manufactured by Oracle Systems.</td>
</tr>
<tr class="odd">
<td>WebSphere</td>
<td>WebSphere Application Server (WAS) is a J2EE application server manufactured by IBM Corp.</td>
</tr>
<tr class="even">
<td>XLS</td>
<td>Microsoft Office XL worksheet and workbook file format</td>
</tr>
<tr class="odd">
<td>XML</td>
<td><em>Extensible Markup Language</em></td>
</tr>
<tr class="even">
<td>XmlBeans</td>
<td>XMLBeans is a Java-to-XML binding framework which is part of the Apache Software Foundation XML project.</td>
</tr>
<tr class="odd">
<td>XOB Namespace</td>
<td>The VistALink namespace. All VistALink programs and their elements begin with the characters "XOB."</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>http://en.wikipedia.org/wiki/Secure_Shell<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-developer-guide/028.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the Security and Other Common Services Glossary Web page at the following Web address:</p>
<p>REDACTED<br />
<br />
For a comprehensive list of acronyms, please visit the Security and Other Common Services Acronyms Web site at the following Web address:</p>
<blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
</tbody>
</table>


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VistALink Version 1.5 Developer Guide

## Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink website (<http://vista.med.va.gov/migration/foundations/index.htm>) summarizes VistALink architecture and functionality and gives status updates for all VistALink products.

### VistALink 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Enterprise VistA Support (EVS) releases VistALink 1.5, the documentation set for VistALink will be available from the anonymous.software directory at download.vista.med.va.gov. It will include the following:

- *VistALink 1.5 Installation Guide*: Provides detailed instructions for setting up, installing, and configuring the VistALink 1.5 listener on VistA/M servers and the VistALink resource adapter on J2EE application servers. Its intended audience includes server administrators, IRM IT specialists, and Java application developers.
- *VistALink 1.5 System Management Guide*: Contains detailed information on J2EE application server management, institution mapping, the VistALink console, M listener management, and VistALink security, logging, and troubleshooting.
- *VistALink 1.5 Developer Guide*: Contains detailed and background information about writing code utilizing VistALink.
- *VistALink 1.5 Release Notes*: A list of all the features included in each VistALink 1.5 release.
- *Getting Started With the BDK, Chapter 3*: *RPC Overview*. A short guide on writing RPCs from the *RPC Broker* manual.

### BEA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.5 has been tested and is supported on BEA WebLogic Server 8.1 (Service Pack 4) only. WebLogic product documentation can be found at the following website: <http://edocs.bea.com/>.

## # Developer Workstation Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Using Station Number (Institution) and Subdivision

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink asks application code to provide VHA institution station numbers in two situations, for different purposes: system location and multi-division awareness. Because these two modes of use are separate, the meaning of *station number* is "overloaded." The two modes are described in the sections below.

### System Locator: Institution-Connector Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your code must provide a station number to retrieve a connector JNDI name from VistALink's institution-mapping API. Lacking anything better, the station number is used as a location designator for a particular system.

Each connector has a primaryStation attribute, which is configured by the J2EE administrator. On the M system, this value should exactly match the DEFAULT INSTITUTION value in the Kernel Systems Parameter File. VistALink uses primaryStation to confirm that a connector is accessing the correct M system: if the two values don't match, connections are rejected. The primaryStation attribute is also the mapping source between station numbers and connector JNDI names.

In 99 percent of the cases, this attribute is all-numeric (e.g., "523"). When asked for the JNDI name for a station number with a subdivision suffix, such as "523A", the institution mapping API will return a JNDI name mapped to "523". The API handles some special cases too. For example, "5239" would be a nursing home at "523" where "9" is the nursing home indicator.

### Multidivision-Aware Application Code: ConnectionSpec Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your code must also use the station number to create a connection spec, which it then uses to obtain a VistALink connection. When your code executes a remote procedure call (RPC), the station number specified in the connection spec is passed to M to populate the variable DUZ(2) on the M system. On M systems, DUZ(2) is used to make applications multidivision-aware, to give the right view of the data. On merged systems, for example, an end-user might only see the set of patients matching the station number specified in their DUZ(2) (e.g., "523B").

Only one value can be set into DUZ(2) at a time. So, if you construct a connection spec (e.g., "connSpec = new VistaLinkVpidConnectionSpec(division, vpid)") and pass in "523B", VistALink sets DUZ(2) on the M side to "523B". RPCs are then executed under that setting (if it is granted as a permissible subdivision to the end-user.)

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In a merged site, where an end-user has access to "636A" but not to "636", the institution mapping lookup for "636A" will return the connector whose primaryStation attribute is "636". If you create a connection spec and connection to execute an RPC and specify "636A", this value will be set into DUZ(2) on the M side. The RPC will execute with multi-division awareness, i.e., that the current institution is "636A".

## Checked and Unchecked Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two types of exceptions in the Java programming language:

- Checked exceptions: These have to be declared in the method signature "throws" clause if they are thrown by the method. Checked exceptions have to be explicitly caught by the caller within a "try / catch" block.
- Unchecked exceptions: These do not have to be declared in the method signature if they are thrown by the method. Unchecked exceptions do not need to be explicitly caught by the caller. Unchecked exceptions can be caught by the caller even if the method does not explicitly throw them.

The diagram below depicts a class hierarchy of base Java exception classes. VistALink throws only checked exceptions.

> ![](vistalink-version-1-5-developer-guide/006.png)

> <span id="_Toc135039343" class="anchor"></span>Figure 1. Java Base Exception Classes

## Catching Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is important to remember when an application calls a method that (in turn) throws exception *A,* the application can do two things:

- Catch exception *A*
- Catch any exception *AB* that is subclassed from exception *A*, even though calling a method declaration only declares to throw a parent exception. Example:

<span class="mark">publicclass ParentException extends Exception {</span>

<span class="mark">}</span>

<span class="mark">publicclass SubException extends ParentException {</span>

<span class="mark">}</span>

<span class="mark">publicclass ExceptionSample {</span>

<span class="mark"></span>

<span class="mark">publicstaticvoid test() throws ParentException {</span>

<span class="mark">thrownew SubException();</span>

<span class="mark">}</span>

<span class="mark">publicstaticvoid main(String\[\] args) {</span>

<span class="mark"> try {</span>

<span class="mark"> ExceptionSample.test();</span>

<span class="mark"> } catch (SubException e) {</span>

<span class="mark"> System.out.println("Caught SubException exception");</span>

<span class="mark"> } catch (ParentException e) {</span>

<span class="mark"> System.out.println("Caught ParentException exception");</span>

<span class="mark"> }</span>

<span class="mark">}</span>

<span class="mark">}</span>

In the example above, we are declaring ParentException and its subclass SubException. ExceptionSample class has a method test() that declares to throw ParentException. Method test() implementation instead throws a more specific exception SubException. The test() method could choose to declare the fact that it is throwing both ParentException and SubException, but that is not required by the Java specifications.

The test() method caller can only catch ParentException. This takes care of catching ParentException and all ParentException subclasses. But if the test() method caller knows that test() method throws a more specific exception (a subclass of the ParentException), then the caller can choose to catch a more specific SubException, even though test() method does not explicitly declare the fact that it throws SubException.

This is an important point, as both the VistALink security modules and the VistALink resource adapter modules often throw more specific VistALink exceptions, even though those exceptions are not declared to be thrown and only parent exceptions are declared to be thrown from VistALink methods.

## J2EE and J2SE Connectors Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

J2EE Connectors requires adapter methods to throw javax.resource.ResourceException.

### VistaLinkResourceException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink implements gov.va.med.vistalink.adapter.cci.VistaLinkResourceException that extends javax.resource.ResourceException. VistaLinkResourceException is thrown from all J2EE Connectors required methods as well as any custom method in VistALink that implements connection management interfaces.

VistaLinkResourceException more specific exception subclasses include (see the [VistALink Exception Hierarchy](#vistalink-exception-hierarchy) figure above):

- ConnectionHandlesExceededException
- VistaLinkSocketClosedException
- HeartBeatFailedException
- HeartBeatInteractionFailedException.

### FoundationsException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The J2EE Connector Architecture specification defines optional record and interaction management interfaces that are not implemented in VistALink. Instead, VistALink uses VistaLinkConnection::executeRPC(), VistaLinkConnection::executeInteration() and classes in gov.va.med.vistalink.adapter.record package to implement interaction and record management. These methods are not governed by the J2EE Connector Architecture specification. Hence VistALink uses gov.va.med.exception.FoundationsException and its subclasses in these methods.

### VistaLinkFaultException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink communications with M can produce exceptions that originate from the Java code side. In that case, VistaLinkResourceException and FoundationsException will be thrown (described above).

VistALink communications with M can also produce exceptions that originate from the M side. In those cases a Fault message is sent back to VistALink from M. Fault messages are parsed and gov.va.med.vistalink.adapter.record.VistaLinkFaultException that extends FoundationsException are constructed to be thrown in those cases.

VistaLinkFaultException will have all the information that is sent back from the M side to Java, including: faultCode, faultString, faultActor, errorCode, errorType and errorMessage.

VistaLinkFaultException more specific exception subclasses include (see the [VistALink Exception Hierarchy](#vistalink-exception-hierarchy) figure above):

- NoJobSlotsAvailableFaultException
- LoginsDisabledFaultException
- SecurityFaultException (contain more specific subclasses)
- RpcFaultException (contain more specific subclasses)

### Common FoundationsExceptionInterface 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

gov.va.med.exception.FoundationsExceptionInterface is defined to be able to have common interface for all types of VistALink exceptions. Implementation of this interface allows gov.va.med.exception.ExceptionUtils to work exceptions, no matter what they inherit from.

### Exception Nesting 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exception nesting is a technique used to collect full information about the error that occurred in the processing method call. Example:

> Exception *A* can be thrown from a library. Client code catches the exception *A* and rethrows new exception *B* while preserving the original exception *A* within new exception's member variables.

> This new exception B once again could be caught by some other client code that could throw new exception C while preserving caught exception B within exception's C member variables:

> A nested within B nested within C.

This way, all caught and rethrown exceptions are kept as a linked exception list. This lets us keep all information about the error's origination and how the error is handled by the code.

JDK 1.4 has native support for exception nesting, while JDK 1.3 does not have native support for exception nesting. Since VistALink runs both on JDK 1.3 and 1.4, VistALink has implemented a custom exception nesting framework.

All VistALink base exception classes implement exception nesting:

- gov.va.med.foundations.utilities.FoundationsException
- gov.va.med.foundations.adapter.cci.VistaLinkResourceException
- gov.va.med.foundations.security.vistalink.VistaLoginModuleException

## Working with Nested Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your code catches one of the above exceptions, here are some features that can be expected:

> exception.getMessage() returns all nested exception messages in the folling format:

> Wrapper exception;  
> Root cause exception:

> java.lang.Exception: <span class="mark"></span>Here is my nested exception<span class="mark">.</span>

> exception.printStackTrace() will print both nested exception messages and full stack trace:

> gov.va.med.exception.FoundationsException:  
> Wrapper exception<span class="mark">;</span>

> <span class="mark">Root cause exception:</span>

> <span class="mark"></span>java.lang.Exception: <span class="mark"></span>Here is my nested exception.

> java.lang.Exception: <span class="mark">Here is my nested exception.</span>

> <span class="mark">at</span>

> gov.va.med.vistalink.utilities.test.FoundationsExceptionTest.t2  
> <span class="mark">(</span>FoundationsExceptionTest.java:106<span class="mark">)</span>

> <span class="mark">at</span>

> gov.va.med.vistalink.utilities.test.FoundationsExceptionTest.t1  
> (FoundationsExceptionTest.java:109)

> <span class="mark">at</span> gov.va.med.vistalink.utilities.test.FoundationsExceptionTest.testConstructorStrExc(FoundationsExceptionTest.java:128)

> <span class="mark">at</span> sun.reflect.NativeMethodAccessorImpl.invoke0<span class="mark">(Native Method)</span>

> <span class="mark"></span>at sun.reflect.NativeMethodAccessorImpl.invoke<span class="mark">(Unknown Source)</span>

> <span class="mark">at</span> sun.reflect.DelegatingMethodAccessorImpl.invoke<span class="mark">(Unknown Source)</span>

> <span class="mark">at</span> java.lang.reflect.Method.invoke<span class="mark">(Unknown Source)</span>

> <span class="mark">at</span> junit.framework.TestCase.runTest(TestCase.Java:154)

> <span class="mark">at</span> junit.framework.TestCase.runBare(TestCase.Java:127)

> <span class="mark">at</span> junit.framework.TestResult\$1.protect(TestResult.Java:106)

> <span class="mark">at</span> junit.framework.TestResult.runProtected(TestResult.Java:124)

> <span class="mark">at</span> junit.framework.TestResult.run(TestResult.Java:109)

> <span class="mark">at</span> junit.framework.TestCase.run(TestCase.Java:118)

> <span class="mark">at</span> junit.framework.TestSuite.runTest(TestSuite.Java:208)

> <span class="mark">at</span> junit.framework.TestSuite.run(TestSuite.Java:203)

> <span class="mark">at</span> junit.swingui.TestRunner\$16.run(TestRunner.Java:623)

> exception.getNestedException() will return a nested exception. Note: do not use this method to unwind the nested exception linked list as there is a helper method in ExceptionUtils.getNestedExceptionByClass() that does just that.

See the section "ExceptionUtils" below for more methods that can be used when working with exceptions.

### ExceptionUtils

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

gov.va.med.exception.ExceptionUtils is a utility class that contains static helper methods such as getFullStackTrace() and getNestedExceptionByClass() to help unwind the nested exception stack trace.

### ExceptionUtils:: getFullStackTrace(Throwable e)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ExceptionUtils:: getFullStackTrace(Throwable e) returns the full stack trace, in case you need to print the stack trace for exception *e* to some other place other than the system output console, such as the HTML error page or the Swing text box. To print the stack trace to system output console just use exception.printStackTrace().

Notice that we are using Throwable instead of Exception here, as this will allow us to print a stack trace even for Errors. The getFullStackTrace method prints out both the nested exception message set as well as the full stack trace. If you are using this method to return the full stack trace, this means the error message will be part of it and you don't need to use exception.getMessage().

### ExceptionUtils:: getNestedExceptionByClass()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ExceptionUtils:: getNestedExceptionByClass(Throwable e, Class exceptionClass) returns an exception if an exception of a class type exceptionClass exists in the exception *e* nested exception linked list.

So if your nested exceptions look like this:

(a instance of A) nested within (b instance of B) nested within (c instance of C)

Then *a* calls:

> ExceptionUtils:: getNestedExceptionByClass(c, C) returns c.

> ExceptionUtils:: getNestedExceptionByClass(c, B) returns b.

> ExceptionUtils:: getNestedExceptionByClass(c, A) returns a.

### XMLUtilities Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

String xmlStr = XmlUtilities.XML_HEADER

\+ "\<VistaLink messageType='"

\+ RpcRequest.GOV_VA_MED_RPC_REQUEST

\+ "'"

\+ " mode='singleton'"

\+ " version='1.0'"

\+ " xmlns:xsi='http://www.w3.org/2001/XMLSchema-instance'"

\+ " xsi:noNamespaceSchemaLocation='rpcRequest.xsd'"

\+ " xmlns='http://med.va.gov/Foundations'"

+"\>"

\+ " \<RpcHandler version='1.0'/\>"

\+ " \<Request rpcName='' rpcClientTimeOut='600' version='1.0' \>"

\+ " \<RpcContext\>\</RpcContext\>"

\+ " \<Params\>\<Param type='array' \>\</Param\>\</Params\>"

\+ " \</Request\>"

\+ "\</VistaLink\>";

Document doc = XmlUtilities.getDocumentForXmlString(xmlStr);

Node param = XmlUtilities.getNode("/VistaLink/Request/Params/Param", requestDoc);

String type = XmlUtilities.getAttr(param, "type").getValue();

String xmlCopy = XmlUtilities.convertXmlToStr(xmlDoc);

...

FileInputStream xmlStream = FileInputStream("myRequest.xml");

Document myReq = XmlUtilities.getDocumentForXmlInputStream(xmlStream);

...

### VistaLoginModule Callback Handlers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to decouple the user interface for logon from the login module, the JAAS standard allows login modules such as VistaLoginModule to supply different callback handlers. VistALink supplies two callback handler classes, one for an interactive logon, and one for non-interactive unit testing:

- CallbackHandlerSwingCCOW: for production application use. Performs single-signon if credentials are already present in CCOW user context. Otherwise, collects access code, verify code, division and "change verify code" input via a set of Swing dialogs; stores single sign-on credentials in CCOW user context for subsequent application use.
- CallbackHandlerSwing: for production application use. Collects access code, verify code, division and "change verify code" input via a set of Swing dialogs.
- CallbackHandlerUnitTest: for unit testing only (not production use). Access code, verify code, division are passed as parameters to the class constructor, resulting in a "silent" login suitable for (non-interactive) unit testing. The "change verify code" functionality is not supported.

Part of the JAAS VistALink login involves instantiating one of these two callback handler classes and passing the class as a parameter to create a JAAS login context (see "[Putting the Pieces Together](#_Putting_the_Pieces_Together: VistAL)," below.
