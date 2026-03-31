---
title: XWB*1.1*73 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: 
app_code: XWB
app_name: Remote Procedure Call (RPC) Broker
section: INF
app_status: active
pkg_ns: XWB
patch_ver: 1.1
patch_id: XWB*1.1*73
group_key: "XWB:XWB:1.1"
file_numbers: []
security_keys: []
menu_options: 11
description: 
audience: 
keywords: 
  - strong
  - broker
  - table
  - class
  - contents
  - server
  - remote
  - client
  - routine
  - vista
page_count: 0
word_count: 17485
section_count: 29
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_tm_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_tm_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=23"
---

---
title: |
  RPC Broker 1.1

  Technical Manual (REDACTED)
---

![](xwb-1-1-73-technical-manual/001.png)

September 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

<span id="_Toc97001457" class="anchor"></span>Revision History

Documentation Revisions

<table>
<caption><p><span id="_Ref449364879" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 42%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Authors</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>09/15/2021</td>
<td>10.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*73 (Client-Side only; no VistA M Server updates):</p>
<ul>
<li><p>Supports Delphi XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4: Sections <u>3.2.2</u> and <u>10.1.1</u>.</p></li>
<li><p>Corrects the following issues:</p></li>
</ul>
<ul>
<li><p>Ensures the data placed into the <strong>Brokerx.User.Division</strong> field is correctly formatted.</p></li>
<li><p>Redesigned the method of certificate processing; it automatically selects the user's Authentication certificate, eliminating the need for the user to select from a list of certificates.</p></li>
</ul>
<ul>
<li><p>Added the <strong>ShowCertDialog</strong> property.</p></li>
<li><p>Deleted references to online help and <strong>.chm</strong> file, since the online help is <em>not</em> being released with RPC Broker Patch XWB*1.1*73.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*73 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>12/17/2020</td>
<td>9.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*72 (Client-Side only; no VistA M Server updates):</p>
<ul>
<li><p>Supports Delphi XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4: Sections <u>3.2.2</u> and <u>10.1.1</u>.</p></li>
<li><p>Corrects the following issues:</p></li>
</ul>
<ul>
<li><p>Ensures the DIVISION field is properly set.</p></li>
<li><p>Addresses Hints and Warnings along with many of the memory leaks.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*72 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>05/05/2020</td>
<td>8.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*71.</p>
<ul>
<li><p>Updated <u>Table 10</u>.</p></li>
<li><p>Changed all references throughout to “Patch XWB*1.1*71” as the latest BDK release.</p></li>
<li><p>Updated references to show RPC Broker Patch XWB*1.1*71 supports Delphi 10.3, 10.2, 10.1, 10.0, and XE8 throughout.</p></li>
<li><p>This was a bug fix-only patch, so no new options, routines, files, fields, security keys, APIs, or RPCs.</p></li>
<li><p>Reformatted all references to file and field name numbers throughout.</p></li>
<li><p>Updated all styles and formatting to match current documentation standards and style guidelines.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*71 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>02/09/2017</td>
<td>7.0</td>
<td><p>Tech Edits based on release of RPC Broker Patch XWB*1.1*65:</p>
<ul>
<li><blockquote>
<p>Reformatted document to follow current documentation standards and style formatting requirements.</p>
</blockquote></li>
<li><blockquote>
<p>Updated references to show RPC Broker Patch XWB*1.1*65 supports Delphi Versions: XE4, XE5, XE6, XE7, XE8, 10 Seattle (10.0), and 10 Berlin (10.1) throughout.</p>
</blockquote></li>
<li><blockquote>
<p>Added Note and explanatory text with reference to the Client Agent in Section <u>1.1.1</u> and Section <u>3.2.1</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Added Section <u>2.1</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Removed reference to Single Signon from <u>Table 3</u> and Section <u>2.2</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Removed file size Note from and updated BSE references to the “8994.5” entry in <u>Table 4</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Deleted the <strong>XWBPRS2</strong> routine from and updated routines released with BSE in <u>Table 6</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Moved Section 5.6, “Exported RPCs to Section <u>9</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Updated title and content in Section <u>7</u>. Added <u>Table 8</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Added Section <u>8</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Updated Section <u>10.1.1</u>.</p>
</blockquote></li>
<li><blockquote>
<p>Removed Note referring to support for SSH and IPv4/IPv6 from Section <u>10.1.2</u>.</p>
</blockquote></li>
</ul>
<ul>
<li><p>Deleted Section 10.1.4, “RPC Broker Remote Procedures;” moved to Section <u>9</u>.</p></li>
<li><p>Added Windows Server 2012 R2 as a supported Windows OS in Section <u>10.2.3</u>. Also, replaced “NT” with “Windows.”</p></li>
<li><p>Deleted the “Signon Delays” section.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*65 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>04/27/2016</td>
<td>6.0</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Reformatted document to follow current documentation standards and style formatting requirements.</p></li>
<li><p>Updated the “Orientation” section.</p></li>
<li><p>Updated Sections 3.2.1 and 3.2.2.</p></li>
<li><p>Updated Table 6.</p></li>
<li><p>Updated Sections 5.3.4, 5.3.5, and 5.3.6.</p></li>
<li><p>Updated Sections 8.1.2 and 8.1.4.</p></li>
<li><p>Updated Sections 8.2.1 and 8.2.3.</p></li>
<li><p>Added the “Troubleshooting” section.</p></li>
<li><p>Deleted references to <strong>TSharedRPCBroker</strong> and <strong>TSharedBroker</strong> components throughout, since they were removed from the software.</p></li>
<li><p>Updated help file references from “BROKER.HLP” to “<strong>Broker_1_1.chm</strong>” throughout.</p></li>
<li><p>Updated references to show RPC Broker Patch XWB*1.1*60 supports Delphi XE7, XE6, XE5, and XE4 throughout.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*60 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>12/04/2013</td>
<td>5.1</td>
<td><p>Tech Edit:</p>
<ul>
<li><p>Updated document for RPC Broker Patch XWB*1.1*50 based on feedback from the developer.</p></li>
<li><p>Removed references related to Virgin Installations throughout.</p></li>
<li><p>Updated file name references throughout.</p></li>
<li><p>Removed distribution files that are obsolete or no longer distributed throughout.</p></li>
<li><p>Updated RPC Broker support on the following software:</p></li>
</ul>
<ul>
<li><p>Microsoft<sup>®</sup> XP and 7.0 (operating system) throughout.</p></li>
<li><p>Microsoft<sup>®</sup> Office Products 2010 throughout.</p></li>
<li><p>Changed references from “Borland” to “Embarcadero” and updated support for Delphi Versions XE5, XE4, XE3, and XE2 throughout.</p></li>
</ul>
<ul>
<li><p>Updated all images for prior Microsoft<sup>®</sup> Windows operating systems to Windows 7 dialogues.</p></li>
<li><p>Updated Section 3.2.</p></li>
<li><p>Updated Section 3.3.1.</p></li>
<li><p>Updated Table 6.</p></li>
<li><p>Updated the option list and descriptions in Section 5 and Table 7.</p></li>
<li><p>Reformatted Section 6.</p></li>
<li><p>Added the <strong>TContextorControl</strong> component to the list in Section 8.1.1.</p></li>
<li><p>Updated Section 8.2.3.</p></li>
<li><p>Updated Sections 11.3.1 and 11.3.2.</p></li>
<li><p>Redacted document for the following information:</p></li>
</ul>
<ul>
<li><p>Names (replaced with role and initials).</p></li>
<li><p>Production IP addresses and ports.</p></li>
<li><p>Intranet websites.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*50 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>07/25/2013</td>
<td>5.0</td>
<td><p>Tech Edit:</p>
<ul>
<li><p>Baselined document.</p></li>
<li><p>Updated all styles and formatting to follow current internal team style template.</p></li>
<li><p>Updated all organizational references.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*50 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>08/26/2008</td>
<td>4.3</td>
<td><p>Updates for RPC Broker Patch XWB*1.1*50:</p>
<ul>
<li><p>Added new properties.</p></li>
<li><p>Support for Delphi 5, 6, 7, 2005, 2006, and 2007.</p></li>
<li><p>Changed references form Patch 47 to Patch 50 where appropriate.</p></li>
</ul></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>07/03/2008</td>
<td>4.2</td>
<td><p>Updates for RPC Broker Patch XWB*1.1*47:</p>
<ul>
<li><p>No content changes required; no new public classes, methods, or properties added to those available in XWB*1.1*40.</p></li>
<li><p>Bug fixes to the <strong>ValidAppHandle</strong> function and fixed memory leaks.</p></li>
<li><p>Support added for Delphi 2005, 2006, and 2007.</p></li>
<li><p>Reformatted document.</p></li>
<li><p>Changed references form Patch 40 to Patch 47 where appropriate.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*50 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>08/29/2006</td>
<td>4.1</td>
<td><p>Added new REMOTE APPLICATION (#8994.5) file to the file list. This file was released with RPC Broker Patch XWB*1.1*45 as part of the Broker Security Enhancement (BSE) Project.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*50 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>02/28/2005</td>
<td>4.0</td>
<td><p>Revised Version for RPC Broker Patches XWB*1.1*35 and 40.</p>
<p>Also, reviewed document and edited for the “Data Scrubbing” and the “PDF 508 Compliance” projects.</p>
<ul>
<li><p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to standards and conventions as indicated below:</p></li>
</ul>
<ul>
<li><p>The first three digits (prefix) of any Social Security Numbers (SSN) start with “<strong>000</strong>” or “<strong>666</strong>.”</p></li>
<li><p>Patient or user names are formatted as follows: XWBPATIENT,[N] or XWBUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., XWBPATIENT, ONE, XWBPATIENT, TWO, etc.).</p></li>
<li><p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p></li>
</ul>
<ul>
<li><p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*35 &amp; 40 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>05/08/2002</td>
<td>3.0</td>
<td><p>Revised Version for RPC Broker Patch XWB*1.1*26.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*26 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>04/08/2002</td>
<td>2.0</td>
<td><p>Revised Version for RPC Broker Patch XWB*1.1*13.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*13 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>09/--/1997</td>
<td>1.0</td>
<td><p>Initial RPC Broker Version 1.1 software release.</p>
<p><strong>RPC Broker 1.1</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref449364879" class="anchor"></span>Table : Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc82599966" class="anchor"></span>List of Figures

[Figure 1: RPC Broker Management Menu Option \[XWB MENU\] [12](#_Ref373762728)](#_Ref373762728)

[Figure 2: RPC Broker Connection Diagnostic Application [39](#_Ref362526803)](#_Ref362526803)

<span id="_Toc82599967" class="anchor"></span>List of Tables

<span id="_Toc8096541" class="anchor"></span>

Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of the Remote Procedure Call (RPC) Broker 1.1 Development Kit (BDK) and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA).

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

<span id="disclaimers" class="anchor"></span>Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](xwb-1-1-73-technical-manual/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimer

This manual provides an overall explanation of RPC Broker and the functionality contained in RPC Broker 1.1; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](xwb-1-1-73-technical-manual/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](xwb-1-1-73-technical-manual/004.png)       | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](xwb-1-1-73-technical-manual/005.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref449365305" class="anchor"></span>Table : Commonly Used RPC Broker Terms

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666.”
- Patient and user names are formatted as follows:
- *\[Application Name\]*PATIENT,*\[N\]*
- *\[Application Name\]*USER,*\[N\]*

Where “*\[Application Name\]*” is defined in the Approved Application Abbreviations document and “*\[N\]*” represents the first name as a number spelled out and incremented with each new entry.

For example, in RPC Broker (XWB) test patient names would be documented as follows:

XWBPATIENT,ONE; XWBPATIENT,TWO; XWBPATIENT,14, etc.

For example, in RPC Broker (XWB) test user names would be documented as follows:

XWBUSER,ONE; XWBUSER,TWO; XWBUSER,14, etc.

- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code are shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts are in boldface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box is in boldface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are in boldface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](xwb-1-1-73-technical-manual/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](xwb-1-1-73-technical-manual/007.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Click/Highlight the Back command and press Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Click/Highlight the Forward command and press Add to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](xwb-1-1-73-technical-manual/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

Commonly Used Terms

<u>Table 2</u> lists terms and their descriptions that can be helpful while reading the RPC Broker documentation:

<table>
<caption><p><span id="_Ref468281704" class="anchor"></span>Table : RPC Broker—Site Parameter References</p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Client</td>
<td>A single term used interchangeably to refer to a user, the workstation (i.e., PC), and the portion of the program that runs on the workstation.</td>
</tr>
<tr class="even">
<td>Component</td>
<td><p>A software object that contains data and code. A component may or may not be visible.</p>
<p>![](xwb-1-1-73-technical-manual/009.png) <strong>REF:</strong> For a more detailed description, see the <em>Embarcadero Delphi for Windows User Guide</em>.</p></td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>The Graphical User Interface application that is developed for the client workstation.</td>
</tr>
<tr class="even">
<td>Host</td>
<td>The term Host is used interchangeably with the term Server.</td>
</tr>
<tr class="odd">
<td>Server</td>
<td>The computer where the data and the RPC Broker remote procedure calls (RPCs) reside.</td>
</tr>
</tbody>
</table>

<span id="_Ref468281704" class="anchor"></span>Table : RPC Broker—Site Parameter References

![](xwb-1-1-73-technical-manual/010.png) REF: For additional terms and definition, see the “[Glossary](#glossary).”

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xwb-1-1-73-technical-manual/011.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](xwb-1-1-73-technical-manual/012.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- Remote Procedure Call (RPC) Broker—VistA Client/Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language
- Object Pascal programming language
- Object Pascal programming language/Embarcadero Delphi Integrated Development Environment (IDE)—RPC Broker

References

Readers who wish to learn more about RPC Broker should consult the following:

- *RPC Broker Release Notes*
- *RPC Broker Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*
- *RPC Broker Systems Management Guide*
- *RPC Broker Technical Manual* (this manual)
- *RPC Broker User Guide*
- *RPC Broker Developer’s Guide*
- RPC Broker VA Intranet website.  
    
  This site provides announcements, additional information (e.g., Frequently Asked Questions \[FAQs\], advisories), documentation links, archives of older documentation and software downloads.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) website: <http://www.va.gov/vdl/>

The RPC Broker documentation is located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=23>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Product Overview](#product-overview)
    - [RPC Broker Includes](#rpc-broker-includes)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Namespace](#namespace)
    - [RPC Broker](#rpc-broker)
    - [Broker Security Enhancement (BSE)](#broker-security-enhancement-bse)
  - [Site Parameters](#site-parameters)
  - [Performance and Scalability](#performance-and-scalability)
- [Files](#files)
  - [VistA M Server Files](#vista-m-server-files)
  - [Client Files](#client-files)
    - [End-User Workstation](#end-user-workstation)
    - [Programmer Workstation](#programmer-workstation)
  - [Global Translation, Journaling, and Protection](#global-translation-journaling-and-protection)
    - [Translation](#translation)
    - [Journaling](#journaling)
    - [Protection](#protection)
- [Routines](#routines)
- [Exported Options](#exported-options)
  - [XWB BROKER EXAMPLE](#xwb-broker-example)
  - [XWB RPC TEST](#xwb-rpc-test)
  - [XWB MENU](#xwb-menu)
    - [XWB LISTENER EDIT](#xwb-listener-edit)
    - [XWB LISTENER STARTER](#xwb-listener-starter)
    - [XWB LISTENER STOP ALL](#xwb-listener-stop-all)
    - [XWB LOG CLEAR](#xwb-log-clear)
    - [XWB DEBUG EDIT](#xwb-debug-edit)
    - [XWB LOG VIEW](#xwb-log-view)
  - [XWB EGCHO](#xwb-egcho)
    - [Historical Use](#historical-use)
  - [XWB M2M CACHE LISTENER](#xwb-m2m-cache-listener)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
- [Callable Entry Points](#callable-entry-points)
- [Direct Mode Utilities](#direct-mode-utilities)
- [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
- [External Relationships](#external-relationships)
  - [External Interfaces](#external-interfaces)
    - [RPC Broker Components](#rpc-broker-components)
    - [RPC Broker Dynamic Link Library (DLL)](#rpc-broker-dynamic-link-library-dll)
    - [Pascal Functions](#pascal-functions)
  - [External Relations](#external-relations)
    - [Relationship to Other Software](#relationship-to-other-software)
    - [Relationship with Kernel and VA FileMan](#relationship-with-kernel-and-va-fileman)
    - [Relationships with Operating Systems](#relationships-with-operating-systems)
  - [DBA Approvals and Integration Control Registrations (ICRs)](#dba-approvals-and-integration-control-registrations-icrs)
    - [ICRs—Current List for RPC Broker as Custodian](#icrscurrent-list-for-rpc-broker-as-custodian)
    - [ICRs—Detailed Information](#icrsdetailed-information)
    - [ICRs—Current List for RPC Broker as Subscriber](#icrscurrent-list-for-rpc-broker-as-subscriber)
- [Internal Relationships](#internal-relationships)
- [Global Variables](#global-variables)
- [Security](#security)
  - [Security Management](#security-management)
  - [Mail Groups, Bulletins, and Alerts](#mail-groups-bulletins-and-alerts)
  - [Remote Systems](#remote-systems)
    - [Connections](#connections)
    - [Remote Data Views](#remote-data-views)
  - [Interfaces](#interfaces)
  - [Electronic Signatures](#electronic-signatures)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [Official Policies](#official-policies)
- [Troubleshooting](#troubleshooting)
  - [Test the Broker Using the RPC Broker Diagnostic Program](#test-the-broker-using-the-rpc-broker-diagnostic-program)
  - [Verify and Test the Network Connection](#verify-and-test-the-network-connection)
  - [RPC Broker FAQs](#rpc-broker-faqs)
The *RPC Broker Technical Manual* provides descriptive information and instructions on the use of the Remote Procedure Call (RPC) Broker (also referred to as “Broker”) software within the VA’s Veterans Health Information Systems and Technology Architecture (VistA) environment. This document is intended for:
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).
It acquaints users with the utilities, software structure, and functionality of the RPC Broker system modules, including information about the routines and files that comprise this software. It also has information about the software’s structure and recommendations regarding its efficient use. Additional information on installation, security, management features, and other requirements is also included.

## Product Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker is considered to be part of the infrastructure of VistA. It establishes a common and consistent foundation for communication between clients and VistA M Servers.

The RPC Broker is a bridge connecting the client application front-end on the client workstation (e.g., Delphi GUI applications) to the M-based data and business rules on the VistA M Server. It links one part of a program running on a client workstation to its counterpart on the server. The client and the server can be, and most often are, written in different computer languages. Therefore, the RPC Broker bridges the gap between the traditionally proprietary VistA and COTS/HOST products.

### RPC Broker Includes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A common communications driver for the VistA M Server interface that handles the device-specific characteristics of the supported communications protocol.
- An interface component on the VistA M Server, separate from the communications driver, that interprets client messages, executes the required code, and eventually returns data to the communications driver.
- A common file on the VistA M Server that all applications use to store the information about the queries to which they respond (i.e., REMOTE PROCEDURE \[#8994\] file).
- The Client Agent application that runs on client workstations, supporting single signon.

![](xwb-1-1-73-technical-manual/013.png) NOTE: The Client Agent (CLAGENT.exe) on client workstations was used only for legacy Single Sign-On (SSO) functions. Because it is incompatible with 2-factor authentication, it was deprecated and no longer referenced in the RPC Broker Development Kit (BDK).

- The TRPCBroker component for Delphi, enabling development of client applications that can communicate via the RPC Broker.
- A dynamic link library (DLL) that provides access to RPC Broker functionality for development environments other than Delphi.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The *RPC Broker Deployment, Installation, Back-Out, and Rollback Guide* provides detailed information regarding the installation of the RPC Broker. It also contains many requirements and recommendations regarding how the Broker should be configured.

![](xwb-1-1-73-technical-manual/014.png) REF: Before attempting to install the RPC Broker, be sure to read the *RPC Broker Deployment, Installation, Back-Out, and Rollback Guide (DIBRG)*.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RPC Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker namespace is XWB.

### Broker Security Enhancement (BSE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Broker Security Enhancement (BSE)-related software consists of patches that have been assigned to the following namespaces:

- XU—Kernel
- XWB—RPC Broker

![](xwb-1-1-73-technical-manual/015.png) NOTE: The Broker Security Enhancement (BSE)-related software comprises two patches and software releases from the following VistA applications (listed alphabetically):

- Kernel—Kernel Patch XU\*8.0\*404
- RPC Broker—RPC Broker Patch XWB\*1.1\*45

![](xwb-1-1-73-technical-manual/016.png) REF: Kernel components released with the BSE software are documented in the *Kernel 8.0 & Kernel Toolkit 7.3 Toolkit Technical Manual*.

## Site Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists the area of the Broker that requires site parameter review and configuration:

| Functional Area  | Documentation Reference                                                                         |
|------------------|-------------------------------------------------------------------------------------------------|
| Broker Listeners | See the “RPC Broker Site Parameters File” section in the *RPC Broker Systems Management Guide*. |

<span id="_Ref473104650" class="anchor"></span>Table : RPC Broker—Files and Globals

## Performance and Scalability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Current performance statistics are limited. However, results indicate that the processing time and resources consumed by the Broker itself are minimal. The RPC Broker does *not* introduce any additional overhead to the messages sent between the client and the server.

The RPC Broker listener does *not* tend to get overloaded, because it jobs off incoming requests to another process and then keeps listening for another request. This action is only limited by the number of partitions the M configuration supports.

Performance should instead be measured at the application level to determine the amount of resources consumed by VistA client/server applications that use the Broker. Performance and scalability, from a site’s point of view, have been impacted by the load introduced by application executing on the host system, as opposed to the load introduced by the RPC Broker itself.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## VistA M Server Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker consists of a single global with three files. <u>Table 4</u> lists and describes the RPC Broker files. It includes the file number, file name, global location, file description, indicates if there is any data exported with the file and any lists any specific data settings.

<table>
<caption><p><span id="_Toc82600045" class="anchor"></span>Table : RPC Broker—Global Information</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 31%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>File #</th>
<th>File Name</th>
<th>Global Location</th>
<th>Description</th>
<th>Data w/ File</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8994</td>
<td>REMOTE PROCEDURE</td>
<td>^XWB(8994,</td>
<td><p>This file is used as a repository of server-based procedures (i.e., remote procedure calls [RPCs]) in the context of the Client/Server architecture. All RPCs used by any site-specific client/server application software using the RPC Broker interface <em>must</em> be registered and stored in this file. Applications running on client workstations can invoke (call) the RPCs in this file to be executed by the server and the results are returned to the client application. Each RPC is associated with an entry point (i.e., ROUTINE with optional TAG).</p>
<p>![](xwb-1-1-73-technical-manual/017.png) <strong>NOTE:</strong> The RPC (#19.05) subfield of the OPTION (#19) file points to the RPC (#.01) field of the REMOTE PROCEDURE (#8994) file.</p></td>
<td><p>NO</p>
<p>![](xwb-1-1-73-technical-manual/018.png) <strong>NOTE:</strong> RPCs are distributed and installed as separate components during the installation of the RPC Broker.</p></td>
</tr>
<tr class="even">
<td>8994.1</td>
<td>RPC BROKER SITE PARAMETERS</td>
<td>^XWB(8994.1,</td>
<td>Site managers can use this file to configure and adjust many characteristics of an RPC Broker installation/implementation at a site.</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>8994.5</td>
<td>REMOTE APPLICATION</td>
<td>^XWB(8994.5,</td>
<td><p>This file was introduced as part of the Broker Security Enhancement (BSE) Project (i.e., released with RPC Broker Patch XWB*1.1*45). This file helps better secure remote user/visitor access to Remote VistA M Servers initiated by RPC Broker-based GUI applications. Remote user/visitor access permits applications where users need to access a large number of sites and do so <em>without</em> requiring a separate Access and Verify code at each site.</p>
<p>Once BSE is fully implemented, those RPC Broker-based applications that require remote/visitor access <em>must</em> have an entry in this file with a one-way hash of a secure phrase. It is a one-way hash value that is only known to the application that creates it.</p>
<p>Identification of an entry in the file is based on the application passing in the original phrase, which is then hashed and used for a cross-reference lookup.</p>
<p>The application <em>must</em> have at least one entry in the CALLBACKTYPE (#1) Multiple field indicating all of the following:</p>
<ul>
<li><p>Connection type</p></li>
<li><p>Valid address for the authenticating server</p></li>
<li><p>Connection port number.</p></li>
<li><p>URL String for HTTP connections</p></li>
</ul>
<p>This information is necessary for the Remote VistA M Server to directly connect the Authenticating VistA M Server to obtain the demographic information necessary to create or match the user/visitor entry in the NEW PERSON (#200) file. The application also specifies the desired context option for the user/visitor. This is given to the remote user/visitor instead of forcing the application to determine how to set this value.</p></td>
<td>NO</td>
</tr>
</tbody>
</table>

<span id="_Toc82600045" class="anchor"></span>Table : RPC Broker—Global Information

## Client Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### End-User Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-technical-manual/019.png) NOTE: RPC Broker 1.0 released the initial end-user client workstation files (XWB1_0.EXE; 1996). RPC Broker 1.1 released an updated version (XWB1_1WS.EXE; 1997). Thus, this installation has *not* been updated since 1997. However, the standard VA workstation disk image includes the field-tested end-user client workstation files from (unreleased) patch XWB\*1.1\*58.

- ..\Program Files (x86)\VistA\Broker
- CLAGENT.exe (Obsolete)

![](xwb-1-1-73-technical-manual/020.png) NOTE: The Client Agent (CLAGENT.exe) on client workstations was used only for legacy Single Sign-On (SSO) functions. Because it is incompatible with 2-factor authentication, it was deprecated and no longer referenced in the RPC Broker Development Kit (BDK).

- CLAGENT.hlp (Obsolete)
- rpctest.exe
- rpctest.hlp
- ..\Windows\System32

### Programmer Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-technical-manual/021.png) NOTE: As of RPC Broker Patch XWB\*1.1\*73, RPC Broker 1.1 supports Delphi Versions: 10.4, 10.3, 10.2, 10.1, 10.0, and XE8.

Files installed vary depending on BDK patch level, installation choices, and Delphi version. For XWB\*1.1\*73, files are often placed in the following directories:

- ..\Program Files (x86)\VistA\BDK32\Samples\BrokerEx
- ..\Program Files (x86)\VistA\BDK32\Samples\BSE
- ..\Program Files (x86)\VistA\BDK32\Source

After installing and compiling the Broker Development Kit (BDK) in a developer workstation, Delphi stores .bpl and .dcp files in the default working paths for the Delphi Integrated Development Environment (IDE). The exact path and file name depend on the versions of Delphi and the version of Microsoft<sup>®</sup> Windows you are running. For example, with Delphi XE8 running on Microsoft<sup>®</sup> Windows 7, the default paths and file names are:

- C:\Users\Public\Public Documents\RAD Studio\12.0\Bpl\\XWB_DXE8.bpl
- C:\Users\Public\Public Documents\RAD Studio\12.0\Bpl\\XWB_RXE8.bpl
- C:\Users\Public\Public Documents\RAD Studio\12.0\Dcp\\XWB_DXE8.dcp
- C:\Users\Public\Public Documents\RAD Studio\12.0\Dcp\\XWB_RXE8.dcp

## Global Translation, Journaling, and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Translation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Translation is *recommended* for the sole RPC Broker global (i.e., ^XWB global). The ^XWB global has the potential to be read-intensive as more and more remote procedures are added to it in the future.

![](xwb-1-1-73-technical-manual/022.png) REF: Consult the Cookbook recommendations for suggestions regarding journaling, translation, and replication; the information here may not apply.

### Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Journaling of this global is not required, since the ^XWB global, for the most part is static (except during the addition of new remote procedures).

### Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following global protection should be set:

<table>
<caption><p><span id="_Ref473123184" class="anchor"></span>Table : RPC Broker—Routines</p></caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Global Name</th>
<th>Caché Protection</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>^XWB</strong></td>
<td><p>Owner: <strong>RWD</strong></p>
<p>Group: <strong>N</strong></p>
<p>World: <strong>N</strong></p>
<p>Network: <strong>RWD</strong></p></td>
</tr>
</tbody>
</table>

<span id="_Ref473123184" class="anchor"></span>Table : RPC Broker—Routines

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists the routines exported with the RPC Broker. A brief description of the routines is provided.

![](xwb-1-1-73-technical-manual/023.png) NOTE: Those routine entries exported with the Broker Security Enhancement (BSE) and M2M Broker are shaded in grey in <u>Table 6</u>.

<table>
<caption><p><span id="_Ref373829125" class="anchor"></span>Table : RPC Broker—Exported Options (listed alphabetically by option name)</p></caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>XWB2HL7</strong></td>
<td>This routine contains various functions and procedures that are used by the Broker for Remote Data Views (RDV) via HL7.</td>
</tr>
<tr class="even">
<td><strong>XWB2HL7A</strong></td>
<td>This routine contains various functions and procedures that are used by the Broker for Remote Data Views (RDV) via HL7.</td>
</tr>
<tr class="odd">
<td><strong>XWB2HL7B</strong></td>
<td>This routine contains various functions and procedures that are used by the Broker for Remote Data Views (RDV) via HL7.</td>
</tr>
<tr class="even">
<td><strong>XWB2HL7C</strong></td>
<td>This routine contains various functions and procedures that are used by the Broker for Remote Data Views (RDV) via HL7.</td>
</tr>
<tr class="odd">
<td><strong>XWB45PO</strong></td>
<td>This post-install routine was released with BSE (i.e., RPC Broker Patch XWB*1.1*45). It contains REMOTE APPLICATION (#8994.5) file entries that are used for development and testing by BSE.</td>
</tr>
<tr class="even">
<td><strong>XWBBRK</strong></td>
<td>This routine contains calls that are designed to parse the various attributes of the Broker messages. All of this information is used internally. In the case of large arrays sent by the client, the function <strong>BREAD</strong> is used to read in the variable length subscripts and values.</td>
</tr>
<tr class="odd">
<td><strong>XWBBRK2</strong></td>
<td>This routine is a continuation of <strong>XWBBRK</strong>. The main entry point (i.e., CAPI actually calls the application RPC.</td>
</tr>
<tr class="even">
<td><strong>XWBCAGNT</strong></td>
<td><p>Server code for RPC Broker client agent application.</p>
<p>![](xwb-1-1-73-technical-manual/024.png) <strong>NOTE:</strong> The Client Agent (<strong>CLAGENT.exe</strong>) on client workstations was used only for legacy Single Sign-On (SSO) functions. Because it is incompatible with 2-factor authentication, it was deprecated and no longer referenced in the RPC Broker Development Kit (BDK).</p></td>
</tr>
<tr class="odd">
<td><strong>XWBDLOG</strong></td>
<td>Debug Logging for Broker</td>
</tr>
<tr class="even">
<td><strong>XWBDRPC</strong></td>
<td>This routine contains various functions and procedures that are used for deferred RPCs by the Broker for Remote Data Views (RDV).</td>
</tr>
<tr class="odd">
<td><strong>XWBEXMPL</strong></td>
<td>This routine is used to support the Broker Example application. The Broker Example application is used to test the RPC Broker connectivity, actions, and RPCs. It is distributed with the Broker.</td>
</tr>
<tr class="even">
<td><strong>XWBFM</strong></td>
<td>This routine contains entry points used to interface to the VA FileMan database server.</td>
</tr>
<tr class="odd">
<td><strong>XWBLIB</strong></td>
<td>This routine contains various functions and procedures used by the Broker. It is best described as a library or depository.</td>
</tr>
<tr class="even">
<td><strong>XWBM2MC</strong></td>
<td>M2M Broker Client APIs.</td>
</tr>
<tr class="odd">
<td><strong>XWBM2MEZ</strong></td>
<td>This routine was released with BSE (i.e., RPC Broker Patch XWB*1.1*45). It contains various functions and procedures for M-to-M Broker server connections that are used by BSE.</td>
</tr>
<tr class="even">
<td><strong>XWBM2MS</strong></td>
<td>M2M Broker Server.</td>
</tr>
<tr class="odd">
<td><strong>XWBM2MT</strong></td>
<td>M2M Broker Example.</td>
</tr>
<tr class="even">
<td><strong>XWBPRS</strong></td>
<td>RPC Broker Message Parser.</td>
</tr>
<tr class="odd">
<td><strong>XWBRL</strong></td>
<td>M2M Broker Link Methods.</td>
</tr>
<tr class="even">
<td><strong>XWBRM</strong></td>
<td>M2M Broker Server Request Manager. This routine was enhanced with BSE (i.e., RPC Broker Patch XWB*1.1*45).</td>
</tr>
<tr class="odd">
<td><strong>XWBRMX</strong></td>
<td>M2M Broker Server Request Manager.</td>
</tr>
<tr class="even">
<td><strong>XWBRPC</strong></td>
<td>M2M Broker Server Message Request Handler (MRH).</td>
</tr>
<tr class="odd">
<td><strong>XWBRPCC</strong></td>
<td>M2M Broker Client Utilities.</td>
</tr>
<tr class="even">
<td><strong>XWBRW</strong></td>
<td>Read/Write for Broker TCP.</td>
</tr>
<tr class="odd">
<td><strong>XWBSEC</strong></td>
<td>This routine contains various functions and procedures used by the Broker. Calls in this routine are used for client/server security.</td>
</tr>
<tr class="even">
<td><strong>XWBTCP</strong></td>
<td>This routine contains functions and procedures used to control the Broker TCP/IP Listener process. Systems personnel can use calls in this routine to start, stop, and debug the Broker process.</td>
</tr>
<tr class="odd">
<td><strong>XWBTCPC</strong></td>
<td>This job is started for each Broker request. The Listener process (i.e., <strong>XWBTCPL</strong>) will receive a connection request from a client and then dispatch, using the M <strong>JOB</strong> command, <strong>XWBTCPC</strong> to manage the rest of the interaction.</td>
</tr>
<tr class="even">
<td><strong>XWBTCPL</strong></td>
<td>This is the Broker Listener process. System administrators start this job. It remains running on a system listening for TCP/IP connection requests. Once a request is received, this routine will start a separate process to manage the rest of the connection, then returns to “listening” for a new request.</td>
</tr>
<tr class="odd">
<td><strong>XWBTCPM</strong></td>
<td>TCP/IP Process Handler.</td>
</tr>
<tr class="even">
<td><strong>XWBTCPM1</strong></td>
<td>Support for <strong>XWBTCPM</strong>.</td>
</tr>
<tr class="odd">
<td><strong>XWBTCPM2</strong></td>
<td>Test WEB Service. This routine was enhanced with BSE (i.e., RPC Broker Patch XWB*1.1*45).</td>
</tr>
<tr class="even">
<td><strong>XWBTCPMT</strong></td>
<td>This routine was released with RPC Broker Patch XWB*1.1*43. Test a connection.</td>
</tr>
<tr class="odd">
<td><strong>XWBUTL</strong></td>
<td>M2M Programmer Utilities.</td>
</tr>
<tr class="even">
<td><strong>XWBVL</strong></td>
<td>M2M Broker Server Link Utility.</td>
</tr>
<tr class="odd">
<td><strong>XWBVLC</strong></td>
<td>M2M Broker Client.</td>
</tr>
<tr class="even">
<td><strong>XWBVLL</strong></td>
<td>M2M Broker Listener.</td>
</tr>
<tr class="odd">
<td><strong>XWBZ1</strong></td>
<td><p>Archive: This routine supports the RPC Broker 1.0 Echo application, which was originally used to test RPC Broker connectivity, actions, and APIs.</p>
<p>![](xwb-1-1-73-technical-manual/025.png) <strong>NOTE:</strong> The Echo client application is <em>not</em> distributed with RPC Broker 1.1; it was replaced by the RPC Test application (i.e., <strong>rpctest.exe</strong>). It is listed here for historical purposes only.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref373829125" class="anchor"></span>Table : RPC Broker—Exported Options (listed alphabetically by option name)

![](xwb-1-1-73-technical-manual/026.png) NOTE: For a list of Kernel routines exported with the Broker Security Enhancement (BSE), see the *Kernel 8.0 & Kernel Toolkit 7.3 Toolkit Technical Manual*.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists the options that are exported with the RPC Broker:

<table>
<caption><p><span id="_Ref473111510" class="anchor"></span>Table : RPC Broker—APIs (Callable Entry Points): Supported and Controlled Subscription</p></caption>
<colgroup>
<col style="width: 31%" />
<col style="width: 41%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th>Menu Text</th>
<th>Type</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XWB BROKER EXAMPLE</td>
<td>RPC BROKER PROGRAMMING EXAMPLE</td>
<td><p>Broker (Client/Server)</p>
<p>(See Section <u>5.1</u>.)</p></td>
</tr>
<tr class="even">
<td>XWB DEBUG EDIT</td>
<td>Debug Parameter Edit</td>
<td><p>VistA M Server: Run Routine</p>
<p>(See Section <u>5.3.5</u>.)</p></td>
</tr>
<tr class="odd">
<td>XWB EGCHO</td>
<td>RPC BROKER DEMO/TEST</td>
<td><p>Broker (Client/Server)</p>
<p>(See Section <u>5.4</u>.)</p></td>
</tr>
<tr class="even">
<td>XWB LISTENER EDIT</td>
<td>RPC Listener Edit</td>
<td><p>VistA M Server: Edit</p>
<p>(See Section <u>5.3.1</u>.)</p></td>
</tr>
<tr class="odd">
<td>XWB LISTENER STARTER</td>
<td>Start All RPC Broker Listeners</td>
<td><p>VistA M Server: Run Routine</p>
<p>(See Section <u>5.3.2</u>.)</p></td>
</tr>
<tr class="even">
<td>XWB LISTENER STOP ALL</td>
<td>Stop All RPC Broker Listeners</td>
<td><p>VistA M Server: Run Routine</p>
<p>(See Section <u>5.3.3</u>.)</p></td>
</tr>
<tr class="odd">
<td>XWB LOG CLEAR</td>
<td>Clear XWB Log Files</td>
<td><p>VistA M Server: Run Routine</p>
<p>(See Section <u>5.3.4</u>.)</p></td>
</tr>
<tr class="even">
<td>XWB LOG VIEW</td>
<td>View XWB Log</td>
<td><p>VistA M Server: Run Routine</p>
<p>(See Section <u>5.3.6</u>.)</p></td>
</tr>
<tr class="odd">
<td>XWB M2M CACHE LISTENER</td>
<td>Start M2M RPC Broker Cache Listener</td>
<td><p>VistA M Server: Run Routine</p>
<p>(See Section <u>5.5</u>.)</p></td>
</tr>
<tr class="even">
<td>XWB MENU</td>
<td>RPC Broker Management Menu</td>
<td><p>VistA M Server: Menu</p>
<p>(See Section <u>5.3</u>.)</p></td>
</tr>
<tr class="odd">
<td>XWB RPC TEST</td>
<td>RPC</td>
<td><p>Broker (Client/Server)</p>
<p>(See Section <u>5.2</u>.)</p></td>
</tr>
</tbody>
</table>

<span id="_Ref473111510" class="anchor"></span>Table : RPC Broker—APIs (Callable Entry Points): Supported and Controlled Subscription

Broker client/server applications are Type “B” options (i.e., Broker client/server options) in the OPTION (#19) file:

- User *must* have the client/server application option assigned to them as with any other assigned option in VistA.
- Client/Server application only runs for those users who are allowed to activate it.

![](xwb-1-1-73-technical-manual/027.png) NOTE: The client/server application options will not be displayed in the user’s menu tree.

## XWB BROKER EXAMPLE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC BROKER PROGRAMMING EXAMPLE \[XWB BROKER EXAMPLE\] option is a Broker (Client/Server) option. It supports the Broker Example (BrokerEx) demonstration program provided in the Broker Development Kit (BDK). Developers should assign this option to themselves, if they want to try out the BrokerEx application. For programmers who have the XUPROGMODE security key, however, assigning this option to themselves is *not* necessary.

## XWB RPC TEST

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC \[XWB RPC TEST\] option is a Broker (Client/Server) option. It is a tool that can be used to verify and test the Broker client/server connection and signon process. It displays information about the client and the server and can be a useful debugging tool for system administrators. The rpctest.exe application on the client workstation runs the RPC Broker Diagnostic application.

It is *recommended* that the RPC \[XWB RPC TEST\] option be given to users running Broker-based VistA client/server applications. To enable remote troubleshooting by system administrators for all users, you can put this option on the Common menu (i.e., System Command Options \[XUCOMMAND\] menu). This enables any user to run the rpctest.exe application on their workstation at your request.

## XWB MENU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker Management Menu \[XWB MENU\] is for system managers. It contains the following options:

<span id="_Ref373762728" class="anchor"></span>Figure : RPC Broker Management Menu Option \[XWB MENU\]

Select RPC Broker Management Menu Option:

RPC Listener Edit

Start All RPC Broker Listeners

Stop All RPC Broker Listeners

Clear XWB Log Files

Debug Parameter Edit

View XWB Log

![](xwb-1-1-73-technical-manual/028.png) NOTE: This menu was introduced with RPC Broker Patch XWB\*1.1\*9 and updated with subsequent RPC Broker patches.

### XWB LISTENER EDIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Listener Edit \[XWB LISTENER EDIT\] option creates or edits listener entries in the RPC BROKER SITE PARAMETERS (#8994.1) file.

![](xwb-1-1-73-technical-manual/029.png) REF: For more information on this option, see the *RPC Broker Systems Management Guide*.

### XWB LISTENER STARTER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Start All RPC Broker Listeners \[XWB LISTENER STARTER\] option automatically starts all listeners configured in the RPC BROKER SITE PARAMETERS (#8994.1) file. This option first stops any of these listeners that may be running, and then starts all of them up.

![](xwb-1-1-73-technical-manual/030.png) NOTE: TaskMan *must* be running to use this option. This option was introduced with patch XWB\*1.1\*9.

![](xwb-1-1-73-technical-manual/031.png) REF: For more information on this option, see the *RPC Broker Systems Management Guide*.

### XWB LISTENER STOP ALL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Stop All RPC Broker Listeners \[XWB LISTENER STOP ALL\] option stops all running listeners configured in the RPC BROKER SITE PARAMETERS (#8994.1) file set to automatically start.

### XWB LOG CLEAR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clear XWB Log Files \[XWB LOG CLEAR\] option clears (KILLs) the XWB log files, which are stored in a temporary global under ^TMP(“XWBDEBUG”,\$J).

### XWB DEBUG EDIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Debug Parameter Edit \[XWB DEBUG EDIT\] option edits the Broker debug parameter (XWBDEBUG) defined in the PARAMETER DEFINITION (#8989.51) file and stored in the PARAMETERS (#8989.5) file when set.

### XWB LOG VIEW

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The View XWB Log \[XWB LOG VIEW\] option allows the user to view the temporary debug log files that the Broker can set. The XWBDEBUG parameter *must* be set for log files to be recorded in the ^TMP(“XWBDEBUG”,\$J) temporary global.

## XWB EGCHO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC BROKER DEMO/TEST \[XWB EGCHO\] option is a Broker Client/Server option. It supports development and testing of new versions of the RPC Broker using restricted Remote Procedure Calls (RPCs).

### Historical Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC BROKER DEMO/TEST \[XWB EGCHO\] option was originally used to run the Echo client application, which was first released with RPC Broker 1.0. It was used to test RPC Broker connectivity, actions, and APIs. It was replaced by the RPC Test application (i.e., rpctest.exe).

It called the following RPCs:

- <sup>\*</sup>XWB EGCHO LIST
- <sup>\*</sup>XWB EGCHO BIG LIST
- <sup>\*</sup>XWB EGCHO STRING
- <sup>\*</sup>XWB EGCHO MEMO
- <sup>\*</sup>XWB EGCHO SORT LIST
- XWB GET VARIABLE VALUE

![](xwb-1-1-73-technical-manual/032.png) <sup>\*</sup>NOTE: The EGCHO RPCs were used with an obsolete tester from RPC Broker 1.0; however, they will be removed in a future patch.

![](xwb-1-1-73-technical-manual/033.png) REF: For more information on the RPC Test application (i.e., rpctest.exe), see Section <u>5.2</u>.

## XWB M2M CACHE LISTENER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-technical-manual/034.png) NOTE: This option is for Caché/NT only. It calls STRT^XWBVLL() and is jobbed off.

The Start M2M RPC Broker Cache Listener \[XWB M2M CACHE LISTENER\] option starts the RPC Broker M2M listener. It prompts the user for the port number, and it provides a default value used for M2M.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific archiving procedures or recommendations for the following RPC Broker components:

- ^XWB global
- REMOTE PROCEDURE (#8994) file
- RPC BROKER SITE PARAMETERS (#8994.1) file

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no software-specific purging procedures or recommendations for the following RPC Broker components:

- ^XWB global
- REMOTE PROCEDURE (#8994) file
- RPC BROKER SITE PARAMETERS (#8994.1) file

# Callable Entry Points

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists all of the callable entry points (i.e., Application Program Interfaces \[APIs\]) that are available for general use with RPC Broker (i.e., supported or controlled subscription).

Other programming interfaces are also provided (e.g., Delphi components, DLL, Pascal functions, and RPCs).

![](xwb-1-1-73-technical-manual/035.png) REF: For information on these other programming interfaces, see the “<u>External Relationships</u>” section.

<u>Table 8</u> lists the RPC Broker APIs. It includes the routine name, tag entry point, Integration Control Registration (ICR) number, if any, and a brief description.

| Routine     | Entry Point | ICR \# | Description                                                                                                                                                                                    |
|-------------|-------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XWB2HL7 | DIRECT      | 3144   | This call is used to make an RPC call on a remote facility. Users of this API should be prepared to modify their calls to support strong authentication when made available by Infrastructure. |
| XWB2HL7 | EN1         | 3144   | CPRS Remote Data Views uses this entry point. It places the HL7 message into the HL7 message queue for deferred transfer.                                                                      |
| XWB2HL7 | RPCCHK      | 3144   | Use this entry point after a call to EN1^XWB2HL7 to check the status of the call.                                                                                                              |
| XWBDRPC | RTNDATA     | 3149   | This call returns data retrieved from a remote site.                                                                                                                                           |
| XWBDRPC | CLEAR       | 3149   | This call clears the data (in ^XTMP) connected with the handle that is passed into the call.                                                                                               |
| XWBDRPC | CLEARALL    | 3149   | This call clears *all* Remote or Deferred data for the current job.                                                                                                                            |
| XWBLIB  | \$\$BROKER  | 2198   | Use this function in the M code called by an RPC to determine if the current process is being executed by the Broker.                                                                          |
| XWBLIB  | \$\$RTRNFMT | 2238   | Use this function in the M code called by an RPC to change the return value type that the RPC returns on-the-fly.                                                                              |
| XWBLIB  | VARLST      | 3030   | Access a tag in a Broker routine to extract a list of variables that the Broker needs protected when KILL^XUSCLEAN is called by a package in an RPC.                                           |
| XWBSEC  | CHKPRMIT    | 4053   | Check whether a user is permitted to execute an RPC.                                                                                                                                           |
| XWBLIB  | CRCONTXT    | 4053   | Create a valid RPC Broker context.                                                                                                                                                             |
| XWBLIB  | SET         | 4053   | Store the value of DUZ in Broker “state” prior to calling CVC^XUSRB (which requires the value to be stored in Broker “state”).                                                             |
| XWBTCP  | STOPALL     | 4645   | This entry point stops *all* Broker listeners defined by the RPC Broker site parameters. It does *not* stop listeners controlled by an operating system process.                               |
| XWBTCP  | RESTART     | 4645   | This entry point restarts *all* Broker listeners defined by the RPC Broker site parameters. It does *not* start listeners controlled by an operating system process.                           |

<span id="_Ref473108791" class="anchor"></span>Table : RPC Broker—Direct Mode Utilities

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists all RPC Broker direct mode utilities. Direct mode utilities can be used from programmer mode, but developers *cannot* call them from within applications.

<u>Table 9</u> lists the direct mode utilities in routine order and by tag within each routine.

| Direct Mode Utility | Description                                                                                                           | Reference Documentation |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|-------------------------|
| START^XWBVLL        | Start the M2M Broker Listener.                                                                                        | Not available.      |
| DEBUG^XWBTCPM       | Start an RPC Broker Listener in debug mode.                                                                           | Not available.      |
| CALL^XWBTCPMT       | Run an interactive broker test to connect to a remote listener                                                        | Not available.      |
| CHECK^XWBTCPMT      | Check server setup. This will check for some of the errors that can prevent the Broker listener from getting started. | Not available.      |

<span id="_Ref473108899" class="anchor"></span>Table : RPC Broker—Remote Procedure Calls (RPCs)

# Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 10</u> lists the Remote Procedure Calls (RPCs) in the RPC Broker namespace as stored in the REMOTE PROCEDURE (#8994) file (listed alphabetically by RPC name):

![](xwb-1-1-73-technical-manual/036.png) REF: For more information, see the *RPC Broker User Guide*.

<table>
<caption><p><span id="_Ref59089503" class="anchor"></span>Table : RPC Broker—File Security</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>RPC</th>
<th>Tag^Routine</th>
<th><p>Input</p>
<p>Parameter</p></th>
<th><p>Output / Return</p>
<p>Parameter</p></th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>XWB ARE RPCS AVAILABLE</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>CKRPCS^XWBLIB</td>
<td><ul>
<li><p>RPC: This <strong>0-based</strong> array contains list of RPCs to be checked along with (optionally) a minimum acceptable version of the RPC. The format is:<br />
<br />
<strong>RPCName^RPCVersionNumber</strong><br />
<br />
The <strong>RPCVersionNumber</strong> is only used if the RUN CONTEXT parameter = "<strong>R</strong>". If a numeric value is in the second <strong>^</strong>-piece and the RUN CONTEXT ="<strong>R</strong>", the value <em>must</em> be less than or equal to the value in the VERSION field of the REMOTE PROCEDURE (#8994) file for the RPC to be marked available. <strong>NOTE:</strong> If the VERSION field is <strong>NULL</strong>, the check will fail for any numeric value.</p></li>
<li><p>RUN CONTEXT: Specific context in which RPCs will run. Possible values are:</p></li>
</ul>
<ul>
<li><p><strong>L—</strong>Run Locally (on the server the user is logged on to)</p></li>
<li><p><strong>R—</strong>Run Remotely (on a server the user is not logged on to).</p></li>
</ul>
<p>If this parameter is not sent, RPC is checked for both local and remote. The check is done against the value in the INACTIVE field in the REMOTE PROCEDURE (#8994) file. See that field's description for more details.</p></td>
<td><p>Returns: A <strong>0-based</strong> array. The index corresponds to the index of the RPC in the RPC Input Parameter.</p>
<ul>
<li><p>A value of <strong>1</strong> means the corresponding RPC is available.</p></li>
<li><p>A value of <strong>0</strong> means it is <em>not</em> available.</p></li>
</ul></td>
<td><p>If the RPC in the passed-in array is installed, available in relevant context, and of proper version, it returns either of the following:</p>
<ul>
<li><p><strong>1</strong> for that RPC.</p></li>
<li><p><strong>0</strong>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XWB CREATE CONTEXT</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>CRCONTXT^XWBSEC</td>
<td>OPTION: Encrypted OPTION (#19) file entry name. The encryption algorithm is an external implementation of the Kernel $$ENCRYP^XUSRB1(text) API.</td>
<td><p>Returns either of the following:</p>
<ul>
<li><p><strong>1</strong> if the user is allowed to use this option and RPC is valid.</p></li>
<li><p>Message string explaining why the option or RPC is not allowed.</p></li>
</ul></td>
<td><p>Establishes context on the server, which will be checked by the Broker before executing any other remote procedure. Since context is nothing more than a client/server “<strong>B</strong>”-type option in the OPTION (#19) file, standard MenuMan security is applied in establishing a context. Therefore, a context option can be granted to users exactly the same way as regular options are done using MenuMan. A context cannot be established for either of the following reasons:</p>
<ol type="1">
<li><p>The user has no access to that option.</p></li>
<li><p>The option is temporarily out of order.</p></li>
</ol>
<p>An application can switch from one context to another as often as it needs to. Each time a context is created the previous context is overwritten.</p></td>
</tr>
<tr class="odd">
<td><p>XWB DEFERRED CLEAR</p>
<p><strong>Availability:</strong></p>
<p><strong>PUBLIC</strong></p></td>
<td>CLEAR^XWBDRPC</td>
<td>HANDLE: This is the HANDLE from the XWB DEFERRED RPC.</td>
<td>Returns: The return value is always an array. The first node of the array is equal to <strong>1</strong>.</td>
<td>This RPC is used to CLEAR the data under a handle in the <strong>^XTMP</strong> global.</td>
</tr>
<tr class="even">
<td><p>XWB DEFERRED CLEARALL</p>
<p><strong>Availability:</strong></p>
<p><strong>PUBLIC</strong></p></td>
<td>CLEARALL^XWBDRPC</td>
<td>None.</td>
<td>Returns: The return value is always an array. The first node of the array is equal to <strong>1</strong>.</td>
<td>This RPC is used to CLEAR all the data known to this job in the <strong>^XTMP</strong> global. Makes use of the list in <strong>^TMP("XWBHDL",$J,handle)</strong>.</td>
</tr>
<tr class="odd">
<td><p>XWB DEFERRED GETDATA</p>
<p><strong>Availability:</strong></p>
<p><strong>PUBLIC</strong></p></td>
<td>RTNDATA^XWBDRPC</td>
<td>HANDLE: The HANDLE from the XWB DEFERRED RPC. It is used to link the call to the data.</td>
<td>Returns: The return value is the array of data. In the event of an error condition, the first node of the array is equal to a string with the syntax “<strong>-1^error text</strong>”.</td>
<td>This RPC is used to return the data from the XWB DEFERRED RPC call.</td>
</tr>
<tr class="even">
<td><p>XWB DEFERRED RPC</p>
<p><strong>Availability:</strong></p>
<p><strong>PUBLIC</strong></p></td>
<td>EN1^XWBDRPC</td>
<td><p>RPC: This parameter is the name of the RPC to be run in the background. This first input parameter can include optional version information about the RPC, making the syntax like this:</p>
<p><strong>RPCname^RPCversion</strong></p>
<p>The optional version number will be placed in XWBAPVER when the RPC runs in the background.</p>
<p><strong>P1</strong> through <strong>P10</strong>: These parameters are for the RPC that is to be run in the background.</p></td>
<td>Returns: The return value is always an array. The first node of the array is equal to a string that serves as a HANDLE. This is used to check the status of an RPC request and to retrieve the results of the RPC. In the case of an error condition, the first node of the array is equal to a string with the syntax “<strong>-1^error text</strong>”.</td>
<td>This is the RPC that is called to request that an RPC be run through TaskMan in the background.</td>
</tr>
<tr class="odd">
<td><p>XWB DEFERRED STATUS</p>
<p><strong>Availability:</strong></p>
<p><strong>PUBLIC</strong></p></td>
<td>RPCCHK^XWBDRPC</td>
<td>HANDLE: The HANDLE returned from the XWB DEFERRED RPC.</td>
<td><p>Returns: The return value is always an array. The first node of the array is equal to one of the following values:</p>
<ul>
<li><p>“<strong>-1^Bad Handle—</strong>An invalid handle has been passed.</p></li>
<li><p>“<strong>0^New”—</strong>The request has been sent.</p></li>
<li><p>“<strong>0^Running</strong>”<strong>—</strong>The RPC is still processing.</p></li>
<li><p>“<strong>1^Done</strong>”<strong>—</strong>The RPC has completed, and the data has returned to the local server.</p></li>
</ul>
<p>The data is <em>not</em> returned by this RPC. Use the XWB REMOTE GETDATA RPC to retrieve the data.</p></td>
<td>This RPC returns the status of a deferred RPC.</td>
</tr>
<tr class="even">
<td><p>XWB DIRECT RPC</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>DIRECT^XWB2HL7</td>
<td><ul>
<li><p>LOC: This is the INSTITUTION (#4) file station <strong>#</strong> to send the RPC to.</p></li>
<li><p>RRPC: This is the name of the remote RPC to be run.</p></li>
</ul></td>
<td>Returns: The return value is the array of data. In the case of an error condition, the first node of the array is equal to a string with the syntax “<strong>-1^error text</strong>”.</td>
<td>This is the Broker RPC that is called to request that an RPC be run on a remote system. The data is passed by HL7 to the remote system as is the return value. The difference between this and the XWB REMOTE RPC is this is a blocking call meaning the user's workstation does <em>not</em> process anything else until the data returns from the remote system.</td>
</tr>
<tr class="odd">
<td><p><strong><sup>*</sup></strong>XWB EGCHO BIG LIST</p>
<p><strong>Availability:</strong></p>
<p><strong>RETIRED</strong></p></td>
<td>BIG^XWBZ1</td>
<td>None.</td>
<td>Returns: <strong>32K</strong> String.</td>
<td>This RPC brings back a lot of meaningless data to the client. It exists for support of the EGcho Broker demonstration program</td>
</tr>
<tr class="even">
<td><p><strong><sup>*</sup></strong>XWB EGCHO LIST</p>
<p><strong>Availability:</strong></p>
<p><strong>RETIRED</strong></p></td>
<td>LIST^XWBZ1</td>
<td>None.</td>
<td>Returns: List with <strong>28</strong> entries.</td>
<td>This RPC brings back a small list of elements to the client. It exists for support of the EGcho Broker demonstration program.</td>
</tr>
<tr class="odd">
<td><p><strong><sup>*</sup></strong>XWB EGCHO MEMO</p>
<p><strong>Availability:</strong></p>
<p><strong>RETIRED</strong></p></td>
<td>MEMO^XWBZ1</td>
<td>X: Array of strings.</td>
<td>Returns: Array echoing back the input array.</td>
<td>This RPC accepts text from a client that it sends right back to the client. It exists for support of the EGcho Broker demonstration program.</td>
</tr>
<tr class="even">
<td><p><strong><sup>*</sup></strong>XWB EGCHO SORT LIST</p>
<p><strong>Availability:</strong></p>
<p><strong>RETIRED</strong></p></td>
<td>SRT^XWBZ1</td>
<td><ul>
<li><p>DIRECTION: The string <strong>LO</strong> or <strong>HI</strong>.</p></li>
<li><p>ARRAY: The array of numbers. Pass using <strong>.</strong> syntax.</p></li>
</ul></td>
<td>Returns: Sorted array.</td>
<td>Sorts a given numeric array, starting from <strong>HI</strong> or <strong>LO</strong>. It exists for support of the EGcho Broker demonstration program.</td>
</tr>
<tr class="odd">
<td><p><strong><sup>*</sup></strong>XWB EGCHO STRING</p>
<p><strong>Availability:</strong></p>
<p><strong>RETIRED</strong></p></td>
<td>ECHO1^XWBZ1</td>
<td>INP: String</td>
<td>Returns: String</td>
<td>This RPC receives a string that is sent right back to the client. It exists for support of the EGcho Broker demonstration program.</td>
</tr>
<tr class="even">
<td><p>XWB EXAMPLE BIG TEXT</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>BIGTXT^XWBEXMPL</td>
<td>ARRAY: Array of text to be evaluated</td>
<td><p>Returns: A string containing a character and line count in the format:</p>
<p>char^lines</p></td>
<td>This RPC receives an array containing text data and returns a count of characters and lines. It exists for support of the RPC Broker Example program.</td>
</tr>
<tr class="odd">
<td><p>XWB EXAMPLE ECHO STRING</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>ECHOSTR^XWBEXMPL</td>
<td>INP: A string of up to <strong>255</strong> characters.</td>
<td>Returns: A copy of the input string.</td>
<td>This RPC receives a string that is sent right back to the client. It exists for support of the RPC Broker Example program.</td>
</tr>
<tr class="even">
<td><p>XWB EXAMPLE GET LIST</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>GETLIST^XWBEXMPL</td>
<td><ul>
<li><p>ITEMS: This parameter can be only one of two values:</p></li>
</ul>
<ul>
<li><p><strong>LINES—</strong>RPC returns a number of lines.</p></li>
<li><p><strong>KILOBYTES—</strong>RPC returns a number of kilobytes of data.</p></li>
</ul>
<ul>
<li><p>QUANTITY: Either a number of lines or a number of kilobytes to send back.</p></li>
</ul></td>
<td>Returns: An array of meaningless data.</td>
<td>This RPC brings back a list of elements to the client. The user can request either a number of lines or a number of Kilobytes of data to be returned. It exists for support of the RPC Broker Example program.</td>
</tr>
<tr class="odd">
<td><p>XWB EXAMPLE GLOBAL SORT</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>GSORT^XWBEXMPL</td>
<td><ul>
<li><p>DIRCTN: Direction to sort in <strong>HI</strong> or <strong>LO</strong>.</p></li>
<li><p>ROOT: Array of numbers to sort.</p></li>
</ul></td>
<td>Returns: An array of sorted numbers.</td>
<td>This RPC uses the global call to send down a <em>big</em> list of numbers to sort. It saves the data into a temp global. It exists for support of the RPC Broker Example program.</td>
</tr>
<tr class="even">
<td><p>XWB EXAMPLE SORT NUMBERS</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>SORTNUM^XWBEXMPL</td>
<td><ul>
<li><p>DIRCTN: Direction to sort in <strong>HI</strong> or <strong>LO</strong>.</p></li>
<li><p>ARRAY: Array of numbers to sort.</p></li>
</ul></td>
<td>Returns: An array of sorted numbers.</td>
<td>This RPC sorts an array of numbers. It exists for support of the RPC Broker Example program.</td>
</tr>
<tr class="odd">
<td><p>XWB EXAMPLE WPTEXT</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>WPTEXT^XWBEXMPL</td>
<td>None.</td>
<td>Returns: A word processing array.</td>
<td>This RPC uses a VA FileMan DBS call to retrieve the file description for the REMOTE PROCEDURE (#8994) file. It exists for support of the RPC Broker Example program.</td>
</tr>
<tr class="even">
<td><p>XWB GET BROKER INFO</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>BRKRINFO^XWBLIB</td>
<td>None.</td>
<td>Returns: A <strong>0</strong>-based array. Currently returns a single value containing the length of the handler read timeout.</td>
<td>Returns info regarding setup and parameters of the Broker.</td>
</tr>
<tr class="odd">
<td><p>XWB GET VARIABLE VALUE</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>VARVAL^XWBLIB</td>
<td>VARIABLE: Name of M environment variable whose value is to be returned.</td>
<td>Returns: The value of the input variable.</td>
<td>This RPC accepts the name of a variable that is evaluated, and its value returned to the server. For example, this RPC can be called with a parameter variable like <strong>DUZ</strong>, which is returned as <strong>123456</strong>. It should <em>not</em> be used to return the value of anything other than a variable. For example, the RPC should <em>not</em> attempt to return the value of a global or function call, as these are unsupported uses of the RPC and are <em>not</em> guaranteed to work consistently.</td>
</tr>
<tr class="even">
<td><p>XWB IM HERE</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>IMHERE^XWBLIB</td>
<td>None.</td>
<td>Returns: An integer value of <strong>1</strong>. This value is not used by the client.</td>
<td>Returns a simple value to the client. Used to establish continued existence of the client to the server: resets the server <strong>READ</strong> timeout.</td>
</tr>
<tr class="odd">
<td><p>XWB IS RPC AVAILABLE</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>CKRPC^XWBLIB</td>
<td><ul>
<li><p>RPC: Name of the RPC to be tested.</p></li>
<li><p>RUN CONTEXT: Specific context in which RPC will run. Possible values are:</p></li>
</ul>
<ul>
<li><p><strong>L—</strong>Run Locally (on the server the user is logged on to).</p></li>
<li><p><strong>R—</strong>Run Remotely (on a server the user is <em>not</em> logged on to).</p></li>
</ul>
<p>If this parameter is <em>not</em> sent, RPC is checked for both local and remote. The check is done against the value in the INACTIVE field in the REMOTE PROCEDURE (#8994) file. See that field’s description for more details.</p>
<ul>
<li><p>VERSION NUMBER: Minimum version number of the RPC. This parameter is only used if the RUN CONTEXT parameter = “<strong>R</strong>”. If a numeric value is in this parameter, the value <em>must</em> be less than or equal to the value in the VERSION field of the REMOTE PROCEDURE (#8994) file for the RPC to be marked available. <strong>NOTE:</strong> If the VERSION field is <strong>NULL</strong>, the check will fail for any numeric value in this parameter.</p></li>
</ul></td>
<td><p>Returns: A Boolean value:</p>
<ul>
<li><p><strong>1—</strong>RPC available.</p></li>
<li><p><strong>0—</strong>RPC <em>not</em> available.</p></li>
</ul></td>
<td><p>This RPC checks if a specified RPC is installed, available in relevant context, and of proper version. Returns:</p>
<ul>
<li><p><strong>1—</strong>RPC available.</p></li>
<li><p><strong>0—</strong>RPC <em>not</em> available.</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>XWB REMOTE CLEAR</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>CLEAR^XWBDRPC</td>
<td>HANDLE: This is the HANDLE from the XWB REMOTE RPC.</td>
<td>Returns: The return value is always an array. The first node of the array is equal to <strong>1</strong>.</td>
<td>This RPC is used to CLEAR the data under a HANDLE in the <strong>^XTMP</strong> global.</td>
</tr>
<tr class="odd">
<td><p>XWB REMOTE GETDATA</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>RTNDATA^XWBDRPC</td>
<td>HANDLE: This is the HANDLE from the XWB REMOTE RPC call. It is used to link the call to the data.</td>
<td>Returns: The return value is the array of data. In the event of an error condition, the first node of the array is equal to a string with the syntax “<strong>-1^error text</strong>”.</td>
<td>This RPC returns an array with whatever data has been sent back from the remote site.</td>
</tr>
<tr class="even">
<td><p>XWB REMOTE RPC</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>EN1^XWB2HL7</td>
<td><ul>
<li><p>LOC: This is the INSTITUTION (#4) file station # to send the RPC to.</p></li>
<li><p>RRPC: This is the name of the remote RPC to be run.</p></li>
<li><p>IP1: This is the first input parameter to the remote RPC.</p></li>
<li><p>IP2: This is the second input parameter to the remote RPC.</p></li>
</ul></td>
<td>Returns: The return value is always an array. The first node of the array is equal to a string that serves as a HANDLE. This is used to check the status of an RPC request and to retrieve the results of the RPC. In the case of an error condition, the first node of the array is equal to a string with the syntax “<strong>-1^error text</strong>”.</td>
<td>This is the RPC that is called to request that an application RPC be run on a remote system. The data is passed by HL7 to the remote system as is the return value. This RPC returns a HANDLE that can be used to check if the data has been sent back from the remote system. The HANDLE can be used in another RPC to check the status of the RPC.</td>
</tr>
<tr class="odd">
<td><p>XWB REMOTE STATUS CHECK</p>
<p><strong>Availability:</strong></p>
<p><strong>SUBSCRIPTION</strong></p></td>
<td>RPCCHK^XWB2HL7</td>
<td>HANDLE: This is the HANDLE used to check the status of the remote RPC.</td>
<td><p>Returns: The return value is always an array. The first node of the array is equal to one of the following values:</p>
<ul>
<li><p><strong>“-1^Bad Handle”—</strong>Invalid HANDLE has been passed.</p></li>
<li><p><strong>“0^New”—</strong>Request has been sent.</p></li>
<li><p><strong>“0^Running”—</strong>HL7 indicates that the message is being processed.</p></li>
<li><p><strong>“1^Done”—</strong>RPC has completed, and the data has returned to the local server.</p></li>
</ul>
<p>The data is <em>not</em> returned by this RPC. Use the <strong>XWB REMOTE GETDATA</strong> RPC to retrieve the data. The second node of the array is the status from the HL7 package.</p></td>
<td>This RPC returns the status of a remote RPC.</td>
</tr>
<tr class="even">
<td><p>XWB RPC LIST</p>
<p><strong>Availability:</strong></p>
<p><strong>RESTRICTED</strong></p></td>
<td>APILIST^XWBFM</td>
<td>START: String value of first characters of a routine name (e.g., namespace)</td>
<td><p>Returns: An array of APIs from the REMOTE PROCEDURE (#8994) file in the format</p>
<p>“IEN [API^routine]”</p></td>
<td>Returns a list of remote procedures from the REMOTE PROCEDURE (#8994) file.</td>
</tr>
</tbody>
</table>

<span id="_Ref59089503" class="anchor"></span>Table : RPC Broker—File Security

![](xwb-1-1-73-technical-manual/037.png) <sup>\*</sup>NOTE: EGCHO RPCs were used with an obsolete tester from RPC Broker 1.0; however, they will be removed in a future patch.

# External Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following external interfaces to RPC Broker functionality are provided:

### RPC Broker Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 (fully patched) provides programmers with the capability to develop new VistA client/server software using the following RPC Broker Delphi components in the 32-bit environment (listed alphabetically):

- TCCOWRPCBroker
- TContextorControl
- TRPCBroker (original component)
- TXWBRichEdit
- TXWBSSOiToken

![](xwb-1-1-73-technical-manual/038.png) NOTE: These RPC Broker components wrap the functionality of the Broker resulting in a more modularized and orderly interface. Those components derived from the original TRPCBroker component, inherit the TRPCBroker properties and methods.

These RPC Broker components (with the exception of TXWBRichEdit) provide all functionality needed for client applications to communicate with VistA M servers via the RPC Broker. All of these components are compatible with Embarcadero Delphi XE8 and greater.

![](xwb-1-1-73-technical-manual/039.png) NOTE: As of RPC Broker Patch XWB\*1.1\*73, RPC Broker 1.1 supports Delphi Versions: 10.4, 10.3, 10.2, 10.1, 10.0, and XE8.

![](xwb-1-1-73-technical-manual/040.png) CAUTION: This statement defines the extent of support relative to use of Delphi. The Office of Information and Technology (OIT) only supports the Broker Development Kit (BDK) running in the currently offered version of Delphi and the immediately previous version of Delphi. This level of support became effective 06/12/2000.  
  
Sites may continue to use outdated versions of the RPC Broker Development Kit but do so with the understanding that support is not be available and that continued use of outdated versions do not afford features that can be essential to effective client/server operations in the VistA environment. An archive of old (no longer supported) Broker Development Kits will be maintained in the VA Intranet Broker Archive.

![](xwb-1-1-73-technical-manual/041.png) REF: For more information on the Broker components, see the *RPC Broker User Guide* and *RPC Broker Developer’s Guide*.

### RPC Broker Dynamic Link Library (DLL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker DLL (BAPI32.DLL) provides access to RPC Broker functionality for development environments other than Delphi.

![](xwb-1-1-73-technical-manual/042.png) REF: For more information on the RPC Broker DLL, see the *RPC Broker User Guide* and *RPC Broker Developer’s Guide*.

### Pascal Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following Pascal functions are provided by the TRPCBroker component:

- GetServerInfo function
- Splash Screen functions:
- SplashOpen
- SplashClose
- Piece function
- Translate function
- Encryption functions::
- Decrypt
- Encrypt

![](xwb-1-1-73-technical-manual/043.png) REF: For more information on these Pascal functions, see the *RPC Broker User Guide* and the *RPC Broker Developer’s Guide*.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Relationship to Other Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 was developed to aid the VistA development community and system administrators. It is considered to be part of the VistA infrastructure. Other infrastructure products include:

- Kernel
- Kernel Toolkit
- VA FileMan
- MailMan
- VistALink

The RPC Broker is used by all VistA client/server applications. The RPC Broker fully integrates with Kernel 8.0 and VA FileMan 22.2.

Remote Procedure Calls (RPCs) are also being used by other applications to provide the same functionality and security as the RPC Broker, and in some cases are being exposed as registered services on the Enterprise Services Bus (ESB). In this case, the REMOTE PROCEDURE (#8994) file *must* be present for those applications to function correctly.

### Relationship with Kernel and VA FileMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before installing the RPC Broker, the following software *must* be in place and fully patched:

- Kernel 8.0
- Kernel Toolkit 7.3
- VA FileMan 22.2 or higher

### Relationships with Operating Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the client side, it was decided that the 32-bit Microsoft<sup>®</sup> Windows environment would be the supported platform. Thus, the client portions of the RPC Broker are compatible with the following Microsoft<sup>®</sup> Windows operating systems:

- Windows Server 2012 R2
- Windows 10
- Windows 8.1
- Windows 7

On the server side, the RPC Broker supports the following ANSI M environments:

- InterSystems Caché for:
- Windows
- Linux
- OpenVMS
- Greystone Technology MUMPS (GT.M) on Linux

## DBA Approvals and Integration Control Registrations (ICRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Integration Control Registrations (ICR) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are not available to the general programming public.

### ICRs—Current List for RPC Broker as Custodian

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain a current list of ICRs to which the RPC Broker (XWB) software is a custodian, perform the following procedure:

1.  Sign on to the FORUM system.
10. Go to the DBA \[DBA\] menu.
11. Select the Integration Agreements Menu \[DBA IA ISC\] option.
12. Select the Custodial Package Menu \[DBA IA CUSTODIAL MENU\] option.
13. Choose the ACTIVE by Custodial Package \[DBA IA CUSTODIAL\] option.
14. When prompted for a package, enter XWB or RPC BROKER.
15. All current ICRs to which the RPC Broker software is custodian are listed.

### ICRs—Detailed Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain detailed information on a specific ICR:

1.  Sign on to the FORUM system.
16. Go to the DBA \[DBA\] menu.
17. Select the Integration Agreements Menu \[DBA IA ISC\] option.
18. Select the Inquire \[DBA IA INQUIRY\] option.
19. When prompted for “INTEGRATION REFERENCES,” enter the specific Integration Control Registration (ICR) number you would like to display.
20. The option then lists the full text of the ICR you requested.

### ICRs—Current List for RPC Broker as Subscriber

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To obtain the current list of ICRs, if any, to which the RPC Broker software is a subscriber, perform the following procedure:

1.  Sign on to the FORUM system.
21. Go to the DBA \[DBA\] menu.
22. Select the Integration Agreements Menu \[DBA IA ISC\] option.
23. Select the Subscriber Package Menu \[DBA IA SUBSCRIBER MENU\] option.
24. Choose the Print ACTIVE by Subscribing Package \[DBA IA SUBSCRIBER\] option.
25. When prompted with “START WITH SUBSCRIBING PACKAGE,” enter XWB or RPC BROKER (uppercase).
26. When prompted with “GO TO SUBSCRIBING PACKAGE,” enter XWB or RPC BROKER (uppercase).
27. All current ICRs to which the RPC Broker (XWB) software is a subscriber are listed.

# Internal Relationships

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No options in the RPC Broker product assume that the entry/exit logic of another option has already occurred.

# Global Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker does *not* create any global (software-wide) variables that have received Standards and Conventions Committee (SACC) exemptions.

# Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no special legal requirements involved in the use of RPC Broker 1.1.

![](xwb-1-1-73-technical-manual/044.png) REF: For more information on official policies, see the “[Disclaimers](#disclaimers)” section.

## Mail Groups, Bulletins, and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no mail groups exported or bulletins and alerts associated with RPC Broker 1.1.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker M server process:

- Allows connections from client applications.
- Authenticates client application connection as any normal logon requires.
- Allows client applications to use any remote procedure call (RPC) authorized to the application, if the application is authorized to the signed-on user.
- Exchanges data (typically) between clients and the RPC Broker server.
- Allows clients can be anywhere on VA’s TCP/IP network.
- Uses encryption when a user’s Access and Verify codes are sent from the client to the server.
- Provides an encryption API for developer to use in their own applications to encode and decode messages passed between client and server.

Security with the RPC Broker is a four-part process:

1.  Client workstations *must* send a valid connection request to the M Server.
28. Users *must* have valid Access and Verify codes.
29. Users *must* be valid users of a VistA client/server application.
30. Any remote procedure call *must* be registered and valid for the application being executed.

![](xwb-1-1-73-technical-manual/045.png) REF: For more information regarding Broker security, see Chapter 2, “Security,” in the *RPC Broker Systems Management Guide*.

### Remote Data Views

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker can be used to facilitate invocation of Remote Procedure Calls on a remote server. Applications can use either of the following RPCs to pass information between servers:

- XWB DIRECT RPC
- XWB REMOTE RPC

These RPC pass the following:

- Desired remote server.
- Desired remote RPC.
- Parameters for the remote RPC.

Communications between local and remote servers is as follows:

1.  RPC Broker on the local server passes the remote RPC name and parameters to the remote server using VistA HL7.
31. VistA HL7 sends any results from the remote server back to the local server.
32. RPC Broker on the local server passes the results back to the client application.

![](xwb-1-1-73-technical-manual/046.png) NOTE: The XWB DIRECT RPC and XWB REMOTE RPC are available only on a controlled subscription basis.

## Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No *non*-VA products are embedded in or required by RPC Broker 1.1, other than those provided by the underlying operating systems.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no electronic signatures used within RPC Broker 1.1.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* specific security keys exported with RPC Broker 1.1. However, to bypass security for development purposes, it is *recommended* that client/server application developers be assigned the XUPROGMODE security key.

All users assigned the XUPROGMODE security key can do the following:

- Run any VistA client/server application, regardless of whether it is in their menu tree or not.
- Access any RPC without regard to the application context.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker establishes the file security as shown in <u>Table 11</u>:

| Number | Name                       | DD    | RD    | WR    | DEL   | LAYGO | AUDIT |
|--------|----------------------------|-------|-------|-------|-------|-------|-------|
| 8994   | REMOTE PROCEDURE           | @ | @ | @ | @ | @ | @ |
| 8994.1 | RPC BROKER SITE PARAMETERS | @ | @ | @ | @ | @ | @ |
| 8994.5 | REMOTE APPLICATION         | @ | @ | @ | @ | @ | @ |

<span id="_Ref467590751" class="anchor"></span>Table : Glossary of Terms and Acronyms

![](xwb-1-1-73-technical-manual/047.png) REF: For more information on these files, see the “<u>VistA M Server Files</u>” section.

## Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Modification of any part of the RPC Broker software is *strongly* discouraged.
- Distribution of the RPC Broker software is unrestricted.
- The VHA IT Architecture Statement of Direction for FY98 prescribes *“Use of Kernel Broker for client-server communication...”*
- As per the Software Engineering Process Group/Software Quality Assurance (SEPG/SQA) Standard Operating Procedure (SOP) 192-039—Interface Control Registration and Approval (effective 01/29/01), application programmers *must* not alter any Health*<u>e</u>*Vet VistA Class I software code.

![](xwb-1-1-73-technical-manual/048.png) REF: For more information on official policies, see the “[Disclaimers](#disclaimers)” section.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Test the Broker Using the RPC Broker Diagnostic Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker Patch XWB\*1.1\*47 included a diagnostic tool for the client workstation (<u>Figure 2</u>). This tool can be used to verify and test the Broker client/server connection and signon process. This program (i.e., rpctest.exe) also displays specific information about the client workstation that can be useful to system administrators when trying to determine and/or correct any problems with or to test the Broker.

![](xwb-1-1-73-technical-manual/049.png) NOTE: This utility has *not ye*t been updated to support IPv4/IPv6 dual-stack environment testing and has not been reviewed for Section 508 conformance.

It displays the following information:

- Default workstation information that includes the Name and IP Address.
- Local connection information that includes the Name, Client IP, Current Socket, and Broker State.
- VistA user information that includes the Name and Last Signon Date/Time.
- Remote connection information that includes the Server, Port, IP Address, Operating System Version information, and Job ID.
- A color-coded Link State indicator that shows the status of your connection:
- Red = no link/connection.
- Yellow = attempting link/connection.
- Green = successful link/connection.

When you run the RPC Broker Connection Diagnostic Program (i.e., rpctest.exe), the dialogue in <u>Figure 2</u> is displayed:

<span id="_Ref362526803" class="anchor"></span>Figure : RPC Broker Connection Diagnostic Application

![](xwb-1-1-73-technical-manual/050.png)

You should verify that the connection from the client workstation to the server is functioning correctly. For example:

- Try logging on to the server by choosing a server/port combination and pressing Log On; you will be presented with the “VistA Sign-on” dialogue. The Link State indicator will change from red to yellow to green as you progress through the connection process.
- Test various connections by changing the server and port information under the “Remote Connection Info” block. To verify the connection process is working properly, try logging on to known servers and ports with Listeners running.

You can also use this tool to resolve a server address without having to log on to the server. Type in a server name in the “Server” box located in the “Remote Connection Info” section of the dialogue and press the Enter key. If the server can be found, the IP address will be displayed in the “IP Addr” box in that same section.

If you encounter an error while testing the Broker, make sure you check the following:

- Is the Broker Listener running on the specified port? If not, start the Broker Listener on the specified port.

![](xwb-1-1-73-technical-manual/051.png) REF: For more information on starting the Broker Listener, see the “Broker Listeners and Ports” section in the *RPC Broker Systems Management Guide*.

- Have you installed all current Kernel, Kernel Toolkit, and VA FileMan patches? If not, you *must* install all required patches (see the *RPC Broker Deployment, Installation, Back-Out, and Rollback Guide \[DIBRG\]*).
- Did you change the IP address for BROKERSERVER in the HOSTS file in this session? If the IP address and server name are not resolvable, you need to correct the entry.

![](xwb-1-1-73-technical-manual/052.png) NOTE: Your site can use the HOSTS file or DNS to resolve IP addresses and server names. If the HOSTS file is not supported in your LAN, then you will need to work with the DNS database and see if the value returned by the DNS query really identifies the machine where the listener is running.

- Is the IP address resolvable for the BROKERSERVER listed under the TCP/IP Server? If not, edit the HOSTS file in your Microsoft<sup>®</sup> Windows directory and correct the IP address for the BROKERSERVER or resolve the IP address with DNS.
- Does the TCP/IP address (used in the HOSTS file) correspond to the IP address that is owned by the node used to start up the Broker Listener? If you have several nodes that can service your Test/Production account, you *must* make sure that the one used to start up the Listener is the one being referenced in the HOSTS file.

## Verify and Test the Network Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To detect and avoid network problems, do the following:

1.  First, make sure you actually have TCP/IP running correctly on your workstation.

At the DOS/Command prompt type PING \###.###.###.### to the server host to which you are trying to connect (where \###.###.###.### equals the IP address of the server). For example:

C:\\PING \<REDACTED\>

Alternatively, you can PING the same server name you are trying to connect to or resolve (e.g., BROKERSERVER). For example:

C:\\PING BROKERSERVER

![](xwb-1-1-73-technical-manual/053.png) NOTE: “PING” is a way to test connectivity. PING sends an Internet Control Message Protocol (ICMP) packet to the server in question and requests a response. It verifies that the server is running, and the network is properly configured:

- If the host is unreachable, there is a network problem and you should consult with your network administrator.
- If you get a timeout, it may be your network configuration on the client workstation, proceed to [Step 2](#verify_test_network_onnection_step_02).
- If the server is reachable, proceed to [Step 4](#verify_test_network_onnection_step_04).
33. <span id="verify_test_network_onnection_step_02" class="anchor"></span>Check the properties of the WINSOCK.DLL on the client workstation and make sure it’s the correct version. Install the latest Service Pack.
34. Make sure that the files on the client are in the correct directories.
35. <span id="verify_test_network_onnection_step_04" class="anchor"></span>Make sure that all of the client workstation TCP/IP settings are correct in the network properties. Typos, etc. can be a real problem, as can gateways, DNS servers, etc. Try removing items in your WINS configuration/DNS configuration, etc.

![](xwb-1-1-73-technical-manual/054.png) REF: For more information on telecommunications support, please visit the Telecommunications Support Office Home Page on the VA Intranet.

## RPC Broker FAQs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For examples of general or development-specific frequently asked questions (FAQs) about the RPC Broker, see VA Intranet website.

  
<span id="glossary" class="anchor"></span>

Glossary

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CLIENT</td>
<td>A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</td>
</tr>
<tr class="even">
<td>COMPONENT</td>
<td>An object-oriented term used to describe the building blocks of GUI applications. A software object that contains data and code. A component may or may not be visible. These components interact with other components on a form to create the GUI user application interface.</td>
</tr>
<tr class="odd">
<td>DHCP</td>
<td><strong>D</strong>ynamic <strong>H</strong>ost <strong>C</strong>onfiguration <strong>P</strong>rotocol.</td>
</tr>
<tr class="even">
<td>DLL</td>
<td><p><strong>D</strong>ynamic <strong>L</strong>ink <strong>L</strong>ibrary. A DLL allows executable routines to be stored separately as files with a DLL extension. These routines are only loaded when a program calls for them. DLLs provide several advantages:</p>
<ul>
<li><p>Help save on computer memory, since memory is only consumed when a DLL is loaded. They also save disk space. With static libraries, your application absorbs all the library code into your application, so the size of your application is greater. Other applications using the same library will also carry this code around. With the DLL, you do not carry the code itself; you have a pointer to the common library. All applications using it will then share one image.</p></li>
<li><p>Ease maintenance tasks. Because the DLL is a separate file, any modifications made to the DLL will not affect the operation of the calling program or any other DLL.</p></li>
<li><p>Help avoid redundant routines. They provide generic functions that can be used by a variety of programs.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>GUI</td>
<td><strong>G</strong>raphical <strong>U</strong>ser Interface. A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.</td>
</tr>
<tr class="even">
<td>ICON</td>
<td>A picture or symbol that graphically represents an object or a concept.</td>
</tr>
<tr class="odd">
<td>REMOTE PROCEDURE CALL</td>
<td>A remote procedure call (RPC) is essentially M code that may take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="even">
<td>SERVER</td>
<td>The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION (#19) file. An automated mail protocol that is activated by sending a message to a server at another location with the “<strong>S.server</strong>” syntax. A server’s activity is specified in the OPTION (#19) file and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td>USER ACCESS</td>
<td><p>This term is used to refer to a limited level of access to a computer system that is sufficient for using/operating software, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any of VistA’s options can be locked with a security key (e.g., XUPROGMODE, which means that invoking that option requires programmer access).</p>
<p>The user’s access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="even">
<td>USER INTERFACE</td>
<td>The way the software is presented to the user, such as Graphical User Interfaces that display option prompts, help messages, and menu choices. A standard user interface can be achieved by using Embarcadero’s Delphi Graphical User Interface to display the various menu option choices, commands, etc.</td>
</tr>
<tr class="odd">
<td>WINDOW</td>
<td>An object on the screen (dialogue) that presents information such as a document or message.</td>
</tr>
</tbody>
</table>

![](xwb-1-1-73-technical-manual/055.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet website.

  
<span id="_Toc82600038" class="anchor"></span>Index

^

^XWB Global, 8

Archiving, 15

Purging, 15

^XWB(8994, Global, 4

^XWB(8994.1, Global, 4

^XWB(8994.5, Global, 5

A

Acronyms

Intranet Website, 43

ACTIVE by Custodial Package Option, 34

Alerts, 35

Applications

rpctest.exe, 12

Applications

Diagnostic, 12

rpctest.exe, 12

Archiving, 15

Assumptions, xvi

B

Broker

FAQs, 41

BROKERSERVER, 40

C

Callable Entry Points, 15

CALLBACKTYPE (#1) Multiple Field, 5

Callout Boxes, xiv

Clear XWB Log Files Option, 11, 13

Client Files, 6

Commonly Used Terms, xv

Components

RPC Broker, 31

TCCOWRPCBroker, 31

TContextorControl, 31

TRPCBroker, 31

TXWBRichEdit, 31

TXWBSSOiToken, 31

Connections, 36

Diagnostics, 39

Contents, ix

Custodial Package Menu, 34

D

Data Dictionary

Data Dictionary Utilities Menu, xvi

Listings, xvi

DBA Approvals, 34

DBA Approvals and ICRs, 34

DBA IA CUSTODIAL MENU, 34

DBA IA CUSTODIAL Option, 34

DBA IA INQUIRY Option, 34

DBA IA ISC Menu, 34, 35

DBA IA SUBSCRIBER MENU, 35

DBA IA SUBSCRIBER Option, 35

DBA Menu, 34, 35

Debug Parameter Edit Option, 11, 13

DECRYP^XUSRB1, 32

Decryption

Function, 32

Demographics, 5

DI DDU Menu, xvi

Diagnostic application, 12

Diagnostics

Connection, 39

DILIST Option, xvi

Disclaimers, xiii

Software, xii

DLL, 2, 15, 32

WINSOCK.DLL, 41

DNS, 40

Documentation

Revisions, ii

Symbols, xiii

Documentation Conventions, xiii

Documentation Navigation, xv

Dynamic Link Library, 32

E

Electronic Signatures, 37

ENCRYP^XUSRB1, 32

Encryption, 36

Function, 32

Functions, 32

End-User Workstation Files, 6

Entry Points

Callable, 15

Environment, 33

Exported

Options, 11

External

Interfaces, 31

Relations, 33

Relationships, 31

F

FAQs, 41

Features

Server, 12

Fields

CALLBACKTYPE (#1) Multiple, 5

RPC (#.01), 4

RPC (#19.05), 4

Figures, xi

Files, 4

Client, 6

End-User Workstations, 6

HOSTS, 40

NEW PERSON (#200), 5

OPTION (#19), 4, 12

Programmer Workstations, 7

REMOTE APPLICATION (#8994.5), 5, 37

REMOTE PROCEDURE (#8994), 1, 4, 18, 33

Archiving, 15

Purging, 15

Security, 16, 37

REMOVE APPLICATION (#8994.5), 8

RPC BROKER SITE PARAMETERS (#8994.1), 4, 13

Archiving, 15

Purging, 15

Security, 37

Security, 37

Frequently Asked Questions, 41

Functions

Decryption, 32

Encryption, 32

Pascal, 32

Piece, 32

Translate, 32

G

GetServerInfo Method, 32

Global Variables, 35

Globals, 4

^XWB, 8

Archiving, 15

Purging, 15

^XWB(8994,, 4

^XWB(8994.1,, 4

^XWB(8994.5,, 5

Journaling, 8

Protection, 8

Translation, 7

Glossary, 42

Intranet Website, 43

H

Help

At Prompts, xvi

Online, xvi

Question Marks, xvi

History

Revisions, ii

Home Pages

Acronyms Intranet Website, 43

Adobe Website, xvii

Glossary Intranet Website, 43

RPC Broker Website, xvii

VA Software Document Library (VDL) Website, xvii

RPC Broker, xvii

HOSTS File, 40

How to

Obtain Technical Information Online, xvi

Use this Manual, xii

I

ICRs, 34

Implementation, 2

Inquire Option, 34

Integration Agreements Menu Option, 34, 35

Integration Control Registration (ICR), 34

Current List for RPC Broker

Custodian, 34

Subscriber, 35

Detailed Information, 34

Intended Audience, xii

Interfaces, 37

External, 31

Internal

Relationships, 35

Introduction, 1

J

Journaling, 8

K

Keys

Security, 37

XUPROGMODE, 12, 37

L

LAN, 40, 42

List File Attributes Option, xvi

M

Mail Groups, 35

Maintenance, 2

Management

Security, 35

Menu for System Managers, 12

Menus

Custodial Package Menu, 34

Data Dictionary Utilities, xvi

DBA, 34, 35

DBA IA CUSTODIAL MENU, 34

DBA IA ISC, 34, 35

DBA IA SUBSCRIBER MENU, 35

DBA Option, 34, 35

DI DDU, xvi

Integration Agreements Menu, 34, 35

RPC Broker Management Menu, 11, 12

Subscriber Package Menu, 35

System Command Options, 12

XUCOMMAND, 12

XWB MENU, 11, 12

Methods

GetServerInfo, 32

Splash Screen, 32

SplashClose, 32

SplashOpen, 32

N

Network Connection, 40

NEW PERSON (#200) File, 5

O

Obtaining

Data Dictionary Listings, xvi

Official Policies, 38

Online

Documentation, xvi

Technical Information, How to Obtain, xvi

OPTION (#19) File, 4, 12

Options

ACTIVE by Custodial Package, 34

Clear XWB Log Files, 11, 13

Custodial Package Menu, 34

Data Dictionary Utilities, xvi

DBA, 34, 35

DBA IA CUSTODIAL, 34

DBA IA CUSTODIAL MENU, 34

DBA IA INQUIRY, 34

DBA IA ISC, 34, 35

DBA IA SUBSCRIBER MENU, 35

DBA IA SUBSCRIBER Option, 35

DBA Option, 34, 35

Debug Parameter Edit, 11, 13

DI DDU, xvi

DILIST, xvi

Exported, 11

Inquire, 34

Integration Agreements Menu, 34, 35

List File Attributes, xvi

Print ACTIVE by Subscribing Package, 35

RPC, 11, 12

RPC BROKER DEMO/TEST, 11, 14

RPC Broker Management Menu, 11, 12

RPC BROKER PROGRAMMING EXAMPLE, 11, 12

RPC Listener Edit, 11, 13

Start All RPC Broker Listeners, 11, 13

Start M2M RPC Broker Cache Listener, 11, 14

Stop All RPC Broker Listeners, 11, 13

Subscriber Package Menu, 35

System Command Options Menu, 12

View XWB Log, 11, 13

XUCOMMAND, 12

XWB BROKER EXAMPLE, 11, 12

XWB DEBUG EDIT, 11, 13

XWB EGCHO, 11, 14

XWB LISTENER EDIT, 11, 13

XWB LISTENER STARTER, 11, 13

XWB LISTENER STOP ALL, 11, 13

XWB LOG CLEAR, 11, 13

XWB LOG VIEW, 11, 13

XWB M2M CACHE LISTENER, 11, 14

XWB MENU, 11, 12

XWB RPC TEST, 11, 12

Orientation, xii

Overview

Product, 1

P

Parameters, 3

Pascal Functions, 32

Patches

Revisions, viii

Performance, 3

Piece Function, 32

PING, 40

Print ACTIVE by Subscribing Package Option, 35

Product

Overview, 1

Security, 35

Product Support (PS)

Anonymous Directories, xvii

Programmer Workstation Files, 7

Programs

rpctest.exe, 38, 39

Protection, 8

PS

Anonymous Directories, xvii

Purging, 15

Q

Question Mark Help, xvi

R

Relations

External, 33

Relationships

External, 31

Internal, 35

To Other Software, 33

With Kernel and VA FileMan, 33

With Operating Systems, 33

REMOTE APPLICATION (#8994.5) File, 5, 37

Remote Data Views, 36

REMOTE PROCEDURE (#8994) File, 1, 4, 18, 33

Archiving, 15

Purging, 15

Security, 16, 37

Remote Systems, 36

REMOVE APPLICATION (#8994.5) File, 8

Revision History, ii

Documentation, ii

Patches, viii

Routines, 8

XWB2HL7, 8

XWB2HL7A, 8

XWB2HL7B, 8

XWB2HL7C, 8

XWB45PO, 8

XWBBRK, 9

XWBBRK2, 9

XWBCAGNT, 9

XWBDLOG, 9

XWBDRPC, 9

XWBEXMPL, 9

XWBFM, 9

XWBLIB, 9

XWBM2MC, 9

XWBM2MEZ, 9

XWBM2MS, 9

XWBM2MT, 9

XWBPRS, 9

XWBRL, 9

XWBRM, 9

XWBRMX, 9

XWBRPC, 9

XWBRPCC, 9

XWBRW, 9

XWBSEC, 9

XWBTCP, 10

XWBTCPC, 10

XWBTCPL, 10

XWBTCPM, 10

XWBTCPM1, 10

XWBTCPM2, 10

XWBTCPMT, 10

XWBUTL, 10

XWBVL, 10

XWBVLC, 10

XWBVLL, 10

XWBZ1, 10

RPC (#.01) Field, 4

RPC (#19.05) Field, 4

RPC Broker

Components, 31

Diagnostic Program

How to test the Broker, 38

DLL, 32

FAQs, 41

Website, xvii

RPC BROKER DEMO/TEST Option, 11, 14

RPC Broker Management Menu, 11, 12

RPC BROKER PROGRAMMING EXAMPLE Option, 11, 12

RPC BROKER SITE PARAMETERS (#8994.1) File, 4, 13

Archiving, 15

Purging, 15

Security, 37

RPC Listener Edit Option, 11, 13

RPC Option, 11, 12

RPCs, 18

XWB ARE RPCS AVAILABLE, 18

XWB CREATE CONTEXT, 20

XWB DEFERRED CLEAR, 20

XWB DEFERRED CLEARALL, 21

XWB DEFERRED GETDATA, 21

XWB DEFERRED RPC, 21

XWB DEFERRED STATUS, 22

XWB DIRECT, 36

XWB DIRECT RPC, 23

XWB EGCHO BIG LIST, 23

XWB EGCHO LIST, 23

XWB EGCHO MEMO, 23

XWB EGCHO SORT LIST, 24

XWB EGCHO STRING, 24

XWB EXAMPLE BIG TEXT, 24

XWB EXAMPLE ECHO STRING, 24

XWB EXAMPLE GET LIST, 24

XWB EXAMPLE GLOBAL SORT, 25

XWB EXAMPLE SORT NUMBERS, 25

XWB EXAMPLE WPTEXT, 25

XWB GET BROKER INFO, 26

XWB GET VARIABLE VALUE, 26

XWB IM HERE, 26

XWB IS RPC AVAILABLE, 27

XWB REMOTE, 36

XWB REMOTE CLEAR, 28

XWB REMOTE GETDATA, 28

XWB REMOTE RPC, 28

XWB REMOTE STATUS CHECK, 29

XWB RPC LIST, 30

rpctest.exe, 38, 39

rpctest.exe Application, 12

S

Scalability, 3

Security, 35

Connections, 36

Electronic Signatures, 37

Files, 37

Interfaces, 37

Keys, 37

XUPROGMODE, 12, 37

Management, 35

Remote Data Views, 36

Remote Systems, 36

Server

Features, 12

Site Parameters, 3

Software Disclaimer, xii

Splash Screen Method, 32

SplashClose Method, 32

SplashOpen Method, 32

Start All RPC Broker Listeners Option, 11, 13

Start M2M RPC Broker Cache Listener Option, 11, 14

Stop All RPC Broker Listeners Option, 11, 13

Subscriber Package Menu Option, 35

Support

Anonymous Directories, xvii

Symbols

Found in the Documentation, xiii

System Command Options Menu, 12

T

Table of Contents, ix

Tables, xi

TCCOWRPCBroker Component, 31

TContextorControl Component, 31

TCP/IP, 40, 41

Test the Broker Using the RPC Broker Diagnostic Program, 38

Translate Function, 32

Translation, 7

Troubleshooting, 38

Network Connection, 40

RPC Broker Diagnostic Program, 38

TRPCBroker Component, 31

TXWBRichEdit Component, 31

TXWBSSOiToken Component, 31

U

URLs

Acronyms Intranet Website, 43

Adobe Website, xvii

Glossary Intranet Website, 43

RPC Broker Website, xvii

VA Software Document Library (VDL) Website, xvii

RPC Broker, xvii

V

VA Software Document Library (VDL)

Website, xvii

RPC Broker, xvii

Variables

Global, 35

Verify and Test the Network Connection, 40

View XWB Log Option, 11, 13

VistA M Server Files, 4

W

Websites

Acronyms Intranet Website, 43

Adobe Website, xvii

Glossary Intranet Website, 43

RPC Broker, xvii

VA Software Document Library (VDL) Website, xvii

RPC Broker, xvii

WINSOCK.DLL, 41

X

XUCOMMAND Menu, 12

XUPROGMODE Security Key, 12, 37

XWB ARE RPCS AVAILABLE RPC, 18

XWB BROKER EXAMPLE Option, 11, 12

XWB CREATE CONTEXT RPC, 20

XWB DEBUG EDIT Option, 11, 13

XWB DEFERRED CLEAR RPC, 20

XWB DEFERRED CLEARALL RPC, 21

XWB DEFERRED GETDATA RPC, 21

XWB DEFERRED RPC, 21

XWB DEFERRED STATUS RPC, 22

XWB DIRECT RPC, 23, 36

XWB EGCHO BIG LIST RPC, 23

XWB EGCHO LIST RPC, 23

XWB EGCHO MEMO RPC, 23

XWB EGCHO Option, 11, 14

XWB EGCHO SORT LIST RPC, 24

XWB EGCHO STRING RPC, 24

XWB EXAMPLE BIG TEXT RPC, 24

XWB EXAMPLE ECHO STRING RPC, 24

XWB EXAMPLE GET LIST RPC, 24

XWB EXAMPLE GLOBAL SORT RPC, 25

XWB EXAMPLE SORT NUMBERS RPC, 25

XWB EXAMPLE WPTEXT RPC, 25

XWB GET BROKER INFO RPC, 26

XWB GET VARIABLE VALUE RPC, 26

XWB IM HERE RPC, 26

XWB IS RPC AVAILABLE RPC, 27

XWB LISTENER EDIT Option, 11, 13

XWB LISTENER STARTER Option, 11, 13

XWB LISTENER STOP ALL Option, 11, 13

XWB LOG CLEAR Option, 11, 13

XWB LOG VIEW Option, 11, 13

XWB M2M CACHE LISTENER Option, 11, 14

XWB MENU, 11, 12

XWB REMOTE CLEAR RPC, 28

XWB REMOTE GETDATA RPC, 28

XWB REMOTE RPC, 28, 36

XWB REMOTE STATUS CHECK RPC, 29

XWB RPC LIST RPC, 30

XWB RPC TEST Option, 11, 12

XWB2HL7 Routine, 8

XWB2HL7A Routine, 8

XWB2HL7B Routine, 8

XWB2HL7C Routine, 8

XWB45PO Routine, 8

XWBBRK Routine, 9

XWBBRK2 Routine, 9

XWBCAGNT Routine, 9

XWBDLOG Routine, 9

XWBDRPC Routine, 9

XWBEXMPL Routine, 9

XWBFM Routine, 9

XWBLIB Routine, 9

XWBM2MC Routine, 9

XWBM2MEZ Routine, 9

XWBM2MS Routine, 9

XWBM2MT Routine, 9

XWBPRS Routine, 9

XWBRL Routine, 9

XWBRM Routine, 9

XWBRMX Routine, 9

XWBRPC Routine, 9

XWBRPCC Routine, 9

XWBRW Routine, 9

XWBSEC Routine, 9

XWBTCP Routine, 10

XWBTCPC Routine, 10

XWBTCPL Routine, 10

XWBTCPM Routine, 10

XWBTCPM1 Routine, 10

XWBTCPM2 Routine, 10

XWBTCPMT Routine, 10

XWBUTL Routine, 10

XWBVL Routine, 10

XWBVLC Routine, 10

XWBVLL Routine, 10

XWBZ1 Routine, 10