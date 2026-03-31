---
consolidated_title: "mobile electronic documentation (med) installation guide"
app_code: MED
doc_type: IG
master_source: "TIU*1*262 Mobile Electronic Documentation (MED) Installation Guide"
master_pub_date: January 2011
consolidated_from: 5 versions
prior_versions:
  - "TIU*1*244 Mobile Electronic Documentation (MED) Installation Guide"
  - "TIU*1*264 Mobile Electronic Documentation (MED) Installation Guide"
  - "TIU*1*311 Mobile Electronic Documentation (MED) Installation Guide"
  - "TIU*1*315 Mobile Electronic Documentation (MED) Installation Guide"
---

![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/001.png)

MOBILE ELECTRONIC DOCUMENTATION (MED)

RELEASE NOTES &  
INSTALLATION GUIDE

Documentation Patch: TIU\*1.0\*262  
Server Patch: TIU\*1.0\*257  
Client Software: Version 2.3

Original Release January 2011

Department of Veterans Affairs (VA)

Office of Information & Technology (OIT)

Product Development (PD)

This page intentionally left blank for double-sided printing.

<span id="_Toc345590303" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref296588203" class="anchor"></span>Table 1. Contents of TIU_1_257_MED.ZIP distribution file</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 44%" />
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
<td>01/11/2013</td>
<td>2.8</td>
<td><p>With patch TIU*1*264:</p>
<ul>
<li><blockquote>
<p>Corrected the security key reference to TIU MED MGT security key in Step #5 in the "Configure MED VistA Software" section.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/21/2011</td>
<td>2.7</td>
<td><p>Tech review and edit updates based on review/feedback from <mark>REDACTED</mark> review:</p>
<ul>
<li><p>Updated all MED document file references to the following:</p></li>
</ul>
<ul>
<li><p>TIU_1_262_MED_IG.doc/pdf</p></li>
<li><p>TIU_1_262_MED_TM.doc/pdf</p></li>
<li><p>TIU_1_262_MED_UM.doc/pdf</p></li>
</ul>
<ul>
<li><p>Updated all footers to reference MED documentation Patch TIU*1.0*262.</p></li>
<li><p>Updated the "General Updates" section to reference Patch TIU*1.0*262 and MED documentation updates.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>09/14/2011</td>
<td>2.6</td>
<td><p>Tech review and edit updates based on review/feedback from <mark>REDACTED</mark> review:</p>
<ul>
<li><p>Updated and renamed Section 3.2, "Prerequisite Software and Documentation."</p></li>
<li><p>Updated Section 3.3, "Software and Documentation Retrieval." Since MED is now to be a nationally released package, removed references to phased implementation and release.</p></li>
<li><p>Added and updated software-related sub-sections 3.3.1.1 and 3.3.1.2.</p></li>
<li><p>Added and updated documentation-related sub-sections 3.3.2.1, 3.3.2.2, and 3.3.2.3.</p></li>
<li><p>Updated the first paragraph in Step 3 in Section 5.2. Changed "deploring" to "deploying."</p></li>
<li><p>Updated note in Step 3d in Section 5.2. Changed "need" to "needed."</p></li>
<li><p>Added the following sentence to blank pages added so all chapter/document ends on an even page for double-sided printing:</p></li>
</ul>
<p>"This page intentionally left blank for double-sided printing."</p></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>09/05/2011</td>
<td>2.5</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Updated the following sections to indicate users <em>must</em> be given <strong>Full Control</strong> access permission to the MED directory (i.e., Read, Write, Modify, and Execute), as <mark>REDACTED</mark></p></li>
</ul>
<ul>
<li><p>Section 5.1, "Install MED GUI Software."</p></li>
<li><p>Section 5.2, "Configure MED GUI Software."</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>08/11/2011</td>
<td>2.4</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Removed patch compliance dates from the "<a href="#_Toc336755501">How to Use this Manual</a>" and "Distribution Files" sections, as per Chuck Schofer.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>08/10/2011</td>
<td>2.3</td>
<td><p>Tech review and edit updates based on review/feedback from MED Core team:</p>
<ul>
<li><p>Updated the cautionary note regarding national release in the "Software and Documentation Retrieval" section, as per <mark>REDACTED</mark>r review.</p></li>
<li><p>Updated reference from "VA Service Desk" to "National Service Desk-Tuscaloosa" in the "General Support" section, as per Chuck Schofer review.</p></li>
<li><p>Added Note to the Description field for the TIU MED MANUAL PATIENT security key in Table 5, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Updated responsible parties for obtaining and exporting templates in the "Install MED GUI Software" section, as per <mark>REDACTED</mark> review.</p></li>
<li><p>Removed author references, other than Project Manager and Tech Writer, from "Revision History" section, as per Product Support review.</p></li>
<li><p>Added phrase "to the network share directory" to Step 3b in the "Install MED GUI Software" section, as per Product Support review.</p></li>
<li><p>Removed lock from the TIU MED DEL PARM option in Table 4, as per Product Support review.</p></li>
<li><p>Updated Step 5 in the "Configure MED VistA Software" section, as per Product Support review.</p></li>
<li><p>Updated the procedures in the "Install MED GUI Software" section, as per Product Support review.</p></li>
<li><p>Updated Note contact info in Step 3d in the "Configure MED GUI Software" section, as per Product Support review.</p></li>
<li><p>Removed "Product Support (PS)" from the "<a href="#intended_audience">Intended Audience</a>" section, as per Product Support review.</p></li>
<li><p>Updated the Note in Step 2 in the "Configure MED GUI Software" section, as per Product Support review.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>07/27/2011</td>
<td>2.2</td>
<td><p>Tech review and edit updates based on review/feedback from Product Support team:</p>
<ul>
<li><blockquote>
<p>Added all Mobile Electronic Device (MED) VistA patch references and Graphical User Interface (GUI) client software version to the Title page.</p>
</blockquote></li>
<li><blockquote>
<p>Added the "<a href="#_Toc18284794">Orientation</a>" section in accordance with national documentation standards. Moved topics from the "Introduction" section into this new section.</p>
</blockquote></li>
<li><blockquote>
<p>Clarified the GUI version number in the "General Updates" section.</p>
</blockquote></li>
<li><blockquote>
<p>Changed the compliance date for Patch TIU*1.0*257 from 08/07/11 to 10/02/11 in the "Distribution Files" section.</p>
</blockquote></li>
<li><blockquote>
<p>Corrected the security key reference to TIU MED MGT security key in Step #5 in the "Configure MED VistA Software" section.</p>
</blockquote></li>
<li><blockquote>
<p>Added "The CAC is responsible for creating/determining which HBPC Health Summary will be used." to introductory paragraph in Step #5 in the "Configure MED VistA Software" section.</p>
</blockquote></li>
<li><blockquote>
<p>Removed Step #6 from the "Configure MED VistA Software" section and added it to the MED User Manual.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the roles responsible and content for the procedures in the "Install MED GUI Software" section. For example, changed "Write access" to "Read, Write, Modify, and Execute access".</p>
</blockquote></li>
<li><blockquote>
<p>Added a note suggesting users accept the default install directory in Step #5 in the "Install MED GUI Software" section.</p>
</blockquote></li>
<li><blockquote>
<p>Updated the "Configure MED GUI Software" section:</p>
</blockquote></li>
</ul>
<ul>
<li><p>Deleted information on setting the MED.exe program file properties in Step #1 to just reference the desktop shortcut properties.</p></li>
<li><p>Added procedures to set permission for the Mobile Electronic Documentation folder in Step #2.</p></li>
<li><p>Added Step #3 procedures to configure the MED default "Template Update Path".</p></li>
</ul>
<ul>
<li><blockquote>
<p>Added the <mark>REDACTED</mark>phone number to the "General Support" section.</p>
</blockquote></li>
<li><blockquote>
<p>Made general style, formatting, grammar, punctuation, and spelling updates as needed.</p>
</blockquote></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>07/12/2011</td>
<td>2.1</td>
<td><p>Tech review and updates based on conference call/Patient Safety team (Jeanie Scott) review/feedback:</p>
<ul>
<li><p>Separated VistA M Server and GUI instructions into separate chapters.<br />
<br />
Verified installation steps in each section only apply to the environment being described (i.e., VistA M Server OR client workstation).</p></li>
<li><p>Updated the "Prerequisite Software" section.</p></li>
<li><p>Updated the "Install MED GUI Software" section.</p></li>
<li><p>Updated the "Configure MED GUI Software" section.</p></li>
<li><p>Deleted duplicate content already listed in the MED Technical Manual (e.g., options, security keys, and RPCs) and User Guide (e.g., Import Template samples and security keys).</p></li>
<li><p>Added/Updated the following sections due to National Documentation Standard requirements:</p></li>
</ul>
<ul>
<li><p>Added "Uninstall MED GUI Software" section.</p></li>
<li><p>Updated the "Troubleshooting and Training" section; however, the content was reduced to refer user to open Remedy tickets for any issues.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>06/23/2011</td>
<td>2.0</td>
<td><p>Tech review and updates:</p>
<ul>
<li><p>Renamed document. Retained patch reference ID as part of name, since installation guide are patch-specific.</p></li>
<li><p>Reformatted document to follow current national documentation standards and style guides.</p></li>
<li><p>Added alternate text to all images for Section 508 compliance.</p></li>
<li><p>Added "Release Notes" section to list the changes made with Patch TIU*1.0*257 to the software since the release of Patch TIU*1.0*244.</p></li>
<li><p>Updated the "Introduction" section to be consistent across the MED documentation set.</p></li>
<li><p>Added/Updated other sections similar to the Patch TIU*1.0*244 Installation Guide.</p></li>
<li><p>Remedy Tickets #483291 and 485507: Added Step 6 in the "Installing and Configuring MED—GUI Client Workstation" section. Advises user to add IP/DNS and port information to MED launch desktop shortcut.</p></li>
<li><p>Made grammar, punctuation, and spelling updates as needed.</p></li>
</ul></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>01/21/2011</td>
<td>1.0</td>
<td>Patch TIU*1.*257 Initial document.</td>
<td>MED Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref296588203" class="anchor"></span>Table 1. Contents of TIU_1_257_MED.ZIP distribution file

This page intentionally left blank for double-sided printing.

Contents

This page intentionally left blank for double-sided printing.

<span id="_Toc345590304" class="anchor"></span>Figures and Tables

Figures

Tables

[Table 5. MED—Security keys for validating patient identification for manually entered MED  
patients [11](#_Ref300639398)](#_Ref300639398)

This page intentionally left blank for double-sided printing.

<span id="_Toc18284794" class="anchor"></span>Orientation

<span id="_Toc336755501" class="anchor"></span>How to Use this Manual

The Mobile Electronic Documentation (MED) application consists of both a Veterans Health Information Systems and Technology Architecture (VistA) M Server component and a Microsoft® Windows laptop/client workstation Graphical User Interface (GUI) component:

- Original VistA M Server Patch: TIU\*1.0\*244 (released date: 06/03/2010).
- Updated VistA M Server Patch: TIU\*1.0\*257 (released date: 01/21/2011).
- Documentation-only VistA M Server Patch TIU\*1.0\*262.
- Current Laptop/Client Workstation software: MED.exe Version 2.3.

This manual provides the installation instructions for installing the Text Integration Utility (TIU) Patch TIU\*1.0\*257 on the VistA M Server and the MED GUI software Version 2.3 on the laptop/client workstation.

MED works in tandem with CPRS; however, this manual does *not* attempt to fully document how to create templates or describe other functions of CPRS.

<table>
<caption><p><span id="_Ref303777997" class="anchor"></span>Table 2. FTP download servers—Anonymous directories</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/002.png)</td>
<td><p><strong>REF:</strong> For installation instructions; lists of routines, files, and options; additional technical information; and user information on CPRS, see the CPRS documentation on the VA Document Library (VDL) at the following link:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appid=61">http://www.va.gov/vdl/application.asp?appid=61</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Ref303777997" class="anchor"></span>Table 2. FTP download servers—Anonymous directories

<span id="intended_audience" class="anchor"></span>Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM)
- Clinical Application Coordinators (CAC)
- Product Support (PS)

Legal Requirements

There are no special legal requirements involved in the use of MED software.

Disclaimers

This manual provides an overall explanation of how to configure the MED software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Web sites on the Internet and VA Intranet for a general orientation to VistA. For example, visit the Office of Information & Technology (OIT) VistA Development VA Intranet Web Site:

http://vaww.vista.med.va.gov/

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/003.png) | DISCLAIMER: The appearance of any external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

<span id="_Ref297833149" class="anchor"></span>Table 3. MED documentation

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

Table ii. Documentation symbol/term descriptions

|                                                   |                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                            | Description                                                                                                         |
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/004.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/005.png) | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |

<span id="_Ref300667117" class="anchor"></span>Table 4. Secondary options for setting, modifying, and deleting MED parameters

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, an MED test patient and user names would be documented as follows: MEDPATIENT,ONE; MEDPATIENT,TWO; MEDPATIENT,THREE; MEDUSER,ONE, MEDUSER,TWO, MEDUSER,THREE, etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft® Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard. Other special keys are represented within angle brackets (\< \>). For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/006.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

<span id="_Ref300639398" class="anchor"></span>Table 5. MED—Security keys for validating patient identification for manually entered MED patients

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the TIU MED MGT key).

Documentation Navigation

This document uses Microsoft® Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Press the dropdown arrow in the "Choose commands from:" box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Click/Highlight the Back command and press the Add button to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Click/Highlight the Forward command and press the Add button to add it to your customized toolbar.
9.  Press OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/007.png)</td>
<td><p><strong>NOTE:</strong> Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic.</p>
<p><strong>REF:</strong> See the <em>Mobile Electronic Documentation (MED) Technical Manual</em> for further information.</p></td>
</tr>
</tbody>
</table>

Online Help

VistA M-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M-based software.

The MED laptop/client workstation software includes an MED GUI online help file (i.e., MED.chm). Instructions, procedures, and other information are available from the. To access the online help do either of the following:

- Inside MED, click on the Help \| Contents menu options from the MED GUI toolbar or press the F1 key while you have any MED dialogue screen open.
- Outside MED, double-click on the MED.chm file.

Obtaining Data Dictionary Listings

Technical information about VistA M-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                   |                                                                                                                                                                                                           |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/008.png) | REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions about the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- Microsoft® Windows
- M programming language

Reference Materials

Readers who wish to learn more about MED should consult the following:

- *Mobile Electronic Documentation (MED) User Manual*—Contains instructions on how to use the MED software.
- *Mobile Electronic Documentation (MED) Technical Manual*—Contains instructions for implementing and maintaining the MED software on the VistA M Server and Laptop/Client Workstation.
- *FORUM Patches: TIU\*1.0\*244, TIU\*1.0\*257, and TIU\*1.0\*262.*

VistA documentation is made available online in Microsoft® Word format and Adobe® Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe® Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe® Systems Incorporated at the following Website:

<http://www.adobe.com/>

VistA documentation can be downloaded from the VHA Software Document Library (VDL) Website:

<http://www4.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) anonymous directories:

- Preferred Method <span class="mark">REDACTED</span>

|                                                   |                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/009.png) | NOTE: This method transmits the files from the first available FTP server. |

<span class="mark">REDACTED</span>

This page intentionally left blank for double-sided printing.

# Release Notes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Release Notes](#release-notes)
  - [General Updates](#general-updates)
  - [Option Updates](#option-updates)
- [Introduction](#introduction)
- [Pre-Installation Instructions](#pre-installation-instructions)
  - [Distribution Files](#distribution-files)
  - [Prerequisite Software and Documentation](#prerequisite-software-and-documentation)
  - [Software and Documentation Retrieval](#software-and-documentation-retrieval)
    - [Software](#software)
    - [Documentation](#documentation)
  - [Verify MED Folder and Template Installed in CPRS](#verify-med-folder-and-template-installed-in-cprs)
- [Installing and Configuring MED—VistA M Server](#installing-and-configuring-medvista-m-server)
  - [Install Patch TIU\1.0\257](#install-patch-tiu10257)
  - [Configure MED VistA Software](#configure-med-vista-software)
- [Installing and Configuring MED—GUI Client Workstation](#installing-and-configuring-medgui-client-workstation)
  - [Install MED GUI Software](#install-med-gui-software)
  - [Configure MED GUI Software](#configure-med-gui-software)
  - [Uninstall MED GUI Software](#uninstall-med-gui-software)
- [Troubleshooting and Training](#troubleshooting-and-training)
  - [General Support](#general-support)
  - [Training](#training)
This chapter describes updates to the Mobile Electronic Documentation (MED) software with the installation of the Text Integration Utility (TIU) Patch TIU\*1.0\*257 and 262.

## General Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Patch TIU\*1.0\*257 addresses two issues with the MED application initially released with Patch TIU\*1.0\*244:
- Intermittent failure when retrieving patient data into the MED database when two or more users simultaneously attempted to retrieve Health Summary information. The data was either not imported or imported and associated within the MED database to the incorrect patient.
- Patient having an incomplete or corrupted Date of Birth (DOB). MED would not allow patient information to be retrieved and would not allow that patient to be imported into the MED database. This issue is fixed in the latest Graphical User Interface (GUI) client workstation software Version 2.3.257.21.
- Patch TIU\*1.0\*262 updated all of the following MED documentation:
- Mobile Electronic Documentation (MED) Installation Guide (TIU_1_262_MED_IG.doc/pdf)
- Mobile Electronic Documentation (MED) Technical Manual (TIU_1_262_MED_TM.doc/pdf)
- Mobile Electronic Documentation (MED) User Manual (TIU_1_262_MED_UM.doc/pdf)

## Option Updates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch TIU\*1.0\*257 removes and replaces the Mobile Electronic Documentation option \[TIU MED GUI RPC\] distributed with Patch TIU\*1.0\*244 with the following option:

Mobile Electronic Documentation option \[TIU MED GUI RPC V2\]—Creates the desired context for the GUI application on the VistA M Server.

This page intentionally left blank for double-sided printing.

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation (MED) 2.3 is a Veterans Health Information Systems and Technology Architecture (VistA) software application. It enables Department of Veterans Affairs (VA) staff to access a patient's previously downloaded electronic medical record information when not connected to the VA network. MED is designed to work in tandem with the Computerized Patient Record System (CPRS) as temporary storage of patient notes. This includes the ability to enter notes using CPRS exported Templates (.txml). MED promotes user satisfaction and efficiency in the login and documentation process by allowing access to CPRS at the point of care (POC) and avoid the duplicate process of charting handwritten notes at the end of the day.

When providing health care services, Home and Community Care staff (e.g., physicians, nurses, dieticians, social workers, and health care providers) must travel to a variety of geographic locations in which Internet access and coverage is often unreliable or sometimes unavailable. MED does the following:

- Allows access to secure patient information without the need for wireless Internet connectivity.
- Promotes the security of patient information by removing the need to print and carry excessive amounts of patient-sensitive data out of the clinical setting and into the community.
- Allows users to view and download to their secured laptops/client workstations Health Summary and MED Created Notes for patients in Home Based Primary Care (HBPC) Clinics.
- Provides the ability to enter and review patient documentation (e.g., Progress Notes) remotely at the point of care (POC), such as patient's home, when they are not connected to the VA network.
- Enables the transfer of patient data documented in MED during a home visit to be imported into CPRS as a patient note, which becomes part of the patient record.
- Minimizes errors from home visits by removing the need for paper records or the need to manually transfer (e.g., copy and paste) patient data from a mobile device.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/010.png)</td>
<td><p>CAUTION: This version of MED does <em>not</em> encrypt data. All laptops/client workstations are required to have full disk encryption and VA security policies. They should have normal health checks including security updates and antivirus.</p>
<p>Please be aware that if a laptop/client workstation is assigned to multiple users, MED notes and health summaries include patient information that is viewable to <em>all</em> users of that computer. Therefore, <em>all</em> users of the same laptop/client workstation <em>must</em> have the same level of security access to view this information.</p></td>
</tr>
</tbody>
</table>

  

This page intentionally left blank for double-sided printing.

# Pre-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Distribution Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mobile Electronic Documentation (MED) application consists of both a VistA M Server component and a Windows® Client Workstation component.

- VistA M Server Text Integration Utility (TIU) Patches: TIU\*1.0\*257 (released date: 01/21/2011)
- Client Workstation (e.g., laptops): MED 2.3 Graphical User Interface (GUI) software

All the required MED files for Patch TIU\*1.0\*257 are contained in the following Zip distribution file:

TIU_1_257_MED.ZIP

## Prerequisite Software and Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch TIU\*1.0\*257 requires the installation of Patch TIU\*1.0\*244 on the VistA M server. The complete MED documentation set and required prerequisite software is included in the Patch TIU\*1.0\*244 distribution zip file (i.e., TIU_1_244_MED.ZIP).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/011.png)</td>
<td><p><strong>REF:</strong> For instructions on how to obtain the TIU_1_244_MED.ZIP distribution and install Patch TIU*1.0*244, see the <em>Mobile Electronic Documentation (MED) Installation Guide</em> for Patch TIU*1.0*244 located on the VA Software Document Library (VDL) at:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appid=190">http://www.va.gov/vdl/application.asp?appid=190</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Software and Documentation Retrieval

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Contents

The TIU_1_257_MED.ZIP distribution file contains the MED VistA M Server and GUI software (Table 1).
| File              | Description                   | FTP Format |
|-------------------|-------------------------------|------------|
| MED Setup.exe     | MED GUI Client Install File   | Binary     |
| TIU_1_257_MED.KID | MED VistA M Server KIDS build | ASCII      |

#### Download Location—Anonymous Directories

The TIU_1_257_MED.ZIP distribution file is available on the Product Support (PS) ANONYMOUS.SOFTWARE FTP directories listed below:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 37%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th>Location</th>
<th>FTP Address</th>
<th>Directory</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>VistA Download Site<br />
</strong>(This is the preferred site. It transmits the files from the first available FTP server.)</td>
<td><strong>download.vista.med.va.gov</strong></td>
<td><strong>ANONYMOUS.SOFTWARE</strong></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

### Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Contents

The MED and Patch TIU\*1.0\*257/262 documentation consists of the following files:
<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 32%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>File</th>
<th>Description</th>
<th>FTP Format</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TIU_1_262_MED_IG.DOC</td>
<td>Install Guide<br />
(Word Version)</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>TIU_1_262_MED_IG.PDF</td>
<td>Install Guide<br />
(Adobe Acrobat Version)</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>TIU_1_262_MED_TM.DOC</td>
<td>Technical Manual<br />
(Word Version)</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>TIU_1_262_MED_TM.PDF</td>
<td>Technical Manual<br />
(Adobe Acrobat Version)</td>
<td>Binary</td>
</tr>
<tr class="odd">
<td>TIU_1_262_MED_UM.DOC</td>
<td>User Manual<br />
(Word Version)</td>
<td>Binary</td>
</tr>
<tr class="even">
<td>TIU_1_262_MED_UM.PDF</td>
<td>User Manual<br />
(Adobe Acrobat Version)</td>
<td>Binary</td>
</tr>
</tbody>
</table>

#### Download Location—Anonymous Directories

The MED documentation files are available on the Product Support (PS) ANONYMOUS.SOFTWARE FTP directories listed in Table 2.

#### Download Location—VA Software Document Library (VDL) Web Site

The MED documentation is also available on the VA Software Document Library (VDL) Web Site:

<http://www.va.gov/vdl/application.asp?appid=190>

## Verify MED Folder and Template Installed in CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinical Application Coordinator (CAC) *must* verify that the Mobile Electronic Documentation template folder and the Import M.E.D. Notes template were installed in the TIU TEMPLATE file (#8927) as part of Computerized Patient Record System (CPRS).

|                                                   |                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/012.png) | NOTE: Patch TIU\*1\*244 *should have* already created this template folder and template! |

To verify the existence of the folder and template, perform the following procedures:

1.  Open the Computerized Patient Record System (CPRS) application.
2.  Select the Notes tab.
3.  Click the Templates button.
4.  Expand the Shared Templates folder.
5.  Verify that the Mobile Electronic Documentation folder and the Import M.E.D. Notes template exists, as shown below:

> <span id="_Toc303778423" class="anchor"></span>Figure 1. CPRS—Verifying the Mobile Electronic Documentation folder and the Import M.E.D. Notes template exists

![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/013.png)

|                                                   |                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/014.png) | CAUTION: If the Mobile Electronic Documentation folder and the Import M.E.D. Notes template are *not* installed in CPRS, <u>STOP</u>! Have your CAC enter a National Remedy ticket to Text Integrated Utilities (TIU) for assistance *before* continuing with the installation! |

This page intentionally left blank for double-sided printing.

# Installing and Configuring MED—VistA M Server

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Install and configure the Mobile Electronic Documentation (MED) software on the Veterans Health Information Systems and Technology Architecture (VistA) M Server.

## Install Patch TIU\*1.0\*257

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Text Integration Utility (TIU) Patch TIU\*1.0\*257 can be installed with users on the system. Installation should take less than 2 minutes; however, it is recommended that installation is performed at non-peak requirement hours.

To install the VistA KIDS Patch TIU\*1.0\*257, perform the follow procedures:

1.  Verify the Mobile Electronic Documentation folder and the Import M.E.D. Notes template are installed in CPRS (see Section 3.4).

|                                                   |                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/015.png) | CAUTION: If the Mobile Electronic Documentation folder and the Import M.E.D. Notes template are *not* installed in CPRS, <u>STOP</u>! Have your Clinical Application Coordinator (CAC) enter a National Remedy ticket to Text Integrated Utilities (TIU) for assistance *before* continuing with the installation! |

2.  From the KIDS—Kernel Installation & Distribution System menu \[XPD MAIN\], select the Installation menu \[XPD INSTALLATION MENU\].
6.  At the "Select Installation Option:" prompt, select the Load a Distribution option \[XPD LOAD DISTRIBUTION\].
7.  At the "Enter a Host File:" prompt, enter TIU_1_257_MED.KID. You may need to prepend a directory name (e.g., USER\$:\[TEMP\]).
8.  At the "Want to Continue with Load? YES//" prompt, enter YES. The patch has now been loaded into a Transport global on your system. Use KIDS to install the transport global.
9.  From the KIDS—Kernel Installation and Distribution System menu \[XPD MAIN\], select the Installation menu \[XPD INSTALLATION MENU\].
10. (Recommended) From the Installation menu \[XPD INSTALLATION MENU\], select the Verify Checksums in Transport Global option \[XPD PRINT CHECKSUM\] to verify that all routines have the correct checksums; it ensures the integrity of the routines that are in the transport global:

TIU Routine CHECK1^XTSUMBLD values:

- Routine Name: TIUMED1:
- Before: B39834276
- After: B40119157
11. (Optional) From the Installation menu \[XPD INSTALLATION MENU\], use any of the following additional options as needed:
- Print Transport Global option \[XPD PRINT INSTALL\]—Use this option to print or view the contents of the transport global (i.e., KIDS build).
- Compare Transport Global to Current System option \[XPD COMPARE TO SYSTEM\]—Use this option to compare the routines in the Production account to the routines in the patch. It compares all components of the patch (e.g., routines, data dictionaries \[DDs\], templates, etc.).
- Backup a Transport Global option \[XPD BACKUP\]—Use this option to create a backup copy of the routines exported with the patch prior to installation. It does not backup any other changes (e.g., DDs or templates).

When prompted for an INSTALL NAME, enter TIU\*1.0\*257.

12. At the "Select Installation Option:" prompt, select the Install Package(s) option.
13. At the "Select INSTALL NAME:" prompt, enter TIU\*1.0\*257.
14. If prompted:
1.  "Want KIDS to INHIBIT LOGONs during the install? YES//", enter NO.
2.  "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//", enter NO.
3.  "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//", enter NO.
4.  "Delay Install (Minutes): (0-60): 0//", enter 0 (Zero).

## Configure MED VistA Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After installing MED Patch TUI\*1.0\*257, Information Resources Management (IRM) staff and Clinical Applications Coordinators (CAC) should configure the MED software on the VistA M Server

To configure the MED VistA M Server software, perform the following procedures:

1.  Assign the TIU MED MGT security key to IRM/CAC staff, if not already assigned.
15. Assign the following secondary options to the IRM/CAC staff so they can set, modify, and delete MED parameters:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 33%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Option Text</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TIU MED MANAGEMENT</td>
<td>MANAGE MOBILE ELECTRONIC DOCUMENTATION</td>
<td><p>Use this option to select the desired Health Summary Report.</p>
<p>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/016.png) This option is locked with the TIU MED MGT security key.</p></td>
</tr>
<tr class="even">
<td>TIU MED DEL PARM</td>
<td>HEALTH SUMMARY PARAMETER DELETE</td>
<td>Use this option to delete Health Summaries that have been previously set.</td>
</tr>
</tbody>
</table>

1.  Assign the following security keys to those individuals who will be tasked with validating patient identification for manually entered MED patients (e.g., CAC and Home Based Primary Care \[HBPC\] super users):

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>Security Key</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TIU MED MANUAL PATIENT</td>
<td><p>This security key allows users to enter manual patient notes in MED. If you hold this security key, the following <em>must</em> match exactly:</p>
<ul>
<li><p>The first letter of the last name.</p></li>
<li><p>The first letter of the first name.</p></li>
</ul>
<blockquote>
<p>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/017.png) <strong>NOTE:</strong> If the user types Last Name,First Name with a space after the comma, the patient will <em>not</em> be recognized when attempting to import into CPRS.</p>
</blockquote>
<ul>
<li><p>The date of birth (DOB).</p></li>
<li><p>The nine-digit Social Security Number (SSN).</p></li>
</ul></td>
</tr>
<tr class="even">
<td>TIU MED MANUAL OVERRIDE</td>
<td><p>This security key allows users to enter manual patient notes in MED. If you hold this security key, the full SSN <em>must</em> match exactly.</p>
<p>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/018.png) CAUTION: Only a select few users should be given the TIU MED MANUAL OVERRIDE security key. Most users should <em>not</em> be given this key.<br />
<br />
It is suggested that there be a document review and patient review before importing notes into patient records that have typographical or missing data that stops a user from importing the information as outlined with the TIU MED MANUAL PATIENT security key.</p></td>
</tr>
</tbody>
</table>

2.  Assign the Mobile Electronic Documentation secondary option \[TIU MED GUI RPC V2\] to HBPC users.
3.  Set the Health Summary Type for MED parameter \[TIU MED HSTYPE\] to generate Health Summaries in MED. The CAC is responsible for creating/assigning the HBPC Health Summaries that will be used.

To set the TIU MED HSTYPE parameter, the IRM/CAC staff needs to perform the following procedures:

1.  Select the MANAGE MOBILE ELECTRONIC DOCUMENTATION option \[TIU MED MANAGEMENT\].

|                                                   |                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/019.png) | NOTE: This option is locked with the TIU MED MGT security key. |

5.  At the "Enter Selection" prompt, select one of the following options:
- 1—User \[choose from NEW PERSON\].  
    
  At the "Please Select USER" prompt enter a user name in the NEW PERSON file (#200).
- 2—Service \[choose from SERVICE/SECTION\].  
    
  At the "Please select a SERVICE" prompt enter the service in the SERVICE/SECTION file (#49).
- 3—Division \[choose from INSTITUTION\].  
    
  At the "Please select a DIVISION:" prompt, enter the institution in the INSTITUTION file (#4).
- 4—System \[XXXXXXXX.MED.VA.GOV\]  
    
  Choose from the local system (e.g., ANYWHERE.MED.VA.GOV).

> <span id="_Toc297811667" class="anchor"></span>Figure 2. Manage Mobile Electronic Documentation option—Sample user dialogue to set the TIU MED HSTYPE parameter

Select Clinical Informatics Main Menu Option: MANAGE MOBILE ELECTRONIC DOCUMENTATION

TIU MED HSTYPE may be set for the following:

1 User \[choose from NEW PERSON\]

2 Service \[choose from SERVICE/SECTION\]

3 Division \[choose from INSTITUTION\]

4 System \[ANYWHERE.MED.VA.GOV\]

Enter Selection: 4 \<Enter\> System

Enter a HS for SYSTEM \[ANYWHERE.MED.VA.GOV\]: HBPC MED//

This page intentionally left blank for double-sided printing.

# Installing and Configuring MED—GUI Client Workstation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the Mobile Electronic Documentation (MED) software has been successfully installed and configured on the Veterans Health Information Systems and Technology Architecture (VistA) M Server (see Chapter 4), install and configure the MED Graphical User Interface (GUI) software component on individual laptops/client workstations.

## Install MED GUI Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the MED GUI laptop/client workstation software, perform the following procedures:

1.  The Information Resource Management (IRM) network staff needs to create a network share download directory (e.g., \\VHA...\TIU MED) with Full Control access permission (i.e., Read, Write, Modify, and Execute).
2.  The IRM network staff downloads and unzips the MED distribution file (TIU_1_257_MED.ZIP, see Section 3.1) into the network share download directory: The MED Setup.exe installer runs standalone and installs the MED software on a laptop/client workstation.
3.  The Clinical Applications Coordinator (CAC) obtains the TIU templates (.txml files) that will be used in MED from the POC/CAC for MED. The CAC exports those TIU templates that will be used for MED to this network shared folder:
1.  The IRM network staff creates a sub-folder called "Templates" under the network share download directory in Step 1:

\\VHA...\TIU MED\\Templates

6.  The CAC (with Full Control access permission to the network share directory) exports any TIU templates, with the exception of Reminder Dialogs, through the CPRS Template Editor into the Templates folder on the network share directory.

|                                                   |                                                                                                                                                                                                                   |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/020.png) | NOTE: Reminder Dialogs *cannot* be used within the MED application. In addition, you can use patient data objects in any template, but the data will *not* populate until the template is imported into CPRS. |

7.  Add a "ScratchPad\_" prefix (be sure to include the underscore) to the name of any TIU templates that are to be used as a Scratch Pad templates in MED (e.g., ScratchPad\_*NAMEOFTEMPLATE*.txml).
4.  From the laptop that will be used for MED, run the MED Setup.exe file from the network share download directory or copy it onto the laptop/client workstation and then run it from that location.
5.  Click Next through the following dialogues:

> <span id="_Toc295140650" class="anchor"></span>Figure 3. MED Install—Welcome wizard dialogue

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/021.png)

> <span id="_Toc295140651" class="anchor"></span>Figure 4. MED Install—Readme Information dialogue

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/022.png)

By default, MED installs in the following directory:

C:\Program Files\Mobile Electronic Documentation

|                                                   |                                                                                                                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/023.png) | NOTE: It is suggested you use the default settings from the Med Setup.exe install wizard; however, you can change the installation directory by clicking the Browse button and selecting a new install location. |

> <span id="_Toc295140652" class="anchor"></span>Figure 5. MED Install—Destination folders dialogue

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/024.png)

6.  Click Next to select a Program Group. By default, "Mobile Electronic Documentation" is used.

> <span id="_Toc295140653" class="anchor"></span>Figure 6. MED Install—Program group selection dialogue

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/025.png)

16. Click Next to begin installing the files.
17. Click Finish. The MED Setup.exe software automatically does the following:
- Creates the Mobile Electronic Documentation folder in the Microsoft® Windows Programs Files group, which includes the MED client application (MED.exe), help file (MED.chm) and other files as shown below:

> <span id="_Toc303778429" class="anchor"></span>Figure 7. Microsoft® Windows Explorer—Program Files MED directory folder and files

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/026.png)

- Adds a "Launch MED" shortcut icon on the laptop/client workstation, as shown below:

> <span id="_Toc303778430" class="anchor"></span>Figure 8. MED—Desktop shortcut icon

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/027.png)

- Copies all .txml template files from the network Templates folder to the following laptop/client workstation directory:

C:\Program Files\Mobile Electronic Documentation\Templates

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/028.png)</td>
<td><p><strong>REF:</strong> For further information about using MED, see the <em>Mobile Electronic Documentation Help</em> (i.e., MED.chm help file) in the Mobile Electronic Documentation folder on the laptop/client workstation and <em>Mobile Electronic Documentation (MED) User Manual</em> located on the VDL at:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appid=190">http://www.va.gov/vdl/application.asp?appid=190</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Configure MED GUI Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Update the "Launch MED" desktop shortcut with your site IP and RPC Broker port as follows:
1.  Right-click on the MED launch icon on the desktop.
2.  Select Properties.
3.  Select Shortcut tab.
4.  In the target field, append the site IP address or Domain Name Service (DNS) and RPC Broker port information after the MED.exe location. For example:

"C:\Program Files\Mobile Electronic Documentation\MED.exe" *s=test.alexandria.med.va.gov p=9201*

> <span id="_Toc303778431" class="anchor"></span>Figure 9. MED—Shortcut Target properties

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/029.png)

18. Set Permission for the Mobile Electronic Documentation folder.

On the HBPC laptop/client workstation, do the following:

1.  Navigate to the following directory:

C:\Program Files\Mobile Electronic Documentation

8.  Right click on the Mobile Electronic Documentation folder.
9.  Select Properties.
10. Select the group or user name in the upper portion of the Properties dialogue.
11. Check the Write checkbox under the Allow column in the lower portion of the Properties dialogue.
12. Press OK.

|                                                   |                                                                                                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/030.png) | NOTE: In order for users to write the appropriate information while using the MED software, they *must* have Full Control access permission to this folder; otherwise, they will get access violation errors when launching MED. |

19. Configure the MED default "Template Update Path".

Before deploying the HBPC laptop/client workstation to the user, the IRM or CAC *must* retrieve and select a patient in MED on each laptop/client workstation and add the network Templates path so the templates will be available for use in MED.

1.  Launch MED.
2.  Click Retrieve Patient(s).
3.  Click Select a Patient.
4.  Sign onto VistA: Enter your Access/Verify code.

|                                                   |                                    |
|---------------------------------------------------|------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/031.png) | <span class="mark">REDACTED</span> |

5.  Select a patient to retrieve from the list.
6.  Click Retrieve.
7.  Once the patient is retrieved, click Close.
8.  The MED Patient Select window is displayed; select the patient name again and click OK.
9.  Select the Tools menu and then select the Settings option, as shown below:

> <span id="_Toc303778432" class="anchor"></span>Figure 10. MED—Settings menu option

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/032.png)

10. In the Users & Settings dialogue, if not already selected, click on the Data & Files tab.
11. Enter the following directory path (created in Step 3a in Section 5.1) in the "Template Update Path" field (Figure 11):

\\VHA...\TIU MED\\Templates

12. Verify that the Retrieve Health Summaries checkbox is checked, as shown below:

> <span id="_Ref299466726" class="anchor"></span>Figure 11. MED Users & Settings dialogue—Data & Files

> ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/033.png)

These templates will become available for the user of that laptop/client workstation after MED is closed and re-opened.

## Uninstall MED GUI Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If necessary, to uninstall/remove the MED software from the laptop/client workstation, perform the following procedures:

1.  Press Start.
2.  Select Settings.
3.  Select Control Panel.
4.  Select Add or Remove Programs.
5.  Scroll through the list and select Mobile Electronic Documentation.
6.  Press Change/Remove.

This page intentionally left blank for double-sided printing.

# Troubleshooting and Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## General Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

|                                                   |                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/034.png) | CAUTION: If the Mobile Electronic Documentation folder and the Import M.E.D. Notes template are *not* installed in CPRS (see Section 3.4), <u>STOP</u>! Have your Clinical Application Coordinator (CAC) enter a National Remedy ticket to Text Integrated Utilities (TIU) for assistance *before* continuing with the installation! |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-262-mobile-electronic-documentation-med-installation-guide/035.png)</td>
<td><p><strong>REF:</strong> For further troubleshooting tips using MED, see the "Troubleshooting" section in the <em>Mobile Electronic Documentation (MED) Technical Manual</em> located on the VDL at:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appid=190">http://www.va.gov/vdl/application.asp?appid=190</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Training

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

This page intentionally left blank for double-sided printing.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: TIU*1*244 Mobile Electronic Documentation (MED) Installation Guide

## Verify Single "Shared Templates" Type in the TIU Template File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When Patch TIU\*1\*244 is installed, it looks for the Shared Templates shared root container TYPE in the TIU TEMPLATE file (#8927) .

|                                                                                                                   |                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-244-mobile-electronic-documentation-med-installation-guide/012.png) | CAUTION: You *must* have only one "Shared Templates" entry for the MED installation to work properly. If there is more than one entry "Shared Templates," you *must* identify the national root container in the TIU TEMPLATE file (#8927), and rename the other "Shared Templates" folders temporarily for the MED installation. |

## Install Patch TIU\*1.0\*244

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Text Integration Utility (TIU) Patch TIU\*1.0\*244 can be installed with users on the system. Installation should take less than 10 minutes; however, it is recommended that installation is performed at non-peak requirement hours.

To install the VistA KIDS Patch TIU\*1.0\*244, perform the follow procedures:

1.  From the KIDS—Kernel Installation & Distribution System menu \[XPD MAIN\], select the Installation menu \[XPD INSTALLATION MENU\].
1.  At the "Select Installation Option:" prompt, select the Load a Distribution option \[XPD LOAD DISTRIBUTION\].
2.  At the "Enter a Host File:" prompt, enter TIU\*1.0\*244.KID. You may need to prepend a directory name (e.g., USER\$:\[TEMP\]).
2.  At the "Want to Continue with Load? YES//" prompt, enter YES. The patch has now been loaded into a Transport global on your system. Use KIDS to install the transport global.
3.  From the KIDS—Kernel Installation and Distribution System menu \[XPD MAIN\], select the Installation menu \[XPD INSTALLATION MENU\].
4.  (Recommended) From the Installation menu \[XPD INSTALLATION MENU\], select the Verify Checksums in Transport Global option \[XPD PRINT CHECKSUM\] to verify that all routines have the correct checksums; it ensures the integrity of the routines that are in the transport global:

TIU Routine CHECK1^XTSUMBLD values:

- Routine Name: TIUCHECK:
- Before: B3689564
- After: B3648881 \*\*249,244\*\*
- Routine Name: TIUMED1:
- Before: N/A
- After: B39834276 \*\*244\*\*
- Routine Name: TIUPS244:
- Before: N/A
- After: B9297883 \*\*244\*\*
- Routine list of preceding patches: 249
5.  (Optional) From the Installation menu \[XPD INSTALLATION MENU\], use any of the following additional options as needed:
- Print Transport Global option \[XPD PRINT INSTALL\]—Use this option to print or view the contents of the transport global (i.e., KIDS build).
- Compare Transport Global to Current System option \[XPD COMPARE TO SYSTEM\]—Use this option to compare the routines in the Production account to the routines in the patch. It compares all components of the patch (e.g., routines, data dictionaries \[DDs\], templates, etc.).
- Backup a Transport Global option \[XPD BACKUP\]—Use this option to create a backup copy of the routines exported with the patch prior to installation. It does not backup any other changes (e.g., DDs or templates).

When prompted for an INSTALL NAME, enter TIU\*1.0\*244.

3.  At the "Select Installation Option:" prompt, select the Install Package(s) option.
4.  At the "Select INSTALL NAME:" prompt, enter TIU\*1.0\*244.
5.  If prompted:
1.  "Want KIDS to INHIBIT LOGONs during the install? YES//", enter NO.
2.  "Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//", enter NO.
3.  "Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//", enter NO.
4.  "Delay Install (Minutes): (0-60): 0//", enter 0 (Zero).

## Post Install Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After Patch TIU\*1\*244 is installed on the VistA M Server, the post-installation process does the following:

- Creates the "Mobile Electronic Documentation" TIU template folder under the "Shared Templates" TYPE field (#.03) in the TIU TEMPLATE file (#8927), which store the TIU templates (.txml files) that are found on the Computerized Patient Record System (CPRS) Notes tab.
- Adds the "Import M.E.D. Notes" TIU template. This template is used for importing the MED notes, in the following directory on the client workstation:

C:/Program Files/Mobile Electronic Documentation/Templates

- Adds the MED NOTE IMPORT .COM object in the OE/RR COM OBJECTS file (#101.15).
- Adds the TIU MED HSTYPE parameter in the PARAMETER DEFINITION NAME file (#8989.51).

|                                                                                                                   |                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-244-mobile-electronic-documentation-med-installation-guide/013.png) | CAUTION: If the Mobile Electronic Documentation" TIU template folder and "Import M.E.D. Notes" TIU template were not created, enter a National Remedy ticket to Text Integrated Utilities (TIU) for assistance. |

### From: TIU*1*315 Mobile Electronic Documentation (MED) Installation Guide

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the Mobile Electronic Documentation v2.3.315.1 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Mobile Electronic Documentation v2.3.315.1 project is for installation on a fully patched VistA system. There is also a Graphical User Interface (GUI) component that should be running on a Windows system.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.315.1 and the associated M patch are expected to be installed on existing VistA platforms. The hardware may reside at local or regional data centers. Mobile Electronic Documentation v2.3.315.1 utilizes existing, nationally released security controls to control access.

## Timeline 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no timeline specifically for deployment. This is considered a maintenance release and installation will be at the site’s discretion, within the constraints of the compliance period for the release.

## Site Readiness Assessment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the locations that will receive the Mobile Electronic Documentation v2.3.315.1 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.315.1 will be deployed to each VistA instance. That will include local sites as well as regional data processing centers. The executable will also be deployed to the Citrix Access Gateway.

### Site Information (Locations, Deployment Recipients) 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The initial deployment will be to IOC sites for verification of functionality. Once that testing is completed and approval is given for national release, Mobile Electronic Documentation v2.3.315.1 (TIU\*1.0\*315) will be deployed to all VistA systems.

The Production (IOC) testing sites are:

- Charlie Norwood VAMC (Augusta, GA)
- Central Plains HCS (Iowa City, IA)

### Site Preparation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There is no special preparation required for Mobile Electronic Documentation v2.3.315.1. A fully patched VistA system is the only requirement.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Facility Specifics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Hardware 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Software 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

### Communications 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Service Delivery and Engineering (SDE) Field Implementation Services will be sending out an Action item and National Change Order prior to the release of Mobile Electronic Documentation v2.3.315.1 advising them of the upcoming release.

Mobile Electronic Documentation v2.3.315.1 will be deployed using the standard method of patch release from the National Patch Module rather than a phased deployment. When patch TIU\*1.0\*315 is released, the National Patch Module will send a notification to all the personnel who have subscribed to those notifications.

#### Deployment/Installation/Back-Out Checklist

The deployment and installation will be performed by site support personnel once it is nationally released.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.315.1 assumes a fully-patched VistA system.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] This patch should be loaded during non-peak hours to minimize disruption to users. Installation will take less than 5 minutes. Users may remain on the system.

\[GUI\] The time to deploy the GUI will depend on which method the site utilizes for running the executable (network share, Citrix, individual workstation installs, etc.)

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mobile Electronic Documentation v2.3.315.1 is being released as a PackMan Message distributed through Forum combined with a .ZIP file containing the GUI file(s).

The preferred method is to retrieve files from <span class="mark">REDACTED</span>.

This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

Sites may retrieve the software and/or documentation directly using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at the following

| Location                           | Site                               |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Documentation can also be found on the VA Software Documentation Library at:

http://www.va.gov/vdl/

| File Name             | File Contents                                                 | Download Format |
|-----------------------|---------------------------------------------------------------|-----------------|
| TIU_1_315.ZIP         | Mobile Electronic Documentation executable and fresh database | Binary          |
| TIU_1_315_Upgrade.ZIP | Mobile Electronic Documentation executable                    | Binary          |

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation of Mobile Electronic Documentation v2.3.315.1 requires the following to install:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual work-station installs – access/ability to push executable to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TIU\*1.0\*315 VistA Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Select Kernel Installation & Distribution System Option: Installation

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

3.  From this menu, must use the \[Backup a Transport Global\] option to create a back out Patch
4.  Also from this menu, you may elect to use the following options:
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  Use the Install Package(s) options and select the package TIU\*1.0\*315
6.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? NO//', respond NO.
7.  When prompted ‘Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//’, respond NO.

### Mobile Electronic Documentation v2.3.315.1 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ZIP files contain the Mobile Electronic Documentation GUI executable and associated files. Download the ZIP file and extract all the files.

Due to the nature of the bug presented in the prior TIU\*1.0\*311 patch, version 2.3.315.1 is being offered as two separate downloads.

One download is for current users of TIU\*1.0\*311 and allows them to retain their current notes. The prior bug would not allow for these notes to be imported into CPRS prior to the install. Because of this it is recommended for users of the prior software to keep their database and just use the new executable and import DLL.

The second method is for fresh installs and is more traditional. This will install both the GUI application as well as a fresh empty database.

#### Mobile Electronic Documentation GUI Methods of Installation

The following methods of installation of Mobile Electronic Documentation are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

- Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the GUI executable (MED.exe) across the LAN.

> The GUI executable (MED.exe), and help file (MED.chm), are copied to a network shared location. Users are provided with a desktop shortcut to run MED.exe directly from the network shared drive. The necessary command line parameters (VistA server address or name and RPC Broker Port number) are entered in the “Target” field of the shortcut properties

> At the time of a Mobile Electronic Documentation version update the copy of MED.exe and the help file are simply replaced, on the network share, with the new version.

> Any users requiring access to another site's Mobile Electronic Documentation system can be given an alternate desktop shortcut with command line parameters appropriate to the intended target VistA system.

> If a user requires access to an older or newer version of Mobile Electronic Documentation (e.g. for testing purposes) a different version of MED.exe can be placed in a separate network location and the user be supplied with an appropriate alternate shortcut (different Target path and different VistA server command line parameters).

- Citrix installation:

> The GUI executable (MED.exe) and associated files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to either the Gold Path or the Direct Access methods outlined below.

- Local workstation installation:

  This is the “standard” method of installation where the GUI executable (MED.exe) and associated files are installed on and run from the user's local workstation. This method of installation initially requires the distribution and installation of a Microsoft Software Installation (MSI) file to each user's workstation, typically accomplished via SCCM. This is outside the scope of the Sustainment team. A National package (Mobile Electronic Documentation v2.3.315.1) has been prepared and made available to Regional COR Client Technologies leadership.
- Manual install:

  This method is used for users who wish to have a production instance and a non-production instance running on the same machine. An example would be users who are testing this software or needs to have access to a pre-production (mirror) VistA instance.
1.  Locate the TIU_10_315.ZIP and unzip the file.
2.  Copy the contents of the zip archive to a test directory, for example, C:\MEDGUITest. You may need to create this new directory.
3.  Run the MedBatch.bat file as outlined in Appendix A. The system needs to be set to test during the testing phase. This will adjust the registries to point to the test DLL instead of the production one.

    Note: You need to have a user with Administrator rights to this PC to complete these steps.
4.  Create a Shortcut and name it “Test MEDv315”. This is to give the user another visual cue that this is not the normal Mobile Electronic Documentation icon.

<span id="_Toc517273827" class="anchor"></span>Figure 1: Shortcut Icon for Test MEDv315

![](tiu-1-315-mobile-electronic-documentation-med-installation-guide/002.png)

5.  Determine the DNS server name or IP address for the appropriate VistA server.
6.  Determine the Broker RPC port for the VistA account.
7.  Enter IP (or DNS name) and RPC port in the Target field of the Shortcut properties (or use ServerList.exe).

<span id="_Toc517273828" class="anchor"></span>Figure 2: Test MEDv315 Properties

![](tiu-1-315-mobile-electronic-documentation-med-installation-guide/003.png)

> **NOTE:** The server and port number shown above are not real and are for example only.

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VISTA\] Verify the checksum of routine TIU315P is equal to the checksum listed on the patch description.

\[GUI\] Launch the Mobile Electronic Documentation GUI and verify the splash screen now announces that you are running version 2.3.315.1.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\[VistA\] In section 8.4.1 (step 3) the individual installing the patch used option \[Backup a Transport Global\] to create a packman message that will revert the Mobile Electronic Documentation components to their pre-v2.3.315.1 state. This includes everything transported in the TIU\*1.0\*315 (Mobile Electronic Documentation v2.3.315.1) build. If for any reason that PackMan Message cannot be located, Contact HPS Sustainment: Clinical (see section 5.6)

\[GUI\] To revert to the Mobile Electronic Documentation GUI, the 2.3.311.6 GUI would have to be redistributed

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No load testing was performed on Mobile Electronic Documentation v2.3.315.1. This was a maintenance release to correct defects discovered in Mobile Electronic Documentation 2.3.311.6. There was no additional functionality included.

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User acceptance testing was conducted by the three test sites listed in section 3.2.2.

The sites followed the provided test plan and executed the test cases according to the plan for the first build of TIU\*1.0\*315. The sites either passed or failed any item based on testing. The tests were performed by Clinical Application Coordinators at each site who are familiar using the application. The test cases were then delivered with concurrence by the sites to the HPS Clinical Sustainment team. Any items that failed were re-developed and then sent back to the sites for the next build and further acceptance testing following the same process. Once in production, the same final test cases from the last build were tested in production. No subsequent builds were created as the test cases passed and sites signed off on concurrence for release of the product.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out would only be considered if there was a catastrophic failure that causes loss of function for the application and a significant patient safety issue.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Backing out Mobile Electronic Documentation v2.3.315.1 would result in the re-instatement of the issues addressed in Mobile Electronic Documentation v2.3.315.1.

In addition, there is a risk that the process, which would be performed only in an emergent situation, would significantly impact patient care due to the interruption.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These steps assume that the only reason to consider a back-out for Mobile Electronic Documentation v2.3.315.1 is in the event of a catastrophic failure.

> **NOTE:** The Vista Changes and GUI changes are independent of each other. In the case of a catastrophic failure of the GUI, the VistA Patch can remain in the system; consequently, if the catastrophic failure is in the VistA side, the site can back out the VistA patch and continue to use the updated GUI

1.  Contact the HPS Clinical Sustainment implementation team to notify them there has been a catastrophic failure with Mobile Electronic Documentation v2.3.315.1. Use the following contacts:

<span id="_Toc517273829" class="anchor"></span>Figure 3: HPS Clinical Sustainment Contacts

| Name & Title                       | Email                              | Telephone Number                   |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

8.  If the decision is made to proceed with back-out and rollback, the HPS Sustainment Clinical team be available to assist sites that have misplaced their backup PackMan message, as well as give you the instructions on downloading the executable.
9.  \[VistA\] (if needed)
1.  Open the Backup MailMan Message
2.  At the “Enter message action (in IN basket): Ignore//” prompt Enter “X” for \[Xtract PackMan\]
3.  At the “Select PackMan function:” prompt select \[INSTALL/CHECK MESSAGE\]. The old routine is now restored
4.  \[GUI\] (if needed) Coordinate with the appropriate IT support, local and regional, to schedule the time to install TIU\*1.0\*311 and to push out / install the previous GUI executable.
10. Once TIU\*1.0\*311 and Mobile Electronic Documentation 2.3.311.6 have been installed, verify operations before making available to all staff.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Ensure the 2.3.311.6 executable launches properly.
11. Perform site-specific testing appropriate to the areas where the catastrophic failure was identified.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Facility CIO has the final authority to require the rollback and accept the associated risks

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out will automatically rollback version.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## New User Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run MEDBatch.bat (administrative privileges required)
12. Choose if you are currently using a screen reader or not
13. Choose New Setup Tools
14. Choose Yes to create the new registries
15. Follow any prompts

## Set system to test/production

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run MEDBatch.bat (administrative privileges required)
16. Choose if you are currently using a screen reader or not
17. Choose Testing Tools
18. Ensure that the production and test paths are correct. If not see the Setting system paths section below
19. To set the system to Test, choose Set system to test and follow any prompts
20. To set the system to Production, choose Set system to production and follow any prompts

## Patch specific test

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run MEDBatch.bat (administrative privileges required)
21. Choose if you are currently using a screen reader or not
22. Choose Testing Tools
23. Choose Patch Specific Setup
24. Follow the prompts to perform patch specific test

\*For TIU\*1.0\*315, this will copy the local production database over to the test folder to validate a fix for importing TIU documents via CPRS. This patch now moves the database to the user's AppData folder for use. Since there maybe times where this test may be re-ran, this process also renames the database that is out there so a new copy can be brought over. See the following path c:\Users\\username\]\AppData\Local\Mobile Electronic Documentation\db

## Setting system paths

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run MEDBatch.bat (administrative privileges required)
25. Choose if you are currently using a screen reader or not
26. Choose Testing Tools
27. Choose Change file locations
28. Follow the prompts to either change the production or test location.

\*\*Note, to make this change permanent you will need to edit the MEDBatch.bat and the MEDBatch508.bat file. Please make the change to the two variables at the top of the file (ProdLoc and TestLoc)

### From: TIU*1*311 Mobile Electronic Documentation (MED) Installation Guide

## PRE-INSTALLATION Steps for the MED GUI Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** if your site has previously installed and is currently using the TIU MED software, then some of these pre-installation steps will <u>not</u> need to be preformed.

1.  The Information Resource Management (IRM) network staff needs to create a network share download directory (e.g., \\YOURAPPSERVER\TIU MED) with Full Control access permission (i.e., Read, Write, Modify, and Execute) granted to your Clinical Applications Coordinator (CAC) and READ ONLY access to ALL USERS.
2.  The IRM network staff downloads the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI distribution file located in the software folder on <span class="mark">REDACTED</span>. The file will be used to install the MED software on the TIU MED laptop/client workstations which is described in section 1.3.
3.  The Clinical Applications Coordinator (CAC) obtains the TIU templates (.txml files) that will be used in MED from the POC/CAC for MED. The CAC then exports those TIU templates to the designated TIU MED Templates shared network folder.
1.  The IRM network staff creates a sub-folder called "Templates" under the network share download directory in Step 1:

\\YOURAPPSERVER\TIU MED\\Templates

b\. The CAC (with Full Control access permission to the network share directory) exports any  
TIU templates, with the exception of Reminder Dialogs, through the CPRS Template Editor  
into the Templates folder on the network share directory.

|                                                                                                                |                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/002.png) | NOTE: Reminder Dialogs *cannot* be used within the MED application. In addition, you can use patient data objects in any template, but the data will *not* populate until the MED progress note text is imported into CPRS. |

c\. Add a "ScratchPad\_" prefix (be sure to include the underscore) to the name of any TIU  
templates that are to be used as a Scratch Pad templates in MED  
(e.g., ScratchPad\_*NAMEOFTEMPLATE*.txml).  
> **NOTE:** Lower and upper case text formats need to follow this naming convention for the  
ScratchPad items to work properly. They are case sensitive as described above.

## VistA Patch TIU\*1\*311 Installation

  
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** VISTA Installation is *performed by IT/ IRM programming staff.*

1\. Install the VISTA Patch TIU\*1.0\*311 per the patch description from Forum.

## Client (Laptop) MED GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Notes: MED GUI Client Installation is *performed by  
PC/Desktop support Staff with CAC assistance.*

If your site is currently using the TIU MED software:

a\. Make sure that your Home Based Health Care providers have imported all pending notes from their MED Laptops into CPRS, as appropriate, before you begin the Client installation.

b\. If the laptop already has an existing version of MED installed, the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI will need to be executed twice. The first setup will uninstall the previous MED Client (the database is not uninstalled), and the second setup will then install the new patch 311 MED client files. (see below)

INSTALLATION: For laptops that already have a previous version of TIU MED installed;  
proceed to STEP 1, otherwise go to STEP 3.

STEP 1: Make note of the current TIU templates Update Path by opening MED and selecting a patient.

> Select the ‘Tools’ menu, click Settings and simply make note of the Template Update Path name \>\>\>

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/003.png)

> Note Write down this pathname and then close MED.

STEP 2: Obtain and launch the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI program as administrator. Download instructions are defined in the TIU\*1.0\*311 patch description. It can be launched directly from the network share download directory or copied onto the laptop/client workstation and then run from that location.

> Note *On a Windows7® PC, this means being logged on as an administrator, then right clicking the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSIand choosing “Run as Administrator.”*

> If TIU MED was previously installed you will see this dialog:

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/004.png)

> Click YES and then proceed to STEP 3 to install the new TIU MED 311 Client.

STEP 3: Obtain and launch the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI to install the MED Patch 311 Client and files. Download instructions are defined in the TIU\*1.0\*311 patch description. It can be launched directly from the network share download directory or copied onto the laptop/client workstation and then run from that location.

> Note *On a Windows 7® PC, this means being signed on as an administrator, then right clicking the MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSIand choosing “Run as Administrator.”*

> The Install Wizard will present these dialogs to you:

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/005.png)

> Click NEXT

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/006.png)

> Click NEXT

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/007.png)

> Note *Under Windows 7®, the default programs folder is “Program Files (x86)”.*

> *Under Windows XP®, the default programs folder is "Program Files."*

> Accept the defaults by clicking the NEXT button.

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/008.png)

> Click NEXT

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/009.png)

> Click NEXT

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/010.png)

> Click FINISH

STEP 4: Configure the Launch MED icon target server and port so that MED knows what Vista system to connect to.

> On the desktop, Right Click the “Launch MED” icon and choose properties.

> Enter the appropriate s=servername and p=rpcbrokerport on the Target line as follows:

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/011.png)

> Don’t forget to Click the *APPLY* button.

 

STEP 5: Configure the TIU Template Update folder on every TIU MED Laptop.  
  
Before deploying the HBPC laptop/client workstation to the user, the IRM or CAC *must* retrieve and select a patient in MED on each laptop/client workstation and add the network Templates path so the templates will be available for use in MED.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/012.png) | NOTE: While connected to the VA network/VistA, if you do not supply the appropriate signon credentials (i.e., PIV PIN /VA Access and Verify codes) you can access MED but *cannot* retrieve patients and summaries. You *must* sign into MED using the appropriate signon credentials *before* being given access to retrieve patient information from VistA. |

1.  Launch MED
2.  Click Retrieve Patient(s).
3.  Click Select a Patient.
4.  Sign onto VistA: Enter your Access/Verify code.

|                                                                                                                |                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------|
| ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/013.png) | <span class="mark">REDACTED</span> |

|                                                                                                                |                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/014.png) | NOTE: The person entering the Access and Verify codes will need the Secondary Menu: TIU MED GUI RPC V2 |

5.  Select a patient to retrieve from the list.
6.  Click Retrieve.
7.  Once the patient is retrieved, click Close.
8.  The MED Patient Select window is displayed; select the patient name again and click OK.
9.  Select the Tools menu and then select the Settings option, as shown below:

> TIU MED—Settings menu option

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/015.png)

> In the Users & Settings dialogue, if not already selected, click on the Data & Files tab.

> Next to "Template Update Path:" enter the network pathname where the TIU Templates are contained AND make sure ‘Retrieve Health Summaries’ is checked.

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/016.png)

> Note *If needed, your CPRS Clinical Coordinator should be able to assist you with this pathname.*

> Close MED. Then re-open MED to the Notes tab for a patient to ensure that the templates are present.

> Your installation of the Patch TIU\*1\*311 MED Client is complete.

STEP 6: Set Permissions for the Mobile Electronic Documentation folder.

On the HBPC laptop/client workstation, do the following:

a\. Navigate to the following directory:

*Windows XP® C:\Program Files\Mobile Electronic Documentation\Templates*

or

*Windows 7® C:\Program Files (x86)\Mobile Electronic Documentation\Templates*

b\. Right click on the Mobile Electronic Documentation folder.

c\. Select Properties.

d\. Select the group or user name in the upper portion of the Properties dialogue.

e\. Check the Write checkbox under the Allow column in the lower portion of the Properties dialogue.

f\. Press OK.

|                                                                                                                |                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/017.png) | NOTE: In order for users to write the appropriate information while using the MED software, they *must* have Full Control access permission to the Mobile Electronic Documentation folder; otherwise, they will get access violation errors when launching MED. |

STEP 7: CPRS Registration and Windows 7®: CPRS must be properly registered in the  
Windows 7® registry for COM objects to properly launch in CPRS, otherwise your end users may see this message when trying to import MED notes into CPRS.

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/018.png)

> Please note: This is not a CPRS software bug. In Windows XP®, when CPRS was launched by a non admin user, it properly registered itself because the registry wasn’t locked down like it is in Windows 7®.

> SOLUTION: CPRS will register itself in the registry automatically in Windows 7® if CPRS is launched once as ‘Run as Administrator’. Sign on to the laptop as an administrator. Right Click the CPRS Icon and select ‘Run as Administrator.’ You don’t even have to sign on to CPRS, just launching CPRS once as ‘run as administrator’ properly registers CPRS in the Windows 7® registry."

The MOBILEELECTRONICDOCUMENTATION_TIU-1-311.MSI software automatically does the following:

Creates the Mobile Electronic Documentation folder in the Microsoft® Windows Programs Files group, which includes the MED client application (MED.exe), help file (MED.chm) and other files as shown below:

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/019.png)

NOTE \>\> under Windows 7® the program files directory is “Program Files (x86)”

- Adds a "Launch MED" shortcut icon on the laptop/client workstation, as shown below:

> Figure 1. MED—Desktop shortcut icon

> ![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/020.png)

- Copies all .txml template files from the network Templates folder to the following laptop/client workstation directory:

Windows XP® C:\Program Files\Mobile Electronic Documentation\Templates

Windows 7® C:\Program Files (x86)\Mobile Electronic Documentation\Templates

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](tiu-1-311-mobile-electronic-documentation-med-installation-guide/021.png)</td>
<td><p><strong>REF:</strong> For further information about using MED, see the <em>Mobile Electronic Documentation Help</em> (i.e., MED.chm help file) in the Mobile Electronic Documentation folder on the laptop/client workstation and <em>Mobile Electronic Documentation (MED) User Manual</em> located on the VDL at:</p>
<blockquote>
<p><a href="http://www.va.gov/vdl/application.asp?appid=190">http://www.va.gov/vdl/application.asp?appid=190</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Uninstalling the MED GUI Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If necessary, to uninstall/remove the MED software from the laptop/client workstation, perform the following procedures:

1.  Press Start.
2.  Select Settings.
3.  Select Control Panel.
4.  Select Add or Remove Programs.
5.  Scroll through the list and select Mobile Electronic Documentation.
6.  Press Change/Remove.

### From: TIU*1*264 Mobile Electronic Documentation (MED) Installation Guide

## VistA Patch TIU\*1\*264 Installation

  
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** VISTA Installation is *performed by IT/ IRM programming staff.*

1\. Install the VISTA Patch TIU\*1.0\*264 per the patch description from Forum.
