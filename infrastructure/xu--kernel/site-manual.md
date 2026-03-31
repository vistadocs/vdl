---
title: "Kernel 8.0 Systems Management: Main Directory"
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: anchor
doc_subject: "Systems Management: Main Directory"
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
  - management
  - systems
  - table
  - vista
  - software
  - contents
  - options
page_count: 0
word_count: 6336
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management

  Main Directory
---

![](kernel-8-0-systems-management-main-directory/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-main-directory/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td>08/31/2025</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>07/22/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Section <u>1.1</u>: Update links to external Word document to open in a new Window.</p></li>
<li><p>Section <u>1.3.5</u>: Updated internal document navigation instructions.</p></li>
</ul></td>
<td>VASS Development Team</td>
</tr>
<tr class="odd">
<td>05/07/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: Main Directory</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward. This document serves as the main directory for all other, separate Kernel Systems Management User Guides.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
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
  - [Kernel Systems Management User Guides—Main Directory](#kernel-systems-management-user-guidesmain-directory)
  - [Kernel Systems Management User Guides—Overview](#kernel-systems-management-user-guidesoverview)
    - [Users](#users)
    - [System Managers](#system-managers)
  - [Kernel Systems Management User Guides—Orientation](#kernel-systems-management-user-guidesorientation)
    - [How to Use these Manuals](#how-to-use-these-manuals)
    - [Intended Audience](#intended-audience)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [Internal Word Navigation Links Setup Steps](#internal-word-navigation-links-setup-steps)
    - [How to Obtain Technical Information Online](#how-to-obtain-technical-information-online)
    - [Assumptions](#assumptions)
    - [Reference Materials](#reference-materials)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide* provides descriptive information about Kernel 8.0 and Kernel Toolkit 7.3 software for use by system administrators, application developers, Automated Data Processing Application Coordinators (ADPACs), and other end-users.

## Kernel Systems Management User Guides—Main Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*, in addition to this Main Directory, is divided into seven User Guides, based on the following functional divisions within Kernel/Kernel Toolkit:

- [Kernel Signon/Security User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf)
- [Kernel Menu Manager User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_menu_manager_ug.pdf)
- [Kernel Device Handler User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_device_handler_ug.pdf)
- [Kernel TaskMan User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf)
- [Kernel Installation and Distribution System (KIDS) User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_kids_ug.pdf)
- [Kernel Toolkit User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_toolkit_ug.pdf)
- [Kernel Utilities User Guide](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_utilities_ug.pdf)

## Kernel Systems Management User Guides—Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These Kernel Systems Management User Guides assume that the reader is familiar with the computing environment of the VA’s Veterans Health Information Systems and Technology Architecture (VistA) and understands VA FileMan data structures and terminology. Some understanding of the M programming language is helpful for some parts of the manual. No attempt is made to explain how the overall VistA programming system is integrated and maintained; such methods and procedures are documented elsewhere. This manual does, however, provide an explanation of Kernel utilities, describing how they can be used to establish a standard user interface, monitor and manage the computer system, customize the environment according to local site needs, and define new areas of computing activities for users.

Kernel is an applications development environment, as well as a run-time environment providing standard services to applications software. It is *not* an operating system, but a set of utilities and associated files that are executed in an M environment. Kernel is central to VA VistA software strategy; in that it permits any VistA software application to run without modification on any hardware/software platform that supports American National Standards Institute (ANSI) Standard M. All operating system-specific or hardware-specific code is isolated to Kernel. Therefore, porting VistA to a new environment requires modification only to a handful of Kernel routines.

Kernel provides a computing environment that permits controlled user access, presents menus for choosing from various computing activities, allows device selection for output, enables the tasking of background processes, and offers numerous tools for system management and application programming. Kernel also provides tools for software distribution and installation.

VistA users see the same user interface, regardless of the underlying system architecture, because VistA applications are built using Kernel facilities for signon, database access, option selection, and device selection. As a result, user interaction with the system is constant across VistA applications.

### Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides the doorway into the VistA computer system, the menus that tie together the options and utilities to enhance those options.

For the doorway, Kernel provides the 2-Factor Authentication (2FA) system that you use to establish your identity to the VistA computer system.

Once you have signed on, Kernel provides your menus. Each user on the computer system, as identified by their Microsoft<sup>®</sup> Windows Active Directory profile, has their own individual set of menus and options.

The person or department managing the computer system organizes each user’s menus. From your menu, you can run any application the computer system managers have made available to you. Kernel’s menu system is what is used to make VistA applications (such as Scheduling, Nursing, and Personnel) available to users.

To produce output from VistA applications (such as to printers or to the terminal screen), Kernel provides a common device interface called the Device Handler. To queue a job rather than run it directly, the Device Handler links to a common queuing system called TaskMan.

This manual contains information about these and other parts of Kernel. The intent of this manual is to help you learn to use Kernel and take fullest advantage of the facilities it provides. This manual also includes information for system managers and developers; to find the information of interest to you, the general user, look for sections and sub-sections containing the phrase “User Interface” in their titles.

ADP Application Coordinators (ADPACs) may want to skim through the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide* and concentrate on the user interface sections and sub-sections, particularly issues concerning every Kernel user (such as signon process and menu navigation).

### System Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides the backbone of an M computing platform, providing a mechanism to organize M programs as options, and a way to organize those options into a menu system for users. Kernel provides the following major system management components:

- Alerts provide an integrated notification system.
- Device Handler provides a common device interface.
- Electronic Signature Codes provide a secure electronic approval system.
- File Access Security system manages access to VA FileMan files.
- Kernel Installation and Distribution System (KIDS) provides an application distribution and installation system.
- Menu Manager provides a common menu management system.
- Signon/Security organizes users and allows secure logons.
- TaskMan provides a common job queuing system.

Kernel provides the system manager the means to manage a secure, multi-user M-based computer system. Some typical daily tasks performed by system managers using Kernel system management tools include:

- Setting up accounts for new users and terminating accounts for expired users.
- Adding and subtracting options from users’ menus.
- Controlling file access for users.
- Monitoring TaskMan task queues.
- Terminating unwanted tasks.
- Monitoring devices.
- Creating and modifying links to output devices in the DEVICE (#3.5) file.
- Installing software applications.

Within sections and sub-sections of these user guides you can find general user information in the “User Interface” section and system manager information in the “System Management” section.

![](kernel-8-0-systems-management-main-directory/003.png) REF: For information on developer tools (such as Direct Mode Utilities and Application Program Interfaces \[APIs\]), see the [*Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf). Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet Website.  
  
Information on recommended system configuration and setting Kernel’s site parameters, as well as lists of files, routines, options, and other components are documented in the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.  
  
Information about managing computer security, which includes a detailed description of techniques that can be used to monitor and audit computing activity, is presented in the *Kernel Security Tools Manual*.  
  
Instructions for installing Kernel are provided in the *Kernel Installation Guide*. This guide also includes information about software application management (such as recommended settings for site parameters and scheduling time frames for tasked options).

## Kernel Systems Management User Guides—Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This describes the overall structure of all Kernel 8.0 System Management User Guides listed in Section <u>1.1</u>, “<u>Kernel Systems Management User Guides—Main</u> Directory.”

### How to Use these Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout the Kernel Systems Management User Guides, advice and instruction are offered about the numerous Kernel 8.0 and Kernel Toolkit 7.3 tools and functionality provided for the Veterans Health Information Systems and Technology Architecture (VistA) system management and end-users (such as site parameters).

![](kernel-8-0-systems-management-main-directory/004.png) REF: For information on developer tools (such as Direct Mode Utilities and Application Program Interfaces \[APIs\]), see the [*Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf). Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet website.  
  
Information on recommended system configuration and setting Kernel’s site parameters, as well as lists of files, routines, options, and other components are documented in the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.  
  
Information about managing computer security, which includes a detailed description of techniques that can be used to monitor and audit computing activity, is presented in the *Kernel Security Tools Manual*.  
  
Instructions for installing Kernel are provided in the *Kernel Installation Guide*. This guide also includes information about software application management (such as *recommended* settings for site parameters and scheduling time frames for tasked options).

The Kernel Systems Management User Guides are further organized within each document in the following order:

1\. User Interface—Information of relevance to general end-users.

2\. System Management—Information of relevance to system managers.

When a subject is large enough (such as Signon/Security), separate sections are devoted to the “User Interface” and “System Management” topics. In other cases, where the subject matter is smaller (such as the discussion of the Browser device), the two divisions of audience are contained entirely within a section or sub-section.

### Intended Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The intended audience of the Kernel Systems Management User Guides are the following stakeholders:

- Product Delivery Service (PDS)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS)—Personnel who support Kernel-related products.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](kernel-8-0-systems-management-main-directory/005.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per [VA Directive 6402](http://www.va.gov/vapubs/viewPublication.asp?Pub_ID=718&FType=2) (pending signature), these routines should *not* be modified.

![](kernel-8-0-systems-management-main-directory/006.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

#### Documentation Disclaimer

This manual provides an overall explanation of using Kernel; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) Product Delivery Service (PDS) Intranet Website.

![](kernel-8-0-systems-management-main-directory/007.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These user guides use several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. [Table 1](#_Ref455486405) gives a description of each of these symbols:

| Symbol                                                                                              | Description                                                                                                                       |
|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-systems-management-main-directory/008.png)   | NOTE / REF: Used to inform the reader of general information including references to additional reading material.             |
| ![](kernel-8-0-systems-management-main-directory/009.png) | ATTENTION / CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

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

- “Snapshots” of computer commands and online displays (that is screen captures/dialogs) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
  - User’s responses to online prompts are boldface and (optionally) highlighted in yellow (such as <span class="mark">\<Enter\></span>).
  - Emphasis within a dialog box is boldface and (optionally) highlighted in blue (such as<span class="mark"> STANDARD LISTENER: RUNNING</span>).
  - Some software code reserved/key words are boldface with alternate color font.
  - References to “\<Enter\>” within these snapshots indicate that the user should press the Enter (or Return) key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
  - Author’s comments are displayed in italics or as “callout” boxes.

![](kernel-8-0-systems-management-main-directory/010.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- These user guides refer to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M “\>” prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (such as XUPROGMODE security key).

![](kernel-8-0-systems-management-main-directory/011.png) NOTE: Other software code (such as Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (that is CamelCase).

### Internal Word Navigation Links Setup Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document uses Microsoft® Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar for all Word documents, see the [*Tech Writer Tips: Internal Word Navigation Links Setup*](https://dvagov.sharepoint.com/:b:/r/sites/OITDSOSPMTW/Library/Internal_Word_Navigation_Links_Setup_Steps.pdf?csf=1&web=1&e=oc8dP8) (VA Intranet) document.

![](kernel-8-0-systems-management-main-directory/012.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

### How to Obtain Technical Information Online

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exported VistA M Server-based software file, routine, and global documentation can be generated with Kernel, MailMan, and VA FileMan utilities.

![](kernel-8-0-systems-management-main-directory/013.png) NOTE: Methods of obtaining specific technical information online are indicated where applicable under the appropriate section.  
  
REF: See the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual* for further information.

#### Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

#### Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](kernel-8-0-systems-management-main-directory/014.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

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
- *Kernel 8.0 Systems Management Main Directory* (this manual): Divided into seven User Guides, based on the following functional divisions within Kernel:”
  - *Kernel 8.0 Systems Management: Signon/Security User Guide*
  - *Kernel 8.0 Systems Management: Menu Manager User Guide*
  - *Kernel 8.0 Systems Management: Device Handler User Guide*
  - *Kernel 8.0 Systems Management: TaskMan User Guide*
  - *Kernel 8.0 Systems Management: KIDS User Guide*
  - *Kernel 8.0 Systems Management: Toolkit User Guide*
  - *Kernel 8.0 Systems Management: Utilities User Guide*
- *Kernel 8.0 Developer’s Guide: \<Function\> User Guides*
- *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*
- *Kernel Security Tools Manual*
- Kernel VA Intranet Website.

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](kernel-8-0-systems-management-main-directory/015.png) REF: Kernel manuals are located on the VDL at: [VDL Kernel Application Documents](http://www.va.gov/vdl/application.asp?appid=10)

VistA documentation and software can also be downloaded from the Network File Share (NFS) server.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-main-directory/016.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

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
<td><strong>Alpha Testing</strong></td>
<td>In VA terminology, Alpha testing is when a VistA test software application is running in a site’s account.</td>
</tr>
<tr class="even">
<td><strong>Auto Menu</strong></td>
<td>An indication to Menu Manager that the current user’s menu items should be displayed automatically. When AUTO MENU is <em>not</em> in effect, the user <em>must</em> enter a question mark at the menu’s select prompt to see the list of menu items.</td>
</tr>
<tr class="odd">
<td><strong>Beta Testing</strong></td>
<td>In VA terminology, Beta testing is when a VistA test software application is running in a Production account.</td>
</tr>
<tr class="even">
<td><strong>Capacity Management</strong></td>
<td>The process of assessing a system’s capacity and evaluating its efficiency relative to workload to optimize system performance. Kernel provides several utilities.</td>
</tr>
<tr class="odd">
<td><strong>Checksum</strong></td>
<td>A numeric value that is the result of a mathematical computation involving the characters of a routine or file.</td>
</tr>
<tr class="even">
<td><strong>Cipher</strong></td>
<td><p>A system that arbitrarily represents each character as one or more other characters.</p>
<p>(See also: ENCRYPTION.)</p></td>
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
<td>This field takes data from other fields and performs a predetermined mathematical function (such as adding two columns together). You do <em>not</em>, however, see the results of the mathematical function on the screen. Only when you are printing or displaying information on the screen do you see the results for this type of field.</td>
</tr>
<tr class="even">
<td><strong>DEA</strong></td>
<td>Drug Enforcement Administration.</td>
</tr>
<tr class="odd">
<td><strong>Device Handler</strong></td>
<td>The Kernel module that provides a mechanism for accessing peripherals and using them in controlled ways (such as user access to printers or other output devices).</td>
</tr>
<tr class="even">
<td><strong>DIFROM</strong></td>
<td>VA FileMan utility that gathers all software components and changes them into routines (<strong>namespaceI*</strong> routines) so that they can be exported and installed in another VA FileMan environment.</td>
</tr>
<tr class="odd">
<td><strong>Double Quote (“)</strong></td>
<td>A symbol used in front of a <strong>Common</strong> option’s menu text or synonym to select it from the <strong>SYSTEM COMMAND OPTIONS</strong> [XUCOMMAND] menu (aka <strong>Common</strong> menu). For example, the five character string <strong>“TBOX</strong> selects the User’s Toolbox [XUSERTOOLS] <strong>Common</strong> option.</td>
</tr>
<tr class="even">
<td><strong>DR String</strong></td>
<td>The set of characters used to define the <strong>DR</strong> variable when calling VA FileMan. Since a series of parameters may be included within quotes as a literal string, the variable’s definition is often called the <strong>DR</strong> string. To define the fields within an edit sequence, for example, the developer may specify the fields using a <strong>DR</strong> string rather than an INPUT template.</td>
</tr>
<tr class="odd">
<td><strong>DUZ(0)</strong></td>
<td>A local variable that holds the FILE MANAGER ACCESS CODE (#3) field of the signed-on user.</td>
</tr>
<tr class="even">
<td><strong>Encryption</strong></td>
<td>Scrambling data or messages with a cipher or code so that they are unreadable without a secret key. In some cases, encryption algorithms are one directional, that is, they only encode, and the resulting data <em>cannot</em> be unscrambled (such as Access and Verify Codes).</td>
</tr>
<tr class="odd">
<td><strong>EPCS</strong></td>
<td>Drug Enforcement Administration (DEA) Electronic-Prescribing of Controlled Substances (ePCS).</td>
</tr>
<tr class="even">
<td><strong><br />
File Access Security System</strong></td>
<td>Formerly known as Part 3 of the Kernel Inits. If the File Access Security conversion has been run, file-level security for VA FileMan files is controlled by Kernel’s File Access Security system, <em>not</em> by VA FileMan Access Codes (that is FILE MANAGER ACCESS CODE [#3] field in the NEW PERSON [#200] file).</td>
</tr>
<tr class="odd">
<td><strong>Forced Queuing</strong></td>
<td>A device attribute indicating that the device can only accept queued tasks. If a job is sent for foreground processing, the device rejects it and prompt the user to queue the task instead.</td>
</tr>
<tr class="even">
<td><strong>Go-Home Jump</strong></td>
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
<td><strong>Jump</strong></td>
<td><p>In VistA applications, the Jump command allows you to go from a particular field within an option to another field within that same option. You can also Jump from one menu option to another menu option without having to respond to all the prompts in between. To jump, type a caret (<strong>^</strong>) and then type the name of the field or option to which you wish to jump.</p>
<p>(See also GO-HOME JUMP, PHANTOM JUMP, RUBBER-BAND JUMP, or UP-ARROW JUMP.)</p></td>
</tr>
<tr class="odd">
<td><strong>Jump Start</strong></td>
<td>A logon procedure whereby the user enters the “Access Code;Verify code;option” to go immediately to the target option, indicated by its menu text or synonym. The jump syntax can be used to reach an option within the menu trees by entering “<strong>accesscode;verifycode;option</strong>”.</td>
</tr>
<tr class="even">
<td><strong>Kermit</strong></td>
<td>A standard file transfer protocol. It is supported by Kernel and can be set up as an alternate editor.</td>
</tr>
<tr class="odd">
<td><strong>Manager Account</strong></td>
<td>A UCI that holds vendor shared routines.</td>
</tr>
<tr class="even">
<td><strong>Menu Cycle</strong></td>
<td>The process of first visiting a menu option by picking it from a menu’s list of choices and then returning to the menu’s select prompt. Menu Manager keeps track of information (such as the user’s place in the menu trees) according to the completion of a cycle through the menu system.</td>
</tr>
<tr class="odd">
<td><strong>Menu Manager</strong></td>
<td>The Kernel module that controls the presentation of user activities (such as menu choices or options). Information about each user’s menu choices is stored in the Compiled Menu System, the <strong>^XUTL</strong> global, for easy and efficient access.</td>
</tr>
<tr class="even">
<td><strong>Menu System</strong></td>
<td>The overall Menu Manager logic as it functions within the Kernel framework.</td>
</tr>
<tr class="odd">
<td><strong>Menu Template</strong></td>
<td>An association of options as pathway specifications to reach one or more destination options. The final options <em>must</em> be executable activities and <em>not</em> merely menus for the template to function. Any user can define user-specific MENU templates through the corresponding <strong>Common</strong> option.</td>
</tr>
<tr class="even">
<td><strong>Menu Trees</strong></td>
<td>The menu system’s hierarchical tree-like structures that can be traversed or navigated, like pathways, to give users easy access to various options.</td>
</tr>
<tr class="odd">
<td><strong>PAC</strong></td>
<td><strong>P</strong>rogrammer <strong>A</strong>ccess <strong>C</strong>ode. An optional user attribute that can function as a second level password into programmer mode.</td>
</tr>
<tr class="even">
<td><strong>Part 3 of the Kernel Init</strong></td>
<td>See FILE ACCESS SECURITY SYSTEM.</td>
</tr>
<tr class="odd">
<td><strong>Pattern Match</strong></td>
<td>A preset formula used to test strings of data. Refer to your system’s M Language Manuals for information on Pattern Match operations.</td>
</tr>
<tr class="even">
<td><strong>Phantom Jump</strong></td>
<td>Menu jumping in the background. Used by the menu system to check menu pathway restrictions.</td>
</tr>
<tr class="odd">
<td><strong>Primary Menus</strong></td>
<td>The list of options presented at signon. Each user <em>must</em> have a PRIMARY MENU OPTION (#201) to sign on and reach Menu Manager. Users are given primary menus by system administrators. This menu should include most of the computing activities the user needs Value is stored in the PRIMARY MENU OPTION (#201) field in the NEW PERSON (#200) file.</td>
</tr>
<tr class="even">
<td><strong>Programmer Access</strong></td>
<td>Privilege to become a developer on the system and work outside many of the security controls of Kernel. Accessing programmer mode from Kernel’s menus requires having the at-sign security code (<strong>@</strong>), which sets the variable <strong>DUZ(</strong>A<strong>0</strong>A<strong>)=@</strong>.</td>
</tr>
<tr class="odd">
<td><strong>Protocol</strong></td>
<td>An entry in the PROTOCOL (#101) file. Used by the Order Entry/Results Reporting (OE/RR) software to support the ordering of medical tests and other activities. Kernel includes several protocol-type options for enhanced menu displays within the OE/RR software.</td>
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
<td><strong>Rubber-Band Jump</strong></td>
<td><p>A menu jump used to go out to an option and then return, in a bouncing motion. The syntax of the jump is two carets (<strong>^^</strong>, uppercase-6 on most keyboards) followed by an option’s menu text or synonym (such as <strong>^^Print Option File</strong>). If the two carets are <em>not</em> followed by an option specification, the user is returned to the primary menu.</p>
<p>(See also: GO-HOME JUMP.)</p></td>
</tr>
<tr class="even">
<td><strong>Scheduling Options</strong></td>
<td>A way of ordering TaskMan to run an option at a designated time with a specified rescheduling frequency (such as once per week).</td>
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
<td>A controlled system whereby menus and security keys can be allocated by people other than system administrators (such as application coordinators) who have been so authorized. SMD is a part of Menu Manager.</td>
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
<td><p>A field in the OPTION (#19) file. Options can be selected by their menu text or synonym.</p>
<p>(See also: MENU TEXT.)</p></td>
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
<td><strong>Up-Arrow Jump</strong></td>
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

![](kernel-8-0-systems-management-main-directory/017.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.