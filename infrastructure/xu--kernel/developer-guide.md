---
title: "Kernel 8.0 Developers Guide: Main Directory"
doc_type: DG
doc_label: Developer Guide
doc_layer: anchor
doc_subject: "Developers Guide: Main Directory"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - strong
  - kernel
  - class
  - guide
  - developer
  - vista
  - tools
  - software
  - table
  - even
page_count: 0
word_count: 7576
section_count: 5
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide

  Main Directory
---

![](kernel-8-0-developers-guide-main-directory/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developers-guide-main-directory/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><blockquote>
<p><span id="_Ref455486405" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p>
</blockquote></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel 8.0 Developer’s Guide: Main Directory</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward. This document serves as the main directory for all other, separate Kernel Developer’s User Guides.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref455486405" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Kernel Developer’s User Guides—Main Directory](#kernel-developers-user-guidesmain-directory)
  - [Kernel Developer’s User Guides—Overview](#kernel-developers-user-guidesoverview)
  - [API and Extrinsic Function Information](#api-and-extrinsic-function-information)
  - [Kernel Developer’s User Guides—Orientation](#kernel-developers-user-guidesorientation)
    - [Intended Audience](#intended-audience)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [Internal Word Navigation Links Setup Steps](#internal-word-navigation-links-setup-steps)
    - [How to Obtain Technical Information Online](#how-to-obtain-technical-information-online)
    - [Assumptions](#assumptions)
    - [Reference Materials](#reference-materials)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide* provides descriptive information about Kernel 8.0 and Kernel Toolkit 7.3 software for use by application developers. Kernel provides developers with several tools. These tools include Application Programming Interfaces (APIs), Extrinsic Functions, and Direct Mode Utilities. These tools let you create applications that are fully integrated with Kernel and that take advantage of Kernel’s features and functionality.

## Kernel Developer’s User Guides—Main Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*, in addition to this Main Directory, is divided into thirty-two (32) User Guides, based on the following functional divisions within Kernel/Kernel Toolkit:

- [Address Hygiene: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf)
- [Alerts: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_alerts_ug.pdf)
- [Common Services: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_common_services_ug.pdf)
- [Data Security: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_data_security_ug.pdf)
- [Device Handler: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf)
- [Domain Name Service (DNS): Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_dns_ug.pdf)
- [Electronic Signatures: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_esig_ug.pdf)
- [Error Processing: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_error_processing_ug.pdf)
- [Field Monitoring: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_field_monitoring_ug.pdf)
- [File Access Security: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_file_access_security_ug.pdf)
- [Help Processor: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_help_processor_ug.pdf)
- [Host Files: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_host_files_ug.pdf)
- [Institution File: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_institution_file_ug.pdf)
- [Kernel Installation and Distribution System (KIDS): Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_kids_ug.pdf)
- [Menu Manager: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_menu_manager_ug.pdf)
- [Lock Manager: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_lock_manager_ug.pdf)
- [Miscellaneous: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_miscellaneous_ug.pdf)
- [Name Standardization: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_name_standardization_ug.pdf)
- [National Provider Identifier (NPI): Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_npi_ug.pdf)
- [Operating System (OS) Interface: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_os_interface_ug.pdf)
- [Security Keys: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_security_keys_ug.pdf)
- [Server Options: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_server_options_ug.pdf)
- [Signon/Security: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_signon_security_ug.pdf)
- [Spooling: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_spooling_ug.pdf)
- [TaskMan: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf)
- [Toolkit: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_toolkit_ug.pdf)
- [Unwinder: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_unwinder_ug.pdf)
- [User: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_user_ug.pdf)
- [XGF Function Library: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xgf_fl_ug.pdf)
- [XLF Function Library: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xlf_fl_ug.pdf)
- [XML Parser (VistA): Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xml_parser_ug.pdf)
- [^XTMP Global: Developer Tools User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xtmp_global_ug.pdf)

![](kernel-8-0-developers-guide-main-directory/003.png) REF: For general user information and system manager information, see the *Kernel 8.0 Systems Management: \<Function\> User Guides*.  
  
Instructions for installing Kernel are provided in the *Kernel Installation Guide*. This guide also includes information about software application management (such as *recommended* settings for site parameters and scheduling time frames for tasked options).  
  
Information on recommended system configuration and setting Kernel’s site parameters, as well as lists of files, routines, options, and other components are documented in the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.  
  
Information about managing computer security, which includes a detailed description of techniques that can be used to monitor and audit computing activity, is presented in the *Kernel Security Tools Manual*.

## Kernel Developer’s User Guides—Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Kernel Developer’s User Guides assume that the reader is familiar with the computing environment of the VA’s Veterans Health Information Systems and Technology Architecture (VistA) and understands VA FileMan data structures and terminology. Understanding of the M programming language is required for this manual. No attempt is made to explain how the overall VistA programming system is integrated and maintained; such methods and procedures are documented elsewhere.

This manual provides an explanation of Kernel utilities, describing how they can be used to establish a standard user interface, monitor and manage the computer system, customize the environment according to local site needs, and define new areas of computing activities for users.

Kernel is an applications development environment, as well as a run-time environment providing standard services to applications software. It is *not* an operating system, but a set of utilities and associated files that are executed in an M environment. Kernel is central to VA VistA software strategy; in that it permits any VistA software application to run without modification on any hardware/software platform that supports American National Standards Institute (ANSI) Standard M. All operating system-specific or hardware-specific code is isolated to Kernel. Therefore, porting VistA to a new environment requires modification only to a handful of Kernel routines.

Kernel provides a computing environment that permits controlled user access, presents menus for choosing from various computing activities, allows device selection for output, enables the tasking of background processes, and offers numerous tools for system management and application programming. Kernel also provides tools for software distribution and installation.

VistA users see the same user interface, regardless of the underlying system architecture, because VistA applications are built using Kernel facilities for signon, database access, option selection, and device selection. As a result, user interaction with the system is constant across VistA applications.

## API and Extrinsic Function Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each API and Extrinsic Function displays the following information in the order listed:

1.  API or Extrinsic Function Name (required):

This is the name of the API or Extrinsic Function and is followed by a colon and a brief descriptive phrase of its use. It is written in one of the following formats:

- ^ROUTINE or TAG^ROUTINE—This format is used when the API is an entry point that does *not* take any input parameters in a parameter list (that is no parenthesis following the routine name).
- TAG^ROUTINE()—This format is used when the API is a procedure. Parentheses following the routine name indicate that the API may take input parameters.
- \$\$TAG^ROUTINE()—This format is used when the API is an extrinsic function. Parentheses following the routine name indicate that the API may take input parameters.

For example:

MAIL^XLFNSLK(): Get IP Addresses for a Domain Name

In this case "MAIL" is the tag name, "XLFNSLK" is the routine name, and the parenthesis indicate that it may take input parameters. The lack of "\$\$" preceding the tag name indicates that this is an API (procedure) and not an Extrinsic Function. The brief text that follows the colon gives you a general idea of what the API does.

Another example:

\$\$ADDRESS^XLFNSLK(): Conversion (Domain Name to IP Addresses)

In this case "ADDRESS" is the tag name, "XLFNSLK" is the routine name, and the parenthesis indicate that this it may take input parameters. The "\$\$" preceding the tag name indicates that this is an Extrinsic Function. The brief text that follows the colon gives you a general idea of what this Extrinsic Function does.

2.  Reference Type (required):

The Reference Type indicates the Integration Control Registration (ICR) for the API:

- Supported Reference—An API of this type is open for use by any VistA application. It has been recorded as a Supported Reference in the IA database on FORUM. VistA software applications do *not* need to request an IA to use it.
- Controlled Subscription Reference—An API of this type is controlled in its use. Permission to use the API is granted by the custodial package (software application, such as Kernel) on a case-by-case basis.

![](kernel-8-0-developers-guide-main-directory/004.png) NOTE: Private APIs are *not* documented in this manual.

3.  Category (required):

The Category indicates the general category to which the API or Extrinsic Function belongs.

4.  Integration Control Registration (required):

The Integration Control Registration indicates the Supported or Controlled Subscription Reference Integration Control Registration (ICR) number for the API or Extrinsic Function.

5.  Description (required):

This section provides an overall description of the API or Extrinsic Function. Please include the patch reference ID (such as XU\*8.0\*999) if this API or Extrinsic Function is being released by a patch.

6.  Format (required):

This section displays the format (usage) of the API or Extrinsic Function. Optional parameters appear inside rectangular brackets \[ \]. For example:

tag^routine(x\[,y\])

Where the x input parameter is required, and the y input parameter is optional. Rectangular brackets around a leading period \[.\] in front of a parameter indicate that you can optionally pass that parameter by reference.

7.  Input Parameters / Input Variables (optional):

This section lists all input parameters/variables for the API:

- Input Parameters—Input passed in a parameter list to procedure and function APIs. For documentation purposes only, parameters are shown in lowercase.
- Input Variables—Input variables passed through the symbol table to APIs without a parameter list. For documentation purposes only, variables are shown in UPPERCASE.

All input parameters *must* indicate whether they are "Required" or "Optional."

8.  Output / Output Parameters / Output Variables (optional):

This section lists all output or output variables returned by the API:

- Output—Output returned through a "pass by reference" variable from a API procedure or the return value of an extrinsic function.
- Output Parameters—Output parameters returned by the API or Extrinsic Function.
- Output Variables—Output variables returned through the symbol table from an API or Extrinsic Function.
9.  Details (optional):

This section provides additional information regarding the use of the API or Extrinsic Function. This should include anything *not* already included in the "Description" section.

10. Examples (required):

This section provides one or more examples demonstrating the use/functionality of the API or Extrinsic Function (*not* all APIs or Extrinsic Function have examples).

## Kernel Developer’s User Guides—Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual describes the overall structure of all Kernel 8.0 Developer’s User Guides listed in Section <u>1.1</u>, “<u>Kernel Developer’s User Guides—Main Directory</u>.”

### Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience of the Kernel Developer’s User Guides are the following stakeholders:

- Product Delivery Service (PDS)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS)—Personnel who support Kernel-related products.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](kernel-8-0-developers-guide-main-directory/005.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per [VA Directive 6402](http://www.va.gov/vapubs/viewPublication.asp?Pub_ID=718&FType=2) (pending signature), these routines should *not* be modified.

![](kernel-8-0-developers-guide-main-directory/006.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

#### Documentation Disclaimer

This manual provides an overall explanation of using Kernel; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) Product Delivery Service (PDS) Intranet Website.

![](kernel-8-0-developers-guide-main-directory/007.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These user guides use several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. [Table 1](#_Ref455486405) gives a description of each of these symbols:

| Symbol                                                                                              | Description                                                                                                                       |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-developers-guide-main-directory/008.png)   | NOTE / REF: Used to inform the reader of general information including references to additional reading material.             |
| ![](kernel-8-0-developers-guide-main-directory/009.png) | ATTENTION / CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<Application Name/Abbreviation/Namespace\>*PATIENT,*\<N\>*
- *\<Application Name/Abbreviation/Namespace\>*USER,*\<N\>*

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in Kernel (XU or KRN) test patient and user names would be documented as follows:

XUPATIENT,ONE; XUPATIENT,TWO; XUPATIENT,THREE; … XUPATIENT,14; and so on.

XUUSER,ONE; XUUSER,TWO; XUUSER,THREE; … XUUSER,14; and so on.

- “Snapshots” of computer commands and online displays (that is screen captures/dialogs) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
  - User’s responses to online prompts are boldface and (optionally) highlighted in yellow (such as <span class="mark">\<Enter\></span>).
  - Emphasis within a dialog box is (optionally) boldface and highlighted in blue (such as <span class="mark">STANDARD LISTENER: RUNNING</span>).
  - Some software code reserved/key words are boldface with alternate color font.
  - References to “\<Enter\>” within these snapshots indicate that the user should press the Enter (or Return) key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
  - Author’s comments are displayed in italics or as “callout” boxes.

![](kernel-8-0-developers-guide-main-directory/010.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- These user guides refer to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M “\>” prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- MUMPS (M) API and Extrinsic Functions are two distinct concepts within the MUMPS programming language.
  - APIs—Provide a set of functions and procedures that can be called from within MUMPS programs, allowing for the manipulation of data and control of the execution environment.
  - Extrinsic Functions—Are specific to MUMPS and can be invoked to return a value from another M routine. They are used to perform tasks that are not part of the standard MUMPS functionality but are specific to the MUMPS environment.

The key difference lies in the scope and purpose of each, with the APIs serving as a broader framework for interaction with the M environment, while Extrinsic Functions are more focused on returning values from specific routines.

- The following conventions are used with regards to APIs and Extrinsic Functions:
- The following API/Extrinsic Functions types are documented:
- Supported:

This applies where any VistA application may use the attributes/functions defined by the Integration Control Registration (ICR); these are also called “Public”. An example is an ICR that describes a standard API. The package that creates/maintains the Supported Reference *must* ensure it is recorded as a Supported Reference in the ICR database. There is no need for other VistA packages to request an ICR to use these references; they are open to all by default.

- Controlled Subscription:

Describes attributes/functions that *must* be controlled in their use. The decision to restrict the Integration Control Registration (ICR) is based on the maturity of the custodian package. Typically, these ICRs are created by the requesting package based on their independent examination of the custodian package's features. For the ICR to be approved the custodian grants permission to other VistA packages to use the attributes/functions of the ICR; permission is granted on a one-by-one basis where each is based on a solicitation by the requesting package.

![](kernel-8-0-developers-guide-main-directory/011.png) Private APIs are *not* documented.

- Headings for developer API and Extrinsic Functions descriptions (such as supported for use in applications and on the Database Integration Committee \[DBIC\] list) include the routine tag (if any), the caret (^) used when calling the routine, and the routine name. The following is an example:

EN1^XQH

- For APIs and Extrinsic Functions that take input parameter, the input parameter is labeled “Required” when it is a required input parameter and labeled “Optional” when it is an optional input parameter.
- For APIs and Extrinsic Functions that take parameters, parameters are shown in lowercase, and variables are shown in uppercase. This is to convey that the parameter name is merely a placeholder. M allows you to pass a variable of any name as the parameter or even a string literal (if the parameter is *not* being passed by reference). The following is an example of the formatting for input parameters:

XGLMSG^XGLMSG(msg_type,\[.\]var\[,timeout\])

- Rectangular brackets \[\] around a parameter are used to indicate that passing the parameter is optional. Rectangular brackets around a leading period \[.\] in front of a parameter indicate that you can optionally pass that parameter by reference.
- All APIs and Extrinsic Functions are categorized by function. This categorization is subjective and subject to change based on feedback from the development community. In addition, some APIs could fall under multiple categories; however, they are only listed once under a chosen category.  
    
  APIs and Extrinsic Functions within a category are first sorted alphabetically by Routine name and then within routine name are sorted alphabetically by Tag reference. The \$\$, ^, or ^% prefixes on APIs and Extrinsic Functions is ignored when alphabetizing.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (such as XUPROGMODE security key).

![](kernel-8-0-developers-guide-main-directory/012.png) NOTE: Other software code (such as Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (that is CamelCase).

### Internal Word Navigation Links Setup Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses Microsoft® Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar for all Word documents, see the [*Tech Writer Tips: Internal Word Navigation Links Setup*](https://dvagov.sharepoint.com/:b:/r/sites/OITDSOSPMTW/Library/Internal_Word_Navigation_Links_Setup_Steps.pdf?csf=1&web=1&e=oc8dP8) (VA Intranet) document.

![](kernel-8-0-developers-guide-main-directory/013.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

### How to Obtain Technical Information Online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exported VistA M Server-based software file, routine, and global documentation can be generated with Kernel, MailMan, and VA FileMan utilities.

![](kernel-8-0-developers-guide-main-directory/014.png) NOTE: Methods of obtaining specific technical information online are indicated where applicable under the appropriate section.  
  
REF: See the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual* for further information.

#### Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

#### Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](kernel-8-0-developers-guide-main-directory/015.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These user guides are written with the assumption that the reader is familiar with the following:

- VistA computing environment:
  - Kernel—VistA M Server software
  - VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

### Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Readers who wish to learn more about Kernel should consult the following:

- *Kernel Release Notes*
- *Kernel Installation Guide*
- *Kernel 8.0 Systems Management: Main Directory User Guide*: Divided into seven User Guides, based on the following functional divisions within Kernel:”
  - *Kernel 8.0 Systems Management: Signon/Security User Guide*
  - *Kernel 8.0 Systems Management: Menu Manager User Guide*
  - *Kernel 8.0 Systems Management: Device Handler User Guide*
  - *Kernel 8.0 Systems Management: TaskMan User Guide*
  - *Kernel 8.0 Systems Management: KIDS User Guide*
  - *Kernel 8.0 Systems Management: Toolkit User Guide*
  - *Kernel 8.0 Systems Management: Utilities User Guide*
- *Kernel 8.0 Developer’s Guide: Main Directory User Guide* (this manual): Divided into 32 User Guides, based on the following API functional divisions within Kernel. For a list of User Guides, see Section <u>1.1</u>.
- *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*
- *Kernel Security Tools Manual*
- Kernel VA Intranet Website.

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

Redacted VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](kernel-8-0-developers-guide-main-directory/016.png) REF: Kernel manuals are located on the [Kernel application on the VDL](http://www.va.gov/vdl/application.asp?appid=10).

Unredacted VistA documentation and software can also be downloaded from the Network File Share (NFS) server.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developers-guide-main-directory/017.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Main_Glossary" class="anchor"></span>Glossary

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Alerts</strong></td>
<td><p>An alert notifies one or more users of a matter requiring immediate attention. Alerts function as brief notices that are distinct from mail messages or triggered bulletins.</p>
<p>Alerts are designed to provide interactive notification of pending computing activities (such as the need to reorder supplies or review a patient’s clinical test results). Along with the alert message is an indication that the <strong>View Alerts</strong> common option should be chosen to take further action.</p>
<p>An alert includes any specifications made by the developer when designing the alert. This minimally includes the alert message and the list of recipients (an information-only alert). It can also include an alert action, software application identifier, alert flag, and alert data. Alerts are stored in the ALERT (#8992) file.</p></td>
</tr>
<tr class="even">
<td><strong>Alert Action</strong></td>
<td>The computing activity that can be associated with an alert (that is an option [<strong>XQAOPT</strong> input variable] or routine [<strong>XQAROU</strong> input variable]).</td>
</tr>
<tr class="odd">
<td><strong>Alert Data</strong></td>
<td>An optional string that the developer can define when creating the alert. This string is restored in the <strong>XQADATA</strong> input variable when the alert action is taken.</td>
</tr>
<tr class="even">
<td><strong>Alert Flag</strong></td>
<td>An optional tool currently controlled by the Alert Handler to indicate how the alert should be processed (<strong>XQAFLG</strong> input variable).</td>
</tr>
<tr class="odd">
<td><strong>Alert Handler</strong></td>
<td>The name of the mechanism by which alerts are stored, presented to the user, processed, and deleted. The Alert Handler is a part of Kernel, in the <strong>XQAL</strong> namespace.</td>
</tr>
<tr class="even">
<td><strong>Alert Identifier</strong></td>
<td>A three-semicolon piece identifier, composed of the original Package Identifier (described below) as the first piece; the <strong>DUZ</strong> of the alert creator as the second piece; and the date and time (in VA FileMan format) when the alert was created as the third piece. The Alert Identifier is created by the Alert Handler and uniquely identifies an alert.</td>
</tr>
<tr class="odd">
<td><strong>Alert Message</strong></td>
<td>One line of text that is displayed to the user (the <strong>XQAMSG</strong> input variable).</td>
</tr>
<tr class="even">
<td><strong>Alpha Testing</strong></td>
<td>In VA terminology, Alpha testing is when a VistA test software application is running in a site’s account.</td>
</tr>
<tr class="odd">
<td><strong>Audit Access</strong></td>
<td>A user’s authorization to mark the information stored in a computer file to be audited.</td>
</tr>
<tr class="even">
<td><strong>Auditing</strong></td>
<td>Monitoring computer usage such as changes to the database and other user activity. Audit data can be logged in several VA FileMan and Kernel files.</td>
</tr>
<tr class="odd">
<td><strong>Auto Menu</strong></td>
<td>An indication to Menu Manager that the current user’s menu items should be displayed automatically. When AUTO MENU is <em>not</em> in effect, the user <em>must</em> enter a question mark at the menu’s select prompt to see the list of menu items.</td>
</tr>
<tr class="even">
<td><strong>Beta Testing</strong></td>
<td>In VA terminology, Beta testing is when a VistA test software application is running in a Production account.</td>
</tr>
<tr class="odd">
<td><strong>Capacity Management</strong></td>
<td>The process of assessing a system’s capacity and evaluating its efficiency relative to workload to optimize system performance. Kernel provides several utilities.</td>
</tr>
<tr class="even">
<td><strong>Caret</strong></td>
<td>A symbol expressed as <strong>^</strong> (caret);<br />
<strong>Shift-6</strong> on most keyboards. In many M systems, a caret is used as an exiting tool from an option. Also referred to as the “up-arrow” symbol.</td>
</tr>
<tr class="odd">
<td><strong>Checksum</strong></td>
<td>A numeric value that is the result of a mathematical computation involving the characters of a routine or file.</td>
</tr>
<tr class="even">
<td><strong>Cipher</strong></td>
<td><p>A system that arbitrarily represents each character as one or more other characters.</p>
<p>(See also: <a href="#Encryption_glossary">Encryption</a>.)</p></td>
</tr>
<tr class="odd">
<td><strong>Common Menu</strong></td>
<td><strong>SYSTEM COMMAND OPTIONS</strong> [XUCOMMAND] menu (aka <strong>Common</strong> menu). Options on this menu are available to all users. Entering two question marks (<strong>??</strong>) at the menu’s select prompt displays any SECONDARY MENU OPTIONS (#203) available to the signed-on user along with the <strong>Common</strong> menu options available to all users.</td>
</tr>
<tr class="even">
<td><strong>Compiled Menu System (^XUTL Global)</strong></td>
<td>Job-specific information that is kept on each CPU so that it is readily available during the user’s session. It is stored in the <strong>^XUTL</strong> global, which is maintained by the menu system to hold commonly referenced information. The user’s place within the menu trees is stored, for example, to enable navigation by menu jumping.</td>
</tr>
<tr class="odd">
<td><strong>Computed Field</strong></td>
<td>This field takes data from other fields and performs a predetermined mathematical function (such as adding two columns together). You do <em>not</em>, however, see the results of the mathematical function on the screen. Only when you are printing or displaying information on the screen do you see the results for this type of field.</td>
</tr>
<tr class="even">
<td><strong>Device Handler</strong></td>
<td>The Kernel module that provides a mechanism for accessing peripherals and using them in controlled ways (such as user access to printers or other output devices).</td>
</tr>
<tr class="odd">
<td><strong>DIFROM</strong></td>
<td>VA FileMan utility that gathers all software components and changes them into routines (<strong>namespaceI*</strong> routines) so that they can be exported and installed in another VA FileMan environment.</td>
</tr>
<tr class="even">
<td><strong>Double Quote (“)</strong></td>
<td>A symbol used in front of a <strong>Common</strong> option’s menu text or synonym to select it from the <strong>SYSTEM COMMAND OPTIONS</strong> [XUCOMMAND] menu (aka <strong>Common</strong> menu). For example, the five character string <strong>“TBOX</strong> selects the User’s Toolbox [XUSERTOOLS] <strong>Common</strong> option.</td>
</tr>
<tr class="odd">
<td><strong>DR String</strong></td>
<td>The set of characters used to define the <strong>DR</strong> variable when calling VA FileMan. Since a series of parameters may be included within quotes as a literal string, the variable’s definition is often called the <strong>DR</strong> string. To define the fields within an edit sequence, for example, the developer may specify the fields using a <strong>DR</strong> string rather than an INPUT template.</td>
</tr>
<tr class="even">
<td><strong>DUZ(0)</strong></td>
<td>A local variable that holds the FILE MANAGER ACCESS CODE (#3) field of the signed-on user.</td>
</tr>
<tr class="odd">
<td><span id="Encryption_glossary" class="anchor"></span><strong>Encryption</strong></td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases, encryption algorithms are one directional, that is, they only encode, and the resulting data <em>cannot</em> be unscrambled (such as Access and Verify Codes).</td>
</tr>
<tr class="even">
<td><strong><br />
</strong><span id="File_Access_Security_System_glossary" class="anchor"></span><strong>File Access Security System</strong></td>
<td>Formerly known as Part 3 of the Kernel Inits. If the File Access Security conversion has been run, file-level security for VA FileMan files is controlled by Kernel’s File Access Security system, <em>not</em> by VA FileMan Access Codes (that is FILE MANAGER ACCESS CODE [#3] field in the NEW PERSON [#200] file).</td>
</tr>
<tr class="odd">
<td><strong>Forced Queuing</strong></td>
<td>A device attribute indicating that the device can only accept queued tasks. If a job is sent for foreground processing, the device rejects it and prompt the user to queue the task instead.</td>
</tr>
<tr class="even">
<td><span id="Go_Home_Jump_glossary" class="anchor"></span><strong>Go-Home Jump</strong></td>
<td>A menu jump that returns the user to the primary menu presented at signon. It is specified by entering two carets (<strong>^^</strong>) at the menu’s select prompt. It resembles the “Rubber-band Jump” but <em>without</em> an option specification/name following the carets.</td>
</tr>
<tr class="odd">
<td><strong>Help Processor</strong></td>
<td>A Kernel module that provides a system for creating and displaying online documentation. It is integrated within the menu system so that help frames associated with options can be displayed with a standard query at the menu’s select prompt.</td>
</tr>
<tr class="even">
<td><strong>Host File Server (HFS)</strong></td>
<td>A procedure available on layered systems whereby a file on the host system can be identified to receive output. It is implemented by the Device Handler’s HFS device type.</td>
</tr>
<tr class="odd">
<td><strong>INIT</strong></td>
<td>Initialization of a software application. <strong>INIT*</strong> routines are built by VA FileMan’s DIFROM and, when run, recreate a set of files and other software components.</td>
</tr>
<tr class="even">
<td><strong>JSON</strong></td>
<td>JavaScript Object Notation.</td>
</tr>
<tr class="odd">
<td><strong>Jump</strong></td>
<td><p>In VistA applications, the Jump command allows you to go from a particular field within an option to another field within that same option. You can also Jump from one menu option to another menu option without having to respond to all the prompts in between. To jump, type a caret (<strong>^</strong>) and then type the name of the field or option to which you wish to jump.</p>
<p>(See also <a href="#Go_Home_Jump_glossary">Go-Home Jump</a>, <a href="#Phantom_Jump_glossary">Phantom Jump</a>, <a href="#Rubber_Band_Jump_glossary">Rubber-Band Jump</a>, or <a href="#Up_Arrow_Jump_glossary">Up-Arrow Jump</a>.)</p></td>
</tr>
<tr class="even">
<td><strong>Jump Start</strong></td>
<td>A logon procedure whereby the user enters the “<strong>Access Code;Verify code;option</strong>” to go immediately to the target option, indicated by its menu text or synonym. The jump syntax can be used to reach an option within the menu trees by entering “<strong>accesscode;verifycode;option</strong>”.</td>
</tr>
<tr class="odd">
<td><strong>Kermit</strong></td>
<td>A standard file transfer protocol. It is supported by Kernel and can be set up as an alternate editor.</td>
</tr>
<tr class="even">
<td><strong>Manager Account</strong></td>
<td>A UCI that holds vendor shared routines.</td>
</tr>
<tr class="odd">
<td><strong>Menu Cycle</strong></td>
<td>The process of first visiting a menu option by picking it from a menu’s list of choices and then returning to the menu’s select prompt. Menu Manager keeps track of information (such as the user’s place in the menu trees) according to the completion of a cycle through the menu system.</td>
</tr>
<tr class="even">
<td><strong>Menu Manager</strong></td>
<td>The Kernel module that controls the presentation of user activities (such as menu choices or options). Information about each user’s menu choices is stored in the Compiled Menu System, the <strong>^XUTL</strong> global, for easy and efficient access.</td>
</tr>
<tr class="odd">
<td><strong>Menu System</strong></td>
<td>The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="even">
<td><strong>Menu Template</strong></td>
<td>An association of options as pathway specifications to reach one or more destination options. The final options <em>must</em> be executable activities and <em>not</em> merely menus for the template to function. Any user can define user-specific MENU templates through the corresponding <strong>Common</strong> option.</td>
</tr>
<tr class="odd">
<td><strong>Menu Trees</strong></td>
<td>The menu system’s hierarchical tree-like structures that can be traversed or navigated, like pathways, to give users easy access to various options.</td>
</tr>
<tr class="even">
<td><strong>PAC</strong></td>
<td><strong>P</strong>rogrammer <strong>A</strong>ccess <strong>C</strong>ode. An optional user attribute that can function as a second level password into programmer mode.</td>
</tr>
<tr class="odd">
<td><strong>Part 3 of the Kernel Init</strong></td>
<td>See <a href="#File_Access_Security_System_glossary">File Access Security System</a>.</td>
</tr>
<tr class="even">
<td><strong>Pattern Match</strong></td>
<td>A preset formula used to test strings of data. Refer to your system’s M Language Manuals for information on Pattern Match operations.</td>
</tr>
<tr class="odd">
<td><span id="Phantom_Jump_glossary" class="anchor"></span><strong>Phantom Jump</strong></td>
<td>Menu jumping in the background. Used by the menu system to check menu pathway restrictions.</td>
</tr>
<tr class="even">
<td><strong>Primary Menus</strong></td>
<td>The list of options presented at signon. Each user <em>must</em> have a PRIMARY MENU OPTION (#201) to sign on and reach Menu Manager. Users are given primary menus by system administrators. This menu should include most of the computing activities the user needs Value is stored in the PRIMARY MENU OPTION (#201) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="odd">
<td><strong>Programmer Access</strong></td>
<td>Privilege to become a developer on the system and work outside many of the security controls of Kernel. Accessing <strong>Programmer</strong> mode from Kernel’s menus requires having the at-sign security code (<strong>@</strong>), which sets the variable <strong>DUZ(</strong>A<strong>0</strong>A<strong>)=@</strong>.</td>
</tr>
<tr class="even">
<td><strong>Protocol</strong></td>
<td>An entry in the PROTOCOL (#101) file. Used by the Order Entry/Results Reporting (OE/RR) software to support the ordering of medical tests and other activities. Kernel includes several protocol-type options for enhanced menu displays within the OE/RR software.</td>
</tr>
<tr class="odd">
<td><strong>Purge Indicator</strong></td>
<td>Checked by the Alert Handler (in the <strong>XQAKILL</strong> input variable) to determine whether an alert should be deleted, and whether deletion should be for the current user or for all users who might receive the alert.</td>
</tr>
<tr class="even">
<td><strong>Queuing</strong></td>
<td>Requesting that a job be processed in the background rather than in the foreground within the current session. Kernel’s TaskMan module handles the queuing of tasks.</td>
</tr>
<tr class="odd">
<td><strong>Queuing Required</strong></td>
<td>An option attribute that specifies that the option <em>must</em> be processed by TaskMan (the option can only be queued). The option can be invoked, and the job prepared for processing, but the output can only be generated during the specified time periods.</td>
</tr>
<tr class="even">
<td><strong>Resource</strong></td>
<td>A method that enables sequential processing of tasks. The processing is accomplished with a RES device type designed by the application developer and implemented by system administrators. The process is controlled by the RESOURCE (#3.54) file.</td>
</tr>
<tr class="odd">
<td><span id="Rubber_Band_Jump_glossary" class="anchor"></span><strong>Rubber-Band Jump</strong></td>
<td><p>A menu jump used to go out to an option and then return, in a bouncing motion. The syntax of the jump is two carets (<strong>^^</strong>, <strong>Shift-6</strong> on most keyboards) followed by an option’s menu text or synonym (such as <strong>^^Print Option File</strong>). If the two carets are <em>not</em> followed by an option specification, the user is returned to the primary menu.</p>
<p>(See also: <a href="#Go_Home_Jump_glossary">Go-Home Jump</a>.)</p></td>
</tr>
<tr class="even">
<td><strong>Scheduling Options</strong></td>
<td>A way of ordering TaskMan to run an option at a designated time with a specified rescheduling frequency (such as once per week).</td>
</tr>
<tr class="odd">
<td><strong>Scroll/No Scroll</strong></td>
<td>The <strong>Scroll/No Scroll</strong> button (also called Hold Screen) allows the user to “stop” (No Scroll) the terminal screen when large amounts of data are displayed too fast to read and “restart” (Scroll) when the user wishes to continue.</td>
</tr>
<tr class="even">
<td><strong>Secondary Menu Options</strong></td>
<td>Options assigned to individual users to tailor their menu choices. If a user needs a few options in addition to those available on the primary menu, the options can be assigned as secondary options. To facilitate menu jumping, secondary menus should be specific activities, <em>not</em> elaborate and deep menu trees. Values are stored in the SECONDARY MENU OPTION (#203) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="odd">
<td><strong>Secure Menu Delegation (SMD)</strong></td>
<td>A controlled system whereby menus and security keys can be allocated by people other than system administrators (such as application coordinators) who have been so authorized. SMD is a part of Menu Manager.</td>
</tr>
<tr class="even">
<td><strong>Server Option</strong></td>
<td>An entry in the OPTION (#19) file. An automated mail protocol that is activated by sending a message to the server with the “<strong>S.server</strong>” syntax. A server option’s activity is specified in the OPTION (#19) file and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td><strong>Signon/Security</strong></td>
<td>The Kernel module that regulates access to the menu system. It performs several checks to determine whether access can be permitted at a particular time. A log of signons is maintained.</td>
</tr>
<tr class="even">
<td><strong>Special Queueing</strong></td>
<td>An option attribute indicating that TaskMan should automatically run the option whenever the system reboots.</td>
</tr>
<tr class="odd">
<td><strong>Spooler</strong></td>
<td>An entry in the DEVICE (#3.5) file. It uses the associated operating system’s spool facility, whether it’s a global, device, or host file. Kernel manages spooling so that the underlying OS mechanism is transparent. In any environment, the same method can be used to send output to the spooler. Kernel subsequently transfers the text to a global for subsequent despooling (printing).</td>
</tr>
<tr class="even">
<td><strong>Synonym</strong></td>
<td>A field in the OPTION (#19) file. Options can be selected by their menu text or synonym.</td>
</tr>
<tr class="odd">
<td><strong>TaskMan</strong></td>
<td>The Kernel module that schedules and processes background tasks (also called Task Manager).</td>
</tr>
<tr class="even">
<td><strong>Timed Read</strong></td>
<td>The amount of time Kernel waits for a user response to an interactive <strong>READ</strong> command before starting to halt the process.</td>
</tr>
<tr class="odd">
<td><span id="Up_Arrow_Jump_glossary" class="anchor"></span><strong>Up-Arrow Jump</strong></td>
<td>In the menu system, entering a caret (<strong>^</strong>; sometimes referred to as an up-arrow) followed by an option specification/name accomplishes a jump to the target option without needing to take the usual steps through the menu pathway.</td>
</tr>
<tr class="even">
<td><strong>XINDEX</strong></td>
<td>A Kernel utility used to verify routines and other M code associated with a software application. Checking is done according to current ANSI MUMPS standards and VistA programming standards. This tool can be invoked through an option or from direct mode (&gt;<strong>D ^XINDEX</strong>).</td>
</tr>
<tr class="odd">
<td><strong>Z Editor (^%Z)</strong></td>
<td>A Kernel tool used to edit routines or globals. It can be invoked with an option, or from direct mode after loading a routine with &gt;<strong>X ^%Z</strong>.</td>
</tr>
<tr class="even">
<td><strong>ZOSF Global (^%ZOSF)</strong></td>
<td>The Operating System File—a manager account global distributed with Kernel to provide an interface between VistA software and the underlying operating system. This global is built during Kernel installation when running the manager setup routine (<strong>ZTMGRSET</strong>). The nodes of the global are filled-in with operating system-specific code to enable interaction with the operating system. Nodes in the <strong>^%ZOSF</strong> global can be referenced by VistA application developers so that separate versions of the software need <em>not</em> be written for each operating system.</td>
</tr>
</tbody>
</table>

![](kernel-8-0-developers-guide-main-directory/018.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.