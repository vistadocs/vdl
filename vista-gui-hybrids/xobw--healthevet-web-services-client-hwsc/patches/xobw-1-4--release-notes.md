---
title: XOBW*1*4 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: 
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
description: HealtheVet Web Services Client (HWSC) Patch XOBW\1.0\4 enables the use of Transport Layer Security/Secure Socket Layer (TLS/SSL) on OpenVMS systems.
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - table
  - contents
  - patch
  - hwsc
  - client
  - healthevet
  - xobw
  - services
  - configuration
  - applications
page_count: 0
word_count: 1165
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p4_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/HealtheVet_Web_Services_Client/xobw_1_0_p4_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=180"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>HealtheVet Web Services Client <span class="smallcaps">(HWSC)</span> 1.0  
  Patch XOBW\*1.0\*4

  Release Notes
---

![](xobw-1-4-release-notes/001.png)

October 2016

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Introduction](#introduction)
- [Purpose](#purpose)
- [Audience](#audience)
- [HealtheVet Web Services Client Patch XOBW\1.0\4](#healthevet-web-services-client-patch-xobw104)
  - [New Features and Functions](#new-features-and-functions)
  - [Enhancements and Modifications to Existing](#enhancements-and-modifications-to-existing)
  - [Known Issues](#known-issues)
  - [Patch Numbering Scheme](#patch-numbering-scheme)
- [Product Documentation](#product-documentation)
<table>
<caption>Table used for formatting purposes, only.</caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 50%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Document Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/05/2023</td>
<td>1.1</td>
<td>Updated for 508 compliance</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/20/2016</td>
<td>1.0</td>
<td><p>HealtheVet Web Services Client (HWSC), Patch XOBW*1.0*4 initial Release Notes document:</p>
<ul>
<li><blockquote>
<p>Installs a Caché SSL/TLS Configuration named “encrypt_only.”</p>
</blockquote></li>
<li><blockquote>
<p>Disables the flag that prevents the configuration and execution of TLS/SSL enabled HWSC web service clients, specifically for OpenVMS.</p>
</blockquote></li>
<li><blockquote>
<p>Disables verification of the remote server's host name. This is something that is enabled by default in Web browsers where a user is interacting with a browser; however, HWSC is a web service client with no user interaction. Also, RFC 2818 allows for disabling this verification when "the client has external information as to the expected identity of the server" to which HWSC applications can be configured to use.</p>
</blockquote></li>
</ul></td>
<td>HealtheVet Web Services Client (HWSC) Project Team</td>
</tr>
</tbody>
</table>
Table used for formatting purposes, only.
Table of Contents

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HealtheVet Web Services Client (HWSC) Patch XOBW\*1.0\*4 enables the use of Transport Layer Security/Secure Socket Layer (TLS/SSL) on OpenVMS systems.

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These release notes cover the changes to the HealtheVet Web Services Client (HWSC) project with patch XOBW\*1.0\*4.

# Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The audience for this document is Veterans Health Information Systems and Technology Architecture (VistA) application developers and Caché System Administrators.

# HealtheVet Web Services Client Patch XOBW\*1.0\*4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previous to this release, HWSC VistA applications were enabled to use Secure Socket Layer/Transport Layer Security (SSL/TLS) configurations to encrypt the connections; however, this worked on Linux systems, only. This feature was disabled in VistA applications on OpenVMS due to a problem with using SSL/TLS on OpenVMS systems. This is no longer the case. Thus, this feature has been enabled consistently on all VistA systems for both Linux and OpenVMS.

## New Features and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HWSC VistA applications can now enable SSL/TLS encryption to work in VistA applications on OpenVMS by referencing the “encrypt_only” SSL/TLS configuration or any new customized SSL/TLS configurations.

## Enhancements and Modifications to Existing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch XOBW\*1.0\*4 makes the following enhancements to HWSC:

- Installs a Caché SSL/TLS Configuration named “encrypt_only” using SSL Version 3.
- Disables the flag that prevents the configuration and execution of TLS/SSL enabled HWSC Web service clients, specifically for OpenVMS.
- Disables verification of the remote server's host name. This is something that is enabled by default in Web browsers in which a user is interacting with a browser; however, HWSC is a Web service client with no user interaction. Also, RFC 2818 allows for disabling this verification when "the client has external information as to the expected identity of the server," which HWSC applications can be configured to use.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The TLS/SSL configuration *must* be installed in all nodes of a VistA system, both front-end server nodes and database server nodes, as described in the *HealtheVet Web Services Client (HWSC) 1.0 Patch XOBW\*1.0\*4 Installation, Back-Out, and Rollback Guide*.
- The SSL/TLS configuration uses SSL version 3. The first application making use of SSL/TLS in HWSC is Master Patient Index (MPI), and the application needed to use SSL v 3 in order to connect to their PSIM remote server. In the future, all VA systems will be mandated to upgrade to higher versions of TLS and disable the use of older versions of SSL. When that happens, either a new XOBW patch will be issued to instruct system administrators to upgrade the SSL/TLS configuration to a higher version of TLS, or control of these configurations will be given to the System Administrators’ group, Health Systems Platform, so that they can do the SSL/TLS configuration upgrades directly.

> We expect that any future changes to the SSL/TLS configuration will be coordinated with all the VistA application teams using SSL/TLS configurations, including HWSC-based applications and any other VistA applications that will have to use SSL/TLS encryption like HL7 applications. The coordination is important, so that the proper testing can be performed before the changes are made to the production systems.

- This is the first use of SSL/TLS security, and the first application that used it, MPI, used the SOAP messaging features of HWSC. The SSL/TLS security should work the same with applications using REST-based features as both styles use the same underlying security functionality of SSL/TLS. We expect that future applications using REST and SSL/TLS security will do the appropriate testing before they release their application.
- Also, another security feature that was not used in this release with MPI is the use of Certificate Authentication. We expect that future applications using Certificate Authentication will do the appropriate testing before they release their application.

## Patch Numbering Scheme

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is an inconsistency in the numbering scheme used to describe this patch and should be noted. This patch contains changes to both M routines and Caché ObjectScript classes.

- The M routines correctly use the traditional patch numbering system on the second line as:

;;1.0;HwscWebServiceClient;\*\*4\*\*;September 13, 2010;Build 9

Where the current version number is 1.0, the patch number is 4, and the build number is 9.

- The two Caché ObjectScript classes incorrectly use the following scheme in the class comment as:

// HealtheVet Web Service Client v1 \[Build: 1.0.1.009\]

Where “Build: 1.0.1.009” is interpreted as version 1.0, patch 1, and build 9. The number should correctly have been “Build: 1.0.4.009”.

The most important number to consider is the current version, 1.0, which is correctly displayed in both the routines and the classes.

This patch numbering discrepancy will not break any functionality or affect any applications using this software.

# Product Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following documents describe the new functionality introduced with this release:

- *HealtheVet Web Services Client (HWSC) 1.0 Patch XOBW\*1.0\*4 Installation, Back-Out, and Rollback Guide*
- *HealtheVet Web Services Client (HWSC): Patch XOBW\*1.0\*4 Security Configuration Guide*

HealtheVet Web Services Client (HWSC) user documentation can also be found on the VA Software Document Library (VDL) at: http://www.va.gov/vdl/application.asp?appid=180