---
title: PDX V. 1.5 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: VAQ
app_name: Patient Data Exchange (PDX)
section: INF
app_status: active
pkg_ns: VAQ
patch_ver: 1.5
patch_id: VAQ*1.5
group_key: "VAQ:VAQ:1.5"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - patient
  - class
  - strong
  - facility
  - time
  - date
  - request
  - mark
  - remote
page_count: 0
word_count: 26913
section_count: 10
table_count: 13
figure_count: 1
appendix_count: 3
has_toc: False
is_stub: False
pub_date: August 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Patient_Data_Exch_(PDX)/pdx1_5um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Patient_Data_Exch_(PDX)/pdx1_5um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=22"
---

---
title: |
  <span id="_Toc412806483" class="anchor"></span>Patient Data Exchange (PDX)

  Software Version 1.5

  User Manual
---

![](pdx-v-1-5-user-manual/001.png)

August 2018

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Ref25652056" class="anchor"></span>Revision History

<table>
<caption><blockquote>
<p><span id="_Ref522270095" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p>
</blockquote></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revision</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/22/2018</td>
<td>5.0</td>
<td><p><strong>Updates:</strong></p>
<ul>
<li><p>Patch XU*8.0*679: Electronic Signatures—Added note after Figure 1 concerning electronic Signature Block restrictions.</p></li>
<li><p>Reformatted document to follow current Office of Information and Technology (OIT) documentation standards and style guidelines.</p></li>
</ul></td>
<td>Existing Product Intake Program (EPIP) Technical Writer</td>
</tr>
<tr class="even">
<td>02/27/2015</td>
<td>4.0</td>
<td>Converted document to MS-Word 2007 format and incorporated <em><u>some</u></em> format changes from the ProPath User Guide Template.</td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="odd">
<td>01/11/2005</td>
<td>3.0</td>
<td><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="even">
<td>09/27/2004</td>
<td>2.0</td>
<td><p>Reformatted document to follow ISS styles and guidelines, no other content updates made.</p>
<p>Reviewed document and edited for the “Data Scrubbing” and the “PDF 508 Compliance” projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><p>The first three digits (prefix) of any Social Security Numbers (SSN) start with “000” or “666.”</p></li>
<li><p>Patient or user names are formatted as follows: PDXPATIENT,[N] or PDXUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., PDXPATIENT, ONE, PDXPATIENT, TWO, etc.).</p></li>
<li><p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p></li>
</ul></td>
<td>Infrastructure Technical Writer, Oakland, OIFO</td>
</tr>
<tr class="odd">
<td>11/1993</td>
<td>1.0</td>
<td>Initial Patient Data Exchange 1.5 software documentation creation.</td>
<td>REDACTED, NY OIFO</td>
</tr>
</tbody>
</table>

<span id="_Ref522270095" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Table of Contents

<span id="_Toc522273871" class="anchor"></span>List of Figures

<span id="_Toc522273872" class="anchor"></span>List of Tables

<span id="_Toc234301877" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instruction are offered regarding the use of the Patient Data Exchange (PDX) software within Veterans Health Information Systems and Technology Architecture (VistA) system.

Most of the PDX option documentation found in this manual contains the following components:

- Introduction—The Introduction gives a detailed description of the option, its use, and any special instructions.
- Process Chart—The Process Chart illustrates the flow of the option, step-by-step, and shows the various choices allowed at each prompt.
- Examples—An example of what may appear on the screen while using the option and an example of any output produced by the option are provided.

The process charts in this manual do *not* contain documentation of the system’s response to erroneous input. In certain instances, in order to preserve the integrity of previously entered data, the system does *not* allow the entry of a caret (^). This also may *not* be documented.

The options in this manual appear in the same order in which the main menu usually appears on the screen. Since the menu may be changed by the site and all users do *not* have all options, the menu structure shown in this manual may be different from the one seen by every user.

Intended Audience

The intended audience of this manual is the following stakeholders:

- Patient Data Exchange (PDX) end-users.
- Product Support (PS).
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- Information Security Officers (ISOs)—Personnel at VA sites responsible for system security.

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](pdx-v-1-5-user-manual/002.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per VHA Directive 2004-038, this routine should not be modified.

![](pdx-v-1-5-user-manual/003.png) CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for *non*-VistA use should be referred to the VistA site’s local Office of Information Field Office (OIFO).

Documentation Disclaimers

The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                            | Description                                                                                                         |
|-------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](pdx-v-1-5-user-manual/004.png)      | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](pdx-v-1-5-user-manual/005.png) | CAUTION/DISCLAIMER: Used to caution the reader to take special notice of critical information.                  |

<span id="_Ref522185846" class="anchor"></span>Table 2: Request PDX for Patient Option—Process Chart

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<Application Name/Abbreviation/Namespace\>*PATIENT,*\<N\>*
- *\<Application Name/Abbreviation/Namespace\>*USER,*\<N\>*

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in Patient Data Exchange (PDX) test patient and user names would be documented as follows:

PDXPATIENT,ONE; PDXPATIENT,TWO; PDXPATIENT,THREE; … PDXPATIENT,14; etc.

PDXUSER,ONE; PDXUSER,TWO; PDXUSER,THREE; … PDXUSER,14; etc.

- “Snapshots” of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- User’s responses to online prompts will be bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box will be bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- References to “\<Enter\>“ within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](pdx-v-1-5-user-manual/006.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M “\>“ prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](pdx-v-1-5-user-manual/007.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case.

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](pdx-v-1-5-user-manual/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

![](pdx-v-1-5-user-manual/009.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

![](pdx-v-1-5-user-manual/010.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” chapter in the “File Management” section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel 8.0 Installation and Distribution System (KIDS)
- VA 22.2 data structures and terminology
- MailMan 8.0
- M programming language

Reference Materials

Readers who wish to learn more about PDX should consult the following:

- *Patient Data Exchange (PDX) Installation Guide & Release Notes*
- *Patient Data Exchange (PDX) Technical Manual*
- *Patient Data Exchange (PDX) Security Guide*
- *Patient Data Exchange (PDX) User Manual (this manual)*

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by Adobe<sup>®</sup> Systems Incorporated at the following Website: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Software Management](#software-management)
- [Software Operation](#software-operation)
  - [Implementation](#implementation)
  - [PDX Options](#pdx-options)
    - [Request PDX for Patient](#request-pdx-for-patient)
    - [Unsolicited PDX](#unsolicited-pdx)
    - [Process External PDX](#process-external-pdx)
    - [Load/Edit PDX Data](#loadedit-pdx-data)
  - [Display PDX Data](#display-pdx-data)
    - [Display PDX by Transaction](#display-pdx-by-transaction)
    - [Display PDX by User](#display-pdx-by-user)
  - [System Reports](#system-reports)
    - [Requires Processing Report](#requires-processing-report)
    - [Sort By Remote Facility](#sort-by-remote-facility)
    - [Sort By User That Generated Request](#sort-by-user-that-generated-request)
    - [Sort By Patient’s Name](#sort-by-patients-name)
    - [Sort By Date Received](#sort-by-date-received)
    - [Sort By User That Released Information](#sort-by-user-that-released-information)
    - [Sort By Requesting Date](#sort-by-requesting-date)
    - [Sort By Status of Transaction](#sort-by-status-of-transaction)
    - [Sort Criteria Defined By User](#sort-criteria-defined-by-user)
  - [Work Load Reports](#work-load-reports)
    - [Sort By Date](#sort-by-date)
    - [Sort By Remote Facility](#sort-by-remote-facility-1)
    - [Sort By Patient’s Name](#sort-by-patients-name-1)
    - [Sort Criteria Defined By User](#sort-criteria-defined-by-user-1)
    - [Sort By Type of Work Done](#sort-by-type-of-work-done)
  - [PDX Edit Files](#pdx-edit-files)
    - [Add/Edit Fields to Encrypt](#addedit-fields-to-encrypt)
    - [Edit maximum limits for automatic processing](#edit-maximum-limits-for-automatic-processing)
    - [Add/Edit Outgoing Group](#addedit-outgoing-group)
    - [Edit Parameter File](#edit-parameter-file)
    - [Add/Edit Segment Group - Private](#addedit-segment-group-private)
    - [Add/Edit Segment Group - Public](#addedit-segment-group-public)
    - [Add/Edit Release Group](#addedit-release-group)
    - [Add/Edit Segment Group - All](#addedit-segment-group-all)
  - [Purging](#purging)
    - [Purge Using Default Age](#purge-using-default-age)
    - [Purge Using User Defined Age](#purge-using-user-defined-age)
    - [Purge Using User Defined Date](#purge-using-user-defined-date)
  - [Mail Groups and Bulletins](#mail-groups-and-bulletins)
    - [Mail Groups](#mail-groups)
    - [Bulletins](#bulletins)
- [Appendix A—List Manager](#appendix-alist-manager)
- [Appendix B—Health Summary Components](#appendix-bhealth-summary-components)
- [Appendix C—PDX Transaction Statuses](#appendix-cpdx-transaction-statuses)
This is the user manual for the Veterans Health Information Systems and Technology Architecture (VistA) Patient Data Exchange (PDX) software. It is designed to introduce users to the PDX system and provide guidelines and assistance for effective use of the PDX functions.
Patient Data Exchange (PDX) manages the transfer of patient information (demographics, episodes of care, medications, and diagnostic evaluations) between VA facilities using the MailMan electronic mail utility. Once transferred, this information can be combined with pertinent local information and assembled into a coherent composite record.
Requests for PDX data can be processed manually or automatically. For requests to be processed manually, the site would have to be a member of the Release Group and meet the requirements for automatic processing. Records determined to be “sensitive” and those that exceed the maximum time and occurrence limits for Health Summary components may *not* be returned automatically and will be held for manual processing.
![](pdx-v-1-5-user-manual/011.png) REF: For a list of the Health Summary components supported by PDX, see “<u>Appendix C—PDX Transaction Statuses</u>.”
PDX 1.5 uses the List Manager utility extensively. The List Manager is a tool designed to display a list of items. It allows you to select items from the list and perform specific actions against those items.
![](pdx-v-1-5-user-manual/012.png) REF: For help in using the List Manager utility, if necessary, see “<u>Appendix A—List Manager</u>.”
The software provides numerous system reports (current transactions and work load), which allow predefined and customizable sorts.
The following is a brief description of the major options and menus contained in the PDX software:
- Request PDX for Patient—This option is used to electronically request PDX data for a selected patient from another VA facility(s).
- Unsolicited PDX—This option is used to send PDX information to a remote site without having first received a request.
- Process External PDX—This option is used to process PDX requests received from other VA facilities that do not meet the criteria for automatic processing.
- Load/Edit PDX Data—This option allows you to load or edit data fields in your PATIENT file with data from your PDX file.
- Display PDX Data Menu—This menu allows you to display or print PDX data for a selected patient by either transaction or user who requested the information.
- System Reports Menu:
- Requires Processing Report—This option is used to print a report of all PDX requests that require manual processing.
- Current Transactions Report Menu—The options on this menu allow you to print reports of PDX transactions on file by several different sorting methods.
- Work Load Reports Menu—The options on this menu allow you to print work load reports of PDX transactions on file by several different sorting methods.
- PDX Edit Files Menu:
- Add/Edit Fields to Encrypt—This option provides the ability to encrypt selected data fields in the PDX transmission.
- Edit Maximum Limits for Automatic Processing—This option is used to edit the maximum time and occurrence limits that your site is willing to allow for automatic processing of a PDX transaction.
- Add/Edit Outgoing Group—This option is used to create outgoing groups and add/edit/delete remote facilities in those groups.
- Edit Parameter File—This option is used to set up site specific PDX parameters.
- Add/Edit Segment Group Options—These three options are used to create segment groups (selected group of data segments).
- Add/Edit Release Group—This option is used to enter/edit facilities into the release group for automatic processing of PDX requests.
- Purging Menu—These three options provide purging capabilities by default age, user defined age, or user defined date.

## Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users of the PDX software *must* set up an electronic signature in order to use the software. This can be accomplished through the Edit Electronic Signature Code option of the User’s Toolbox menu.

As an optional security measure, this software provides the ability to encrypt data using existing data encryption methods. Sites wishing to encrypt certain fields will have to turn the flag on through the Edit Parameter File option and add those fields to the VAQ - ENCRYPTED FIELDS (#394.73) file.

# Software Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All users of the PDX software *must* set up an electronic signature in order to use the software. This may be accomplished by entering “TBOX” at your main menu and selecting the Edit Electronic Signature code option.

![](pdx-v-1-5-user-manual/013.png) NOTE: The signature code *must* be 6-20 characters in length and contain no control or lowercase characters.

An example of what may appear on the screen when using the option is shown in <u>Figure 1</u>.

<span id="_Ref522180436" class="anchor"></span>Figure 1: Edit Electronic Signature code Option—Sample User Dialogue

Select User’s Toolbox Option: Edit Electronic \<Enter\> Signature code

This option is designed to permit you to enter or change your Initials, Signature Block Information and Office Phone number. In addition, you are permitted to enter a new Electronic Signature Code or to change an existing code.

INITIAL: <span class="mark">GU</span>

SIGNATURE BLOCK PRINTED NAME: <span class="mark">FIVE PDXUSER</span>

SIGNATURE BLOCK TITLE: <span class="mark">ELIGIBILITY CLERK</span>

OFFICE PHONE: <span class="mark">555-5555</span>

ENTER NEW SIGNATURE CODE:

![](pdx-v-1-5-user-manual/014.png) NOTE: If the SIGNATURE BLOCK PRINTED NAME and SIGNATURE BLOCK TITLE fields are disabled at your site, contact your supervisor to request entry of your name and title.

## Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A release group can be defined in the VAQ - PARAMETER (#394.81) file through VA FileMan. Data is returned automatically, upon request, for sites you specify. A VAQ UNSOLICITED RECEIVED mail group can also be set up through VA FileMan. Members of this mail group will receive MailMan bulletins upon receipt of an unsolicited request or when a PDX request received by your site requires manual processing.

![](pdx-v-1-5-user-manual/015.png) REF: For further instruction on implementation of this software, including the setup of the release group and mail groups, see the “Installation Guide” section of the *PDX Release Notes & Installation Guide*.

## PDX Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Request PDX for Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Request PDX for Patient option electronically requests PDX (Patient Data Exchange) data for a selected patient from another VA facility. Information can be retrieved from any VA facility running the PDX 1.5 software.

Once the PDX request is received at the remote site (the site you from which are requesting the data), it is stored in their PDX files where it remains until it is processed automatically (if your site is defined in the remote site’s release group and the request meets criteria for automatic processing), or manually through the Process External PDX Request option.

Once processing is complete, the data is returned to you electronically. You will also receive a MailMan bulletin when the request has been processed and returned by the remote site. A sample bulletin is provided in the example section of this option documentation.

When a PDX request is created, an entry is made in the VAQ - Transaction (#394.61) file and a request number is automatically assigned. This is the transaction number for this request.

You can select numerous domains from which to request the data and the particular data segments you wish to request from each domain. Segment groups, which may be set up through other PDX options, can be used during the request. These groups contain predefined data segments and allow you to request numerous segments with one entry. The proper format *must* be used when entering the request domain(s). Two question marks (??) be entered at the domain prompt for a list of network addresses shown in the required format.

If there is no entry in the PATIENT (#2) file for the selected patient and you choose to proceed, you will be prompted for the patient’s social security number (SSN) and date of birth (DOB). Any information entered/edited through this option is changed in the PDX files only. The PATIENT (#2) file is *not* affected. An entry is made in your VAQ - WORKLOAD file for each request made.

Time and occurrence limits can be placed on applicable data segments. These limits determine how far back the system searches for the component and the number of occurrences of that component the system reports. Default values for these fields can be set through the Edit Parameter File option.

#### Process

The process chart in <u>Table 2</u> shows the steps and prompts involved in using the Request PDX for Patient option.

<table>
<caption><p><span id="_Ref522185975" class="anchor"></span>Table 3: Unsolicited PDX Option—Process Chart</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 38%" />
<col style="width: 45%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>At this Prompt...</th>
<th>If User Answers with...</th>
<th>Then Step</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td>Select Patient Name:</td>
<td>Patient from your PATIENT (#2) file.</td>
<td><strong>3</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>Patient not in your PATIENT (#2) file.</td>
<td><strong>2</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> or Caret &lt;<strong>^</strong>&gt;</td>
<td><strong>16</strong></td>
</tr>
<tr class="even">
<td></td>
<td>If you select to request a PDX, you will be prompted for the patient’s name, social security number, and date of birth before proceeding.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>2</strong></td>
<td><p>{Step 1 entry} not found in local patient file...</p>
<p>Request PDX? YES//</p></td>
<td><strong>&lt;Enter&gt;</strong> to accept default.</td>
<td><strong>3</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>NO</strong></td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>The PDX Status screen is displayed listing any PDX transactions on file for the patient.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td>Select Action: Quit//</td>
<td><strong>CR</strong> to create PDX request</td>
<td><strong>4</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>DP</strong> to display PDX (if one exists with results)</td>
<td><strong>13</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to accept default</td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>The PDX Request screen is displayed.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>4</strong></td>
<td>Select Action: Quit//</td>
<td><strong>AE</strong> to add/edit PDX request</td>
<td><strong>5</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>TR</strong> to transmit PDX, if applicable</td>
<td><strong>10</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>CO</strong> to copy PDX, if applicable</td>
<td><strong>15</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>CP</strong> to change to another patient</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to accept default</td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td><strong>5</strong></td>
<td>Enter Domain:</td>
<td>E-mail address of the facility or group from which you wish to request the PDX</td>
<td><strong>6</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> (1st appearance of prompt)</td>
<td><strong>4</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> (subsequent appearance)</td>
<td><strong>9</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;??&gt;</strong> For list of domain/group addresses</td>
<td><strong>5</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;?&gt;</strong> For list of choices you may enter at this prompt</td>
<td><strong>5</strong></td>
</tr>
<tr class="even">
<td></td>
<td>The PDX*MIN data segment will automatically be included in any request.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td>Enter Segment:</td>
<td>Data segment or segment group you wish to request from selected domain</td>
<td><strong>7</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong></td>
<td><strong>5</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;??&gt;</strong> For list of data segments/groups</td>
<td><strong>6</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;?&gt;</strong> For list of choices you may enter at this prompt</td>
<td><strong>6</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>Steps 7 and 8 may/may not appear depending on the data segment selected.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td>Time Limit:</td>
<td>Time limit to use for selected data segment</td>
<td><strong>8</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to not specify a limit</td>
<td><strong>8</strong></td>
</tr>
<tr class="even">
<td><strong>8</strong></td>
<td>Occurrence Limit:</td>
<td>Occurrence limit to use for selected date segment</td>
<td><strong>6</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to not specify a limit</td>
<td><strong>6</strong></td>
</tr>
<tr class="even">
<td></td>
<td>The PDX Request screen is redisplayed showing your domain and segment choices. Time and occurrence limits will be displayed with the segments, if applicable.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>9</strong></td>
<td>Select Action: Quit//</td>
<td><strong>AE</strong> to add/edit PDX request</td>
<td><strong>5</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>TR</strong> to transmit PDX</td>
<td><strong>10</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>CO</strong> to copy PDX</td>
<td><strong>15</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>CP</strong> to change to another patient</td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to accept default</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td></td>
<td>Your signature code <em>must</em> be previously established through the Toolbox utility.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>10</strong></td>
<td>Enter your Signature Code:</td>
<td>Signature code</td>
<td><strong>11</strong></td>
</tr>
<tr class="even">
<td></td>
<td>This prompt will be repeated until no further entries are made and you press the Enter key. These users will be notified when the PDX data is received from the remote site(s). You need to enter yourself at this prompt in order to receive the mail bulletin.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>11</strong></td>
<td>User to notify:</td>
<td>Users at your site you wish notified of this PDX request</td>
<td><strong>12</strong></td>
</tr>
<tr class="even">
<td></td>
<td>After your entry at this step, you will be asked if you wish to exit the “Notify” functionality. If you answer NO, you will return to step 11.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>12</strong></td>
<td>Include Data with Notification(s):? NO//</td>
<td><strong>YES</strong> if you wish users specified at previous step to receive the actual data received</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> if you wish users specified at previous step to receive only notification of the PDX request and not the actual data</td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td><p>The PDX Segments screen is displayed listing all segments for the selected PDX.</p>
<p>If there is more than one entry to choose from and you enter DS, you will be asked to select the desired entry(s).</p></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>13</strong></td>
<td>Select Action: Quit//</td>
<td><strong>DS</strong> to display a selected segment</td>
<td><strong>14</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>DA</strong> to display all listed segments</td>
<td><strong>14</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to accept default</td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>You will be prompted for a device. If you choose to print to the screen, the PDX Data Display screen is displayed showing the patient data for the selected segment (s). If the transaction did not contain information for a segment, that message will be displayed. You will proceed to step 13 or 3 depending on the number of segments selected for display.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>14</strong></td>
<td>Select Action: Quit//</td>
<td><strong>&lt;Enter&gt;</strong> to accept default</td>
<td><strong>13 or 3</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>You may now add another domain(s) for this PDX request without going through all the steps of the request again. This prompt will be repeated until no further entries are made and you press the Enter key.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>15</strong></td>
<td>Copy to Domain:</td>
<td>Domain or domain group name</td>
<td><strong>9</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong></td>
<td><strong>9</strong></td>
</tr>
<tr class="even">
<td><strong>16</strong></td>
<td>Return to the menu.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref522185975" class="anchor"></span>Table 3: Unsolicited PDX Option—Process Chart

#### Example

<u>Figure 2</u> and <u>Figure 3</u> are examples of what may appear on your screen while using the Request PDX for Patient option followed by a sample of the type of MailMan bulletin (<u>Figure 4</u>), which may be received when the request is processed at the remote site. The remote user name, in this case, indicates that this request was processed automatically. If processed manually, this field would show the name of the user at the remote site who processed the request.

<span id="_Ref522183746" class="anchor"></span>Figure 2: Request PDX for Patient Option—Sample User Dialogue (1 of 2)

Select Patient Name: <span class="mark">PDXPATIENT,ONE \<Enter\></span> 02-22-22 000111111 SC VETERAN

PDX V1.5 - STATUS Sep 01, 1993 08:14:57 Page: 1 of 1

Patient : PDXPATIENT,ONE Type: SC VETERAN

Patient SSN: 000-11-1111 DOB: FEB 22,1922

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*\* No PDX transactions found for this patient...

Enter ?? for more actions

CR Create Request DP Display PDX

Select Action: Quit// <span class="mark">cr \<Enter\></span> Create Request

PDX V1.5 - REQUEST Sep 01, 1993 08:16:32 Page: 1 of 1

Patient : PDXPATIENT,ONE Type: SC VETERAN

Patient SSN: 000-11-1111 DOB: FEB 22,1922

Entry Domain Data Segment(s) \[Time:Occurrence\]

\*\* Select an option or \<Return\> to exit

Enter ?? for more actions

AE Add/Edit Request CO Copy Request

TR Transmit Request CP Change Patient

Select Action: Quit// <span class="mark">ae \<Enter\></span> Add/Edit Request

Enter Domain: <span class="mark">REDACTED.VA.GOV</span>

------------------------------ Segments Selected -----------------------------

PDX\*MIN

------------------------------------------------------------------------------

Enter Segment: <span class="mark">rad</span>

1 RADIOLOGY IMPRESSION Radiology Impression (RI)

2 RADIOLOGY PROFILE Radiology Profile (RP)

3 RADIOLOGY STATUS Radiology Status (RS)

CHOOSE 1-3: 1 \<Enter\> Radiology Impression

Enter Time Limit: 1Y// <span class="mark">\<Enter\></span>

Enter Occurrence Limit: 5// <span class="mark">\<Enter\></span>

Enter Segment: <span class="mark">\<Enter\></span>

<span id="_Ref522188910" class="anchor"></span>Figure 3: Request PDX for Patient Option—Sample User Dialogue (2 of 2)

------------------------------ Domains Selected ------------------------------

REDACTED.VA.GOV

------------------------------------------------------------------------------

Enter Domain: <span class="mark">\<Enter\></span>

PDX V1.5 - REQUEST Sep 01, 1993 08:17:12 Page: 1 of 1

Patient : PDXPATIENT,ONE Type: SC VETERAN

Patient SSN: 000-11-1111 DOB: FEB 22,1922

Entry Domain Data Segment(s) \[Time:Occurrence\]

1 REDACTED.VA.GOV PDX\*MIN RI \[1Y:5\]

Enter ?? for more actions

AE Add/Edit Request CO Copy Request

TR Transmit Request CP Change Patient

Select Action: Quit// <span class="mark">T\<Enter\></span> Transmit Request

Enter your Signature Code: <span class="mark">\<CODE\></span> SIGNATURE VERIFIED

User to notify: <span class="mark">PDXUSER,THREE</span>

-------------------------------- User Selected -------------------------------

PDXUSER,THREE

------------------------------------------------------------------------------

User to notify: <span class="mark">\<Enter\></span>

Include Data with Notification(s):? NO// <span class="mark">\<Enter\></span>

Exit Notify:? YES// <span class="mark">\<Enter\></span>

Working...

Transactions filed and queued

Press RETURN to continue: <span class="mark">\<Enter\></span>

Select Patient Name:

<span id="_Ref522188896" class="anchor"></span>Figure 4: Request PDX for Patient Option—Sample MailMan Bulletin

Subj: PDX INFORMATION RETURNED FROM REDACTED (500) \[#23493\] 2 Sep 93 13:53 9 Lines

From: PDX SERVER in ‘IN’ basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

Your request for PDX information from REDACTED (500)

has been processed and returned.

Patient: PDXPATIENT,ONE SSN: 000111111 DOB: FEB 22,1922

Local Message ID: 23490

Remote User Name: PDX Server

Status: RECORD RETURNED

Additional Text:

Select MESSAGE Action: IGNORE (in IN basket)//

### Unsolicited PDX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Unsolicited PDX option sends unsolicited PDX (Patient Data Exchange) information to a remote site(s). A remote site is any other VA facility with which data is exchanged. The patient selected *must* be in your PATIENT file.

When the data is received at the remote site, members of the VAQ UNSOLICITED RECEIVED mail group, defined through VA FileMan at the remote site, will be notified via MailMan that an unsolicited PDX has arrived from your site. A sample bulletin is provided in the example section of this option documentation.

You may select numerous domains and the particular data segments you wish to send to each domain. Segment groups, which may be set up through other PDX options, can be used during the request. These groups contain predefined data segments and allow you to request numerous segments with one entry. The proper format *must* be used when entering the domain(s). Two question marks (??) can be entered at the domain prompt for a list of network addresses shown in the required format.

An entry is made to your VAQ - WORKLOAD file for each unsolicited PDX sent.

Time and occurrence limits can be placed on applicable data segments. These will determine how far back the system will search for the component and the number of occurrences of that component the system will report. Default values for these fields can be set through the Edit Parameter File option.

A word processing field is provided for any comments you may wish to include with the transaction.

#### Process

The process chart in <u>Table 3</u> shows the steps and prompts involved in using the Unsolicited PDX option.

| Step   | At this Prompt...                                                                                                                                                                                                                                                                                                                                                 | If User Answers with...                                                   | Then Step   |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|-------------|
| 1  | Select Patient Name:                                                                                                                                                                                                                                                                                                                                              | Patient from your PATIENT (#2) file                                       | 2       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> or caret \<^\>                                          | 15      |
|        | The PDX Status screen is displayed listing any PDX transactions on file for the patient.                                                                                                                                                                                                                                                                          |                                                                           |             |
| 2  | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                             | CR to create PDX request                                              | 3       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | DP to display PDX, if one exists                                      | 12      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to accept default                                           | 1       |
|        | The PDX Unsolicited screen is displayed.                                                                                                                                                                                                                                                                                                                          |                                                                           |             |
| 3  | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                             | AE to add/edit PDX request                                            | 4       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | TR to transmit PDX, if applicable                                     | 9       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | CO to copy PDX, if applicable                                         | 14      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | CP to change to another patient                                       | 1       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to accept default                                           | 1       |
| 4  | Enter Domain:                                                                                                                                                                                                                                                                                                                                                     | E-mail address of the facility or group to which you wish to send the PDX | 5       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> (1st appearance of prompt)                                  | 3       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> (subsequent appearance)                                     | 8       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<??\> For list of domain/group addresses                             | 4       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<?\> For list of choices you may enter at this prompt                | 4       |
|        | The PDX\*MIN data segment will automatically be included in any transaction.                                                                                                                                                                                                                                                                                      |                                                                           |             |
| 5  | Enter Segment:                                                                                                                                                                                                                                                                                                                                                    | Data segment or segment group you wish to send to selected domain         | 6       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\>                                                             | 4       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<??\> for list of data segments/groups                               | 5       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<?\> for list of choices you may enter at this prompt                | 5       |
|        | Steps 6 and 7 may/may not appear depending on the data segment selected.                                                                                                                                                                                                                                                                                          |                                                                           |             |
| 6  | Time Limit:                                                                                                                                                                                                                                                                                                                                                       | Time limit to use for selected data segment                               | 7       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to not specify a limit                                      | 7       |
| 7  | Occurrence Limit:                                                                                                                                                                                                                                                                                                                                                 | Occurrence limit to use for selected date segment                         | 5       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to not specify a limit                                      | 5       |
|        | The PDX Unsolicited screen is redisplayed showing your domain and segment choices. Time and occurrence limits will be displayed with the segments, if applicable.                                                                                                                                                                                                 |                                                                           |             |
| 8  | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                             | AE to add/edit PDX request                                            | 4       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | TR to transmit PDX                                                    | 9       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | CO to copy PDX                                                        | 14      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | CP to change to another patient                                       | 1       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to accept default                                           | 1       |
|        | Your signature code *must* be previously established through the Toolbox utility.                                                                                                                                                                                                                                                                                 |                                                                           |             |
| 9  | Enter your Signature Code:                                                                                                                                                                                                                                                                                                                                        | Signature code                                                            | 10      |
| 10 | Enter PDX Unsolicited Request Comment:                                                                                                                                                                                                                                                                                                                            | Optional comment                                                          | 11      |
|        | 1\>                                                                                                                                                                                                                                                                                                                                                               | \<Enter\> to not enter a comment                                      | 1       |
| 11 | EDIT Option:                                                                                                                                                                                                                                                                                                                                                      | Edit option if you wish to edit comment                                   | 11      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<??\> for list of edit options                                       | 11      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to not edit comment or when editing is complete             | 1       |
|        | The PDX Segments screen is displayed listing all known PDXs for the selected patient. If there is more than one entry to choose from and you enter DS, you will be asked to select the desired entry(s).                                                                                                                                                          |                                                                           |             |
| 12 | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                             | DS to display a selected PDX                                          | 13      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | DA to display all listed PDXs                                         | 13      |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\> to accept default                                           | 1       |
|        | You will be prompted for a device. If you choose to print to the screen, the PDX Data Display screen is displayed showing the patient data for the selected segment (s). If the transaction did not contain information for a segment, that message will be displayed. You will proceed to step 12 or 2 depending on the number of segments selected for display. |                                                                           |             |
| 13 | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                             | \<Enter\> to accept default                                           | 12 or 2 |
|        | You may now add another domain(s) for this PDX without going through all the steps again. This prompt will be repeated until no further entries are made and you press the Enter key.                                                                                                                                                                             |                                                                           |             |
| 14 | Copy to Domain:                                                                                                                                                                                                                                                                                                                                                   | Domain or domain group name                                               | 8       |
|        |                                                                                                                                                                                                                                                                                                                                                                   | \<Enter\>                                                             | 8       |
| 15 | Return to the menu.                                                                                                                                                                                                                                                                                                                                               |                                                                           |             |

<span id="_Ref522199181" class="anchor"></span>Table 4: Process External PDX Option—Process Chart

#### Example

<u>Figure 5</u> and <u>Figure 6</u> are examples of what may appear on your screen while using the Unsolicited PDX option followed by a sample of the type of MailMan bulletin that may be received when the request is received at the remote site (<u>Figure 7</u>).

<span id="_Ref522186182" class="anchor"></span>Figure 5: Unsolicited PDX Option—Sample User Dialogue (1 of 2)

Select Patient Name: <span class="mark">PDXPATIENT,ONE \<Enter\></span> 02-22-22 000111111 SC VETERAN

PDX V1.5 - STATUS Sep 01, 1993 08:14:57 Page: 1 of 1

Patient : PDXPATIENT,ONE Type: SC VETERAN

Patient SSN: 000-11-1111 DOB: FEB 22,1922

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\*\* No PDX transactions found for this patient...

Enter ?? for more actions

CR Create Request DP Display PDX

Select Action: Quit// <span class="mark">cr \<Enter\></span> Create Request

PDX V1.5 - UNSOLICITED Sep 01, 1993 08:16:32 Page: 1 of 1

Patient : PDXPATIENT,ONE Type: SC VETERAN

Patient SSN: 000-11-1111 DOB: FEB 22,1922

Entry Domain Data Segment(s) \[Time:Occurrence\]

\*\* Select an option or \<Return\> to exit

Enter ?? for more actions

AE Add/Edit Request CO Copy Request

TR Transmit Request CP Change Patient

Select Action: Quit// <span class="mark">ae \<Enter\></span> Add/Edit Request

Enter Domain: <span class="mark">REDACTED.VA.GOV</span>

------------------------------ Segments Selected -----------------------------

PDX\*MIN

------------------------------------------------------------------------------

Enter Segment: <span class="mark">rad</span>

1 RADIOLOGY IMPRESSION Radiology Impression (RI)

2 RADIOLOGY PROFILE Radiology Profile (RP)

3 RADIOLOGY STATUS Radiology Status (RS)

CHOOSE 1-3: <span class="mark">1 \<Enter\></span> Radiology Impression

Enter Time Limit: 1Y// <span class="mark">\<Enter\></span>

Enter Occurrence Limit: 5// <span class="mark">\<Enter\></span>

Enter Segment: <span class="mark">\<Enter\></span>

<span id="_Ref522188951" class="anchor"></span>Figure 6: Unsolicited PDX Option—Sample User Dialogue (2 of 2)

------------------------------ Domains Selected ------------------------------

REDACTED.VA.GOV

------------------------------------------------------------------------------

Enter Domain: <span class="mark">\<Enter\></span>

PDX V1.5 - UNSOLICITED Sep 01, 1993 08:17:12 Page: 1 of 1

Patient : PDXPATIENT,ONE Type: SC VETERAN

Patient SSN: 000-11-1111 DOB: FEB 22,1922

Entry Domain Data Segment(s) \[Time:Occurrence\]

1 REDACTED.VA.GOV PDX\*MIN RI \[1Y:5\]

Enter ?? for more actions

AE Add/Edit Request CO Copy Request

TR Transmit Request CP Change Patient

Select Action: Quit// <span class="mark">T \<Enter\></span> Transmit Request

Enter your Signature Code: <span class="mark">\<CODE\> \<Enter\></span> SIGNATURE VERIFIED

Enter PDX Unsolicited Request Comment:

1\>Veteran is traveling to your area

2\><span class="mark">\<Enter\></span>

EDIT Option: <span class="mark">\<Enter\></span>

Working...

Transactions filed and queued

Press RETURN to continue: <span class="mark">\<Enter\></span>

Select Patient Name:

<span id="_Ref522189065" class="anchor"></span>Figure 7: Unsolicited PDX Option—Sample MailMan Bulletin

Subj: RECEIPT OF UNSOLICITED PDX \[#9852\] 2 Sep 93 13:53 17 Lines

From: PDX in ‘IN’ basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The following Unsolicited PDX has been received...

Transaction number: 1068

Name: PDXPATIENT,ONE

PID: 000111111

DOB: FEB 22,1922

Received on: SEP 2, 1993

Sent by: PDXUSER,ONE

Site: REDACTED VAMC

Domain: REDACTED.VA.GOV

Comments:

Veteran is traveling to your area

Select MESSAGE Action: IGNORE (in IN basket)//

### Process External PDX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Process External PDX option is used to process PDX requests received from other VA facilities that were not processed automatically. Members of the VAQ MANUAL PROCESSING mail group at your site will be notified of these requests via MailMan.

When this option is selected from the PDX menu, any requests in your VAQ - TRANSACTION (#394.61) file with a status of “PDX Request from remote facility that requires manual processing” will be displayed with the following information.

- Entry number—Numerical order of requests that require manual processing
- Transaction number—Assigned by receiving facility, unique identifier of the transaction
- Patient name, patient ID, patient date of birth, domain of requesting facility, segments requested, date/time of request
- Reason request needs manual processing, which include:
- Bad input or no input, error.
- Patient not found (not currently used).
- Ambiguous patient.
- Sensitive patient.
- Domain not in work group.

Requests that have “ambiguous patient” for the reason request needs manual processing can only be processed as “not found”. A mail bulletin will be sent to the remote site informing them of this. A sample of the bulletin can be found in the Example section of this option documentation.

The user selects each PDX request and determines if the data should be released or the request rejected. Once this determination has been made, you will be prompted to enter an optional release/reject comment. This comment will appear in the MailMan bulletin the requestor at the remote site will receive notifying them that the PDX has been processed and returned or rejected.

#### Process

The processing chart in <u>Table 4</u> shows the steps and prompts involved in using the Process External PDX option.

<table>
<caption><p><span id="_Ref522187190" class="anchor"></span>Table 5: Load/Edit PDX Data Option—Process Chart</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 38%" />
<col style="width: 45%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr class="header">
<th>Step</th>
<th>At this Prompt...</th>
<th>If User Answers with...</th>
<th>Then Step</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><p>The PDX Manual Process screen is displayed showing all requests requiring manual processing:</p>
<ul>
<li><p>If there is more than one from which to select, you will be prompted to choose.</p></li>
<li><p>If there are none, the message “No pending transactions queued for manual processing...” will appear.</p></li>
</ul></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td>Select Action: Quit//</td>
<td><strong>PM</strong> to process (patient found)</td>
<td><strong>3</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>PM</strong> to process (patient not found)</td>
<td><strong>2</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> or caret &lt;<strong>^</strong>&gt;</td>
<td><strong>8</strong></td>
</tr>
<tr class="odd">
<td><strong>2</strong></td>
<td>Requested patient not found...</td>
<td><strong>&lt;Enter&gt;</strong> to accept default</td>
<td><strong>4</strong></td>
</tr>
<tr class="even">
<td></td>
<td>Process as not found YES//</td>
<td><strong>NO</strong></td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>The PDX Manual Release screen is displayed showing abbreviated information for the selected request.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td>Select Action: Quit//</td>
<td><strong>RL</strong> to release data with comment</td>
<td><strong>4</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>RJ</strong> to reject data with comment</td>
<td><strong>4</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>EE</strong> to display PIMS data</td>
<td><strong>7</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong> to quit</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td></td>
<td>Your signature code <em>must</em> be previously established through the Toolbox utility. If you have reached this step from Step 2, you will return to Step 1 after your signature code is entered.</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>4</strong></td>
<td>Enter your Signature Code:</td>
<td>Signature code</td>
<td><strong>5</strong></td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td>Enter PDX {Release/Reject} Comment:</td>
<td>Optional comment</td>
<td><strong>6</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>1&gt;</td>
<td><strong>&lt;Enter&gt;</strong> to not enter a comment</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td><strong>6</strong></td>
<td>EDIT Option:</td>
<td>Edit option if you wish to edit comment</td>
<td><strong>6</strong></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td><strong>&lt;??&gt;</strong> For list of edit options</td>
<td><strong>6</strong></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td><strong>&lt;Enter&gt;</strong></td>
<td><strong>1</strong></td>
</tr>
<tr class="odd">
<td></td>
<td>The PDX Minimal screen is displayed showing PIMS data (PDX*MIN segment) for the selected request.</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>7</strong></td>
<td>Select Action: Quit//</td>
<td><strong>&lt;Enter&gt;</strong></td>
<td><strong>3</strong></td>
</tr>
<tr class="odd">
<td><strong>8</strong></td>
<td>Return to the menu.</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref522187190" class="anchor"></span>Table 5: Load/Edit PDX Data Option—Process Chart

#### Example

<u>Figure 8</u> is an example of what may appear on your screen while using the Process External PDX option.

<span id="_Ref522186619" class="anchor"></span>Figure 8: Process External PDX Option—Sample User Dialogue

Select Patient Data Exchange Option: <span class="mark">PROC \<Enter\></span> ess External PDX

PDX V1.5 - MANUAL PROCESS Sep 02, 1993 14:38:13 Page: 1 of 1

PDX Activity Requiring Manual Processing

Entry \# : 1 Trans \#: 119

Patient : PDXPATIENT,FIVE Date/Time: SEP 1,1993@14:33:58 (Rq)

Patient SS: 000-55-5555 DOB: 09-01-1953

Domain : REDACTED VAMC Reason: Domain not in release group

Segments : COPAY PDX\*MIN PDX\*MT

Enter ?? for more actions

PM Process Manual

Select Action:Quit// <span class="mark">PM \<Enter\></span> Process Manual PDXPATIENT,FIVE 09-01-53 000555555

PDX V1.5 - MANUAL RELEASE Sep 02, 1993 14:38:22 Page: 1 of 1

Remote Patient: PDXPATIENT,FIVE ID: 000-55-5555 DOB: 09-01-1953

Entry Local Patient Name DOB SSN PID

1 PDXPATIENT,FIVE 09-01-1953 000-55-5555 000-55-5555

Enter ?? for more actions

RL Release W/Comment RJ Reject W/Comment EE Expand Entry

Select Action:Quit// <span class="mark">RL \<Enter\></span> Release W/Comment

Enter your Signature Code: <span class="mark">\<CODE\> \<Enter\></span> SIGNATURE VERIFIED

Enter PDX Release Comment:

1\>OK TO RELEASE

2\>\<Enter\>

EDIT Option: <span class="mark">\<Enter\></span>

Working ...

Manual process of entry queued

Press RETURN to continue: <span class="mark">\<Enter\></span>

PDX V1.5 - MANUAL PROCESS Sep 02, 1993 14:38:59 Page: 1 of 1

PDX Activity Requiring Manual Processing

\*\* No pending transactions queued for manual processing...

Enter ?? for more actions

PM Process Manual

Select Action:Quit//

<u>Figure 9</u> is an example of the MailMan bulletin the requesting facility will receive if the request is processed as “not found”.

<span id="_Ref522186699" class="anchor"></span>Figure 9: Process External PDX Option—Sample MailMan Bulletin: Process Not Found

Subj: RESULTS OF PDX REQUEST \[#112896\] 02 Sep 93 13:17 13 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

Your request for information has been rejected...

Transaction number: 119

Name: PDXPATIENT,FIVE

PID: 000-55-5555

DOB: 09-01-1953

Requested by: PDXUSER,THREE

Requested on: SEP 01, 1993

Processed by: PDXUSER,TWENTY-FIVE

Site: REDACTED VAMC

Domain: REDACTED.VA.GOV

Reason: Domain not in release group

Select MESSAGE Action: IGNORE (in IN basket)//

<u>Figure 10</u> is an example of the MailMan notification the requesting facility will receive after you successfully process the external PDX.

<span id="_Ref522186745" class="anchor"></span>Figure 10: Process External PDX Option—Sample MailMan Bulletin: Process Successful (1 of 2)

Subj: RESULTS OF PDX REQUEST \[#112902\] 02 Sep 93 14:40 40 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------

Your request for information has been processed and returned ...

Transaction number: 119

Name: PDXPATIENT,FIVE

PID: 000-55-5555

DOB: 09-01-1953

Requested by: PDXUSER,THREE

Requested on: SEP 02, 1993

Processed by: PDXUSER,TWENTY-SIX

Site: REDACTED VAMC

Domain: REDACTED.VA.GOV

Comments:

OK TO RELEASE

The portion shown in <u>Figure 11</u> only appears if during the request YES was answered to the “Include Data with Notification(s):?” prompt.

<span id="_Ref522186798" class="anchor"></span>Figure 11: Process External PDX Option—Sample MailMan Bulletin: Process Successful (2 of 2)

Subj: RESULTS OF PDX REQUEST \[#112902\] Page 2

------------------------------------------------------------------------

Requested information:

----------------------\< MAS Minimum Patient Information \>---------------

PAT Name: PDXPATIENT,FIVE DOB: SEP 1, 1953 AGE: 40

Addr: 123 MAIN ST SSN: 000-55-5555

: Sex: MALE MS: MARR

: Religion: UNKNOWN/NO PREFERENC

City/ST: ANYTOWN, NY

Zip: 12047 County: RENSSELAER

Patient Type: NSC VETERAN Veteran: YES

Period of Service: VIETNAM ERA

Service Connected: NO Percentage: %

Eligibility: NSC

Select MESSAGE Action: IGNORE (in IN basket)//

### Load/Edit PDX Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Load/Edit PDX Data option allows you to compare and load data fields in your PATIENT (#2) file with data from your PDX file. The information in your PDX file is data that was received from other sites’ PATIENT (#2) files.

Once the patient is selected, all sites from which you have received PDX data for the selected patient will be displayed. If an entry does not exist in your PATIENT (#2) file for the selected patient, you may upload the basic information needed to enter the patient. The remainder of the data should be entered through the ADT portion of the MAS software.

If an entry already exists in your PATIENT (#2) file for the selected patient, the system looks for differences. The fields where differences are found are displayed with the headings “- PATIENT FILE -” showing the entry from your PATIENT (#2) File and “- PDX File -” showing the entry from the PDX file. The entries *must* be identical for the system to recognize them as the same. For example, if the MOST RECENT LOCATION OF CARE field is Buffalo in the PATIENT (#2) file and Buffalo, NY in the PDX file, the system would see this as a difference. Each data field showing a difference should be examined to determine if the PDX data is the most current and that you are sure you wish to place this data in your PATIENT (#2) file.

![](pdx-v-1-5-user-manual/016.png) NOTE: The extractions for PDX 1.0 and PDX 1.5 are different and some fields may be in different formats.

After you attempt to upload the data, the Load/Edit screen is redisplayed. The first part of the screen lists all the fields that could not be uploaded due to these fields not passing the criteria for uploading. You should attempt to upload these fields again. Due to the data fields that were uploaded on the first attempt now being in place, you may be more successful in uploading the remaining data elements. A list of the fields that remain after the second attempt should be printed. You may then try entering these fields through the PIMS Registration option, Load/Edit Patient Data.

Rated disabilities or other eligibility codes *must* be entered through the Update HINQs to the Patient file option of the HINQ software. Missing or ineligible information or any other data you are not successful in uploading through PDX *must* be entered through the Load/Edit Patient Data option of the Registration menu in ADT.

For multiple fields, the data from your PDX file will be added to the data in your PATIENT file. Existing data will remain intact.

You *must* hold the VAQ LOAD security key to access this option.

#### Process

The process chart in <u>Table 5</u> shows the steps and prompts involved in using the Load/Edit PDX Data option.

| Step   | At this Prompt...                                                                                                         | If User Answers with...                                                     | Then Step  |
|--------|---------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|------------|
| 1  | Identify PDX:                                                                                                             | Patient name                                                                | 3      |
|        |                                                                                                                           | Transaction number                                                          | 3      |
|        |                                                                                                                           | \<??\>                                                                  | 2      |
|        |                                                                                                                           | \<Enter\> or caret \<^\>                                            | 11     |
|        | Once you choose a display option at this prompt, applicable patients will be listed for selection.                        |                                                                             |            |
| 2  | \(1\) - All PDX transaction patients                                                                                      |                                                                             |            |
|        | \(2\) - All PDX transaction patients (results)                                                                            |                                                                             |            |
|        | \(3\) - All PDX transaction patients (unsolicited)                                                                        |                                                                             |            |
|        | Select Display Option:                                                                                                    | 1 to list ALL patients with PDX transactions                            | 1      |
|        |                                                                                                                           | 2 to list those patients for whom request results have been received    | 1      |
|        |                                                                                                                           | 3 to list those patients for whom you have unsolicited PDX transactions | 1      |
|        | The PDX Load/Edit Status screen is displayed listing the transactions for the selected patient.                           |                                                                             |            |
| 3  | Select Action: Quit//                                                                                                     | LE={entry number} to select an entry                                    | 4      |
|        |                                                                                                                           | EE={entry number}to display PIMS data                                   | 10     |
|        |                                                                                                                           | \<Enter\> to accept default                                             | 1      |
|        | Your signature code *must* be previously established through the Toolbox utility.                                         |                                                                             |            |
| 4  | Enter your Signature Code:                                                                                                | Signature code                                                              | 5      |
|        | The PDX Possible Matches screen is displayed.                                                                             |                                                                             |            |
| 5  | Select Action: Quit//                                                                                                     | UE={entry number} if a listed entry matches the selected patient        | 6      |
|        |                                                                                                                           | NP for new patient                                                      | 9      |
|        |                                                                                                                           | EE={entry number}to display PIMS data                                   | 10     |
|        |                                                                                                                           | \<Enter\> to accept default                                             | 3      |
|        | The PDX Load/Edit Data screen is displayed listing the differences between the PATIENT file and the PDX file.             |                                                                             |            |
| 6  | Select Action: Quit//                                                                                                     | LF to load selected data fields                                         | 7      |
|        |                                                                                                                           | LD to load all data fields                                              | 8      |
|        |                                                                                                                           | \<Enter\> or caret \<^\>                                            | 1      |
| 7  | Select Entry(s):                                                                                                          | Number(s) or range of numbers you wish to load                              | 8      |
|        |                                                                                                                           | Caret \<^\>                                                             | 6      |
|        | The PDX Load/Edit Data screen is redisplayed. The first part of the screen shows those fields that could not be uploaded. |                                                                             |            |
| 8  | Select Action: Quit//                                                                                                     | LF to load selected data fields                                         | 7      |
|        |                                                                                                                           | LD to load all data fields                                              | 8      |
|        |                                                                                                                           | \<Enter\> or caret \<^\>                                            | 1      |
|        | The PDX Minimal Update screen is displayed for the selected patient.                                                      |                                                                             |            |
| 9  | Select Action: Quit//                                                                                                     | AP to add patient                                                       | 3      |
|        |                                                                                                                           | \<Enter\> or caret \<^\>                                            | 3      |
|        | The PDX Minimal screen is displayed showing PIMS data (PDX\*MIN segment) for the selected request.                        |                                                                             |            |
| 10 | Select Action: Quit//                                                                                                     | \<Enter\>                                                               | 3 or 5 |
| 11 | Return to the menu.                                                                                                       |                                                                             |            |

<span id="_Ref522187900" class="anchor"></span>Table 6: Display PDX by Transaction Option—Process Chart

#### Example

<u>Figure 12</u> and <u>Figure 13</u> are examples of what may appear on your screen while using the Load/Edit PDX Data option.

<span id="_Ref522187289" class="anchor"></span>Figure 12: Load/Edit PDX Data Option—Sample User Dialogue (1 of 2)

Identify PDX: <span class="mark">??</span>

\(1\) - All PDX transaction patients

\(2\) - All PDX transaction patients (results)

\(3\) - All PDX transaction patients (unsolicited)

Select Display Option: <span class="mark">1</span>

CHOOSE FROM:

111 Name: PDXPATIENT,ZERO R Pid: 000-00-0000

113 Name: PDXPATIENT,ONE Pid: 000-11-1111

114 Name: PDXPATIENT,TWO Pid: 000-22-2222

115 Name: PDXPATIENT,THREE Pid: 000-33-3333

117 Name: PDXPATIENT,FOUR Pid: 000-44-4444

119 Name: PDXPATIENT,FIVE Pid: 000-55-5555

Identify PDX: <span class="mark">119 \<Enter\></span> (PID: 000-55-5555)

PDX V1.5 LOAD/EDIT STATUS Sep 07, 1993 08:07:19 Page: 1 of 1

Remote Patient: PDXPATIENT,FIVE ID: 000-55-5555 DOB: 09-01-1993

Entry Domain Date/Time Transaction

1 REDACTED.VA.GOV SEP 2,1993@13:26:53 (Rs) 119

2 REDACTED.VA.GOV SEP 4,1993@13:26:15 (Rs) 120

Enter ?? for more actions

LE Load/Edit EE Expand Entry

Select Action:Quit// <span class="mark">le=1 \<Enter\></span> Load/Edit

Enter your Signature Code: <span class="mark">\<CODE\> \<Enter\></span> SIGNATURE VERIFIED.

<span id="_Ref522189234" class="anchor"></span>Figure 13: Load/Edit PDX Data Option—Sample User Dialogue (2 of 2)

PDX V1.5 - POSSIBLE MATCHES Sep 07, 1993 08:07:39 Page: 1 of 1

Remote Patient: PDXPATIENT,FIVE ID: 000-55-5555 DOB: 09-05-1953

Entry Local Patient Name DOB SSN PID

1 PDXPATIENT,FIVE 09-05-1953 000-55-5555 000-55-5555

Enter ?? for more actions

UE Update Entry NP New Patient EE Expand Entry

Select Action:Quit// <span class="mark">ue \<Enter\></span> Update Entry

Please wait while MAS information is collected...

Please wait while differences are found...

PDX V1.5 LOAD/EDIT DATA Sep 07, 1993 10:26:19 Page: 1 of 1

Remote Patient: PDXPATIENT,FIVE ID: 000-55-5555 DOB: 09-05-1953

\- Patient File - - PDX File -

1 (D-WORK PHONE NUMBER)

\* no data in patient file (518) 555-9999

2 (ELIGIBILITY STATUS ENTERED BY)

PDXPATIENT,ZERO R. PDXPATIENT,SIX

Enter ?? for more actions

LF Load Field(s) LD Load Data (all)

Select Action:Quit// <span class="mark">LF \<Enter\></span> Load Field(s)

Select Entry(s): (1-2): 1-2

PDX V1.5 LOAD/EDIT DATA Sep 07, 1993 10:26:52 Page: 1 of 1

Remote Patient: PDXPATIENT,FIVE ID: 000-55-5555 DOB: 09-05-1953

\- Patient File - - PDX File -

\*\* No differences found...

Enter ?? for more actions

LF Load Field(s) LD Load Data (all)

Select Action:Quit// <span class="mark">\<Enter\></span>

Identify PDX:

## Display PDX Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display PDX by Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Display PDX by Transaction option allows you to display or print PDX data for a selected patient by transaction.

You first choose the entry you wish displayed. If two question marks (??) are entered at the first prompt, you will be presented with three groups from which to choose an entry:

- All patients with PDX transactions.
- Patients for whom request results have been received.
- Patients for whom you have unsolicited PDX transactions.

You can then display selected segments of data or all segments for that entry.

If the data segment could *not* be extracted from the remote facility, the following message is displayed:

\*\* Transaction did not contain information for segment

This will typically occur when the data segment is a Health Summary Component that is *not* active at the remote facility. In some cases, it may also indicate that a nonfatal error occurred while extracting the data. You may wish to contact the remote facility to determine if the data can be extracted, and request that this information be sent to you in an Unsolicited PDX.

#### Process

The process chart in <u>Table 6</u> shows the steps and prompts involved in using the Display PDX by Transaction option.

| Step  | At this Prompt...                                                                                                                                                                                                                                                                                                                                      | If User Answers with...                                                     | Then Step |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|-----------|
| 1 | Identify PDX:                                                                                                                                                                                                                                                                                                                                          | Patient name                                                                | 3     |
|       |                                                                                                                                                                                                                                                                                                                                                        | Transaction number                                                          | 3     |
|       |                                                                                                                                                                                                                                                                                                                                                        | \<??\>                                                                  | 2     |
|       |                                                                                                                                                                                                                                                                                                                                                        | \<Enter\> or caret \<^\>                                            | 6     |
|       | Once you choose a display option at this prompt, applicable patients will be listed for selection.                                                                                                                                                                                                                                                     |                                                                             |           |
| 2 | \(1\) - All PDX transaction patients                                                                                                                                                                                                                                                                                                                   |                                                                             |           |
|       | \(2\) - All PDX transaction patients (results)                                                                                                                                                                                                                                                                                                         |                                                                             |           |
|       | \(3\) - All PDX transaction patients (unsolicited)                                                                                                                                                                                                                                                                                                     |                                                                             |           |
|       | Select Display Option:                                                                                                                                                                                                                                                                                                                                 | 1 to list ALL patients with PDX transactions                            | 1     |
|       |                                                                                                                                                                                                                                                                                                                                                        | 2 to list those patients for whom request results have been received    | 1     |
|       |                                                                                                                                                                                                                                                                                                                                                        | 3 to list those patients for whom you have unsolicited PDX transactions | 1     |
|       | The PDX Display by Patient screen is displayed.                                                                                                                                                                                                                                                                                                        |                                                                             |           |
| 3 | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                  | SE to select an entry                                                   | 4     |
|       |                                                                                                                                                                                                                                                                                                                                                        | \<Enter\> to accept default                                             | 1     |
|       | The PDX Segments screen is displayed. If you enter DS, you will be prompted for the segment(s) you wish to display.                                                                                                                                                                                                                                    |                                                                             |           |
| 4 | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                  | DS to display a selected entry                                          | 5     |
|       |                                                                                                                                                                                                                                                                                                                                                        | DA to display all entries                                               | 5     |
|       |                                                                                                                                                                                                                                                                                                                                                        | \<Enter\> to accept default                                             | 3     |
| 5 | You will be prompted for a device. If you choose to print to the screen, the PDX Data Display screen is displayed showing all selected data segments. The default at the “Select Action:” prompt will be “Next Screen” if there are additional screens to view, or “Quit” if you are at the last data screen. Entering Quit will return you to Step 3. |                                                                             |           |
| 6 | Return to the menu                                                                                                                                                                                                                                                                                                                                     |                                                                             |           |

<span id="_Ref522188191" class="anchor"></span>Table 7: Display PDX by User Option—Process Chart

#### Example

<u>Figure 14</u> and <u>Figure 15</u> are examples of what may appear on your screen while using the Display PDX by Transaction option.

<span id="_Ref522187912" class="anchor"></span>Figure 14: Display PDX by Transaction Option—Sample User Dialogue (1 of 2)

Identify PDX: <span class="mark">PDXPATIENT,FIVE \<Enter\></span> 119 (PID: 000-55-5555)

PDX V1.5 DISPLAY BY PATIENT Sep 03, 1993 12:43:56 Page: 1 of 1

Remote Patient: PDXPATIENT,FIVE ID: 000-55-5555 DOB: 09-01-1993

Entry Domain Date/Time Trans No

1 REDACTED.VA.GOV SEP 2,1993@13:26:53 (Rs) 119

2 REDACTED.VA.GOV SEP 3,1993@08:26:15 (Rs) 120

Enter ?? for more actions

SE Select Entry

Select Action:Quit// <span class="mark">SE \<Enter\></span> Select Entry

Select Entry(s): (1-2): 1

PDX V1.5 - SEGMENTS Sep 03, 1993 12:44:09 Page: 1 of 1

Patient: PDXPATIENT,FIVE Remote Domain: REDACTED.VA.GOV

ID: 000-55-5555 Date/Time: SEP 2,1993@13:26:53

Entry Mnemonic Segment Name

1 PDX\*MIN MAS Minimum Patient Information

Enter ?? for more actions

DS Display Selected DA Display all

Select Action:Quit// <span class="mark">DA \<Enter\></span> Display all

DEVICE: HOME// <span class="mark">\<Enter\></span> LAT RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

<span id="_Ref522189296" class="anchor"></span>Figure 15: Display PDX by Transaction Option—Sample User Dialogue (2 of 2)

PDX V1.5 - DATA DISPLAY Sep 03, 1993 12:44:45 Page: 1 of 2

Patient: PDXPATIENT,FIVE Remote Domain: REDACTED.VA.GOV

ID: 000-55-5555 Date/Time: SEP 2,1993@13:26:53

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

----------------------\< MAS Minimum Patient Information \>--------------------

PAT Name: PDXPATIENT,FIVE DOB: SEP 5, 1953 AGE: 39

Addr: 123 MAIN ST SSN: 000-55-5555

: Sex: MALE MS: MARRIED

: Religion: UNKNOWN/NO PREFERENC

City/ST: ANYTOWN, NY

Zip: 12047 County: RENSSELAER

Patient Type: NSC VETERAN Veteran: YES

Period of Service: VIETNAM ERA

Service Connected: NO Percentage: %

Eligibility: NSC

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span> NEXT SCREEN

PDX V1.5 - DATA DISPLAY Sep 03, 1993 12:51:13 Page: 2 of 2

Patient: PDXPATIENT,FIVE Remote Domain: REDACTED.VA.GOV

ID: 000-55-5555 Date/Time: SEP 2,1993@13:26:53

+\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[ End of Data \]

Enter ?? for more actions

Select Action:Quit//

### Display PDX by User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Display PDX by User option allows you to display or print PDX data for a selected patient by user who requested the information.

Upon entering the option, the PDX 1.5 “Display By Requestor” screen will appear. This lists all the PDX requests by the user accessing the option. An entry is chosen from this list. Selected segments of data or all segments for this entry may then be chosen for display.

If the data segment could not be extracted from the remote facility, the following message is displayed:

\*\* Transaction did not contain information for segment

This will typically occur when the data segment is a Health Summary Component that is not active at the remote facility. In some cases, it may also indicate that a nonfatal error occurred while extracting the data. You may wish to contact the remote facility to determine if the data can be extracted, and request that this information be sent to you in an Unsolicited PDX.

#### Process

The chart in <u>Table 7</u> shows the steps and prompts involved in using the Display PDX by User option.

| Step  | At this Prompt...                                                                                                                                                                                                                                                                                                                                      | If User Answers with...            | Then Step |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|-----------|
|       | The PDX Display by Requestor screen is displayed. If you enter SE and there is more than one entry to choose from, you will be prompted for the entry you wish to display.                                                                                                                                                                             |                                    |           |
| 1 | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                  | SE to select an entry          | 2     |
|       |                                                                                                                                                                                                                                                                                                                                                        | \<Enter\> to accept default    | 4     |
|       | The PDX Segments screen is displayed. If you enter DS, you will be prompted for the segment(s) you wish to display.                                                                                                                                                                                                                                    |                                    |           |
| 2 | Select Action: Quit//                                                                                                                                                                                                                                                                                                                                  | DS to display a selected entry | 3     |
|       |                                                                                                                                                                                                                                                                                                                                                        | DA to display all entries      | 3     |
|       |                                                                                                                                                                                                                                                                                                                                                        | \<Enter\> to accept default    | 1     |
| 3 | You will be prompted for a device. If you choose to print to the screen, the PDX Data Display screen is displayed showing all selected data segments. The default at the “Select Action:” prompt will be “Next Screen” if there are additional screens to view, or “Quit” if you are at the last data screen. Entering Quit will return you to Step 1. |                                    |           |
| 4 | Return to the menu.                                                                                                                                                                                                                                                                                                                                    |                                    |           |

<span id="_Ref522195832" class="anchor"></span>Table 8: Add/Edit Outgoing Group Option—Process Chart

#### Example

<u>Figure 16</u> and <u>Figure 17</u> are examples of what may appear on your screen while using the Display PDX by User option.

<span id="_Ref522188259" class="anchor"></span>Figure 16: Display PDX by User Option—Sample User Dialogue (1 of 2)

PDX V1.5 DISPLAY BY REQUESTOR Sep 03, 1993 15:01:10 Page: 1 of 2

Requestor: SNYDER,TRACEY

Entry Domain\Patient Date/Time Tran No

1 REDACTED.VA.GOV SEP 1,1993@16:06:52 (Rs) 115

PDXPATIENT,SEVENTEEN

2 REDACTED.VA.GOV SEP 1,1993@14:38:38 (Rs) 116

PDXPATIENT,EIGHT

3 REDACTED.VA.GOV SEP 2,1993@13:26:53 (Rs) 119

PDXPATIENT,FIVE

4 REDACTED.VA.GOV SEP 2,1993@10:56:15 (Rs) 120

PDXPATIENT,NINE

\+ Enter ?? for more actions

SE Select Entry

Select Action:Next Screen// <span class="mark">se=3 \<Enter\></span> Select Entry

PDX V1.5 - SEGMENTS Sep 03, 1993 12:44:09 Page: 1 of 1

Patient: PDXPATIENT,FIVE Remote Domain: REDACTED.VA.GOV

ID: 000-55-5555 Date/Time: SEP 2,1993@13:26:53

Entry Mnemonic Segment Name

1 PDX\*MIN MAS Minimum Patient Information

Enter ?? for more actions

DS Display Selected DA Display all

Select Action:Quit// <span class="mark">DA \<Enter\></span> Display all

DEVICE: HOME// \<Enter\> LAT RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

<span id="_Ref522189362" class="anchor"></span>Figure 17: Display PDX by User Option—Sample User Dialogue (2 of 2)

PDX V1.5 - DATA DISPLAY Sep 03, 1993 12:44:45 Page: 1 of 2

Patient: PDXPATIENT,FIVE Remote Domain: REDACTED.VA.GOV

ID: 000-55-5555 Date/Time: SEP 2,1993@13:26:53

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

----------------------\< MAS Minimum Patient Information \>--------------------

PAT Name: PDXPATIENT,FIVE DOB: SEP 5, 1953 AGE: 39

Addr: 123 MAIN ST SSN: 000-55-5555

: Sex: MALE MS: MARRIED

: Religion: UNKNOWN/NO PREFERENC

City/ST: ANYTOWN, NY

Zip: 12047 County: RENSSELAER

Patient Type: NSC VETERAN Veteran: YES

Period of Service: VIETNAM ERA

Service Connected: NO Percentage: %

Eligibility: NSC

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span> NEXT SCREEN

PDX V1.5 - DATA DISPLAY Sep 03, 1993 12:51:13 Page: 2 of 2

Patient: PDXPATIENT,FIVE Remote Domain: REDACTED.VA.GOV

ID: 000-55-5555 Date/Time: SEP 2,1993@13:26:53

+\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\[ End of Data \]

Enter ?? for more actions

Select Action:Quit//

## System Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Requires Processing Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Requires Processing Report option is used to print a report of all PDX requests that require manual processing.

The transaction number, patient name, patient ID, date of birth, date requested, the individual who made the request, and the facility making the request are provided for each transaction.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/017.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 18</u> is an example of what may appear on your screen while using the Requires Processing Report option.

<span id="_Ref522188416" class="anchor"></span>Figure 18: Requires Processing Report Option—Sample User Dialogue

Select System Reports Option: <span class="mark">Requires \<Enter\></span> Processing Report

DEVICE: <span class="mark">\<Enter\></span> LAT RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Requests That Require Manual Processing SEP 1,1993 14:37 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 1152

Patient : HARRIS,EDWARD

Patient ID : 098-76-0987

Date of Birth : 07-09-43

Requested On : SEP 1,1993 08:23

Requested By : PDXUSER,FIFTEEN

Facility : SAN DIEGO VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 1158

Patient : PDXPATIENT,SEVENTEEN

Patient ID : 000-17-1717

Date of Birth : 10-10-33

Requested On : SEP 1,1993 08:32

Requested By : PDXUSER,FIFTEEN

Facility : SAN DIEGO VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Remote Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Remote Facility option is used to print a report of all PDX transactions on file by the remote facility. Trans-actions with the following statuses will be excluded.

- PDX request from remote facility being processed automatically
- PDX request from remote facility that requires manual processing
- Acknowledgement for receipt of unsolicited PDX by remote facility

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/018.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 19</u> is an example of what may appear on your screen while using the Sort By Remote Facility option followed by an example of the output (<u>Figure 20</u>).

<span id="_Ref522188690" class="anchor"></span>Figure 19: Sort By Remote Facility Option—Sample User Dialogue (1 of 2)

Select Current Transactions Report Option: <span class="mark">fac \<Enter\></span> Sort by remote facility

DEVICE: <span class="mark">B100 \<Enter\></span> RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 111

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Date Of Birth : 04-26-1947

Status : PDX Request

Segments : MAS Minimum Patient Information

Requested On : AUG 27,1993 09:41

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522188747" class="anchor"></span>Figure 20: Sort By Remote Facility Option—Sample User Dialogue (2 of 2)

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 113

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Date Of Birth : 02-22-1922

Status : Acknowledgement for receipt of PDX Request by remote facility

Segments : MAS Minimum Patient Information

Radiology Impression

Requested On : SEP 1,1993 08:18

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,SEVENTEEN

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By User That Generated Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By User That Generated Request option is used to print a report of all PDX transactions on file alphabetically by the user who generated the request. Transactions with the following statuses will be excluded:

- PDX request from remote facility being processed automatically
- PDX request from remote facility that requires manual processing
- Acknowledgement for receipt of unsolicited PDX by remote facility

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/019.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 21</u> is an example of what may appear on your screen while using the Sort By User That Generated Request option followed by an example of the output (<u>Figure 22</u>).

<span id="_Ref522189792" class="anchor"></span>Figure 21: Sort By User That Generated Request Option—Sample User Dialogue (1 of 2)

Select Current Transactions Report Option: <span class="mark">gnrt \<Enter\></span> Sort by user that generated request

DEVICE: <span class="mark">B100 \<Enter\></span> RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 111

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Date Of Birth : 04-26-1947

Status : PDX Request

Segments : MAS Minimum Patient Information

Requested On : AUG 27,1993 09:41

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522189873" class="anchor"></span>Figure 22: Sort By User That Generated Request Option—Sample User Dialogue (2 of 2)

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 113

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Date Of Birth : 02-22-1922

Status : Acknowledgement for receipt of PDX Request by remote facility

Segments : MAS Minimum Patient Information

Radiology Impression

Requested On : SEP 1,1993 08:18

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,SEVENTEEN

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Patient’s Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Patient’s Name option is used to print a report of all PDX transactions on file alphabetically by the patient’s name. Transactions with the following statuses will be excluded:

- PDX request from remote facility being processed automatically.
- PDX request from remote facility that requires manual processing.
- Acknowledgement for receipt of unsolicited PDX by remote facility.

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/020.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 23</u> is an example of what may appear on your screen while using the Sort By Patient’s Name option followed by an example of the output (<u>Figure 24</u>).

<span id="_Ref522199843" class="anchor"></span>Figure 23: Sort By Patient’s Name Option—Sample User Dialogue

Select Current Transactions Report Option: pat \<Enter\> Sort by patient’s name

DEVICE: B100 \<Enter\> RIGHT MARGIN: 80// \<Enter\>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,SEVENTEEN

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522199855" class="anchor"></span>Figure 24: Sort By Patient’s Name Option—Sample Output

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 113

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Date Of Birth : 02-22-1922

Status : Acknowledgement for receipt of PDX Request by remote facility

Segments : MAS Minimum Patient Information

Radiology Impression

Requested On : SEP 1,1993 08:18

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 111

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Date Of Birth : 04-26-1947

Status : PDX Request

Segments : MAS Minimum Patient Information

Requested On : AUG 27,1993 09:41

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Date Received

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Date Received option is used to print a report of all PDX transactions on file by date the request was received. Transactions with the following statuses will be excluded.

- PDX request from remote facility being processed automatically.
- PDX request from remote facility that requires manual processing.
- Acknowledgement for receipt of unsolicited PDX by remote facility.

You may sort for a date range or print all transactions. If you accept the default value of FIRST at the initial prompt, all transactions will be printed. If you wish to sort for a date range, enter a date at this prompt.

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/021.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 25</u> is an example of what may appear on your screen while using the Sort By Date Received option followed by an example of the output (<u>Figure 26</u>).

<span id="_Ref522200129" class="anchor"></span>Figure 25: Sort By Date Received Option—Sample User Dialogue

Select Current Transactions Report Option: <span class="mark">rcvd \<Enter\></span> Sort by date received

START WITH Date/Time of Reply: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">B100 \<Emter\></span> RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 111

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Date Of Birth : 04-26-1947

Status : PDX Request

Segments : MAS Minimum Patient Information

Requested On : AUG 27,1993 09:41

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522200138" class="anchor"></span>Figure 26: Sort By Date Received Option—Sample Output

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 113

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Date Of Birth : 02-22-1922

Status : Acknowledgement for receipt of PDX Request by remote facility

Segments : MAS Minimum Patient Information

Radiology Impression

Requested On : SEP 1,1993 08:18

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,SEVENTEEN

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By User That Released Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By User That Released Information option is used to print a report of all PDX transactions on file alphabetically by the user who released the information. Transactions with the following statuses will be excluded.

- PDX request from remote facility being processed automatically.
- PDX request from remote facility that requires manual processing.
- Acknowledgement for receipt of unsolicited PDX by remote facility.

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

The user who released the information will be PDX Server if the transaction was automatically processed.

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/022.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 27</u> is an example of what may appear on your screen while using the Sort By User That Released Information option followed by an example of the output (<u>Figure 28</u>).

<span id="_Ref522200449" class="anchor"></span>Figure 27: Sort By User That Released Information Option—Sample User Dialogue

Select Current Transactions Report Option: <span class="mark">rlsd \<Enter\></span> Sort by user that released information

DEVICE: <span class="mark">B100 \<Enter\></span> RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDX SERVER

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522200459" class="anchor"></span>Figure 28: Sort By User That Released Information Option—Sample Output

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 115

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1923

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : SNOW,JEROME

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,EIGHTEEN

Releasing Facility : WEST ROXBURY VAMC

Comments:

OK

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 119

Patient : PDXPATIENT,FIVE

Patient ID : 000-55-5555

Date Of Birth : 09-01-1993

Status : Requested information was returned

Segments : MAS Minimum Patient Information

Requested On : SEP 2,1993 13:23

Requested By : PDXUSER,EIGHT

Requesting Facility : REDACTED VAMC

Released On : SEP 2,1993 13:26

Released By : PDXUSER,NINE

Releasing Facility : SYRACUSE VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Requesting Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### INTRODUCTION

The Sort By Requesting Date option is used to print a report of all PDX transactions on file by the date the transaction was requested. Transactions with the following statuses will be excluded:

- PDX request from remote facility being processed automatically
- PDX request from remote facility that requires manual processing
- Acknowledgement for receipt of unsolicited PDX by remote facility

You can sort for a date range or print all transactions. If you accept the default value of FIRST at the initial prompt, all transactions will be printed. If you wish to sort for a date range, enter a date at this prompt.

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/023.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 29</u> is an example of what may appear on your screen while using the Sort By Requesting Date option followed by an example of the output (<u>Figure 30</u>).

<span id="_Ref522198939" class="anchor"></span>Figure 29: Sort By Requesting Date Option—Sample User Dialogue

Select Current Transactions Report Option: <span class="mark">sent \<Enter\></span> Sort by requesting date

START WITH Date/Time of Request: FIRST// <span class="mark">\<Enter\></span>

DEVICE: B100 \<Enter\> LAT RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 111

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Date Of Birth : 04-26-1947

Status : PDX Request

Segments : MAS Minimum Patient Information

Requested On : AUG 27,1993 09:41

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522198950" class="anchor"></span>Figure 30: Sort By Requesting Date Option—Sample Output

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 113

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Date Of Birth : 02-22-1922

Status : Acknowledgement for receipt of PDX Request by remote facility

Segments : MAS Minimum Patient Information

Radiology Impression

Requested On : SEP 1,1993 08:18

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,SEVENTEEN

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Status of Transaction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Status of Transaction option is used to print a report of all PDX transactions on file by transaction status. Transactions with the following statuses will be excluded.

- PDX request from remote facility being processed automatically
- PDX request from remote facility that requires manual processing
- Acknowledgement for receipt of unsolicited PDX by remote facility

The statuses will appear in the following order on the output.

- Requested patient could not be uniquely identified at remote facility
- Requested patient could not be found at remote facility
- PDX transmission that is currently being received
- Requested information was not released by remote facility
- PDX request
- Requested information was returned
- Request to transmit message using previous version
- Unsolicited PDX that was transmitted from local facility
- Acknowledgement for receipt of unsolicited PDX by remote facility
- Unsolicited PDX

The following information will be provided for each trans-action on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/024.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 31</u> is an example of what may appear on your screen while using the Sort By Status of Transaction option followed by an example of the output (<u>Figure 32</u>).

<span id="_Ref522198624" class="anchor"></span>Figure 31: Sort By Status of Transaction Option—Sample User Dialogue

Select Current Transactions Report Option: <span class="mark">stat \<Enter\></span> Sort by status of transaction

DEVICE: <span class="mark">B100 \<Enter\></span> RIGHT MARGIN: 80// <span class="mark">\<Enter\></span>

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 1

------------------------------------------------------------------------------

Transaction \# : 113

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Date Of Birth : 02-22-1922

Status : Acknowledgement for receipt of PDX Request by remote facility

Segments : MAS Minimum Patient Information

Radiology Impression

Requested On : SEP 1,1993 08:18

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522198635" class="anchor"></span>Figure 32: Sort By Status of Transaction Option—Sample Output

PDX Transactions Currently On File SEP 9,1993 08:50 PAGE 2

------------------------------------------------------------------------------

Transaction \# : 111

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Date Of Birth : 04-26-1947

Status : PDX Request

Segments : MAS Minimum Patient Information

Requested On : AUG 27,1993 09:41

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On :

Released By :

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 114

Patient : PDXPATIENT,THREE

Patient ID : 000-33-3333

Date Of Birth : 08-31-1953

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,SIXTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,SEVENTEEN

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort Criteria Defined By User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort Criteria Defined By User option is used to print a report of all PDX transactions on file where the sort criteria is determined by the user.

Several different levels of sorting may be selected through this option. You may enter two question marks (??) at the sort by prompt for a list of the available fields by which you may choose to sort the report. If you accept the default value of FIRST at a prompt, all values will be printed. If you wish to sort for a range of values, enter a value instead of accepting the default.

The following information will be provided for each transaction on the report, if applicable:

- Transaction number
- Patient name
- Patient ID
- Date of birth
- Transaction status
- Requested segments
- Requested on
- Requested by
- Requesting facility
- Released on
- Released by
- Releasing (remote) facility

Your facility will be the requesting facility unless the transaction status is “Unsolicited PDX that was transmitted from local facility”. In that case, your facility would be the releasing facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu and the VAQ RPT USER security key to access this option.

![](pdx-v-1-5-user-manual/025.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 33</u> through <u>Figure 37</u> are examples of what may appear on your screen while using the Sort Criteria Defined By User option followed by an example of the output.

<span id="_Ref522198284" class="anchor"></span>Figure 33: Sort Criteria Defined By User Option—Sample User Dialogue and Output (1 of 5)

Select Current Transactions Report Option: user \<Enter\> Sort criteria defined by user

SORT BY: Transaction Number// <span class="mark">??</span>

CHOOSE FROM:

.01 Transaction Number

.02 Current Status

.03 Patient Ptr

.04 Sensitive Patient

.05 Release Status

.06 Remote Transaction Number

.07 Remote Version Number

10 Patient’s Name

11 Patient’s SSN

12 Patient’s DOB

13 Patient ID

20 Date/Time of Request

21 Requestor

30 Requesting Site

31 Requesting Address

40 Encrypted

41 Encryption Method

50 Date/Time of Reply

51 Authorizer

60 Authorizing Site

61 Authorizing Address

70 Data in Notification

71 Notify (multiple)

80 Data Segment (multiple)

90 Purge

TYPE ‘-’ IN FRONT OF NUMERIC-VALUED FIELD TO SORT FROM HI TO LO

TYPE ‘+’ IN FRONT OF FIELD NAME TO GET SUBTOTALS BY THAT FIELD,

‘#’ TO PAGE-FEED ON EACH FIELD VALUE, ‘!’ TO GET RANKING NUMBER,

‘@’ TO SUPPRESS SUB-HEADER, ‘\]’ TO FORCE SAVING SORT TEMPLATE

TYPE \[TEMPLATE NAME\] IN BRACKETS TO SORT BY PREVIOUS SEARCH RESULTS

SORT BY: Transaction Number// <span class="mark">.05 \<Enter\></span> Release Status

START WITH Release Status: FIRST// <span class="mark">\<Enter\></span>

WITHIN Release Status, SORT BY: <span class="mark">50 \<Enter\></span> Date/Time of Reply

START WITH Date/Time of Reply: FIRST// <span class="mark">\<Enter\></span>

WITHIN Date/Time of Reply, SORT BY: <span class="mark">\<Enter\></span>

DEVICE: A138 \<Enter\> RIGHT MARGIN: 132// <span class="mark">\<Enter\></span>

<span id="_Toc520297464" class="anchor"></span>Figure 34: Sort Criteria Defined By User Option—Sample User Dialogue and Output (2 of 5)

DO YOU WANT YOUR OUTPUT QUEUED? NO// <span class="mark">y \<Enter\></span> (YES)

REQUESTED TIME TO PRINT: NOW// <span class="mark">\<Enter\></span>

REQUEST QUEUED!

PDX Transactions Currently On File SEP 10,1993 10:54 PAGE 1

------------------------------------------------------------------------------

Release Status: VAQ-REJ

Transaction \# : 118

Patient : PDXPATIENT,FOUR

Patient ID : 000-44-4444

Date Of Birth : 01-01-1955

Status : Requested information was not released by remote facility

Segments : Lab Chemistry & Hematology

MAS Minimum Patient Information

Surgery Reports

Requested On : SEP 2,1993 13:16

Requested By : PDXUSER,FOURTEEN

Requesting Facility : REDACTED VAMC

Released On : SEP 3,1993 10:45

Released By : PDXUSER,THREE

Releasing Facility :

Comments:

unidentifiable

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Toc520297465" class="anchor"></span>Figure 35: Sort Criteria Defined By User Option—Sample User Dialogue and Output (3 of 5)

PDX Transactions Currently On File SEP 10,1993 10:54 PAGE 2

------------------------------------------------------------------------------

Release Status: VAQ-RQST

Transaction \# : 115

Patient : PDXPATIENT,SEVEN

Patient ID : 000-77-7777

Date Of Birth : 08-22-1939

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 16:06

Released By : PDXUSER,NINETEEN

Releasing Facility : REDACTED VAMC

Comments:

OK

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 119

Patient : PDXPATIENT,FIVE

Patient ID : 000-55-5555

Date Of Birth : 09-01-1948

Status : Requested information was returned

Segments : MAS Minimum Patient Information

Requested On : SEP 2,1993 13:23

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On : SEP 2,1993 13:26

Released By : PDXUSER,TWENTY

Releasing Facility : REDACTED VAMC

Comments:

OK

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Toc520297466" class="anchor"></span>Figure 36: Sort Criteria Defined By User Option—Sample User Dialogue and Output (4 of 5)

PDX Transactions Currently On File SEP 10,1993 10:54 PAGE 3

------------------------------------------------------------------------------

Release Status: VAQ-RSLT

Transaction \# : 116

Patient : DUKE,PAUL

Patient ID : 098-00-2090

Date Of Birth : 01-16-1955

Status : Requested information was returned

Segments : Integrated Billing

MAS Minimum Patient Information

Means Test Information

Requested On : SEP 1,1993 14:33

Requested By : PDXUSER,THREE

Requesting Facility : REDACTED VAMC

Released On : SEP 1,1993 14:38

Released By : PDXUSER,TWENTY-ONE

Releasing Facility : REDACTED VAMC

Comments:

OK

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Transaction \# : 120

Patient : PDXPATIENT,FIVE

Patient ID : 000-55-5555

Date Of Birth : 09-05-1953

Status : Requested information was returned

Segments : MAS Minimum Patient Information

Requested On : SEP 2,1993 13:24

Requested By : PDXUSER,TWENTY-TWO

Requesting Facility : REDACTED VAMC

Released On : SEP 2,1993 13:26

Released By : PDXUSER,TWENTY-THREE

Releasing Facility : BUFFALO VAMC

Comments:

OK

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Toc520297467" class="anchor"></span>

Figure 37: Sort Criteria Defined By User Option—Sample User Dialogue and Output (5 of 5)

PDX Transactions Currently On File SEP 10,1993 10:54 PAGE 4

------------------------------------------------------------------------------

Release Status: VAQ-UNACK

Transaction \# : 123

Patient : PDXPATIENT,ZERO R.

Patient ID : 000-00-0000

Date Of Birth : 09-06-1922

Status : Unsolicited PDX

Segments : MAS Registration Information

MAS Minimum Patient Information

Requested On :

Requested By :

Requesting Facility :

Released On : SEP 7,1993 09:03

Released By : PDXUSER,TWENTY-FOUR

Releasing Facility : REDACTED VAMC

Comments:

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

## Work Load Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sort By Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Date option is used to print a work load report of all PDX transactions on file by the date/time the work was performed.

The following information will be provided for each transaction on the report, if applicable:

- Date/time work performed
- Type of work done
- User who performed the work
- Patient name
- Patient ID
- Remote facility

The remote facility will always be the external facility.

You may sort for a date range or print all transactions. If you accept the default value of FIRST at the initial prompt, all transactions will be printed. If you wish to sort for a date range, enter a date at this prompt.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/026.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 38</u> is an example of what may appear on your screen while using the Sort By Date option followed by an example of the output (<u>Figure 39</u>).

<span id="_Ref522197684" class="anchor"></span>Figure 38: Sort By Date Option—Sample User Dialogue

Select Work Load Reports Option: <span class="mark">date \<Enter\></span> Sort by date

START WITH Date/Time of Work: FIRST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">A138 \<Enter\></span> RIGHT MARGIN: 132// <span class="mark">\<Enter\></span>

DO YOU WANT YOUR OUTPUT QUEUED? NO// <span class="mark">y \<Enter\></span> (YES)

REQUESTED TIME TO PRINT: NOW// <span class="mark">\<Enter\></span>

REQUEST QUEUED!

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 1

------------------------------------------------------------------------------

Date/Time : JUL 27,1993 15:17

Work Done : Generation of a PDX Request

Done By : PDXUSER,TEN

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 17:13

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 28,1993 09:03

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522197697" class="anchor"></span>Figure 39: Sort By Date Option—Sample Output

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 2

------------------------------------------------------------------------------

Date/Time : SEP 1,1993 08:18

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FOURTEEN

Patient ID : 000-14-1414

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 11:35

Work Done : Generation of a PDX Request

Done By : PDXUSER,TWELVE

Patient : PDXPATIENT,TWO

Patient ID : 000-22-2222

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:33

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FIFTEEN

Patient ID : 000-15-1515

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:38

Work Done : Requested information was released

Done By : PDXUSER,FOUR

Patient : PDXPATIENT,THIRTEEN

Patient ID : 000-13-1313

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 2,1993 13:16

Work Done : Generation of a PDX Request

Done By : PDXUSER,THIRTEEN

Patient : PDXPATIENT,SIXTEEN

Patient ID : 000-16-1616

Remote Facility : WHITE RIVER JNCT VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Remote Facility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Remote Facility option is used to print a work load report of all PDX transactions on file by the remote facility. Within that sort, the transactions are listed by the date/time the work was performed.

The following information will be provided for each transaction on the report, if applicable:

- Date/time work performed
- Type of work done
- User who performed the work
- Patient name
- Patient ID
- Remote facility

The remote facility will always be the external facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/027.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 40</u> is an example of what may appear on your screen while using the Sort By Remote Facility option followed by an example of the output (<u>Figure 41</u>).

<span id="_Ref522197496" class="anchor"></span>Figure 40: Sort By Remote Facility Option—Sample User Dialogue

Select Work Load Reports Option: fac \<Enter\> Sort by remote facility

DEVICE: A138 \<Enter\> RIGHT MARGIN: 132// \<Enter\>

DO YOU WANT YOUR OUTPUT QUEUED? NO// y \<Enter\> (YES)

REQUESTED TIME TO PRINT: NOW// \<Enter\>

REQUEST QUEUED!

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 1

------------------------------------------------------------------------------

Date/Time : JUL 27,1993 17:13

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 28,1993 09:03

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:38

Work Done : Requested information was released

Done By : PDXUSER,FOUR

Patient : PDXPATIENT,THIRTEEN

Patient ID : 000-13-1313

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522197512" class="anchor"></span>Figure 41: Sort By Remote Facility Option—Sample Output

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 2

------------------------------------------------------------------------------

Date/Time : SEP 1,1993 11:35

Work Done : Generation of a PDX Request

Done By : PDXUSER,TWELVE

Patient : PDXPATIENT,TWO

Patient ID : 000-22-2222

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 15:17

Work Done : Generation of a PDX Request

Done By : PDXUSER,TEN

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 08:18

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FOURTEEN

Patient ID : 000-14-1414

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:33

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FIFTEEN

Patient ID : 000-15-1515

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 2,1993 13:16

Work Done : Generation of a PDX Request

Done By : PDXUSER,THIRTEEN

Patient : PDXPATIENT,SIXTEEN

Patient ID : 000-16-1616

Remote Facility : WHITE RIVER JNCT VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Patient’s Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Patient’s Name option is used to print a work load report of all PDX transactions on file by the patient’s name. Within that sort, the transactions are listed by the date/time the work was performed.

The following information will be provided for each transaction on the report, if applicable:

- Date/time work performed
- Type of work done
- User who performed the work
- Patient name
- Patient ID
- Remote facility

The remote facility will always be the external facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/028.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 42</u> is an example of what may appear on your screen while using the Sort By Patient’s Name option followed by an example of the output (<u>Figure 43</u>).

<span id="_Ref522197288" class="anchor"></span>Figure 42: Sort By Patient’s Name Option—Sample User Dialogue

Select Work Load Reports Option: pat \<Enter\> Sort by patient’s name

DEVICE: A138 \<Enter\> RIGHT MARGIN: 132// \<Enter\>

DO YOU WANT YOUR OUTPUT QUEUED? NO// y \<Enter\> (YES)

REQUESTED TIME TO PRINT: NOW// \<Enter\>

REQUEST QUEUED!

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 1

------------------------------------------------------------------------------

Date/Time : SEP 1,1993 08:18

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FOURTEEN

Patient ID : 000-14-1414

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 11:35

Work Done : Generation of a PDX Request

Done By : PDXUSER,TWELVE

Patient : PDXPATIENT,TWO

Patient ID : 000-22-2222

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:38

Work Done : Requested information was released

Done By : PDXUSER,FOUR

Patient : PDXPATIENT,THIRTEEN

Patient ID : 000-13-1313

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522197303" class="anchor"></span>Figure 43: Sort By Patient’s Name Option—Sample Output

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 2

------------------------------------------------------------------------------

Date/Time : SEP 2,1993 13:16

Work Done : Generation of a PDX Request

Done By : PDXUSER,THIRTEEN

Patient : PDXPATIENT,SIXTEEN

Patient ID : 000-16-1616

Remote Facility : WHITE RIVER JNCT VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:33

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FIFTEEN

Patient ID : 000-15-1515

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 17:13

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 28,1993 09:03

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 15:17

Work Done : Generation of a PDX Request

Done By : PDXUSER,TEN

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort Criteria Defined By User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### INTRODUCTION

The Sort Criteria Defined By User option is used to print a work load report of all PDX transactions on file where the sort criteria is determined by the user.

Several different levels of sorting may be selected through this option. You can enter two question marks (??) at the sort by prompt for a list of the available fields by which you may choose to sort the report. If you accept the default value of FIRST at a prompt, all values will be printed. If you wish to sort for a range of values, enter a value instead of accepting the default.

The following information will be provided for each transaction on the report, if applicable:

- Date/time work performed
- Type of work done
- User who performed the work
- Patient name
- Patient ID
- Remote facility

The remote facility will always be the external facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu and the VAQ RPT USER key to access this option.

![](pdx-v-1-5-user-manual/029.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 44</u> is an example of what may appear on your screen while using the Sort Criteria Defined By User option followed by an example of the output (<u>Figure 45</u> and <u>Figure 46</u>).

<span id="_Ref522197018" class="anchor"></span>Figure 44: Sort Criteria Defined By User Option—Sample User Dialogue

Select Work Load Reports Option: <span class="mark">user \<Enter\></span> Sort criteria defined by user

SORT BY: Date/Time of Work// <span class="mark">??</span>

CHOOSE FROM:

.01 Date/Time of Work

.02 Done By

.03 Work Done

10 Patient Ptr

11 Patient’s Name

12 Patient’s SSN

13 Patient ID

20 Remote Facility

21 Remote Domain

30 Segment in Transaction (multiple)

TYPE ‘-’ IN FRONT OF NUMERIC-VALUED FIELD TO SORT FROM HI TO L

TYPE ‘+’ IN FRONT OF FIELD NAME TO GET SUBTOTALS BY THAT FIELD

‘#’ TO PAGE-FEED ON EACH FIELD VALUE, ‘!’ TO GET RANKING N

‘@’ TO SUPPRESS SUB-HEADER, ‘\]’ TO FORCE SAVING SORT TEMP

TYPE \[TEMPLATE NAME\] IN BRACKETS TO SORT BY PREVIOUS SEARCH RE

SORT BY: Date/Time of Work// <span class="mark">Work Done</span>

START WITH Work Done: FIRST// <span class="mark">\<Enter\></span>

WITHIN Work Done, SORT BY: <span class="mark">Done By</span>

START WITH Done By: FIRST// <span class="mark">\<Enter\></span>

WITHIN Done By, SORT BY: <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">A200 \<Enter\></span> RIGHT MARGIN: 132// <span class="mark">\<Enter\></span>

DO YOU WANT YOUR OUTPUT QUEUED? NO// <span class="mark">y \<Enter\></span> (YES)

REQUESTED TIME TO PRINT: NOW// <span class="mark">\<Enter\></span>

REQUEST QUEUED!

<span id="_Ref522197050" class="anchor"></span>Figure 45: Sort Criteria Defined By User Option—Sample Output (1 of 2)

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 1

------------------------------------------------------------------------------

Date/Time : SEP 2,1993 13:16

Work Done : Generation of a PDX Request

Done By : PDXUSER,THIRTEEN

Patient : PDXPATIENT,SIXTEEN

Patient ID : 000-16-1616

Remote Facility : WHITE RIVER JNCT VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 08:18

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FOURTEEN

Patient ID : 000-14-1414

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:33

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FIFTEEN

Patient ID : 000-15-1515

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 15:17

Work Done : Generation of a PDX Request

Done By : PDXUSER,TEN

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 11:35

Work Done : Generation of a PDX Request

Done By : PDXUSER,TWELVE

Patient : PDXPATIENT,TWO

Patient ID : 000-22-2222

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522197066" class="anchor"></span>Figure 46: Sort Criteria Defined By User Option—Sample Output (2 of 2)

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 2

------------------------------------------------------------------------------

Date/Time : SEP 1,1993 14:38

Work Done : Requested information was released

Done By : PDXUSER,FOUR

Patient : PDXPATIENT,THIRTEEN

Patient ID : 000-13-1313

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 17:13

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 28,1993 09:03

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

### Sort By Type of Work Done

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Sort By Type of Work Done option is used to print a work load report of all PDX transactions on file by the type of work that was performed. Within that sort, the transactions are listed by the date/time the work was performed.

The following information will be provided for each transaction on the report, if applicable:

- Date/time work performed
- Type of work done
- User who performed the work
- Patient name
- Patient ID
- Remote facility

The remote facility will always be the external facility.

This report may be quite lengthy. It is *recommended* you queue the report to a printer during off hours.

You *must* hold the VAQ RPT security key to access the System Reports menu.

![](pdx-v-1-5-user-manual/030.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 47</u> is an example of what may appear on your screen while using the Sort By Type of Work Done option followed by an example of the output (<u>Figure 48</u>).

<span id="_Ref522196631" class="anchor"></span>Figure 47: Sort By Type of Work Done Option—Sample User Dialogue (1 of 2)

Select Work Load Reports Option: <span class="mark">work \<Enter\></span> Sort by type of work done

DEVICE: <span class="mark">A138 \<Enter\></span> RIGHT MARGIN: 132// <span class="mark">\<Enter\></span>

DO YOU WANT YOUR OUTPUT QUEUED? NO// <span class="mark">y \<Enter\></span> (YES)

REQUESTED TIME TO PRINT: NOW// <span class="mark">\<Enter\></span>

REQUEST QUEUED!

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 1

------------------------------------------------------------------------------

Date/Time : JUL 27,1993 15:17

Work Done : Generation of a PDX Request

Done By : PDXUSER,TEN

Patient : PDXPATIENT,ZERO R

Patient ID : 000-00-0000

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 08:18

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FOURTEEN

Patient ID : 000-14-1414

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 11:35

Work Done : Generation of a PDX Request

Done By : PDXUSER,TWELVE

Patient : PDXPATIENT,TWO

Patient ID : 000-22-2222

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

<span id="_Ref522196652" class="anchor"></span>Figure 48: Sort By Type of Work Done Option—Sample User Dialogue (2 of 2)

Work Done Using Patient Data Exchange (PDX) SEP 10,1993 15:34 PAGE 2

------------------------------------------------------------------------------

Date/Time : SEP 1,1993 14:33

Work Done : Generation of a PDX Request

Done By : PDXUSER,ELEVEN

Patient : PDXPATIENT,FIFTEEN

Patient ID : 000-15-1515

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 2,1993 13:16

Work Done : Generation of a PDX Request

Done By : PDXUSER,THIRTEEN

Patient : PDXPATIENT,SIXTEEN

Patient ID : 000-16-1616

Remote Facility : WHITE RIVER JNCT VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : SEP 1,1993 14:38

Work Done : Requested information was released

Done By : PDXUSER,FOUR

Patient : PDXPATIENT,THIRTEEN

Patient ID : 000-13-1313

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 27,1993 17:13

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

Date/Time : JUL 28,1993 09:03

Work Done : Sending of an Unsolicited PDX

Done By : PDXUSER,TWO

Patient : PDXPATIENT,ONE

Patient ID : 000-11-1111

Remote Facility : REDACTED VAMC

\* \* \* \* \* \* \* \* \* \* \* \* \* \* \* \*

## PDX Edit Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add/Edit Fields to Encrypt

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### INTRODUCTION

The Add/Edit Fields to Encrypt option allows the user to select data fields to be encrypted in the PDX transmission. Four fields from the PATIENT (#2) file and two fields from the PRESCRIPTION (#52) file are sent with the software. Sites may wish to encrypt other data fields that contain patient identification information. An incrementing number is used to uniquely enter each field requiring encryption. If a plus sign (+) is entered at the Select VAQ - ENCRYPTED FIELDS Encrypt Field: prompt, the system will automatically determine the incrementing number.

The Encrypt Fields site parameter *must* be set to YES in order to correctly use this option.

You *must* hold the VAQ EDIT FILE security key to access the Add/Edit Fields to Encrypt option.

![](pdx-v-1-5-user-manual/031.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 49</u> is an example of what may appear on your screen while using the Add/Edit Fields to Encrypt option.

<span id="_Ref522196406" class="anchor"></span>Figure 49: Add/Edit Fields to Encrypt Option—Sample User Dialogue

Select VAQ - ENCRYPTED FIELDS Encrypt Field: <span class="mark">??</span>

CHOOSE FROM:

1 FILE: 2 FIELD: .01

2 FILE: 2 FIELD: .09

3 FILE: 52 FIELD: 6

4 FILE: 2.01 FIELD: .01

5 FILE: 2.01 FIELD: 1

6 FILE: 52 FIELD: 2

Incrementing number used to uniquely identify each entry. Entering

‘+’ will automatically determine this number.

Select VAQ - ENCRYPTED FIELDS Encrypt Field: <span class="mark">+</span>

ARE YOU ADDING ‘7’ AS A NEW VAQ - ENCRYPTED FIELDS (THE 7TH)? <span class="mark">Y \<Enter\></span> (YES)

Encrypt Field: 7// <span class="mark">\<Enter\></span>

File: <span class="mark">2</span>

Field: <span class="mark">.03</span>

Select VAQ - ENCRYPTED FIELDS Encrypt Field:

### Edit maximum limits for automatic processing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### INTRODUCTION

The Edit maximum limits for automatic processing option is used to edit the maximum time and occurrence limits that your site is willing to allow for automatic processing of a PDX transaction. The limits entered here for each data segment will be compared to the limits contained in the request from the remote site. If a requested data segment’s limits are over this maximum, the request will require manual processing.

If the request requires manual processing, the members of the VAQ MANUAL PROCESSING mail group will receive the PDX Request Requires Processing mail bulletin. An example of this bulletin is contained in the Example section of this option documentation.

You *must* hold the VAQ EDIT FILE security key to access this option.

![](pdx-v-1-5-user-manual/032.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 50</u> is an example of what may appear on your screen while using the Edit maximum limits for automatic processing option.

<span id="_Ref522196080" class="anchor"></span>Figure 50: Edit maximum limits for automatic processing Option—Sample User Dialogue

Select VAQ - DATA SEGMENT Data Segment Name: <span class="mark">ri \<Enter\></span> Radiology Impression (RI)

Maximum Time Limit: 1Y// <span class="mark">\<Enter\></span>

Maximum Occurrence Limit: 10// <span class="mark">\<Enter\></span>

Select VAQ - DATA SEGMENT Data Segment Name: <span class="mark">LAB</span>

1 LAB BLOOD AVAILABILITY Lab Blood Availability (BA)

2 LAB BLOOD TRANSFUSIONS Lab Blood Transfusions (BT)

3 LAB CHEMISTRY & HEMATOLOGY Lab Chemistry & Hematology (CH)

4 LAB CUMULATIVE-SELECTED Lab Cumulative-Selected (SCLU)

5 LAB CUMULATIVE-SELECTED 1 Lab Cumulative-Selected 1 (SCL1)

6 LAB CUMULATIVE-SELECTED 2 Lab Cumulative-Selected 2 (SCL2)

TYPE ‘^’ TO STOP, OR

CHOOSE 1-6: <span class="mark">6 \<Enter\></span> Lab Cumulative-Selected 2

Maximum Time Limit: 1Y// <span class="mark">\<Enter\></span>

Maximum Occurrence Limit: 10// <span class="mark">\<Enter\></span>

Select VAQ - DATA SEGMENT Data Segment Name:

<u>Figure 51</u> is an example of the mail bulletin generated when a request requires manual processing.

<span id="_Ref522195957" class="anchor"></span>Figure 51: Edit maximum limits for automatic processing Option—Sample MailMan Bulletin

Subj: PDX REQUEST REQUIRES PROCESSING \[#112896\] 02 Sep 93 13:17 13 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

The following PDX Request requires manual processing ...

Transaction number: 119

Name: PDXPATIENT,FIVE

PID: 000-55-5555

DOB: 09-01-1953

Requested by: PDXUSER,THREE

Site: ISC REGION 1

Domain: DEMO.ISC-REDACTED.VA.GOV

Reason for manual processing:

Maximum time & occurrence limits exceeded by 1 segment

Segments that were over the allowable time & occurrence limits:

Requested Maximum Requested Maximum

Segment Time Time Occurrence Occurrence

------- --------- ------- ---------- ----------

VS 2Y 1Y 10 10

Select MESSAGE Action: IGNORE (in IN basket)//

### Add/Edit Outgoing Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Add/Edit Outgoing Group option is used to create outgoing groups and add/edit/delete remote facilities in those groups. A site may create as many outgoing groups as it deems necessary.

Creating outgoing groups allows for expeditious sending of PDX requests as they may be sent to many remote facilities with one entry, the outgoing group name.

#### Process

The process chart in <u>Table 8</u> shows the steps and prompts involved in using the Add/Edit Outgoing Group option.

| Step  | At this Prompt...                                                                                 | If User Answers with...                                | Then Step |
|-------|---------------------------------------------------------------------------------------------------|--------------------------------------------------------|-----------|
| 1 | Select VAQ - OUTGOING GROUP                                                                       |                                                        |           |
|       | Group Name:                                                                                       | New group name                                         | 2     |
|       |                                                                                                   | Existing group name                                    | 3     |
|       |                                                                                                   | \<Enter\> or caret \<^\>                       | 8     |
| 2 | ARE YOU ADDING ‘{step 1 entry}’ AS A NEW VAQ - OUTGOING GROUP(THE nTH)?                           | YES                                                | 3     |
|       |                                                                                                   | NO                                                 | 1     |
| 3 | Group Name: {name}//                                                                              | \<Enter\> to accept default                        | 4     |
|       |                                                                                                   | Correct name                                           | 4     |
|       |                                                                                                   | At-sign (@) to delete group                        | 1     |
| 4 | Select Remote Facility:                                                                           | New facility for this group                            | 5     |
|       |                                                                                                   | Existing facility contained in this group              | 6     |
|       |                                                                                                   | \<Enter\> (default)                                | 6     |
|       |                                                                                                   | \<Enter\> (no default)                             | 1     |
| 5 | ARE YOU ADDING ‘{step 4 entry}’ AS A NEW Remote Facility (THE nTH FOR THIS VAQ - OUTGOING GROUP)? | YES                                                | 4     |
|       |                                                                                                   | NO                                                 | 4     |
| 6 | Remote Facility: {name}//                                                                         | \<Enter\> to accept default                        | 7     |
|       |                                                                                                   | At-sign (@) to delete facility from outgoing group | 4     |
| 7 | Remote Domain:                                                                                    | Electronic mail address of selected remote facility    | 4     |
|       |                                                                                                   | \<??\> for list of addresses                       | 7     |
| 8 | Return to the menu                                                                                |                                                        |           |

<span id="_Ref522195459" class="anchor"></span>Table 9: PDX Parameters

#### Example

<u>Figure 52</u> is an example of what may appear on your screen while using the Add/Edit Outgoing Group option.

<span id="_Ref522195742" class="anchor"></span>Figure 52: Add/Edit Outgoing Group Option—Sample User Dialogue

Select VAQ - OUTGOING GROUP Group Name: <span class="mark">eastern</span>

ARE YOU ADDING ‘eastern’ AS A NEW VAQ - OUTGOING GROUP (THE 2ND)? <span class="mark">Y \<Enter\></span> (YES)

Group Name: eastern// <span class="mark">\<Enter\></span>

Select Remote Facility: <span class="mark">REDACTED, MA \<EnteR\></span> 518

ARE YOU ADDING ‘REDACTED, MA’ AS A NEW Remote Facility (THE 1ST FOR THIS

VAQ - OUTGOING GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Remote Domain: <span class="mark">REDACTED.VA.GOV</span>

Select Remote Facility: <span class="mark">REDACTED</span>

1 REDACTED OC, MA 750

2 REDACTED, MA 523

3 REDACTED-RO MASSACHUSETTS 301

CHOOSE 1-3: <span class="mark">2</span>

ARE YOU ADDING ‘REDACTED, MA’ AS A NEW Remote Facility (THE 2ND FOR THIS

VAQ - OUTGOING GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Remote Domain: <span class="mark">REDACTED</span>

1 REDACTED-OC.VA.GOV

2 REDACTED.VA.GOV

CHOOSE 1-2: <span class="mark">2</span>

Select Remote Facility: <span class="mark">\<Enter\></span>

Select VAQ - OUTGOING GROUP Group Name:

### Edit Parameter File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Edit Parameter File option is used to set site-specific PDX parameters. Your site should be the only entry in this file. You *must* hold the VAQ EDIT FILE security key to access this option.

<u>Table 9</u> lists the PDX parameters with a brief description:

<table>
<caption><p><span id="_Ref522195085" class="anchor"></span>Table 10: Edit Parameter File Option—Process Chart</p></caption>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DOMAIN</td>
<td>The electronic mail address of the facility or primary division.</td>
</tr>
<tr class="even">
<td>LIFETIME OF DATA</td>
<td>The number of days the PDX will be valid. The PDX will be flagged for purging after this time and will not be displayed when using display options. <strong>Fifteen</strong> (<strong>15</strong>) days is the <em>recommended</em> time.</td>
</tr>
<tr class="odd">
<td>ENCRYPT FIELDS</td>
<td><p>(<strong>YES/NO</strong>) A <strong>YES</strong> entry will allow encryption of selected data fields through the Add/Edit Fields to Encrypt option. The <em>recommended</em> response is <strong>NO</strong>.</p>
<p>![](pdx-v-1-5-user-manual/033.png) <strong>NOTE:</strong> When processing, this field is overwritten by the setting at the requesting facility. For example, if your site receives an encrypted request, your site will send an encrypted response regardless of how this field is set. If you receive an unencrypted request, you will send an unencrypted response.</p></td>
</tr>
<tr class="even">
<td>ENCRYPTION METHOD</td>
<td><p>The method of encryption to use for PDX requests and unsolicited PDXs. This field is only relevant when the ENCRYPT FIELDS field is set to <strong>YES</strong>.</p>
<p>There is only one encryption method available at this time: Kernel Hashing.</p></td>
</tr>
<tr class="odd">
<td>DEFAULT TIME LIMIT</td>
<td>The default number of days/months/years you are asking the remote system to the search back through a patient’s data (your system on unsolicited requests). It consists of a number and letter (e.g., <strong>30D</strong>, <strong>6M</strong>, <strong>1Y</strong>). This parameter will only apply to applicable data segments predetermined by the system.</td>
</tr>
<tr class="even">
<td>DEFAULT OCCURRENCE LIMIT</td>
<td>The default number of occurrences of a data segment you are asking the remote system to report (your system on unsolicited requests). For example, if a <strong>5</strong> is entered, the system will report the five most recent occurrences of that segment. This parameter will only apply to applicable data segments predetermined by the system.</td>
</tr>
</tbody>
</table>

<span id="_Ref522195085" class="anchor"></span>Table 10: Edit Parameter File Option—Process Chart

#### Process

The process chart in <u>Table 10</u> shows the steps and prompts involved in using the Edit Parameter File option.

| Step  | At this Prompt...                                                                                                                           | If User Answers with...                                                                                                                                                                                                                           | Then Step |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| 1 | Select VAQ - PARAMETER Facility:                                                                                                            | Name of your facility                                                                                                                                                                                                                             | 2     |
|       |                                                                                                                                             | \<Enter\> or caret \<^\>                                                                                                                                                                                                                  | 9     |
| 2 | Facility: {entry at Step 1}//                                                                                                               | \<Enter\> to accept default                                                                                                                                                                                                                       | 3     |
|       |                                                                                                                                             | Correct facility name                                                                                                                                                                                                                             | 3     |
|       | If you are editing an existing entry, the following fields may appear with default values. You may enter a \<Enter\> to accept the default. |                                                                                                                                                                                                                                                   |           |
| 3 | Domain:                                                                                                                                     | E-Mail address of the main facility                                                                                                                                                                                                               | 4     |
|       |                                                                                                                                             | \<??\> for list of domains                                                                                                                                                                                                                    | 3     |
| 4 | Lifetime of Data:                                                                                                                           | Number of days PDX is valid (*recommend*15 days)                                                                                                                                                                                             | 5     |
| 5 | Encrypt Fields:                                                                                                                             | YES to encrypt selected fields                                                                                                                                                                                                                | 6     |
|       |                                                                                                                                             | NO                                                                                                                                                                                                                                            | 6     |
| 6 | Encryption Method:                                                                                                                          | Method of encryption to use for PDX requests and unsolicited PDXs                                                                                                                                                                                 | 7     |
|       |                                                                                                                                             | \<??\> For a list of encryption methods                                                                                                                                                                                                       | 6     |
| 7 | Default Time Limit:                                                                                                                         | Number and letter that represent the default number of days/months/years you wish the remote system to search back through a patient’s data on applicable data segments (your system on unsolicited requests) (e.g., 30D or 6M or 1Y) | 8     |
| 8 | Default Occurrence Limit:                                                                                                                   | Default number of occurrences of a data segment you are asking the remote system to report (your system on unsolicited requests)                                                                                                                  | 1     |
| 9 | Return to the menu.                                                                                                                         |                                                                                                                                                                                                                                                   |           |

<span id="_Ref522194648" class="anchor"></span>Table 11: Add/Edit Segment Group - Private Option—Process Chart

#### EXAMPLE

<u>Figure 53</u> is an example of what may appear on your screen while using the Edit Parameter File option.

<span id="_Ref522194931" class="anchor"></span>Figure 53: Edit Parameter File Option—Sample User Dialogue

Select VAQ - PARAMETER Facility: <span class="mark">REDACTED \<Enter\></span> ALASKA 11000

Facility: REDACTED// <span class="mark">\<Enter\></span>

Domain: <span class="mark">REDACTED.VA.GOV</span>

Lifetime of Data: <span class="mark">30</span>

Encrypt Fields: <span class="mark">NO</span>

Encryption Method: <span class="mark">\<Enter\></span>

Default Time Limit: <span class="mark">1Y</span>

Default Occurrence Limit: <span class="mark">5</span>

Select VAQ - PARAMETER Facility:

### Add/Edit Segment Group - Private

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Add/Edit Segment Group - Private option is used to enter/edit private segment groups. A private segment group is one that only the person who created it can use when requesting PDX data.

A segment group is a group of selected data segments. It may contain any number of the currently available data segments. All segment groups will automatically contain the PDX\*MIN data segment, which is the minimal amount of patient data necessary to add a patient to the data base.

Data segments are comprised of Health Summary, Means Test, Copay, and specially created PDX components.

![](pdx-v-1-5-user-manual/034.png) NOTE: It should be noted that some segments may contain overlapping information. You may *not* add/edit/delete the data within the data segments.

Time and occurrence limits can be placed on applicable data segments selected for the segment group. These will determine how far back the system will search for the component and the number of occurrences of that component the system will report. The initial default values for these fields are set through the Edit Parameter File option.

Creating segment groups allows for expeditious requesting/sending of information as numerous data segments may be requested/sent by one entry, the segment group name.

#### Process

The process chart in <u>Table 11</u> shows the steps and prompts involved in using the Add/Edit Segment Group - Private option.

| Step  | At this Prompt...                                                                                                                 | If User Answers with...                           | Then Step  |
|-------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|------------|
| 1 | Select VAQ - SEGMENT GROUP                                                                                                        |                                                   |            |
|       | Group Name:                                                                                                                       | New group name                                    | 2      |
|       |                                                                                                                                   | Existing group name                               | 3      |
|       |                                                                                                                                   | \<Enter\> or caret \<^\>                  | 9      |
| 2 | ARE YOU ADDING ‘{step 1 entry}’ AS A NEW VAQ - SEGMENT GROUP?                                                                     | YES                                           | 3      |
|       |                                                                                                                                   | NO                                            | 1      |
| 3 | Group Name: {name}//                                                                                                              | \<Enter\> to accept default                   | 4      |
|       |                                                                                                                                   | Correct name                                      | 4      |
|       |                                                                                                                                   | At-sign (@) to delete group                   | 1      |
| 4 | Select Data Segment:                                                                                                              | New data segment for this group                   | 5      |
|       |                                                                                                                                   | Existing data segment contained in this group     | 6      |
|       |                                                                                                                                   | \<Enter\> (default)                           | 6      |
|       |                                                                                                                                   | \<Enter\> (no default)                        | 1      |
|       |                                                                                                                                   | \<??\> for list of data segments              | 4      |
|       | If the selected data segment does not require time or occurrence limits, you will return to Step 4 after your entry at this step. |                                                   |            |
| 5 | ARE YOU ADDING ‘{step 4 entry}’ AS A NEW Data Segment (THE nTH FOR THIS VAQ - SEGMENT GROUP)?                                     | YES                                           | 7 or 4 |
|       |                                                                                                                                   | NO                                            | 7 or 4 |
| 6 | Data Segment: {name}//                                                                                                            | \<Enter\> to accept default                   | 7      |
|       |                                                                                                                                   | At-sign (@) to delete data segment            | 4      |
|       | Steps 7 and 8 may/may not appear depending on the data segment selected.                                                          |                                                   |            |
| 7 | Time Limit:                                                                                                                       | Time limit to use for selected data segment       | 8      |
|       |                                                                                                                                   | \<Enter\> to not specify a limit              | 8      |
| 8 | Occurrence Limit:                                                                                                                 | Occurrence limit to use for selected date segment | 4      |
|       |                                                                                                                                   | \<Enter\> to not specify a limit              | 4      |
| 9 | Return to the menu.                                                                                                               |                                                   |            |

<span id="_Ref522194310" class="anchor"></span>Table 12: Add/Edit Segment Group - Public Option—Process Chart

#### Example

<u>Figure 54</u> is an example of what may appear on your screen while using the Add/Edit Segment Group - Private option.

<span id="_Ref522194545" class="anchor"></span>Figure 54: Add/Edit Segment Group - Private Option—Sample User Dialogue

Select VAQ - SEGMENT GROUP Group Name: <span class="mark">basic</span>

ARE YOU ADDING ‘basic’ AS A NEW VAQ - SEGMENT GROUP? <span class="mark">Y \<Enter\></span> (YES)

Group Name: basic// <span class="mark">\<Enter\></span>

Select Data Segment: <span class="mark">LAB ORDERS</span>

1 LAB ORDERS Lab Orders (LO)

2 LAB ORDERS BRIEF Lab Orders Brief (BLO)

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> Lab Orders

ARE YOU ADDING ‘Lab Orders’ AS A NEW Data Segment (THE 1ST FOR THIS VAQ - SEGMENT GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Time Limit: <span class="mark">6M</span>

Occurrence Limit: <span class="mark">3</span>

Select Data Segment: <span class="mark">MAS ADT HISTORY \<Enter\></span> MAS ADT History (ADT)

ARE YOU ADDING ‘MAS ADT History’ AS A NEW Data Segment (THE 2ND FOR THIS

VAQ - SEGMENT GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Time Limit: <span class="mark">\<Enter\></span>

Occurrence Limit: <span class="mark">1</span>

Select Data Segment: <span class="mark">\<Enter\></span>

Select VAQ - SEGMENT GROUP Group Name:

### Add/Edit Segment Group - Public

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Add/Edit Segment Group - Public option is used to enter/edit public segment groups. A public segment group is one that can be used by any user when requesting PDX data. You *must* hold the VAQ EDIT FILE security key to access this option.

A segment group is a group of selected data segments. It may contain any number of the currently available data segments. All segment groups will automatically contain the PDX\*MIN data segment, which is the minimal amount of patient data necessary to add a patient to the data base.

Data segments are comprised of Health Summary, Means Test, Copay, and specially created PDX components.

![](pdx-v-1-5-user-manual/035.png) NOTE: It should be noted that some segments may contain overlapping information. You may *not* add/edit/delete the data within the data segments.

Time and occurrence limits can be placed on applicable data segments selected for the segment group. These will determine how far back the system will search for the component and the number of occurrences of that component the system will report. The initial default values for these fields are set through the Edit Parameter File option.

Creating segment groups allows for expeditious requesting/sending of information as numerous data segments can be requested/sent by one entry, the segment group name.

#### Process

The process chart in <u>Table 12</u> shows the steps and prompts involved in using the Add/Edit Segment Group - Public option.

| Step  | At this Prompt...                                                                                                                 | If User Answers with...                           | Then Step  |
|-------|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|------------|
| 1 | Select VAQ - SEGMENT GROUP                                                                                                        |                                                   |            |
|       | Group Name:                                                                                                                       | New group name                                    | 2      |
|       |                                                                                                                                   | Existing group name                               | 3      |
|       |                                                                                                                                   | \<Enter\> or caret \<^\>                  | 9      |
| 2 | ARE YOU ADDING ‘{step 1 entry}’ AS A NEW VAQ - SEGMENT GROUP?                                                                     | YES                                           | 3      |
|       |                                                                                                                                   | NO                                            | 1      |
| 3 | Group Name: {name}//                                                                                                              | \<Enter\> to accept default                   | 4      |
|       |                                                                                                                                   | Correct name                                      | 4      |
|       |                                                                                                                                   | At-sign (@) to delete group                   | 1      |
| 4 | Select Data Segment:                                                                                                              | New data segment for this group                   | 5      |
|       |                                                                                                                                   | Existing data segment contained in this group     | 6      |
|       |                                                                                                                                   | \<Enter\> (default)                           | 6      |
|       |                                                                                                                                   | \<Enter\> (no default)                        | 1      |
|       |                                                                                                                                   | \<??\> for list of data segments              | 4      |
|       | If the selected data segment does not require time or occurrence limits, you will return to Step 4 after your entry at this step. |                                                   |            |
| 5 | ARE YOU ADDING ‘{step 4 entry}’ AS A NEW Data Segment (THE nTH FOR THIS VAQ - SEGMENT GROUP)?                                     | YES                                           | 7 or 4 |
|       |                                                                                                                                   | NO                                            | 7 or 4 |
| 6 | Data Segment: {name}//                                                                                                            | \<Enter\> to accept default                   | 7      |
|       |                                                                                                                                   | At-sign (@) to delete data segment            | 4      |
|       | Steps 7 and 8 may/may not appear depending on the data segment selected.                                                          |                                                   |            |
| 7 | Time Limit:                                                                                                                       | Time limit to use for selected data segment       | 8      |
|       |                                                                                                                                   | \<Enter\> to not specify a limit              | 8      |
| 8 | Occurrence Limit:                                                                                                                 | Occurrence limit to use for selected date segment | 4      |
|       |                                                                                                                                   | \<Enter\> to not specify a limit              | 4      |
| 9 | Return to the menu.                                                                                                               |                                                   |            |

<span id="_Ref522193734" class="anchor"></span>Table 13: Add/Edit Segment Group - All Option—Process Chart

#### Example

<u>Figure 55</u> is an example of what may appear on your screen while using the Add/Edit Segment Group - Public option.

<span id="_Ref522194197" class="anchor"></span>Figure 55: Add/Edit Segment Group - Public Option—Sample User Dialogue

Select VAQ - SEGMENT GROUP Group Name: <span class="mark">basic</span>

ARE YOU ADDING ‘basic’ AS A NEW VAQ - SEGMENT GROUP? <span class="mark">Y \<Enter\></span> (YES)

Group Name: basic// <span class="mark">\<Enter\></span>

Select Data Segment: <span class="mark">LAB ORDERS</span>

1 LAB ORDERS Lab Orders (LO)

2 LAB ORDERS BRIEF Lab Orders Brief (BLO)

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> Lab Orders

ARE YOU ADDING ‘Lab Orders’ AS A NEW Data Segment (THE 1ST FOR THIS VAQ - SEGMENT GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Time Limit: <span class="mark">6M</span>

Occurrence Limit: <span class="mark">3</span>

Select Data Segment: <span class="mark">MAS ADT HISTORY \<Enter\></span> MAS ADT History (ADT)

ARE YOU ADDING ‘MAS ADT History’ AS A NEW Data Segment (THE 2ND FOR THIS

VAQ - SEGMENT GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Time Limit: <span class="mark">\<Enter\></span>

Occurrence Limit: <span class="mark">1</span>

Select Data Segment: <span class="mark">\<Enter\></span>

Select VAQ - SEGMENT GROUP Group Name:

### Add/Edit Release Group

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Add/Edit Release Group option is used to enter/edit facilities into the release group for automatic processing of PDX requests. If the requesting facility is contained in the release group, the PDX request will be automatically processed. If not, the request will be placed in a queue to be manually processed. All requests pertaining to patients with “sensitive” records and those that exceed the maximum time and occurrence limits for Health Summary components are manually processed.

Only one release group exists per site. Through this option, the site may select how many and which facilities are in their release group.

You *must* hold the VAQ EDIT FILE security key to access this option.

![](pdx-v-1-5-user-manual/036.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 56</u> is an example of what may appear on your screen while using the Add/Edit Release Group option.

<span id="_Ref522194009" class="anchor"></span>Figure 56: Add/Edit Release Group Option—Sample User Dialogue

Select VAQ - RELEASE GROUP Remote Facility: <span class="mark">REDACTED dom \<Enter\></span> NEW YORK

ARE YOU ADDING ‘REDACTED DOM’ AS A NEW VAQ - RELEASE GROUP (THE 1ST)? <span class="mark">y \<Enter\></span> (YES)

Remote Facility: REDACTED DOM// <span class="mark">\<Enter\></span>

Remote Domain: <span class="mark">REDACTED.va.gov.</span>

Select VAQ - RELEASE GROUP Remote Facility: <span class="mark">REDACTED \<Enter\></span> NEW YORK 500

ARE YOU ADDING ‘REDACTED’ AS A NEW VAQ - RELEASE GROUP (THE 2ND)? <span class="mark">Y \<Enter\></span> (YES)

Remote Facility: REDACTED// <span class="mark">\<Enter\></span>

Remote Domain: <span class="mark">REDACTED.va.gov.</span>

Select VAQ - RELEASE GROUP Remote Facility:

### Add/Edit Segment Group - All

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Add/Edit Segment Group - All option is used to enter/edit public and private segment groups. A private segment group is one that only the person who created it can use when requesting PDX data. A public segment group is one that can be used by any user when requesting PDX data. You *must* hold the VAQ EDIT FILE security key to access this option.

A segment group is a group of selected data segments. It may contain any number of the currently available data segments. All segment groups will automatically contain the PDX\*MIN data segment, which is the minimal amount of patient data necessary to add a patient to the data base.

Data segments are comprised of Health Summary, Means Test, Copay, and specially created PDX components.

![](pdx-v-1-5-user-manual/037.png) NOTE: It should be noted that some segments may contain overlapping information. You may *not* add/edit/delete the data within the data segments.

Time and occurrence limits can be placed on applicable data segments selected for the segment group. These will determine how far back the system will search for the component and the number of occurrences of that component the system will report. The initial default values for these fields are set through the Edit Parameter File option.

Creating segment groups allows for expeditious requesting/sending of information as numerous data segments may be requested/sent by one entry, the segment group name.

#### Process

The process chart in <u>Table 13</u> shows the steps and prompts involved in using the Add/Edit Segment Group - All option.

| Step   | At this Prompt...                                                                                                                 | If User Answers with...                                                            | Then Step  |
|--------|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|------------|
| 1  | Select VAQ - SEGMENT GROUP                                                                                                        |                                                                                    |            |
|        | Group Name:                                                                                                                       | New group name                                                                     | 2      |
|        |                                                                                                                                   | Existing group name                                                                | 3      |
|        |                                                                                                                                   | \<Enter\> or caret \<^\>                                                   | 10     |
| 2  | ARE YOU ADDING ‘{step 1 entry}’ AS A NEW VAQ - SEGMENT GROUP (THE nTH)?                                                           | YES                                                                            | 3      |
|        |                                                                                                                                   | NO                                                                             | 1      |
| 3  | Group Name: {name}//                                                                                                              | \<Enter\> to accept default                                                    | 4      |
|        |                                                                                                                                   | Correct name                                                                       | 4      |
|        |                                                                                                                                   | At-sign (@) to delete group                                                    | 1      |
| 4  | Group Type:                                                                                                                       | PRIVATE—If this group can be referenced only by the user who created the group | 5      |
|        |                                                                                                                                   | PUBLIC—If this group can be referenced by all users                            | 5      |
| 5  | Select Data Segment:                                                                                                              | New data segment for this group                                                    | 6      |
|        |                                                                                                                                   | Existing data segment contained in this group                                      | 7      |
|        |                                                                                                                                   | \<Enter\> (default)                                                            | 7      |
|        |                                                                                                                                   | \<Enter\> (no default)                                                         | 1      |
|        |                                                                                                                                   | \<??\> For list of data segments                                               | 5      |
|        | If the selected data segment does not require time or occurrence limits, you will return to Step 5 after your entry at this step. |                                                                                    |            |
| 6  | ARE YOU ADDING ‘{step 4 entry}’ AS A NEW Data Segment (THE nTH FOR THIS VAQ - SEGMENT GROUP)?                                     | YES                                                                            | 8 or 5 |
|        |                                                                                                                                   | NO                                                                             | 8 or 5 |
| 7  | Data Segment: {name}//                                                                                                            | \<Enter\> to accept default                                                    | 8      |
|        |                                                                                                                                   | At-sign (@) to delete data segment                                             | 5      |
|        | Steps 8 and 9 may/may not appear depending on the data segment selected.                                                          |                                                                                    |            |
| 8  | Time Limit:                                                                                                                       | Time limit to use for selected data segment                                        | 9      |
|        |                                                                                                                                   | \<Enter\> to not specify a limit                                               | 9      |
| 9  | Occurrence Limit:                                                                                                                 | Occurrence limit to use for selected date segment                                  | 5      |
|        |                                                                                                                                   | \<Enter\> to not specify a limit                                               | 5      |
| 10 | Return to the menu.                                                                                                               |                                                                                    |            |

<span id="_Toc522274079" class="anchor"></span>Table 14: Glossary

#### Example

<u>Figure 57</u> is an example of what may appear on your screen while using the Add/Edit Segment Group - All option.

<span id="_Ref522193554" class="anchor"></span>Figure 57: Add/Edit Segment Group - All Option—Sample User Dialogue

Select VAQ - SEGMENT GROUP Group Name: <span class="mark">basic</span>

ARE YOU ADDING ‘basic’ AS A NEW VAQ - SEGMENT GROUP (THE 17TH)? <span class="mark">Y \<Enter\></span> (YES)

Group Name: basic// <span class="mark">\<Enter\></span>

Group Type: <span class="mark">0 \<Enter\></span> PRIVATE

Select Data Segment: <span class="mark">LAB ORDERS</span>

1 LAB ORDERS Lab Orders (LO)

2 LAB ORDERS BRIEF Lab Orders Brief (BLO)

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> Lab Orders

ARE YOU ADDING ‘Lab Orders’ AS A NEW Data Segment (THE 1ST FOR THIS VAQ - SEGMENT GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Time Limit: <span class="mark">6M</span>

Occurrence Limit: <span class="mark">3</span>

Select Data Segment: <span class="mark">MAS ADT HISTORY \<Enter\></span> MAS ADT History (ADT)

ARE YOU ADDING ‘MAS ADT History’ AS A NEW Data Segment (THE 2ND FOR THIS

VAQ - SEGMENT GROUP)? <span class="mark">Y \<Enter\></span> (YES)

Time Limit: <span class="mark">\<Enter\></span>

Occurrence Limit: <span class="mark">1</span>

Select Data Segment: <span class="mark">\<Enter\></span>

Select VAQ - SEGMENT GROUP Group Name:

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Purge Using Default Age

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Purge Using Default Age option is used to purge PDX transactions and their associated data based on the value found in the PDX parameter, LIFETIME OF DATA. The Purger automatically adds three days to the parameter value. Once transactions are older than this value, they are flagged for purging and automatically purged when this option is used. The *recommended* value for the LIFETIME OF DATA parameter is 15 days.

The date the last status was assigned to the transaction is the date used in determining when transactions will be flagged for purging.

The only prompt is for a requested start time for the purge. Once the start time is entered, a message will be displayed indicating the task has been queued. The task number is also displayed. This number should be used if it becomes necessary to cancel the task through the TaskMan User Toolbox utility.

If the task is stopped before completion and/or if certain transactions could not be purged, a mail bulletin will be sent notifying the members of the VAQ PDX ERRORS mail group.

You *must* hold the VAQ PURGE security key to access the Purging menu.

![](pdx-v-1-5-user-manual/038.png) NOTE: The purging process may be quite time consuming and should be queued to run during off hours.

![](pdx-v-1-5-user-manual/039.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 58</u> is an example of what may appear on your screen while using the Purge Using Default Age option. An example of the PDX Transactions Could Not Be Purged mail bulletin is also provided below.

<span id="_Ref522193354" class="anchor"></span>Figure 58: Purge Using Default Age Option—Sample User Dialogue

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (SEP 08, 1993@10:46:27)

Purging of PDX Transactions has been queued.

Task number: 11438

Subj: PDX TRANSACTIONS COULD NOT BE PURGED \[#113054\] 08 SEP 93 13:16 EST

14 Lines

From: PDX in ‘IN’ basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The following PDX Transaction(s) could not be purged ...

Entry \#: 25

Global: ^VAT(394.61,25)

Reason: TEST BULLETIN

\*\* Please remember that PDX Transactions may also \*\*

\*\* have associated data stored in file number 394.62 \*\*

Select MESSAGE Action: IGNORE (in IN basket)//

### Purge Using User Defined Age

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Purge Using User Defined Age option is used to purge PDX transactions and their associated data based on an age entered by the user.

You will be prompted for the number of days to use for purging. The Purger automatically adds three days to the user-entered value. Once transactions are older than this value, they are flagged for purging and automatically purged when this option is used. The default value displayed with the prompt is the entry in the PDX site parameter, LIFETIME FOR DATA.

The date the last status was assigned to the transaction is the date used in determining when transactions will be flagged for purging.

The second prompt is a requested start time for the purge. Once the start time is entered, a message will be displayed indicating the task has been queued. The task number is also displayed. This number should be used if it becomes necessary to cancel the task through the TaskMan User Toolbox utility.

If the task is stopped before completion and/or if certain transactions could not be purged, a mail bulletin will be sent notifying the members of the VAQ PDX ERRORS mail group.

You *must* hold the VAQ PURGE security key to access the Purging menu.

![](pdx-v-1-5-user-manual/040.png) NOTE: The purging process may be quite time consuming and should be queued to run during off hours.

![](pdx-v-1-5-user-manual/041.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 59</u> is an example of what may appear on your screen while using the Purge Using User Defined Age option. An example of the PDX Transactions Could Not Be Purged mail bulletin is also provided below.

<span id="_Ref522193104" class="anchor"></span>Figure 59: Purge Using User Defined Age Option—Sample User Dialogue

Lifetime to use for purging: 15// <span class="mark">25</span>

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (SEP 08, 1993@11:06:21)

Purging of PDX Transactions has been queued.

Task number: 11440

Subj: PDX TRANSACTIONS COULD NOT BE PURGED \[#113054\] 08 SEP 93 13:16 EST

14 Lines

From: PDX in ‘IN’ basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The following PDX Transaction(s) could not be purged ...

Entry \#: 25

Global: ^VAT(394.61,25)

Reason: TEST BULLETIN

\*\* Please remember that PDX Transactions may also \*\*

\*\* have associated data stored in file number 394.62 \*\*

Select MESSAGE Action: IGNORE (in IN basket)//

### Purge Using User Defined Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The Purge Using User Defined Date option is used to purge PDX transactions and their associated data based on a date entered by the user.

You will be prompted for the date to use for purging (date *must* be before three days ago). Transactions older than this value will be automatically purged when this option is used.

The date the last status was assigned to the transaction is the date used in determining when transactions will be flagged for purging.

The second prompt is a requested start time for the purge. Once the start time is entered, a message will be displayed indicating the task has been queued. The task number is also displayed. This number should be used if it becomes necessary to cancel the task through the TaskMan User Toolbox utility.

If the task is stopped before completion and/or if certain transactions could not be purged, a mail bulletin will be sent notifying the members of the VAQ PDX ERRORS mail group.

You *must* hold the VAQ PURGE security key to access the Purging menu.

![](pdx-v-1-5-user-manual/042.png) NOTE: The purging process may be quite time consuming and should be queued to run during off hours.

![](pdx-v-1-5-user-manual/043.png) NOTE: Due to the brevity of this option, a process chart has *not* been provided.

#### Example

<u>Figure 60</u> is an example of what may appear on your screen while using the Purge Using User Defined Date option. An example of the PDX Transactions Could Not Be Purged mail bulletin is also provided below.

<span id="_Ref522192755" class="anchor"></span>Figure 60: Purge Using User Defined Date Option—Sample User Dialogue

Date to use for purging: 08-09-1993// <span class="mark">\<Enter\></span> (AUG 09, 1993)

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (SEP 08, 1993@11:06:21)

Purging of PDX Transactions has been queued.

Task number: 11449

Subj: PDX TRANSACTIONS COULD NOT BE PURGED \[#113054\] 08 SEP 93 13:16 EST

14 Lines

From: PDX in ‘IN’ basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

\*\* Purger was stopped before completion \*\*

The following PDX Transaction(s) could not be purged ...

Entry \#: 25

Global: ^VAT(394.61,25)

Reason: TEST BULLETIN

\*\* Please remember that PDX Transactions may also \*\*

\*\* have associated data stored in file number 394.62 \*\*

Select MESSAGE Action: IGNORE (in IN basket)//

## Mail Groups and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mail Groups

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are three mail groups associated with the PDX software.

- VAQ MANUAL PROCESSING—Members of this group will receive notification when a PDX request received at their site requires manual processing.
- VAQ PDX ERRORS—Members of this group will receive notification of purging errors and errors in transmission of PDX transactions.
- VAQ UNSOLICITED RECEIVED—Members of this group will receive notification when an unsolicited PDX transaction is received at their site.

### Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The mail bulletins contained in the PDX software will have one of five different subjects. These bulletins are described below along with an example of each.

#### PDX Request Requires Processing

This bulletin is generated when a PDX request is received at your site that requires manual processing. Members of the VAQ MANUAL PROCESSING mail group will receive this bulletin. The four reasons a request would require manual processing are as follows:

- Sensitive patient
- Domain not in mail group
- Ambiguous patient
- Maximum time and occurrence limits exceeded by {#} segments

<span id="_Toc520297491" class="anchor"></span>Figure 61: PDX Request Requires Processing—Sample Bulletin

Subj: PDX REQUEST REQUIRES PROCESSING \[#112899\] 02 Sep 93 13:24 27 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

The following PDX Request requires manual processing ...

Transaction number: 120

Name: PDXPATIENT,FIVE

PID: 000-55-5555

DOB: 09-01-1933

Requested by: PDXUSER,THREE

Site: REDACTED VAMC

Domain: REDACTED.VA.GOV

Reason for manual processing:

Maximum time & occurrence limits exceeded by 3 segments

Segments that were over the allowable time & occurrence limits:

Requested Maximum Requested Maximum

Segment Time Time Occurrence Occurrence

------- --------- ------- ---------- ----------

DD 1Y - 20 10

OPC 2Y 1Y 10 -

RI - 1Y 10 10

Select MESSAGE Action: IGNORE (in IN basket)//

#### Results of PDX Request

This bulletin is generated after the remote site takes action on your PDX transaction. Users who were specified to receive notification at the time the request was made will receive this bulletin. The bulletin will inform you whether your request has been processed and returned or has been rejected by the remote site. Except for those patients who are deemed “sensitive”, the requested data will be contained in the mail bulletin if it was so specified during the request.

<span id="_Toc520297492" class="anchor"></span>Figure 62: Results of PDX Request Option—Sample Bulletin

Subj: RESULTS OF PDX REQUEST \[#112839\] 01 Sep 93 16:08 50 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

Your request for information has been processed and returned ...

Transaction number: 115

Name: PDXPATIENT,TEN

PID: 000-10-1010

DOB: 08-31-1952

Requested by: PDXUSER,THREE

Requested on: SEP 01, 1993

Processed by: PDXUSER,TWENTY-SEVEN

Site: REDACTED VAMC

Domain: REDACTED.VA.GOV

Comments: None listed

Subj: RESULTS OF PDX REQUEST \[#112839\] Page 2

------------------------------------------------------------------------------

Requested information:

-----------------------------\< Integrated Billing \>---------------------------

MEANS TEST BILLING INFORMATION

--- This patient has no current Means Test Billing activity ---

----------------------\< MAS Minimum Patient Information \>---------------------

PAT Name: PDXPATIENT,TEN DOB: AUG 31, 1952 AGE: 71

Addr: 123 MAIN ST SSN: 000-10-1010

: PARKLAND LEFT Sex: MALE MS: NEVER MARR

: Religion: CATHOLIC

City/ST: ANYTOWN, NY

Zip: 12180 County: RENSSELAER

Patient Type: NSC VETERAN Veteran: YES

Period of Service: VIETNAM ERA

Service Connected: NO Percentage: %

Eligibility: NSC

Select MESSAGE Action: IGNORE (in IN basket)//

#### Receipt of Unsolicited PDX

This bulletin is generated when an unsolicited PDX request is received at your site. Members of the VAQ UNSOLICITED REVIEW mail group will receive this bulletin.

<span id="_Toc520297493" class="anchor"></span>Figure 63: Receipt of Unsolicited PDX—Sample Bulletin

Subj: RECEIPT OF UNSOLICITED PDX \[#112899\] 02 Sep 93 13:24 24 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

The following Unsolicited PDX has been received...

Transaction number: 120

Name: PDXPATIENT,FIVE

PID: 000-55-5555

DOB: 09-01-1933

Received on: SEP O2, 1993

Sent by: PDXUSER,THREE

Site: REDACTED VAMC

Domain: REDACTED.VA.GOV

Comments: None listed

Select MESSAGE Action: IGNORE (in IN basket)//

#### PDX Transaction Could Not Be Purged

This bulletin is generated when either or both of the following occur:

- Process of purging the PDX data is stopped before completion.
- Purge has completed and certain transactions were found that could *not* be purged.

Members of the VAQ PDX ERRORS mail group will receive this bulletin.

<span id="_Toc520297494" class="anchor"></span>Figure 64: PDX Transaction Could Not Be Purged—Sample Bulletin

Subj: PDX TRANSACTIONS COULD NOT BE PURGED \[#113054\] 08 SEP 93 13:16 EST

14 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

\*\* Purger was stopped before completion \*\*

The following PDX Transaction(s) could not be purged ...

\*\* Please remember that PDX Transactions may also \*\*

\*\* have associated data stored in file number 394.62 \*\*

Select MESSAGE Action: IGNORE (in IN basket)//

Subj: PDX TRANSACTIONS COULD NOT BE PURGED \[#113054\] 08 SEP 93 13:16 EST

14 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

The following PDX Transaction(s) could not be purged ...

Entry \#: 25

Global: ^VAT(394.61,25)

Reason: TEST BULLETIN

\*\* Please remember that PDX Transactions may also \*\*

\*\* have associated data stored in file number 394.62 \*\*

Select MESSAGE Action: IGNORE (in IN basket)//

#### Unable to Send Messages

These bulletins are generated when an error occurred during transmission of the PDX transaction. Members of the VAQ PDX ERRORS mail group will receive the first bulletin while the person generating the transaction will receive the second bulletin.

<span id="_Toc520297495" class="anchor"></span>Figure 65: Unable to Send Messages—Sample Bulletin

Subj: UNABLE TO SEND MESSAGES \[#112899\] 02 Sep 93 13:24 11 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

The following error(s) occurred while generating PDX transmissions...

\(1\) Transaction Number: 120

IFN: 26

Global Location: ^VAT(394.61,26)

User: PDXUSER,SEVEN. (1934)

Transaction did not contain a domain to transmit message to

Select MESSAGE Action: IGNORE (in IN basket)//

Subj: UNABLE TO SEND MESSAGES \[#112889\] 02 Sep 93 13:24 16 Lines

From: PDX in ‘IN’ basket. Page 1

------------------------------------------------------------------------------

The following message(s) could not be transmitted ...

\(1\) Transaction Number: 120

Name: PDXPATIENT,TWELVE

PID: 000-12-1212

SSN: 000121212

DOB: 11-12-44

Sent By: PDXUSER,SEVEN

Site: Could not be determined (Contact your PDX ADPAC)

Domain: Could not be determined (Contact your PDX ADPAC)

Message Type:

Select MESSAGE Action: IGNORE (in IN basket)//

<span id="_Toc522273996" class="anchor"></span>Glossary

| Term           | Definition                                                                                                                                                                                                                                                                                       |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Data Segment   | Comprised of Health Summary, Means Test, Copay, and specially created PDX components.                                                                                                                                                                                                            |
| Domain         | A facility’s electronic mail address.                                                                                                                                                                                                                                                            |
| Mnemonic       | A device or code intended to assist memory.                                                                                                                                                                                                                                                      |
| Outgoing Group | A group of remote facilities. Creating outgoing groups allows for expeditious sending of PDX requests as they may be sent to all the facilities contained in the group with one entry, the outgoing group name.                                                                                  |
| PDX            | Patient Data Exchange                                                                                                                                                                                                                                                                            |
| Release Group  | A group of sites defined in the VAQ - RELEASE GROUP file through FileMan. Requests for sites you enter in your release group will be processed automatically upon receipt. Conversely, your requests will be processed automatically by sites who have your site defined in their release group. |
| Remote Site    | The facility with which your site is exchanging data. If you are requesting a PDX, the site you are requesting the data from would be the remote site. If you receive a request for a PDX, the site requesting the data would be the remote site.                                                |
| Segment Group  | A group of selected data segments.                                                                                                                                                                                                                                                               |
| Transaction    | A number automatically assigned to a PDX request when the number message is originated and/or received.                                                                                                                                                                                          |

<span id="_Toc522274080" class="anchor"></span>Table 15: Military Time Conversion Table:

![](pdx-v-1-5-user-manual/044.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

| Standard       | Military   |
|----------------|------------|
| 12:00 MIDNIGHT | 2400 HOURS |
| 11:00 PM       | 2300 HOURS |
| 10:00 PM       | 2200 HOURS |
| 9:00 PM        | 2100 HOURS |
| 8:00 PM        | 2000 HOURS |
| 7:00 PM        | 1900 HOURS |
| 6:00 PM        | 1800 HOURS |
| 5:00 PM        | 1700 HOURS |
| 4:00 PM        | 1600 HOURS |
| 3:00 PM        | 1500 HOURS |
| 2:00 PM        | 1400 HOURS |
| 1:00 PM        | 1300 HOURS |
| 12:00 NOON     | 1200 HOURS |
| 11:00 AM       | 1100 HOURS |
| 10:00 AM       | 1000 HOURS |
| 9:00 AM        | 0900 HOURS |
| 8:00 AM        | 0800 HOURS |
| 7:00 AM        | 0700 HOURS |
| 6:00 AM        | 0600 HOURS |
| 5:00 AM        | 0500 HOURS |
| 4:00 AM        | 0400 HOURS |
| 3:00 AM        | 0300 HOURS |
| 2:00 AM        | 0200 HOURS |
| 1:00 AM        | 0100 HOURS |

<span id="_Ref522191402" class="anchor"></span>Table 16: generic List Manager actions

# Appendix A—List Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The List Manager is a tool that displays a list of items in a screen format and provides the following functionality:

- Browse through the list.
- Select items that need action.
- Take action against those items.
- Select other List Manager actions without leaving the option.

Actions are entered by typing the names or abbreviations at the “Select Action” prompt. Actions can be preselected by separating them with semicolons (;). For example, “AL;CI” (Appointment Lists;Checked In) will advance through the two actions automatically.

Entries may be preselected in the following manner:

CI=1 will process entry 1 for check-in

CI=3 4 5 will process entries 3,4,5 for check-in

CI=1-3 will process entries 1,2,3 for check-in

In addition to the various actions that may be available specific to the option you are working in, List Manager provides generic actions applicable to any List Manager screen. You can enter two question marks (??) at the “Select Action” prompt for a list of all actions available.

<u>Table 16</u> lists the generic List Manager actions with a brief description. The abbreviation for each action is shown in brackets \[\] following the action name. Entering the abbreviation is the quickest way to select an action.

| Action                        | Description                                                                      |
|-------------------------------|----------------------------------------------------------------------------------|
| Next Screen \[+\]             | Move to the next screen.                                                         |
| Previous Screen \[-\]         | Move to the previous screen.                                                     |
| Up a Line \[UP\]              | Move up one line.                                                                |
| Down a Line \[DN\]            | Move down one line.                                                              |
| Shift View to Right \[\>\]    | Move the screen to the right if the screen width is more than 80 characters. |
| Shift View to Left \[\<\]     | Move the screen to the left if the screen width is more than 80 characters.  |
| First Screen \[FS\]           | Move to the first screen.                                                        |
| Last Screen \[LS\]            | Move to the last screen.                                                         |
| Go to Page \[G0\]             | Move to any selected page in the list.                                           |
| Re Display Screen (RD)        | Redisplay the current screen.                                                    |
| Print Screen \[PS\]           | Prints the header and the portion of the list currently displayed.               |
| Print List \[PL\]             | Prints the list of entries currently displayed.                                  |
| Search List \[SL\]            | Finds selected text in list of entries.                                          |
| Auto Display(On/Off) \[ADPL\] | Toggles the menu of actions to be displayed/not displayed automatically.         |
| Quit \[QU\]                   | Exits the screen.                                                                |

# Appendix B—Health Summary Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of the Health Summary Components supported by PDX 1.5. The descriptions were extracted from the Health Summary Components file.

Component Name: ADVERSE REACTIONS/ALLERGIES

Display Name: Adv React/Allerg

Abbreviation: ADR

Time Limits Apply:

Max Occurrences Apply:

Description: This component contains information from MAS, Pharmacy, and Dietetics software. It provides a list of all known food, drug and environmental allergies or adverse reactions (e.g., hay fever).

Component Name: CLINICAL WARNINGS

Display Name: Clinical Warnings

Abbreviation: CW

Time Limits Apply:

Max Occurrences Apply:

Description: This component contains clinical warning notes entered using the Generic Progress Note software. No time or maximum occurrence limits apply to this component. Clinical Warnings are a type of progress note, which includes clinical information to which clinicians need to be alerted. If this component is printed out on a CRT, information will include title, text of note, electronic signature block, and date posted. If the printout is to another device type, information will include electronic signature block and date posted to ensure security of information.

Component Name: CRISIS NOTES

Display Name: Crisis Notes

Abbreviation: CN

Time Limits Apply:

Max Occurrences Apply:

Description: This component contains crisis notes entered using the Generic Progress Note software. No time or maximum occurrence limits apply to this component. Crisis Notes are a type of progress note that contains important information for anyone who deals with a patient. If this component is printed out on a CRT, information will include title, text of note, electronic signature block, and date posted. If the printout is to another device type, information will include electronic signature block and date posted to ensure security of information.

Component Name: DIETETICS

Display Name: Dietetics

Abbreviation: DI

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the Dietetics software. Time and occurrence limits apply to this component. Data presented include: diet orders, start/stop dates, type of service (e.g., tray); nutritional status, date assessed; supplemental feedings, start/stop dates; tube feedings, start/stop dates, strength of product, quantity ordered, and daily dosages.

![](pdx-v-1-5-user-manual/045.png) NOTE: When a time limit is selected, the data presented reflects orders initiated within the time period.

Component Name: LAB BLOOD AVAILABILITY

Display Name: Blood Availability

Abbreviation: BA

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the Blood Bank module of the Lab software. Time and occurrence limits apply to this component. Data presented include: patient blood type (whether or not units have been assigned), unit expiration date, unit ID#, blood product(s), cross- match results, last known location, and a flag for autologous units.

![](pdx-v-1-5-user-manual/046.png) NOTE: An asterisked date (e.g., \* 10/10/90) indicates that the unit is due to expire within the next 48 hours.

Component Name: LAB BLOOD TRANSFUSIONS

Display Name: Blood Transfusions

Abbreviation: BT

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the Blood Bank module of the Lab software. Time and occurrence limits apply to this component. Data presented include: transfusion date and abbreviated blood products \[with total number of units transfused for each, e.g., RBC (2)\]. A key of the abbreviations is presented at the bottom of the display to help identify any unfamiliar blood products.

Component Name: LAB CHEMISTRY & HEMATOLOGY

Display Name: Chem & Hematology

Abbreviation: CH

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Time and maximum occurrence limits apply to this component. Data presented include: collection date/time, specimen, test name, results (w/ref flag: High/Low/Critical), units, and Reference range. Comments will also be conditionally displayed, depending on the value of the DISPLAY COMMENTS ON LABS Health Summary Site Parameter. Results that include comments will be indicated with the symbol !!, in the event that the parameter is set to 0 or NO.

Component Name: LAB CUMULATIVE SELECTED

Display Name: Lab Cum Selected

Abbreviation: SCLU

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Not only do time and maximum occurrence limits apply to this component, but the user is allowed to select any number of atomic Lab tests. Data presented include: collection date/time, specimen, test names with results and reference flags in columnar (horizontal) format.

Component Name: LAB CUMULATIVE SELECTED 1

Display Name: Lab Cum Selected 1

Abbreviation: SCL1

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Not only do time and maximum occurrence limits apply to this component, but the user is allowed to select as many as seven atomic Lab tests. Data presented include: collection date/time, specimen, test names with results and reference flags in columnar (horizontal) format.

Component Name: LAB CUMULATIVE SELECTED 2

Display Name: Lab Cum Selected 2

Abbreviation: SCL2

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Not only do time and maximum occurrence limits apply to this component, but the user is allowed to select as many as seven atomic Lab tests. Data presented include: collection date/time, specimen, test names with results and reference flags in columnar (horizontal) format.

Component Name: LAB CUMULATIVE SELECTED 3

Display Name: Lab Cum Selected 3

Abbreviation: SCL3

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Not only do time and maximum occurrence limits apply to this component, but the user is allowed to select as many as seven atomic Lab tests. Data presented include: collection date/time, specimen, test names with results and reference flags in columnar (horizontal) format.

Component Name: LAB CUMULATIVE SELECTED 4

Display Name: Lab Cum Selected 4

Abbreviation: SCL4

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Not only do time and maximum occurrence limits apply to this component, but the user is allowed to select as many as seven atomic Lab tests. Data presented include: collection date/time, specimen, test names with results and reference flags in columnar (horizontal) format.

Component Name: LAB CYTOPATHOLOGY

Display Name: Cytopathology

Abbreviation: CY

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Cytopathology module of the Lab software. Time and maximum occurrence limits apply. Data presented include: collection date/time, accession number, specimen, gross description and microscopic exam (both word processing fields), ICD diagnoses, and SNOMED fields: topography, disease, morphology, etiology, and procedures.

Component Name: LAB MICROBIOLOGY

Display Name: Microbiology

Abbreviation: MIC

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Microbiology module of the Lab software. Time and maximum occurrence limits apply. Data include: collection date/time, site/specimen, Parasite Report, organism(s), Mycology Report, Bacteriology Report, Mycobacteriology Report, Gram Stain Result, Culture and Susceptibility, Antibiotic Serum Level, and remarks.

Component Name: LAB MICROBIOLOGY BRIEF

Display Name: Brief Microbiology

Abbreviation: BMIC

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Time and maximum occurrence limits apply to this component in addition to collection date/time, test name, specimen, report status, Culture and Susceptibility, Antibiotic Serum Level, and test results.

Component Name: LAB ORDERS

Display Name: Lab Orders

Abbreviation: LO

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Time and maximum occurrence limits apply. Data presented include: collection date (either actual or expected), lab test, provider, accession, date/time ordered, specimen, and date/time results available.

Component Name: LAB ORDERS BRIEF

Display Name: Brief Lab Orders

Abbreviation: BLO

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Time and maximum occurrence limits apply. Data presented include: collection date/time, lab test name, specimen, urgency, and order status (e.g., ORDERED, COLLECTED, PROCESSING, COMPLETE).

Component Name: LAB SURGICAL PATHOLOGY

Display Name: Surgical Pathology

Abbreviation: SP

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Surgical Pathology module of the Lab software. Time and maximum occurrence limits apply. Data presented include: collection date/time, accession number, specimen, gross description and microscopic exam (both word processing fields), ICD diagnoses, and SNOMED fields: topography, disease, morphology, etiology, and procedures.

Component Name: LAB TESTS SELECTED

Display Name: Lab Tests Selected

Abbreviation: SLT

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Lab software. Not only do time and maximum occurrence limits apply to this component, but the user is allowed to select any number of atomic Lab tests. Data include: collection date/time, specimen, test name, result, units and reference range.

![](pdx-v-1-5-user-manual/047.png) NOTE: This component corresponds to the vertical format for the Lab software cumulative reports.

Component Name: MAS ADMISSIONS/DISCHARGES

Display Name: Admission/Discharge

Abbreviation: ADC

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the MAS software. Time and occurrence limits apply to this component. Data presented include: date range of admission, ward, length of stay (LOS), last treating specialty, last provider, admitting diagnosis text, bed section, principal diagnosis, diagnosis for longest length of stay (DXLS), and secondary ICD diagnoses.

Component Name: MAS ADT HISTORY

Display Name: ADT History

Abbreviation: ADT

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the MAS software. It can only be used with MAS Version 5 and up. Time and maximum occurrence limits apply. Data presented include: movement date, movement type (ADM=Admission, TR=Transfer, TS= Treating Specialty, DC=Discharge), movement description, specialty, and provider.

Component Name: MAS CLINIC VISITS FUTURE

Display Name: Fut Clinic Visits

Abbreviation: CVF

Time Limits Apply:

Max Occurrences Apply:

Description: This component provides a listing from the MAS scheduling module that contains future clinic visit dates, the clinic visited, and the appointment type.

Component Name: MAS CLINIC VISITS PAST

Display Name: Past Clinic Visits

Abbreviation: CVP

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the MAS scheduling module. Time and occurrence limits apply to this component. Data presented include: past clinic visits, dates, and a visit status (e.g., NO SHOW, INPATIENT VISIT).

![](pdx-v-1-5-user-manual/048.png) NOTE: Cancellations and Unscheduled Visits are shown.

Component Name: MAS DEMOGRAPHICS

Display Name: Demographics

Abbreviation: DEM

Time Limits Apply:

Max Occurrences Apply:

Description: This component contains the following patient demographic data (if available) from the MAS software: address, phone, county, marital status, religion, period of service, POW status (Y or N), branch of service, combat status (Y or N), eligibility code, current (verified) eligibility status, service connected %, eligible for care (Y or N), next of kin (NOK), NOK phone number and address.

Component Name: MAS DEMOGRAPHICS BRIEF

Display Name: Brief Demographics

Abbreviation: BDEM

Time Limits Apply:

Max Occurrences Apply:

Description: This component contains information from the MAS software. It provides brief patient demographic information including: address, phone number, and eligibility code (e.g., service connected 50-100%).

Component Name: MAS DISABILITIES

Display Name: Disabilities

Abbreviation: DS

Time Limits Apply:

Max Occurrences Apply:

Description: This component provides information from the MAS software about a patient’s eligibility code and eligibility status (Verified), and rated disabilities, including the disability percentage and whether the disability is service connected or non-service connected.

Component Name: MAS DISCHARGE DIAGNOSIS

Display Name: Discharge Diagnosis

Abbreviation: DD

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the MAS software. Time and occurrence limits apply to this component. Data presented include: Date range of admission through discharge, length of stay (LOS), Principal diagnosis, diagnosis for longest length of stay (DXLS), and secondary ICD discharge diagnoses.

![](pdx-v-1-5-user-manual/049.png) NOTE: This component provides discharge diagnoses coded in the MAS PTF file. The occurrence limits are determined by the occurrence of admissions.

Component Name: MAS DISCHARGES

Display Name: Discharges

Abbreviation: DC

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the MAS software. Time and occurrence limits apply to this component. Data presented include: date of discharge, DXLS, bedsection, disposition type, disposition place, and outpatient treatment flag.

![](pdx-v-1-5-user-manual/050.png) NOTE: The occurrence limits are determined by the occurrence of admissions.

Component Name: MAS PROCEDURES ICD CODES

Display Name: ICD Procedures

Abbreviation: PRC

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains MAS coded procedures, by admission, extracted from the MAS software. Time and occurrence limits apply to this component. Data presented include: procedure date, procedure name, and ICD-9CM procedure codes.

![](pdx-v-1-5-user-manual/051.png) NOTE: The occurrence limits are determined by the occurrence of admissions.

Component Name: MAS SURGERIES ICD CODES

Display Name: ICD Surgeries

Abbreviation: OPC

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains MAS coded surgeries, by admission, extracted from the MAS software. Time and occurrence limits apply to this component. Data presented include: surgery date, procedure name, and ICD-9CM procedure codes.

![](pdx-v-1-5-user-manual/052.png) NOTE: The occurrence limits are determined by the occurrence of admissions.

Component Name: MAS TRANSFERS

Display Name: Transfers

Abbreviation: TR

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the MAS software. Time and occurrence limits apply to this component. Data presented include: transfer date, type, destination, and provider (when available).

![](pdx-v-1-5-user-manual/053.png) NOTE: The occurrence limits are determined by the occurrence of admissions.

Component Name: MAS TREATING SPECIALTY

Display Name: Treating Specialty

Abbreviation: TS

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the MAS software. Time and occurrence limits apply to this component. Data presented include: treating specialty change date/time, new treating specialty, (admission date), and provider.

![](pdx-v-1-5-user-manual/054.png) NOTE: The occurrence limits are determined by the occurrence of admissions.

Component Name: MEDICINE SUMMARY

Display Name: Medicine Summary

Abbreviation: MED

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information extracted from the Medicine software. Time and maximum occurrence limits apply. Data presented include: procedure date/time, medical procedure name, and result (e.g., normal, abnormal, borderline).

![](pdx-v-1-5-user-manual/055.png) NOTE: This component is a summary of procedure statuses.

Component Name: ORDERS CURRENT

Display Name: Current Orders

Abbreviation: ORC

Time Limits Apply: yes

Max Occurrences Apply:

Description: This component contains current orders from the OE/RR software. Since the OE/RR software integrates all orders for the ancillary services, the orders will be reported in most recent orders first sequence without concern for the ancillary software the order originated from/for. Current orders are defined as those orders with an OE/RR order status other than discontinued or expired. The component information includes item ordered, OE/RR order status, start date, and stop date. OE/RR order status abbreviations include “blank”=Active, “c”=Complete, “dc”=Discontinued, “e”= expired, “?”=Flagged, “h”=Hold, “i”=incomplete, “p”=pending, “s”=scheduled.

Component Name: PHARMACY INTRAVENOUS

Display Name: IV Pharmacy

Abbreviation: RXIV

Time Limits Apply: yes

Max Occurrences Apply:

Description: This component contains IV orders extracted from the Pharmacy software. Only time limits apply. Data presented include: start date, stop date, drug (additives), dose, status, solutions and infusion rates.

![](pdx-v-1-5-user-manual/056.png) NOTE: If no time limit is defined, only active IV orders are reported. If a time limit is defined, all IV orders that have an expiration or cancel date within the time limit range are reported.

Component Name: PHARMACY OUTPATIENT

Display Name: Outpatient Pharmacy

Abbreviation: RXOP

Time Limits Apply: yes

Max Occurrences Apply:

Description: This component contains information from the Outpatient Pharmacy software. Only time limits apply. Data presented include: drug, prescription number, status expiration/cancellation date (when appropriate), quantity, issue date, last fill date, refills remaining, provider, and cost/fill (when available).

![](pdx-v-1-5-user-manual/057.png) NOTE: This component is formatted similar to the Short Medication Profile. If no time limit is defined, all orders are reported. When a time limit is defined, all outpatient pharmacy orders that have an expiration or cancel date within the time limit range are reported.

Component Name: PHARMACY UNIT DOSE

Display Name: Unit Dose Pharmacy

Abbreviation: RXUD

Time Limits Apply: yes

Max Occurrences Apply:

Description: This component contains Unit Dose information extracted from the Pharmacy software. Only time limits apply. Data presented include: Drug, dose, pharmacy status, start date, stop date, and sig (which includes schedule instructions and route).

![](pdx-v-1-5-user-manual/058.png) NOTE: If no time limit is defined, all active orders are reported. If a time limit is defined, all unit dose orders that have an expiration or cancel date within the time limit range are reported.

Component Name: PROGRESS NOTES

Display Name: Progress Notes

Abbreviation: PN

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains progress notes from the Generic Progress Notes software *and* progress notes from the Mental Health software. Time and maximum occurrence limits apply to this component. Data presented include: Progress note date/time written, title, text of note, electronic signature block (including possible cosignature and cosigner comments), and the note’s correction text and correction date/time. Only those notes that have been signed with an electronic signature or (for generic progress notes) electronically marked signed on chart will be reported.

Component Name: PROGRESS NOTES BRIEF

Display Name: Brief Progress Notes

Abbreviation: BPN

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the Mental Health and Generic Progress Notes softwares. Time and maximum occurrence limits apply. Data presented include: Progress note date/time, title, author and last correction date/time. Only those notes that have been signed with an electronic signature or (for generic progress notes) electronically marked signed on chart will be listed.

Component Name: RADIOLOGY IMPRESSION

Display Name: Radiology Impression

Abbreviation: RI

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains impressions from the Radiology software. Time and maximum occurrence limits apply. Data presented include: study date, procedure(s), status, and radiologist’s impression (narrative). Only radiology impressions that have been verified are reported.

Component Name: RADIOLOGY IMPRESSION SELECTED

Display Name: Sel Rad Impression

Abbreviation: SRI

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains impressions from the Radiology software. Time and occurrence limits apply. Data presented include: study date, procedure(s), status and radiologist’s impression (narrative) for the procedures selected by the user (e.g., CHEST 2 VIEWS -PA & LAT). Only radiology impressions that have been verified are reported.

Component Name: RADIOLOGY PROFILE

Display Name: Radiology Profile

Abbreviation: RP

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the Radiology software. Time and maximum occurrence limits apply. Data presented include: study date, procedure(s) with status(es), report status, staff radiologist, resident radiologist, and the narrative fields modifier, history, report, and impression. Only radiology profiles that have been verified are reported.

Component Name: RADIOLOGY STATUS

Display Name: Radiology Status

Abbreviation: RS

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains procedure statuses from the Radiology software. Time and maximum occurrence limits apply. Data presented include: request date/ time, status, procedure, scheduled date/time, and provider name.

Component Name: SURGERY REPORTS

Display Name: Surgery Reports

Abbreviation: SR

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains information from the Surgery software. Time and maximum occurrence limits apply. Data presented include: surgery date, surgeon, surgery report status, pre-operative diagnosis, post-operative diagnosis, surgeon’s dictation, current procedural terminology operation code and text. Only surgery reports that have been verified are reported.

Component Name: SURGERY REPORTS BRIEF

Display Name: Brief Surgery Rpts

Abbreviation: BSR

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains surgery report statuses extracted from the Surgery software. Time and maximum occurrence limits apply. Data presented include: surgery date, surgical procedure, and report status (e.g., COMPLETE).

Component Name: VITAL SIGNS

Display Name: Vital Signs

Abbreviation: VS

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains vital measurements extracted from the Vital Signs module of the Nursing software. Time and maximum occurrence limits apply. Data presented include: measurement date/time, blood pressure (as SBP/DBP), pulse, temperature, height, weight, and respiratory rate.

Component Name: VITAL SIGNS SELECTED

Display Name: Vital Signs Selected

Abbreviation: SVS

Time Limits Apply: yes

Max Occurrences Apply: yes

Description: This component contains selected vital measurements extracted from the Vital Signs module of the Nursing software. Time and maximum occurrence limits apply, and the user is allowed to select any of the vital measurement types defined in the Vital Type file (e.g., pulse, blood pressure, temperature, height, weight, and respiration rate). Data presented include: measurement date/time, measurement type and measurement value.

![](pdx-v-1-5-user-manual/059.png) NOTE: Formatted display is horizontal.

# Appendix C—PDX Transaction Statuses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the statuses that can be assigned to PDX transactions:

- Requested patient could not be uniquely identified at remote facility
- PDX request from remote facility being processed automatically
- Requested patient could not be found at remote facility
- PDX request from remote facility that requires manual processing
- PDX transmission that is currently being received
- Requested information was not released by remote facility
- Acknowledgement for receipt of PDX request by remote facility
- PDX request
- Requested information was returned
- Request to retransmit message using previous version
- Unsolicited PDX that was transmitted from local facility
- Acknowledgement for receipt of unsolicited PDX by remote facility
- Unsolicited PDX

<span id="_Toc522274000" class="anchor"></span>Index

A

Acronyms

Intranet Website, 115

Add/Edit Fields to Encrypt, 90

Example, 90

Add/Edit Outgoing Group, 92

Example, 94

Process, 93

Add/Edit Release Group, 102

Example, 102

Add/Edit Segment Group – All, 102

Example, 105

Process, 103

Add/Edit Segment Group – Private, 97

Example, 99

Process, 97

Add/Edit Segment Group – Public, 99

Example, 101

Process, 100

Appendix A—List Manager, A, 117

Appendix B—Health Summary Components, B, 119

Assumptions, xv

B

Bulletins, 110

PDX Request Requires Processing, 110

PDX Transaction Could Not Be Purged, 113

Receipt of Unsolicited PDX, 112

Results of PDX Request, 111

Unable to Send Messages, 114

C

Callout Boxes, xiii

Contents, iv

D

Data Dictionary

Data Dictionary Utilities Menu, xiv

Listings, xiv

Disclaimers

Software, xi

Display PDX by Transaction, 41

Example, 44

Process, 42

Display PDX by User, 45

Example, 47

Process, 46

Display PDX Data, 41

Documentation

Symbols, xii

Documentation Conventions, xii

Documentation Navigation, xiii

E

Edit maximum limits for automatic processing, 91

Example, 91

Edit Parameter File, 94

Example, 96

Process, 95

ES Anonymous Directories, xv

F

Files

PRESCRIPTION (#52), 90

VAQ - ENCRYPTED FIELDS (#394.73), 17

G

Glossary, 115

Intranet Website, 115

H

Help

At Prompts, xiv

Online, xiv

Question Marks, xiv

Home Pages

Acronyms Intranet Website, 115

Adobe Website, xv

Glossary Intranet Website, 115

VHA Software Document Library (VDL) Website, xv

How to

Obtain Technical Information Online, xiv

Use this Manual, x

I

Implementation, 18

Intended Audience, x

Introduction, 16

L

List File Attributes Option, xiv

Load/Edit PDX Data, 37

Example, 40

Process, 38

M

Mail Groups, 109

VAQ PDX ERRORS, 109

VAQ UNSOLICITED RECEIVED, 109

Menus

Data Dictionary Utilities, xiv

O

Obtaining

Data Dictionary Listings, xiv

Online

Documentation, xiv

Technical Information, How to Obtain, xiv

Options

Data Dictionary Utilities, xiv

List File Attributes, xiv

Orientation, x

Overview, 16

P

PDX Edit Files, 90

PDX Request Requires Processing Bulletin, 110

PDX Transaction Could Not Be Purged Bulletin, 113

PRESCRIPTION (#52) File, 90

Process External PDX, 32

Example, 35

Process, 33

Purge Using Default Age

Example, 105, 106

Purge Using User Defined Age, 106

Example, 107

Purge Using User Defined Date, 108

Example, 109

Purging, 105

Q

Question Mark Help, xiv

R

Receipt of Unsolicited PDX Bulletin, 112

Reference Materials, xv

Request PDX for Patient, 19

Example, 24

Process, 20

Requires Processing Report, 48

Example, 49

Results of PDX Request Bulletin, 111

Revision History, ii

S

Software Disclaimer, xi

Software Management, 17

Software Operation, 18

Sort By Date

Example, 75, 76

Sort By Date Received, 57

Example, 59

Sort By Patient’s Name, 55, 81

Example, 56, 82

Sort By Remote Facility, 49, 78

Example, 50, 79

Sort By Requesting Date, 64

Example, 65

Sort By Status of Transaction, 67

Example, 68

Sort By Type of Work Done, 87

Example, 88

Sort By User That Generated Request, 52

Example, 53

Sort By User That Released Information, 61

Example, 62

Sort Criteria Defined By User, 69, 84

Example, 71, 85

Symbols

Found in the Documentation, xii

System Reports, 48

T

Table of Contents, iv

U

Unable to Send Messages Bulletin, 114

Unsolicited PDX, 26

Example, 30

Process, 26

URLs

Acronyms Intranet Website, 115

Adobe Website, xv

Glossary Intranet Website, 115

VHA Software Document Library (VDL) Website, xv

Use this Manual, How to, x

V

VAQ - ENCRYPTED FIELDS File (#394.73), 17

VAQ Mail Groups

MANUAL PROCESSING, 109

VAQ MANUAL PROCESSING Mail Group, 109

VAQ PDX ERRORS Mail Group, 109

VAQ UNSOLICITED RECEIVED Mail Group, 109

VHA Software Document Library (VDL)

Website, xv

W

Web Pages

Adobe Website, xv

VHA Software Document Library (VDL) Website, xv

Websites

Acronyms Intranet Website, 115

Glossary Intranet Website, 115

Work Load Reports, 75