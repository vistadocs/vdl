---
title: XOBV*1.6*5 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
app_code: XOBV
app_name: VistALink
section: INF
app_status: active
pkg_ns: XOBV
patch_ver: 1.6
patch_id: XOBV*1.6*5
group_key: "XOBV:XOBV:1.6"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - contents
  - vistalink
  - weblogic
  - updates
  - jars
  - libraries
  - java
  - compatibility
  - shared
page_count: 0
word_count: 1071
section_count: 12
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_5_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_5_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=163"
---

> ![](xobv-1-6-5-release-notes/001.png)

VISTALINK RELEASE NOTES

> Version 1.6

> July 2020

> Department of Veterans Affairs Office of Information and Technology Product Development

> *This page is left blank intentionally.*

> Contents

1.  [Introduction 1-1](#introduction)
    1.  [About VistALink 1-1](#about-vistalink)
    2.  [WebLogic Updates Project 1-1](#weblogic-updates-project)
    3.  [New Product Web Site 1-1](#new-product-web-site)
    4.  [For More Information 1-1](#for-more-information)
2.  [VistALink Adapter Updates 2-1](#vistalink-adapter-updates)
    1.  [WebLogic 10.3.6/12.1.2 Compatibility 2-1](#weblogic-10.3.612.1.2-compatibility)
    2.  [Fortify and TRM Compliance 2-1](#fortify-and-trm-compliance)
    3.  [Reminder - RAR Changes Summary since Previous Version – 1.5 2-1](#reminder---rar-changes-summary-since-previous-version-1.5)
    4.  [New Recommendation: Deploy VistALink Jars as J2EE Shared Libraries (Production Systems Only) 2-2](#new-recommendation-deploy-vistalink-jars-as-j2ee-shared-libraries-production-systems-only)
    5.  [Updated Sample log4j Configuration Files 2-2](#updated-sample-log4j-configuration-files)
3.  [VistALink Administration Console Updates 3-3](#vistalink-administration-console-updates)
    1.  [WebLogic 10.3 Compatibility 3-3](#weblogic-10.3-compatibility)
4.  [J2SE Client/Server Updates 4-3](#j2se-clientserver-updates)
    1.  [Java 1.7 or Greater Required 4-3](#java-1.7-or-greater-required)

> July 2020 VistALink V. 1.6 Release Notes iii

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [About VistALink](#about-vistalink)
  - [WebLogic Updates Project](#weblogic-updates-project)
  - [New Product Web Site](#new-product-web-site)
  - [For More Information](#for-more-information)
- [VistALink Adapter Updates](#vistalink-adapter-updates)
  - [WebLogic 10.3.6/12.1.2 Compatibility](#weblogic-10361212-compatibility)
  - [Fortify and TRM Compliance](#fortify-and-trm-compliance)
  - [Reminder - RAR Changes Summary since Previous Version – 1.5](#reminder-rar-changes-summary-since-previous-version-15)
  - [New Recommendation: Deploy VistALink Jars as J2EE Shared Libraries (Production Systems Only)](#new-recommendation-deploy-vistalink-jars-as-j2ee-shared-libraries-production-systems-only)
  - [Updated Sample log4j Configuration Files](#updated-sample-log4j-configuration-files)
- [VistALink Administration Console Updates](#vistalink-administration-console-updates)
  - [WebLogic 10.3 Compatibility](#weblogic-103-compatibility)
- [J2SE Client/Server Updates](#j2se-clientserver-updates)
  - [Java 1.7 or Greater Required](#java-17-or-greater-required)

## About VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistALink resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet- VistA Java applications and VistA/Mumps (M) servers, in both client-server and n-tier environments. It is a runtime and development tool that allows java applications to execute remote procedure calls (RPCs) on the VistA/M system and retrieve results, synchronously. VistALink is also referred to as VistALink J2M.

> VistALink consists of Java-side adapter libraries and an M-side listener:

- The adapter libraries use the Java 2 Enterprise Edition (J2EE) Connector Architecture (J2CA) 1.5 specification to integrate Java applications with legacy systems.
- The Mumps (M) listener process receives and processes requests from client applications.
- Java applications can call RPCs on the M server, executing RPC Broker RPCs on the M server without modification.

## WebLogic Updates Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In support of the Department of Veterans Affairs Information Technology Application Modernization effort, the three applications VistALink, Fat-client Kernel Authentication and Authorization (FatKAAT), and Kernel Authentication and Authorization for the Java 2 Enterprise Edition (KAAJEE) have been developed. Based on the direction of the Technical Review Model (TRM) and in order to support applications that upgrade to the new WebLogic Server versions 10.3.6 and 12.1.2, this project is required. The scope of the project is to upgrade these three applications to work with the WebLogic Server versions

> 10.3.6 and 12.1.2.

> The previous version of VistALink, 1.5, was released in June of 2006, and provided project developers with J2EE and Java Platform, Standard Edition (J2SE) application connectivity to VistA/M servers. It was designed specifically for J2EE 1.3 application servers (e.g., WebLogic 8.1).

## New Product Web Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> New VistALink Web site REDACTED

> summarizes VistALink architecture and functionality and gives status updates for all VistALink products.

## For More Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For more information on any new feature discussed in the release notes, please see the VistALink documentation set on the VA Software Document Library (VDL) at the following address:

> [<u>http://www.va.gov/vdl/application.asp?appid=163</u>](http://www.va.gov/vdl/application.asp?appid=163)

> July 2020 VistALink V. 1.6 Release Notes 1-1

> *This page is left blank intentionally.*

> July 2020 VistALink V. 1.6 Release Notes 1-1

# VistALink Adapter Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## WebLogic 10.3.6/12.1.2 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistALink 1.6.1 adapters have been updated to be compatible with:

- WebLogic 10.3.6 and 12.1.2
- Java 1.7
- J2EE 1.4+
- J2EE Connector Architecture 1.5

## Fortify and TRM Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistALink 1.6.1 codebase have been updated with following noteworthy items:

- Introduced a \*.fortify package
- Implemented Reverse-DNS validation on the IP addresses of targeted M systems at the configuration file \*\*\*
- Reset authentication byte arrays
- Dereferenced null references
- Updated codebase with API references to log4j2 libraries

> \*\*\* A Reverse-DNS information validation is now in place. VistALink will not connect to IP address without a reverse dns information in the PTR record.

## Reminder - RAR Changes Summary since Previous Version – 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- vljFoundationsLib and vljConnector jars: New versions provide a J2CA 1.5 and VA’s TRM compliant adapter implementation.
- Deployment Descriptor Changes: The format of both the ra.xml and weblogic-ra.xml descriptors are different. Existing adapters' deployment descriptors need to be updated. Using the provided sample/template descriptors, only weblogic-ra.xml will need to be modified when creating a VistALink RAR:
  - META-INF/ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. In most cases, it no longer needs any further editing when creating a RAR.
  - META-INF/weblogic-ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. It must be edited for each RAR deployed.
  - META-INF/MANIFEST.MF: The template version provided in the VistALink distribution is updated to support use of J2EE Shared Libraries by RARs.
- lib/saxpath.jar, lib/jaxen-core.jar, and lib/jaxen-dom.jar are no longer needed in the RAR as their functionality has been replaced by the XPath implementation introduced in Java 5.

> July 2020 VistALink V. 1.6 Release Notes 2-1

> J2SE Client/Server Updates

- lib/xbean.jar no longer needed in the RAR since an implementation of XML Beans is included in WebLogic 9 and onward.
- Linked adapters (link-ref mechanism) no longer supported for VistALink 1.6 adapters.
- Development System Classloading: Automatic classloading of all jars in RAR is now supported by WebLogic 10.3.6. Library jars included in RAR no longer need to be manually added to the server classpath.
- Production System Classloading: Oracle (formerly known as BEA) recommends removing all jars from RARs on production systems, and deploying them as J2EE shared libraries instead (to reduce resource consumption – replacement for resource-saving aspect of the 8.1 link-ref mechanism). When deployed as J2EE shared libraries, the jars supporting VistALink RARs no longer need to be manually added to the server class path.

## New Recommendation: Deploy VistALink Jars as J2EE Shared Libraries (Production Systems Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As a replacement for the WebLogic 8.1 “Linked Adapters” feature (not supported for upgraded adapters like VistALink 1.6), Oracle recommends removing all jars from RARs on production systems, and deploying each one as a J2EE shared library instead. This addresses the reduced resource consumption benefit formerly provided by using the 8.1 link-ref mechanism. Therefore, on production systems only, we recommend that the following jars be removed from all RARs and deployed (once) as J2EE shared libraries:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Jar Name</strong></th>
<th><strong>J2EE Shared Library Deployment Name</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>vljConnector-1.6.1.jar</td>
<td>vljConnector(1.6,1.6)</td>
</tr>
<tr class="even">
<td>vljFoundationsLib-1.6.1.jar</td>
<td>vljFoundationsLib(1.6,1.6)</td>
</tr>
<tr class="odd">
<td><p>log4j-api-2.10.0</p>
<p>log4j-core-2.10.0</p></td>
<td><p>log4j-api-2</p>
<p>log4j-core-2</p></td>
</tr>
</tbody>
</table>

> Two different versions of an example RAR are provided in the distribution zip file, one structured for development system deployments, the other for production deployments:

- rar\Rar-Dev (contains all needed jars)
- rar\Rar-Prod (contains no jars; MANIFEST.MF file looks for jars as J2EE shared libraries)

## Updated Sample log4j Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> With log4j dependency being upgraded to version 2, there is a change in the syntax of log4j configuration file. The new sample log4j configuration files are located in the log4j directory inside the VistALink distribution zip file, as follows:

| File Name | Description |
|---------------|-----------------|

> 2-2 VistALink V. 1.6 Release Notes July 2020

> WebLogic Updates Project: VistALink Version 1.6

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th>log4j2SampleJ2EEConfig.xml</th>
<th><p>Example configuration for a J2EE system, turning DEBUG-level logging on for VistALink classes of interest on a J2EE system.</p>
<p>NOTE: Turning on ‘debug’ level can adversely affect system performance.</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>log4j2SampleJ2SEConfig.xml</td>
<td><p>Example configuration for a J2SE (Java client-M server) application, turning DEBUG-level logging on for</p>
<p>VistALink classes of interest for client/server applications.</p></td>
</tr>
</tbody>
</table>

> *.*

# VistALink Administration Console Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## WebLogic 10.3 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Due to difficulties encountered integrating the VistALink administration console with the earlier versions of WebLogic (specifically its navigation tree and tab set), the VistALink administration console is provided as a standalone web application, in an EAR file. Therefore, for WebLogic 10.3 we recommend installing the VistALink administration console as a standalone web application, not integrated with the WebLogic console. The standalone EAR can also be used on 10.3.6 and 12.1.1 of WebLogic if desired.

# J2SE Client/Server Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Java 1.7 or Greater Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Because VistALink 1.6’s jars, used both on WebLogic 10 and WebLogic 12.1.2, and for client/server connectivity, are compiled with Java 1.7, new client/server applications using VistALink 1.6 will need to use JDK 1.7 and up.

> July 2020 VistALink V. 1.6 Release Notes 4-3

> J2SE Client/Server Updates

> *This page is left blank intentionally.*

> 4-4 VistALink V. 1.6 Release Notes July 2020