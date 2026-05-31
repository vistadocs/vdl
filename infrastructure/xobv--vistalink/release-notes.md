---
title: VistALink Version 1.6 Release Notes
doc_type: RN
doc_label: Release Notes
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
file_numbers: []
security_keys: []
menu_options: 0
description: '| | | | | |-----------------------------------------------------|---------------------------------------------|--------------------------------------------|-------------------------------------------| | Revision History Date | Revised Pages | Patch Number | Description | | 10/24/2019 | N/A |...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 3993
section_count: 34
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: October 2019
revision_count: 0
revision_newest: null
revision_oldest: null
docx_url: https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_rn.docx
pdf_url: https://www.va.gov/vdl/documents/Infrastructure/VistALink/vistalink_1_6_rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=163
audit_applied: '2026-05-31'
master_source: VistALink Version 1.6 Release Notes
master_pub_date: October 2019
consolidated_from: 3 versions
prior_versions:
- VistALink Version 1.5 Release Notes
- VistaLink Version 1.6.7 Release Notes
consolidated_title: vistalink release notes
---

![](vistalink-version-1-6-release-notes/001.png)

VISTALINKRELEASE NOTES

October 2019

Office of Information and Technology

Product Development

|                                                     |                                             |                                            |                                           |
|-----------------------------------------------------|---------------------------------------------|--------------------------------------------|-------------------------------------------|
| <span class="mark">Revision History Date</span> | <span class="mark">Revised Pages</span> | <span class="mark">Patch Number</span> | <span class="mark">Description</span> |
| 10/24/2019                                          | N/A                                         | XOBV/XOBS\*1.6\*4                          | No Changes                                |
| 01/14/2019                                          | 6-2                                         | XOBV/XOBS\*1.6\*3                          | Added 2 factor authentication RPC call.   |

Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [About VistALink](#about-vistalink)
  - [WebLogic Updates Project](#weblogic-updates-project)
  - [New Product Web Site](#new-product-web-site)
  - [For More Information](#for-more-information)
- [M Updates](#m-updates)
  - [Include Client IP address in error traps for Failed Connections](#include-client-ip-address-in-error-traps-for-failed-connections)
  - [Elimination of SETMSG+5^XOBVRH (Telnet Connection) Hard Error](#elimination-of-setmsg5xobvrh-telnet-connection-hard-error)
  - [Added Support for Launching Cache/Linux Listeners via XINETD](#added-support-for-launching-cachelinux-listeners-via-xinetd)
  - [New Connection Manager (aka 'Zapper')](#new-connection-manager-aka-zapper)
- [VistALink Adapter Updates](#vistalink-adapter-updates)
  - [WebLogic 9/10 Compatibility](#weblogic-910-compatibility)
  - [RAR Changes Summary since Previous Version](#rar-changes-summary-since-previous-version)
  - [New Recommendation: Deploy VistALink Jars as J2EE Shared Libraries (Production Systems Only)](#new-recommendation-deploy-vistalink-jars-as-j2ee-shared-libraries-production-systems-only)
  - [Revised VistALink MBeans](#revised-vistalink-mbeans)
  - [VistALink Adapters No Longer Cache DNS Lookups for M Systems](#vistalink-adapters-no-longer-cache-dns-lookups-for-m-systems)
  - [Automatic ServerType Detection](#automatic-servertype-detection)
  - [Updated Sample log4j Configuration Files](#updated-sample-log4j-configuration-files)
  - [Added Support Needed to Connect to VistALink Listeners Through an SSH (Secure Shell) Tunnel](#added-support-needed-to-connect-to-vistalink-listeners-through-an-ssh-secure-shell-tunnel)
    - [Security: SSH Needs Client IP Address](#security-ssh-needs-client-ip-address)
    - [Added Support for Deployment Toolkit](#added-support-for-deployment-toolkit)
- [Institution Mapping Updates](#institution-mapping-updates)
  - [Leading '0' Allowed in Primary Station Number](#leading-0-allowed-in-primary-station-number)
  - [Elimination of primaryStationSuffix Attribute](#elimination-of-primarystationsuffix-attribute)
  - [New Pluggable Institution Mapping Rules](#new-pluggable-institution-mapping-rules)
- [# VistALink Administration Console Updates](#vistalink-administration-console-updates)
  - [WebLogic 9/10 Compatibility](#weblogic-910-compatibility-1)
  - [WebLogic 10.3 Compatibility](#weblogic-103-compatibility)
  - [Console Honors Monitor Role Restrictions](#console-honors-monitor-role-restrictions)
  - [Configuration Editor Access/Verify Code Encryption Changes](#configuration-editor-accessverify-code-encryption-changes)
  - [Elimination of the Upload/Download Configuration File Feature](#elimination-of-the-uploaddownload-configuration-file-feature)
  - [New JNDI Name Recommendations](#new-jndi-name-recommendations)
- [# Developer API Updates](#developer-api-updates)
  - [Exception Nesting Changes in VistALink 1.6](#exception-nesting-changes-in-vistalink-16)
  - [VistALink Deprecated APIs](#vistalink-deprecated-apis)
  - [VistALink New APIs](#vistalink-new-apis)
- [Pursuant to Memorandum for Implementation of Federal Personal Identity Verification (PIV) Credentials for Federal Employee and Contractor Access to VA IT Systems (VAIQ# 7614373) 2 Factor Authentication (2FA) was implemented to connect to a VistA system, VistALink is being updated to add an RPC that accepts the SAML token and validates the user log on in the same manner as the RPC Broker software does for web applications. RPC XOBV VALIDATE SAML calls tag SAML for routine XOBVSAML then returns an ARRAY that either contains the users DUZ if successful, or returns "1^error message" and subsequent failure or success messages for the consuming application in the lower subscripts. The RPC receives a SAML token to validate a user logon to VistA of type literal specified as parameter DOC that is the SAML token with a maximum data length of 32000 characters.](#pursuant-to-memorandum-for-implementation-of-federal-personal-identity-verification-piv-credentials-for-federal-employee-and-contractor-access-to-va-it-systems-vaiq-7614373-2-factor-authentication-2fa-was-implemented-to-connect-to-a-vista-system-vistalink-is-being-updated-to-add-an-rpc-that-accepts-the-saml-token-and-validates-the-user-log-on-in-the-same-manner-as-the-rpc-broker-software-does-for-web-applications-rpc-xobv-validate-saml-calls-tag-saml-for-routine-xobvsaml-then-returns-an-array-that-either-contains-the-users-duz-if-successful-or-returns-1error-message-and-subsequent-failure-or-success-messages-for-the-consuming-application-in-the-lower-subscripts-the-rpc-receives-a-saml-token-to-validate-a-user-logon-to-vista-of-type-literal-specified-as-parameter-doc-that-is-the-saml-token-with-a-maximum-data-length-of-32000-characters)
- [J2SE Client/Server Updates](#j2se-clientserver-updates)
  - [Java 5 or Greater Required](#java-5-or-greater-required)
  - [Elimination of Unnecessary J2SE Logger Error-Level Message](#elimination-of-unnecessary-j2se-logger-error-level-message)
  - [CCOW User Context Update](#ccow-user-context-update)
  - [Smaller Geronimo Jar Replaces Need for J2EE/WebLogic Jar for Clients](#smaller-geronimo-jar-replaces-need-for-j2eeweblogic-jar-for-clients)
  - [Section 508 Compliance: Differentiate Focus on Change Verify Code Check Box](#section-508-compliance-differentiate-focus-on-change-verify-code-check-box)

## About VistALink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink resource adapter is a transport layer that provides communication between Health*<u>e</u>*Vet-VistA Java applications and VistA/M servers, in both client-server and n-tier environments. It is a runtime and development tool that allows java applications to execute remote procedure calls (RPCs) on the VistA/M system and retrieve results, synchronously. VistALink is also referred to as VistALink J2M.

VistALink consists of Java-side adapter libraries and an M-side listener:

- The adapter libraries use the Java 2 Enterprise Edition (J2EE) Connector Architecture (J2CA) 1.5 specification to integrate Java applications with legacy systems.
- The M listener process receives and processes requests from client applications.
- Java applications can call Remote Procedure Calls (RPCs) on the M server, executing RPC Broker RPCs on the M server without modification.

## WebLogic Updates Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In support of the Department of Veterans Affairs Information Technology application Modernization effort, the three applications VistALink, Fat-client Kernel Authentication and Authorization (FatKAAT), and Kernel Authentication and Authorization for the Java 2 Enterprise Edition (KAAJEE) have been developed. Based on the direction of the Technical Review Model (TRM) and in order to support applications that upgrade to the new WebLogic Server versions 9.2 and 10.x, this project is required. The scope of the project is to upgrade these three applications to work with the WebLogic Server versions 9.2, 10.x, and 11g.

The previous version of VistALink, 1.5, was released in June of 2006, and provided project developers with J2EE and Java Platform, Standard Edition (J2SE) application connectivity to VistA/M servers. It was designed specifically for J2EE 1.3 application servers (e.g., WebLogic 8.1).

## New Product Web Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New VistALink Web site REDACTED summarizes VistALink architecture and functionality and gives status updates for all VistALink products.

## For More Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For more information on any new feature discussed in the release notes, please see the VistALink documentation set on the VA Software Document Library at the following address:

> <u><http://www.va.gov/vdl/application.asp?appid=163></u>

# M Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Include Client IP address in error traps for Failed Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For failed connections (e.g., when a port scanner or telnet client tries to connect to your listener) where an error is logged, the variable XWBTIP is now defined in the error trap, and contains the client IP address. This will help VistA sites determine the source of the errors/connection failures.

## Elimination of SETMSG+5^XOBVRH (Telnet Connection) Hard Error 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Formerly when connecting to a VistALink listener via telnet (e.g., to test listener connectivity) a hard M error (SETMSG+5^XOBVRH) would be set into the Kernel error trap. Now a "soft" error (dialog \#184001) is displayed and logged in the error trap instead.

## Added Support for Launching Cache/Linux Listeners via XINETD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new entry point has been added (CACHELNX^XOBVTCP) for operations staff to support running VistALink listeners at the Linux operating system level via xinetd, when running Caché on Linux. As this still an M system configuration that VA OI&T is experimenting with at the time of writing, VistALink's support is also experimental at the current point in time.

## New Connection Manager (aka 'Zapper')

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new "Connection Manager" functionality in VistALink 1.6 provides a UI screen to view all VistALink processes connected to the M system, including the associated user, and actions to kill either a selected process or all connected VistALink processes. This functionality may be useful during software installations, for example, where it might be desirable to get all VistALink processes off of the system.

# VistALink Adapter Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## WebLogic 9/10 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6 adapters have been updated to be compatible with:

- WebLogic 9.2, 10.x and 11g
- Java 5
- J2EE 1.4+
- J2EE Connector Architecture 1.5

## RAR Changes Summary since Previous Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- vljFoundationsLib and vljConnector jars: New versions provide a J2CA 1.5 compliant adapter implementation.
- Deployment Descriptor Changes: The format of both the ra.xml and weblogic-ra.xml descriptors is different. Existing adapters' deployment descriptors need to be updated. Using the provided sample/template descriptors, only weblogic-ra.xml will need to be modified when creating a VistALink RAR:
  - META-INF/ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. In most cases, it no longer needs any further editing when creating a RAR.
  - META-INF/weblogic-ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. It must be edited for each RAR deployed.
  - META-INF/MANIFEST.MF: The template version provided in the VistALink distribution is updated to support use of J2EE Shared Libraries by RARs.
- lib/saxpath.jar, lib/jaxen-core.jar, and lib/jaxen-dom.jar are no longer needed in the RAR as their functionality has been replaced by the XPath implementation introduced in Java 5.
- lib/xbean.jar no longer needed in the RAR since an implementation of XML Beans is included in WebLogic 9/10.
- Linked adapters (link-ref mechanism) no longer supported for VistALink 1.6 adapters.
- Development System Classloading: Automatic classloading of all jars in RAR is now supported by WebLogic 9.x/10. Library jars included in RAR no longer need to be manually added to the server classpath.
- Production System Classloading: Oracle (formerly known as BEA) recommends removing all jars from RARs on production systems, and deploying them as J2EE shared libraries instead (to reduce resource consumption – replacement for resource-saving aspect of the 8.1 link-ref mechanism). When deployed as J2EE shared libraries, the jars supporting VistALink RARs no longer need to be manually added to the server classpath.

## New Recommendation: Deploy VistALink Jars as J2EE Shared Libraries (Production Systems Only)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a replacement for the WebLogic 8.1 "Linked Adapters" feature (not supported for upgraded adapters like VistALink 1.6), Oracle recommends removing all jars from RARs on production systems, and deploying each one as a J2EE shared library instead. This addresses the reduced resource consumption benefit formerly provided by using the 8.1 link-ref mechanism. Therefore, on production systems only, we recommend that the following jars be removed from all RARs and deployed (once) as J2EE shared libraries:

| Jar Name                | J2EE Shared Library Deployment Name |
|-----------------------------|-----------------------------------------|
| vljConnector-1.6.0.jar      | vljConnector(1.6,1.6)                   |
| vljFoundationsLib-1.6.0.jar | vljFoundationsLib(1.6,1.6)              |
| log4j-1.2.13.jar            | log4j-1                                 |

Two different versions of an example RAR are provided in the distribution zip file, one structured for development system deployments, the other for production deployments:

- <u>rar\Rar-Dev</u> (contains all needed jars)
- <u>rar\Rar-Prod</u> (contains no jars; MANIFEST.MF file looks for jars as J2EE shared libraries)

## Revised VistALink MBeans

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink MBeans have been revamped, with one MBean per running adapter, allowing third-party management tools to more easily monitor on VistALink-specific error thresholds (e.g., authentication failures). VistALink provides two MBean types that can be monitored:

- VistaLinkConnector MBean

> Deployed: One per deployed VistALink adapter, per JVM

> MBean Type: VistaLinkConnector

> ObjectName: gov.va.med:Name=VistaLink_xxxxx,Type=VistaLinkConnector  
> (where xxxxx is the JNDI name of the adapter)

- VistaLinkInstitutionMapping MBean

> Deployed: One instance per JVM where VistALink adapters are deployed

> Type: VistaLinkInstitutionMapping

> ObjectName: gov.va.med:Name=VistaLinkInstitutionMapping,Type=  
> VistaLinkInstitutionMapping

## VistALink Adapters No Longer Cache DNS Lookups for M Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A major area of concern with VA facility system administrators using VistALink has been updating VistALink adapters based on DNS updates for M systems. In VistALink 1.5, adapters cached DNS information obtained for an M system, and that information stayed cached until either the J2EE system restarted or the adapter was undeployed/redeployed.

In 1.6, VistALink adapters no longer cache DNS lookups. As long as the underlying JVM is also configured to not cache DNS lookups (by default it is not!), VistALink 1.6 adapters will always use a live DNS lookup each time a new connection is created.

## Automatic ServerType Detection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

J2EE server type detection is now automatic for WebLogic servers. Passing the JVM argument -Dgov.va.med.environment.servertype=weblogic is no longer necessary on WebLogic servers in most configurations. If passed, however, the JVM argument still overrides automatic detection. The gov.va.med.environment.Environment getServerType() Application Program Interface (API) does auto-detection (for WebLogic only) \by examining the classloader hierarchy.

## Updated Sample log4j Configuration Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The names and purposes of the sample log4j config files in the distribution have changed with the move to WebLogic 9.x/10. The new sample log4j configuration files are located in the log4j directory inside the VistALink distribution zip file, as follows:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 65%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File Name</strong></td>
<td><strong>Description</strong></td>
</tr>
<tr class="even">
<td>log4jSampleJ2EEConfig.xml</td>
<td><p>Example configuration for a J2EE system, turning DEBUG-level logging on for VistALink classes of interest on a J2EE system.</p>
<p>NOTE: Turning on 'debug' level can adversely affect system performance.</p></td>
</tr>
<tr class="odd">
<td>log4jSampleJ2SEConfig.xml</td>
<td>Example configuration for a J2SE (Java client-M server) application, turning DEBUG-level logging on for VistALink classes of interest for client/server applications.</td>
</tr>
</tbody>
</table>

## Added Support Needed to Connect to VistALink Listeners Through an SSH (Secure Shell) Tunnel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security: SSH Needs Client IP Address

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pilot work done using Secure Shell (SSH), allowing data to be exchanged using a secure channel between two networked devices, revealed that the client IP address must be explicitly passed from the client. VistALink has been updated to do this, similar to how the Remote Procedure Call (RPC) Broker handles client IP address detection.

### Added Support for Deployment Toolkit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Restructured the ZIP file based on recommendations to support Deployment Toolkit (DTK) functionality for WebLogic Application Server 9.x/10.x.

# Institution Mapping Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Leading '0' Allowed in Primary Station Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

"Primary Stations" for connector configurations can now start with '0' (e.g., to match a primary station of '050' as configured in the FOIA Caché distribution.)

## Elimination of primaryStationSuffix Attribute

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The rarely-used *primaryStationSuffix* connector attribute (for AITC 200-series station numbers, in the gov.va.med.vistalink.connectorConfig.xml file) no longer necessary. This change should affect only the Austin Information Technology Center (AITC) 200-series (i.e., AITC) station numbers. Any such primary station numbers should now be entered entirely within the "primaryStation" attribute in the configuration file, including any suffix (e.g., '200M').

## New Pluggable Institution Mapping Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New for non-VA users of VistALink: Organization-specific rules for parsing primary station numbers (validity checking and lookup) are now externalized in a new IPrimaryStationRules implementation. Non-VA users of VistALink can provide their own implementation, and override the default VA-specific rules implementation via a new JVM argument, "-Dgov.va.med.vistalink.primary-station-rules-class".

# # VistALink Administration Console Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## WebLogic 9/10 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WebLogic's console plug-in mechanism changed from 8.1 to versions 9.x/10. The VistALink console plug-in has been updated to be compatible with WebLogic 9.x/10.

## WebLogic 10.3 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to difficulties encountered integrating the VistALink administration console with the WebLogic 10.3 console (specifically its navigation tree and tab set), the VistALink administration console is also provided as a standalone web application, in an EAR file. Therefore, for WebLogic 10.3 we recommend installing the VistALink administration console as a standalone web application, not integrated with the WebLogic console. The standalone EAR can also be used on 9 and 10.0 of WebLogic if desired.

## Console Honors Monitor Role Restrictions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

WebLogic's console supports four roles: Administrators, Deployers, Operators and Monitors. The 1.5 VistALink administration console did not distinguish between these roles, particularly the Monitors role, and it allowed write access (i.e., VistALink's configuration editor) to the otherwise read-only Monitors role. The 1.6 VistALink administration console restricts users in the Monitors role to read-only access.

> **NOTE:** To support access by users in the Monitors role, the system administrator currently needs to explicitly declare the "Listen Address" attribute in the WebLogic domain configuration, for each server in the domain. Otherwise a JMX remote call that is needed, fails, under Monitor privileges alone.

## Configuration Editor Access/Verify Code Encryption Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Encryption of the access and verify codes in the configuration file (gov.va.med.vistalink.connectorConfig.xml) adds an additional level of security to help protect connector proxy user credentials. The access/verify code connector attributes in the configuration file are encrypted when:

- A specific connector configuration is loaded by a deployed adapter on a given J2EE server
- A specific connector definition is edited or created inside the Configuration Editor

In addition, the following new encryption-related features have been added to the 1.6 VistALink administration console:

- The number of currently unencrypted entries in the configuration file is listed on the main Configuration Editor page
- An "Encrypt Unencrypted Entries" button allows you to encrypt all unencrypted entries

A new encryption type ("scoped") has been added:

- "scoped" encryption type changes the encryption of access codes to include a WebLogic domain-specific token, making it harder to decrypt the access/verify codes in a WebLogic domain other than the one the configuration file was encrypted in.
- The new file-wide \<connectors\> attribute "encryptionScoped" in gov.va.med.vistalink.connectorConfig.xml reflects whether entries have been encrypted with domain-scoped encryption or not.
- New console action to change encryption type to scoped. The original encryption type ("not scoped") is supported as well.
- When the console is used to change the encryption type, it will decrypt and then re-encrypt all currently encrypted access/verify codes, and also change the new "encryptionScoped" file-wide attribute to "true".

## Elimination of the Upload/Download Configuration File Feature

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The configuration file upload/download feature is no longer supported in the new VistALink administration console.

## New JNDI Name Recommendations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend that the JNDI name should not contain most punctuation characters. If editing the JNDI name with the Configuration Editor, the following punctuation characters are allowed: - \_ / \\ ( ) \[ \]

Additionally, we recommend not using the '/' punctuation character if you plan to write WLST scripts to monitor VistALink MBeans (in WLST this character is used for another purpose that interferes with accessing an MBean, and VistALink MBean names are based on adapter JNDI names.)

# # Developer API Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Exception Nesting Changes in VistALink 1.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous versions of VistALink were designed to work with Java version 1.3, which did not support nested exceptions. To compensate, nested exception capability was built into all VistALink exception classes.

Now that Java versions 1.4 and above support nested exceptions "out of the box", VistaLink's nested exception facilities have been deprecated, and VistALink's classes have been internally modified to store nested exceptions using Java's nested exception functionality instead.

Any code that currently relies on VistALink's deprecated nested exception facilities to obtain nested exception information should switch to using the now-standard Java nested exception facilities.

## VistALink Deprecated APIs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following APIs have been marked for deprecation in VistALink 1.6:

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

## VistALink New APIs 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Pursuant to Memorandum for Implementation of Federal Personal Identity Verification (PIV) Credentials for Federal Employee and Contractor Access to VA IT Systems (VAIQ# 7614373) 2 Factor Authentication (2FA) was implemented to connect to a VistA system, VistALink is being updated to add an RPC that accepts the SAML token and validates the user log on in the same manner as the RPC Broker software does for web applications. RPC XOBV VALIDATE SAML calls tag SAML for routine XOBVSAML then returns an ARRAY that either contains the users DUZ if successful, or returns "1^error message" and subsequent failure or success messages for the consuming application in the lower subscripts. The RPC receives a SAML token to validate a user logon to VistA of type literal specified as parameter DOC that is the SAML token with a maximum data length of 32000 characters.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# J2SE Client/Server Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Java 5 or Greater Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because VistALink 1.6's jars, used both on WebLogic 9/10, and for client/server connectivity, are compiled with Java 5, new client/server applications using VistALink 1.6 will need to be compiled with and run under a minimum of Java 5 as well.

## Elimination of Unnecessary J2SE Logger Error-Level Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An unnecessary error-level log4j log message meaningful for J2EE environments only is no longer logged when running in client/server mode in a J2SE environment.

## CCOW User Context Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CCOW logins now add in the user's DUZ(2) as a second "^"-piece in the user.id.logon.vistalogon context item, for both client/server and FatKAAT logins. Doing this makes VistALink consistent with the RPC Broker's user context population, and supports functionality needed by FatKAAT.

## Smaller Geronimo Jar Replaces Need for J2EE/WebLogic Jar for Clients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistALink distribution now includes a small jar (37K), geronimo-j2ee-connector_1.5_spec-1.1.1.jar, from the Apache Geronimo J2EE server. Distribution of this jar completely satisfies VistALink's need on the J2SE client side for an implementation of J2EE's javax.resource.ResourceException class, replacing the former need for J2SE installers to either place weblogic.jar on the client side, or go to the Sun web site and download the Sun App Server, to obtain a single (large) file, j2ee.jar. Neither Sun's j2ee.jar nor weblogic.jar had been included in previous VistALink distributions for two reasons, 1) licensing restrictions, and 2) size.

## Section 508 Compliance: Differentiate Focus on Change Verify Code Check Box

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to a known defect in Java Swing ([<u>http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4985801</u>](http://bugs.sun.com/bugdatabase/view_bug.do?bug_id=4985801)), and as defined by Section 508 compliance, it might be difficult for end-users to distinguish when focus occurs on the Change Verify Code check box in the login dialog window when using the Windows "Look and Feel" High Contrast Black color scheme.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: VistALink Version 1.5 Release Notes

## J2EE Connector Architecture (J2CA)-Compliant Resource Adapter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first version of VistALink (1.0) supported Java rich clients connecting to M servers, but did not support connectivity from a J2EE middle tier. VistALink 1.5 addresses this need, by adding support for the J2EE Connector Architecture (J2CA), a J2EE standard for integrating J2EE applications with non-J2EE enterprise information systems.

VistALink J2M now provides a J2CA-compliant resource adapter, enabling J2EE-based middle-tier application code to communicate with VistA/M systems. By complying with the J2CA specification, the adapter is able to take care of built-in J2EE platform support for J2CA, including connection pooling.

The VistALink resource adapter is packaged in a Resource Adapter Archive (RAR), in both exploded and packaged formats.

## J2EE Connector Proxy User Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *connector proxy user* is the M server's primary gatekeeper for controlling access to M from the new VistALink J2CA resource adapter. This is a special user class in the Kernel NEW PERSON file (#200). Only J2EE connectors configured by IRMs with credentials for "connector proxy" Kernel users can connect to an M VistALink listener. Once a connection is established through a connector proxy user, J2EE applications on the J2EE server can execute a variety of RPCs on the M server under a variety of end-user identities.

VistALink leverages the connector proxy functionality and security features of Kernel patch XU\*8.0\*361. The Foundations menu has a new menu option to create a connector proxy user. The menu option wraps the CONT^XUSAP entry point.

## J2CA Re-Authentication Connection Specification Types 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using the VistALink J2CA connector, it is the J2EE application's responsibility to specify (re-authenticate) the end-user identity with which to execute each remote procedure call (RPC) on the M system.

Several classes in the gov.va.med.vistalink.adapter.cci package support different ways for the J2EE application to identify (re-authenticate) the end user to the M system:

- VistaLinkDuzConnectionSpec (if application knows the user's DUZ, e.g. via logon)
- VistaLinkVpidConnectionSpec (if application knows the user's VPID, e.g. via logon)
- VistaLinkAppProxyConnectionSpec (see *Application Proxy Users,* below)

## Application Proxy Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistaLinkAppProxyConnectionSpec allows the J2EE application to execute RPCs on the M system under the identity of a special application-level *application proxy user*, rather than the actual end-user. Application proxies are expected to be used in either of the following special situations:

- The J2EE end-user does not have a user account on the M system on which an RPC is to be executed, i.e., when a service uses VistALink from an EJB (when an end-user is not practical)
- It is not appropriate for the RPC to execute under the identity of a particular end-user.

Kernel patch XU\*8\*361 is required to support the new functionality.

> **NOTE:** A "tester" application proxy user is distributed with VistALink. It is added to the NEW PERSON file (#200) during the installation post-init, and named "XOBVTESTER,APPLICATION PROXY."

## Institution Mapping API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

J2EE applications retrieve resource adapters from the Java Naming and Directory Interface (JNDI), using a JNDI name. Applications using VistALink J2CA resource adapters usually need a way to retrieve the resource adapter associated with a particular M system. This is because multiple VistALink resource adapters, connecting to different M systems, can be configured on a given J2EE system.

VistALink's institution mapping functionality allows J2EE applications to retrieve the JNDI name of a particular resource adapter, based on the station number of the M system it wishes to connect to. The station number is a piece of information any multi-divisional-aware application is likely to possess. The institution mapping API is provided in the gov.va.med.vistalink.institution.InstitutionMappingDelegate class.

## VistaLinkRequestRetryStrategy API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While executing an RPC, connectivity to the VistA system can fail, due to a network failure or anything else that breaks connectivity. For J2EE applications using the VistALink J2CA resource adapter, the application request's implementation of the VistaLinkRequestRetryStrategy interface determines whether or not VistALink automatically retries the request (by retrieving a new connection from the resource adapter connection pool).

Two default retry strategies are provided: [VistaLinkRequestRetryStrategyAllow](file:///C:\Users\VHAISPLOWERC\v15-026\stage\zip\vlj-1.5.0.026\javadoc\gov\va\med\vistalink\adapter\record\VistaLinkRequestRetryStrategyAllow.html) and  
[VistaLinkRequestRetryStrategyDeny](file:///C:\Users\VHAISPLOWERC\v15-026\stage\zip\vlj-1.5.0.026\javadoc\gov\va\med\vistalink\adapter\record\VistaLinkRequestRetryStrategyDeny.html). The strategy interface is gov.va.med.vistalink.adapter.record.VistaLinkRequestRetryStrategy.

## Environment API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The gov.va.med.environment.Environment API exposes the following environment settings on the J2EE server:

- isProduction – this J2EE setting must match the production/test setting of the M system
- getServerType – currently, this setting is

> JBOSS \| ORACLE \| SUN_RI_13 \| UNKNOWN \| WEBLOGIC \| JAVASE \| WEBSPHERE

The values returned by these APIs are currently controlled by JVM arguments configured by the J2EE system manager.

## WebLogic Console Plug-in to Monitor Resource Adapter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.5 provides a console plug-in for the WebLogic administration console. The VistALink console provides visibility into the internal functioning of VistALink connectors and helps with some VistALink management tasks. The VistALink console runs as an extension in the WebLogic console, on the administration server for a given WebLogic configuration.

The VistALink console provides both summary and detailed views of deployed VistALink resource adapters, as well as the current institution mapping values. The detailed connector view can be used to test the connectivity of the resource adapter, because accessing the detailed view makes calls over the adapter to the corresponding Vista/M system to retrieve information used in the detailed display.

## J2EE Configuration File Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another part of the WebLogic console plug-in is the VistALink configuration editor. It provides a user-friendly interface for editing the VistALink configuration file, which persists configuration settings for each VistALink adapter/connector.

## J2EE Sample Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new VistALink sample Web application demonstrates the use of the VistALink J2CA resource adapter from a J2EE middle tier. It demonstrates use of all of the connection specification types, including VistaLinkAppProxyConnectionSpec.

## Log4J Logger Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink core log4j categories are documented in the spreadsheet provided in the log4j subdirectory of the VistALink distribution file. Each logger category provides a description and notes the supported logger levels (e.g., DEBUG and ERROR). You can use the logger category name(s) to set up loggers in your log4j configuration files, as needed, to log information from specific parts of the VistALink package.

## New M Site Parameters 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new M site parameters are provided for supporting J2EE connectivity:

- J2EE Connection Timeout: This field indicates the number of seconds that a VistALink connection from J2EE to M should be allowed to remain connected when inactive, before M drops the connection.
- J2EE Reauthentication Timeout: This field indicates the number of seconds between 180 and 3600 (inclusive) before a re-authenticated connection is considered expired and must go through the re-authentication process again (default: 600 secs).

Site parameters can be edited using the Site Parameters action in the Foundations menu.

## Modified VLINK.COM files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink M listeners are typically configured as TCP/IP services on VAMC systems, as per HSITES guidance. VistALink VMS .COM files will need to be updated, similar to the modifications now required for Broker, MailMan, and HL7 services.

HSITES has provided a cookbook (VISTALINK_TCPIP_COOKBOOK.DOC) and .COM files to assist VistA/M system managers who need to create the VLINK service or simply modify the existing VLINK service files. For more information, please see the VistALink Installation Guide.

## Specify Any Host/Port in SwingTester Application 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The J2SE sample/test application (gov.va.med.vistalink.samples.VistaLinkRpcSwingTester) now allows ad hoc entry of the IP and port of the target VistALink listener. Previously, an explicit configuration was required in the jaas.config file to connect to a VistALink listener.

## CCOW-Based SSO/UC Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink's client/server mode now supports single sign-on to M systems based on CCOW user context, as implemented by the Office of Information's SSO/UC (Single Sign-On/User Context) project.

For application developers, a new CCOW-enabled JAAS (Java Authentication and Authorization Service) CallbackHandler class (CallbackHandlerSwingCCOW) is provided for the VistaLoginModule class. A new sample application (gov.va.med.vistalink.samples.VistaLinkRpcSwingSimpleCcow) is also provided, to demonstrate the coding necessary to implement CCOW-based SSO/UC support.

### From: VistaLink Version 1.6.7 Release Notes

## WebLogic 12.2 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6.7 adapters have been updated to be compatible with:

- WebLogic 12.2
- Java 1.8
- J2EE 2+
- J2EE Connector Architecture 1.5

## Fortify and TRM Compliance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistALink 1.6.1 codebase have been updated with following noteworthy items:

- Introduced a \*.fortify package
- Implemented Reverse-DNS validation on the IP addresses of targeted M systems at the configuration file \*\*\*
- Reset authentication byte arrays
- Dereferenced null references
- Updated codebase with API references to log4j2 libraries

\*\*\* A Reverse-DNS information validation is now in place. VistALink will not connect to IP address without a reverse dns information in the PTR record.

## Reminder - RAR Changes Summary since Previous Version – 1.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- vljFoundationsLib and vljConnector jars: New versions provide a J2CA 1.5 and VA's TRM compliant adapter implementation.
- Deployment Descriptor Changes: The format of both the ra.xml and weblogic-ra.xml descriptors are different. Existing adapters' deployment descriptors need to be updated. Using the provided sample/template descriptors, only weblogic-ra.xml will need to be modified when creating a VistALink RAR:
  - META-INF/ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. In most cases, it no longer needs any further editing when creating a RAR.
  - META-INF/weblogic-ra.xml: The template version provided in the VistALink distribution is updated to be J2CA 1.5 compliant. It must be edited for each RAR deployed.
  - META-INF/MANIFEST.MF: The template version provided in the VistALink distribution is updated to support use of J2EE Shared Libraries by RARs.
- lib/saxpath.jar, lib/jaxen-core.jar, and lib/jaxen-dom.jar are no longer needed in the RAR as their functionality has been replaced by the XPath implementation introduced in Java 5.
- lib/xbean.jar no longer needed in the RAR since an implementation of XML Beans is included in WebLogic 9 and onward.
- Linked adapters (link-ref mechanism) no longer supported for VistALink 1.6 adapters.
- Development System Classloading: Automatic classloading of all jars in RAR is now supported by WebLogic 10.3.6. Library jars included in RAR no longer need to be manually added to the server classpath.
- Production System Classloading: Oracle (formerly known as BEA) recommends removing all jars from RARs on production systems, and deploying them as J2EE shared libraries instead (to reduce resource consumption – replacement for resource-saving aspect of the 8.1 link-ref mechanism). When deployed as J2EE shared libraries, the jars supporting VistALink RARs no longer need to be manually added to the server class path.

## WebLogic 12.2 Compatibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Due to difficulties encountered integrating the VistALink administration console with the earlier versions of WebLogic (specifically its navigation tree and tab set), the VistALink administration console is provided as a standalone web application, in an EAR file. Therefore, for WebLogic 10.3 we recommend installing the VistALink administration console as a standalone web application, not integrated with the WebLogic console. The standalone EAR can also be used on 12.2 of WebLogic if desired.

## Java 1.8 or Greater Required

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because VistALink 1.6's jars, used on WebLogic 12.2, and for client/server connectivity, are compiled with Java 1.8, new client/server applications using VistALink 1.6 will need to use JDK 1.8 and up.

*This page is left blank intentionally.*
