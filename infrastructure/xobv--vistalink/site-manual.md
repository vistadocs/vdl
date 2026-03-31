---
consolidated_title: "vistalink system management guide"
app_code: XOBV
doc_type: SM
master_source: "VistALink Version 1.6 System Management Guide"
master_pub_date: revision_count: 0
consolidated_from: 3 versions
prior_versions:
  - "VistALink Version 1.5 System Management Guide"
  - "VistaLink Version 1.6.7 System Management Guide"
---

# ![](vistalink-version-1-6-system-management-guide/001.png)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [![](vistalink-version-1-6-system-management-guide/001.png)](#vistalink-version-1-6-system-management-guide001png)
- [Revision History](#revision-history)
- [Contents](#contents)
- [Figures](#figures)
- [Tables](#tables)
- [Orientation](#orientation)
    - [Terminology](#terminology)
    - [Text Conventions](#text-conventions)
    - [WebLogic Systems](#weblogic-systems)
- [# Introduction](#introduction)
  - [VistALink 1.6 Overview](#vistalink-16-overview)
  - [WebLogic Updates Project](#weblogic-updates-project)
  - [Fortify and TRM updates](#fortify-and-trm-updates)
    - [Install the Critical Patch Update](#install-the-critical-patch-update)
    - [Extend the blacklists](#extend-the-blacklists)
    - [Set up SSL on a WebLogic Server](#set-up-ssl-on-a-weblogic-server)
- [Deploying VistALink Adapters on J2EE](#deploying-vistalink-adapters-on-j2ee)
  - [RAR Overview](#rar-overview)
    - [Summary of RAR Changes Since Previous Version](#summary-of-rar-changes-since-previous-version)
  - [Creating a RAR](#creating-a-rar)
    - [Exploded 1.6.1 RAR Layout, Production Systems](#exploded-161-rar-layout-production-systems)
    - [Exploded 1.6.1 RAR Layout, Non-Production Systems](#exploded-161-rar-layout-non-production-systems)
    - [Deployment Descriptor: ra.xml](#deployment-descriptor-raxml)
  - [VistALink Connector Configuration File](#vistalink-connector-configuration-file)
    - [Connector Entry Format](#connector-entry-format)
    - [Connector Settings](#connector-settings)
    - [Advanced Connector Settings](#advanced-connector-settings)
    - [File-Wide Setting: encryptionScoped](#file-wide-setting-encryptionscoped)
    - [Obsolete Settings](#obsolete-settings)
  - [Deploying J2EE Shared Libraries for VistALink (Production Systems Only)](#deploying-j2ee-shared-libraries-for-vistalink-production-systems-only)
  - [Deploying a RAR](#deploying-a-rar)
  - [Updating Already-Deployed Adapters](#updating-already-deployed-adapters)
  - [DNS Updates and VistALink Adapters](#dns-updates-and-vistalink-adapters)
  - [Pool Size Management/Tuning](#pool-size-managementtuning)
- [Configuring log4j Logging](#configuring-log4j-logging)
  - [log4j Configuration Overview](#log4j-configuration-overview)
  - [Configuring log4J](#configuring-log4j)
    - [Alternative Approach](#alternative-approach)
  - [Sample log4j Configuration Files](#sample-log4j-configuration-files)
  - [VistALink Core log4j Categories](#vistalink-core-log4j-categories)
- [Institution Mapping](#institution-mapping)
  - [Managing the Mapping](#managing-the-mapping)
    - [PrimaryStation Attribute (VistALink Configuration File)](#primarystation-attribute-vistalink-configuration-file)
    - [How the Mapping Is Initialized](#how-the-mapping-is-initialized)
    - [Viewing the Current Mapping](#viewing-the-current-mapping)
    - [Updating Institution Mappings](#updating-institution-mappings)
    - [How Applications Use Institution Mappings](#how-applications-use-institution-mappings)
  - [Troubleshooting Institution Mapping Issues](#troubleshooting-institution-mapping-issues)
    - [Out-of-Synch Configuration Files on Multiple Physical Servers](#out-of-synch-configuration-files-on-multiple-physical-servers)
    - [Connector Station and M System Mismatch](#connector-station-and-m-system-mismatch)
    - [JNDI Name Configuration Mismatch](#jndi-name-configuration-mismatch)
    - [Mappings with Undeployed Connectors (Stopped or Deleted)](#mappings-with-undeployed-connectors-stopped-or-deleted)
  - [Pluggable Institution Mapping Rules](#pluggable-institution-mapping-rules)
- [The VistALink Administration Console](#the-vistalink-administration-console)
  - [Overview](#overview)
  - [Monitor Role Restrictions](#monitor-role-restrictions)
  - [Accessing the VistALink Administration Console](#accessing-the-vistalink-administration-console)
    - [VistALink Administration Console as Standalone Web Application](#vistalink-administration-console-as-standalone-web-application)
    - [VistALink Administration Console as WebLogic Console Extension](#vistalink-administration-console-as-weblogic-console-extension)
  - [Monitoring Connector Status](#monitoring-connector-status)
    - [Adapter List/Summary](#adapter-listsummary)
    - [Adapter Detail](#adapter-detail)
    - [Monitoring Institution Mapping](#monitoring-institution-mapping)
  - [Configuration Editor](#configuration-editor)
    - [About the Configuration File](#about-the-configuration-file)
    - [How to Propagate Configuration Changes to Other Servers](#how-to-propagate-configuration-changes-to-other-servers)
    - [Viewing and Editing Connector Properties](#viewing-and-editing-connector-properties)
    - [Encryption of Access/Verify Codes](#encryption-of-accessverify-codes)
- [Monitoring VistALink via JMX and MBeans](#monitoring-vistalink-via-jmx-and-mbeans)
  - [Overview](#overview-1)
  - [VistALink MBeans](#vistalink-mbeans)
    - [VistaLinkConnector MBean](#vistalinkconnector-mbean)
    - [VistaLinkInstitutionMapping MBean](#vistalinkinstitutionmapping-mbean)
  - [VistALink MBean Security](#vistalink-mbean-security)
- [M Server Management](#m-server-management)
  - [Overview](#overview-2)
  - [Finding User Processes with the Connection Manager](#finding-user-processes-with-the-connection-manager)
  - [Finding VistALink Processes without the Connection Manager](#finding-vistalink-processes-without-the-connection-manager)
    - [VMS Systems](#vms-systems)
    - [Non-VMS Systems](#non-vms-systems)
  - [Listener Management](#listener-management)
    - [Listener Management for Caché/VMS Systems](#listener-management-for-cachévms-systems)
    - [Listener Management for Caché/NT Systems](#listener-management-for-cachént-systems)
    - [Listener Management for DSM/VMS Systems](#listener-management-for-dsmvms-systems)
  - [M Listener Site Parameters File](#m-listener-site-parameters-file)
    - [Site Parameters for All System Types](#site-parameters-for-all-system-types)
    - [Site Parameters for Windows Systems](#site-parameters-for-windows-systems)
- [Security](#security)
  - [J2EE System Manager Security Tasks for VistALink](#j2ee-system-manager-security-tasks-for-vistalink)
  - [M System Manager Security Tasks for VistALink](#m-system-manager-security-tasks-for-vistalink)
  - [VistALink's J2SE Security Model](#vistalinks-j2se-security-model)
  - [VistALink's J2EE Security Model](#vistalinks-j2ee-security-model)
    - [Connector Proxy User (J2EE)](#connector-proxy-user-j2ee)
    - [J2EE Re-authentication Mechanisms for End-Users](#j2ee-re-authentication-mechanisms-for-end-users)
  - [RPC Security (B-Type Option)](#rpc-security-b-type-option)
  - [Creating Connector Proxy Users for J2EE Systems](#creating-connector-proxy-users-for-j2ee-systems)
    - [Security Caution](#security-caution)
    - [Creating the "Connector Proxy User"](#creating-the-connector-proxy-user)
  - [Additional Security Issues (J2SE Mode)](#additional-security-issues-j2se-mode)
    - [Authentication in Client/Server Mode](#authentication-in-clientserver-mode)
    - [CCOW-Based Single Sign-on](#ccow-based-single-sign-on)
    - [Kernel Auto Sign-on](#kernel-auto-sign-on)
    - [Sensitivity of VistALink-Logged Data](#sensitivity-of-vistalink-logged-data)
- [Troubleshooting VistALink 1.6](#troubleshooting-vistalink-16)
  - [Overview](#overview-3)
  - [Symptoms and Possible Solutions](#symptoms-and-possible-solutions)
    - [Connection Attempt to Bad Listener Address/Port](#connection-attempt-to-bad-listener-addressport)
    - [Connection Attempt to RPC Broker Listener](#connection-attempt-to-rpc-broker-listener)
    - [Invalid Connector Proxy Credentials](#invalid-connector-proxy-credentials)
    - [Connector Proxy Expired Verify Code](#connector-proxy-expired-verify-code)
    - [Sporadic Socket Timeouts](#sporadic-socket-timeouts)
    - [Connection Pool Capacity Exceeded](#connection-pool-capacity-exceeded)
    - [ClassCastException](#classcastexception)
    - [Configuration File Confusion](#configuration-file-confusion)
    - [Reauthentication (End-User Identification) Failure](#reauthentication-end-user-identification-failure)
    - [Division Mismatch](#division-mismatch)
    - [Failure to Authorize RPC (B-Type Option)](#failure-to-authorize-rpc-b-type-option)
    - [M-Side Error Returned to J2EE](#m-side-error-returned-to-j2ee)
    - [Abrupt Disconnects (M-Side Errors)](#abrupt-disconnects-m-side-errors)
    - [J2SE Connection Attempt to 1.0 Listener](#j2se-connection-attempt-to-10-listener)
  - [Analyzing VistALink Errors in the M Error Trap](#analyzing-vistalink-errors-in-the-m-error-trap)
    - [XOBSTR Variable](#xobstr-variable)
    - [XWBTIP Variable](#xwbtip-variable)
    - [XOBLASTR Variable (M Request Timestamp)](#xoblastr-variable-m-request-timestamp)
  - [Analyzing VistALink Java Exceptions](#analyzing-vistalink-java-exceptions)
  - [Section 508 Compliance: Differentiate Focus on Change Verify Code Check Box](#section-508-compliance-differentiate-focus-on-change-verify-code-check-box)
- [Appendix A: Listener Management for Cache/NT Systems](#appendix-a-listener-management-for-cachent-systems)
  - [Creating/Editing Listener Configurations](#creatingediting-listener-configurations)
  - [Starting All Configured Listeners](#starting-all-configured-listeners)
  - [Starting a Single Unconfigured Listener](#starting-a-single-unconfigured-listener)
  - [Stopping a Configured or Unconfigured Listener](#stopping-a-configured-or-unconfigured-listener)
  - [Scheduling Listener Startup at System Startup](#scheduling-listener-startup-at-system-startup)
- [Appendix B: Listener Management for DSM/VMS Systems](#appendix-b-listener-management-for-dsmvms-systems)
  - [Setting Up an OpenVMS User Account](#setting-up-an-openvms-user-account)
  - [Setting Up a Home Directory for the VistALink Handler Account](#setting-up-a-home-directory-for-the-vistalink-handler-account)
  - [Creating a DCL Login Command Procedure for the VistALink Handler](#creating-a-dcl-login-command-procedure-for-the-vistalink-handler)
    - [Sample DCL Login Command Procedure](#sample-dcl-login-command-procedure)
  - [Setting Up and Enabling the TCP/IP Service](#setting-up-and-enabling-the-tcpip-service)
  - [Obtaining an Available Listener Port (for Alpha/VMS systems only)](#obtaining-an-available-listener-port-for-alphavms-systems-only)
  - [Creating the TCP/IP Service](#creating-the-tcpip-service)
  - [Enabling and Saving the Service](#enabling-and-saving-the-service)
  - [Access Control List ACL Issues](#access-control-list-acl-issues)
  - [Controlling the Number of Log Files](#controlling-the-number-of-log-files)
  - [Disabling New Connections](#disabling-new-connections)
  - [Terminating All Connections and Preventing New Ones](#terminating-all-connections-and-preventing-new-ones)
- [Glossary](#glossary)
VISTALINKSYSTEM MANAGEMENT GUIDE
July 2020
Office of Information and Technology
Enterprise Program Management Office

# Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 42%" />
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
<td>07/08/20</td>
<td>XOBV*1.6*5 – VistALink Version 1.6.1 release.</td>
<td><blockquote>
<p>Health Product Support Tier 3 Sustainment team.</p>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10/24/19</td>
<td>XOBVS*1.6*4 N/A Changes</td>
<td><blockquote>
<p>REDACTED</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/03/10</td>
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
</ul>
<blockquote>
<p>Technical Writer—REDACTED</p>
</blockquote></td>
</tr>
<tr class="even">
<td>05/2006</td>
<td>Initial VistALink Version 1.5 release.</td>
<td><p>REDACTED , technical writer</p>
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

<span id="_Toc281211662" class="anchor"></span>Table i. Revision History

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Figures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This System Management Guide is intended for use in conjunction with the VistALink software. It outlines the details of VistALink-related software and gives guidelines on how the software is used within Health*<u>e</u>*Vet-Veterans Health Information Systems and Technology Architecture (VistA).

The intended audience of this manual is all key stakeholders. The primary stakeholder is the Product Development Security Program team. Additional stakeholders include:

- Health*<u>e</u>*Vet-VistA application developers of Web-based applications in the WebLogic 10.3.6/12.1.2 Application Server environment.
- Information Resource Management (IRM) and Information Security Officers (ISOs) at Veterans Affairs Medical Centers (VAMCs) responsible for computer management and system security.
- Product Support (PS).
- Department of Veterans Affairs (VA) facility personnel who will be using Health*<u>e</u>*Vet-VistA Web-based applications running in the WebLogic 10.3.6/12.1.2 Application Server environment.

Document Overview

This manual provides information on the management of VistALink resource adapters and servers. It contains detailed information on:

- Deploying VistALink on Java 2 Enterprise Edition (J2EE) Servers
- J2EE Logging
- VistALink’s Institution Mapping
- The VistALink administration console
- Monitoring Adapters
- M listener management
- VistALink security
- Troubleshooting

> Its intended audience includes server administrators and IRM Information Technology (IT) specialists at VA facilities, as well as developers of Java applications requiring communication with VistA/Mumps (M).

Generally, the installation and maintenance instructions presented here assume the use of Windows as the client operating system. Where appropriate, separate steps are displayed for Linux.

### Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term *resource adapter* is often shortened in this guide to "adapter*,*" and is also used interchangeably with the term *connector*.

### Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File names and directory names are set off from other text using bold font (e.g., config.xml). Bold is also used to indicate Graphical User Interface (GUI) elements, such as tab, field, and button names (e.g., "press Delete").

All caps are used to indicate M routine and option names (e.g., XMINET). All caps used inside angle brackets indicate file names to be supplied by the user. Example:

> \<JAVA_HOME\>\bin\java -Dlog4j.configuration=file:///c:/localConfigs/mylog4j.xml

Names for Java objects, methods, and variables are indicated by Courier font. Snapshots of computer displays also appear in Courier, surrounded by a border:

Select Installation Option: LOAD a Distribution

Enter a Host File: XOB_1_6.KID

In these examples, the response that the user enters at a prompt appears in bold font:

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\> TELNET PORT

Boldface text is also used in code and deployment descriptor samples to indicate lines of particular interest, discussed in the preceding text:

\<?xml version="1.0"?\>

\<weblogic-connector xmlns="http://www.bea.com/ns/weblogic/90" xmlns:xsi=http://www.w3.org/2001/XMLSchema-instance xsi:schemaLocation="http://www.bea.com/ns/weblogic/90 http://www.bea.com/ns/weblogic/90/weblogic-ra.xsd"\>

\

- *VistALink 1.6 Developer Guide*: Contains detailed information about workstation setup, re-authentication, institution mapping, executing requests, VistALink exceptions, Foundations Library utilities, and other topics pertaining to writing code that uses VistALink.
- *VistALink 1.6 Release Notes*: Lists all new features included in the release.

VistALink end-user documentation can be downloaded from the VA Software Document Library (VDL) Web site:

> [<u>http://www.va.gov/vdl/application.asp?appid=163</u>](http://www.va.gov/vdl/application.asp?appid=163)

VistALink end-user documentation and software can be downloaded from any of the anonymous.software directories on the Office of Information Field Office (OIFO) File Transfer Protocol (FTP) download sites::

- Albany OIFO [REDACTED](ftp://ftp.fo-albany.med.va.gov)
- Hines OIFO [REDACTED](ftp://ftp.fo-hines.med.va.gov)
- Salt Lake City OIFO [REDACTED](ftp://ftp.fo-slc.med.va.gov)
- Preferred Method REDACTED

The documentation is made available online in Microsoft Word format and Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

### WebLogic Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the current time, VistALink 1.6.1 has been tested and is supported on WebLogic Server 10.3.6/12.1.2, only. WebLogic product documentation can be found at the following website:

<u>http://www.oracle.com/technetwork/middleware/weblogic/overview/index.html</u>

|                                                                                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/004.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# # Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistALink 1.6 Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet-VistA Java applications and VistA/M servers, in both client-server and n-tier environments. It allows Java applications to execute remote procedure calls (RPCs) on the VistA/M system and retrieve results, synchronously. VistALink is also referred to as "VistALink J2M."

VistALink 1.6 consists of Java-side adapter libraries and an M-side listener:

- The adapter libraries use the J2EE Connector Architecture (J2CA 1.5) specification to integrate Java applications with legacy systems.
- The M listener process receives and processes requests from client applications.

## WebLogic Updates Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In support of the Department of Veterans Affairs Information Technology Application Modernization effort, the three applications VistALink, Fat-client Kernel Authentication and Authorization (FatKAAT), and Kernel Authentication and Authorization for the Java 2 Enterprise Edition (KAAJEE) have been developed. Based on the direction of the Technical Review Model (TRM) and to support applications that upgrade to the new WebLogic Server versions 10.3.6/12.1.2, this project is required. The scope of the project is to upgrade these three applications to work with the WebLogic Server versions 10.3.6/12.1.2.

## Fortify and TRM updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following updates were made to the codebase in order to gain a Fortify and TRM compliance:

- Introduced a \*.fortify package
- Implemented Reverse-DNS validation on the IP addresses of targeted M systems at the configuration file (footer reference) \*\*\*
- Reset authentication byte arrays
- Dereferenced null references
- Updated codebase with API references to log4j2 libraries

Some of these items and the constants associated with them will be further expanded upon within the bode of this guide.

\*\*\*A PTR record validation has been implemented to gain Fortify Compliance. From this point all iptables entries with no Reverse DNS information will not be connected upon, by VistALink.

As it was mentioned previously, VistALink 1.6.1 is adherent to the [JCA](#JCA) 1.5 specification. As such, it supports the [JMX](#JMX) standard for Standard Managed Beans’ lifecycle management and monitoring. Two of the VistALink provided MBean classes [implement](#vistalink-mbeans) the Serializable interface. Starting in 2015, there has been a growing concern over the [vulnerability](https://www.contrastsecurity.com/security-influencers/java-serialization-vulnerability-threatens-millions-of-applications) discovered with the default implementations of the Java’s readObject(), writeObject() methods, prompting the developer and expert community to look into all platforms supporting such implementations and relaying their concerns to the respective solution providers. Oracle was included in that list, as a provider for WebLogic - [CVE-2015-4852](https://nvd.nist.gov/vuln/detail/CVE-2015-4852). In April 2018, Oracle was to release a Critical Patch Update in response to [CVE-2018-2628](https://nvd.nist.gov/vuln/detail/CVE-2018-2628).

### Install the Critical Patch Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<http://www.oracle.com/technetwork/security-advisory/cpuapr2018-3678067.html>.

This is a Java deserialization vulnerability in the core components of the WebLogic server and, more specifically, it affects the T3 proprietary protocol. This update includes the following WebLogic platforms:

• 10.3.6.0

• 12.1.3.0

• 12.2.1.2

• 12.2.1.3

System administrators are being instructed to patch their application servers prior to going live. For more information please consult Doc ID 1470197.1 from the Oracle support site (Oracle Support Account is needed):

<https://support.oracle.com/epmos/faces/DocumentDisplay?_afrLoop=292702667580600&id=1470197.1&_adf.ctrl-state=zyhqyrlxq_62>

### Extend the blacklists

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of this patch will provide an opportunity for the system administrators to utilize the blacklists already in place, as well as extend the serialization blacklists. For more information please refer to the following Oracle guide:

<https://docs.oracle.com/javase/10/core/serialization-filtering1.htm#JSCOR-GUID-3ECB288D-E5BD-4412-892F-E9BB11D4C98A>

In addition, the following instructions will help configure a domain in a way that will ensure encryption of all traffic between the domain controller and the managed servers.

### Set up SSL on a WebLogic Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.Obtain an identity (private key and digital certificates) and trust (certificates of trusted certificate authorities) for WebLogic Server. Use the digital certificates, private keys, and trusted CA certificates provided by the WebLogic Server kit, the CertGen utility, Sun Microsystem's keytool utility, or a reputable vendor such as Entrust or Verisign to perform this step.

2.Store the identity and trust. Private keys and trusted CA certificates which specify identity and trust are stored in a keystore.

> **NOTE:** This release of WebLogic Server supports private keys and trusted CA certificates stored in files, or in the WebLogic Keystore provider for the purpose of backward compatibility only.

3.Configure the identity and trust keystores for WebLogic Server in the WebLogic Server Administration Console. See "Configure Keystores" in the Administration Console Online Help.

4.Set SSL configuration options for the private key alias and password in the WebLogic Server Administration Console. Optionally, set configuration options that require the presentation of client certificates (for two-way SSL). See "Configure SSL" and "Configure two-way SSL" in the Administration Console Online Help.

> **NOTE:** When starting a WebLogic Server instance, you can specify the command line argument -Dweblogic.security.ssl.nojce=true to use a FIPS-compliant (FIPS 140-2) crypto module.

*This page is left blank intentionally.*

# Deploying VistALink Adapters on J2EE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## RAR Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On J2EE systems, J2CA-compliant adapters, such as VistALink, are deployed in Resource Adapter Archive (RAR) files. RAR files are analogous to Enterprise Archive (EAR) files and Web Archive (WAR) files, except that they are exclusively for resource adapters (J2CA connectors).

|                                                                                                                |                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/005.png) | NOTE: Oracle (formerly known as BEA) recommends that RARs be deployed in exploded format. |

Deployment characteristics of VistALink RARs running in WebLogic domains:

- VistALink adapters are meant to be deployed as standalone J2CA adapters, e.g., independent of individual J2EE applications.
- For a J2EE application to use a VistALink adapter, the adapter must be running in the same Jave Virtual Machine (JVM) as the J2EE application.
- If a J2EE application using VistALink is targeted to multiple WebLogic servers, so must the VistALink adapter(s) it is using.
- A single VistALink adapter deployment can target multiple WebLogic servers in a domain.
- A VistALink adapter runs individually on each server it is targeted to; it is not aware of itself running on other servers in the domain.
- There are no cluster-aware features or configuration settings for standalone J2CA adapters such as VistALink in WebLogic. In particular, there is no:
- failover across servers
- load-balancing across servers

The configurable settings for deployment of any VistALink adapter are contained in the following locations:

- weblogic-ra.xml: contains WebLogic-specific deployment descriptor configuration settings (such as initial and maximum pool sizes) and Java Naming and Directory Interface (JNDI)-related properties that must be modified for each adapter, to distinguish one adapter from another in JDNI.
- VistALink configuration file: contains VistALink-specific configuration settings, such as access and verify codes for the connector proxy user. The VistALink configuration file contains settings for *all* deployed VistALink connectors. It is in a single location on a given server, in a folder that the deployer places on the server's classpath.

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/006.png) | NOTE: With the deployment descriptor templates provided with VistALink 1.6.1, in most case the ra.xml deployment descriptor does not need to be modified. |

### Summary of RAR Changes Since Previous Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- vljFoundationsLib and vljConnector jars: New versions provide a J2CA 1.5 compliant adapter implementation.
- Deployment Descriptor Changes: The format of both the ra.xml and weblogic-ra.xml descriptors are different. Existing adapters' deployment descriptors need to be updated. Using the provided sample/template descriptors, only weblogic-ra.xml will need to be modified when creating a VistALink RAR:
  - META-INF/ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. In most cases, it no longer needs any further editing when creating a RAR.
  - META-INF/weblogic-ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. It must be edited for each RAR deployed.
  - META-INF/MANIFEST.MF: The template version provided in the VistALink distribution is updated to support use of J2EE Shared Libraries by RARs.
- lib/saxpath.jar, lib/jaxen-core.jar, and lib/jaxen-dom.jar are no longer needed in the RAR as their functionality has been replaced by the XPath implementation introduced in Java 5.
- lib/xbean.jar no longer needed in the RAR since an implementation of XML Beans is included in WebLogic 10.3.6/12.1.2
- Linked adapters (link-ref mechanism) no longer supported for VistALink 1.6 adapters
- Development System Classloading: Automatic classloading of all jars in RAR is now supported by WebLogic 10.3.6/12.1.2. Library jars included in RAR no longer need to be manually added to the server classpath.
- Production System Classloading: Oracle recommends removing all jars from RARs on production systems, and deploying them as J2EE shared libraries instead (to reduce resource consumption – replacement for resource-saving aspect of the 8.1 link-ref mechanism). When deployed as J2EE shared libraries, the jars supporting VistALink RARs no longer need to be manually added to the server classpath.

|                                                                                                                |                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/007.png) | NOTE: VistaLink 1.6.1 is upgraded to be a J2CA 1.5-compliant adapter, and runs in WebLogic 10.3.6/12.1.2. The previous version of VistALink (1.5) implemented the J2CA 1.0 standard, and runs in WebLogic 8.1. |

## Creating a RAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Exploded 1.6.1 RAR Layout, Production Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recommended contents of an exploded VistALink RAR folder, for production systems, are:

> (root) empty

> META-INF\\ - MANIFEST.MF (contains information needed to use J2EE Shared Libraries)

> \- ra.xml (J2EE standard Deployment Descriptor)

> \- weblogic-ra.xml (WLS-specific Deployment Descriptor)

The app-J2EE\Rar-Prod-Template directory in the VistALink distribution zip provides an exploded RAR in this structure.

|                                                                                                                |                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/008.png) | NOTE: On production systems, Oracle recommends that the supporting libraries (JAR files) be deployed as J2EE shared libraries to minimize the consumption of server resources (hence the recommended exploded RAR for a production system contains only deployment descriptors). |

### Exploded 1.6.1 RAR Layout, Non-Production Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recommended contents of an exploded VistALink RAR folder, for non-production systems, are:

> (root) Main VistALink libraries:

> \- vljConnector-1.6.1.jar

> \- vljFoundationsLib-1.6.1.jar

> lib\\ Supporting libraries:

> \- log4j-api-2.10.0.jar

> \- log4j-core-2.10.0.jar

META-INF\\ - MANIFEST.MF (a required RAR artifact)

\- ra.xml (J2EE standard Deployment Descriptor)

> \- weblogic-ra.xml (WLS-specific Deployment Descriptor)

The app-J2EE\Rar-Dev-Template directory in the VistALink distribution zip provides an exploded RAR in this structure.

|                                                                                                                |                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/009.png) | NOTE: Libraries contained in RARs are automatically loaded onto a high-level classloaders, and are thus available to other deployed applications (EARS, WARs, etc) running in the same Java Virtual Machine (JVM). |

### Deployment Descriptor: ra.xml

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A template ra.xml version is provided in the VistALink distribution zip file, in each of the example rar folders. It has been updated to be compatible with 1.5 of the J2CA specification.

In most cases, you can copy this template ra.xml deployment descriptor as-is from the VistALink example RAR for all your RARs, with no further need to edit it.

> \<?xml version="1.0" encoding="UTF-8"?\>

> \<connector xmlns="http://java.sun.com/xml/ns/j2ee" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://java.sun.com/xml/ns/j2ee http://java.sun.com/xml/ns/j2ee/connector_1_5.xsd" version="1.5"\>

> \<description\>J2M VistALink adapter that allows RPC execution from Java/J2EE to

> M/VistA\</description\>

> \<display-name\>VistaLinkAdapter\</display-name\>

> \<vendor-name\>Foundations\</vendor-name\>

> \<eis-type\>VistA\</eis-type\>

> \<resourceadapter-version\>1.6\</resourceadapter-version\>

> \

- Non-production systems: Copy the contents of the app-J2EE\Rar-Dev-Template folder from the VistALink zip distribution to the new RAR folder.
3.  Edit the weblogic-ra.xml deployment descriptor in the new RAR, to have the appropriate JNDI names.

## VistALink Connector Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink-specific resource adapter (connector) settings are stored in a separate, host-file-system-based connector configuration file, named gov.va.med.vistalink.connectorConfig.xml. You can edit this file manually or using the Configuration Editor (see the section "Configuration Editor").

The rules for the VistALink configuration file are:

- The file must be named "gov.va.med.vistalink.connectorConfig.xml".
- The file must be placed in a folder that is on the ‘java’ classpath of the JVM of each WebLogic server instance deploying VistALink connectors.
- Because the gov.va.med.vistalink.connectorConfig.xml file holds login credentials for accessing VA VistA systems, it must be protected. On Linux systems, access to the folder containing the file should be restricted to the account or group under which WebLogic runs. Access to the host file system should be protected on all J2EE systems.

When the server deploys a VistALink connector, the connector does the following:

1.  Gets the connectorJndiName property value from weblogic-ra.xml deployment descriptor.
2.  Loads gov.va.med.vistalink.connectorConfig.xml, via the server ‘java’ classpath.
3.  Looks in the VistALink configuration file for a \<connector\> entry with a matching jndiName attribute.
4.  Uses the settings from the matching entry (ip, port, access-code, verify-code, etc.) to configure the connector.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-system-management-guide/010.png)</td>
<td><strong>NOTE:</strong> Although you can manually edit the VistALink configuration file, a Configuration Editor UI is provided as part of the VistALink console (see the "<br />
Configuration Editor." section in the <em>VistaLink Administration Console</em> chapter.)</td>
</tr>
</tbody>
</table>

### Connector Entry Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink configuration file should contain one \<connector\> entry per connector module/adapter that you will deploy to your J2EE server. Each entry should have a unique jndiName. Each \<connector\> entry describes the characteristics of the M listener that a particular connector module/adapter will connect to.

The following example shows the format of the VistALink configuration file (with a configuration of a single listener):

\<?xml version="1.0" encoding="UTF-8"?\>

\<connectors encryptionScoped="false" <span class="mark">  
</span>xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>"  
xsi:noNamespaceSchemaLocation="connectorConfig.xsd"  
xmlns="<http://med.va.gov/vistalink/adapter/config>"

\>

\<connector

jndiName="vlj/SiouxFalls438"

primaryStation="438"

ip="test.somewhere.va.gov"

port="8000"

access-code="joe.123"

verify-code="ebony.432"

timeout="30"

always-use-default-as-min="false"

enabled="true"

/\>

\</connectors\>

<span id="_Toc198960649" class="anchor"></span>Figure 2‑3. VistALink Configuration File Format Example

### Connector Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration file should contain one or more \<connector\> elements (entries) inside the top-level \<connectors\> element.

The basic settings for each \<connector\> entry are as follows:

- jndiName (required): Uniquely identifies each entry. Should be the same JNDI name as you will specify in the weblogic-ra.xml descriptor for your connector. This setting is also used to create the JNDI half of the mappings between station numbers and connector JNDI names.

|                                                                                                                |                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/011.png) | NOTE: The value must start with an alphanumeric character, and following that can contain only alphanumeric plus the following punctuation characters: - \_ / ( ) \[ \] |

- primaryStation (required): Station number of the M/Kernel system connected to. VistALink’s institution mapping functionality maps this station number to the connector's JNDI name, so the application can retrieve the connector by the station number. This entry is checked against the DEFAULT INSTITUTION field (#217) of the KERNEL SYSTEM PARAMETERS file (#8989.3) at runtime, when connections are made.
- ip (required): IP address of the M VistALink listener to connect to (either numeric or mnemonic).

|                                                                                                                |                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/012.png) | NOTE: When entering ip information in numeric, make sure all the outbound network adapters are configured with Reverse-DNS information. Otherwise you’ll see Connectivity Errors, as VistALink will not connect on the un-validated IP information |

- port (required): Port of the M VistALink listener to connect to.
- access-code and verify-code (required): The access and verify code credentials for the connector proxy user to connect to the M VistALink listener.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-system-management-guide/013.png)</td>
<td><p><strong>NOTE:</strong> When entering access and verify codes directly in the config file (not using the configuration editor), if the codes contain the following special characters, they need to be entered as follows:</p>
<blockquote>
<p><u>special char</u>    <u>enter as</u></p>
<p>    &lt;           &amp;lt;<br />
    &amp;           &amp;amp;<br />
    "           &amp;quot;</p>
<p>    '           &amp;apos;</p>
</blockquote>
<p>or alternatively, use the configuration editor.</p></td>
</tr>
</tbody>
</table>

- encrypted (optional): true \| false. When the access/verify codes are encrypted by VistALink, this attribute is set to true. If you need to manually (outside the configuration editor) update the access / verify code, however, set "encrypted" to false so that VistALink will know the access/verify code is not encrypted.
- enabled (required): true \| false. If false, the connector will not deploy. Use this attribute primarily to retain inactive configurations in your configuration file.
- timeout (optional): Sets the default span of time in seconds socket will wait for response from M (e.g., waiting for an RPC to execute) and after which connection is automatically terminated.

### Advanced Connector Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- always-use-default-as-min: If true, the default timeout will be the lowest timeout value allowed for this connector; it will override any programmatically specified lower value set by an application.
- timestamp: When a connector entry is edited, the configuration editor automatically stamps the entry with a timestamp.

### File-Wide Setting: encryptionScoped

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- encryptionScoped: This attribute should not be edited directly, and instead should be modified only when using the VistALink administration console to modify the encryption type for all configuration file entries. The file-wide \<connectors\> attribute "encryptionScoped" reflects whether entries have been encrypted with domain-scoped encryption or not. If domain scoped, the domain name is included in the encryption, making it difficult to use encrypted values on other WebLogic domains.

### Obsolete Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- primaryStationSuffix: This attribute has been eliminated. Any primary station numbers requiring an alpha suffix, should instead be entered as part of the "primaryStation" attribute, i.e., primaryStation="200M". Note: If VA institution rules are being used, only 200-series (Austin Information Technology Center) station numbers can have alpha suffixes for the <u>primary</u> station number.

## Deploying J2EE Shared Libraries for VistALink (Production Systems Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/014.png) | REF: To minimize the consumption of server resources, Oracle recommends that supporting libraries for RARs should be deployed as J2EE Shared Libraries, on production systems. |

On production systems only, prior to deploying any VistALink RARs, you should install the following jars as J2EE shared libraries:

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
<td><p>log4j-api-2.10.0.jar</p>
<p>log4j-core-2.10.0.jar</p></td>
<td><p>log4j-1</p>
<p>log4j-2</p></td>
</tr>
</tbody>
</table>

To deploy a jar as a shared library (Production Systems):

1.  Place the jar in a folder location accessible on the admin server.
2.  Log on to the WebLogic console.
3.  Select Lock & Edit so you can modify the domain configuration.
4.  Navigate to the Deployments page.
5.  Click Install. Navigate to the jar, select it and click Next.
6.  Choose the server(s) to target. Choose all servers that you will be deploying VistALink RARs on, and click Next.
7.  Leave the Name value as-is, and click Finish.
8.  Click Activate Changes to complete the deployment.

## Deploying a RAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each M system you want your J2EE system to connect to, you need to create and deploy a separate VistALink RAR (exploded or packaged). Each RAR contains two deployment descriptors, ra.xml and weblogic-ra.xml. These need to be configured with the unique settings that describe how the adapter should be deployed on the J2EE system and how it should connect to a specific M system.

To deploy a new VistALink adapter:

1.  If you are deploying to a production system, ensure that you have deployed the necessary supporting libraries for VistALink as J2EE Shared Libraries before proceeding any further.
2.  Create the RAR (see *Creating a RAR* section above).
3.  Add an entry in the gov.va.med.vistalink.connectorConfig.xml file for the new adapter, on all servers that the connector will be deployed on. Its jndiName attribute should match the values used in weblogic-ra.xml in the \<connection-instance\> section, for \<jndi-name\> and connectorJndiName (see *VistALink Connector Configuration File* section above).
4.  Propagate the updated gov.va.med.vistalink.connectorConfig.xml file to all servers in the domain hosting VistALink adapaters.
5.  Use WebLogic to target and deploy the new RAR to one or more servers.
6.  Verify that the new adapter is working correctly on each targeted server, using the VistALink administration console (see *[The VistALink Administration Console](#the-vistalink-administration-console)* for more information).

> Even though the adapter may deploy successfully from WebLogic's point of view, the test for configuration completion is whether the adapter can successfully connect to the M system.

## Updating Already-Deployed Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you update an adapter setting in the VistALink configuration file, weblogic-ra.xml, or ra.xml, you do not need to bounce the server to activate the changed setting. It is sufficient to *update* the adapter in the WebLogic console to make the changed setting(s) active.

|                                                                                                                |                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/015.png) | NOTE: While the adapter is being updated, it may be briefly unavailable to applications. |

To update an adapter:

1.  Log on to the WebLogic console.
2.  Select Lock & Edit so you can modify the domain configuration.
3.  Navigate to the Deployments page.
4.  Select the adapter to update and click Update. Complete the steps necessary to finish the update.
5.  Click Activate Changes.
6.  Verify that the adapter state is Active.
7.  Verify that the updated adapter is working correctly using the VistALink administration console (see "*The VistALink Administration Console*" section for more information).

## DNS Updates and VistALink Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the value of the "Ip" property used to configure a VistALink 1.6 (and up) adapter's destination M system is a domain name, then DNS updates to the IP address corresponding to that DNS name *can* be received dynamically/automatically by the adapter, with a few caveats. This is a change from previous versions of VistALink. The caveats are:  

 

1.  The JVM's "cache forever" setting may force DNS lookup caching at the JVM level. For VistALink adapters to receive DNS updates dynamically, the JVM must be configured to turn off DNS caching. Otherwise, the JVM will resolve the DNS name once, at deployment, and cache that name until the next time the JVM restarts.

> This setting is usually controlled by the "networkaddress.cache.ttl" JVM property in the java.security file, in the lib/security subdirectory of the JRE used for WebLogic. For example:

> \# The Java-level namelookup cache policy for successful lookups:  
> \#  
> \# any negative value: caching forever  
> \# any positive value: the number of seconds to cache an address for  
> \# zero: do not cache  
> \#  
> \# default value is forever (FOREVER). For security reasons, this  
> \# caching is made forever when a security manager is set.  
> \#  
> \# NOTE: setting this to anything other than the default value can

> \# have serious security implications. Do not set it unless

> \#       you are sure you are not exposed to DNS spoofing attack.

> \#

> \# networkaddress.cache.ttl=-1

> In order to disable JVM-level DNS caching, the "networkaddress.cache.ttl" property must be uncommented for the JRE used by WebLogic, for all servers in the domain, and set to some value of 0 or greater.

|                                                                                                                |                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/016.png) | NOTE: The "Java Home" value may need to be explicitly set in the "Configuration \| Server Start" page for each server in the domain (use the WebLogic console), in order for the change in java.security to be picked up. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/017.png) | NOTE: Assuming servers running VistALink are running inside a secure intranet, the security risk of disabling DNS caching is low (if an organization is using DNS at all to dynamically update internal IP addresses, then it has presumably already evaluated the risk to be acceptable.) |

2.  Existing connections in the connection pool remain connected to previous destination. If the DNS is updated, existing open connections to the previous DNS-resolved system will remain until those connections close. The M-side "J2EE Connection Timeout" setting in the M-side VistALink site parameters file determines life of inactive connections. Since the current recommended value is 1 day, even inactive connections could stay open to the former destination for quite some time, and if connections are used, they could stay open even longer.  
    >   
    > Some strategies to ensure existing connections are terminated when DNS is changed for the M system include:
- If the M system at the old address is shut down, all open connections are terminated automatically.
- If the M system manager kills all existing VistALink connections, this will remove any old connections from pool (if won't disrupt service to remaining VistALink clients, if any).
- On the J2EE side, if the J2EE system manager 1) stops the adapter, and 2) updates the adapter, this will shut down the pool and all old connections.

## Pool Size Management/Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pool size management is a key factor in enhancing VistALink’s performance on a J2EE server (and minimizing its impact on M servers). It is costly to have either too many unused open connections or not enough for incoming requests. Connection pool sizing will be part of the art of system tuning in a Health*<u>e</u>*Vet-VistA environment.

On the WebLogic server, you can use the WebLogic console and the weblogic-ra.xml deployment descriptor to control the characteristics of the connection pool for each deployed resource adapter.

Key settings include:

- Initial Capacity: The number of connections to create for the connection pool. Pool creation happens on initial deployment and on server startup. Higher numbers for this setting can add additional time to the server startup process.
- Max Capacity: The high point of expansion for the connection pool. You may want to set this based on the highest load you can place on the M system you are connected to (potential work as well as license slot usage). On the J2EE side, if all connections are in use and the Max Capacity setting is reached, applications requesting a connection will be thrown a ResourceException.
- Shrinking Enabled and Shrink Frequency Seconds: This allows pools to shrink when the number of requests has slowed down and created connections are inactive for a given set of time. Enabling shrinking is recommended in most cases, to reduce the number of inactive connections using license slots on M systems.

# Configuring log4j Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink Java code base has been instrumented with log4j 2 logging statements. log4j is an open-source logging package distributed under the Apache Software license.

It can be helpful in debugging and troubleshooting to review the output information contained in the log files produced at runtime. System administrators can configure log4j to log either VistALink errors only or VistALink errors with debug information.

|                                                                                                                |                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/018.png) | REF: Learn more about the log4j tool at: <u>https://logging.apache.org/log4j/2.x/manual/configuration.html</u> |

## log4j Configuration Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A log4j configuration file contains:

- appender entry(s): Configuration entries describing the destinations for logging information
- logger entry(s): Configuration entries describing the level specific information will be logged. Loggers are typically organized by Java package and class name.

The configuration file is used by log4j to set up a JVM-wide logging configuration. Because this configuration spans applications, Health*<u>e</u>*Vet-VistA applications do not control logging configurations individually. Instead, a single log4j configuration file must be set up with the logging configuration for all Health*<u>e</u>*Vet-VistA applications running on a particular JVM.

## Configuring log4J

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Currently, we recommend the following steps for configuring log4j:

1.  Create a single file named "log4j.xml" to hold the loggers and appenders for all Health*<u>e</u>*Vet-VistA applications on your J2EE system.
2.  Add in all the appender elements required to set up as many logging destinations as you need for your system.
3.  Add in all the logger elements required to configure logging for your Health*<u>e</u>*Vet-VistA applications running on your server. (VistALink provides a list of available loggers, which you can use to configure logging coming from VistALink classes.)
4.  Place this file in a Health*<u>e</u>*Vet-VistA configuration folder on your J2EE server JVM classpaths.

> The purpose of the folder is to hold configuration files for all Health*<u>e</u>*Vet-VistA applications, including VistALink.

If you perform steps 1-4 above, log4j will find the log4j.xml file on your server classpaths, and will be able to establish a JVM-wide log4j logging configuration for all applications running in the JVM.

### Alternative Approach

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Alternatively, you can place a log4j configuration file on the file system and pass its name and location as the log4j.configurationFile system property to the JVM at startup. This file does not need to be on the JVM classpath.

The following example shows how to start a JVM with a log4j configuration stored in a non-log4j.xml file, in a folder that is not on the server classpath:

> \<JAVA_HOME\>\bin\java -Dlog4j.configurationFile=file:///c:/localConfigs/mylog4j.xml

## Sample log4j Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the log4j configuration file, the system administrator can do *one* of the following:

- Use the information above to add to an overall log4j configuration file
- Copy one of the sample log4j configuration files provided in the VistALink distribution zip file or
- Just copy some of the logger elements in the sample files.

The sample log4j configuration files can be located in the log4j directory inside the VistALink distribution zip file. There are two sample log4j configuration files:

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>log4jSampleJ2EEConfig.xml</td>
<td><p>Example configuration for a J2EE system, turning DEBUG-level logging on for VistALink classes of interest on a J2EE system.</p>
<p><strong>Note:</strong> Turning on ‘debug’ level can adversely affect system performance.</p></td>
</tr>
<tr class="odd">
<td>log4jSampleJ2SEConfig.xml</td>
<td>Example configuration for a J2SE (Java client-M server) application, turning DEBUG-level logging on for VistALink classes of interest for client/server applications.</td>
</tr>
</tbody>
</table>

<span id="_Toc198960650" class="anchor"></span>Figure 3‑1. Sample log4j configuration files

The following is a simple log file example with one appender element, two logger elements and a root logger, reduced from "log4jSampleJ2EEConfig.xml":

\<?xml version="1.0" encoding="UTF-8"?\>

\<Configuration status="all"\>

\<Appenders\>

\<Console name="Console" target="SYSTEM_OUT"\>

\<PatternLayout pattern="%d{HH:mm:ss.SSS} \[%t\] %-5level %logger{36} - %msg%n"/\>

\</Console\>

\</Appenders\>

\<Loggers\>

\<Logger name="gov.va.med" level="all" additivity="false"\>

\<AppenderRef ref="Console"/\>

\</Logger\>

\<Root level="all"\>

\<AppenderRef ref="Console"/\>

\</Root\>

\</Loggers\>

\</Configuration\>

<span id="_Toc522197346" class="anchor"></span>Figure 3‑2. Log4j configuration file example

## VistALink Core log4j Categories

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink core log4j categories are documented in the spreadsheet provided in the log4j subdirectory of the VistALink distribution file.

To obtain a full log4j logger category name for a given package and class, concatenate the package with the class. For example, the logger for: gov.va.med.vistalink.adapter.spi (package) and VistaLinkManagedConnection (class) is gov.va.med.vistalink.adapter.spi.VistaLinkManagedConnection.

Each logger category provides a description and notes the supported logger levels (e.g., DEBUG and ERROR). You can then use the logger category name(s) to set up loggers in your log4j configuration files to log information from specific parts of the VistALink package, as needed.

# Institution Mapping 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications using VistALink need the ability to select the resource adapter (connector) to execute a remote procedure call (RPC) on a given M system. On the J2EE side, the way to retrieve a connector is with a Java Naming and Directory Interface (JNDI) name. The institution, station, and division number are the pieces of information an application is likely to have to identify an M system it wants to connect to. Applications should not have to hard-code connector JNDI names; in most cases they should get the appropriate connector using a station number.

## Managing the Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PrimaryStation Attribute (VistALink Configuration File)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primaryStation attribute for connector entries in VistALink's configuration file provide the mapping between connector JNDI names and VistA station numbers. The (required) primaryStation attribute of the \<connector\> element links a particular connector (identified by its JNDI name) with a particular station number.

In the following configuration file example, station number "11000" (and its descendants "11000A," "110000B," etc.) are mapped to the JNDI name "vlj/testconnector":

\<?xml version="1.0" encoding="UTF-8"?\>

\<connectors encryptionScoped="false" <span class="mark">  
</span>xmlns:xsi="<http://www.w3.org/2001/XMLSchema-instance>"  
xsi:noNamespaceSchemaLocation="connectorConfig.xsd"  
xmlns="http://med.va.gov/vistalink/adapter/config"

\>

\<connector

jndiName="vlj/testconnector"primaryStation="11000"

ip="test.somewhere.va.gov" port="8000" access-code="joe.123" verify-code="ebony.432" timeout="30" always-use-default-as-min="false" enabled="true"

/\>

\</connectors\>

<span id="_Toc198960652" class="anchor"></span>Figure 4‑1. Institution Mapping Association in VistALink Configuration File

Assuming the above connector is deployed on a given server, when an application asks for the JNDI name for the connector for station 11000A, it will be returned the string "vlj/testconnector."

### How the Mapping Is Initialized

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Institution mapping is per JVM in-memory cache, based on the settings configured by the administrator in the VistALink configuration file. It is initialized when the first connector is deployed to a given server. The mappings for each connector are added in when each connector deploys. If multiple servers have connectors deployed, each server has its own copy/version of the in-memory cache.

### Viewing the Current Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view the current set of institution-to-station number mappings on any server, use the VistALink administration console on your WebLogic administration server (if deployed). For more information see [Monitoring Institution Mapping](#monitoring-institution-mapping) in the section *The VistALink Administration Console*.

### Updating Institution Mappings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mappings are loaded automatically for a connector whenever the connector is deployed. If a previous connector has been mapped to the same station number, a "last one in wins" strategy is employed, and a warning-level logger entry is logged.

Mappings are marked for removal when a connector is undeployed. The actual removal of the mappings does not happen until garbage collection runs on the server. If garbage collection has not run and a mapping is used to retrieve the JNDI name of an undeployed connector, the attempt to use of the connector will fail at the point the application attempts to retrieve the connection factory from JNDI. If garbage collection *has* run, the attempt to use of the connector will fail when no JNDI name can be returned for the given station number.

### How Applications Use Institution Mappings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications are provided with an Application Program Interface (API) to retrieve a connector's JNDI name, based on a station number. For more information, see the *VistALink 1.6 Developer Guide*.

## Troubleshooting Institution Mapping Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Out-of-Synch Configuration Files on Multiple Physical Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink configuration file (gov.va.med.vistalink.connectorConfig.xml) must be accessible on the JVM classpath of each server with deployed VistALink connectors. Because separate copies of the VistALink configuration file can exist for separate physical servers, it is possible that these copies may not be identical. The primaryStation attributes, on which the institution mapping is based, may be different.

It is the responsibility of the system administrator to keep separate physical copies of the VistALink configuration file synchronized.

### Connector Station and M System Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primaryStation attribute is used to create the mappings that applications use to retrieve the connector. It is always possible to misconfigure a connector, associating it with the wrong station number. Station mismatch checking is employed to catch such configuration errors.

When VistALink connects to an M system, the primaryStation attribute of the connector is passed to M. It is then checked against the DEFAULT INSTITUTION field (#217) of the KERNEL SYSTEM PARAMETERS file (#8989.3). If it doesn't match, the connection is rejected, and a SecurityPrimaryStationMismatchException is returned to the application.

The system administrator should monitor the VistALink administration console and log files for indicators of rejected connections due to primary station mismatches.

### JNDI Name Configuration Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The jndiName attribute in the VistALink configuration file is used to associate a station number with a particular connector. However, the JNDI name under which WLS deploys the connector comes from the \<jndi-name\> element in the weblogic-ra.xml file. If these two values don't match, the mapping will not reflect the correct JNDI name for the connector.

Runtime checking validates whether these values are the same. If they are not, attempts to use the connector will return a VistaLinkResourceException to the application. In addition, the VistALink administration console will display a warning if it sees these values do not match for a given connector.

The two JNDI settings are in the weblogic-ra.xml deployment descriptor and the gov.va.med.vistalink.connectorConfig.xml file. When these settings are out of synch, the result should be an unusable connection (outright failure), rather than an incorrectly routed connection, which is harder to diagnose.

The system administrator should monitor the VistALink administration console and log files for indicators of rejected connections due to JNDI name mismatches.

### Mappings with Undeployed Connectors (Stopped or Deleted)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mappings are marked for removal when a connector is undeployed. However, the actual removal of the mappings does not happen until garbage collection runs on the server.

If a connector has been undeployed and garbage collection has not yet run, the attempted use of the connector will fail at the point the application attempts to retrieve the connection factory from JNDI. If garbage collection has run, the attempted use of the connector will fail when no JNDI name can be returned for the given station number. In both cases, the attempt to use the undeployed connector will fail.

## Pluggable Institution Mapping Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                |                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/019.png) | NOTE: This section is of interest primarily to non-VA users of VistALink. |

The implementation of institution mapping used on the J2EE side of VistALink contains rules with several VA-specific assumptions, in particular:

- Legal station numbers in VA can be 3 digits or 5+ digits with one exception (see nursing homes below).
- For station numbers assigned to the Austin Information Technology Center (AITC) only: If a station number has an alpha suffix, e.g. "200A", the numeric portion must be "200"
- For nursing homes: If a numeric station number is 4 digits, the 4th digit must be a "9"

In order to facilitate use of VistALink outside of VA, the implementation of these VA rules has been placed into a pluggable PrimaryStationRules implementation. By default, the VA-specific implementation of the station number rules is used when working with station numbers on the J2EE side. However, to have VistALink use a different rule implementation in place of the default VA-specific one:

- A new implementation of the IPrimaryStationRules interface must be provided, and
- The package/classname of the new implementation must be passed in a -D JVM argument, "gov.va.med.vistalink.primary-station-rules-class". E.g., pass -Dgov.va.med.vistalink.primary-station-rules-class=org.test.PrimaryStationRulesTest

|                                                                                                                |                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/020.png) | REF: For more information on implementing a non-VA-specific institution rules class, see the *Developer's Guide*. |

# The VistALink Administration Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink administration console runs in two modes depending on installation: either as an extension in the WebLogic console, or as a standalone Web application. In both cases, the VistALink administration console runs on the administration server for a given WebLogic configuration. It provides the following functionality:

- Monitor Connector Status (per server)
  - Connector summary list with health indicators, status
  - Connector detail, including a live call to M system
  - Institution mapping association list
- Configuration Editor (admin server only)
  - Edit connector configurations in VistaLink connector configuration file

## Monitor Role Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WebLogic’s console supports four roles: Administrators, Deployers, Operators and Monitors. The 1.6 VistALink administration console restricts users in the Monitors role to read-only access. Users in the Monitors role can monitor connector status, but are restricted from using the Configuration Editor.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/021.png) | NOTE: To support access by users in the Monitors role, the system administrator currently needs to explicitly declare the "Listen Address" attribute in the WebLogic domain configuration, for each server in the domain. Otherwise a JMX remoting call that is needed, fails, under Monitor privileges alone. |

## Accessing the VistALink Administration Console

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistALink Administration Console as Standalone Web Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If installed as a standalone Web application, you can access it at the following URL:

> http://\<admin server\>:\<port\>/vlconsole

You’ll be prompted for a user name and password. Use the same credentials as you would use to login to the WebLogic administration console. From that point on, the standalone VistALink console application will look almost identical to the console extension plug-in version (except it will not have the WebLogic console content displayed on the left and top.).

![](vistalink-version-1-6-system-management-guide/022.png)

<span id="_Toc522197348" class="anchor"></span>Figure 5‑1. Standalone VistALink 1.6 Administration Console

|                                                                                                                |                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/023.png) | NOTE: On WebLogic 10.3/12c, the VistALink administration console works best when installed as a standalone application. |

### VistALink Administration Console as WebLogic Console Extension

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If installed as an extension in the WebLogic console, access the VistALink console extension as part of the main WebLogic console. Within the WebLogic console, the VistALink console extension can be found in two locations:

- As a tab (‘VistALink J2M’) in the WebLogic console’s domain page
- As a link (‘VistALink J2M’) in the WebLogic console’s navigation tree, under ‘Environment’

|                                                                                                                |                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/024.png) | NOTE: On WebLogic 10, only the tab in the WebLogic console’s domain page may be available. The link in the console’s navigation tree may not be displayed. |

Figure 5‑2 shows two ways to access the VistALink administration console when installed as a WebLogic console extension.

> ![](vistalink-version-1-6-system-management-guide/025.png)

<span id="_Ref193180563" class="anchor"></span>Figure 5‑2. VistALink Administration Console: Access via *link* in navigation tree and *tab* in domain tab set

## Monitoring Connector Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To monitor connector status, pick a server in your domain from the list of servers on the main VistALink Administration console page. You can then monitor various attributes of the VistALink adapter(s) deployed on that server.

### Adapter List/Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the first page after selecting a server, Figure 5‑3, you’ll be shown a list of VistALink adapters on the server, including health indicators and other summary information for each:

- Deployed JNDI Name: The JNDI name under which the adapter has been deployed and made available to other applications
- JNDI Mismatch: Indicates that the JNDI name used to look up the connector settings in the VistALink configuration file (from the “connectorJndiName” custom property value in weblogic-ra.xml) does not match the deployed JNDI name used by the container to deploy the connector, which could indicate a misconfigured connector.
- Health Indicators/Failure Counts:
  - Conn Socket: The number of times, since deployment or server re-start, that an attempt to create a physical connection to the M system has failed.
  - Conn Auth: The number of times, since deployment or server restart, that the connector has attempted and failed to log on to the M system with the connector user access/verify code.
  - Prod Mismatch: The number of times since deployment or server restart that the connector has attempted to log on to the M system and found a mismatch between the Production settings for the M system and the J2EE server's JVM. On the J2EE server, this setting is controlled via the gov.va.med.environment.production JVM argument.
  - Div Mismatch: The number of RPC requests since deployment or server restart that have failed because the division specified in the RPC request is not legal for the re-authentication user. A large number of division mismatches may indicate a misconfigured JNDI-to-institution mapping for the connector in question.
  - Re-Auth: The number of times since deployment or server restart that re-authentication has failed when attempting to execute RPCs on behalf of users. A large number of failures may indicate a misconfigured JNDI-to-institution mapping for the connector in question.
- M System Info: The IP address and port used to connect to the M system configured for the adapter.
- Deployment State: The deployment state of the adapter on the J2EE system.

> ![](vistalink-version-1-6-system-management-guide/026.png)

<span id="_Ref193181225" class="anchor"></span>Figure 5‑3. Connector Summary List

### Adapter Detail

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you click on the “Deployed JNDI Name” link for any adapter on the summary page, you’ll access a detail page, Figure 5‑4 and Figure 5‑5, with more information for the connector:

- WebLogic-specific configuration information
- VistALink-specific configuration information
  - including institution mappings associated with the connector
- Health monitoring indicators
- Performance monitoring indicators
- Live VistALink M/VistA Server Query, including (from M):
  - M VistALink version
  - “Connector Proxy” user name from the New Person file
  - UCI/volume/box-volume pair of the M account
  - Domain, Institution and Test/Production setting of the M account
  - Introductory Text (for visual confirmation of correct system)

|                                                                                                                |                                                                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/027.png) | NOTE: When the detail page is loaded for any connector, a "live" call is made to the M system. The results provide an easy way to get a picture of the M system connected to, and may also help verify whether a connector is reaching the *intended* M system. |

> ![](vistalink-version-1-6-system-management-guide/028.png)

<span id="_Ref193181273" class="anchor"></span>Figure 5‑4. Connector Detail, 1 of 2

> ![](vistalink-version-1-6-system-management-guide/029.png)

<span id="_Ref193181280" class="anchor"></span>Figure 5‑5. Connector Detail, 2 of 2

### Monitoring Institution Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on “Institution Mapping” to display the current set of institution mapping associations on the selected server. For example:

Station \#  JNDI Name

11000  vlj/testconnector

11001 vlj/testconnector1

11002 vlj/testconnector2

The current mappings for the selected server are listed in a table. You can use this information to monitor and verify the current, live institution mappings on your server(s).

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/030.png) | NOTE: Applications typically retrieve an adapter by using the station \#. The actual adapter returned to the application is determined by what JNDI name is mapped to the requested station \#. The list of mappings is generated (and modified) when each adapter’s configuration is loaded during adapter deployment, update, or server startup. |

## Configuration Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink administration console includes the Configuration Editor, for editing the VistALink configuration file storing information about each VistALink adapter/connector, Figure 5‑6.

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/031.png) | NOTE: Users that are in the Monitor role (and not a Deployer, Operator or Administrator) are disallowed from using the configuration editor. |

> ![](vistalink-version-1-6-system-management-guide/032.png)

<span id="_Ref193181375" class="anchor"></span>Figure 5‑6. Configuration Editor Main Interface

### About the Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration file contains additional properties needed to define a VistALink adapter beyond those in the deployment descriptors (ra.xml and weblogic-ra.xml).

The Configuration Editor loads the configuration file from the admin server classpath. If a file named "gov.va.med.vistalink.connectorConfig.xml" is found in a folder on the admin server classpath, the Configuration Editor loads the contents of this file automatically. When changes are made and saved, they are saved to this file as well, on the admin server only.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/033.png) | NOTE: The main page of the Configuration Editor displays the physical file location of the VistaLink connector configuration file that it is using, on the admin server. |

Configuration files must conform to the schema file connectorConfig.xsd, provided with the VistALink 1.6 distribution. For more information about the VistALink configuration file, see the section, "[VistALink Connector Configuration File](#vistalink-connector-configuration-file)."

### How to Propagate Configuration Changes to Other Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A copy of the configuration file must be available on the classpath of all servers in a domain that have deployed VistALink adapters. Changes made by the Configuration Editor, however, are made to the copy of the file on the physical file system of the admin server only.

Multiple Server, Multiple Machine Domain: In order to update the per-server VistALink configuration files for other physical servers in your domain (i.e., managed servers), you must manually copy/propagate the edited file from the admin server to a location on the classpath of the particular server.

Multiple Server, Single Machine Domain: Because all of the servers in this type of domain reside on the same physical machine, it is possible to configure all of their classpaths to contain the same folder, holding a single copy of the VistALink configuration file. In such cases, no further propagation of the configuration file is required.

Single Server Domain: In a single server WebLogic domain, one server is both the admin server and the server on which connectors and applications are deployed. No further propagation of the configuration file beyond the admin server is required.

### Viewing and Editing Connector Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can view and edit connector properties by selecting one of the connectors (hyperlinked) from the connector list. The Configuration Editor will then display the connector’s properties, Figure 5‑7.

> ![](vistalink-version-1-6-system-management-guide/034.png)

<span id="_Ref193174024" class="anchor"></span>Figure 5‑7. Editing a Connector Entry

After editing the file, you can save the changes by clicking the Submit button.

For a description of the various properties in a connector configuration, see the earlier section in the *Deploying VistALink on J2EE* chapter, "[VistALink Connector Configuration File](#vistalink-connector-configuration-file)."

#### JNDI Naming Recommendations

When naming adapters and editing connector entries, we recommend that you begin all connector JNDI names with a common JNDI subcontext name, i.e., "vlj/", followed by a meaningful name to specifically identify the adapter, i.e., "vlj/Salem658".

The Configuration Editor permits the following punctuation characters as part of the JNDI name (the first letter of the JNDI name must be alphanumeric, however): - \_ / \\ ( ) \[ \]

### Encryption of Access/Verify Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Encryption of the access and verify code adds an additional level of security to protect connector proxy user credentials. The properties are encrypted when you:

- Save change when you edit an existing connector, or add a new connector
- Select “Encrypt Unencrypted Entries” on the main Configuration Editor page (only shown if there are unencrypted entries in the file)
- When a connector configuration is loaded by a deployed adapter on a given system

The main page of the Configuration Editor displays the number of unencrypted connector entries, if any.

#### Modifying Access/Verify Codes Outside of Configuration Editor

If necessary, the access and verify code can be modified outside the Configuration Editor, and stored in clear text. When doing this, set the optional encrypted attribute to "false". Then the next time any of the encryption-triggering event above happen for the connector entry, the access and verify codes will be encrypted and the encrypted attribute set to "true".

#### Encrypt Unencrypted Entries Feature

If any unencrypted entries are present in the configuration file, a 'Encrypt Unencrypted Entries' button is displayed. Choosing this will allow you to encrypt all unencrypted entries present in the file.

#### Changing the Encryption Type

The encryption type reflects whether entries have been encrypted with domain-scoped encryption or not. If domain scoped, the domain name is included in the encryption, making it difficult to use encrypted values on other WebLogic domains. Configuration files from before 1.6 do not have domain-scoped encryption.

To change the encryption type, select Change Encryption Type on the main Configuration Editor page, Figure 5‑8.

> ![](vistalink-version-1-6-system-management-guide/035.png)

<span id="_Ref193181480" class="anchor"></span>Figure 5‑8. Changing the encryption type -- confirmation page

*This page is left blank intentionally.*

# Monitoring VistALink via JMX and MBeans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Java Management eXtensions (JMX) is the Java-standard mechanism for making applications manageable, including providing monitoring capabilities. Applications (and the application server itself) supply a variety of Managed Beans (MBeans). Through JMX, attributes on the MBeans can be monitored, and operations invoked, both locally inside a JVM and remotely from outside the JVM.

A variety of built-in and third-party utilities and applications support the use of JMX to access MBean attributes and operations, including:

- third-party JMX consoles
- third-party monitoring applications
- scripting tools such as WebLogic Scripting Tool (WLST) and wlshell
- the WebLogic console itself, which is built around JMX and MBeans

## VistALink MBeans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink provides two MBean types that can be monitored:

### VistaLinkConnector MBean

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Deployed: One instance per JVM, per deployed VistALink adapter

MBean Type: VistaLinkConnector

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 23%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>VistaLinkConnector Attribute</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Description</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>CfgIpAddress</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String</p>
</blockquote></td>
<td><blockquote>
<p>IP address from VistALink configuration file used for this connector.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CfgPort</p>
</blockquote></td>
<td><blockquote>
<p>int</p>
</blockquote></td>
<td><blockquote>
<p>port from VistALink configuration file used for this connector</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>CfgTimeout</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>timeout from VistALink configuration file used for this connector</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>CfgTimeoutAlwaysUseDefaultAsMin</p>
</blockquote></td>
<td><blockquote>
<p>boolean</p>
</blockquote></td>
<td><blockquote>
<p>whether a lower timeout can be set by applications than the configured timeout, from VistALink configuration file used for this connector</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>ContainerMBeanName</p>
</blockquote></td>
<td><blockquote>
<p>javax.management.<br />
ObjectName</p>
</blockquote></td>
<td><blockquote>
<p>System-specific ObjectName of connector's connector MBean linked to this VistALink MBean</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DeploymentState</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String</p>
</blockquote></td>
<td><blockquote>
<p>the current deployment state of the connector (platform-specific string)</p>
<p>Throws: java.rmi.RemoteException - thrown if unable returns this information (obtained from another MBean)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>DistinguishedIdentifier</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>unique, internally managed distinguished identifier for the VistALink connector</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>EisType</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String</p>
</blockquote></td>
<td><blockquote>
<p>the EISType of the connector (for VistALink connectors, should always be 'VistA')</p>
<p>Throws: java.rmi.RemoteException - thrown if unable returns this information (obtained from another MBean)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HlthConnectionAuthFailureCount</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>number of connector proxy authentication failures for this connector, since last system startup or deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HlthConnectionFailureCount</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>number of TCP-level connection failures for this connector, since last system startup or deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HlthDivisionMismatchCount</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>number of mismatches between connector primaryStation setting and target M system's primary station, since last system startup or deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>HlthIdentityFailureCount</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>number of re-authentication identification failures (failure to match requested DUZ, Application Proxy or VPID on M system), since last system startup or deployment</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>HlthProductionMismatchCount</p>
</blockquote></td>
<td><blockquote>
<p>long</p>
</blockquote></td>
<td><blockquote>
<p>number of mismatches between J2EE server's and M server's production setting, since last system startup or deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>JndiNameActual</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String</p>
</blockquote></td>
<td><blockquote>
<p>the JNDI name used to register the connector in the JNDI tree of the server</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>JndiNameCustomProp</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String</p>
</blockquote></td>
<td><blockquote>
<p>the value of the connectorJndiName custom ra.xml property</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>PerfCreateConnectionHandleAvgMillis</p>
</blockquote></td>
<td><blockquote>
<p>double</p>
</blockquote></td>
<td><blockquote>
<p>The amount of time it takes for a VistaLink managed connection to create a new connection handle for the underlying physical connection represented by the ManagedConnection instance; this connection handle is used by the application code to refer to the underlying physical connection</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>PerfMatchManagedConnectionAvgMillis</p>
</blockquote></td>
<td><blockquote>
<p>double</p>
</blockquote></td>
<td><blockquote>
<p>The amount of time it takes for the VistaLink connection factory to either a) match a connection request with an existing connection in pool of managed connections, or b) determine that no such match exists</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QueryMappedInstitutions</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String[]</p>
</blockquote></td>
<td><blockquote>
<p>a formatted string array listing the institutions currently mapped to this connector</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>QueryMSystemMap</p>
</blockquote></td>
<td><blockquote>
<p>java.util.Map</p>
</blockquote></td>
<td><blockquote>
<p>returns a Map containing a set of string keys and values obtained from calling the M system.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>QueryMSystemReport</p>
</blockquote></td>
<td><blockquote>
<p>java.lang.String[]</p>
</blockquote></td>
<td><blockquote>
<p>a formatted string array report representing a set of properties and values obtained from calling the M system</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>VendorSpecificProperties</p>
</blockquote></td>
<td><blockquote>
<p>java.util.Map</p>
</blockquote></td>
<td><blockquote>
<p>a Map containing vendor-specific properties and values</p>
<p>Throws: java.rmi.RemoteException - thrown if unable returns this information (obtained from other MBeans)</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc198960660" class="anchor"></span>Table 6‑1. VistaLinkConnector MBean Attributes

### VistaLinkInstitutionMapping MBean

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Deployed: One instance per JVM where VistALink Connectors are Deployed
- Type: VistaLinkInstitutionMapping

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 19%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Attribute Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Type</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Attribute</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>InstitutionMappings</p>
</blockquote></td>
<td>java.util.Map</td>
<td><blockquote>
<p>A Map containing string keys (station numbers) and string values (JNDI names) representing the current institution mapping associations on this JVM.</p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc198960661" class="anchor"></span>Table 6‑2. VistaLinkInstitutionMapping MBean Attributes

## VistALink MBean Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By default, in WebLogic 10.3.6/12.1.2 domains, customer-supplied MBeans such as those provided by VistALink are secured as follows:

- attributes: anyone who can authenticate to the domain can access
- operations: must possess administrator role to invoke

All VistALink MBean information access is implemented as attributes.

*This page is left blank intentionally.*

# M Server Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because VistALink connectors are deployed on J2EE servers, much of the management workload for VistALink focuses on the J2EE server. However, the VistALink listener (the portion of VistALink that resides on the M server) must also be managed.

In some cases, the same system manager may be responsible for managing both the J2EE and M portions of VistALink. In many cases, however, the two sides will be managed by different system managers, in separate computing facilities.

## Finding User Processes with the Connection Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Connection Manager (new with VistALink 1.6) tracks all active VistALink connections on the current M system, displays the individual processes, and gives you the option to either kill a selected VistALink connection, or all VistALink connections. The Connection Manager could be useful during software installations, for example, where it might be desirable to get all VistALink processes off of the system.

 

In multi-node M environments, the M node you run the Connection Manager on should be on the same node as the VistALink connections are running on, as started by the VistALink listener(s).

Main screen capture:

VL/J2M Connection Manager     Feb 21, <2008@11:33:14>          Page:    1 of    1  
    Job Selection Criteria (matches: 4)  
     Box-Volume Pair: ROU:CACHE2  
   Current Namespace: VL-HEAD  
             Routine: XOBVSKT  
           Job State: READ :: Job is reading from a device.  
 Entry PID         Device:Client IP                   Comment                    
    1  1756        \|TCP\|8016\|1756:10.6.21.65          User=\*KILMADE,JOE          
    2  1757        \|TCP\|8016\|1757:10.6.21.65          User=\*KILMADE,JOE          
    3  11769       \|TCP\|8016\|11769:10.6.17.157        User=\*KILMADE,JOE          
    4  11770       \|TCP\|8016\|11770:10.6.17.157        User=\*KILMADE,JOE        

 

 

 

 

          \* Connector Proxy User                                                 
TA  Terminate All                       RE  Refresh  
TP  Terminate PID                       SS  System Status  
Select Action:Quit//

<span id="_Toc198960662" class="anchor"></span>Figure 7‑1. Using the Connection Manager

| Action         | Description                                                                  |
|--------------------|----------------------------------------------------------------------------------|
| TA (Terminate All) | Kills all VistALink connections                                                  |
| TP (Terminate PID) | Kills a selected VistALink connection                                            |
| RE (Refresh)       | Refreshes/updates the list of connections                                        |
| SS (System Status) | Displays a list of all processes running on the system (not just VistALink ones) |

<span id="_Toc198960663" class="anchor"></span>Table 7‑2. Connection Manager actions and definitions

## Finding VistALink Processes without the Connection Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On VMS systems, the listener for any active VistALink connection is typically configured to be launched via VMS TCP Services. VistALink sets the VMS process name to "VLink_XXXXXXXX", where "XXXXXXXX" is the value of the M \$J converted to hex.

This makes it easier to find which VMS processes are associated with VistALink, and with which M job as well. You can use the DCL command SHOW SYSTEM /PROC=VL to display all VistALink processes. For example:

core\$ show sys /proc=VL\* \<RET\>

OpenVMS V7.3-2 on node ISC1A4 1-MAR-2005 10:19:47.64 Uptime 146 10:17:35

Pid Process Name State Pri I/O CPU Page flts Pages

20F9B10B VLINK_BG1877 HIB 11 179 0 00:00:00.01 202 184 N

20F9F90C VLink_20F9F90C LEF 11 211 0 00:00:00.11 4186 852 S

20FA190D VLINK_BG1891 HIB 11 172 0 00:00:00.04 202 184 N

20F9890E VLink_20F9890E LEF 10 211 0 00:00:00.10 4310 865 S

20F9C90F VLINK_BG1910 HIB 11 172 0 00:00:00.01 202 184 N

20F9C910 VLink_20F9C910 LEF 10 211 0 00:00:00.09 4231 852 S

core\$

<span id="_Toc198960664" class="anchor"></span>Figure 7‑3. Use the DCL command SHOW SYSTEM /PROC=VL to display all VistALink processes

### Non-VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list VistALink processes on non-VMS systems (e.g. Caché on Windows), you can look for processes that are frequently in the XOBVSKT routine; these processes are VistALink listeners. (However, when RPCs are invoked, the routine listed will be different.)

## Listener Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Listener Management for Caché/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the section "Listener Management for Caché/VMS" in Chapter 2 ("VistA/M Server Installation Procedures") of the *VistALink 1.6 Installation Guide*.

### Listener Management for Caché/NT Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See [Appendix A](#appendix-a-listener-management-for-cachent-systems), "Listener Management for Caché/NT Systems."

### Listener Management for DSM/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See [Appendix B](#appendix-b-listener-management-for-dsmvms-systems), "Listener Management for DSM/VMS Systems."

## M Listener Site Parameters File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FOUNDATIONS SITE PARAMETERS file (#18.01) is used to control listener settings for all implementations (Caché and DSM, on VMS and Windows). It contains one entry; the ".01" field is a pointer to the DOMAIN file (#4.2). When VistALink is installed, the install process creates this entry and assigns the proper Domain Name using the DOMAIN file.

The site parameters in this top-level entry pertain to Foundations and VistALink. Currently, all the parameters in this file are related to VistALink and listener configuration. As more Foundations tools are introduced, non-VistALink-related parameters will be added.

|                                                                                                                |                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/036.png) | NOTE: As part of the VistALink installation for Caché systems, a listener configuration named 'DEFAULT' was created for port 8000. |

To edit the site parameters, use the Site Parameters action in the Foundations menu.

### Site Parameters for All System Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit VistALink related site parameters, use the Site Parameters action:

HEARTBEAT RATE: 180// \<Enter\>

LATENCY DELTA: 180// \<Enter\>

J2EE CONNECTION TIMEOUT: 604800//

J2EE REAUTHENTICATION TIMEOUT: 3600//

<span id="_Toc198960665" class="anchor"></span>Figure 7‑4. Edit VistALink related site parameters

### Site Parameters for Windows Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the listener runs in M (rather than via Virtual Memory System (VMS) Transmission Control Protocol (TCP) Services), you should make an entry in the VistALink LISTENER CONFIGURATION file for each set of listeners that you plan to run on your system. After adding a listener configuration, you need to associate that configuration with any BOX-VOLUME where the new configuration is appropriate.

Note that the following portion of the dialog is not presented to a DSM system user:

Select BOX-VOLUME PAIR: ROU:CACHE//

BOX-VOLUME PAIR: ROU:CACHE// \<Enter\>

DEFAULT CONFIGURATION: DEFAULT// \<Enter\>

Select BOX-VOLUME PAIR:

<span id="_Toc198960666" class="anchor"></span>Figure 7‑5. Edit site parameters for Windows systems

It is irrelevant on Caché /VMS as well, if the listener is started via VMS TCP Services.

As part of this action, you are asked to select a Box-Volume Pair entry. Then, within each Box-Volume Pair entry (representing the volume set and system on which the listener should run), you can set the default listener configuration to be automatically started as part of the execution of the XOBV LISTENER STARTUP option. Also, the Start Box action uses this default listener configuration.

The table below defines the Foundations Site Parameter file fields.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field</strong></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Heartbeat Rate</td>
<td><p>This field indicates the rate (in seconds) of the VistALink heartbeat message originating from a client. If there is no activity on the connection for the specified amount of time, the client will send a system heartbeat message.</p>
<p>The client, as part of the initial connection protocol, retrieves this value. As a result, the client and the M server are always synchronized regarding the heartbeat rate.</p></td>
</tr>
<tr class="even">
<td>Latency Delta</td>
<td><p>This field indicates the number of seconds to add to the HEARTBEAT RATE when calculating the initial timeout value for the VistALink listener.</p>
<p>The client and the M server are synchronized regarding the HEARTBEAT RATE. This latency parameter allows the site to fine-tune the timeout value. The site can to take into account any network slowness or other factors that may delay the arrival of the system heartbeat message from the client.</p></td>
</tr>
<tr class="odd">
<td>J2EE Connection Timeout</td>
<td><p>This field indicates the number of seconds that a VistALink connection from J2EE to M should be allowed to remain connected when inactive, before M drops the connection.</p>
<p>It is recommended that the J2EE CONNECTION TIMEOUT parameter be set relatively high, e.g., 1 day (86400 seconds). A high setting is recommended because all the major application server implementations have more robust mechanisms for controlling connection pools.</p>
<p>The site should use the tools/mechanisms supplied by the application server implementation to control how the connection pool size grows and shrinks.</p></td>
</tr>
<tr class="even">
<td>J2EE Re-authentication Timeout</td>
<td><p>This new parameter indicates the number of seconds between 180 and 3600 (inclusive) before a re-authenticated connection is considered expired and must go through the re-authentication process again. (default: 600 secs).</p>
<p>Rules:</p>
<ul>
<li><blockquote>
<p>If a connection in the application server's pool is not reused by a particular re-authenticated user before this timeout limit is reached, the re-authentication is considered expired.</p>
</blockquote></li>
<li><blockquote>
<p>If the timeout is reached, the re-authentication process is performed again even if the same user uses the connection.</p>
</blockquote></li>
<li><blockquote>
<p>If the same connection is used again by the re-authenticated user before the timeout is reached, the session is considered re-authenticated for these number of seconds moving forward. (i.e. the timeout clock is reset)</p>
</blockquote></li>
<li><p>If a different user gains access to the connection, the connection is immediately considered not re-authenticated, and the re-authentication process is performed.</p></li>
</ul>
<p>Example of Re-authentication Expiration:</p>
<ol type="1">
<li><p>User gains access and uses a connection from the pool at 4:00pm</p></li>
<li><p>User signs off and goes home, along with most of the site staff</p></li>
<li><p>After 4:00 pm, user file maintenance is performed and the user's profile is changed. For example, the user's FILE MANAGER ACCESS CODE [DUZ(0)] is changed.</p></li>
<li><p>User signs back on the next morning at 8 am</p></li>
<li><p>Since there is very little activity from 4:00-8 am, the connection has not been re-used by another user and is still associated with 4:00 user</p></li>
<li><p>Since timeout has passed, re-authentication has expired</p></li>
<li><p>Re-authentication process occurs for the user</p></li>
<li><p>Re-authentication process resets DUZ(0) appropriately to the new value.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td>Box-Volume Pair</td>
<td><p>(For M-based listeners only)</p>
<p>This field indicates the BOX-VOLUME pair for the entry.</p>
<p>The XOBV LISTENER STARTUP option uses this field to find the configuration that should be used to startup VistALink listeners for the BOX-VOLUME pair.</p>
<p>Note: This information is presented to both VMS and NT Cache΄ users, but not to DSM users. However, it is ignored if listeners are started via the VMS TCP Service.</p></td>
</tr>
<tr class="even">
<td>Default Configuration</td>
<td><p>(For M-based listeners only)<br />
This field indicates the default startup listener configuration for the BOX-VOLUME PAIR entry.</p>
<p>The XOBV LISTENER STARTUP option uses this field to retrieve the correct listener configuration from the VISTALINK LISTENER CONFIGURATIONS file (#18.03).</p>
<p>The information in the configuration is then used to startup the indicated VistALink listeners on the desired ports.</p>
<p>Note: This information is not presented to a DSM system user.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc98316991" class="anchor"></span>Table 7‑6. Foundations Site Parameter file field definitions

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## J2EE System Manager Security Tasks for VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary J2EE system manager tasks for ensuring VistALink security are:

- Safeguarding the access/verify codes that M system managers provide to configure connectors with.

> These access/verify codes are for "connector proxy" users, and must be kept confidential. The level of system access they provide to the M system is significant.

- Ensuring that connectors are properly configured to reach the appropriate M systems.

> This is done primarily through the VistALink configuration file (gov.va.med.vistalink.connectorConfig.xml) and by making sure that connectors are mapped to the appropriate VA station number, IP, and Port.

## M System Manager Security Tasks for VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primary M system manager tasks for ensuring security for VistALink are:

- Creating connector proxy users for J2EE systems connecting to your M system
- Securely communicating connector proxy credentials (access and verify codes) to authorized J2EE system managers, who use them to configure their J2EE systems to access your M system.

## VistALink's J2SE Security Model

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For J2SE clients operating in client/server mode with VistA, the VistALink security model is as follows:

1.  A persistent connection is created between the Java client and the M server. Actions cannot be performed until the DUZ array has been created on the M side, acting as proof of end-user identity.
2.  To create the DUZ array, the Java client prompts the user for access/verify codes, division (as needed), and new verify code (as needed), and submits this information to Kernel security.
3.  If the credentials are valid, the DUZ array is created.

From that point on, the client can issue RPC requests to the M server. Authorizations are checked through the normal RPC authorization call, based on the contents of the DUZ array. If authorized, the RPC is executed and results are returned. Because this is a persistent connection, the DUZ array "persists" between calls. Because the connection is not used by or available to other clients, it does not need to be reproved each time.

## VistALink's J2EE Security Model 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The security modes for J2EE and J2SE are different. In J2EE n-tier mode, the connections are pooled on the J2EE server and are reused between different users. There are two levels of security.

The first security level is the authentication for the connection itself. It is implemented similarly to the client/server-mode mechanism described in the previous section:

1.  The app server/connector is configured by the app server administrator with the access/verify code of an M user. The M user must be marked as a "connection proxy" user. (In J2EE mode, only users whose Kernel account is marked as "connection proxy" can have connections established on their behalf.)
2.  If the credentials are valid, a J2EE connection is established.
3.  The J2EE server places the connection in a connection pool, for use by J2EE applications running on the J2EE server.

In the J2CA specification, the second level of security is a process called *re-authentication*. Here, the end-user identity information is passed from the calling application to VistALink via a J2CA connection spec. The re-authentication steps are as follows:

1.  When a J2EE application obtains a connection from the J2EE server's pool of connections, it passes identity information about the end-user to VistALink via a J2CA "connection spec."
2.  VistALink (on the J2EE side) passes the identity (DUZ, VPID, or application proxy name) down to M.
3.  Via a "chain of trust," VistALink (on the M side) trusts that the calling J2EE application has authenticated the identity of the end-user (via FatKAAT, KAAJEE, etc.).
4.  VistALink (on the M side) performs a lightweight security context switch to the identity of the specified end-user. RPCs are then executed under the DUZ of the end-user, and normal RPC security is applied.
5.  RPCs continue to execute under the identity of the specified end-user until the connection is "closed" (returned to the pool) by the J2EE application.

### Connector Proxy User (J2EE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The M server’s primary gatekeeper for controlling J2EE/VistALink access to M is the *connector proxy user*. This is a special user class in the Kernel NEW PERSON file (#200). Only J2EE connectors configured with credentials for "connection proxy" Kernel users can connect to an M VistALink listener. Once a connection is established through a connection proxy user, J2EE applications on that J2EE server can execute a variety of RPCs on the M server under a variety of end-user identities.

### J2EE Re-authentication Mechanisms for End-Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a connection is established from J2EE to M via a connector proxy user, VistALink employs a process called *re-authentication*, which runs RPCs under the identity of an actual end-user.

Whenever an application uses a connection to execute a request, re-authentication makes a lightweight security context switch from the connector proxy user identity to actual end-user identities. This switch is performed for the following reasons:

- Connections are pooled for use by multiple end-users on the application server
- Most RPCs need to run in the context of specific Kernel/M end-users

|                                                                                                                |                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/037.png) | NOTE: It is preferable that a connector proxy user have no privileges. |

The VistALink re-authentication architecture assumes that the identity of the end-user has already been authenticated (verified) by the calling application. Therefore, VistALink does not attempt to authenticate the end-user’s identity. To do so would be difficult for an M system, given the variety of client mechanisms through which end-users could be accessing any J2EE application. (There is also the possibility that an end-user might not even have an account on a given M system – in this case, a special "application proxy" user account could be used instead.)

Instead of authenticating the end-user’s identity, VistALink does the following to re-authenticate the end user:

1.  Trusts that the connecting application has authenticated the end-user, relying on the chain of trust established through the connector proxy user
2.  Verifies that it can match the end-user identity passed by the requesting application to an identity on the M system
3.  Checks whether the identified M account is authorized to perform the requested action

When retrieving a VistALink connection from a connection factory, the application supplies end-user credentials as part of the connection specification. These credentials are used to switch security context on the M side. This re-authentication process establishes the correct end-user environment on the M server (VA Person ID (VPID), Application Proxy, etc.) for the duration of the time that the connection is in use.

To link identities, the application selects one connection specification from the following, to retrieve a connection:

| Connection Specification class | Credentials                             |
|------------------------------------|---------------------------------------------|
| VistaLinkDuzConnectionSpec         | Known DUZ value, plus station number        |
| VistaLinkVpidConnectionSpec        | Known VPID value, plus station number       |
| VistaLinkAppProxyConnectionSpec    | Application Proxy name, plus station number |

<span id="_Toc198960668" class="anchor"></span>Table 8‑1. Connection Specification Class and Credentials

VPID is the connection specification expected to be used in most production scenarios. Whatever end-user authentication mechanism is used by a Health*<u>e</u>*Vet-VistA application, the application should be able to obtain the VPID for a given end-user as an output from the authentication process. When the end-user is authenticated, the J2EE application can use the VPID as a way to identify the end-user to any VistA M systems, when executing RPCs on such systems on behalf of the end-user. Kernel patch XU\*8.0\*309 is required to support the VPID connection specification on M-VistA systems.

The User Number, or DUZ (with DuzConnectionSpec), is the primary re-authentication mechanism until the VPID infrastructure is fully rolled out. At that point DuzConnectionSpec will be deprecated, and VpidConnectionSpec will be the primary mechanism. In both cases (DUZ and VPID), it is expected that the login will have been performed already through a VHA-approved authentication mechanism, and that authentication mechanism will make the DUZ or VPID available for use by the application.

The Application Proxy connection specification is expected to be used in either of the following special situations:

- The J2EE end-user does not have a user account on the M system on which an RPC is to be executed
- It is not appropriate for the RPC to execute under the identity of a particular end-user.

## RPC Security (B-Type Option)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All RPCs, whether accessed in J2SE client/server or J2EE mode, are secured with an RPC context (a "B"-type option). Any end-user for whom an RPC is executed must have the "B"-type option in their menu tree associated with the RPC. Otherwise an exception is thrown.

For more information on RPC security, see *Getting Started with the BDK, Chapter 3 (Extract): RPC Overview*, which is bundled in the /doc folder of the VistALink distribution, as the file xwb1_1p13dg-rpc_extract.pdf.

## Creating Connector Proxy Users for J2EE Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To allow VistALink access to your M system from a specific J2EE system (application server), a Kernel "connector proxy" account must be used, as follows:

1.  The M system manager creates a connector proxy account for a given J2EE system.
2.  The M system manager provides the access and verify code of the connector proxy user to the J2EE system manager.
3.  The J2EE system manager configures a connection pool to connect to the particular M system, using the access/verify code credentials of the connector proxy user provided by the M system manager.

### Security Caution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-system-management-guide/038.png)</td>
<td><p><strong>By setting up connector proxy users, you are granting access on your M server to execute a <em>wide variety of RPCs</em> on your system. Therefore you need to do the following:</strong></p>
<ul>
<li><p><strong>Create connection proxy users only for J2EE systems needing access to your M system.</strong></p></li>
<li><p><strong>Give the access/verify codes of the connection proxy users to approved server administrators only.</strong></p></li>
<li><p><strong>Create a different connection proxy user (with different access/verify code credentials) for each J2EE cluster (or data center) that will be connecting to your M system.</strong></p></li>
<li><p><strong>Make sure not to disseminate the access/verify code for a connector proxy user outside of secure communication channels.</strong></p></li>
</ul></td>
</tr>
</tbody>
</table>

### Creating the "Connector Proxy User" 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a connector proxy user:

1.  You must hold the Kernel XUMGR key.
2.  Add a new connector proxy user by using the Foundations menu on your M system and choosing the Enter/Edit Connector Proxy User option.
3.  The account requires no additional information from what is prompted for by the option.
4.  Leave the connector proxy user's Primary Menu empty.
5.  Securely communicate the access code and verify code for the connector proxy user to the J2EE system manager setting up access from J2EE to your system. Also communicate the IP and port of your VistALink listener.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-system-management-guide/039.png)</td>
<td><ul>
<li><blockquote>
<p><strong>Do not enter divisions for a connector proxy user</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Do not enter a primary menu</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Do not also use the connector proxy user as a test "end-user"</strong></p>
</blockquote></li>
<li><blockquote>
<p><strong>Utilize the user only as a connector proxy user</strong></p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

## Additional Security Issues (J2SE Mode)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following issues pertain only to VistALink's client/server (J2SE) mode, where a Java client connects directly to an M system.

### Authentication in Client/Server Mode

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In client/server (J2SE) mode, VistALink authentication, like that of the RPC Broker, is a wrapper around the Kernel login on your M system. It obeys the same authentication rules as other Kernel logins on your system, and uses Kernel code to obtain a "yes/no" authentication decision for each login attempt.

As with the RPC Broker, authorization to execute RPCs is required, based on the "B"-type Kernel option/context mechanism.

### CCOW-Based Single Sign-on

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink's client/server mode supports single sign-on to M systems based on user context, as implemented by the Office of Information’s Single Sign-On/User Context (SSO/UC) project.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-6-system-management-guide/040.png)</td>
<td><p><strong>NOTE:</strong> On VMS-based systems, Clinical Context Object Workgroup (<strong>CCOW</strong>)</p>
<p>-based single sign on is dependent on the GETPEER^%ZOSV call to return the client IP address. The GETPEER^%ZOSV call is in turn dependent on the DCL COM file used to launch the VistALink listener. This file must set up logical symbols used by GETPEER^%ZOSV.</p></td>
</tr>
</tbody>
</table>

### Kernel Auto Sign-on

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink's client/server (J2SE) supports an older single sign-on system, Kernel Auto-Sign on. In addition to the existing requirements for Kernel auto sign-on, VistALink has the following restrictions:

- The Broker client agent must already be running on the workstation.
- RPC Broker, Telnet, or VistALink can all be the first active connection.

|                                                                                                                |                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/041.png) | NOTE: On VMS-based systems, Kernel auto sign-on for VistALink is dependent on the GETPEER^%ZOSV call to return the client IP address. The GETPEER^%ZOSV call is in turn dependent on the DCL COM file used to launch the VistALink listener. This file must set up logical symbols used by GETPEER^%ZOSV. |

### Sensitivity of VistALink-Logged Data 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In client/server (J2SE) mode, VistALink uses the log4J logging utility to write information to a configurable log. The information written by VistALink loggers should not be application-sensitive data, and should not pose a security issue, even if the end-user turns on logging to its most detailed level.

# Troubleshooting VistALink 1.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In general, to troubleshoot most VistALink-related problems, you should check the following locations to gather helpful troubleshooting information:

- VistALink Administration Console – review the status and health indicators/failure counts for the connector in question, on the server in question.
- VistALink Administration Console – can you access the detail page for the connector, which makes a live query over the connector to the M system? Is the query successful? If not, what error message is displayed?
- Review the WebLogic server-specific log file and console output file for the server on which the error occurred:

> \<DOMAIN_HOME\>/servers/\<SERVER_NAME\>/logs/\<SERVER_NAME\>.log

> \<DOMAIN_HOME\>/servers/\<SERVER_NAME\>/logs/\<SERVER_NAME\>.out

- Review the log4j file logs configured for VistALink's logging, for the server on which the error occurred.
- Review the M-side error trap(s) for the M system(s) involved (D ^XTER)

## Symptoms and Possible Solutions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below shows symptoms and possible causes and solutions for VistALink resource adapter problems. It is not an exhaustive list but contains some of the more common error conditions you may encounter.

### Connection Attempt to Bad Listener Address/Port

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: During WebLogic Server startup, an error like the following prints out on the command console and in the WebLogic Server log:

> \####\<Jul 19, 2004 2:59:08 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190032\> \<\< VistaLinkAdapter_vlj_testconnector \> ResourceAllocationException of gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: Can not create VistaSocketConnection;

> Root cause exception:

> gov.va.med.net.VistaSocketException: Can not create TCP/IP socket.;

> Root cause exception:

> java.net.ConnectException: Connection refused: connect on createManagedConnection.\>

> \####\<Jul 19, 2004 2:59:08 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190024\> \<\< VistaLinkAdapter_vlj_testconnector \> Error making initial connections for pool. Reason: gov.va.med.net.VistaSocketException: Can not create TCP/IP socket.;

> Root cause exception:

> java.net.ConnectException: Connection refused: connect\>

Diagnoses and Solutions: The connector module's IP and port may be configured to connect to a non-existent listener.

### Connection Attempt to RPC Broker Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: During WebLogic server start up, an error like the following prints out on the command console and in the WebLogic server log:

> \####\<Jul 19, 2004 2:53:46 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190032\> \<\< VistaLinkAdapter_vlj_testconnector \> ResourceAllocationException of gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: FoundationsException in executeInitSocketInteraction.;

> Root cause exception:

> gov.va.med.foundations.utilities.FoundationsException: Error executing the interaction;

> Root cause exception:

> gov.va.med.vistalink.adapter.spi.VistaLinkSocketClosedException: This connection cannot be retried because construction has failed;

> Root cause exception:

> gov.va.med.net.VistaSocketException: Error occurred reading from socket. ;

> Root cause exception:

> gov.va.med.net.VistaSocketException: End of stream encountered unexpectedly. on createManagedConnection.\>

Diagnoses and Solutions: The connector module's IP and port may be configured to connect to an RPC Broker listener rather than to a VistALink listener.

### Invalid Connector Proxy Credentials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: During WebLogic server start up, an error like the following prints out on the command console and in the WebLogic server log:

> \####\<Jul 19, 2004 3:08:34 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190032\>  
> \<\< VistaLinkAdapter_vlj_testconnector \> ResourceAllocationException of gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: Could not perform logon\[\]Not a valid ACCESS CODE/VERIFY CODE pair. on createManagedConnection.\>

> \####\<Jul 19, 2004 3:08:34 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190024\> \<\< VistaLinkAdapter_vlj_testconnector \> Error making initial connections for pool. Reason: gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: Could not perform logon\[\]Not a valid ACCESS CODE/VERIFY CODE pair.\>

Diagnoses and Solutions: The access and verify code specified for the connector are not valid connector proxy sign-on credentials on the destination M system.

### Connector Proxy Expired Verify Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: During WebLogic Server startup, errors like the following print out in the command console and the WebLogic Server log.

> \####\<Jul 19, 2004 3:13:56 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190032\> \<\< VistaLinkAdapter_vlj_testconnector \> ResourceAllocationException of gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: Need new Verify Code: true Need to select Divisions: false on createManagedConnection.\>

> \####\<Jul 19, 2004 3:13:57 PM PDT\> \<Warning\> \<Connector\> \<testserver\> \<myserver\> \<main\> \<\<WLS Kernel\>\> \<\> \<BEA-190024\> \<\< VistaLinkAdapter_vlj_testconnector \> Error making initial connections for pool. Reason: gov.va.med.vistalink.adapter.cci.VistaLinkResourceException: Need new Verify Code: true Need to select Divisions: false\>

Diagnoses and Solutions: The verify code specified for the connector has expired. Try setting VERIFY CODE never expires? to "Yes" for the connector proxy user. If this doesn’t clear up the problem you may need to change the verify code of the connector proxy user and notify all connecting systems to update their connector configurations with the new verify code.

> **NOTE:** All Connector Proxy users created using the Enter/Edit Connector Proxy User option (on the Foundations menu) should have VERIFY CODE never expires? automatically set to true.

### Sporadic Socket Timeouts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: Application requests occasionally fail, and a VistaSocketTimeOutException is found in the log4j logs coincident with request failures. For example:

> 60871641 2008-03-11 15:07:37,520 \[\[ACTIVE\] ExecuteThread: '1' for queue: 'weblogic.kernel.Default (self-tuning)'\] DEBUG gov.va.med.vistalink.adapter.spi.VistaLinkManagedConnection:executeInteraction:1103 - gov.va.med.vistalink.adapter.spi.VistaLinkManagedConnection\[\]10.6.15.10\[\]8016\[\]1\[\]J2EE\[fdi\]1\[mdi\]5 M \$JOB=24008

> Socket timeout has occurred

> gov.va.med.net.VistaSocketTimeOutException: Socket Timeout occured. Timeout setting was: '15000 ms'. ;

> Root cause exception:

> java.net.SocketTimeoutException: Read timed out

> java.net.SocketTimeoutException: Read timed out

> at java.net.SocketInputStream.socketRead0(Native Method)

> at java.net.SocketInputStream.read(SocketInputStream.java:129)

> at sun.nio.cs.StreamDecoder\$CharsetSD.readBytes(StreamDecoder.java:411)

> at sun.nio.cs.StreamDecoder\$CharsetSD.implRead(StreamDecoder.java:453)

> at sun.nio.cs.StreamDecoder.read(StreamDecoder.java:183)

> at java.io.InputStreamReader.read(InputStreamReader.java:167)

> at java.io.BufferedReader.fill(BufferedReader.java:136)

> at java.io.BufferedReader.read1(BufferedReader.java:187)

> at java.io.BufferedReader.read(BufferedReader.java:261)

> at java.io.Reader.read(Reader.java:122)

> at gov.va.med.net.SocketManager.receiveData(SocketManager.java:160)

> (etc.)

Diagnoses and Solutions: Requests from the J2EE side are occasionally timing out at the socket level. Response time may occasionally take longer than the configured connection timeout due to load on the target M system, network load, etc., particularly at the times of day with the heaviest system loads.

The partial log4j exception output above contains clues (the IP and port of the M system being connected to, and the timeout setting in use at the time of the socket timeout). If you are seeing socket timeout exceptions for a particular connector, you may want to consider raising the default timeout in the VistaLink connector configuration file for the adapter in question.

### Connection Pool Capacity Exceeded

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: Applications log the following error when trying to retrieve a connection from the connector module:

> javax.resource.spi.ApplicationServerInternalException: Unable to get a connection for VistaLinkAdapter_vlj_testconnector connection pool: weblogic.common.resourcepool.ResourceLimitException: No resources currently available in pool VistaLinkAdapter_vlj_testconnector to allocate to applications, please increase the size of the pool and retryDiagnoses and Solutions: There are no connections left in the pool to access. Check the size of the pool; you may need to increase it.

To monitor how many requests are being rejected, check the WebLogic console in the connector module in question. Look under the Monitoring tab at the Connections Rejected Total Count column.

Also, check the connection module for leaked connections: WebLogic console, resource adapter module, Monitoring tab, Number Detected Leaks column. If the application code does not close a connection, it can be leaked. Closing connections should usually be done in the "finally" portion of a try/catch/finally block.

### ClassCastException

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: java.lang.ClassCastException thrown to an application. When an application (such as the VistALink sample web application) tries to retrieve the VistALink connection factory from JNDI, and casts it to VistaLinkConnectionFactory, a java.lang.ClassCastException is thrown. A line of code like the following triggers the ClassCastException:

> ic = new InitialContext();

> VistaLinkConnectionFactory cf = (VistaLinkConnectionFactory)

> ic.lookup("myConnectorJndiName);

Diagnoses and Solutions: Usually this exception means that VistALink is not properly configured on the J2EE server. In particular, its libraries are not present on a classloader higher than that of the calling application. To get VistALink’s libraries on a higher classloader, the two recommended approaches are:

<u>Production Systems</u>: Install the VistALink libraries as J2EE shared libraries.

<u>Non-production systems</u>: VistALink supporting libraries should be included in the exploded RAR, where they will be automatically loaded onto a high-level classloader by WebLogic.

Check you are using the appropriate method for your production or non-production server, and that the necessary supporting libraries are deployed (as J2EE shared libraries for production systems, or within the RAR for development systems):

- vljConnector-1.6.1.xxx.jar
- vljFoundationsLib-1.6.1.xxx.jar
- log4j-api-2.10.0.jar
- log4j-core-2.10.0.jar

If you are still having difficulty, try turning on the following debug settings (WebLogic administration console, Server -\> Debug tab) and then examining the server log output when the next ClassCastException is encountered:

- default.ClassFinder
- weblogic.classloader
- weblogic.classloader.Classloader
- weblogic.classloader.verbose
- weblogic.classloader.verbose.ClassLoaderVerbose

### Configuration File Confusion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: The settings actually being used for deployed adapters (e.g., ip, and/or port, and/or JNDI name, etc.) don’t correspond to the settings in my VistALink configuration file. Also, when I make changes in the settings in the configuration file, and redeploy my adapters, the settings actually used for the adapters don’t change.

Diagnoses and Solutions: Check your classpath to see if more than one directory is included. If so, check to see if the file gov.va.med.vistalink.connectorConfig.xml is present in multiple directories on your classpath. If so, VistALink may be reading settings from the first VistALink configuration file that it finds on the classpath. In this case, remove all files of this name from directories on your server classpath, except for the one that should be the valid configuration file. Make sure the directory containing the valid VistALink configuration file is on your server classpath. Redeploy your connectors; the correct settings should now be read in for each adapter.

### Reauthentication (End-User Identification) Failure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: Applications log the following error when trying to execute an RPC.

> Exception:gov.va.med.vistalink.security.m.SecurityDuzDeterminationFaultException: Fault Code: 'Server'; Fault String: 'Internal Application Error'; Fault Actor: 'XOBV TEST PING'; Code: '182301'; Type: 'XOBV TEST PING'; Message: 'No valid DUZ found. \[Security Type: DUZ\] \[DUZ Value: '117075555'\]' at gov.va.med.vistalink.rpc.RpcResponseFactory.handleSpecificFault(RpcResponseFactory.java:261) at … \[*deleted for brevity*\]

Diagnoses and Solutions: DUZ, the end-user credential used for re-authentication, is not valid on the system being connected to.

> **NOTE:** The reported failure could also be “no valid VPID found”, or “no valid Application Proxy user found”, depending on the type of reauthentication used to identify the end-user.

### Division Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: Applications log the following error when trying to execute an RPC:

> Exception:gov.va.med.vistalink.security.m.SecurityDivisionDeterminationFaultException: Fault Code: 'Server'; Fault String: 'Internal Application Error'; Fault Actor: 'XOBV TEST PING'; Code: '182302'; Type: 'XOBV TEST PING'; Message: 'Division mismatch during user reauthentication for security type \[DUZ\]. DUZ: \[11707\], Passed Division: \[510\] …… \[*deleted for brevity*\]

Diagnoses and Solutions: The division passed in the end-user credential for re-authentication is not valid for the given user. See the sections of this guide *J2EE Re-Authentication Mechanisms for End Users* and *Institution Mapping.*

### Failure to Authorize RPC (B-Type Option)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: Applications log the following error when trying to execute an RPC:

> Exception:gov.va.med.vistalink.rpc.NoRpcContextFaultException: Fault Code: 'Server'; Fault String: 'Internal Application Error'; Fault Actor: 'XOBV TEST PING'; Code: '182006'; Type: 'XOBV TEST PING'; Message: 'User TESTER,JOE does not have access to option XOBV VISTALINK TESTER' at gov.va.med.vistalink.rpc.RpcResponseFactory.handleSpecificFault(RpcResponseFactory.java:253) at … \[*excerpt*\]

Diagnoses and Solutions: The end-user lacks the "B"-type option necessary to execute the RPC in question. See the VistALink Developer’s Guide for information on writing RPCs.

### M-Side Error Returned to J2EE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: Applications log the following error when trying to execute an RPC:

> Exception occurred executing XOBV TEST PING  
> Exception:gov.va.med.vistalink.adapter.record.VistaLinkFaultException: Fault Code: 'Server'; Fault String: 'System Error'; Fault Actor: ''; Code: '181001'; Type: 'system'; Message: 'A system error occurred in M: CALL+1^MYRPC' at gov.va.med.vistalink.adapter.record.VistaLinkResponseFactoryImpl.handleFault(VistaLinkResponseFactoryImpl.java:309) at … \[*excerpt*\]

Diagnoses and Solutions: An M error occurred, most likely in the RPC being executed. Check the M error log.

### Abrupt Disconnects (M-Side Errors)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: \<READ\> or \<ENDOFFILE\> errors logged by the M listener.

Diagnoses and Solutions: On Caché systems, \<READ\> errors typically mean an abrupt disconnect between the WebLogic server and VistALink. For example, this could occur if the machine that the WebLogic server was running on was shut down without performing a graceful shutdown of the WebLogic server first.

\<ENDOFFILE\> errors may mean that the Caché server was shut down without shutting down the WebLogic server first (as often might be the case with enterprise-wide connections).

### J2SE Connection Attempt to 1.0 Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Symptom: The following error message occurs when attempting to run the VistALink Swing Sample App

> Could not create connection;

> Root cause exception:

> Gov.va.med.vistalink.adapter.cci.VistaLinkResourceException:RoundationsException executelnitSocket…

> Root cause exception:

> Gov.va.med.exception.FoundationsException: The response version \[1.0\] is incompatible with this version...Diagnoses and Solutions: The J2SE or J2EE client is attempting to connect to a VistALink/M server that is still running a VistALink 1.0 listener. Upgrade to the current VistALink 1.6 KIDS build.

## Analyzing VistALink Errors in the M Error Trap

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you look through the M error trap, you may see errors with no "subject" line.

Such errors may have been logged by VistALink to note a fault condition detected by the listener. Unfortunately, at the present, there is no easy way to add a non-M fault to the error log and still have the subject show.

### XOBSTR Variable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you see an error log entry without a subject, enter XOBSTR at the "Which symbol? \>" prompt. If the log entry is VistALink-related, that variable will be defined in the error trap, and its value should be an error message describing the fault condition encountered.

Example:

4)  13:08:13 VISTALINK,ROU 553187626 BG875

…

Which symbol? \> XOBSTR

XOBSTR=Primary station &apos;&apos; of the request does not match the primary station &apos;11000&apos; of the M/Kernel system.

<span id="_Toc198960669" class="anchor"></span>Figure 9‑1. M Error Trap

### XWBTIP Variable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When examining a VistALink-related error trap, the XWBTIP variable may be useful in that it contains the IP address of the requesting site, as determined by the operating system:

> 1\) 22:23:15 VL-HEAD,ROU 25537 \|TCP\|8016

> Which symbol? \> XWBTIP

> XWBTIP=10.6.21.65

This variable may be useful in particular, when trying to determine whether a particular client system that is logging a large number of errors in the error trap, and if so, how to contact the managers of that system to correct the condition.

### XOBLASTR Variable (M Request Timestamp)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a new variable that developers and sites can use for debugging:

- XOBLASTR Timestamp of last time any request was made on connection

Developers and site administrators can use this variable via JOBEXAM or the Cache console to watch activity and determine "dead" connections.

## Analyzing VistALink Java Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information about VistALink Java exceptions found in log file output, look up the exception class names in the VistALink Javadoc.

## Section 508 Compliance: Differentiate Focus on Change Verify Code Check Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to a known defect in Java Swing ([<u>http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4985801</u>](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4985801)), and as defined by Section 508 compliance, it might be difficult for end-users to distinguish when focus occurs on the Change Verify Code check box in the login dialog window when using the Windows “Look and Feel” High Contrast Black color scheme.

# Appendix A: Listener Management for Cache/NT Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For Cache/NT systems, listener processes are configured, started, and stopped entirely within the M environment. The Foundations Management menu \[XOBU SITE SETUP MENU\] is located under the Operations Management menu \[XUSITEMGR\] and provides several ListMan actions to do these operations. An example is shown in the figure below.

In Windows, unlike VMS-based systems, the VistALink listener runs as an M process. An application is provided to configure, start, and stop the listener in M-based VistA.

> ![](vistalink-version-1-6-system-management-guide/042.png)

<span id="_Toc198960670" class="anchor"></span>Figure A‑1. Foundations Manager Interface (Cache΄ Systems)

## Creating/Editing Listener Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create or edit listener configuration entries, you should use the "Manage Configurations" action. The Manage Configurations action first prompts you to select a configuration entry. Then, within the entry, you can configure one or more listeners, as shown in the following example:

Select VistALink LISTENER CONFIGURATION NAME: DEFAULT

NAME: DEFAULT// \<Enter\>

Select PORT: 8000// \<Enter\>

PORT: 8000// \<Enter\>

STARTUP: YES// \<Enter\>

<span id="_Toc198960671" class="anchor"></span>Figure A‑2. Create or edit listener configuration entries

The table below defines the site parameter fields for a given listener entry:

| Field | Meaning                                                                                                                                                                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name      | This field contains the name of the default VistALink configuration used with the associated BOX-VOLUME PAIR specified in the FOUNDATIONS SITE PARAMETERS file (#18.01).                                                                                |
| Port      | The port the listener will listen on.                                                                                                                                                                                                                   |
| Startup   | If the listener should be started when this configuration is started, set this field to YES. Otherwise, set to NO. (If you want to keep the port in the configuration but temporarily do not want to start a listener, you would set this field to NO.) |

<span id="_Toc198960672" class="anchor"></span>Table A‑1. Listener Configuration Entries Description Table

## Starting All Configured Listeners

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All listeners configured in the Foundations Site Parameters file for automatic startup, can be started with the Start Box action. This action will start all listeners for the configuration assigned to the current BOX-VOLUME pair.

For more information on configuring listeners for automatic startup, see the section of this chapter titled "Creating/Editing Listener Configurations."

## Starting a Single Unconfigured Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To start a listener, use the Start Listener (SL) action on the Foundations Manager interface and enter the desired port. The action will first check if a listener is already listening on the port and inform you if it is. No damage to the system will occur if a listener is already listening on the port.

## Stopping a Configured or Unconfigured Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To stop new connections:

1.  Use the Stop Listener (STP) action and select the desired listener.

> This action may take up to 60 seconds to actually stop the listener. This prevents new connections from being established to the M system. It does not, however, terminate existing connections.

To terminate all connections and prevent new ones:

1.  Use the Stop Listener (STP) action and select the desired listener. This action may take up to 60 seconds to actually stop the listener.
2.  If you have access to the J2EE system (or can contact the system manager), STOP the associated VistALink connector. This shuts down the connection pool on the J2EE side and stops it from requesting new M connections.
3.  You should shut down the Listener on the M system as well, to block any new connection requests that may come from other clients.

|                                                                                                                |                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/043.png) | NOTE: If the J2EE connector has not been stopped, it will continue to try to establish connections to the M system (which is why it is better to STOP the connector on the J2EE side). |

4.  Manually terminate any remaining XOBVSKT jobs running on the M system. This might include client/server connections or J2EE connectors that you were unable to stop.

## Scheduling Listener Startup at System Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XOBV LISTENER STARTUP option can be tasked to automatically start all required listener processes upon TaskMan start-up. This option starts all VistALink listener configuration operations at one time for the BOX-VOLUME pair. This type of start-up would be required after rebooting the system or restarting the configuration. After VistALink installation on a Cache΄ system, this option should already be scheduled to run at startup.

To automatically start the listeners(s) when TaskMan is restarted, enter the XOBV LISTENER STARTUP option in the OPTION SCHEDULING file (#19.2). Schedule this option with SPECIAL QUEUING set to "Startup."

You can schedule the required options by making entries to the TaskMan Schedule/Unschedule Options, as shown in the figure below.

Select Systems Manager Menu Option: TASKMAN Management

Select Taskman Management Option: SCHedule/Unschedule Options

Select OPTION to schedule or reschedule: XOBV LISTENER STARTUP \<Enter\> Start VistALink Listener Configuration

...OK? Yes// \<Enter\> (Yes)

Edit Option Schedule

Option Name: XOBV LISTENER STARTUP

Menu Text: Start VistALink Listener Configu TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING: STARTUP

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

<span id="_Toc98317611" class="anchor"></span>Figure A‑3. Automatically Starting Listener(s) on TaskMan Restart

# Appendix B: Listener Management for DSM/VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DSM/VMS systems should run VistALink as a TCP/IP service, commonly known as TCP/IP Service for OpenVMS (previously known as UCX). The TCP/IP Service permits multiple TCP/IP clients to connect and run as concurrent processes, up to the limits established by the system. TCP/IP listens on a particular port and launches a specified VistALink handler process for each client connection. Configuring, starting, and stopping listeners is managed entirely through the VMS TCP/IP Service.

DSM/VMS site systems are in the process of converting to Cache΄*/*VMS systems. As such, the instructions below were written for the VistALink 1.0 release (November 21, 2003) and have not been modified for the conversion.

## Setting Up an OpenVMS User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The easiest way to configure an OpenVMS account to be a VistALink handler is to copy most of the parameters from VA MailMan TCP account. To do this:

1.  Determine an unused User Identification Code (UIC), typically in the same group as other DSM for OpenVMS accounts.
2.  Using the OpenVMS Authorize utility, copy the XMINET account to a new VLINK account with the unused UIC. You must have SYSPRV to do this.

Make sure that the account settings for the new VLINK account are the same as in the following example. If they are different, make sure that the impact of the different settings is acceptable for your system. In particular, make sure that the DisCtlY, Restricted, and Captive flags are set for security reasons.

## Setting Up a Home Directory for the VistALink Handler Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to create a home directory for the VistALink handler account. This directory will house the DCL command procedure that is executed whenever a client connects, as well as log files. Make sure that the owner of the directory is the VLINK account.

For example, to create a home directory named \[VLINK\] with ownership of VLINK, enter:

\$ CREATE/DIR \[VLINK\]/OWNER=VLINK

## Creating a DCL Login Command Procedure for the VistALink Handler

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create a Digital Command Language (DCL) login procedure for the VistALink Handler:

1.  Use the home directory for the handler account.
2.  Make sure the command procedure file is owned by the VistALink handler account.
3.  Adjust the Digital Standard Mumps (DSM) command line (environment, UCI, and volume set) for your system.
4.  If access control is enabled, ensure that the VLINK account has access to this UCI, volume set, and routine. (See "Access Control List (ACL) Issues", later in this chapter).

It is possible to run different TCP/IP Service listener processes on multiple nodes.

### Sample DCL Login Command Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the sample procedure below, ‘environ,’ ‘uci,’ and ‘vol’ are site-specific.

\$!VLINK.COM - for incoming connect requests

\$!-------------------------------------------------------------

\$set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$! WAIT 00:00:00

\$ purge/keep=10 sys\$login:VLINK\*.log !Purge log files only

\$! set proc/priv=(share) !May not be required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to DSM

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open "+ x

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt = cnt + 1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ SET NOVERIFY

\$!---------------------------------------------------------------

\$ dsm/env=DSMMANAG /uci=VAH /vol=ROU UCX^XOBVTCP

\$!---------------------------------------------------------------

\$ endif

\$ endif

\$ EXIT:

\$ logout/FULL

<span id="_Toc198960674" class="anchor"></span>Figure B‑1. Sample DCL Login Command Procedure

## Setting Up and Enabling the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you create the VistALink handler, create the TCP/IP Service to listen for connections and launch the VistALink handler. You need to choose:

- The OpenVMS node to run the listener on.

> Choose the node that you want to run the resulting M jobs on to process incoming VistALink messages. This is also the node whose IP address will be advertised to other systems as the location of your VistALink listener.

- The port it should listen on.
- The user account and command file name to invoke when a connection is received.

The steps to set up a TCP/IP Service for VistALink are:

1.  Determine the port
2.  Set up the "VLINK" TCP/IP Service
3.  Enable and save the "VLINK" TCP/IP Service

Prior to setting up TCP/IP in production, you can set up a "test" TCP/IP Service that logs into an M test account. The test TCP/IP Service can use the same OpenVMS account and directory as the production TCP/IP Service. Just create a different DCL command file using the UCI and volume set of the test account.

## Obtaining an Available Listener Port (for Alpha/VMS systems only) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Port selections conflict only if another process is using the same port on the same system. To list the ports currently in use on OpenVMS systems, use the DCL command:

\$ TCPIP SHOW DEVICE_SOCKET

Port Remote

Device_socket Type Local Remote Service Host

bg3 STREAM 8001 0 VistALink 0.0.0.0

bg23 STREAM 9700 0 Z3ZTEST 0.0.0.0

bg24 STREAM 9600 0 ZSDPROTO 0.0.0.0

<span id="_Toc522197365" class="anchor"></span>Figure B‑2. Obtaining an available listener port (for Alpha/VMS systems only)

If ‘8000’ appears in the Local Port column, another application is already using this port number; so you should choose another port.

## Creating the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since the TCP/IP Service is node specific, make sure you are on the same node that you want the listener to run on. Follow this example to create the service:

\$TCPIP

TCPIP\> SET SERVICE VLINK/USER=VLINK/PROC=VLINK /PORT=8000-

\_TCPIP\> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCPIP\> /LIMIT=50/FILE=SYS\$SYSDEVICE:\[VLINK\]VLINK.COM

TCPIP\> SHO SERVICE VLINK/FULL

Service: VLINK

State: Disabled

Port: 8000 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: VLINK<span id="_Toc89843877" class="anchor"></span>

Figure B‑3. Creating the TCP/IP Service

## Enabling and Saving the Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because the TCP/IP service is node specific, make sure you are on the same node that you want the listener to run on. Follow this example to enable the service:

TCPIP\> ENABLE SERVICE VLINK *(enable service immediately)*

TCPIP\> SET CONFIG ENABLE SERVICE VLINK *(save service for reboot)*

TCPIP\> SHO SERVICE/FULL VLINK

Service: VLINK

State: Enabled

Port: 8000 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: VLINK Process: VLINK

Limit: 50 Active: 0 Peak: 0

File: SYS\$SYSDEVICE:\[VLINK\]VLINK.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, VLINK, MPI, TELNET, XMINETMM

TCPIP\> EXIT

<span id="_Toc522197367" class="anchor"></span>Figure B‑4. Enabling and saving the TCP/IP service

|                                                                                                                |                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/044.png) | NOTE: To test the connection, refer to the section of this guide called "Testing the Listener." |

## Access Control List ACL Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some sites use DSM's ACL feature, which controls access explicitly to each OpenVMS account needing to enter that DSM environment. If your site is using ACL, you should set up the VLINK account with PROGRAMMER access, and then specify the Volume set and UCI name that the VLINK user account has authorization to access. Ensure that the OpenVMS VLINK account allows only Network longings, and prohibits Batch, Local, Dialup and Remote logins.

The following is an example of setting this level of access for a VLINK account:

\$ DSM /MAN ^ACL

Environment Access Utilities

1\. ADD/MODIFY USER (ADD^ACL)

2\. DELETE USER (DELETE^ACL)

3\. MODIFY ACTIVE AUTHORIZATIONS (^ACLSET)

4\. PRINT AUTHORIZED USERS (PRINT^ACL)

Select Option \> 1 ADD/MODIFY USER

OpenVMS User Name: \> VLINK

ACCESS MODE VOL UCI ROUTINE

----------- --- --- -------

No access rights for this user.

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> P

Volume set name: \> ROU

UCI: \> VAH

UCI: \> \<RET\>

Volume set name: \> \<RET\>

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> \<RET\>

USER ACCESS MODE VOL UCI ROUTINE

---- ----------- --- --- -------

VLINK PROGRAMMER ROU VAH

OK to file? \<Y\> \<RET\>

OpenVMS User Name: \> \<RET\>

OK to activate changes now? \<Y\> \<RET\>

Creating access authorization file: SYS\$SYSDEVICE:\[DSMMGR\]DSM\$ACCESS.DAT.

<span id="_Toc522197368" class="anchor"></span>Figure B‑5. Access Control List

## Controlling the Number of Log Files 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VLINK TCP/IP Service automatically creates log files in the VLINK directory named "VLINK.LOG;xxx," where 'xxx' is a file version number. This cannot be prevented. New versions of this file will be created until that file version number reaches the maximum number of 32767. To minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME disk\$:\[VLINK\]VLINK.LOG; disk\$:\[VLINK\]VLINK.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the VLINK directory:

\$ SET FILE /VERSION_LIMIT=10 disk\$:\[VLINK\]VLINK.LOG;

|                                                                                                                |                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/045.png) | NOTE: You probably should not limit the number of versions of the log file until you know your VistALink service is working correctly. Keeping the log files can help when diagnosing problems with the service/account. |

## Disabling New Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To stop incoming connections, stop the TCP/IP service.

> This prevents new connections from being established to the M system. Current connections (that have their own connection, PID, etc) will remain, but new connections cannot be made until the service is enabled again.

## Terminating All Connections and Preventing New Ones

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To stop incoming connections, stop the TCP/IP service.
2.  If you have access to the J2EE system (or can contact the system manager), disable the associated VistALink connector. This shuts down the connection pool on the J2EE side and stops it from requesting new M connections. You should shut down the Listener on the M system as well, to block any new connection requests that may come from other clients.

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-6-system-management-guide/046.png) | NOTE: If the J2EE connector has not been stopped, however, it will continue to try to establish connections to the M system (which is why it is better to STOP the connector on the J2EE side). |

3.  Manually terminate any remaining XOBVSKT jobs running on the M system. This might include client/server connections, or J2EE connectors that you were unable to stop.

# Glossary

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
<td>Each Oracle WebLogic server domain must have one server instance that acts as the administration server. This server is used to configure all other server instances in the domain.</td>
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
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a standalone adapter that is completely set up. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters). The deployer only needs to modify a subset of the linked adapters’ deployment descriptor settings. <em>Note: This mechanism is no longer supported in WebLogic 9 and later for J2CA 1.5 adapters (e.g., VistALink 1.6).</em></td>
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
<td>A cached store of connection objects that can be available on demand and reused, increasing performance and scalability. VistALink uses connection pooling when running on a J2EE server.</td>
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
<td>VHA sites are also called <em>institutions</em>. Each institution has a <em>station number</em> associated with it. Occasionally a single institution is made up of multiple sites, known as <em>divisions</em>. To make a connection, VistALink needs a station number from the end-user’s New Person entry in the KERNEL SYSTEM PARAMETERS file (#8989.3). It looks first for a division station number and if it can’t find one, uses the station number associated with default institution.</td>
</tr>
<tr class="odd">
<td>DSM</td>
<td><em>Digital Standard MUMPS.</em> An M environment, a product of InterSystems Corp.</td>
</tr>
<tr class="even">
<td>DUZ</td>
<td>A local variable holding a number that identifies the signed-on user. The number is the Internal Entry Number (IEN) of the user’s record in the NEW PERSON file (file #200)</td>
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
<td>SYSTEM file #18 was the precursor to the KERNEL SYSTEM PARAMETERS file (#8989.3), and is now obsolete. It uses the same number space that is now assigned to VistALink. Therefore, File #18 must be deleted before VistALink can be installed.</td>
</tr>
<tr class="odd">
<td>Global</td>
<td>A multi-dimensional data storage structure -- the mechanism for persistent data storage in a MUMPS database.</td>
</tr>
<tr class="even">
<td>Health<em><u>e</u></em>Vet-VistA</td>
<td>The VHA is converting its MUMPS-based VistA healthcare system to a new J2EE-based platform and application suite. The new system is known as Health<em><u>e</u></em>Vet-VistA.</td>
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
<td>VHA sites are also called <em>institutions</em>. Each institution has a <em>station number</em> associated with it. Occasionally a single institution is made up of multiple sites, known as <em>divisions</em>. To make a connection, VistALink needs a station number from the end-user’s New Person entry in the KERNEL SYSTEM PARAMETERS file (#8989.3). It looks first for a division station number and if it can’t find one, uses the station number associated with default institution.</td>
</tr>
<tr class="even">
<td>Institution Mapping</td>
<td>The VistALink 1.6.1 release includes a small utility that administrators can use to associate station numbers with JNDI names, and which allows runtime code to retrieve the a VistALink connection factory based on station number.</td>
</tr>
<tr class="odd">
<td>ISO</td>
<td><em>Information Security Officer</em></td>
</tr>
<tr class="even">
<td><span id="JCA" class="anchor"></span>J2CA</td>
<td>J2EE Connector Architecture 1.6</td>
</tr>
<tr class="odd">
<td>J2CA</td>
<td><em>J2EE Connector Architecture</em>. J2CA is a framework for integrating J2EE-compliant application servers with Enterprise Information Systems, such as the VHA’s VistA/M systems. It is the framework for J2EE connector modules that plug into J2EE application servers, such as the VistALink adapter.</td>
</tr>
<tr class="even">
<td>J2EE</td>
<td>The <em>Java 2 Platform, Enterprise Edition (J2EE)</em> is an environment for developing and deploying enterprise applications. The J2EE platform consists of a set of services, APIs, and protocols that provide the functionality for developing multi-tiered, Web-based applications. A J2EE Connector Architecture specification for building adapters to connect J2EE systems to non-J2EE enterprise information systems.</td>
</tr>
<tr class="odd">
<td>J2EE</td>
<td><em>Java 2 Enterprise Edition.</em> A standard suite of technologies for developing distributed, multi-tier, enterprise applications.</td>
</tr>
<tr class="even">
<td>J2SE</td>
<td><em>Java 2 Standard Edition.</em> Sun Microsystem’s programming platform based on the Java programming language. It is the blueprint for building Java applications, and includes the Java Development Kit (JDK) and Java Runtime Environment (JRE).</td>
</tr>
<tr class="odd">
<td>JAAS</td>
<td><em>Java Authentication and Authorization Service.</em> JAAS is a pluggable Java framework for user authentication and authorization, enabling services to authenticate and enforce access controls upon users.</td>
</tr>
<tr class="even">
<td>JAR file</td>
<td><em>Java archive</em> file. It is a file format based on the ZIP file format, used to aggregate many files into one.</td>
</tr>
<tr class="odd">
<td>Java Library</td>
<td>A library of Java classes usually distributed in JAR format.</td>
</tr>
<tr class="even">
<td>Javadoc</td>
<td>Javadoc is a tool for generating API documentation in HTML format from doc comments in source code. Documentation produced with this tool is typically called Javadoc.</td>
</tr>
<tr class="odd">
<td>JBoss</td>
<td>JBoss is a free software / open source Java EE-based application server.</td>
</tr>
<tr class="even">
<td>JCA CCI</td>
<td><em>J2EE Connector Architecture Common Client Interface</em></td>
</tr>
<tr class="odd">
<td>JDK</td>
<td><em>Java Development Kit</em>. A set of programming tools for developing Java applications.</td>
</tr>
<tr class="even">
<td><span id="JMX" class="anchor"></span>JMX</td>
<td><em>Java Management eXtensions</em>. A java specification for building manageability into java applications, including J2EE-based ones.</td>
</tr>
<tr class="odd">
<td>JNDI</td>
<td><em>Java Naming and Directory Interface</em>. A protocol to a set of APIs for multiple naming and directory services.</td>
</tr>
<tr class="even">
<td>JRE</td>
<td>The <em>Java Runtime Environment</em> consists of the Java virtual machine, the Java platform core classes, and supporting files. JRE is bundled with the JDK but also available packaged separately.</td>
</tr>
<tr class="odd">
<td>JSP</td>
<td><em>Java Server Pages</em>. A language for building web interfaces for interacting with web applications.</td>
</tr>
<tr class="even">
<td>JVM</td>
<td><em>Java Virtual Machine.</em> The JVM interprets compiled Java binary code (byte code) for specific computer hardware.</td>
</tr>
<tr class="odd">
<td>KAAJEE</td>
<td><em>Kernel Authentication and Authorization for Java 2 Enterprise Edition</em></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>Kernel functions as an intermediary between the host M operating system and VistA M applications. It consists of a standard user and program interface and a set of utilities for performing basic VA computer system tasks, e.g., Menu Manager, Task Manager, Device Handler, and security.</td>
</tr>
<tr class="odd">
<td>KIDS</td>
<td><em>Kernel Installation and Distribution System</em>. The VistA/M module for exporting new VistA software packages.</td>
</tr>
<tr class="even">
<td>LDAP</td>
<td>Acronym for <em>Lightweight Directory Access Protocol.</em> LDAP is an open protocol that permits applications running on various platforms to access information from directories hosted by any type of server.</td>
</tr>
<tr class="odd">
<td>Linked Adapter</td>
<td>Version 8.1 of WebLogic introduced a "link-ref" mechanism enabling the resources of a single "base" adapter to be shared by one or more "linked" adapters. The base adapter is a standalone adapter that is completely set up. Its resources (classes, jars, etc.) can be linked to and reused by other resource adapters (linked adapters). The deployer only needs to modify a subset of linked adapters’ deployment descriptor settings. <em>Note: This mechanism is no longer supported in WebLogic 9 and later for J2CA 1.5 adapters (e.g., VistALink 1.6).</em></td>
</tr>
<tr class="even">
<td>Linux</td>
<td>An <a href="http://www.webopedia.com/TERM/L/open_source.html">open-source</a> <a href="http://www.webopedia.com/TERM/L/operating_system.html">operating system</a> that runs on various types of hardware <a href="http://www.webopedia.com/TERM/L/platform.html">platforms</a>. Health<em><u>e</u></em>Vet-VistA servers use both Linux and Windows operating systems.</td>
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
<td><em>Massachusetts General Hospital Utility Multi-programming System</em>, abbreviated M. M is a high-level procedural programming computer language, especially helpful for manipulating textual data.</td>
</tr>
<tr class="odd">
<td>Managed Server</td>
<td>A server instance in a Oracle WebLogic domain that is not an administration server, i.e., not used to configure all other server instances in the domain.</td>
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
<td>Multiple</td>
<td>A VA FileMan data type that allows more than one value for a single entry.</td>
</tr>
<tr class="odd">
<td>Namespace</td>
<td>A unique 2-4 character prefix for each VistA package. The DBA assigns this character string for developers to use in naming a package’s routines, options, and other elements. The namespace includes a <em>number space</em>, a pre-defined range of numbers that package files must stay within.</td>
</tr>
<tr class="even">
<td>New Person File</td>
<td>The New Person file contains information for all valid users on an M system.</td>
</tr>
<tr class="odd">
<td>NIST</td>
<td><em>National Institute for Standards and Technology</em></td>
</tr>
<tr class="even">
<td>OI</td>
<td><em>Office of Information</em></td>
</tr>
<tr class="odd">
<td>Oracle WebLogic</td>
<td>Oracle WebLogic is a J2EE Platform application server. Oracle has acquired BEA Systems, Inc.</td>
</tr>
<tr class="even">
<td>OS</td>
<td><em>Operating System</em></td>
</tr>
<tr class="odd">
<td>Patch</td>
<td>An update to a VistA software package that contains an enhancement or bug fix. Patches can include code updates, documentation updates, and information updates. Patches are applied to the programs on M systems by IRM services.</td>
</tr>
<tr class="even">
<td>PHI</td>
<td><em>Protected Health Information</em></td>
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
<td>All RPCs are secured with an RPC context (a "B"-type option). An end-user executing an RPC must have the "B"-type option associated with the RPC in the user’s menu tree. Otherwise an exception is thrown.</td>
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
<td>A password used in tandem with the access code to provide secure user access. The Kernel’s Sign-on/Security system uses the verify code to validate the user's identity.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td><em>Veterans Health Information Systems and Technology Architecture</em>. The VHA’s portfolio of M-based application software used by all VA medical centers and associated facilities.</td>
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
<td><em>VA Person Identifier</em>. A new enterprise-level identifier uniquely identifying VA ‘persons’ across the entire VA domain.</td>
</tr>
<tr class="even">
<td>WAR file</td>
<td><em>Web archive</em> file. Contains the class files for servlets and JSPs.</td>
</tr>
<tr class="odd">
<td>WebLogic Server</td>
<td>A J2EE application server manufactured by Oracle WebLogic Systems.</td>
</tr>
<tr class="even">
<td>WebSphere</td>
<td>WebSphere Application Server (WAS) is and IBM application server.</td>
</tr>
<tr class="odd">
<td>XLS</td>
<td>Microsoft Office XL worksheet and workbook file format</td>
</tr>
<tr class="even">
<td>XML</td>
<td><em>Extensible Markup Language</em></td>
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
<td>![](vistalink-version-1-6-system-management-guide/047.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the Security and Other Common Services Glossary Web page at the following Web address:</p>
<blockquote>
<p><u>http://vista.med.va.gov/iss/glossary.asp</u></p>
</blockquote>
<p>For a comprehensive list of acronyms, please visit the Security and Other Common Services Acronyms Web site at the following Web address:</p>
<blockquote>
<p><u>http://vista/med/va/gov/iss/acronyms/index.asp</u></p>
</blockquote></td>
</tr>
</tbody>
</table>
*This page is left blank intentionally.*


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VistaLink Version 1.6.7 System Management Guide

### Exploded 1.6.7 RAR Layout, Production Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recommended contents of an exploded VistALink RAR folder, for production systems, are:

> (root) empty

> META-INF\\ - MANIFEST.MF (contains information needed to use J2EE Shared Libraries)

> \- ra.xml (J2EE standard Deployment Descriptor)

> \- weblogic-ra.xml (WLS-specific Deployment Descriptor)

The app-J2EE\Rar-Prod-Template directory in the VistALink distribution zip provides an exploded RAR in this structure.

| ![](vistalink-version-1-6-7-system-management-guide/008.png) | NOTE: On production systems, Oracle recommends that the supporting libraries (JAR files) be deployed as J2EE shared libraries to minimize the consumption of server resources (hence the recommended exploded RAR for a production system contains only deployment descriptors). |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Exploded 1.6.7 RAR Layout, Non-Production Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The recommended contents of an exploded VistALink RAR folder, for non-production systems, are:

> (root) Main VistALink libraries:

> \- vljConnector-1.6.7.jar

> \- vljFoundationsLib-1.6.7.jar

> lib\\ Supporting libraries:

> \- log4j-api-2.0.14.jar

> \- log4j-core-2.0.14.jar

META-INF\\ - MANIFEST.MF (a required RAR artifact)

\- ra.xml (J2EE standard Deployment Descriptor)

> \- weblogic-ra.xml (WLS-specific Deployment Descriptor)

The app-J2EE\Rar-Dev-Template directory in the VistALink distribution zip provides an exploded RAR in this structure.

| ![](vistalink-version-1-6-7-system-management-guide/009.png) | NOTE: Libraries contained in RARs are automatically loaded onto a high-level classloaders, and are thus available to other deployed applications (EARS, WARs, etc) running in the same Java Virtual Machine (JVM). |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### From: VistALink Version 1.5 System Management Guide

## VistALink 1.5 Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink 1.5 resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet-VistA Java applications and VistA/M servers, in both client-server and n-tier environments. It allows Java applications to execute remote procedure calls (RPCs) on the VistA/M system and retrieve results, synchronously. VistALink 1.5 is also referred to as “VistALink J2M.”

VistALink consists of Java-side adapter libraries and an M-side listener:

- The adapter libraries use the J2EE Connector Architecture (J2CA 1.0) specification to integrate Java applications with legacy systems.
- The M listener process receives and processes requests from client applications.

## Document Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides information on the management of VistALink 1.5 resource adapters and servers. It contains detailed information on J2EE application server management, institution mapping, the VistALink console, M listener management, and VistALink security, logging, and troubleshooting. Its intended audience includes server administrators and IRM IT specialists at VHA facilities, as well as developers of Java applications requiring communication with VistA/M.

Generally, the installation and maintenance instructions presented here assume the use of Windows as the client operating system. Where appropriate, separate steps are displayed for Linux, as in the following example:

|                                                   |                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-system-management-guide/002.png) | Special instructions for Linux systems are set off and indicated with the Linux "Tux" penguin icon. |

### Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The term *resource adapter* is often shortened in this guide to “adapter*,*” and is also used interchangeably with the term *connector*.

### Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File names and directory names are set off from other text using bold font (e.g., config.xml). Bold is also used to indicate GUI elements, such as tab, field, and button names (e.g., “press Delete”).

All caps are used to indicate M routine and option names (e.g., XMINET). All caps used inside angle brackets indicate file names to be supplied by the user. Example:

> \<JAVA_HOME\>\bin\java -Dlog4j.configuration=file:///c:/localConfigs/mylog4j.xml

Names for Java objects, methods, and variables are indicated by Courier font. Snapshots of computer displays also appear in Courier, surrounded by a border:

> Select Installation Option: LOAD a Distribution

> Enter a Host File: XOB_1_5.KID

In these examples, the response that the user enters at a prompt appears in bold font:

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET PORT

Bold font is also used in code samples to indicate lines of particular interest, discussed in the preceding text:

> \<!DOCTYPE weblogic-connection-factory-dd PUBLIC '-//BEA Systems, Inc.//DTD WebLogic 8.1.0 Connector//EN' 'http://www.bea.com/servers/wls810/dtd/weblogic810-ra.dtd'\>

> \<weblogic-connection-factory-dd\>

> \<connection-factory-name\>VistaLinkAdapter\</connection-factory-name\>

> \<jndi-name\>vlj/testconnector\</jndi-name\>

> \<pool-params\>

> \<initial-capacity\>1\</initial-capacity\>

> \<max-capacity\>1\</max-capacity\>

The following symbols appear throughout the documentation to alert the reader to special information or conditions.

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                               |
| ![](vistalink-version-1-5-system-management-guide/003.png) | Used to inform the reader of general information and references to additional reading material, including online information. |
| ![](vistalink-version-1-5-system-management-guide/004.png)                                                              | Used to caution the reader to take special notice of critical information                                                     |

## Additional Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistALink Web Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink website summarizes VistALink architecture and functionality and presents status updates: <http://vista.med.va.gov/migration/foundations/index.htm>.

### VistALink Documentation Set

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents are provided in the VistALink 1.5 documentation set:

- *VistALink 1.5 Installation Guide*: Provides detailed instructions for setting up, installing, and configuring the VistALink 1.5 listener on VistA/M servers and the VistALink resource adapter on J2EE application servers. Its intended audience includes server administrators, IRM IT specialists, and Java application developers.
- *VistALink 1.5 System Management Guide*: Contains detailed information on J2EE application server management, institution mapping, the VistALink console, M listener management, and VistALink security, logging, and troubleshooting.
- *VistALink 1.5 Developer Guide*: Contains detailed information about workstation setup, re-authentication, institution mapping, executing requests, VistALink exceptions, Foundations Library utilities, and other topics pertaining to writing code that uses VistALink.
- *VistALink 1.5 Release Notes*: Lists all new features included in each VistALink 1.5 release.
- *Getting Started With the BDK, Chapter 3*: *RPC Overview*. A short guide on writing RPCs from the *RPC Broker* manual.

### BEA Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

At the current time, VistALink 1.5 has been tested and is supported on BEA WebLogic Server 8.1 (Service Pack 4) only. WebLogic product documentation can be found at the following website: <http://edocs.bea.com/>.

### RAR Physical Layout

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the WebLogic Server, RARs can be deployed in both packaged and exploded formats. The contents of the exploded VistALink RAR are as follows:

> (root) Main VistALink libraries:

> \- vljConnector-1.5.0.jar

> \- vljFoundationsLib-1.5.0.jar

> lib\\ Supporting libraries:

> \- jaxen-core.jar

> \- jaxen-dom.jar

> \- log4j-1.2.8.jar

> \- saxpath.jar

> \- xbean.jar

> META-INF\\ Deployment Descriptors:

> \- ra.xml (J2EE standard)

> \- weblogic-ra.xml (WLS-specific)

> \- jboss-vlj-ds.xml (JBOSS-specific)

> \- oc4j-ra.xml (Oracle-specific)

## Adapter Deployment Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each M system you want your J2EE system to connect to, you need to create and deploy a separate VistALink RAR (exploded or packaged). Each RAR contains two deployment descriptors, ra.xml and weblogic-ra.xml. These need to be configured with the unique settings that describe how the adapter should be deployed on the J2EE system and how it should connect to a specific M system.

For a J2EE server already set up with VistALink, the basic, high-level steps to deploy a new VistALink adapter are as follows:

1.  Create a new exploded or packaged RAR for deployment.
2.  Edit the ra.xml and weblogic-ra.xml deployment descriptors in the new RAR.
3.  Add an entry in the gov.va.med.vistalink.connectorConfig.xml file for the new adapter, on all servers that the connector will be deployed on.
4.  Use WebLogic to deploy the new RAR to one or more servers.
5.  Verify that the new adapter is working correctly using the VistALink administration console plug-in (see the section ["The VistALink Console"](#the-vistalink-console) for more information).

> Even though the adapter may deploy successfully from WebLogic's point of view, the test for configuration completion is whether the adapter can successfully connect to the M system.

The configurable settings for deployment of any VistALink adapter are contained in the following locations:

- ra.xml: contains J2EE-standard deployment descriptor configuration settings and a custom property to select the appropriate VistALink configuration file entry.
- weblogic-ra.xml: contains WebLogic-specific deployment descriptor configuration settings (such as initial and maximum pool sizes)
- VistALink configuration file: contains VistALink-specific configuration settings, such as access and verify codes for the connector proxy user. Unlike the ra.xml and weblogic-ra.xml files, there is only one VistALink configuration file, which contains settings for *all* deployed VistALink connectors. For this reason the VistALink configuration file is not in the META-INF folder of each adapter. It is in a single location on a given server, in a folder that the deployer places on the server's classpath.

## The VistALink Connector Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink-specific resource adapter (connector) settings are stored in a separate connector configuration file, named gov.va.med.vistalink.connectorConfig.xml. You can edit this file manually or using the Configuration Editor (see the section “[Configuration Editor](#configuration-editor)”).

The rules for the VistALink configuration file are:

- The file must be named “gov.va.med.vistalink.connectorConfig.xml”
- The file must be placed in a folder that is on the ‘java’ classpath of the JVM of each WebLogic server instance deploying VistALink connectors
- Because the gov.va.med.vistalink.connectorConfig.xml file holds login credentials for accessing VA VistA systems, it must be protected. On Linux systems, access to the folder containing the file should be restricted to the account or group under which WebLogic runs. Access to the host file system should be protected on all J2EE systems.

When the server deploys a VistALink connector, the connector does the following:

1.  Gets the connectorJndiName attribute value from the ra.xml (base adapters) or weblogic-ra.xml (linked adapters) deployment descriptor.
2.  Loads gov.va.med.vistalink.connectorConfig.xml, via the server ‘java’ classpath
3.  Looks in the VistALink configuration file for a \<connector\> entry with a matching jndiName attribute
4.  Uses the settings from the matching entry (ip, port, access-code, verify-code, etc.) to configure the connector.

### Connector Entry Format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink configuration file should contain one \<connector\> entry per connector module/adapter that you will deploy to your J2EE server. Each entry should have a unique jndiName. Each \<connector\> entry describes the characteristics of the M listener that a particular connector module/adapter will connect to.

The following example shows the format of the VistALink configuration file (with a configuration of a single listener):

> \<?xml version="1.0" encoding="UTF-8"?\>

> \<connectors

> xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

> xsi:noNamespaceSchemaLocation="connectorConfig.xsd"

> xmlns="http://med.va.gov/vistalink/adapter/config"

> \>

> \<connector

> jndiName="vlj/testconnector"

> primaryStation="11000"

> ip="isc1a4.REDACTED.med.va.gov"

> port="8000"

> access-code="joe.123"

> verify-code="ebony.432"

> timeout="30"

> always-use-default-as-min="false"

> enabled="true"

> /\>

> \</connectors\>

> <span id="_Toc136058521" class="anchor"></span>Figure 1. VistALink Configuration File Format Example

You can have one or more \<connector\> entries. Each entry describes the characteristics of the M listener that the particular connector module/adapter will connect to.

### Connector Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The basic settings for each \<connector\> entry are as follows:

- jndiName (required): uniquely identifies each entry. Should be the same JNDI name as you will specify in the weblogic-ra.xml descriptor for your connector. This setting is also used to create the JNDI half of the mappings between station numbers and connector JNDI names.
- primaryStation (required): Station number of the M/Kernel system connected to. VistALink’s institution mapping functionality maps this station number to the connector's JNDI name, so the application can retrieve the connector by the station number. This entry is checked against the DEFAULT INSTITUTION field of the KERNEL SYSTEM PARAMETERS file at runtime, when connections are made.
- Ip (required): IP address of the M VistALink listener to connect to (either numeric or mnemonic)
- Port (required): port of the M VistALink listener to connect to
- access-code (required): the access code credential for the connector proxy user to connect to the M VistALink listener.
- verify-code (required): the verify code credential for the connector proxy user to connect to the M VistALink listener.
- encrypted (optional): true \| false. When the access/verify codes are encrypted by VistALink, this attribute is set to true. If you need to manually (outside the configuration editor) update the access / verify code, however, set "encrypted" to false so that VistALink will know the access/verify code is not encrypted.
- enabled (required): true \| false. If false, the connector will not deploy. Use this attribute primarily to retain inactive configurations in your configuration file.
- timeout (optional): Sets the default span of time in seconds socket will wait for response from M (e.g., waiting for an RPC to execute) and after which connection is automatically terminated.

### Advanced Settings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- always-use-default-as-min: If true, the default timeout will be the lowest timeout value allowed for this connector; it will override any programmatically specified lower value set by an application.
- primaryStationSuffix: This setting is for the very small number of VistALink installations associated with institutions that have an alphanumeric suffix attached to the station numbers. For example, if the M system’s DEFAULT INSTITUTION is “500M,” the primaryStation attribute should be set to “500” and the primaryStationSuffix attribute to “M.”

> The configuration editor does not have an edit box for this field (see the section “[Configuration Editor](#configuration-editor)” ). To add the attribute to a connector, the deployer must manually edit the VistALink configuration file.

- timestamp: When a connector entry is edited, the configuration editor automatically stamps the entry with a timestamp.

|                                                                                                                |                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-system-management-guide/005.png) | Although you can manually edit the VistALink configuration file, you can also edit it with a UI provided as a plug-in to the VistALink console. (See the section “[Configuration Editor](#configuration-editor).”) |

### Selecting a VistALink Configuration in Adapter's Deployment Descriptor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For an adapter to retrieve its \<connector\> configuration entry from the VistALink configuration file, its deployment descriptors (in each RAR's META-INF folder) must be configured with the connectorJndiName property, as follows:

- For base adapters: Add a \<config-property\> to ra.xml named “connectorJndiName”.
- For linked adapters: Add a \<map-config-property\> to weblogic-ra.xml named “connectorJndiName”.

This property’s value is the JNDI name of the connector, and should correspond to the jndiName attribute of the \<connector\> entry it will use in the VistALink configuration file. For more detail, see the section "[Adapter Configuration](#adapter-configuration)," below.

## Adapter Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Base and Linked Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WebLogic 8.1 introduced a “link-ref” mechanism, enabling resources of a single “base” adapter to be shared by one or more “linked” adapters. The base adapter is a completely set up, standalone adapter. Its resources (classes, jars, etc.), however, can be linked to and reused by other resource adapters (“linked” adapters). Each linked adapter needs only a subset of files and deployment descriptor settings.

For connections to multiple M systems, we recommend setting up one adapter (to one M system) as a base adapter, and any additional adapters as linked adapters. At least one base adapter must always be set up connecting to some M system. Each linked adapter then refers back to the base adapter via the weblogic-ra.xml \<ra-link-ref\> property.

|                                                                                                                |                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-system-management-guide/006.png) | For more information about base and linked adapters, the following BEA website is helpful: [<u>http://e-docs.bea.com/wls/docs81/jconnector/config.html</u>](http://e-docs.bea.com/wls/docs81/jconnector/config.html). |

### Base Adapter Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ra.xml Deployment Descriptor (Base Adapters)

The ra.xml deployment descriptor is located in the META-INF subfolder inside the adapter RAR (packaged or exploded). VistALink ships with an adapter that has pre-configured ra.xml and weblogic-ra.xml files.

The key properties to edit are these:

1.  connectorJndiName: This custom \<config-property\> setting identifies the name of the \<connector\> entry in the VistALink configuration file to use for this adapter.
2.  authentication-mechanism:This element controls the internal mechanism WebLogic uses for authenticating the principal user of a hosted application. Because VistALink does its own authenticating, this information is not needed. For performance considerations, you should remove this element.
3.  reauthentication-support: This element controls whether the application server will attempt to re-authenticate the user as time passes. Because you have removed the \<authentication-mechanism\> element for performance considerations (number 2, above), you should set the \<reauthentication-support\> element to “false.”

Example:

\<?xml version="1.0" encoding="UTF-8"?\>

\<!DOCTYPE connector PUBLIC '-//Sun Microsystems, Inc.//DTD Connector 1.0//EN' 'http://java.sun.com/dtd/connector_1_0.dtd'\>

\<connector\>

\<display-name\>VistaLinkAdapter\</display-name\>

\<vendor-name\>Foundations\</vendor-name\>

\<spec-version\>1.0\</spec-version\>

\<eis-type\>VistA\</eis-type\>

\<version\>1.5\</version\>

\<resourceadapter\>

\<managedconnectionfactory-class\>gov.va.med.vistalink.adapter.spi.VistaLinkManagedConnectionFactory\</managedconnectionfactory-class\>

\<connectionfactory-interface\>javax.resource.cci.ConnectionFactory\</connectionfactory-interface\>

\<connectionfactory-impl-class\>gov.va.med.vistalink.adapter.cci.VistaLinkConnectionFactory\</connectionfactory-impl-class\>

\<connection-interface\>javax.resource.cci.Connection\</connection-interface\>

\<connection-impl-class\>gov.va.med.vistalink.adapter.cci.VistaLinkConnection\</connection-impl-class\>

\<transaction-support\>NoTransaction\</transaction-support\>

\<config-property\>\<config-property-name\>connectorJndiName\</config-property-name\>\<config-property-type\>java.lang.String\</config-property-type\>\<config-property-value\>vlj/testconnector\</config-property-value\>\</config-property\>

\<reauthentication-support\>false\</reauthentication-support\>

\</resourceadapter\>

\</connector\>

#### weblogic ra.xml (Base Adapters)

The location of the weblogic-ra.xml deployment descriptor is also the META-INF subfolder inside the adapter RAR file (packaged or exploded).VistALink ships with an adapter with pre-configured ra.xml and weblogic-ra.xml files.

The key properties to modify are:

- connection-factory-name This name should be unique across all adapters.
- jndi-name This identifies the name in JNDI from which applications will retrieve the adapter connection factory.

Example:

\<!DOCTYPE weblogic-connection-factory-dd PUBLIC '-//BEA Systems, Inc.//DTD WebLogic 8.1.0 Connector//EN' 'http://www.bea.com/servers/wls810/dtd/weblogic810-ra.dtd'\>

\<weblogic-connection-factory-dd\>

\<connection-factory-name\>VistaLinkAdapter\</connection-factory-name\>\<jndi-name\>vlj/testconnector\</jndi-name\>

\<pool-params\>

\<initial-capacity\>1\</initial-capacity\>

\<max-capacity\>1\</max-capacity\>

\<capacity-increment\>5\</capacity-increment\>

\<shrinking-enabled\>true\</shrinking-enabled\>

\<connection-profiling-enabled\>false\</connection-profiling-enabled\>

\<shrink-frequency-seconds\>900\</shrink-frequency-seconds\>

\<inactive-connection-timeout-seconds\>0\</inactive-connection-timeout-seconds\>

\<highest-num-waiters\>2147483647\</highest-num-waiters\>

\<highest-num-unavailable\>0\</highest-num-unavailable\>

\<connection-creation-retry-frequency-seconds\>0\</connection-creation-retry-frequency-seconds\>

\<connection-reserve-timeout-seconds\>10\</connection-reserve-timeout-seconds\>

\<test-frequency-seconds\>0\</test-frequency-seconds\>

\<match-connections-supported\>true\</match-connections-supported\>

\</pool-params\>

\<logging-enabled\>true\</logging-enabled\>

\<log-filename\>vlj.log\</log-filename\>

\</weblogic-connection-factory-dd\>

### Deploying Additional (“Linked”) Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your J2EE system connects to multiple M systems, you would typically create and deploy an adapter for each M system. When setting up multiple VistALink adapters for connections to multiple M systems, we recommend setting up one adapter (to one M system) as a base adapter, and any additional adapters as linked adapters.

To create a linked adapter:

1.  Choose a JNDI name for the new adapter.
2.  Determine which “base” adapter the linked adapter will be linked to. The base adapter must be a fully deployed, standalone adapter.
3.  Write down the \<connection-factory-name\> value from the base adapter’s weblogic-ra.xml file.
4.  Create a new folder for the new linked adapter in your staging area.

|                                                                                                                |                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|
| ![](vistalink-version-1-5-system-management-guide/007.png) | The folder name becomes the adapter name in the WebLogic console. |

5.  Create a subfolder inside the new folder named “META-INF".
6.  Copy ra.xml and weblogic-ra.xml from the base adapter's META-INF subfolder to the new adapter's META-INF subfolder.
7.  Edit the copied ra.xml file in the new adapter's META-INF subfolder. Select all the contents, delete them, and save the file. An empty ra.xml file should remain.
8.  Edit the copied weblogic-ra.xml file in the new (linked) adapter's META-INF subfolder:
1.  Set the value of the \<connection-factory-name\> element to a unique name for this connector.
2.  Set the value of the \<jndi-name\> element to a unique name for this connector. This is the JNDI name for the connector.
3.  Add an \<ra-link-ref\> element. The value of the element should be the value of the \<connection-factory-name\> element in the weblogic-ra.xml file of your base adapter (see the weblogic-ra.xml file example below).
4.  Add one custom \<map-config-property\> element as the last element before the closing tag in the weblogic-ra.xml file (see the weblogic-ra.xml file example below). Add two enclosed elements:
    - A \<map-config-property-name\> element whose value is “connectorJndiName.”
    - A \<map-config-property-value\> element set to the JNDI name for the linked adapter. This value must be the same as the \<jndi-name\> attribute specified in step b above.
5.  Change the \<pool-params\> settings (initial-capacity, max-capacity, capacity-increment) as needed for the linked adapter.
9.  The following example weblogic-ra.xml descriptor sets up a linked adapter, linked to a base adapter whose weblogic-ra.xml \<connection-factory-name\> is set to "VistaLinkAdapterBase". The link to the base adapter is made via the linked adapter's \<ra-link-ref\> element.

> Example weblogic-ra.xml file:

\<!DOCTYPE weblogic-connection-factory-dd PUBLIC '-//BEA Systems, Inc.//DTD WebLogic 8.1.0 Connector//EN' 'http://www.bea.com/servers/wls810/dtd/weblogic810-ra.dtd'\>

\<weblogic-connection-factory-dd\>

\<connection-factory-name\>VistaLinkAdapterLinked1\</connection-factory-name\>\<jndi-name\>vlj/vlj-linked1\</jndi-name\>\<ra-link-ref\>VistaLinkAdapterBase\</ra-link-ref\>

\<pool-params\>

\<initial-capacity\>3\</initial-capacity\>\<max-capacity\>6\</max-capacity\>\<capacity-increment\>5\</capacity-increment\>

\<shrinking-enabled\>true\</shrinking-enabled\>

\<connection-profiling-enabled\>false\</connection-profiling-enabled\>

\<shrink-frequency-seconds\>900\</shrink-frequency-seconds\>

\<inactive-connection-timeout-seconds\>0\</inactive-connection-timeout-seconds\>

\<highest-num-waiters\>2147483647\</highest-num-waiters\>

\<highest-num-unavailable\>0\</highest-num-unavailable\>

\<connection-creation-retry-frequency-seconds\>0\</connection-creation-retry-frequency-seconds\>

\<connection-reserve-timeout-seconds\>10\</connection-reserve-timeout-seconds\>

\<test-frequency-seconds\>0\</test-frequency-seconds\>

\<match-connections-supported\>true\</match-connections-supported\>

\</pool-params\>

\<logging-enabled\>true\</logging-enabled\>

\<log-filename\>vlj.log\</log-filename\>

\<map-config-property\>\<map-config-property-name\>connectorJndiName\</map-config-property-name\>\<map-config-property-value\>vlj/vlj-linked1\</map-config-property-value\>\</map-config-property\>

\</weblogic-connection-factory-dd\>

10. If you have not done so already, create a new entry in the VistALink configuration file (gov.va.med.vistalink.connectorConfig.xml) to hold the appropriate settings for the M system connected to.  
      
    For the weblogic-ra.xml file example shown above, you would add a new entry for “vlj/vlj-linked1”. The jndiName attribute of the new entry should match the \<jndi-name\> attribute and the \<map-config-property-name\> value in the linked adapter’s weblogic-ra.xml ("connectorJndiName").
11. Use WebLogic to deploy the linked adapter RAR.

## Pool Size Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pool size management is a key factor in enhancing VistALink’s performance on a J2EE server. It is costly to have either too many unused open connections or not enough for incoming requests. Connection pool sizing will be part of the art of system tuning in a Health*<u>e</u>*Vet-VistA environment.

On the WebLogic server, you can use the WebLogic console and the ra.xml/weblogic-ra.xml deployment descriptors to control the characteristics of the connection pool for each deployed resource adapter (connector).

Key settings include:

- Initial Capacity: The number of connections to create for the connection pool. Pool creation happens on initial deployment and on server startup. Higher numbers for this setting can add additional time to the server startup process.
- Max Capacity: The high point of expansion for the connection pool. You may want to set this based on the highest load you can place on the M system you are connected to (potential work as well as license slot usage). On the J2EE side, if all connections are in use and the Max Capacity setting is reached, applications requesting a connection will be thrown a ResourceException.
- Shrinking Enabled and Shrink Frequency Seconds: This allows pools to shrink when the number of requests has slowed down and created connections are inactive for a given set of time. Enabling shrinking is recommended in most cases, to reduce the number of inactive connections using license slots on M systems.

## Activating Adapter Configuration Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you update an adapter setting in ra.xml, weblogic-ra.xml, or the VistALink configuration file, you do not need to bounce the server to activate the changed setting. It is sufficient to stop and redeploy the adapter in the WebLogic console to make the changed setting active.

|                                                                                                                |                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-system-management-guide/008.png) | When the adapter is stopped, before redeployment completes, the adapter will be briefly unavailable to applications. |

### ### Stopping and Redeploying Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Stopping an adapter makes the adapter unavailable to applications, but leaves the adapter in the server configuration. However, if the server is restarted, a stopped adapter will be redeployed and made available to applications again.

To stop an adapter:

1.  Log on to the WebLogic console and navigate to:

> \<MY_DOMAIN_NAME\> \| Deployments \| Connector Modules

2.  Select the connector you want to stop.
3.  Navigate to the Deploy tab for the particular connector, and press Stop for each server/target you want to stop the adapter on.

To redeploy an adapter:

1.  On the Deploy tab for the particular connector, press Redeploy for each server/target you want to redeploy the adapter on.
2.  Verify that each redeployed adapter is working correctly using the VistALink administration console plug-in (see the section “The VistALink Console” for more information).

## Deleting Adapters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If necessary, you can use the WebLogic Server console to delete VistALink resource adapter (connector) modules from your application server.

Deleting an adapter stops it (makes it unavailable to applications) and then removes it completely from the WebLogic server configuration.

To delete an adapter:

1.  Log on to the WebLogic console and navigate to

> \<MY_DOMAIN_NAME\> \| Deployments \| Connector Modules

2.  From the configuration tab, click on the trash can icon ![](vistalink-version-1-5-system-management-guide/009.png) to remove any adapter.

## VistALink Configuration File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink's configuration file (gov.va.med.vistalink.connectorConfig.xml) controls the mapping of connector JNDI names to VistA station numbers. The (required) primaryStation attribute of the \<connector\> element associates a particular connector (identified by its JNDI name) with a particular station number.

In the following configuration file example, station number “11000” (and its descendants “11000A,” “110000B,” etc.) are mapped to the JNDI name “vlj/testconnector”:

> \<?xml version="1.0" encoding="UTF-8"?\>

> \<connectors

> xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"

> xsi:noNamespaceSchemaLocation="connectorConfig.xsd"

> xmlns="http://med.va.gov/vistalink/adapter/config"

> \>

> \<connector

> jndiName="vlj/testconnector"

> primaryStation="11000"

> ip="isc1a4.REDACTED.med.va.gov"

> port="8000"

> access-code="joe.123"

> verify-code="ebony.432"

> timeout="30"

> always-use-default-as-min="false"

> enabled="true"

> /\>

> \</connectors\>

When an application asks for the JNDI name for the connector for station 11000A, for example, it will get “vlj/testconnector.”

## Accessing Mappings from Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Applications are provided with an API to retrieve a connector's JNDI name, based on a station number. For more information, see the *VistALink 1.5 Developer Guide*.

## Mapping Configuration Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Out-of-Synch Configuration Files on Multiple Physical Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink configuration file (gov.va.med.vistalink.connectorConfig.xml) must be accessible on the JVM classpath of each server with deployed VistALink connectors. Because separate copies of the VistALink configuration file can exist for separate physical servers, it is possible that these copies may not be identical. The primaryStation attributes, on which the institution mapping is based, may be different.

It is the responsibility of the system administrator to keep separate physical copies of the VistALink configuration file synchronized.

### Connector Station and M System Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The primaryStation attribute is used to create the mappings that applications use to retrieve the connector. It is always possible to misconfigure a connector, associating it with the wrong station number. Station mismatch checking is employed to catch such configuration errors.

When VistALink connects to an M system, the primaryStation attribute of the connector is passed to M. It is then checked against the DEFAULT INSTITUTION field of the Kernel System Parameters file. If it doesn't match, the connection is rejected, and a SecurityPrimaryStationMismatchException is returned to the application.

The system administrator should monitor the VistALink console and log files for indicators of rejected connections due to primary station mismatches.

### JNDI Name Configuration Mismatch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The jndiName attribute in the VistALink configuration file is used to associate a station number with a particular connector. However, the JNDI name under which WLS deploys the connector comes from the \<jndi-name\> element in the weblogic-ra.xml file. If these two values don't match, the mapping will not reflect the correct JNDI name for the connector.

Runtime checking validates whether these values are the same. If they are not, attempts to use the connector will return a VistaLinkResourceException to the application. In addition, the VistALink console will display a warning if it sees these values do not match for a given connector.

The two JNDI settings are in the weblogic-ra.xml deployment descriptor and the gov.va.med.vistalink.connectorConfig.xml file. When these settings are out of synch, the result should be an unusable connection (outright failure), rather than an incorrectly routed connection, which is harder to diagnose.

The system administrator should monitor the VistALink console and log files for indicators of rejected connections due to JNDI name mismatches.

### Mappings with Undeployed Connectors (Stopped or Deleted)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mappings are marked for removal when a connector is undeployed. However, the actual removal of the mappings does not happen until garbage collection runs on the server.

If a connector has been undeployed and garbage collection has not yet run, the attempted use of the connector will fail at the point the application attempts to retrieve the connection factory from JNDI. If garbage collection has run, the attempted use of the connector will fail when no JNDI name can be returned for the given station number. In both cases, the attempt to use the undeployed connector will fail.

## Console Navigation Tree

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink console plug-in adds a new branch (called “VistALink”) to the standard WebLogic console navigation tree:

> ![](vistalink-version-1-5-system-management-guide/011.png)

<span id="_Toc98317604" class="anchor"></span>Figure 2. VistALink Console Navigation Tree

## Server-Specific Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under the VistALink Servers node, the navigation tree displays one node for each server in your WebLogic configuration. You can use these nodes to display information about VistALink deployments on a specific server. Because deployments are per server, deployment and status information may vary between servers.

When you click on a server node, a page is displayed with two tabs:

- VistALink Deployed Connectors
- Institution Mappings

### VistALink Deployed Connectors Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information provided on this tab can be helpful for monitoring and troubleshooting connectors. This part of the console also provides an easy way to exercise each connector to see if any error conditions are present, and whether a live call can be made successfully.

This tab of the console provides:

- A summary list of deployed VistALink connectors, including health indicators and other summary information for each.
- A detail page for each connector showing:
  - WebLogic-specific configuration information
  - VistALink-specific configuration information, including the institution mappings associated with the connector
  - Health monitoring indicators
  - Performance monitoring indicators
  - Live VistALink M/VistA Server Query, with results.

> To access the detail page, you click on the connector name.

> When the detail page is loaded for any connector, a "live" call is made to the M system. The results provide an easy way to get a picture of the M system connected to, and may also help verify whether a connector is reaching the *intended* M system. The results include the remote UCI, volume, M version and OS, domain, production setting, and introductory text.

In both views, the following Health Indicators/Failure Counts are provided for each connector:

- JNDI Mismatch: Indicates that the JNDI name used to look up the connector settings in the VistALink configuration file does not match the JNDI name from ra.xml, used by the container to deploy the connector, which could indicate a misconfigured connector.
- Connection Failure Count: The number of times, since deployment or server re-start, that an attempt to create a physical connection to the M system has failed.
- Connection Authentication Failure Count: The number of times, since deployment or server restart, that the connector has attempted and failed to log on to the M system with the connector user access/verify code.
- Production Mismatch Count: The number of times since deployment or server restart that the connector has attempted to log on to the M system and found a mismatch between the Production settings for the M system and the J2EE server's JVM. On the J2EE server, this setting is controlled via the gov.va.med.environment.production JVM argument.
- Division Mismatch Count: The number of RPC requests since deployment or server restart that have failed because the division specified in the RPC request is not legal for the re-authentication user. A large number of division mismatches may indicate a misconfigured JNDI-to-institution mapping for the connector in question.
- Identity Failure Count: The number of times since deployment or server restart that re-authentication has failed when attempting to execute RPCs on behalf of users. A large number of failures may indicate a misconfigured JNDI-to-institution mapping for the connector in question.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](vistalink-version-1-5-system-management-guide/012.png)</td>
<td><p>For the connector portion of the console to function correctly, the JVM argument <strong>gov.va.med.environment.servertype</strong> must be passed with a value of “weblogic” to all WebLogic JVMs deploying resource adapters (connectors). Depending on your WebLogic domain configuration, the set of servers may include managed servers, admin servers, or both.</p>
<p>Example:</p>
<blockquote>
<p>-Dgov.va.med.environment.servertype=weblogic</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Institution Mappings Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This tab of the console lists the currently loaded institution mappings on the selected server. For example:

> Station \#  JNDI Name

> 11000  vlj/testconnector

You can use this information to verify the institution mappings on your server(s).

### Working with Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Loading Files

Configuration files can be loaded into the editor from three sources:

- Server Classpath: If a file named "gov.va.med.vistalink.connectorConfig.xml" is found in a folder on the admin server classpath, the Configuration Editor loads the contents of this file automatically. When changes are made and saved, they are saved to this file on the admin server.
- Upload File: You can upload a file from the client workstation to the configuration editor running on the admin server. To upload a file, use the Upload File button. Changes can only be saved back to the client workstation by downloading.
- Create New: If the gov.va.med.vistalink.connectorConfig.xml file is not found on the server classpath, you can create a new one in the Configuration Editor. In this case, you are given the option to "Create a new configuration file". This file is in-memory: it cannot be saved to the server, but it can be downloaded to the client workstation.

#### Changing File Sources

Some points to observe when changing file sources:

- You cannot create a new file if there is a folder containing the file gov.va.med.vistalink.connectorConfig.xml on the server classpath. (Otherwise, gov.va.med.vistalink.connectorConfig.xml is automatically loaded).
- You can upload a new file to the configuration editor in any edit mode (Server Classpath, Upload File, Create New).
- Once you upload a file, you cannot switch to Create New mode unless you close your browser and reopen it.
- Once you either upload or create a new file, you cannot switch to editing the gov.va.med.vistalink.connectorConfig.xml file that is automatically loaded from a folder on the server classpath, unless you close your browser and reopen it.

#### Saving Files

Some points to understand when saving files:

- Server Classpath: If the configuration file is loaded from the server classpath, click Apply to save changes. The file is saved in the same location it is loaded from.
- Upload File and Create New: These files are created in-memory and cannot be saved to the admin server. However, they can be downloaded back to the client workstation. Click Apply before downloading to save changes in the in-memory copy.

#### Downloading Files

You can download a file from the admin server to your client workstation in any of the three edit modes (Server Classpath, Upload, Create New):

1.  Make sure you click Apply to save all your changes in the in-memory copy of the configuration file first.
2.  Click the Download File button to download the file to your workstation.

### Adding and Deleting Connectors

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Add Connector and Delete Connector buttons can be used to add or delete connectors from the configuration file. This functionality can also be accessed by right-clicking on the connector tree, shown in the following figure:

> ![](vistalink-version-1-5-system-management-guide/016.png)

> <span id="_Toc97010543" class="anchor"></span>Figure 6. Adding and Deleting Connectors

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vistalink-version-1-5-system-management-guide/017.png) | Adding a connector does not auto-save the configuration file, giving users an opportunity to edit the properties of the newly created connector. Deleting a connector does (by default) automatically save the file. This can be controlled by the Auto save the delete operation checkbox, located in the lower left hand corner of an Advanced pane. |

## Avoiding "Graceful Shutdown" Delays on the Admin Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the VistALink Console application is deployed on your admin server, you will see delays after requesting a “graceful shutdown”. These delays will be accompanied by notices such as the following:

> \<Feb 24, 2005 1:41:39 PM EST\> \<Notice\> \<HTTP\> \<BEA-101277\> \<Web application(s) VistaLinkConsole-1.5.0 has 1 non-replicated session(s) respectively.\>

> \<Feb 24, 2005 1:41:39 PM EST\> \<Notice\> \<HTTP\> \<BEA-101275\> \<Server has detected non-replicated sessions while SUSPENDING. Server will wait for non-replicated sessions to either become invalidated or timed out; or will choose a secondary in the case of in-memory replicated sessions. The current timeout value is 3,600 seconds. To terminate non-replicated sessions immediately, use the FORCESHUTDOWN option.\>

These delays will affect the admin server only, not managed servers that may be in your configuration. To avoid the delays, do one of the following:

- Do a “force shutdown” of the admin server instead of a graceful shutdown
- Before shutting down the admin server, check Ignore Sessions During Shutdown on the WebLogic Console’s Control \| Startup page for the admin server. (It will be remembered for future shutdowns.) This will allow you to shut down the admin server gracefully without delays.

## Finding VistALink Processes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On VMS systems, the listener for any active VistALink connection is typically configured to be launched via VMS TCP Services. VistALink sets the VMS process name to “VLink_XXXXXXXX”, where “XXXXXXXX” is the value of the M \$J converted to hex.

This makes it easier to find which VMS processes are associated with VistALink, and with which M job as well. You can use the DCL command SHOW SYSTEM /PROC=VL to display all VistALink processes. For example:

core\$ show sys /proc=VL\*

OpenVMS V7.3-2 on node ISC1A4 1-MAR-2005 10:19:47.64 Uptime 146 10:17:35

Pid Process Name State Pri I/O CPU Page flts Pages

20F9B10B VLINK_BG1877 HIB 11 179 0 00:00:00.01 202 184 N

20F9F90C VLink_20F9F90C LEF 11 211 0 00:00:00.11 4186 852 S

20FA190D VLINK_BG1891 HIB 11 172 0 00:00:00.04 202 184 N

20F9890E VLink_20F9890E LEF 10 211 0 00:00:00.10 4310 865 S

20F9C90F VLINK_BG1910 HIB 11 172 0 00:00:00.01 202 184 N

20F9C910 VLink_20F9C910 LEF 10 211 0 00:00:00.09 4231 852 S

core\$

### Non-VMS Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list VistALink processes on non-VMS systems (e.g. Caché on Windows), you can look for processes that are frequently in the XOBVSKT routine; these processes are VistALink listeners. (However, when RPCs are invoked, the routine listed will be different.)

## Normal Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In general, to troubleshoot any problem, you should check the following sources:

- WebLogic server log file for your domain:

> \<USER_DOMAIN_HOME\>/\<MY_DOMAIN_NAME\>.log

For example:

> C:\bea\user_projects\domains\mydomain\mydomain.log)

- VistALink log4j file log for your domain, based on the log4j configuration file specified in D/log4j.configuration JVM arguments.
- M-side error trap(s) for the M system(s) involved (D ^XTER)

## Request Timestamp

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is a new variable that developers and sites can use for debugging:

> XOBLASTR Timestamp of last time any request was made on connection

Developers and site administrators can use this variable via JOBEXAM or the Cache console to watch activity and determine “dead” connections.

## M Error Trap

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you look through the M error trap, you may see errors with no “subject” line.

Such errors may have been logged by VistALink to note a fault condition detected by the listener. Unfortunately, at the present, there is no easy way to add a non-M fault to the error log and still have the subject show.

If you see an error log entry without a subject, enter XOBSTR at the “Which symbol? \>” prompt. If the log entry is VistALink-related, that variable will be defined in the error trap, and its value should be an error message describing the fault condition encountered.

Example:

> 4)                       13:08:13 VISTALINK,ROU 553187626 BG875

> …

> Which symbol? \> XOBSTR

> XOBSTR=Primary station &apos;&apos; of the request does not match the primary station &apos;11000&apos; of the M/Kernel system.

## Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information about log file exceptions, look up the exception class names in the VistALink Javadoc.
