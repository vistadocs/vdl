---
title: Kernel 8.0 and VA FileMan 22.2 File Access Security
doc_type: SG
doc_label: Security Guide
doc_layer: anchor
doc_subject: and VA FileMan 22.2 File Access Security
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
menu_options: 14
description: 
audience: 
keywords: 
  - access
  - security
  - fileman
  - strong
  - kernel
  - span
  - class
  - table
  - example
  - classic
page_count: 0
word_count: 4498
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/fm22_krn8_file_security.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/fm22_krn8_file_security.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  VA FileMan 22.2 and Kernel 8.0

  File Access Security User Guide
---

![](kernel-8-0-and-va-fileman-22-2-file-access-security/001.png)

July 2007

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc244336446" class="anchor"></span>Revision History

<table>
<caption><blockquote>
<p><span id="_Ref87258570" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p>
</blockquote></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 30%" />
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
<td>07/30/2025</td>
<td>2.0</td>
<td><p>Updates:</p>
<ul>
<li><p>Remodeled document to follow current documentation standards and style guidelines.</p></li>
<li><p>Content updated based on review of the "File Access Security" section in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf"><em><u>Kernel 8.0 Systems Management: Signon/Security User Guide</u></em></a>.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>07/--/2007</td>
<td>1.0</td>
<td>Initial release of <em>VA FileMan 22.2 and Kernel 8.0 File Access Security User Guide</em>.</td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref87258570" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Table of Contents

<span id="_Toc204785937" class="anchor"></span>List of Figures

[Figure 1: Example─Verify Site is Using Kernel File Access Security [4](#_Ref168761732)](#_Ref168761732)

[Figure 2: Example─Security Property Values in the NEW PERSON (#200) File [5](#_Ref168883552)](#_Ref168883552)

<span id="_Toc204785938" class="anchor"></span>List of Tables

[Table 1: Documentation Symbol Descriptions [v](#_Ref87258570)](#_Ref87258570)

[Table 2: File Level Security Properties—Classic VA FileMan File Access Security [7](#_Ref168826189)](#_Ref168826189)

  
<span id="_Toc234301877" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instruction are offered about VA FileMan and Kernel 8.0 file access security for Veterans Health Information Systems and Technology Architecture (VistA) system management and application developers.

Intended Audience

The intended audience of this manual is the following stakeholders:

- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Product Delivery Service (PDS)—VistA legacy development teams.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/002.png) CAUTION: Kernel routines should never be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per VHA Directive 2004-038, this routine should not be modified.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimers

The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                              | Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-and-va-fileman-22-2-file-access-security/004.png)   | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](kernel-8-0-and-va-fileman-22-2-file-access-security/005.png) | CAUTION/DISCLAIMER: Used to caution the reader to take special notice of critical information.                  |

<span id="_Ref168826189" class="anchor"></span>Table 2: File Level Security Properties—Classic VA FileMan File Access Security

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either “000” or “666”.
- Patient and user names are formatted as follows:

> \<Application Name/Abbreviation/Namespace\>PATIENT,\<N\>

> \<Application Name/Abbreviation/Namespace\>USER,\<N\>

Where:

> *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.

> *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in VA FileMan (DI or FM) or Kernel (XU or KRN) test patient and user names would be documented as follows:

FMPATIENT,ONE; KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; … KRNPATIENT,14; and so on.

FMUSER,ONE; KRNUSER,ONE; KRNUSER,TWO; KRNUSER,THREE; … KRNUSER,14; and so on.

- “Snapshots” of computer commands and online displays (that is screen captures/dialogs) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts will be bold typeface and highlighted in yellow (such as <span class="mark">\<Enter\></span>).
- Emphasis within a dialog box will be highlighted in blue (such as <span class="mark">STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- References to “<span class="mark">\<Enter\></span>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M “\>” prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (such as the XUPROGMODE security key).

![](kernel-8-0-and-va-fileman-22-2-file-access-security/007.png) NOTE: Other software code (such as Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Internal Word Navigation Links Setup Steps

This document uses Microsoft® Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar for all Word documents, see the [*Tech Writer Tips: Internal Word Navigation Links Setup*](https://dvagov.sharepoint.com/:b:/r/sites/OITDSOSPMTW/Library/Internal_Word_Navigation_Links_Setup_Steps.pdf?csf=1&web=1&e=oc8dP8) document.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/009.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/010.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about VA FileMan and Kernel should consult the following:

- VA FileMan User Guide
- VA FileMan Advanced User Guide
- VA FileMan Developer’s Guide
- VA FileMan Technical Manual
- Kernel 8.0 Systems Management Guide: Main Directory
- Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide
- Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual
- Kernel Security Tools Manual

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at the following website: [<u>Adobe Website</u>](http://www.adobe.com/).

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: [<u>VDL Website</u>](https://www.va.gov/vdl/).

VistA documentation and software can also be downloaded from the Network File Share (NFS) repository.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [VA FileMan Reserved Symbols Used to Implement File Access Security](#va-fileman-reserved-symbols-used-to-implement-file-access-security)
- [What Type of File Access Security is Your Site Using?](#what-type-of-file-access-security-is-your-site-using)
- [How to Use the File Access Security at Your Site](#how-to-use-the-file-access-security-at-your-site)
  - [Classic VA FileMan File Access Security](#classic-va-fileman-file-access-security)
    - [Kernel File Access Security vs. Classic VA FileMan File Access Security](#kernel-file-access-security-vs-classic-va-fileman-file-access-security)
    - [File Level Security Properties](#file-level-security-properties)
  - [Kernel File Access Security](#kernel-file-access-security)
    - [File Level Security Properties](#file-level-security-properties-1)
VA FileMan is VistA's database management system. VA FileMan APIs are divided up into two categories:
- Classic VA FileMan─Certain modules within VA FileMan are callable by other M routines or when using the VA FileMan exported menu options. File Access Security checking is performed via Classic VA FileMan APIs.
![](kernel-8-0-and-va-fileman-22-2-file-access-security/011.png) NOTE: Another implementation of File Access Security checking is done via Kernel File Access Security. This topic is detailed further in the "File Access Security" section in the "File Access Security" section in the [*<u>Kernel 8.0 Systems Management: Signon/Security User Guide</u>*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf).
- Database Server (DBS)─No File Access Security checking is performed on VA FileMan Database Server (DBS) calls, because they separate interactions with the database created by developers. They are "silent," meaning there is no interaction with the end-user.
![](kernel-8-0-and-va-fileman-22-2-file-access-security/012.png) NOTE: There is no further discussion about the VA FileMan Database Server (DBS) calls in this documentation. For more information on the VA FileMan DBS calls, see the *VA FileMan Developer’s Guide*.

## VA FileMan Reserved Symbols Used to Implement File Access Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan only recognizes the following two symbols as reserved symbols used to implement File Access Security:

- At-Sign (@)─Programmer access in VistA is defined as DUZ(0)="@". It grants the privilege to become a programmer in VistA. Programmer access allows you to work outside many of the security controls enforced by VA FileMan, enables access to all VA FileMan files, access to modify data dictionaries, etc. It is important to proceed with caution when having access to the system in this way.
- Caret (^)─The caret (^) overrides the At-Sign (@). For example, if the user's DUZ(0)="@", but WRITE ("WR") access is set to a caret (^), that user *cannot* WRITE (such as using the VA FileMan Enter or Edit File Entries \[DIEDIT\] option) to that file. This is often used at the field level, obstructing all DUZ(0) access to that field.

All other symbols/characters are available to use to implement site File Access Security via Classic FileMan APIs at the developer or VA Facilities discretion. DUZ(0) is set after the user has been validated by Kernel. The value for any user's DUZ(0) can be found in the FILE MANAGER ACCESS CODE (#3) field in the NEW PERSON (#200) file.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/013.png) REF: For information about DUZ(0)="@"Programmer access in VistA, see the *VA FileMan Developer’s Guide*, on the VA Software Document Library (VDL): [<u>FileMan (DI) Application</u>](https://www.va.gov/vdl/application.asp?appid=5).

# What Type of File Access Security is Your Site Using?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security control for file access at VA facilities is implemented via either of the following two methods:

- <u>Classic VA FileMan File Access Security</u>
- <u>Kernel File Access Security</u>

To know how to manage file security at your site, it is first necessary to determine which security implementation your site is using. An easy way to determine if the Kernel File Access Security \[XUFILEACCESS\] option has been implemented is to use the VA FileMan Data Dictionary Utilities \[DI DDU\] option, as shown in <u>Figure 1</u>.

Select the List File Attributes \[DILIST\] option. At the "START WITH WHAT FILE:" prompt, select a VA FileMan file from which to display the data dictionary. If your site is using Kernel File Access Security, the following message appears after the file description and security access information is displayed, <u>Figure 1</u>:

(NOTE: Kernel's File Access Security has been installed in this UCI.)

![](kernel-8-0-and-va-fileman-22-2-file-access-security/014.png) NOTE: The file used to create the screen capture in <u>Figure 1</u> is fictitious and used only for the purposes of this example.

<span id="_Ref168761732" class="anchor"></span>Figure 1: Example─Verify Site is Using Kernel File Access Security

VA FileMan Version 22.2

Enter or Edit File Entries

Print File Entries

Search File Entries

Modify File Attributes

Inquire to File Entries

Utility Functions ...

<span class="mark">Data Dictionary Utilities ...</span>

Transfer Entries

Other Options ...

Select VA FileMan \<TEST ACCOUNT\> Option: <span class="mark">DATA \<Enter\></span> Dictionary Utilities

<span class="mark">List File Attributes</span>

Map Pointer Relations

Check/Fix DD Structure

Find Pointers into a File

Update the META Data Dictionary

Select Data Dictionary Utilities \<TEST ACCOUNT\> Option: <span class="mark">LIST \<Enter\></span> File Attributes

START WITH WHAT FILE: FILE// <span class="mark">EXAMPLE \<Enter\></span>

GO TO WHAT FILE: EXAMPLE// <span class="mark">\<Enter\></span>

Select SUB-FILE: <span class="mark">\<Enter\></span>

Select LISTING FORMAT: STANDARD// <span class="mark">\<Enter\></span>

Start with field: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Right Margin: 80// <span class="mark">\<Enter\></span>

STANDARD DATA DICTIONARY \#123 -- EXAMPLE FILE 1

STORED IN ^MYGLOBAL(123, (999 ENTRIES) SITE: \<REDACTED\>.VA.GOV UCI: NVS,NOU

DATA NAME GLOBAL DATA

ELEMENT TITLE LOCATION TYPE

-------------------------------------------------------------------------------

This is an example file.

DD ACCESS: @

RD ACCESS: D

WR ACCESS: d

DEL ACCESS: d

LAYGO ACCESS: d

AUDIT ACCESS: @

(NOTE: Kernel's File Access Security applies to this File.)

*\[Data Dictionary listing continues as it would normally…\]*

If your VA Facility has implemented Kernel File Access Security, it is *not* using Classic VA FileMan File Access Security.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/015.png) NOTE: Developers can also verify Kernel File Access Security by checking for the ^VA(200,"AFOF") cross-reference. If it exists, then Kernel File Access Security has been implemented.

<u>Figure 2</u> shows user field values in the NEW PERSON (#200) file using the same (fictitious) EXAMPLE (#123) file from <u>Figure 1</u>:

<span id="_Ref168883552" class="anchor"></span>Figure 2: Example─Security Property Values in the NEW PERSON (#200) File

NEW PERSON LIST JUN 10,2025 12:18 PAGE 1

FILE MANAGER

NAME ACCESS CODE

DD DEL LAYGO RD WR AUDIT

FILE ACCESS ACCESS ACCESS ACCESS ACCESS ACCESS

---------------------------------------------------------------------------------------------

FMUSER,ONE dS

EXAMPLE YES

A NULL value is equal to ”NO”. In <u>Figure 2</u>, the DUZ(0) for the user named ONE FMUSER is equal to “dS.” Based on the security access shown in <u>Figure 1</u>, this indicates that the user does not have READ (RD) access.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/016.png) REF: For information on the difference between Kernel and VA Classic FileMan File Access Security, see the "<u>Kernel File Access Security vs. Classic</u> VA FileMan File Access Security" section.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/017.png) REF: For information about Kernel File Access Security, see the "File Access Security" section in the [*<u>Kernel 8.0 Systems Management: Signon/Security User Guide</u>*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf).

# How to Use the File Access Security at Your Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to use the File Access Security at your site:

- If your VA Facility is not using Kernel File Access Security, see the "<u>Classic VA FileMan File Access Security</u>" section.
- If your VA Facility is using Kernel File Access Security, see the "<u>Kernel File Access Security</u>" section.

## Classic VA FileMan File Access Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Given the example in <u>Figure 1</u>, if you *do not* see the following message when displaying a VistA file in the VA FileMan Data Dictionary Utilities option, then your site has *not* implemented Kernel File Access Security:

(NOTE: Kernel's File Access Security has been installed in this UCI.)

This means that File Access Security at your site is implemented based on VA FileMan symbol(s) that are set into the security access property for a particular file via Classic VA FileMan APIs. User file access is based upon the VA FileMan symbols contained in the DUZ(0) value.

<span id="Classic_Example" class="anchor"></span>Example

In this example:

- The READ ("RD") access for the (fictitious) EXAMPLE (#123) file in Figure 1, is equal to "D,"
- The user's DUZ(0) is equal to "AaZz."

This means that the user is not able to view the data via VA FileMan's exported menus, because the DUZ(0) does not contain the symbol "D." If that same user's DUZ(0) was equal to Aa<span class="mark">D</span>Zz, then the user is authorized to view the file's data via the VA FileMan's exported menus, because the DUZ(0) contains the symbol "D."

### Kernel File Access Security vs. Classic VA FileMan File Access Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the Classic VA FileMan File Access Security environment, the user (shown in the previous [<u>example</u>](#Classic_Example)) would *not* be authorized to view the data contained in the (fictitious) EXAMPLE (#123) file using the VA FileMan exported menu options, because the user's (ONE FMUSER) FILEMANAGER ACCESS CODE (#3) field in the NEW PERSON (#200) file does not contain the symbol "D." However, in a Kernel File Access Security environment, the file READ ("RD") access is set to YES for the user. Hence, the user would be able to view the data.

### File Level Security Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists the six File Access Security properties involved with File Access Security. If a File Access Security property is *not* defined, the value is NULL. In the Classic VA FileMan File Access Security environment, properties with NULL values allow full user access to the VA FileMan exported menu options for that property.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 43%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th>Access</th>
<th>Security Property Description</th>
<th>Property Location<br />
(Classic VA FileMan)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AUDIT</strong></td>
<td><p>The <strong>AUDIT</strong> security property controls the setting of auditing characteristics and the deletion of audit trails. This property only deals with the auditing of data and <em>not</em> the auditing of data dictionary (DD) changes. To audit DD changes, users would enter "<strong>YES</strong>" at the "DD AUDIT? NO// " prompt when modifying a file's File Security Access. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Fields Being Audited</strong> [DIAUDITED FIELDS]</p></li>
<li><p><strong>Data Dictionaries Being Audited</strong> [DIAUDIT DD]</p></li>
<li><p><strong>Purge Data Audits</strong> [DIAUDIT PURGE DATA]</p></li>
<li><p><strong>Purge DD Audits</strong> [DIAUDIT PURGE DD]</p></li>
<li><p><strong>Turn Data Audit On/Off</strong> [DIAUDIT TURN ON/OFF]</p></li>
</ul></td>
<td><strong>^DIC(&lt;file number&gt;,0,”AUDIT”)=&lt;value&gt;</strong></td>
</tr>
<tr class="even">
<td><strong>DATA DICTIONARY ("DD")</strong></td>
<td><p>The DATA DICTIONARY security property controls who has access to modify the data dictionary. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Modify File Attributes</strong> [DIMODIFY]</p></li>
<li><p><strong>Utility Functions</strong> [DIUTILITY]</p></li>
<li><p><strong>Data Dictionary Utilities</strong> [DI DDU]</p></li>
</ul>
<p>For example, to use the <strong>Map Pointer Relations</strong> option, <strong>DD</strong> access is needed to the PACKAGE (#9.4) file and to the files one selects for mapping.</p></td>
<td><strong>^DIC(&lt;file number&gt;,0,”DD”)=&lt;value&gt;</strong></td>
</tr>
<tr class="odd">
<td><strong>DELETE ("DEL")</strong></td>
<td><p>The <strong>DELETE</strong> security property controls who can delete an existing record that is contained within the file. It does <em>not</em> permit deletion of the file or any of its attribute fields. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Enter or Edit File Entries</strong> [DIEDIT]</p></li>
<li><p><strong>Transfer Entries</strong> [DITRANSFER]</p></li>
</ul></td>
<td><strong>^DIC(&lt;file number&gt;,0,”DEL”)=&lt;value&gt;</strong></td>
</tr>
<tr class="even">
<td><strong>LAYGO</strong></td>
<td><p>The <strong>LAYGO</strong> (Learn As You Go) security property controls who can add a new record to the file. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p>Enter or Edit File Entries [DIEDIT]</p></li>
</ul>
<p>![](kernel-8-0-and-va-fileman-22-2-file-access-security/018.png) <strong>NOTE:</strong> You <em>must</em> have <strong>LAYGO</strong> and <strong>WRITE</strong> access to a file to add new entries. In addition, you <em>must</em> have <strong>WRITE</strong> access at the field level for all required identifier fields.</p></td>
<td><strong>^DIC(&lt;file number&gt;,0,”LAYGO”)=&lt;value&gt;</strong></td>
</tr>
<tr class="odd">
<td><strong>READ ("RD")</strong></td>
<td><p>The <strong>READ</strong> security property controls who has access to read data contained within a file. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Print File Entries</strong> [DIPRINT]</p></li>
<li><p><strong>Search File Entries</strong> [DISEARCH]</p></li>
<li><p><strong>Inquire to File Entries</strong> [DIINQUIRE]</p></li>
<li><p><strong>Statistics</strong> [DISTATISTICS]</p></li>
<li><p><strong>List File Attributes</strong> [DILIST]</p></li>
<li><p><strong>Transfer Entries</strong> [DITRANSFER]</p></li>
</ul>
<p>To transfer text, the user needs <strong>READ</strong> access to the file from which text is being transferred. Similarly, <strong>WRITE</strong> access is needed for the file to which entries are being transferred with this option.</p>
<p>Transfer File Entries (transfer-to file)</p>
<p>![](kernel-8-0-and-va-fileman-22-2-file-access-security/019.png) <strong>NOTE:</strong> <strong>READ</strong> access is also required to use some of the Filegram and Audit options.</p></td>
<td><strong>^DIC(&lt;file number&gt;,0,”RD”)=&lt;value&gt;</strong></td>
</tr>
<tr class="even">
<td><strong>WRITE ("WR")</strong></td>
<td><p>The <strong>WRITE</strong> security property controls who can alter data in an existing record that is contained within the file. It will not permit the adding of new entries to the file. Examples of the VA FileMan options that this property controls are as follows:</p>
<ul>
<li><p><strong>Enter or Edit File Entries</strong> [DIEDIT]</p></li>
<li><p><strong>Transfer Entries</strong> [DITRANSFER]</p></li>
</ul>
<p>To transfer text, the user needs <strong>READ</strong> access to the file from which text is being transferred. Similarly, <strong>WRITE</strong> access is needed for the file to which entries are being transferred with this option.</p>
<p>Transfer File Entries (transfer-to file)</p>
<p>Compare/Merge File Entries</p></td>
<td><strong>^DIC(&lt;file number&gt;,0,”WR”)=&lt;value&gt;</strong></td>
</tr>
</tbody>
</table>

## Kernel File Access Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Given the example in <u>Figure 1</u>, if you *do* see the following message when displaying a VistA file in the VA FileMan Data Dictionary Utilities option:

(NOTE: Kernel's File Access Security has been installed in this UCI.)

File Access Security is controlled by the ACCESSIBLE FILE (#32) Multiple in the NEW PERSON (#200) file. This means that File Access Security to a particular file is not based on the VA FileMan Access Code DUZ(0) value. Rather, a lookup is done on the user's ACCESSIBLE FILE (#32) Multiple record in the NEW PERSON (#200) file to determine which accesses are allowed to the file in question via VA FileMan exported menus. If the user’s VA FileMan Access Code \[that is DUZ(0)\] is equal to the At-Sign (@), they are allowed access to all files.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/020.png) NOTE: Kernel File Access Security is known as an Access Control List in other systems.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/021.png) REF: For more information on Kernel File Access Security, see the "File Access Security" section in the [*<u>Kernel 8.0 Systems Management: Signon/Security User Guide</u>*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_signon_security_ug.pdf).

### File Level Security Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists the six security properties involved with File Access Security for Kernel that are equivalent to the Classic VA FileMan File Access Security. Unlike Classic VA FileMan File Access Security, in a Kernel File Access Security environment, if the security property is not defined (that is the value is NULL), the VA FileMan exported menu options for that property are not open to full access for users.

![](kernel-8-0-and-va-fileman-22-2-file-access-security/022.png) NOTE: These same security properties left undefined in a Classic VA FileMan File Access Security environment allow the related VA FileMan exported menu options up to full access for users.