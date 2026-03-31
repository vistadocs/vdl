---
title: Electronic Signature (ESig) Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
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
audience: 
keywords: 
  - class
  - esig
  - table
  - vista
  - contents
  - strong
  - xobe
  - signature
  - even
  - distribution
page_count: 0
word_count: 4727
section_count: 11
table_count: 18
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: November 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Electronic_Signature/xobe_1_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/VistA_GUI_Hybrids/Electronic_Signature/xobe_1_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=171"
---

![](electronic-signature-esig-version-1-installation-guide/001.png)

Electronic Signature (ESig)

Installation Guide

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

[Figure 1-1. ESig Architecture [2](#_Toc150746594)](#_Toc150746594)

List of Tables

# Introduction 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [ESig Overview](#esig-overview)
    - [VistALink 1.5 Dependency](#vistalink-15-dependency)
    - [Installation](#installation)
  - [Using this Guide](#using-this-guide)
    - [Purpose/Audience](#purposeaudience)
    - [Text Conventions](#text-conventions)
  - [Additional Resources](#additional-resources)
    - [ESig Reference Materials](#esig-reference-materials)
    - [Online Technical Information](#online-technical-information)
- [Preliminary Considerations](#preliminary-considerations)
  - [ESig 1.0 Distribution Files](#esig-10-distribution-files)
  - [VistA/M Server Requirements](#vistam-server-requirements)
    - [Server Operating System and M Environment](#server-operating-system-and-m-environment)
    - [Fully Patched Accounts](#fully-patched-accounts)
    - [Network Communications Software](#network-communications-software)
  - [User Requirements](#user-requirements)
- [Installing ESig on the VistA/M Server](#installing-esig-on-the-vistam-server)
  - [FTPing the XOBE10.KIDS File to the M Server](#ftping-the-xobe10kids-file-to-the-m-server)
  - [Installing the ESig KIDS Build](#installing-the-esig-kids-build)
  - [Verifying the Checksum Value](#verifying-the-checksum-value)
  - [Assigning the User Context Menu](#assigning-the-user-context-menu)
- [Appendix A: Sample KIDS Installation](#appendix-a-sample-kids-installation)
- [Glossary](#glossary)

## ESig Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As Health*<u>e</u>*Vet-VistA developers migrate VistA applications to modern technologies, interim solutions may be required until enterprise solutions are mature and stable. The Electronic Signature (ESig) service provides an interim solution for the use of electronic codes in place of wet signatures while Health*<u>e</u>*Vet-VistA’s security infrastructure and architecture are being defined. The service duplicates for Java applications (J2EE or J2SE) the Kernel 8.0 electronic signature functionality currently used by VistA/M applications.

ESig furnishes a standard, consistent set of APIs that Health*<u>e</u>*Vet-VistA developers can implement to provide users access to electronic signature data stored on VistA/M systems. ESig APIs make calls from Java applications to VistA/M systems to retrieve, validate, and store electronic signature codes and signature block information (name, title, office phone, etc.). Additional Java APIs provide encoding/decoding, hash, and checksum calculation utilities, but do not interact with the VistA/M system.

Applications that implement the ESig service must provide a user interface (UI) to prompt users for their secret codes when authorizing orders, prescriptions, financial transactions, or other business processes. Users may also need the UI to create or modify their code or signature block data.

### VistALink 1.5 Dependency

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig requires the VistALink 1.5 service, which provides the transport layer enabling communication between a Java application and a VistA/M system.

The figure below shows ESig APIs communicating with VistA through VistALink 1.5. When a Health*<u>e</u>*Vet user signs on successfully, the connection from the application to VistA via VistALink is established. Consuming applications pass the VistaLinkConnection object to the ESig APIs that communicate with the VistA server.

![](electronic-signature-esig-version-1-installation-guide/002.png)

<span id="_Toc150746594" class="anchor"></span>Figure 1-1. ESig Architecture

### Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Health*<u>e</u>*Vet ESig consists of three parts:

- An M package containing a routine, a Broker option, and a set of Remote Procedures for accessing electronic signature codes and related data in the Kernel’s NEW PERSON file
- A JAR file containing a set of Java APIs for passing and receiving electronic signature related information from M and for performing hashing, encryption, and decryption of strings. For ESig functionality to work, the ESig JAR file must be present on an application’s classpath.
- Sample Java Swing, client console, and JSP utility applications to test or verify installation and configuration of the ESig components. These are included in the ESig distribution.

Although ESig is a Health*<u>e</u>*Vet-VistA application with Java and M components, the only installation required by each IRM is the KIDS build on the VistA/M server. Health*<u>e</u>*Vet-VistA applications requiring electronic signature functionality will include the ESig JAR file in their classpath. The JAR file contains APIs to perform ESig functions, including calling the VistA/M database.

Application developers and testers may want to deploy the sample ESig applications to client workstations (J2SE) or application servers (J2EE) to test the installation of the M server pieces. Instructions for deploying the sample applications are included in the *ESig 1.0 Developer Guide*.

## Using this Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purpose/Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document provides instructions for installing the Electronic Signature 1.0 software on VistA/M servers. It is intended mainly for VistA/M system administrators. It will also be useful to Health*<u>e</u>*Vet-VistA application developers and anyone testing ESig functionality in Health*<u>e</u>*Vet applications.

This guide focuses on the VistA/M environment and assumes that readers are familiar with the following:

- VistA/M computing environment
- VA FileMan data structures and terminology
- M programming language
- Microsoft Windows

The instructions for using ESig’s sample (test) J2SE and J2EE applications are included in the *ESig 1.0 Developer Guide*.

### Text Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below summarizes specialized use of typographical styles in this document.

<span id="_Toc125360492" class="anchor"></span>Table 1-2. Text Conventions

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
| ![](electronic-signature-esig-version-1-installation-guide/003.png) | Used to inform the reader of general information and reference material.  |
| ![](electronic-signature-esig-version-1-installation-guide/004.png) | Used to caution the reader to take special notice of critical information |

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

Technical information about files and the fields in files is stored in data dictionaries. To print formatted data dictionaries, reference the VA FileMan v.22.0 Advanced User Manual at <http://www.va.gov/vdl>.

#### Javadocs

Java class and package documentation is included in the ESig distribution file. Locate the javadoc folder and open your browser to the index.html file.

|                                                   |                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/005.png) | To learn more about Javadoc files, refer to Sun’s Javadoc Tool Home Page at: <http://java.sun.com/j2se/javadoc/>. |

|                                                   |                                                                                                                                                                                                                                                                                                                  |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/006.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs of the information, products, or services on the Website. The VHA does not exercise any editorial control over the information you may find at these locations. |

# Preliminary Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig is installed as a KIDS build on the VistA/M server. Sites may wish to obtain only the KIDS file and the ESIG documentation. Office of Information developers and support teams should note a separate distribution zip file. The ESig distribution zip file includes optional sample applications to test the KIDS installation and configuration. These sample applications may also be useful examples for developers implementing the ESig service in their applications.

|                                                   |                                                                                                                                                    |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/007.png) | It is strongly recommended that you install the ESig KIDS build in a VistA/M server’s Test account prior to installing it in a Production account. |

## ESig 1.0 Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_Toc112746834" class="anchor"></span>Table 2-1. Electronic Signature Distribution Files

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 65%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XOBE_1_0IG.PDF</td>
<td>Binary</td>
<td>Installation Guide. Use in conjunction with the readme text file.</td>
</tr>
<tr class="even">
<td>XOBE_1_0DG.PDF</td>
<td>Binary</td>
<td>Developer Guide.</td>
</tr>
<tr class="odd">
<td>XOBE_1_0SM.PDF</td>
<td>Binary</td>
<td>System Management Guide.</td>
</tr>
<tr class="even">
<td>XOBE_1_0.KID</td>
<td>ASCII</td>
<td><p>KIDS Host File. Contains the Electronic Signature Vista/M server software:</p>
<p>Server Routines</p>
<p>Kernel Option and Remote Procedure Calls</p></td>
</tr>
<tr class="odd">
<td>XOBE_1_0.ZIP</td>
<td>Binary</td>
<td>Contains the client-side Java libraries, sample applications (J2SE and J2EE), the M server KIDS host file, and Javadoc reference information. The contents are: jars, javadoc, m, samples, readme</td>
</tr>
</tbody>
</table>

The ESig distribution zip file contains:

> (root)

├─ readme.txt (Provides any last minute changes, new instructions, and additional

│ information to supplement the guides. Read all sections of this file

│ prior to installation.)

> ├─ jars/ (ESig JAR files)

> ├─ javadoc/ (Javadocs for ESig APIs)

> ├─ m/

> │ └─ XOBE_1_0.KID (KIDS build for VistA/M server)

> └─ samples/

> ├─ J2EE/ (sample J2EE application)

> └─ J2SE/ (sample client/server sample applications)

## VistA/M Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the minimum VistA/M server software required to install and use ESig.

### Server Operating System and M Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ESig requires either of the following operating systems:

- Caché /NT
- Caché /VMS

### Fully Patched Accounts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should have both a Test account and a Production account for the ESig software. The account(s) must contain the *fully* patched versions of the software listed in following table.

> <span id="_Toc150746602" class="anchor"></span>Table 2-2. Required Fully Patched M Accounts

|                |             |                       |
|----------------|-------------|-----------------------|
| Software   | Version | Patch Information |
| Kernel         | 8.0         | Fully patched.        |
| Kernel Toolkit | 7.3         | Fully patched         |
| RPC Broker     | 1.1         | Fully patched.        |
| VA FileMan     | 22.0        | Fully patched.        |
| VistALink      | 1.5         | Fully patched.        |

These packages must be properly installed and fully patched prior to installing the Electronic Signature VistA/M server software distribution. Patches must be installed in published sequence.

|                                                   |                                                                                                                                                                      |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/008.png) | VistALink 1.5 is a collection of three separate packages under the XOB\* namespace: Foundations 1.5 (XOBU); VistALink 1.5 (XOBV); and VistALink Security 1.5 (XOBS). |

### Network Communications Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

One or more properly configured VistALink 1.5 listeners must be running as a TCP/IP VMS service on your VistA/M server(s)

## User Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM support staff responsible for installing ESig on VistA/M servers (and optionally, client workstations) should be familiar with the following areas:

- VistA computing environment
- Installing software and managing a VistA/M system
- Setting up a VistALink 1.5 listener and ensuring the service is enabled
- Kernel Installation and Distribution System (KIDS)
- VA FileMan data structures and terminology
- Microsoft Windows
- Red Hat Linux
- M programming language

# Installing ESig on the VistA/M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 95%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](electronic-signature-esig-version-1-installation-guide/009.png)</td>
<td><p>Be sure to check the readme.txt file included in the Electronic Signature distribution zip file for the most recent installation instructions.</p>
<p>Electronic Signature requires a VistALink 1.5 listener.</p></td>
</tr>
</tbody>
</table>

The instructions in this section are applicable for the Test/Production accounts in Caché/NT and Caché/VMS environments.

Check the FORUM Patch Module and make any new patches that have been released by the applications listed in section 2.2.2 readily available, so that you can apply them before you begin the Electronic Signature installation process.

|                                                   |                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/010.png) | There are three VistALink 1.5 packages loaded in the FORUM Patch Module: Foundations, VistALink, and VistALink Security. |

## FTPing the XOBE_1_0.KIDS File to the M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IRM staff tasked with installation and support of the Esig package are only responsible for the VistA/M installation activities described here. You’ll need the XOBE_1_0.KID file, the VistA/M server software in Kernel 8.0 KIDS format. It is available from the OI ANONYMOUS.SOFTWARE directories. FTP the KIDS file to your VistA/M system in ASCII format only. The file is also exported in the m folder of the Electronic Signature distribution zip file.

## Installing the ESig KIDS Build

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use KIDS to install the Electronic Signature routine, option, and remote procedures.

From the KIDS menu you will use the following sequence of options:

1.  Load a Distribution: Use the host file name, XOBE_1_0.KID
1.  Verify Checksums in Transport Global: Use the install name, XOBE 1.0
2.  Backup a Transport Global: Use the install name, XOBE 1.0
3.  Install Package(s): Use the install name, XOBE 1.0

During the installation of the package in step 4 above, you will be asked three questions. Answer NO to all of them:

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

> Want KIDS to INHIBIT LOGONs during the install? YES // NO

> Want to DISABLE Scheduled Options, Menu Options,

> and Protocols? YES// NO

Installation will take less than one minute. No options need to be placed out of order, and users can remain on the system. Production system installations will generate a MailMan message to update the FORUM National Patch/Package Tracking module for your site.

|                                                   |                                                                       |
|---------------------------------------------------|-----------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/011.png) | See Appendix A of this guide for an example of the KIDS installation. |

## Verifying the Checksum Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Kernel Toolkit 8.0 checksum utility to verify the checksums of the XOBE\* routine(s) installed. From the programmer prompt:

> \>D CHECK1^XTSUMBLD

> New CheckSum CHECK1^XTSUMBLD:

> This option determines the current checksum of selected routine(s).

> The Checksum of the routine is determined as follows:

> 1\. Any comment line with a single semi-colon is presumed to be

> followed by comments and only the line tag will be included.

> 2\. Line 2 will be excluded from the count.

> 3\. The total value of the routine is determined (excluding

> exceptions noted above) by multiplying the ASCII value of each

> character by its position on the line and position of the line in

> the routine being checked.

> Select one of the following:

> P Package

> B Build

> Build from: Build

> This will check the routines from a BUILD file.

> Select BUILD NAME: XOBE 1.0 ELECTRONIC SIGNATURE

> XOBESIG value = 35924230

> done

|                                                   |                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------|
| ![](electronic-signature-esig-version-1-installation-guide/012.png) | The checksum value obtained should be “35924230,” as shown above. |

## Assigning the User Context Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Context for Electronic Signature Users\[XOBE ESIG USER\] option is a Broker (Client/Server) option that contains the remote procedures used by ESig. To use the remote procedures, at least one of the following must be true:

- The user must have the \[XOBE ESIG USER\] Broker option added to his or her secondary menu.
- The \[XOBE ESIG USER\] Broker option must be added to the Common Menu \[XUCOMMAND\] in Kernel. In this case, all users on the system would have access to the ESig options; the Broker option need not be assigned specifically to individual users.
- The user must be defined as a programmer on the VistA/M system.

The recommended procedure for giving users access to the ESig remote procedures is to add the \[XOBE ESIG USER\] Broker option to the Common Menu \[XUCOMMAND\] in Kernel.

This concludes the Esig installation activities.

# Appendix A: Sample KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is an example of an M-side Electronic Signature software installation in a VistA/M test or mirror account.

Select Kernel Installation & Distribution System Option: INstallation

<span class="mark">1 Load a Distribution</span>

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 1 Load a Distribution

Enter a Host File: XOBE_1_0.KID

KIDS Distribution saved on Sep 27, 2005@08:03:32

Comment: Electronic Signature v1.0 \[Build 1.0.0.024\]

This Distribution contains Transport Globals for the following Package(s):

XOBE 1.0

Distribution OK!

Want to Continue with Load? YES// \<Enter\>

Loading Distribution...

XOBE 1.0

Use INSTALL NAME: XOBE 1.0 to install this Distribution.

1 Load a Distribution

<span class="mark">2 Verify Checksums in Transport Global</span>

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 2 Verify Checksums in Transport Global

Select INSTALL NAME: XOBE 1.0 Loaded from Distribution 11/22/05@15:13:20

=\> Electronic Signature v1.0 \[Build 1.0.0.024\] ;Created on Sep 27, 2005@

This Distribution was loaded on Nov 22, 2005@15:13:20 with header of

Electronic Signature v1.0 \[Build 1.0.0.024\] ;Created on Sep 27, 2005@08:03:32

It consisted of the following Install(s):

XOBE 1.0

DEVICE: HOME// \<Enter\>

PACKAGE: XOBE 1.0 Nov 22, 2005 3:13 pm PAGE 1

-------------------------------------------------------------------------------

1 Routine checked, 0 failed.

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

<span class="mark">5 Backup a Transport Global</span>

6 Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 5 Backup a Transport Global

Select INSTALL NAME: XOBE 1.0 Loaded from Distribution 11/22/05@15:13:20

=\> Electronic Signature v1.0 \[Build 1.0.0.024\] ;Created on Sep 27, 2005@

This Distribution was loaded on Nov 22, 2005@15:13:20 with header of

Electronic Signature v1.0 \[Build 1.0.0.024\] ;Created on Sep 27, 2005@08:03:3

2

It consisted of the following Install(s):

XOBE 1.0

Subject: Backup of XOBE 1.0 install on Nov 22, 2005

Replace \<Enter\>

Loading Routines for XOBE 1.0.

Send mail to: INSTALLER,TEST

Select basket to send to: IN// \<Enter\>

And Send to: \<Enter\>

1 Load a Distribution

2 Verify Checksums in Transport Global

3 Print Transport Global

4 Compare Transport Global to Current System

5 Backup a Transport Global

<span class="mark">6 Install Package(s)</span>

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: XOBE 1.0 Loaded from Distribution 11/22/05@15:13:20

=\> Electronic Signature v1.0 \[Build 1.0.0.024\] ;Created on Sep 27, 2005@

This Distribution was loaded on Nov 22, 2005@15:13:20 with header of

Electronic Signature v1.0 \[Build 1.0.0.024\] ;Created on Sep 27, 2005@08:03:3

2

It consisted of the following Install(s):

XOBE 1.0

Checking Install for Package XOBE 1.0

Install Questions for XOBE 1.0

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

XOBE 1.0

────────────────────────────────────────────────────────────────────────────────

Install Started for XOBE 1.0 :

Nov 22, 2005@15:13:44

Build Distribution Date: Sep 27, 2005

Installing Routines:

Nov 22, 2005@15:13:44

Installing PACKAGE COMPONENTS:

Installing REMOTE PROCEDURE

Installing OPTION

Nov 22, 2005@15:13:44

Updating Routine file...

Updating KIDS files...

XOBE 1.0 Installed.

Nov 22, 2005@15:13:44

Not a production UCI

NO Install Message sent

────────────────────────────────────────────────────────────────────────────────

┌────────────────────────────────────────────────────────────┐

100% │ 25 50 75 │

Complete └────────────────────────────────────────────────────────────┘

XOBE 1.0 Installed.

Nov 22, 2005@15:13:44

Not a production UCI

NO Install Message sent

Install Completed

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
<td>VAX (Virtual Address eXtension) is an established line of mid-range server computers from the Digital Equipment Corporation (DEC).</td>
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
#
