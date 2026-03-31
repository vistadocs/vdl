---
title: XWB*1.1*73 User Guide
doc_type: UG
doc_label: User Guide
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
menu_options: 2
description: 
audience: 
keywords: 
  - strong
  - broker
  - table
  - server
  - application
  - vista
  - contents
  - class
  - remote
  - component
page_count: 0
word_count: 19198
section_count: 32
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: September 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_ug_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_ug_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=23"
---

---
title: |
  RPC Broker 1.1

  User Guide (REDACTED)
---

![](xwb-1-1-73-user-guide/001.png)

September 2021

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

<span id="_Toc97001457" class="anchor"></span>Revision History

Document Revisions

<table>
<caption><p><span id="_Ref449345480" class="anchor"></span>Table : Documentation Symbol Descriptions</p></caption>
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
<li><p>Supports Delphi XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4: Sections <u>1.1.1</u> and <u>7.1</u>.</p></li>
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
<li><p>Supports Delphi XE8, 10.0, 10.1, 10.2, 10.3, and Delphi/RAD Studio v10.4: Sections <u>1.1.1</u> and <u>7.1</u>.</p></li>
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
<td>05/06/2020</td>
<td>8.0</td>
<td><p>Tech Edits based on the Broker Development Kit (BDK) release with RPC Broker Patch XWB*1.1*71.</p>
<ul>
<li><p>Updated Section <u>1.1.1</u> functionality added with XWB*1.1*71</p></li>
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
<td>05/18/2017</td>
<td>7.2</td>
<td><p>Updated the <strong>CALLBACKTYPE</strong> entry in “<u>Table 10: Fields in the REMOTE APPLICATION (#8994.5) File</u>” to include the “<strong>S—</strong>Station-number callback” value.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*65 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>05/17/2017</td>
<td>7.1</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Updated/Added “Caution” note for the <strong>Reference PType</strong> input parameter in <u>Table 6</u>, Step 1 in Section <u>3.6</u>, and Section <u>4.3</u>.</p></li>
<li><p>Reformatted all references to file and field name numbers throughout.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*65 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>01/24/2017</td>
<td>7.0</td>
<td><p>Tech Edits based on release of RPC Broker Patch XWB*1.1*65:</p>
<ul>
<li><p>Reformatted document to follow current documentation standards and style formatting requirements.</p>
<p>Inserted Section <u>5</u>, “<u>Broker Security Enhancement (BSE)</u>;” content taken from Chapters 1-2 in the Broker Security Enhancement (BSE) Patch XWB*1.1*45 Supplement.</p></li>
<li><p>Added content and references to the <strong>TXWBSSOi</strong> component in Sections <u>1.1</u> and <u>2.4</u>.</p></li>
<li><p>Updated Section <u>1.1.1</u> for 2-factor authentication feature and current level of Delphi version support.</p></li>
<li><p>Updated Section <u>2.1.4</u>.</p></li>
<li><p>Added Caution note to the <strong>Reference PType</strong> in <u>Table 6</u>.</p></li>
<li><p>Updated <u>Figure 6</u>.</p></li>
<li><p>Updated registry information in Section <u>4.1.1</u>.</p></li>
<li><p>Added <u>Figure 8</u>.</p></li>
<li><p>Corrected Section <u>4.1.2</u>.</p></li>
<li><p>Updated debug instructions in Section <u>6.1</u>.</p></li>
<li><p>Updated instructions in Section <u>6.2.1</u>.</p></li>
<li><p>Updated Section <u>7.1</u> and 7.1.1 for currently supported Delphi versions.</p></li>
<li><p>Updated Section <u>7.1.2</u> and <u>7.1.3</u> for .bpl file references.</p></li>
<li><p>Changed references from “Borland Delphi” to “Embarcadero Delphi” throughout.</p></li>
<li><p>Added new <a href="#glossary">glossary</a> terms: SAML and XML.</p></li>
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
<li><p>Updated the “<a href="#Orientation">Orientation</a>” section.</p></li>
<li><p>Updated Section <u>1.1.1</u>.</p></li>
<li><p>Updated <u>Table 3</u> for <strong>TRPCBroker</strong> component key properties.</p></li>
<li><p>Updated Section <u>2.1.4</u>.</p></li>
<li><p>Updated <u>Figure 1</u>.</p></li>
<li><p>Deleted Sections 2.3, "<strong>TSharedBroker</strong> Component" and 2.4, "<strong>TSharedRPCBroker</strong> Component."</p></li>
<li><p>Updated Section <u>3.2</u>. Added Section <u>3.2.1</u> and titled and modified Section <u>3.2.2</u>.</p></li>
<li><p>Updated <u>Table 7</u>.</p></li>
<li><p>Updated Section <u>3.7.2</u>.</p></li>
<li><p>Updated <u>Figure 6</u>.</p></li>
<li><p>Updated Section <u>4.1</u>.</p></li>
<li><p>Updated <u>Figure 7</u>.</p></li>
<li><p>Updated Section <u>4.1.2</u>.</p></li>
<li><p>Update <u>Figure 9</u>.</p></li>
<li><p>Updated Sections <u>6.2.1</u> and <u>6.2.2</u>.</p></li>
<li><p>Updated Section <u>7</u>.</p></li>
<li><p>Updated Sections <u>7.1.1</u>, <u>7.1.2</u>, and <u>7.1.3</u>.</p></li>
<li><p>Deleted, Sections 6.1.4, "SharedRPCBroker_RXE5.bpl File" and 6.1.5, "SharedRPCBroker_DXE5.bpl File."</p></li>
<li><p>Deleted Sections 6.2, “Delphi XE4 Packages,” 6.3, "Delphi XE3 Packages," and 6.4, “Delphi XE2 Packages.”</p></li>
<li><p>Updated Section <u>8.1</u>.</p></li>
</ul>
<ul>
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
<li><p>Deleted Section 6, “RPC Broker Developer Utilities,” since those utilities no longer exist in this latest version of the Broker.</p></li>
<li><p>Updated the “<u>RPC Broker and Delphi</u>” section for Delphi XE5, XE4, XE3, and XE2.</p></li>
<li><p>Removed sample DLL from Section <u>8</u>.</p></li>
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
<td>4.2</td>
<td><p>Updates for RPC Broker Patch XWB*1.1*50:</p>
<ul>
<li><p>Added new properties.</p></li>
<li><p>Support for Delphi 5, 6, 7, 2005, 2006, and 2007.</p></li>
<li><p>Changed references form Patch 47 to Patch 50 where appropriate.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*50 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>07/03/2008</td>
<td>4.1</td>
<td><p>Updates for RPC Broker Patch XWB*1.1*47:</p>
<ul>
<li><p>No content changes required; no new public classes, methods, or properties added to those available in XWB*1.1*40.</p></li>
<li><p>Bug fixes to the <strong>ValidAppHandle</strong> function and fixed memory leaks.</p></li>
<li><p>Support added for Delphi 2005, 2006, and 2007.</p></li>
<li><p>Reformatted document.</p></li>
<li><p>Changed references form Patch 40 to Patch 47 where appropriate.</p></li>
</ul>
<p><strong>RPC Broker 1.1; XWB*1.1*47 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>02/24/2005</td>
<td>4.0</td>
<td><p>Revised Version for RPC Broker Patches XWB*1.1*35 and 40.</p>
<p>Also, reviewed document and edited for the “Data Scrubbing” and the “PDF 508 Compliance” projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to standards and conventions as indicated below:</p>
<ul>
<li><p>The first three digits (prefix) of any Social Security Numbers (SSN) start with “<strong>000</strong>” or “<strong>666</strong>.”</p></li>
<li><p>Patient or user names are formatted as follows: XWBPATIENT,[N] or XWBUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., XWBPATIENT, ONE, XWBPATIENT, TWO, etc.).</p></li>
<li><p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p>
<p><strong>RPC Broker 1.1; XWB*1.1*35 &amp; 40 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>05/08/2002</td>
<td>3.0</td>
<td><p>Revised Version for RPC Broker Patch XWB*1.1*26.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*26 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="even">
<td>05/01/2002</td>
<td>2.0</td>
<td><p>Revised Version for RPC Broker Patch XWB*1.1*13.</p>
<p><strong>RPC Broker 1.1; XWB*1.1*13 BDK</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
<tr class="odd">
<td>09/--/1997</td>
<td>1.0</td>
<td><p>Initial RPC Broker Version 1.1 software release.</p>
<p><strong>RPC Broker 1.1</strong></p></td>
<td>RPC Broker Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref449345480" class="anchor"></span>Table : Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc97001458" class="anchor"></span>List of Figures

<span id="_Toc449362416" class="anchor"></span>List of Tables

<span id="Orientation" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of the Remote Procedure Call (RPC) Broker 1.1 Development Kit (BDK) and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA).

Intended Audience

The intended audience of this manual is the following stakeholders:

- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) regional and local sites who are responsible for computer management and system security on the VistA M Servers.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

![](xwb-1-1-73-user-guide/002.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of this software for *non*-VistA use should be referred to the VistA site’s local Office of Information and Technology Field Office (OITFO).

Documentation Disclaimer

This manual provides an overall explanation of RPC Broker and the functionality contained in RPC Broker 1.1; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet Websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OIT) VistA Development Intranet website.

![](xwb-1-1-73-user-guide/003.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                           |
|-----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](xwb-1-1-73-user-guide/004.png)       | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](xwb-1-1-73-user-guide/005.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref449345481" class="anchor"></span>Table : Commonly Used RPC Broker Terms

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

![](xwb-1-1-73-user-guide/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](xwb-1-1-73-user-guide/007.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

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

![](xwb-1-1-73-user-guide/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

Commonly Used Terms

<u>Table 2</u> lists terms and their descriptions that can be helpful while reading the RPC Broker documentation:

<table>
<caption><p><span id="_Ref449355452" class="anchor"></span>Table : TRPCBroker Component Key Properties</p></caption>
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
<td><p>A software object that contains data and code. A component may or may <em>not</em> be visible.</p>
<p>![](xwb-1-1-73-user-guide/009.png) <strong>REF:</strong> For a more detailed description, see the <em>Embarcadero Delphi for Windows User Guide</em>.</p></td>
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

<span id="_Ref449355452" class="anchor"></span>Table : TRPCBroker Component Key Properties

![](xwb-1-1-73-user-guide/010.png) REF: For additional terms and definitions, see the “[Glossary](#glossary).”

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](xwb-1-1-73-user-guide/011.png) NOTE: Methods of obtaining specific technical information online are indicated where applicable under the appropriate section.  
  
REF: For further information, see the *RPC Broker Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes \[DILIST\] option on the Data Dictionary Utilities \[DI DDU\] menu in VA FileMan to print formatted data dictionaries.

![](xwb-1-1-73-user-guide/012.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

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
- *RPC Broker Technical Manual*
- *RPC Broker User Guide* (this manual)
- *RPC Broker Developer’s Guide*
- RPC Broker VA Intranet website.  
    
  This site provides announcements, additional information (e.g., Frequently Asked Questions \[FAQs\], advisories), documentation links, archives of older documentation and software downloads.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: <http://www.va.gov/vdl/>

RPC Broker documentation is located on the VDL at: <https://www.va.gov/vdl/application.asp?appid=23>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [About this Version of the BDK](#about-this-version-of-the-bdk)
    - [Features](#features)
    - [Backward Compatibility Issues](#backward-compatibility-issues)
- [RPC Broker Components for Delphi](#rpc-broker-components-for-delphi)
  - [TRPCBroker Component](#trpcbroker-component)
    - [TRPCBroker Properties and Methods](#trpcbroker-properties-and-methods)
    - [TRPCBroker Key Properties](#trpcbroker-key-properties)
    - [TRPCBroker Key Methods](#trpcbroker-key-methods)
    - [How to Connect to an M Server](#how-to-connect-to-an-m-server)
  - [TCCOWRPCBroker Component](#tccowrpcbroker-component)
    - [Single Signon/User Context (SSO/UC)](#single-signonuser-context-ssouc)
  - [TXWBRichEdit Component](#txwbrichedit-component)
  - [TXWBSSOiToken Component](#txwbssoitoken-component)
- [Remote Procedure Calls (RPCs)](#remote-procedure-calls-rpcs)
  - [What is a Remote Procedure Call?](#what-is-a-remote-procedure-call)
    - [Relationship between an M Entry Point and an RPC](#relationship-between-an-m-entry-point-and-an-rpc)
  - [Create Your Own RPCs](#create-your-own-rpcs)
    - [Preliminary Considerations](#preliminary-considerations)
    - [Process](#process)
  - [Writing M Entry Points for RPCs](#writing-m-entry-points-for-rpcs)
    - [First Input Parameter for RPCs (Required)](#first-input-parameter-for-rpcs-required)
    - [Return Value Types for RPCs](#return-value-types-for-rpcs)
    - [Input Parameter Types for RPCs (Optional)](#input-parameter-types-for-rpcs-optional)
    - [RPC M Entry Point Examples](#rpc-m-entry-point-examples)
  - [RPC Entry in the REMOTE PROCEDURE File](#rpc-entry-in-the-remote-procedure-file)
  - [What Makes a Good Remote Procedure Call?](#what-makes-a-good-remote-procedure-call)
  - [How to Execute an RPC from a Client Application](#how-to-execute-an-rpc-from-a-client-application)
  - [RPC Security: How to Register an RPC](#rpc-security-how-to-register-an-rpc)
    - [Bypassing RPC Security for Development](#bypassing-rpc-security-for-development)
    - [BrokerExample Online Code Example](#brokerexample-online-code-example)
- [Other RPC Broker APIs](#other-rpc-broker-apis)
  - [GetServerInfo Function](#getserverinfo-function)
    - [Overview](#overview)
    - [Syntax](#syntax)
  - [VistA Splash Screen Procedures](#vista-splash-screen-procedures)
  - [XWB GET VARIABLE VALUE RPC](#xwb-get-variable-value-rpc)
  - [M Emulation Functions](#m-emulation-functions)
    - [Translate Function](#translate-function)
  - [Encryption Functions](#encryption-functions)
    - [In Delphi](#in-delphi)
    - [On the VistA M Server](#on-the-vista-m-server)
  - [\$\$BROKER^XWBLIB](#brokerxwblib)
  - [\$\$RTRNFMT^XWBLIB](#rtrnfmtxwblib)
- [Broker Security Enhancement (BSE)](#broker-security-enhancement-bse)
  - [Introduction](#introduction-1)
    - [Features](#features-1)
    - [Architectural Scope](#architectural-scope)
  - [Process Overview](#process-overview)
    - [Process Diagrams](#process-diagrams)
  - [BSE-related VistA Applications and Modules](#bse-related-vista-applications-and-modules)
  - [Kernel—Authentication Interface to VistA](#kernelauthentication-interface-to-vista)
  - [RPC Broker](#rpc-broker)
    - [Client](#client)
    - [Server](#server)
  - [REMOTE APPLICATION (#8994.5) File](#remote-application-89945-file)
  - [Security Phrase](#security-phrase)
  - [Kernel Authentication Token](#kernel-authentication-token)
- [Debugging and Troubleshooting](#debugging-and-troubleshooting)
  - [How to Debug Your Client Application](#how-to-debug-your-client-application)
    - [RPC Error Trapping](#rpc-error-trapping)
  - [Troubleshooting Connections](#troubleshooting-connections)
    - [Identifying the Listener Process on the Server](#identifying-the-listener-process-on-the-server)
    - [Identifying the Handler Process on the Server](#identifying-the-handler-process-on-the-server)
    - [Testing Your RPC Broker Connection](#testing-your-rpc-broker-connection)
- [RPC Broker and Delphi](#rpc-broker-and-delphi)
  - [Delphi 10.4, 10.3, 10.2, 10.1, 10.0, and XE8 Packages](#delphi-104-103-102-101-100-and-xe8-packages)
    - [Delphi Starter Edition—Not Recommended for BDK Development](#delphi-starter-editionnot-recommended-for-bdk-development)
    - [XWBRXE\#.bpl File](#xwbrxebpl-file)
    - [XWBDXE\#.bpl File](#xwbdxebpl-file)
- [RPC Broker Dynamic Link Library (DLL)](#rpc-broker-dynamic-link-library-dll)
  - [DLL Interface](#dll-interface)
    - [Exported Functions](#exported-functions)
    - [Header Files Provided](#header-files-provided)
    - [Return Values from RPCs](#return-values-from-rpcs)
    - [COTS Development and the DLL](#cots-development-and-the-dll)
The Remote Procedure Call (RPC) Broker (also referred to as “Broker”) is a client/server system within Department of Veterans Affairs (VA) Veterans Health Information Systems and Technology Architecture (VistA) environment. It establishes a common and consistent foundation for client/server applications being written as part of VistA. It enables client applications to communicate and exchange data with M Servers.
This manual provides an overview of software development with the RPC Broker. It introduces developers to the RPC Broker and the Broker Development Kit (BDK) with emphasis on using the RPC Broker in conjunction with Embarcadero’s Delphi software. However, the RPC Broker supports other development environments.
![](xwb-1-1-73-user-guide/013.png) REF: For more complete information on development with the RPC Broker components, see the *RPC Broker Developer’s Guide.*
This document is intended for the VistA development community and system administrators. A wider audience of technical personnel engaged in operating and maintaining the Department of Veterans Affairs (VA) software can also find it useful as a reference.

## About this Version of the BDK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

RPC Broker 1.1 (fully patched) provides developers with the capability to create new VistA client/server software using the following RPC Broker Delphi components in the 32-bit environment:

- TCCOWRPCBroker
- TContextorControl
- TRPCBroker (original component)
- TXWBRichEdit
- TXWBSSOi

![](xwb-1-1-73-user-guide/014.png) NOTE: These RPC Broker components wrap the functionality of the Broker resulting in a more modularized and orderly interface. Those components derived from the original TRPCBroker component, inherit the TRPCBroker properties and methods.

### Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This enhanced Broker software has the following functionality/features:

- Selection of the User's Authentication Certificate—Eliminates the need for the user to select from a list of certificates.
- Supports Active Directory (AD) Credentials—When a user is unable to log onto a workstation with their Personal Identity Verification (PIV) card, the user contacts the Enterprise Service Desk (ESD) to receive a PIV exemption to allow them to log on with their Active Directory (AD) credentials (username and password). This enhanced BDK detects this condition and allows the user to use their AD credentials to secure a SAML token from IAM for logging onto VistA via applications compiled with this version of the BDK.
- Supports 2-factor Authentication—The TRPCBroker component authenticates a user by making a mutual Transport Layer Security (TLS) authentication connection to the Identity and Access Management (IAM) Secure Token Service (STS). Mutual authentication refers to two parties authenticating each other at the same time. Mutual TLS authentication uses the TLS protocol to authenticate and identify a user using Public Key Encryption (PKI) certificates (usually found on a portable smart card or device) and a private Personal Identification Number (PIN) to unlock the certificate. The STS server returns a digitally-signed token containing the user’s identity. This token is trusted by the VistA M Server as a delegated form of user authentication.
- Supports IPv4/IPv6 Dual-Stack Environment—The TRPCBroker component uses WinSock 2.2 Application Programming Interfaces (APIs) that support network connections using Internet Protocol (IP) version 4 and/or IP version 6. IPv6 is a protocol designed to handle the growth rate of the Internet and to cope with the demanding requirements of services, mobility, and end-to-end security.
- Supports Secure Shell (SSH)—The TRPCBroker component enabled Secure Shell (SSH) Tunnels to be used for secure connections. This functionality is controlled by setting an internal property value (mandatory SSH) or command line option at run-time.
- Supports Broker Security Enhancement (BSE)—The TRPCBroker component enabled visitor access to remote sites using authentication established at a home site.
- Supports Single Sign-On/User context (SSO/UC)—TCCOWRPCBroker component enables Single Sign-On/User Context (SSO/UC) in CCOW-enabled applications.
- Supports Non-Callback Connections—By default the RPC Broker components are built with a UCX or *non*-callback Broker connection, so that it can be used from behind firewalls, routers, etc.
- Supports Silent Logon capabilities—RPC Broker provides “Silent Login” capability. It provides functionality associated with the ability to make logins to a VistA M Server without the RPC Broker asking for Access and Verify code information.
- Documented Deferred RPCs and Capability to Run RPCs on a Remote Server.
- Multi-instances of the RPC Broker—RPC Broker code permits an application to open two separate Broker instances with the same Server/ListenerPort combination, resulting in two separate partitions on the server. Previously, an attempt to open a second Broker instance ended up using the same partition. For this capability to be useful for concurrent processing, an application would have to use threads to handle the separate Broker sessions.

![](xwb-1-1-73-user-guide/015.png) CAUTION: Although we believe there should be no problems, the RPC Broker is *not* guaranteed to be thread safe.

- Updated components, properties, methods, and types.
- Separate DesignTime and RunTime Packages—BDK contains separate RunTime and DesignTime packages.
- Supports Delphi 10.4, 10.3, 10.2, 10.1, 10, 10.0, and XE8.

To develop VistA applications in a 32-bit environment you *must* have Delphi XE8 or greater. However, the Broker routines on the M server continue to support VistA applications previously developed in the 16-bit environment.

The default installation of the Broker creates a separate BDK directory (i.e., BDK32) that contains the required Broker files for development.

![](xwb-1-1-73-user-guide/016.png) REF: For a complete list of all new or modified features and functionality with RPC Broker 1.1, see the *RPC Broker Release Notes*.

### Backward Compatibility Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Client applications compiled with RPC Broker 1.1 will *not* work at a site that has *not* upgraded its RPC Broker server software to Version 1.1.

On the other hand, client applications compiled with RPC Broker 1.0 will work with the RPC Broker 1.1 server.

# RPC Broker Components for Delphi

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xwb-1-1-73-user-guide/017.png) REF: For more detailed information on the RPC Broker components for Delphi, see the *RPC Broker Developer’s Guide.*

## TRPCBroker Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main tool to develop client applications for the RPC Broker environment is the TRPCBroker component for Delphi. The TRPCBroker component adds the following abilities to your Delphi application:

- Connecting to an M server:
- Authenticate the user
- Set up the environment on the server
- Bring back the introductory text
- Invoking Remote Procedure Calls (RPCs) on the M Server:
- Send data to the M Server
- Perform actions on the server
- Return data from the server to the client

To add the TRPCBroker component to your Delphi application, simply drop it from the Kernel tab of Delphi’s component palette to a form in your application.

### TRPCBroker Properties and Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a Delphi component, the TRPCBroker component is controlled and accessed through its properties and methods. By setting its properties and executing its methods, you can connect to an M server from your application and execute RPCs on the M server to exchange data and perform actions on the M server.

For most applications, you only need to use a single TRPCBroker component to manage communications with the M server.

### TRPCBroker Key Properties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists the most important properties of the TRPCBroker component.

![](xwb-1-1-73-user-guide/018.png) REF: For a complete list of all of Broker properties, see the *RPC Broker Developer’s Guide.*

| Property                | Description                                                                                                                                                                                                                                         |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ClearParameters     | If True, the Param property is cleared *after* every invocation of the Call, strCall, or the lstCall methods.                                                                                                                   |
| ClearResults        | If True, the Results property is cleared *before* every invocation of the Call method, thus assuring that only the results of the last call are returned.                                                                               |
| Connected           | Setting this property to True connects your application to the server.                                                                                                                                                                          |
| ListenerPort        | Sets server port to connect to a Broker Listener process (mainly for development purposes; for end-users, determine on the fly with GetServerInfo method.)                                                                                      |
| Param               | RunTime array in which you set any parameters to pass as input parameters when calling an RPC on the server.                                                                                                                                    |
| RemoteProcedure     | Name of a RemoteProcedure entry that the Call, lstCall, or strCall method should invoke.                                                                                                                                            |
| Results             | This is where any results are stored after a Call, lstCall, or strCall method completes.                                                                                                                                                |
| Server              | Name of the server to connect to (mainly for development purposes; for end-users, determine on-the-fly with GetServerInfo method.)                                                                                                              |
| SSHPort             | Holds a specific port number for Secure Shell (SSH) Tunneling if the UseSecureConnection property is set to “SSH” or “PLINK”. If *not* specified, uses the RPC Broker listener port for the remote server.                              |
| SSHPw               | Holds a password for SSH Tunneling if the UseSecureConnection property is set to “PLINK”.                                                                                                                                                   |
| SSHUser             | Holds a specific username for SSH Tunneling if the UseSecureConnection property is set to “SSH”. For VA VistA servers, the username is typically of the form *xxx*vista where the *xxx* is the station’s three letter abbreviation. |
| UseSecureConnection | Used to specify whether SSH Tunneling is to be used when making the connection.                                                                                                                                                                     |

<span id="_Toc82598507" class="anchor"></span>Table : TRPCBroker Component Methods

### TRPCBroker Key Methods

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the most important methods of the TRPCBroker component.

![](xwb-1-1-73-user-guide/019.png) REF: For a complete list of all of Broker methods, see the *RPC Broker Developer’s Guide.*

<table>
<caption><p><span id="_Ref97011490" class="anchor"></span>Table : RPC Broker Return Value Types</p></caption>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th>Method</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>procedure Call;</strong></td>
<td><p>This method executes an RPC on the server and returns the results in the <strong>TRPCBroker</strong> component’s <strong>Results</strong> property.</p>
<p><strong>Call</strong> expects the name of the remote procedure and its parameters to be set up in the <strong>RemoteProcedure</strong> and <strong>Param</strong> properties respectively.</p>
<p>If <strong>ClearResults</strong> is <strong>True</strong>, then the <strong>Results</strong> property is cleared before the call.</p>
<p>If <strong>ClearParameters</strong> is <strong>True</strong>, then the <strong>Param</strong> property is cleared after the call finishes.</p></td>
</tr>
<tr class="even">
<td><strong>function strCall: string;</strong></td>
<td>This method is a variation of the <strong>Call</strong> method. Only use it when the return type is a single string. Instead of returning results in the <strong>TRPCBroker</strong> component’s <strong>Results[0]</strong> property node, results are returned as the value of the function call. Unlike the <strong>Call</strong> method, the <strong>Results</strong> property is <em>not</em> affected; no matter the setting of <strong>ClearResults</strong>, the value is left unchanged.</td>
</tr>
<tr class="odd">
<td><strong>procedure lstCall(OutputBuffer: TStrings);</strong></td>
<td>This method is a variation of the <strong>Call</strong> method. Instead of returning results in the <strong>TRPCBroker</strong> component’s <strong>Results</strong> property, it instead returns results in the <strong>TStrings</strong> object you specify. Unlike the <strong>Call</strong> method, the <strong>Results</strong> property is <em>not</em> affected; no matter the setting of <strong>ClearResults</strong>, the value is left unchanged.</td>
</tr>
<tr class="even">
<td><strong>function CreateContext(strContext: string): boolean;</strong></td>
<td>This method creates a context for your application. Pass an option name in the <strong>strContext</strong> parameter. If the function returns <strong>True</strong>, a context was created, and your application can use all RPCs entered in the option’s RPC multiple.</td>
</tr>
</tbody>
</table>

<span id="_Ref97011490" class="anchor"></span>Table : RPC Broker Return Value Types

Examples

For examples of how to use these methods to invoke RPCs, see the “<u>How to Execute an RPC from a Client Application</u>” section.

### How to Connect to an M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To establish a connection from your application to a Broker server, perform the following procedure:

1.  From the Kernel component palette tab, add a TRPCBroker component to your form.
10. Add code to your application to connect to the server; one likely location is your form’s OnCreate event handler. The code should:
1.  Use the GetServerInfo function to retrieve the RunTime server and port to connect to, and SSHUsername if available.

![](xwb-1-1-73-user-guide/020.png) NOTE: This function is *not* a method of the TRPCBroker component; it is described in the “<u>Other RPC Broker APIs”</u> section.

2.  Inside of an exception handler try...except block, set RPCBroker1’s Connected property to True. This causes an attempt to connect to the Broker server and authenticates the user.
3.  Check if an EBrokerError exception is raised. If this happens, connection failed. You should inform the user of this and then terminate the application.

The code, placed in an OnCreate event handler, should look like <u>Figure 1</u>:

<span id="_Ref449355847" class="anchor"></span>Figure : OnCreate Event Handler—Sample Code

procedure TForm1.FormCreate(Sender: TObject);

var ServerStr: String;

PortStr: String;

begin

*// get the correct port and server from registry*

if GetServerInfo(ServerStr,PortStr,SSHUsernameStr)\<\>mrCancel then

begin

RPCBroker1.Server:=ServerStr;

RPCBroker1.ListenerPort:=StrToInt(PortStr);

if SSHUsernameStr \<\> ‘’ then

begin

RPCBroker1.UseSecureConnection := ‘SSH’;

RPCBroker1.SSHport := ‘‘;

RPCBroker1.SSHUser := SSHUsernameStr;

RPCBroker1.SSHpw := ‘‘;

RPCBroker1.SSHHide := true;

end;

end

else Application.Terminate;

*// establish a connection to the Broker*

try

RPCBroker1.Connected:=True;

except

On EBrokerError do

begin

ShowMessage(‘Connection to server could not be established!’);

Application.Terminate;

end;

end;

end;

11. A connection with the Broker M Server is now established. You can use the CreateContext method of the TRPCBroker component to authorize use of RPCs for your user, and then use the Call, lstCall, and strCall methods of the TRPCBroker component to execute RPCs on the M server.

![](xwb-1-1-73-user-guide/021.png) REF: For information on creating and executing RPCs, see the “<u>Remote Procedure Calls (RPCs)</u>” section.

## TCCOWRPCBroker Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Patch XWB\*1.1\*40, the TCCOWRPCBroker component was added to Version 1.1 of the RPC Broker. The TCCOWRPCBroker Delphi component allows VistA application developers to make their applications CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware with all of the client/server-related functionality in one integrated component. Using the TCCOWRPCBroker component, an application can share User Context stored in the CCOW Context Vault.

Thus, when a VistA CCOW-enabled application is recompiled with the TCCOWRPCBroker component and other required code modifications are made, that application would then become SSO/UC-aware and capable of single sign-on (SSO).

![](xwb-1-1-73-user-guide/022.png) NOTE: This RPC Broker component is derived from the original <u>TRPCBroker Component</u>; it inherits the TRPCBroker properties and methods.

### Single Signon/User Context (SSO/UC)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veterans Health Administration (VHA) information systems user community expressed a need for a single sign-on (SSO) service with interfaces to VistA, Health*e*Vet VistA, and *non*-VistA systems. This architecture allows users to authenticate and sign on to multiple applications that are CCOW-enabled and SSO/UC-aware using a single set of credentials, which reduces the need for multiple ID’s and passwords in the Health*e*Vet clinician desktop environment. The RPC Broker software addressed this architectural need by providing a new TCCOWRPCBroker component in RPC Broker Patch XWB\*1.1\*40.

The TCCOWRPCBroker component allows VistA application developers to make their applications CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware with all of the client/server-related functionality in one integrated component. Using the TCCOWRPCBroker component, an application can share User Context stored in the CCOW Context Vault.

Thus, when a VistA CCOW-enabled application is recompiled with the TCCOWRPCBroker component and other required code modifications are made, that application would then become SSO/UC-aware and capable of single sign-on (SSO).

![](xwb-1-1-73-user-guide/023.png) REF: For more information on SSO/UC and making your Broker-based applications CCOW-enabled and SSO/UC-aware, please consult the *Single Sign-On/User Context (SSO/UC) Installation Guide* and *Single Sign-On/User Context (SSO/UC) Deployment Guide* on the VA Software Document Library (VDL) at: <https://www.va.gov/vdl/application.asp?appid=162>

## TXWBRichEdit Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Patch XWB\*1.1\*13, the TXWBRichEdit component was added to Version 1.1 of the RPC Broker. The TXWBRichEdit Delphi component replaces the Introductory Text Memo component on the Login Form. TXWBRichEdit is a version of the TRichEdit component that uses Version 2 of Microsoft’s RichEdit Control and adds the ability to detect and respond to a Uniform Resource Locator (URL) in the text. This component permits us to provide some requested functionality on the login form. As an XWB namespaced component, it *must* be put it on the Kernel tab of the component palette, however, it rightly belongs on the Win32 tab.

## TXWBSSOiToken Component

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of Patch XWB\*1.1\*65, the TXWBSSOiToken component was added to RPC Broker 1.1. The TXWBSSOiToken Delphi component is used to authenticate a user into the Identity and Access Management (IAM) Secure Token Service (STS) and obtain a Security Assertion Markup Language (SAML) token containing an authenticated user’s identity. The TXWBSSOiToken component does *not* need to be specifically added to an RPC Broker application, as authentication is built into the <u>TRPCBroker Component</u>. However, it is made available as a separate component for those applications that might need to obtain a SAML token for authentication into *non*-RPC Broker applications or servers.

# Remote Procedure Calls (RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## What is a Remote Procedure Call?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A remote procedure call (RPC) is a defined call to M code that runs on an M server. A client application, through the RPC Broker, can make a call to the M server and execute an RPC on the M server. This is the mechanism through which a client application can:

- Send data to an M server.
- Execute code on an M server.
- Retrieve data from an M server.

An RPC can take optional parameters to do some task and then return either a single value or an array to the client application. RPCs are stored in the REMOTE PROCEDURE (#8994) file.

### Relationship between an M Entry Point and an RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An RPC can be thought of as a wrapper placed around an M entry point for use with client applications. Each RPC invokes a single M entry point. The RPC passes data in specific ways to its corresponding M entry point and expects any return values from the M entry point to be returned in a pre-determined format. This allows client applications to connect to the RPC Broker, invoke an RPC, and through the RPC, invoke an M entry point on a server.

## Create Your Own RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Preliminary Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Because creating a Remote Procedure Call (RPC) could introduce security risks, you should consider your options prior to creating a new one:

1.  First, look for an existing RPC that provides the data you need. You may need an Integration Control Registration (ICR) for permission to use the RPC.
12. If you *cannot* locate an existing RPC that meets your needs, look for an existing Application Programming Interface (API) that can be wrapped with a new RPC.
13. If an existing RPC or API provides “almost” what you need, contact the package owners to see whether there is a modification or alternative that could be provided to meet your needs. For example, determine whether post-processing of the data in your application would provide the results you need.
14. You should create a new RPC only as a last result. When creating a new RPC is necessary, you should carefully consider how general to make the RPC, so that it can potentially be used by other applications in the future.

### Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can create your own custom RPCs to perform actions on the M server and to retrieve data from the M server. Then you can call these RPCs from your client application. Creating an RPC requires you to perform the following steps:

1.  Reference the [*RPC Broker Developers Guide*](http://www.va.gov/vdl/application.asp?appid=23) for instructions and examples when creating a new RPC.
2.  Write and test the M entry point that is called by the RPC.
15. Add the RPC entry that invokes your M entry point, in the REMOTE PROCEDURE (#8994) file. The RPC name should begin with the VistA package namespace that owns the RPC. For example, “XWB EXAMPLE BIG TEXT” is owned by the RPC Broker package (namespace: XWB). M Programming Standards and Conventions (SAC) provide policy on name requirements for new RPCs.
16. Add the RPC to a “B-Broker (Client/Server)” type option in the OPTION (#19) file. The option should be in your VistA package namespace. M Programming Standards and Conventions (SAC) provide policy on name requirements for options.

## Writing M Entry Points for RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### First Input Parameter for RPCs (Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker always passes a variable by reference in the first input parameter to your M routine. It expects results (one of five types described in <u>Table 5</u>) to be returned in this parameter. You *must* always set some return value into that first parameter before your routine returns.

### Return Value Types for RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 5</u> lists the five RETURN VALUE TYPES for RPCs. Choose a return value type that is appropriate to the type of data your RPC needs to return to your client. Your M entry point should set the return value (in the routine’s first input parameter) accordingly.

<table style="width:100%;">
<caption><p><span id="_Ref468167430" class="anchor"></span>Table : Input Parameter Types</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 44%" />
<col style="width: 14%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th>RPC Return Value Type</th>
<th>How M Entry Point Should Set the Return Parameter</th>
<th>RPC WORD WRAP ON Setting</th>
<th>Value(s) returned in Client Results</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Single Value</strong></td>
<td><p>Set the return parameter to a single value.</p>
<p>For example:</p>
<p>TAG(RESULT) ;</p>
<p>S RESULT=“DOE, JOHN”</p>
<p>Q</p></td>
<td>No effect</td>
<td>Value of parameter, in <strong>Results[0]</strong>.</td>
</tr>
<tr class="even">
<td><strong>Array</strong></td>
<td><p>Set an array of strings into the return parameter, each subscripted one level descendant.</p>
<p>For example:</p>
<p>TAG(RESULT) ;</p>
<p>S RESULT(1)=“ONE”</p>
<p>S RESULT(2)=“TWO”</p>
<p>Q</p>
<p>For large arrays consider using the <strong>GLOBAL ARRAY</strong> return value type to avoid memory allocation errors.</p></td>
<td>No effect</td>
<td>Array values, each in a Results item.</td>
</tr>
<tr class="odd">
<td rowspan="2"><strong>Word-processing</strong></td>
<td rowspan="2">Set the return parameter the same as you set it for the <strong>Array</strong> type. The only difference is that the WORD WRAP ON (#.08) field setting affects the <strong>Word-Processing</strong> return value type.</td>
<td><strong>True</strong></td>
<td>Array values, each in a Results item.</td>
</tr>
<tr class="even">
<td><strong>False</strong></td>
<td>Array values concatenated into <strong>Results[0]</strong>.</td>
</tr>
<tr class="odd">
<td rowspan="2"><strong>Global Array</strong></td>
<td rowspan="2"><p>Set the return parameter to a closed global reference in <strong>^TMP</strong>. The global’s data nodes are traversed using <strong>$QUERY</strong>, and all data values on global nodes descendant from the global reference are returned.</p>
<p>The <strong>Global Array</strong> type is especially useful for returning data from VA FileMan word-processing fields, where each line is on a <strong>0</strong>-subscripted node.</p>
<p>![](xwb-1-1-73-user-guide/024.png) CAUTION: The global reference you pass is killed by the Broker at the end of RPC Execution as part of RPC cleanup. Do not pass a global reference that is <em>not</em> in ^TMP or that should <em>not</em> be killed.</p>
<p>This type is useful for returning large amounts of data to the client, where using the <strong>Array</strong> type can exceed the symbol table limit and crash your RPC.</p>
<p>For example, to return signon introductory text you could do:</p>
<p>TAG(RESULT);</p>
<p>M ^TMP(“A6A”,$J)=</p>
<p>^XTV(8989.3,1,”INTRO”)</p>
<p>;this node not needed</p>
<p>K ^TMP(“A6A”,$J,0)</p>
<p>S RESULT=$NA(^TMP(“A6A”,$J))</p>
<p>Q</p></td>
<td><strong>True</strong></td>
<td>Array values, each in a Results item.</td>
</tr>
<tr class="even">
<td><strong>False</strong></td>
<td>Array values concatenated into <strong>Results[0]</strong>.</td>
</tr>
<tr class="odd">
<td><strong>Global Instance</strong></td>
<td><p>Set the return parameter to a closed global reference.</p>
<p>For example, to return the <strong>0<sup>th</sup></strong> node from the NEW PERSON (#200) file for the current user:</p>
<p>TAG(RESULT) ;</p>
<p>S RESULT=$NA(^VA(200,DUZ,0))</p>
<p>Q</p></td>
<td>No effect</td>
<td>Value of global node, in <strong>Results[0]</strong>.</td>
</tr>
</tbody>
</table>

<span id="_Ref468167430" class="anchor"></span>Table : Input Parameter Types

### Input Parameter Types for RPCs (Optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The M entry point for an RPC can optionally have input parameters (i.e., beyond the first parameter, which is always used to return an output value). The client passes data to your M entry point through these parameters.

<u>Table 6</u> lists the three format types that the client can send data to an RPC (and therefore your entry point):

<table>
<caption><p><span id="_Ref449509690" class="anchor"></span>Table : REMOTE PROCEDURE File Key Field Entries</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th>Param PType</th>
<th>Param Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Literal</strong></td>
<td>Delphi string value; passed as a string literal to the M server.</td>
</tr>
<tr class="even">
<td><strong>Reference</strong></td>
<td><p>Delphi string value; treated on the M Server as an M variable name and resolved from the symbol table at the time the RPC executes.</p>
<p>![](xwb-1-1-73-user-guide/025.png) CAUTION: For enhanced security reasons, the reference parameter type may be deprecated and removed in subsequent updates to the BDK.</p></td>
</tr>
<tr class="odd">
<td><strong>List</strong></td>
<td>A single-dimensional array of strings in the <strong>Mult</strong> subproperty of the <strong>Param</strong> property, passed to the M Server where it is placed in an array. String subscripting can be used.</td>
</tr>
</tbody>
</table>

<span id="_Ref449509690" class="anchor"></span>Table : REMOTE PROCEDURE File Key Field Entries

The type of the input parameters passed in the Param property of the TRPCBroker component determines the format of the data you *must* be prepared to receive in your M entry point.

### RPC M Entry Point Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following two examples illustrate sample M code that could be used in simple RPCs.

#### Sum of Two Numbers

The example in <u>Figure 2</u> takes two numbers and returns their sum:

<span id="_Ref39643257" class="anchor"></span>Figure : RPC M Entry Point Example—Sum of Two Numbers

> SUM(RESULT,A,B) ;add two numbers

> S RESULT=A+B

> Q

#### Sorted Array

The example in <u>Figure 3</u> receives an array of numbers and returns them as a sorted array to the client:

<span id="_Ref39643284" class="anchor"></span>Figure : RPC M Entry Point Example—Sorted Array

SORT(RESULT,UNSORTED) ;sort numbers

N I

S I=““

F S I=\$O(UNSORTED(I)) Q:I=““ S RESULT(UNSORTED(I))=UNSORTED(I)

Q

## RPC Entry in the REMOTE PROCEDURE File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the M code is complete, you need to create the RPC itself in the REMOTE PROCEDURE (#8994) file. The following fields in the REMOTE PROCEDURE (#8994) file are key to the correct operation of an RPC:

<table>
<caption><p><span id="_Ref59095285" class="anchor"></span>Table : BSE—Application Authentication Server Class Types</p></caption>
<colgroup>
<col style="width: 32%" />
<col style="width: 14%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Required?</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)</td>
<td>Yes</td>
<td>The name that identifies the RPC (this entry should be namespaced in the package namespace).</td>
</tr>
<tr class="even">
<td>TAG (#.02)</td>
<td>Yes</td>
<td>The tag at which the remote procedure call begins.</td>
</tr>
<tr class="odd">
<td>ROUTINE (#.03))</td>
<td>Yes</td>
<td>The name of the routine that should be invoked to start the RPC.</td>
</tr>
<tr class="even">
<td>WORD WRAP ON (#.08)</td>
<td>No</td>
<td><p>Affects <strong>Global Array</strong> and <strong>Word-Processing</strong> return value types only:</p>
<ul>
<li><p>If set to <strong>False</strong>, data is returned in a single concatenated string in <strong>Results[0]</strong>.</p></li>
<li><p>If set to <strong>True</strong>, each array node on the M side is returned as a distinct array item in Results.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>RETURN VALUE TYPE (#.04)</td>
<td>Yes</td>
<td>This indicates to the Broker how to format the return values. For example, if the RETURN VALUE TYPE is set as <strong>Word-Processing</strong>, then each entry in the returning list has a <strong>&lt;CR&gt;&lt;LF&gt;</strong> (<strong>&lt;carriage return&gt;&lt;line feed&gt;</strong>) appended.</td>
</tr>
<tr class="even">
<td>APP PROXY ALLOWED (#.11)</td>
<td>No</td>
<td><p>This field <em>must</em> be set to <strong>Allowed</strong> (<strong>1</strong>) if this RPC is to be run by an APPLICATION PROXY user. The default is to <em>not</em> allow access.</p>
<p>![](xwb-1-1-73-user-guide/026.png) CAUTION: APPLICATION PROXY users do <em>not</em> meet Health Insurance Portability and Accounting Act of 1996 (HIPAA) requirements for user identification and should <em>not</em> be permitted to access an RPC that reads or writes Personal Health Information (PHI).</p></td>
</tr>
<tr class="odd">
<td>PARAMETER TYPE (#8994.02,.02) field of the INPUT PARAMETER Multiple (#8994.02)</td>
<td>Yes</td>
<td><p>This field is used to indicate the type (<strong>Literal</strong>, <strong>List</strong>, <strong>Reference</strong>, or <strong>Word-Processing</strong> entry) of value passed by this parameter. The <strong>Literal</strong>, <strong>List</strong>, and <strong>Reference</strong> types correspond to the <strong>TParamType</strong> of the same name. A <strong>Word-Processing</strong> type would also be a <strong>List</strong> <strong>TParamType</strong>.</p>
<p>Currently, this declaration is mandatory for a reference, but <em>recommended</em> for other types. In the future the parameter type declaration will be enforced for all types.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref59095285" class="anchor"></span>Table : BSE—Application Authentication Server Class Types

## What Makes a Good Remote Procedure Call?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following make for a good remote procedure call (RPC) :

- Silent calls (no I/O to terminal or screen, no user intervention required).
- Minimal resources required (passes data in brief, controlled increments).
- Discrete calls (requiring as little information as possible from the process environment).
- Generic as possible (different parts of the same package as well as other packages could use the same RPC).

## How to Execute an RPC from a Client Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To execute an RPC from a client application, perform the following procedure:

1.  If your RPC has any input parameters beyond the mandatory first parameter, set a Param node in the TRPCBroker’s Param property for each. For each input parameter, set the following sub properties:
- Value
- PType (Literal, List, or Reference)

If the parameter’s PType is List, however, set a list of values in the Mult subproperty rather than setting the Value subproperty.

![](xwb-1-1-73-user-guide/027.png) CAUTION: For enhanced security reasons, the reference parameter type may be deprecated and removed in subsequent updates to the BDK.

<u>Figure 4</u> is an example of some settings of the Param property:

<span id="_Ref361734575" class="anchor"></span>Figure : Param Property—Sample Settings

> RPCBroker1.Param\[0\].Value := ‘10/31/97’;

> RPCBroker1.Param\[0\].PType := literal;

> RPCBroker1.Param\[1\].Mult\[‘“NAME”‘\] := ‘XWBUSER, ONE’;

> RPCBroker1.Param\[1\].Mult\[‘“SSN”‘\] := ‘000-45-6789’;

> RPCBroker1.Param\[1\].PType := list;

17. Set the TRPCBroker’s RemoteProcedure property to the name of the RPC to execute.

RPCBroker1.RemoteProcedure:=‘A6A LIST’;

18. Invoke the Call method of the TRPCBroker component to execute the RPC. All calls to the Call method should be done within an exception handler try...except statement, so that all communication errors (which trigger the EBrokerError exception) can be trapped and handled. For example:

<span id="_Toc202777928" class="anchor"></span>Figure : Exception Handler—try...except Code—Sample Usage

> try

> RPCBroker1.Call;

> except

> On EBrokerError do

> ShowMessage(‘A problem was encountered communicating with the server.’);

> end;

19. Any results returned by your RPC are returned in the TRPCBroker component’s Results property. Depending on how you set up your RPC, results are returned either in a single node of the Results property (Result\[0\]) or in multiple nodes of the Results property.

![](xwb-1-1-73-user-guide/028.png) NOTE: You can also use the lstCall and strCall methods to execute an RPC. The main difference between these methods and the Call method is that lstCall and strCall do *not* use the Results property, instead returning results into a location you specify.

## RPC Security: How to Register an RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Security for RPCs is handled through the RPC registration process. Each client application *must* create a context for itself, which checks if the application user has access to a “B”-type option in the Kernel menu system. Only RPCs assigned to that option can be run by the client application.

To enable your application to create a context for itself, perform the following procedure:

1.  Create a “B”-type option in the OPTION (#19) file for your application.

![](xwb-1-1-73-user-guide/029.png) NOTE: The OPTION TYPE “B” represents a Broker client/server type option.

20. In the RPC multiple for this option type, add an entry for each RPC that your application calls. You can also specify a security key that can lock each RPC (this is a pointer to the SECURITY KEY \[#19.1\] file) and M code in the RULES subfield that can also determine whether to enable access to each RPC.
21. When you export your software using KIDS, export both your RPCs and your software option.
22. Your application *must* create a context for itself on the server, which checks access to RPCs. In the initial code of your client application, make a call to the CreateContext method of your TRPCBroker component. Pass your application’s “B”-type option’s name as a parameter. For example:

RPCBroker1.CreateContext(option_name)

If the CreateContext method returns True, only those RPCs designated in the RPC multiple of your application option are permitted to run.

If the CreateContext method returns False, you should terminate your application (if you do *not*, your application runs, but you get errors every time you try to access an RPC).

23. End-users of your application *must* have the “B”-type option assigned to them on one of their menus, in order for the CreateContext method to return True.

### Bypassing RPC Security for Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Having the XUPROGMODE security key allows you to bypass the Broker security checks. You can run any RPC without regard to application context (without having to use the CreateContext method). This is a convenience for application development. When you complete development, make sure you test your application from an account *without* the XUPROGMODE key, to ensure that all RPCs needed are properly registered.

### BrokerExample Online Code Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BrokerExample sample application (i.e., BROKEREXAMPLE.EXE) provided with the BDK demonstrates the basic features of developing RPC Broker-based applications, including:

- Connecting to an M server.
- Creating an application context.
- Using the GetServerInfo function.
- Displaying the VistA splash screen.
- Setting the TRPCBroker’s Param property for each Param PType (literal, reference, and list).
- Calling RPCs with the Call method.
- Calling RPCs with the lstCall and strCall methods.
- Secure Shell (SSH) connection (from Options menu) methods.

The client source code files for the BrokerExample application are located in the SAMPLES\RPCBROKER\BROKEREX subdirectory of the main BDK32 directory.

<span id="_Ref449356107" class="anchor"></span>Figure : RPC Broker Example Application

![](xwb-1-1-73-user-guide/030.png)

# Other RPC Broker APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## GetServerInfo Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The GetServerInfo function retrieves the end-user workstation’s server, port, and SSHUsername if available. Use this function to set the TRPCBroker component’s Server, ListenerPort, and SSHUser properties to reflect the end-user workstation’s settings before connecting to the server.

If there is more than one server/port to choose from, GetServerInfo displays dialogue that allows users to select a service to connect to, as shown in <u>Figure 7</u>:

<span id="_Ref361733242" class="anchor"></span>Figure : Server and Port Configuration Selection Dialogue (REDACTED)

![](xwb-1-1-73-user-guide/031.png)

If exactly one server and port entry is defined in the Microsoft Windows Registry, GetServerInfo does *not* display the dialogue in <u>Figure 7</u>. The values in the single Microsoft Windows Registry entry are returned, with no user interaction required.

If more than one server and port entry exists in the Microsoft<sup>®</sup> Windows Registry, the dialogue is displayed, and the user chooses to which server they want to connect.

If no values for server and port are defined in the Microsoft<sup>®</sup> Windows Registry, GetServerInfo does *not* display the dialogue in <u>Figure 7</u>, and automatic default values are returned (i.e., BROKERSERVER and \<REDACTED\>).

The values are stored in either of the following registries:

- HKEY_CURRENT_USER (HKCU)
- HKEY_LOCAL_MACHINE (HKLM)

These registries are located under:

\Software\Vista\Broker\Servers

Entries are of the format:

- Name: Server,ListenerPort
- Type: REG_SZ
- Data: SSHUser

For example, a connection to server address “\<REDACTED\>.va.gov” using port \<REDACTED\> and SSHUsername of “\<REDACTED\>” would look like:

<span id="_Ref468168360" class="anchor"></span>Figure : Sample Registry Information (REDACTED)

![](xwb-1-1-73-user-guide/032.png)

### Syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two versions of the GetServerInfo function are supported:

- Legacy Version—Retrieves the end user’s server and port:

function GetServerInfo(var Server, Port: string): integer;

- New Version—Retrieves the end user’s server and port as well as the SSHUsername value from the Windows registry:

function GetServerInfo(var Server, Port, SSHUsername: string): integer;

Both versions continue to support specification of SSHUsername at the command line.

![](xwb-1-1-73-user-guide/033.png) NOTE: The unit is RpcConf1.

## VistA Splash Screen Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two procedures in SplVista.PAS unit are provided to display a VistA splash screen when an application loads:

- procedure SplashOpen;
- procedure SplashClose(TimeOut: longint);

It is *recommended* that the splash screen be opened and closed in the section of Pascal code in an application’s project file (i.e., .DPR).

To use the splash screen in an application, perform the following procedure:

1.  Open your application’s project (.DPR) file (in Delphi, choose View \| Project Source).
24. Include the SplVista in the uses clause of the project source.
25. Call SplashOpen immediately after the first form of your application is created and call SplashClose just prior to invoking the Application.Run method.
26. Use the TimeOut parameter to ensure a minimum display time.

<span id="_Ref449357395" class="anchor"></span>Figure : VistA Splash Screen

![](xwb-1-1-73-user-guide/034.png)

<span id="_Toc202777932" class="anchor"></span>Figure : Displaying a VistA Splash Screen: Sample Code

uses

Forms, Unit1 in ‘Unit1.pas’, SplVista;

*{\$R \*.RES}*begin

Application.Initialize;

Application.CreateForm(TForm1, Form1);

SplashOpen;

SplashClose(2000);

Application.Run;

end.

## XWB GET VARIABLE VALUE RPC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can call the XWB GET VARIABLE VALUE RPC (distributed with the RPC Broker) to retrieve the value of any M variable in the server environment. Pass the variable name in Param\[0\].Value and the type (reference) in Param\[0\].PType. Also, the current context of your user *must* give them permission to execute the XWB GET VARIABLE VALUE RPC (it *must* be included in the RPC multiple of the “B”-type option registered with the CreateContext function). For example:

<span id="_Toc202777933" class="anchor"></span>Figure : XWB GET VARIABLE VALUE RPC Usage—Sample Code

RPCBroker1.RemoteProcedure := ‘XWB GET VARIABLE VALUE’;

RPCBroker1.Param\[0\].Value :=‘DUZ’;

RPCBroker1.Param\[0\].PType := reference;

try

RPCBroker1.Call;

exceptOn EBrokerError do

ShowMessage(‘Connection to server could not be established!’);

end;

ShowMessage(‘DUZ is ‘+RPCBroker1.Results\[0\]);

![](xwb-1-1-73-user-guide/035.png) CAUTION: For enhanced security reasons, the reference parameter type may be deprecated and removed in subsequent updates to the BDK.

## M Emulation Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Piece Function

The Piece function is a scaled down Pascal version of M’s \$PIECE function. It is declared in MFUNSTR.PAS.

function Piece(x: string; del: string; piece: integer) : string;

### Translate Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Translate function is a scaled down Pascal version of M’s \$TRANSLATE function. It is declared in MFUNSTR.PAS.

function Translate(passedString, identifier, associator: string): string;

## Encryption Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel and the RPC Broker provide some rudimentary encryption and decryption functions. Data can be encrypted on the client end and decrypted on the server, and vice-versa.

### In Delphi

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Include HASH in the “uses” clause of the unit in which you’ll be encrypting or decrypting.

Function prototypes are as follows:

- function Decrypt(EncryptedText: string): string;
- function Encrypt(NormalText: string): string;

### On the VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Encryption

To encrypt:

<span id="_Toc202777934" class="anchor"></span>Figure : Encryption in VistA M Server—Sample Code

\><span class="mark">S CIPHER=\$\$ENCRYP^XUSRB1(“Hello world!”) W CIPHER</span>

/U’llTG~TVl&f-

#### Decryption

To decrypt:

<span id="_Toc202777935" class="anchor"></span>Figure : Decryption in VistA M Server—Sample Code

\><span class="mark">S PLAIN=\$\$DECRYP^XUSRB1(CIPHER) W PLAIN</span>

Hello world!

## \$\$BROKER^XWBLIB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the \$\$BROKER^XWBLIB function in the M code called by an RPC to determine if the Broker is executing the current process. It returns:

- 1—If this is True.
- 0—If False.

## \$\$RTRNFMT^XWBLIB

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the \$\$RTRNFMT^XWBLIB function in the M code called by an RPC to change the return value type that the RPC returns on-the-fly. This allows you to change the return value type to any valid return value type (Single Value, Array, Word-Processing, Global Array, or Global Instance). It also lets you set WORD WRAP ON (#.08) field to True or False, on-the-fly, for the RPC.

![](xwb-1-1-73-user-guide/036.png) REF: For more information about \$\$RTRNFMT^XWBLIB, see the *RPC Broker Developer’s Guide.*

# Broker Security Enhancement (BSE)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the mechanism by which the Broker Security Enhancement (BSE) enables RPC Broker Delphi-based applications to make remote user/visitor connections in a more secure manner. This BSE-based mechanism subsequently replaces the current Compensation And Pension Records Interchange (CAPRI)-based mechanism for remote user/visitor access by RPC Broker Delphi-based client/server applications.

The Veterans Health Administration (VHA) information systems management and user community has expressed a need to secure access to patient information at remote sites.

Some VistA application users require access to data located at remote sites at which the users:

- Do *not* have assigned Access and Verify codes.
- Have *not* been entered into the NEW PERSON (#200) file by system administrators.
- Want to avoid having multiple Access/Verify code pairs.

The Compensation And Pension Records Interchange (CAPRI) application was the first application with these requirements. This application is used by Veterans Benefits Administration (VBA) staff to remotely access VistA data related to claims for veterans treated at any VistA site.

The CAPRI application was the first application to use the modified version of the VistA Remote Procedure Call (RPC) Broker software, which was based on the Remote Data Views (RDV) access method, as a means for obtaining such access. This access enters the user's information into the NEW PERSON (#200) file as a visitor but does *not* require an Access or Verify code for the user at the remote site. As a result of the CAPRI application, there has been an increase in the number of other applications that also require or are requesting this type of remote data access.

The goal of the Broker Security Enhancement (BSE) Project is to accomplish the following:

- Enable RPC Broker Delphi-based applications to access Remote VistA M Servers with increased security.
- Enhance the RPC Broker method used to connect to Remote VistA M Servers.
- Ensure correct information for user access to prevent the mistaken identification of an incorrect or non-existent user (spoofing) via unauthorized applications.
- Provide the ability for RPC Broker Delphi-based applications that have implemented BSE to specify their own context option.
- Allow the VistA Imaging Display Client to pull in images from remote sites without requiring credentials on the Remote VistA M Servers.

### Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Broker Security Enhancement (BSE) Project provides the following features and functionality:

- Adds a step to the RPC Broker signon process to authenticate the connecting application. This also involves passing a secret encoded phrase that is established on the VistA M Server via a patch and KIDS build.
- Adds a step to the RPC Broker signon process on the Remote VistA M Server to authenticate the user by connecting back to the Authenticating VistA M Server.
- Provides the capability for remote applications to specify their own context option.

### Architectural Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The architectural scope of BSE is as follows:

- Use of Kernel Authentication—Kernel is used as the authenticator. Kernel is a valid means of authenticating on a backend VistA M Server.
- Client/Server-based Application Support—This document only discusses the BSE functionality provided with VistA RPC Broker Delphi-based client/server applications.

## Process Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The overall process to make a remote connection via an RPC Broker Delphi-based client/server application that has implemented the Broker Security enhancement (BSE) is as follows:

1.  The user starts the BSE-enabled application.
1.  The BSE-enabled application connects to the Authenticating VistA M Server and presents the VistA login GUI dialogue to the user.

![](xwb-1-1-73-user-guide/037.png) NOTE: The Authenticating VistA M Server is identified in the CALLBACKSERVER (#.03) field in the CALLBACKTYPE (#1) Multiple field in the REMOTE APPLICATION (#8994.5) file.

2.  The user enters their Kernel Access and Verify codes, is authenticated via Kernel, and is signed onto the BSE-enabled application's Authenticating VistA M Server.
3.  The BSE-enabled application gets a Kernel Authentication Token for the authenticated user from the Authenticating VistA M Server. This token is eventually used by the Remote VistA M Server to obtain the necessary user information for populating a user as a "visitor" entry in the remote site's NEW PERSON (#200) file. This ensures the following:
- The user is *not* spoofed.
- The data at the remote site is valid.

A sample Kernel Authentication Token follows:

XWBHDL977-124367_0

4.  The BSE-enabled application completes any other processing necessary to identify the Remote VistA M Server and gathers any other required information.
5.  The BSE-enabled application disconnects from the Authenticating VistA M Server.
6.  <span id="process_overview_step_07" class="anchor"></span>The BSE-enabled application performs the following tasks:
1.  <span id="process_overview_step_07a" class="anchor"></span>Creates a Security Pass Phrase value that is composed of the following two pieces of data:
- Security Phrase—A one-way hashed value that is stored in the REMOTE APPLICATION (#8994.5) file and used to identify the BSE-enabled application's file entry.

![](xwb-1-1-73-user-guide/038.png) REF: For more information on the Security Phrase, see the "<u>Security Phrase</u>" section.

- Kernel Authentication Token
4.  <span id="process_overview_step_07b" class="anchor"></span>Sets the SecurityPhrase property of the RPCBroker login component to the Security Pass Phrase value (see [Step 7a](#process_overview_step_07a)), which is later used by the Remote VistA M Server to call back the Authenticating VistA M Server.
5.  Sets the other appropriate RPCBroker login component properties in order to call the Remote VistA M Server.

![](xwb-1-1-73-user-guide/039.png) REF: For more information on the specific RPCBroker login component property settings, see the "Step-By-Step Procedures to Implement BSE" section in the *RPC Broker Developer’s Guide*.

7.  The BSE-enabled application connects to the Remote VistA M Server with the RPCBroker login component passing in the encoded value of the SecurityPhrase property (see [Step 7](#process_overview_step_07)).

![](xwb-1-1-73-user-guide/040.png) CAUTION: Remote access is only permitted at sites that have installed the application's information (including the hashed Security Phrase) into the REMOTE APPLICATION (#8994.5) file, ensuring that a rogue application *cannot* obtain access.

![](xwb-1-1-73-user-guide/041.png) REF: For more information on the application's Security Phrase, see the "<u>Security Phrase</u>" section.

8.  The Kernel software on the Remote VistA M Server performs the following tasks:
1.  Identifies and hashes the decoded value of the RPCBroker login component's SecurityPhrase property (see Steps [7a](#process_overview_step_07a) and [7b](#process_overview_step_07b)).
6.  Uses the hashed value of the BSE-enabled application's Security Pass Phrase to identify the application's entry in the REMOTE APPLICATION (#8994.5) file.

![](xwb-1-1-73-user-guide/042.png) NOTE: Included in that entry is the mechanisms for contacting the Authenticating VistA M Server.

7.  Connects to the Authenticating VistA M Server passing in the Kernel Authentication Token that identifies the user.
8.  Obtains the user demographic information from the Authenticating VistA M Server. This user demographic information is used to establish the user as a remote user/visitor.
9.  Disconnects from the Authenticating VistA M Server.
10. Uses the demographic information obtained from the Authenticating VistA M Server to set up the user as a visitor entry on the Remote VistA M Server. It creates or matches an entry in the NEW PERSON (#200) file and provides the visitor with the context option specified for the BSE-enabled application in the REMOTE APPLICATION (#8994.5) file.
9.  The BSE-enabled application is notified by the RPCBroker login component that it successfully connected, and that the user is signed on to the Remote VistA M Server. The user can then continue with any processing necessary on the Remote VistA M Server. If for some reason the user signon fails on the Remote VistA M Server, the user is prompted to enter a valid Access and Verify code on the Remote VistA M Server. If the user cancels the signon, he/she is prompted with a signon cancellation dialogue box.

![](xwb-1-1-73-user-guide/043.png) REF: For more information on the REMOTE APPLICATION (#8994.5) file, see the "<u>REMOTE APPLICATION (#8994.5) File</u>" section.

If any of the following error conditions exist, the user is prompted with a regular GUI signon dialogue instructing them to enter their Access and Verify codes:

- No entry for the application in the REMOTE APPLICATION (#8994.5) file.
- No match for the Kernel Authentication Token on the Authenticating VistA M Server.
- Cannot connect to the Authenticating VistA M Server.

The Remote VistA M Server connects to the Authenticating VistA M Server and passes in the Kernel Authentication Token identifying the user. The Authenticating VistA M Server responds back by returning the demographic information necessary to establish the user as a remote user. The Remote VistA M Server disconnects from the Authenticating VistA M Server and sets up the user's profile as a visitor entry, including the necessary context option specified for the application in the REMOTE APPLICATION (#8994.5) file.

The BSE-enabled application is notified that the user is signed on and continues processing as normal.

<u>Table 8</u> lists the two classes of applications that use this BSE authentication mechanism:

<table>
<caption><p><span id="_Ref73867751" class="anchor"></span>Table : BSE—Software Applications and Modules</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Application Class</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Single Server Authentication</td>
<td><p>Applications that require users to authenticate against a single VistA M Server and determine the remote locations to be accessed (e.g., CAPRI).</p>
<p>For those applications where the users all authenticate on a single VistA M Server, the application only needs to specify the Uniform Resource Locator (URL) for its VistA M Server and one or more methods for connecting to it (including port number[s]) in the CALLBACKTYPE Multiple of the REMOTE APPLICATION (#8994.5) file.</p></td>
</tr>
<tr class="even">
<td>Multiple Server Authentication</td>
<td><p>Applications that require users to authenticate at their local medical center or other site (e.g., VistAWeb or other Web-based applications).</p>
<p>For those applications where each user authenticates on multiple/different VistA M Servers, the application needs to obtain both a Kernel Authentication Token and the demographic data necessary for identifying or adding a remote user/visitor during the authentication process on the Authenticating VistA M Server. The application passes in the Kernel Authentication Token and application Security Pass Phrase, as described above (see the "<u>Process Overview</u>" topic). The REMOTE APPLICATION (#8994.5) file contains an address for the Web-based application and the Remote VistA M Server returns the Kernel Authentication Token to the application and expects it to return the demographic information associated with that Kernel Authentication Token. This requires the application to keep the Kernel Authentication Token and demographic data in a location that is accessible by the application until the demographic data has been provided to the Remote VistA M Server.</p>
<p>![](xwb-1-1-73-user-guide/044.png) <strong>RECOMMENDATION:</strong> VistA Infrastructure (VI) <strong>highly encourages that other <em>non</em>-Web-based applications use a single server rather than multiple servers for user authentication.</strong></p></td>
</tr>
</tbody>
</table>

<span id="_Ref73867751" class="anchor"></span>Table : BSE—Software Applications and Modules

### Process Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 14</u> illustrates the BSE process sequence flow:

<span id="_Ref468113580" class="anchor"></span>Figure : BSE—Process Sequence Flow Diagram

![](xwb-1-1-73-user-guide/045.png)

<u>Figure 15</u> illustrates the BSE process overview:

<span id="_Ref468113643" class="anchor"></span>Figure : BSE—Process Overview

![](xwb-1-1-73-user-guide/046.png)

## BSE-related VistA Applications and Modules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the new or modified functionality made to the BSE-related software applications and modules as listed in <u>Table 9</u>.

An RPC Broker Delphi-based and BSE-enabled VistA application comprises software that has been re-compiled using the RPCBroker login component, modified for BSE. BSE capability comes into play when you are using a BSE-enabled application (e.g., Compensation And Pension Records Interchange \[CAPRI\] or VistAWeb).

![](xwb-1-1-73-user-guide/047.png) REF: For information on how to implement BSE in VistA RPC Broker Delphi-based client/server applications, see the "Implementing BSE in VistA RPC Broker-based Applications," in the *RPC Broker Developer’s Guide*.

This section discusses in more detail the various software applications and modules that, together, provide for BSE functionality:

<table>
<caption><p><span id="_Ref473019702" class="anchor"></span>Table : Fields in the REMOTE APPLICATION (#8994.5) File</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 58%" />
</colgroup>
<thead>
<tr class="header">
<th>Application/Module</th>
<th>Location</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VistA M Server</td>
<td>VistA M Server</td>
<td><p>This is the "backend server" where the Kernel and RPC Broker software act as the authentication source for all VistA applications (i.e., client/server, rich client, Web, and roll-and-scroll applications). The VistA M Server also executes remote procedure calls (RPCs) and provides other functions to VistA applications.</p>
<p>![](xwb-1-1-73-user-guide/048.png) <strong>REF:</strong> For a list of BSE-related Vista M Server patches, see the “BSE Installation Instructions for Developers” section in the <em>RPC Broker Developer’s Guide</em>.</p></td>
</tr>
<tr class="even">
<td>Client/Server Login Component: RPC Broker</td>
<td>Client<br />
(Developer workstations only)</td>
<td><p>The <strong>RPCBroker</strong> login component allows client/server applications to authenticate against the VistA M Server and obtain a persistent connection over which remote procedure calls (RPCs) are executed. This component is modified in BSE to be more secure when accessing data at remote sites.</p>
<p>RPC Broker-based applications using remote or visitor access (e.g., Compensation And Pension Records Interchange [CAPRI], VistAWeb) <em>must</em> invoke this modified <strong>RPCBroker</strong> login component to implement the Broker Security Enhancement (BSE).</p></td>
</tr>
</tbody>
</table>

<span id="_Ref473019702" class="anchor"></span>Table : Fields in the REMOTE APPLICATION (#8994.5) File

![](xwb-1-1-73-user-guide/049.png) REF: For the specific software patches required for the implementation of BSE, see the “BSE Installation Instructions for Developers” section in the *RPC Broker Developer’s Guide*.

## Kernel—Authentication Interface to VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Authentication is the process of verifying a user identity to ensure that the person requesting access to a VistA system (e.g., clinical information system) is, in fact, that person to whom entry is authorized.

Currently, Kernel on the VistA M Server is the approved method to provide both Authentication and Authorization (AA) services for all VistA applications Kernel was assessed as the most straightforward and timely approach to also be used for remote signon authentication in BSE. By using Kernel as the authenticator for BSE, the NEW PERSON (#200) file continues to serve as the single user data store for VistA and BSE.

Some potential advantages to employing Kernel as the AA source include the following:

- Ease of file maintenance by system administrators.
- Provides a single point of user management for existing and new VistA RPC Broker Delphi-based applications.
- Allows the use of an existing credential (i.e., the Access and Verify code) for Authentication and Authorization, rather than introducing a new security credential.
- Ease of coding requirements by application developers.
- Avoids an additional user store, which simplifies the migration to any future AA solutions.

The BSE functionality for Kernel was introduced with Kernel Patch XU\*8.0\*404 (server-side). The BSE functionality includes the creation of a Kernel Authentication Token. The Kernel Authentication Token is generated once a user has been initially authenticated on the Authenticating VistA M Server via their Access and Verify codes. This Kernel Authentication Token can then be used to authenticate a user on a Remote VistA M Server.

## RPC Broker

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker software consists of both a client and server software piece.

### Client

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPCBroker login component is embedded in a Embarcadero Delphi-based rich client/server application (e.g., Compensation And Pension Records Interchange \[CAPRI\]). The RPCBroker login component is used to connect the application running on a Microsoft Windows client workstation to the VistA M Server. This connection allows data retrieval from the VistA M Server database. The RPCBroker login component uses Kernel's Access and Verify codes to authenticate a user to VistA.

The BSE functionality for the RPCBroker login component was introduced with RPC Broker Patch XWB\*1.1\*45 (client-side) and Kernel Patch XU\*8.0\*404 (server-side). BSE functionality includes the addition of a property to the RPCBroker login component that allows applications to pass an application's Security Phrase and Kernel Authentication Token, which is referred to in this documentation as the Security Pass Phrase. Thus, when a VistA RPC Broker Delphi-based application, such as CAPRI, is recompiled with the BSE-updated RPCBroker login component and other required code modifications are made, that application would then become capable of accessing Remote VistA M Servers without requiring users to re-enter their Access and Verify codes.

### Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In order to implement BSE and use the RPC-Broker callback type, the central Authenticating VistA M server *must* run the RPC Broker as a TCPIP service. The *Non*-callback RPC Broker Listener/TCPIP service is distributed and described with RPC Broker Patch XWB\*1.1\*35 and was updated with XWB\*1.1\*44.

![](xwb-1-1-73-user-guide/050.png) REF: For more information on the RPC Broker and TCPIP service setup, see the RPC Broker Patches XWB\*1.1\*35 and 44 on FORUM and the RPC Broker documentation, specifically the *RPC Broker TCP/IP Supplement*, located on the VDL at the following Web address: <http://www.va.gov/vdl/application.asp?appid=23>

![](xwb-1-1-73-user-guide/051.png) REF: For more detailed information on the application developer procedures and code modifications needed to implement BSE in RPC Broker Delphi-based applications, see the "Implementing BSE in VistA RPC Broker-based" section in the *RPC Broker Developer’s Guide*.

## REMOTE APPLICATION (#8994.5) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The REMOTE APPLICATION (#8994.5) file was released with RPC Broker Patch XWB\*1.1\*45. This file helps better secure remote user/visitor access to Remote VistA M Servers initiated by RPC Broker Delphi-based GUI applications. Remote user/visitor access permits applications where users need to access a large number of sites and do so *without* requiring separate Access and Verify codes at each target remote site.

The REMOTE APPLICATION (#8994.5) file contains the fields listed in <u>Table 10</u>:

<table>
<caption><p><span id="_Ref473019959" class="anchor"></span>Table : Header Files that Provide Correct Declarations for DLL Functions</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Field Name</th>
<th>Field Number</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME</td>
<td>.01</td>
<td>(required) This is the name for the RPC Broker Delphi-based application that requires remote user/visitor access. The name <em>must</em> be from <strong>3</strong> to <strong>30</strong> characters, not numeric or starting with punctuation.</td>
</tr>
<tr class="even">
<td>CONTEXTOPTION</td>
<td>.02</td>
<td>(required) This is the name of the context option (i.e., client/server or "<strong>B</strong>"-type option) that the application users need. The name <em>must</em> be from <strong>3</strong> to <strong>45</strong> characters. The user is signed on as a visitor and given this context option as a secondary menu option.</td>
</tr>
<tr class="odd">
<td>APPLICATIONCODE</td>
<td>.03</td>
<td><p>(required) This is the hashed value for an application's Security Phrase.</p>
<p>![](xwb-1-1-73-user-guide/052.png) <strong>REF:</strong> For more information on the Security Phrase, see the "<u>Security Phrase</u>" section.</p></td>
</tr>
<tr class="even">
<td>CALLBACKTYPE</td>
<td>1</td>
<td>(required) This is a Multiple field. It can contain multiple values describing the mechanisms by which the Remote VistA M Server can contact the application's Authenticating VistA M Server to obtain the demographic information. It consists of the subfields described below.</td>
</tr>
<tr class="odd">
<td>CALLBACKTYPE<br />
(CALLBACKTYPE Multiple)</td>
<td>.01</td>
<td><p>(required) This field indicates the mechanisms by which the server should contact the Authenticating VistA M Server to obtain information necessary to sign the current user onto the current server. The values for this field are:</p>
<ul>
<li><p><strong>R—</strong>RPC Broker TCP/IP connection</p></li>
<li><p><strong>M—</strong>M-to-M Broker connection</p></li>
<li><p><strong>H—</strong>HyperText Transport Protocol (HTTP) connection</p></li>
<li><p><strong>S—</strong>Station-number callback</p></li>
</ul></td>
</tr>
<tr class="even">
<td>CALLBACKPORT<br />
(CALLBACKTYPE Multiple)</td>
<td>.02</td>
<td>(required) This is the port number (<strong>3 - 5</strong> characters) to be used for the callback connection to the Authenticating VistA M Server for the CALLBACKTYPE (#.01) specified.</td>
</tr>
<tr class="odd">
<td>CALLBACKSERVER<br />
(CALLBACKTYPE Multiple)</td>
<td>.03</td>
<td>(required) This is the server designation (address) to be used for the callback to the Authenticating VistA M Server for the CALLBACKTYPE (#.01) specified. This should be a Domain Name Service (DNS) name-based address rather than an Internet Protocol (IP) address, because IP addresses can change. It should be a server name ending in <strong>&lt;REDACTED&gt;.VA.GOV</strong> or <strong>&lt;REDACTED&gt;.VA.GOV</strong>. The DNS servers resolve the name, and thus, ensure that the site is a valid VistA M Server.</td>
</tr>
<tr class="even">
<td>URLSTRING<br />
(CALLBACKTYPE Multiple)</td>
<td>.04</td>
<td><p>(optional) This field holds the text that should follow the SERVER ADDRESS (#.03) field for HTTP connections to obtain the information for the Kernel Authentication Token passed in for a REMOTE APPLICATION connection.</p>
<p>If the complete Uniform Resource Locator (URL) to be used for the callback is:</p>
<p>http://&lt;REDACTED&gt;.va.gov/some/kind/of/location/<br />
somePage.aspx</p>
<p>The CALLBACKSERVER (#.03) field could be:</p>
<p>&lt;REDACTED&gt;.va.gov</p>
<p>and the URLSTRING would be:</p>
<p>some/kind/of/location/somePage.aspx</p>
<p>This field is only used if the CALLBACKTYPE filed (#.01) value is <strong>H</strong> for HTTP.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref473019959" class="anchor"></span>Table : Header Files that Provide Correct Declarations for DLL Functions

![](xwb-1-1-73-user-guide/053.png) REF: For more information on the REMOTE APPLICATION (#8994.5) file, see the "Files" section in the *RPC Broker Technical Manual*.

## Security Phrase

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Security Phrase is an RPC Broker Delphi-based application's entry into the REMOTE APPLICATION (#8994.5) file. The Security Phrase is a general phrase that is known only to the application that created it. When it is stored in the REMOTE APPLICATION (#8994.5) file, it *must* be hashed. This one-way hashed value, which is the result of a call to the \$\$EN^XUSHSH(phrase) API, is entered into the APPLICATIONCODE (#.03) field in the REMOTE APPLICATION (#8994.5) file for the application.

This Security Phrase is combined with the Kernel Authentication Token to make up the Security Pass Phrase, which is then stored in the SecurityPhrase property of the RPCBroker login component.

![](xwb-1-1-73-user-guide/054.png) CAUTION: It is important to realize that the Security Phrase identifies only those applications that are authorized to perform remote user/visitor access. Thus, the stored value of the Security Phrase is a one-way hash so that other rogue applications *cannot* mimic an application and access the Remote VistA M Server.

![](xwb-1-1-73-user-guide/055.png) RECOMMENDATION: Since the Security Phrase is the application's identifier, VistA Infrastructure (VI) *recommends* developers identify the Security Phrase as a const value in an include file in any RPC Broker Delphi-based program implementing BSE. A substitute include file containing a phrase similar to the Security Phrase should then be included with release of the source code.

## Kernel Authentication Token

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel Authentication Token is generated by the same code used to generate handles (i.e., a unique text string that is used to identify a specific user for which it was generated) for other purposes used in the RPC Broker software. Once created, the token is stored in the ^XTMP temporary global. The basic format of the token (handle) is as follows:

XWBHDL*nnn*-*nnnnnn*\_*n*

The "XWBHDL" indicates that it is an RPC Broker handle; where "XWB" is the RPC Broker namespace and "HDL" indicates that it is a handle.

The following is an example of a Kernel Authentication Token:

XWBHDL977-124367_0

# Debugging and Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## How to Debug Your Client Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Beside the normal debugging facilities provided by Delphi, you can also invoke a debug mode, so that you can step through your code on the client side and your RPC code on the M server side simultaneously.

To invoke the debug mode, perform the following procedure:

1.  On the client side, set the DebugMode property on the TRPCBroker component to True.
27. Switch over to the VistA M Server and set any break points in the routines being called in order to help isolate the problem.
28. Issue the M debug command (e.g., ZDEBUG) or follow instructions in the InterSystems Caché documentation on “Debugging with the Caché Debugger.”
29. Start the following VistA M Server process:

\>D DEBUG^XWBTCPM

30. <span id="debug_step_05" class="anchor"></span>Enter a unique Listener port number (i.e., a port number *not* in general use).
31. Switch over to the client application and connect the client application to the VistA M Server using the server’s IP address and the port number you entered [Step 5](#debug_step_05).
32. You can now step through the code on your client and simultaneously step through the code on the VistA M Server side for any RPCs that your client calls.

### RPC Error Trapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

M errors on the VistA M Server that occur during RPC execution are trapped by the use of M and Kernel error handling. In addition, the M error message is sent back to the Delphi client. Delphi raises an exception EBrokerError and a popup box displaying the error. At this point, RPC execution terminates, and the channel is closed.

## Troubleshooting Connections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Identifying the Listener Process on the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On InterSystems Caché systems, where the Broker Listener is running and the System Status \[XUSTATUS\] menu option is available, the Listener process name is:

\|TCP\|*\####*

Where *\####* is the port number being listened to. This should help quickly locate Listener processes when troubleshooting any connection problems.

On systems with greater security or with listener processes started by Linux xinetd.d scripts, the following commands can be helpful:

- List all xinetd.d scripts:

\>!ls –al /etc/xinetd.d

- List xinetd.d scripts containing string “vis”:

\>!ls –al/etc/xinetd.d \| grep vis

- Display script “vis_rpct”:

\>!cat /etc/xinetd.d/vis_rpct

- Look for listener running on port \<REDACTED\>:

\>!netstat –an \| grep :\<REDACTED\>

### Identifying the Handler Process on the Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On InterSystems Caché systems the name of a Handler process for IPv4 is:

\|TCP\|*nnn*.*nnn*.*nnn*.*nnn*: \####

Where *nnn.nnn.nnn.nnn* is the client IPv4 address and *\####* is the port number.

Alternatively, for IPv6:

\|TCP\|*hhhh*:*hhhh*::*hhhh*:####

Where *hhhh* represents the hexadecimal segments of the client IPv6 address and *\####* is the port number.

### Testing Your RPC Broker Connection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To test the RPC Broker connection from your workstation to the M Server, use the RPC Broker Diagnostic Program (rpctest.exe).

![](xwb-1-1-73-user-guide/056.png) REF: For a complete description of the RPC Broker Diagnostic program, see the “Troubleshooting” chapter in the *RPC Broker Systems Management Guide*.

# RPC Broker and Delphi

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections highlight changes made to or comments about the RPC Broker to accommodate a particular version of Delphi.

![](xwb-1-1-73-user-guide/057.png) RECOMMENDATION: To avoid problems with the BDK, it is *recommended* for all Delphi packages that you accept the default directory after compiling the Broker Development Kit (BDK) on a workstation.

## Delphi 10.4, 10.3, 10.2, 10.1, 10.0, and XE8 Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Delphi *Starter* Edition—*Not* Recommended for BDK Development

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Delphi 10.4, 10.3, 10.2, 10.1, 10.0, and XE8 comes in three flavors:

- Starter
- Professional
- Enterprise

![](xwb-1-1-73-user-guide/058.png) RECOMMENDATION: It is *recommended* that you use either the Professional or Enterprise version of Delphi to develop applications using the RPC Broker.

This version of the BDK requires the Professional or Enterprise Edition. The Starter editions are targeted mainly at students, and as such, leave out many features. We do *not* recommend using any of the Starter editions of Delphi for RPC Broker development at this time. Delphi Starter Edition does *not* ship the following:

- OpenHelp help system—Allow easy integration of 3<sup>rd</sup> party component help with Delphi’s own internal component help.
- VCL source code unit (i.e., dsgnintf.pas file)—RPCBroker component has a dependency on a VCL source code unit. Delphi Starter Editions do *not* ship VCL source code unit in either .PAS or .DCU form; however, VCL Source code units are available in Delphi Professional and Enterprise editions.

![](xwb-1-1-73-user-guide/059.png) NOTE: When installing Delphi Professional or Enterprise editions, make sure you leave the VCL Source installation option selected.

### XWB_RXE*\#*.bpl File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This RunTime package contains the source code for the standard RPCBroker components and is found in the following directory after compiling the Broker Development Kit (BDK) on a workstation. Shown are the default paths for various versions of Delphi, where *\#* represents the version number. If you have changed any default paths, your files may be in a different location:

- C:\Users\Public\Public Documents\Embarcadero\Studio\16.0\Bpl\\XWB_RXE8.bpl
- C:\Users\Public\Public Documents\Embarcadero\Studio\17.0\Bpl\\XWB_RunTime.bpl
- C:\Users\Public\Public Documents\Embarcadero\Studio\18.0\Bpl\\XWB_RunTime.bpl

### XWB_DXE*\#*.bpl File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This DesignTime package contains the installed components for the standard RPCBroker and is found in the following directory after compiling the Broker Development Kit (BDK) on a workstation. Shown are the default paths for various versions of Delphi, where \# represents the version number. If you have changed any default paths, your files may be in a different location:

- C:\Users\Public\Public Documents\Embarcadero\Studio\16.0\Bpl\\XWB_DXE8.bpl
- C:\Users\Public\Public Documents\Embarcadero\Studio\17.0\Bpl\\XWB_DesignTime.bpl
- C:\Users\Public\Public Documents\Embarcadero\Studio\18.0\Bpl\\XWB_DesignTime.bpl

# RPC Broker Dynamic Link Library (DLL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## DLL Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RPC Broker provides a Dynamic Link Library (DLL) interface, which acts like a “shell” around the Delphi TRPCBroker component. The DLL is contained in the BAPI32.DLL file.

The DLL interface enables client applications, written in any language that supports access to Microsoft Windows DLL functions, to take advantage of all features of the TRPCBroker component. This allows programming environments other than Embarcadero Delphi to make use of the TRPCBroker component. All of the communication to the server is handled by the TRPCBroker component, accessed via the DLL interface.

The DLL interface has *not* been updated to support Secure Shell (SSH) or IPv4/IPv6 dual-stack environments.

### Exported Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The complete list of functions exported in the DLL is provided in the BDK *RPC Broker Developer’s Guide.* Functions are provided in the DLL for:

- Creating and destroying RPC Broker components.
- Setting and retrieving RPC Broker component properties.
- Executing RPC Broker component methods.

### Header Files Provided

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 11</u> lists the header files that provide correct declarations for DLL functions:

| Language     | Header File |
|--------------|-------------|
| C            | BAPI32.H    |
| C++          | BAPI32.HPP  |
| Visual Basic | BAPI32.BAS  |

<span id="_Toc202777938" class="anchor"></span>Table : TRPCBroker Component’s Results Property

### Return Values from RPCs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Results from an RPC executed on an M server are returned as a text stream. This text stream may or may *not* have embedded \<CR\>\<LF\> character combinations.

When you call an RPC using the TRPCBroker component for Delphi, the text stream returned from an RPC is automatically parsed and returned in the TRPCBroker component’s Results property as follows:

<table>
<caption><p><span id="_Ref467590751" class="anchor"></span>Table : Glossary of Terms and Acronyms</p></caption>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th>Results Stream Contains &lt;CR&gt;&lt;LF&gt; Combinations</th>
<th>Results Location/Format<br />
(assumes RPC’s WORD WRAP ON field is True if RPC is Global Array or Word-processing type)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Yes</td>
<td>Results nodes; split based on <strong>&lt;CR&gt;&lt;LF&gt;</strong> delimiter</td>
</tr>
<tr class="even">
<td>No</td>
<td><strong>Results[0]</strong></td>
</tr>
</tbody>
</table>

<span id="_Ref467590751" class="anchor"></span>Table : Glossary of Terms and Acronyms

When you call an RPC using the DLL interface, the return value is the unprocessed text stream, which may or may *not* contain \<CR\>\<LF\> combinations. It is up to you to parse out what would have been individual Results nodes in Delphi, based on the presence of any \<CR\>\<LF\> character combinations in the text stream.

### COTS Development and the DLL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Broker DLL serves as the gateway to the REMOTE PROCEDURE (#8994) file for *non*-Delphi client/server applications. In order to use any RPCs *not* written specifically by the client application (e.g., CONSULTS FOR A PATIENT, USER SIGN-ON RPCs, or the more generic VA FileMan RPCs), you *must* call the RPC Broker DLL with input parameters defined and results accepted in the formats required by the RPC being called.

Therefore, to use the Broker DLL interface you *must* determine the following information for each RPC you plan to use:

- How does the RPC expect input parameters, if any, to be passed to it?
- Will you be able to create any input arrays expected by the RPC in the same format expected by the RPC?
- What does the results data stream returned by the RPC look like?

  
<span id="glossary" class="anchor"></span>Glossary

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
<td>BDK</td>
<td>Broker Development Kit.</td>
</tr>
<tr class="even">
<td>BSE</td>
<td>Broker Security Enhancement.</td>
</tr>
<tr class="odd">
<td>Client</td>
<td>A single term used interchangeably to refer to the user, the workstation, and the portion of the program that runs on the workstation. In an object-oriented environment, a client is a member of a group that uses the services of an unrelated group. If the client is on a local area network (LAN), it can share resources with another computer (server).</td>
</tr>
<tr class="even">
<td>Component</td>
<td>An object-oriented term used to describe the building blocks of GUI applications. A software object that contains data and code. A component may or may <em>not</em> be visible. These components interact with other components on a form to create the GUI user application interface.</td>
</tr>
<tr class="odd">
<td>DHCP</td>
<td><strong>D</strong>ynamic <strong>H</strong>ost <strong>C</strong>onfiguration <strong>P</strong>rotocol.</td>
</tr>
<tr class="even">
<td>DLL</td>
<td><p><strong>D</strong>ynamic <strong>L</strong>ink <strong>L</strong>ibrary. A DLL allows executable routines to be stored separately as files with a DLL extension. These routines are only loaded when a program calls for them. DLLs provide several advantages:</p>
<ul>
<li><p>Help save on computer memory, since memory is only consumed when a DLL is loaded. They also save disk space. With static libraries, your application absorbs all the library code into your application, so the size of your application is greater. Other applications using the same library also carry this code around. With the DLL, you do <em>not</em> carry the code itself; you have a pointer to the common library. All applications using it will then share one image.</p></li>
<li><p>Ease maintenance tasks. Because the DLL is a separate file, any modifications made to the DLL do not affect the operation of the calling program or any other DLL.</p></li>
<li><p>Help avoid redundant routines. They provide generic functions that can be used by a variety of programs.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>GUI</td>
<td><strong>G</strong>raphical <strong>U</strong>ser Interface. A type of display format that enables users to choose commands, initiate programs, and other options by selecting pictorial representations (icons) via a mouse or a keyboard.</td>
</tr>
<tr class="even">
<td>IAM</td>
<td>Identity and Access Management.</td>
</tr>
<tr class="odd">
<td>Icon</td>
<td>A picture or symbol that graphically represents an object or a concept.</td>
</tr>
<tr class="even">
<td>PIN</td>
<td>Personal Identification Number.</td>
</tr>
<tr class="odd">
<td>PKI</td>
<td>Public Key Encryption.</td>
</tr>
<tr class="even">
<td>Remote Procedure Call</td>
<td>A remote procedure call (RPC) is essentially M code that can take optional parameters to do some work and then return either a single value or an array back to the client application.</td>
</tr>
<tr class="odd">
<td>SAML</td>
<td>Security Assertion Markup Language. An XML-based industry standard for communicating identities over the Internet.</td>
</tr>
<tr class="even">
<td>Server</td>
<td>The computer where the data and the Business Rules reside. It makes resources available to client workstations on the network. In VistA, it is an entry in the OPTION (#19) file. An automated mail protocol that is activated by sending a message to a server at another location with the “<strong>S.server</strong>” syntax. A server’s activity is specified in the OPTION (#19) file and can be the running of a routine or the placement of data into a file.</td>
</tr>
<tr class="odd">
<td>SSH</td>
<td>Secure Shell.</td>
</tr>
<tr class="even">
<td>SSO/UC</td>
<td>Sign-On/User Context.</td>
</tr>
<tr class="odd">
<td>STS</td>
<td>Secure Token Service.</td>
</tr>
<tr class="even">
<td>User Access</td>
<td><p>This term is used to refer to a limited level of access to a computer system that is sufficient for using/operating software, but does not allow programming, modification to data dictionaries, or other operations that require programmer access. Any of VistA’s options can be locked with a security key (e.g., XUPROGMODE, which means that invoking that option requires programmer access).</p>
<p>The user’s access level determines the degree of computer use and the types of computer programs available. The Systems Manager assigns the user an access level.</p></td>
</tr>
<tr class="odd">
<td>User Interface</td>
<td>The way the software is presented to the user, such as Graphical User Interfaces that display option prompts, help messages, and menu choices. A standard user interface can be achieved by using Borland’s Delphi Graphical User Interface to display the various menu option choices, commands, etc.</td>
</tr>
<tr class="even">
<td>VistA</td>
<td>Veterans Health Information Systems and Technology Architecture.</td>
</tr>
<tr class="odd">
<td>Window</td>
<td>An object on the screen (dialogue) that presents information such as a document or message.</td>
</tr>
<tr class="even">
<td>XML</td>
<td>eXtensible Markup Language.</td>
</tr>
</tbody>
</table>

![](xwb-1-1-73-user-guide/060.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

  
<span id="_Toc82598488" class="anchor"></span>Index

\$

\$\$BROKER^XWBLIB, 26

\$\$EN^XUSHSH API, 39

\$\$RTRNFMT^XWBLIB, 27

^

^XTMP Global, 40

A

About this Version of the BDK, 1

Acronyms

Intranet Website, 49

APIs

\$\$BROKER^XWBLIB, 26

\$\$EN^XUSHSH, 39

\$\$RTRNFMT^XWBLIB, 27

APP PROXY ALLOWED (#.11) Field, 16

Application.Run Method, 24

APPLICATIONCODE (#.03) Field, 38, 39

Architectural Scope, 29

Assumptions, xix

Authentication

Interface to VistA

Kernel, 36

Kernel Authentication Token, 29, 31, 32, 36, 37, 39, 40

Sample, 30

B

Backward Compatibility Issues, 3

BAPI32.BAS File, 45

BAPI32.DLL File, 45

BAPI32.H File, 45

BAPI32.HPP File, 45

Broker

Component, 30, 31, 35, 36, 37, 39

Patches

XWB\*1.1\*45, 37

BrokerExample, 20

BROKEREXAMPLE.EXE, 20

BSE

Introduction, 28

Project Overview, 28

Scope, 29

VistA Applications/Modules, 35

Bypassing Security for Development, 19

C

C Language, 45

C++ Language, 45

Call Method, 6, 18

CALLBACKPORT (#.02) Field

CALLBACKTYPE (#1) Multiple Field, 38

CALLBACKSERVER (#.03) Field

CALLBACKTYPE (#1) Multiple Field, 29, 38

CALLBACKTYPE (#.01) Field

CALLBACKTYPE (#1) Multiple Field, 38

CALLBACKTYPE (#1) Multiple Field, 29, 38

CALLBACKPORT (#.02) Field, 38

CALLBACKSERVER (#.03) Field, 29, 38

CALLBACKTYPE (#.01) Field, 38

URLSTRING (#.04) Field, 39

Callout Boxes, xvi

Calls

Discrete, 17

Silent, 17

CAPRI, 28, 35, 37

ClearParameters Property, 5

ClearResults Property, 5

Commonly Used Terms, xvii

Compatibility Issues, 3

Components

RPC Broker, 30, 31, 35, 36, 37, 39

RPC Broker Components for Delphi, 4

RPCBroker, 35

TCCOWRPCBroker, 9

TRPCBroker, 4

TXWBRichEdit, 9

TXWSSOiToken, 10

Connect To, 22

Connected Property, 5

Connection

Testing Your RPC Broker Connection, 42

Contents, x

CONTEXTOPTION (#.02) Field, 38

COTS Development and the DLL, 46

Create Your Own RPCs

Preliminary Considerations, 11

Process, 12

CreateContext Method, 6, 19, 25

D

Data Dictionary

Data Dictionary Utilities Menu, xviii

Listings, xviii

DEBUG^XWBTCPM, 41

Debugging, 41

Error Trapping, 41

How to Debug Your Client Application, 41

Identifying

Handler Process on the Server, 42

Listener Process on the Server, 41

Testing Your RPC Broker Connection, 42

DebugMode Property, 41

DECRYP^XUSRB1, 26

Decrypt Method, 26

Decryption Functions, 26

Delphi, 43

Starter Edition, 43

Delphi Components

RPC Broker, 4

Demographics, 31, 32, 38

DI DDU Menu, xviii

Diagnostic Program, 42

DILIST Option, xviii

Disclaimers, xv

Software, xiv

Discrete Calls, 17

DLL

COTS Development and the DLL, 46

Exported Functions, 45

Header Files, 45

Interface, 45

Documentation

Revisions, ii

Symbols, xv

Documentation Conventions, xv

Documentation Navigation, xvii

Dynamic Link Library (DLL), 45

E

EBrokerError, 41

ENCRYP^XUSRB1, 26

Encrypt Method, 26

Encryption Functions, 26

Entry in the Remote Procedure File, 16

Error Message Handling, 41

Execute an RPC from a Client Application, How to, 17

Exported

DLL Functions, 45

F

Features, 29

Fields

APP PROXY ALLOWED (#.11), 16

APPLICATIONCODE (#.03), 38, 39

CALLBACKPORT (#.02)

CALLBACKTYPE (#1) Multiple Field, 38

CALLBACKSERVER (#.03)

CALLBACKTYPE (#1) Multiple Field, 29, 38

CALLBACKTYPE (#.01)

CALLBACKTYPE (#1) Multiple Field, 38

CALLBACKTYPE (#1) Multiple, 29, 38

CALLBACKPORT (#.02) Field, 38

CALLBACKSERVER (#.03) Field, 29, 38

CALLBACKTYPE (#.01) Field, 38

URLSTRING (#.04) Field, 39

CONTEXTOPTION (#.02), 38

NAME (#.01), 16, 38

PARAMETER TYPE (#8994.02,.02), 17

RETURN VALUE TYPE (#.04), 16

ROUTINE (#.03), 16

TAG (#.02), 16

URLSTRING (#.04)

CALLBACKTYPE (#1) Multiple Field, 39

WORD WRAP ON (#.08), 13, 16, 27

Figures, xii

Files

BAPI32.BAS, 45

BAPI32.DLL, 45

BAPI32.H, 45

BAPI32.HPP, 45

Header Files, 45

NEW PERSON (#200), 14, 28, 29, 31, 36

OPTION (#19), 12, 19

REMOTE APPLICATION (#8994.5), 29, 30, 31, 32, 38, 39

REMOTE PROCEDURE (#8994), 11, 12, 16, 46

SECURITY KEY (#19.1), 19

XWB_DXE*\#*.bpl, 44

XWB_RXE*\#*.bpl, 44

First Input Parameter for RPCs (Required), 12

Functions

Decryption, 26

Encryption, 26

Exported with DLL, 45

Piece, 25

Translate, 25

G

GetServerInfo Method, 5, 7, 22

Globals

^XTMP, 40

Glossary, 47

Intranet Website, 49

H

HASH, 26

Header Files, 45

Help

At Prompts, xviii

Online, xviii

Question Marks, xviii

History

Revisions, ii

Home Pages

Acronyms Intranet Website, 49

Adobe Website, xix

Glossary Intranet Website, 49

RPC Broker Website, xix

VA Software Document Library (VDL)

RPC Broker Home Page Web Address, 37

VA Software Document Library (VDL) Website, xix

How to

Connect to an M Server, 7

Debug Your Client Application, 41

Execute an RPC from a Client Application, 17

Obtain Technical Information Online, xviii

Register an RPC, 19

Use this Manual, xiv

I

Identifying

Handler Process on the Server, 42

Listener Process on the Server, 41

Input Parameter Types for RPCs (Optional), 15

Intended Audience, xiv

Interface

DLL, 45

Introduction, 1, 28

Issues

Backward Compatibility, 3

K

Kernel, 29, 36

Authentication

Interface to VistA, 36

Token, 29, 31, 32, 36, 37, 39, 40

Sample, 30

Patches

XU\*8.0\*404, 36

L

LAN, 47

List File Attributes Option, xviii

List PType, 15

ListenerPort Property, 5, 22

Literal PType, 15

lstCall Method, 6, 18

M

M Emulation Functions, 25

M Entry Points for RPC Examples, 15

Menus

Data Dictionary Utilities, xviii

DI DDU, xviii

System Status Menu, 41

XUSTATUS, 41

Message Handling, Errors, 41

Methods

Application.Run, 24

Call, 6, 18

CreateContext, 6, 19, 25

Decrypt, 26

Encrypt, 26

GetServerInfo, 5, 22

lstCall, 6, 18

SplashClose, 23, 24

SplashOpen, 23, 24

strCall, 6, 18

TRPCBroker Component, 4

MFUNSTR.PAS, 25

Microsoft Windows Registry, 8, 22

Mult Property, 15, 17

Multiple Server Authentication, 32

N

NAME (#.01) Field, 16, 38

NEW PERSON (#200) File, 14, 28, 29, 31, 36

O

Obtaining

Data Dictionary Listings, xviii

Online

Documentation, xviii

Technical Information, How to Obtain, xviii

Online Code Samples (RPCs), 20

OPTION (#19) File, 12, 19

Options

Data Dictionary Utilities, xviii

DI DDU, xviii

DILIST, xviii

List File Attributes, xviii

System Status Menu, 41

XUSTATUS, 41

Orientation, xiv

Other RPC Broker APIs, 22

P

Param Property, 5, 15, 17, 18

PARAMETER TYPE (#8994.02,.02) Field, 17

Parameters

TimeOut, 24

Patches

Revisions, ix

XU\*8.0\*404, 36

XWB\*1.1\*45, 37

Piece Function, 25

Process

Diagrams, 33

Overview, 29

Product Support (PS)

Anonymous Directories, xx

Programs

BROKEREXAMPLE.EXE, 20

Properties

ClearParameters, 5

ClearResults, 5

Connected, 5

DebugMode, 41

ListenerPort, 5, 22

Mult, 15, 17

Param, 5, 15, 17, 18

RemoteProcedure, 5, 18

Results, 5, 18

SecurityPhrase, 30, 31, 39

Server, 5, 22

SSHPort, 5

SSHPw, 5

SSHUser, 5, 22

SSHUseSecureConnection, 5

TRPCBroker Component, 4

Value, 17

PS

Anonymous Directories, xx

PTypes

List, 15

Literal, 15

Reference, 15

Q

Question Mark Help, xviii

R

Reference PType, 15

Registering RPCs, 19

Registry, 8, 22

Relationship between an M Entry Point and an RPC, 11

REMOTE APPLICATION (#8994.5) File, 29, 30, 31, 32, 38, 39

Remote Data Views, 28

REMOTE PROCEDURE (#8994) File, 11, 12, 16, 46

Remote Procedure Calls (RPCs), 11

RemoteProcedure Property, 5, 18

Results Property, 5, 18

RETURN VALUE TYPE (#.04) Field, 16

Return Value Types for RPCs, 13

Return Values from RPCs, 46

Revision History, ii

Documentation, ii

Patches, ix

ROUTINE (#.03) Field, 16

RPC Broker

Components for Delphi, 4

Delphi, 43

Login Component, 30, 31, 35, 36, 37, 39

Patches

XWB\*1.1\*45, 37

Website, xix

RPCs, 11

Bypassing Security, 19

Create Your Own RPCs

Preliminary Considerations, 11

Process, 12

Error Trapping, 41

Executing, 17

First Input Parameter (Required), 12

Input Parameter Types (Optional), 15

M Entry Point Examples, 15

Online Code Samples, 20

Registering, 19

Relationship between an M Entry Point and an RPC, 11

Return Value Types, 13

RPC Entry in the REMOTE PROCEDURE File, 16

Security, 19

What is a Remote Procedure Call?, 11

Writing M Entry Points for RPCs, 12

XWB GET VARIABLE VALUE, 25

rpctest.exe, 42

S

Security

Bypassing Security for Development, 19

How to Register an RPC, 19

Pass Phrase, 30, 31, 32, 37, 39

Phrase, 38, 39

SECURITY KEY (#19.1) File, 19

Security Keys

XUPROGMODE, 19

SecurityPhrase Property, 30, 31, 39

Server Property, 5, 22

Silent Calls, 17

Single Server Authentication, 32

Single Signon/User Context (SSO/UC), 9

Software Disclaimer, xiv

Splash Screen, 23

SplashClose Method, 23, 24

SplashOpen Method, 23, 24

SplVista.PAS Unit, 23, 24

SSHPort Property, 5

SSHPw Property, 5

SSHUser Property, 5, 22

SSHUseSecureConnection Property, 5

SSO/UC, 9

Starter Edition, 43

strCall Method, 6, 18

Support

Anonymous Directories, xx

Symbols

Found in the Documentation, xv

Syntax

GetServerInfo Function, 23

System Status Menu, 41

T

Table of Contents, x

TAG (#.02) Field, 16

TCCOWRPCBroker Component, 9

Temporary Globals

^XTMP, 40

Testing Your RPC Broker Connection, 42

TimeOut Parameter, 24

Token, 29, 31, 32, 36, 37, 39, 40

Sample, 30

Translate Function, 25

Trapping RPC Errors, 41

Troubleshooting, 41

Connections, 41

Error Trapping, 41

How to Debug Your Client Application, 41

Identifying

Handler Process on the Server, 42

Listener Process on the Server, 41

Testing Your RPC Broker Connection, 42

TRPCBroker Component, 4

Call Method, 6, 18

Connecting to an M Server, 7

CreateContext Method, 6, 19, 25

Key Properties, 5

lstCall Method, 6

Methods, 6

Properties and Methods, 4

strCall Method, 6

TXWBRichEdit Component, 9

TXWBSSOiToken Component, 10

U

Units

SplVista.PAS, 23, 24

URLs

Acronyms Intranet Website, 49

Adobe Website, xix

Glossary Intranet Website, 49

RPC Broker Website, xix

VA Software Document Library (VDL)

RPC Broker Home Page Web Address, 37

VA Software Document Library (VDL) Website, xix

URLSTRING (#.04) Field

CALLBACKTYPE (#1) Multiple Field, 39

V

VA Software Document Library (VDL)

RPC Broker Home Page Web Address, 37

Website, xix

Value Property, 17

Version

About this Version of the BDK, 1

VistA M Server, 35, 36

VistA Splash Screen, 23

Visual Basic Language, 45

W

Web Pages

VA Software Document Library (VDL)

RPC Broker Home Page Web Address, 37

Websites

Acronyms Intranet Website, 49

Adobe Website, xix

Glossary Intranet Website, 49

RPC Broker, xix

VA Software Document Library (VDL) Website, xix

What is a Remote Procedure Call?, 11

What Makes a Good Remote Procedure Call?, 17

Windows Registry, 8, 22

WORD WRAP ON (#.08) Field, 13, 16, 27

Writing M Entry Points for RPCs, 12

X

XU\*8.0\*404, 36

XUPROGMODE Security Key, 19

XUSTATUS Menu, 41

XWB GET VARIABLE VALUE RPC, 25

XWB_DXE*\#*.bpl File, 44

XWB_RXE*\#*.bpl File, 44

XWBLIB

\$\$BROKER^XWBLIB, 26

\$\$RTRNFMT^XWBLIB, 27