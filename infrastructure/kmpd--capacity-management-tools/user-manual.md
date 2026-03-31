---
title: Capacity Management Tools Version 3 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: KMPD
app_name: Capacity Management Tools
section: INF
app_status: active
pkg_ns: KMPD
patch_ver: 3
patch_id: KMPD*3
group_key: "KMPD:KMPD:3"
file_numbers: 
  - 19
  - 8973
security_keys: []
menu_options: 3
description: 
audience: 
keywords: 
  - span
  - time
  - class
  - tools
  - timing
  - background
  - load
  - kmpd
  - coversheet
  - report
page_count: 0
word_count: 19996
section_count: 7
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Capacity_Mgmt_Tools/kmpd3_0um_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Capacity_Mgmt_Tools/kmpd3_0um_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=129"
---

---
title: |
  Capacity Management Tools 3.0

  User Manual
---

![](capacity-management-tools-version-3-user-manual/001.png)

December 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Systems Engineering (ESE)

Capacity and Performance Engineering (CPE)

<span id="_Toc44314817" class="anchor"></span>Revision History

Documentation Revisions

<u>Table 1</u> displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<caption><p><span id="_Ref439161888" class="anchor"></span>Table . Documentation revision history</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 45%" />
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
<td>12/30/2015</td>
<td>1.2</td>
<td><p>Updated document based on Capacity Management Tools Patch KMPD*3.0*3.</p>
<p>Software: <strong>CM Tools 3.0</strong>.</p></td>
<td><p>REDACTED (CPE): St. Petersburg Field Office</p>
<p>Technical Writer: REDACTED</p></td>
</tr>
<tr class="even">
<td>10/--/2015</td>
<td>1.1</td>
<td><p>Corrected reports to reflect both foreground and background CPRS coversheet load timings.</p>
<p>Software: <strong>CM Tools 3.0</strong>.</p></td>
<td>REDACTED (CPE): St. Petersburg Field Office</td>
</tr>
<tr class="odd">
<td>09/20/2012</td>
<td>1.0</td>
<td><p>Initial Capacity Management (CM) Tools software and documentation release.</p>
<p>Software: <strong>CM Tools 3.0</strong></p></td>
<td><p>Capacity Planning Development Team</p>
<ul>
<li><p>Development Manager—REDACTED</p></li>
<li><p>Developer—REDACTED</p></li>
<li><p>Software Quality Assurance (SQA)—REDACTED</p></li>
<li><p>Technical Writer—REDACTED</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref439161888" class="anchor"></span>Table . Documentation revision history

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Contents

<span id="_Toc439222228" class="anchor"></span>Figures and Tables

Figures

Tables

<span id="_Toc18284794" class="anchor"></span>Orientation

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of Capacity Management (CM) Tools software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

Intended Audience

The intended audience of this manual is all key stakeholders. The stakeholders include the following:

- Information Resource Management (IRM)—System administrators and Capacity Management personnel at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Product Development (PD)—VistA legacy development teams.
- Product Support (PS).

Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely provided that any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

Documentation Disclaimer

This manual provides an overall explanation of using the VistA System Monitor (VSM) 1.0 software; however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA Internet and Intranet SharePoint sites and websites for a general orientation to VistA. For example, visit the Office of Information and Technology (OI&T) Product Development (PD) Intranet Website.

![](capacity-management-tools-version-3-user-manual/002.png) DISCLAIMER: The appearance of any external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Website or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 2</u> gives a description of each of these symbols:

| Symbol                                                                                                                            | Description                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| ![](capacity-management-tools-version-3-user-manual/003.png)       | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](capacity-management-tools-version-3-user-manual/004.png) | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |

<span id="_Ref345831418" class="anchor"></span>Table . Documentation symbol/term descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) begin with either “000” or “666”.
- Patient and user names are formatted as follows:
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*PATIENT,*\<N\>*
- *\<APPLICATION NAME/ABBREVIATION/NAMESPACE\>*USER,*\<N\>*

Where “\<*APPLICATION NAME/ABBREVIATION/NAMESPACE\>*“ is defined in the Approved Application Abbreviations document and “\<*N*\>“ represents the first name as a number spelled out or as a number value and incremented with each new entry.

For example, in Capacity Planning (KMPD) test patient and user names would be documented as follows:

- KMPDPATIENT,ONE or KMPDUSER,ONE
- KMPDPATIENT,TWO or KMPDUSER,TWO
- KMPDPATIENT,THREE or KMPDUSER,THREE
- KMPDPATIENT,14 or KMPDUSER,14
- Etc.
- “Snapshots” of computer online displays (i.e., screen captures/dialogues) and computer source code is shown in a *non*-proportional font and can be enclosed within a box.
- User’s responses to online prompts are bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>). The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

Select Primary Menu option: <span class="mark">??</span>

- Emphasis within a dialogue box is bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words are bold typeface with alternate color font.
- References to “\<Enter\>” within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author’s comments are displayed in italics or as “callout” boxes.

![](capacity-management-tools-version-3-user-manual/005.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS is considered an alternate name. This manual uses the name M.
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

![](capacity-management-tools-version-3-user-manual/006.png) NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case (e.g., CamelCase).

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word’s built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to the toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word (*not* the Ribbon section).
2.  Select Customize Quick Access Toolbar from the secondary menu.
3.  Select the drop-down arrow in the “Choose commands from:” box.
4.  Select All Commands from the displayed list.
5.  Scroll through the command list in the left column until you see the Back command (green circle with arrow pointing left).
6.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
7.  Scroll through the command list in the left column until you see the Forward command (green circle with arrow pointing right).
8.  Select/Highlight the Forward command and select Add to add it to the customized toolbar.
9.  Select OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](capacity-management-tools-version-3-user-manual/007.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated using Kernel, MailMan, and VA FileMan utilities.

![](capacity-management-tools-version-3-user-manual/008.png) NOTE: Methods of obtaining specific technical information online is indicated where applicable under the appropriate section.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities menu in VA FileMan to print formatted data dictionaries.

![](capacity-management-tools-version-3-user-manual/009.png) REF: For details about obtaining data dictionaries and about the formats available, see the “List File Attributes” section in the “File Management” section in the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft<sup>®</sup> Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about the Capacity Management Tools software should consult the following:

- *Capacity Management Tools Installation Guide*
- *Capacity Management Tools User Manual* (this manual)
- *Capacity Management Tools Technical Manual*
- Capacity Management (CM) Tools Online Help file (i.e., CM_Tools_3_0.chm)
- Capacity and Performance Engineering (CPE) website (for more information on CPE services).

This site contains other information and provides links to additional documentation.

VistA documentation is made available online in Microsoft<sup>®</sup> Word format and in Adobe<sup>®</sup> Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe<sup>®</sup> Acrobat Reader, which is freely distributed by [Adobe<sup>®</sup> Systems Incorporated](http://www.adobe.com/).

VistA documentation can be downloaded from the [VA Software Document Library (VDL)](http://www.va.gov/vdl/).

![](capacity-management-tools-version-3-user-manual/010.png) REF: See the [Capacity Management Tools manuals on the VDL](http://www.va.gov/vdl/application.asp?appid=129).

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous Directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [CM Tools: Software Overview and Use](#cm-tools-software-overview-and-use)
  - [Functional Description](#functional-description)
  - [Data Collection Process](#data-collection-process)
  - [Statistics and Projections](#statistics-and-projections)
  - [Software Management](#software-management)
- [CM Tools: Options](#cm-tools-options)
  - [Capacity Planning Menu](#capacity-planning-menu)
    - [Capacity Planning Mail Group Edit Option](#capacity-planning-mail-group-edit-option)
    - [CP Tools Manager Menu](#cp-tools-manager-menu)
  - [CM Tools Background Driver Option](#cm-tools-background-driver-option)
The Capacity Management (CM) Tools software is a fully automated support tool developed by Capacity Planning (CP) Service. CM Tools are designed for Information Resource Management (IRM) and system administrators responsible for the capacity planning functions at their site, as well as Veterans Health Information Systems and Technology Architecture (VistA) software developers.
The CM Tools are used to measure system performance, data growth, Computerized Patient Record System (CPRS) coversheet load times, option and protocol execution, and provide various data reports. There are also tools for developers: global lister, error lister, routine search, and evaluate M code.
The CM Tools software allows a site to collect Veterans Health Information Systems and Technology Architecture (VistA) Health Level Seven (HL7) workload information.
The CM Tools software is strongly dependent on the site to schedule and run the background tasks on a regular basis. Menus and options are provided locally at the site to allow IRM staff to accomplish and monitor these tasks.
The background tasks obtain VistA HL7 information from the site and automatically transfers this data via network mail (i.e., VistA MailMan) to the Capacity Planning National Database.
The Department of Veterans Affairs (VA) developed the CM Tools software in order to obtain more accurate information regarding the current and future system and VistA HL7 workload at VA sites (e.g., VA Medical Centers \[VAMCs\]).
The purpose of this manual is to provide information about the Capacity Management Tools software. This manual defines the use of this software as a resource to IRM staff responsible for capacity planning functions at the site. It also highlights the use of the options that are available at the site.

# CM Tools: Software Overview and Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools software application provides fully automated support tools developed by Capacity Planning Service. It entails the daily capture of the following data from participating sites:

- VistA Health Level Seven (HL7) Workload Information—VistA HL7 workload data is summarized and transmitted on a weekly basis.
- VistA Timing Data—Timing data is summarized and transmitted on a daily and weekly basis.

Data collected is automatically transferred via network mail (i.e., VistA MailMan) to the Capacity Planning National Database. The data is displayed graphically on the Capacity Planning Statistics Intranet website.

![](capacity-management-tools-version-3-user-manual/011.png) REF: For more information on the Capacity Planning National Database and data display, see the “<u>Statistics and Projections</u>” section.

The IRM staff utilizes the options that are available at the site to manage the CM Tools software. IRM staff responsible for capacity planning tasks at the site can use these options to review VistA HL7 workload trends.

![](capacity-management-tools-version-3-user-manual/012.png) REF: For more information on the CM Tools options, see Chapter <u>3</u>, “<u>CM Tools: Options</u>.”

The current version of the software is compatible with all current operating system platforms at VA sites and has minimal impact on IRM support staff.

## Data Collection Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing the CM Tools software creates the collection process mechanism and other necessary components of the software. The fully automated data collection mechanism entails capturing the following data:

- VistA HL7 workload specifics at the site—This data is gathered into a temporary ^TMP(“KMPDH”,\$J) collection global.
- Timing data at the site—This data is gathered into the temporary ^KMPTMP(“KMPDT”) collection global.

The collection mechanism is continuously monitoring each process on the system while trapping system timing and VistA HL7 workload data.

On a nightly basis, the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] does the following:

- Moves the data within the ^TMP(“KMPDH”,\$J) collection global to the CM HL7 DATA file (#8973.1).
- Moves the data within the ^KMPTMP(“KMPDT”) collection global. to the CP TIMING file (#8973.2)

Upon completion, the data within both the ^TMP(“KMPDH”,\$J) and ^KMPTMP(“KMPDT”) temporary collection globals is purged.

![](capacity-management-tools-version-3-user-manual/013.png) REF: For more information on the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\], see the “<u>CM Tools Background Driver</u>” section in Chapter <u>3</u>, “<u>CM Tools: Options</u>.”

## Statistics and Projections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every Sunday night, the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] monitors and deletes records from the following files to ensure that the correct maximum number of day’s data is maintained as determined by the appropriate CP parameters:

- CM HL7 DATA file (#8973.1)—The maximum amount of data collected is determined by the Purge HL7 Data After CP parameter.
- CP TIMING file (#8973.2)—The maximum amount of data collected is determined by the Purge Timing Data After CP parameter.

![](capacity-management-tools-version-3-user-manual/014.png) REF: For more information on the CP parameters, see the “<u>Edit CP Parameters File</u>” section in Chapter <u>3</u>, “<u>CM Tools: Options</u>.”

On a nightly basis, the CM Tools Background Driver option automatically compresses the information contained within the CP TIMING file (#8973.2) into daily statistics. These daily statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes.

Also, each Sunday night, the CM Tools Background Driver option automatically compresses the information contained within both the CM HL7 DATA (#8973.1) and CP TIMING (#8973.2) files into weekly statistics. These weekly statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes.

The data is also available on the following Capacity Planning Intranet websites:

- Statistics—Provides statistics for each listed site.
- Projections—Provides data trends for each listed site.

## Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Management Tools software is managed by IRM staff through the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\], which is located under the Capacity Planning menu \[XTCM MAIN\]. The XTCM MAIN menu is found under the Eve menu and should be assigned to IRM staff members who support this software and other capacity management tasks.

![](capacity-management-tools-version-3-user-manual/015.png) REF: For more information on CM Tools software management and maintenance, see the *Capacity Management (CM) Tools Technical Manual*.

# CM Tools: Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter discusses the Capacity Management Tools software options.

## Capacity Planning Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Planning menu \[XTCM MAIN; Synonym: CM\] is located under the Operations Management menu \[XUSITEMGR\], which is located under Kernel’s Systems Manager Menu \[Eve\], as shown in <u>Figure 1</u>:

<span id="_Ref439163551" class="anchor"></span>Figure . Accessing the Capacity Planning menu—User prompts

Select Systems Manager Menu Option: <span class="mark">OPERATIONS MANAGEMENT</span>

System Status

Introductory text edit

CPU/Service/User/Device Stats

<span class="mark">CM Capacity Planning ...</span> <span class="mark">\[XTCM MAIN\]</span>

Alert Management ...

Alpha/Beta Test Option Usage Menu ...

Clean old Job Nodes in XUTL

Delete Old (\>14 d) Alerts

Kernel Management Menu ...

Post sign-in Text Edit

RPC Broker Management Menu ...

User Management Menu ...

Select Operations Management Option: <span class="mark">CAPACITY PLANNING</span>

The Capacity Planning menu holds all the currently available capacity planning options. The XTCM MAIN menu can be assigned to the IRM staff members who support this software and other capacity planning tasks.

The Capacity Planning menu contains the following options:

<span id="_Ref54082428" class="anchor"></span>Figure . Capacity Planning—Menu option

Select Operations Management Option: <span class="mark">CAPACITY PLANNING</span><span class="mark">CPG Capacity Planning Mail Group Edit \[KMP MAIL GROUP EDIT\]</span><span class="mark">TLS CP Tools Manager Menu ... \[KMPD CM TOOLS MANAGER MENU\]</span>

Select Capacity Planning Option:

These Capacity Planning menu-related options are discussed in greater detail in the sections that follow.

### Capacity Planning Mail Group Edit Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Capacity Planning Mail Group Edit option \[KMP MAIL GROUP EDIT; Synonym: CPG\] is located on the Capacity Planning menu \[XTCM MAIN\] (<u>Figure 2</u>). It is used to edit the KMP-CAPMAN mail group. The KMP-CAPMAN mail group is defined with the installation of the CM Tools software.

<u>Figure 3</u> shows the prompts and user responses for the Capacity Planning Mail Group Edit option:

<span id="_Ref231287310" class="anchor"></span>Figure . Capacity Planning Mail Group Edit option—Sample user prompts

Select Capacity Planning Option: <span class="mark">CAPACITY PLANNING MAIL GROUP EDIT</span>

Edit Capacity Planning Mail Group

NAME: KMP-CAPMAN

Select MEMBER: KMPDUSER,ONE// <span class="mark">?</span>

Answer with MEMBER

Choose from:

KMPDUSER,ONE

KMPDUSER,TWO

You may enter a new MEMBER, if you wish

Enter a local user who should receive mail addressed to this group.

User must have an access code and a mailbox.

Answer with NEW PERSON NAME, or INITIAL, or SSN, or VERIFY CODE, or

NICK NAME, or SERVICE/SECTION, or DEA#, or ALIAS

Do you want the entire NEW PERSON List? <span class="mark">N \<Enter\></span> (No)

Select MEMBER: KMPDUSER,ONE// <span class="mark">\<Enter\></span>

TYPE: CC// <span class="mark">??</span>

This field indicates what type of recipient this is.

If this field has nothing in it, it indicates that this recipient is

a primary recipient, and may reply.

CC: indicates that the recipient is being sent a copy, but is not the

primary recipient. The recipient may reply.

INFO: indicates that the recipient may not reply to the message; the

message is being transmitted to the recipient for information purposes

only.

Choose from:

C CC

I INFO

TYPE: CC// <span class="mark">\<Enter\></span>

Select MEMBER: <span class="mark">\<Enter\></span>

DESCRIPTION:

This mail group will receive messages for all Capacity Planning software

(i.e., CM Tools, SAGG, RUM).

Edit? NO// <span class="mark">\<Enter\></span>

TYPE: public// <span class="mark">??</span>

The type of mail group determines who can send mail to it.

Provided there are no AUTHORIZED SENDERS specified, anyone can send mail

to a public group and only its members can send mail to a private group.

If there are AUTHORIZED SENDERS specified, only those users can address

the group.

Choose from:

PU public

PR private

TYPE: public// <span class="mark">\<Enter\></span>

ORGANIZER: KMPDUSER,TWO// <span class="mark">\<Enter\></span>

COORDINATOR: KMPDUSER,TWO// <span class="mark">\<Enter\></span>

Select AUTHORIZED SENDER: <span class="mark">\<Enter\></span>

ALLOW SELF ENROLLMENT?: NO// <span class="mark">?</span>

If users may join this group by themselves, say “YES”

Choose from:

y YES

n NO

ALLOW SELF ENROLLMENT?: NO// <span class="mark">\<Enter\></span>

Select MEMBER GROUP NAME: <span class="mark">?</span>

You may enter a new MEMBER GROUPS, if you wish

If you would like another mail group to be a member of this one enter

a partial match to its name.

A mail group may not be a member of itself.

Answer with MAIL GROUP NAME

Do you want the entire MAIL GROUP List? <span class="mark">n \<Enter\></span> (No)

Select MEMBER GROUP NAME: <span class="mark">\<Enter\></span>

Select REMOTE MEMBER: <span class="mark">?</span>

You may enter a new MEMBERS - REMOTE, if you wish

Enter a remote address (name@domain) or local device (D.device or

H.device) or local server (S.server).

Select REMOTE MEMBER: <span class="mark">\<Enter\></span>

Select DISTRIBUTION LIST: <span class="mark">?</span>

You may enter a new DISTRIBUTION LIST, if you wish

Answer with DISTRIBUTION LIST NAME

Choose from:

486 TEAM

G.IMG@RD4.VA.GOV

GUESS

IRM

IRM

K7 TESTING

K7.1 DISTRIBUTION

SHARED

You may enter a new DISTRIBUTION LIST, if you wish

NAME MUST BE 3-30 CHARACTERS, NOT NUMERIC OR STARTING WITH

PUNCTUATION

Select DISTRIBUTION LIST: <span class="mark">\<Enter\></span>

Select FAX RECIPIENT: <span class="mark">?</span>

You may enter a new FAX RECIPIENT, if you wish

Enter the fax recipient who should receive faxes sent to this mail

group.

Pointed-to File does not exist!

Select FAX RECIPIENT: <span class="mark">\<Enter\></span>

Select FAX GROUP: <span class="mark">?</span>

You may enter a new FAX GROUP, if you wish

Enter the fax group which should receive faxes sent to this mail

group.

Group must be public or user must be (surrogate of) creator of group.

Select FAX GROUP: <span class="mark">\<Enter\></span>

### CP Tools Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU; Synonym: TLS\] is located on the Capacity Planning menu \[XTCM MAIN\] (<u>Figure 2</u>). It contains the following options:

<span id="_Ref54082951" class="anchor"></span>Figure . CP Tools Manager Menu—Menu option

Select Capacity Planning Option: <span class="mark">CP TOOLS MANAGER MENU</span>

STA CP Environment Check \[KMPD STATUS\]

SST Start/Stop Timing Collection \[KMPD TMG START/STOP\]

PRM Edit CP Parameters File \[KMPD PARAM EDIT\]

TMT Timing Monitor \[KMPD TMG MONITOR\]

RPT CP Tools Reports ... \[KMPD CM TOOLS REPORTS\]

Each of these options is discussed in greater detail in the sections that follow.

#### CP Environment Check Option

The CP Environment Check option \[KMPD STATUS; Synonym: STA\] is located on the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\] (<u>Figure 4</u>). It allows users to check the capacity planning environment at their site. It displays data from the following areas (see <u>Figure 5</u>):

- Health Level Seven (HL7)
- Resource Usage Monitor (RUM)
- Statistical Analysis of Global Growth (SAGG)
- Timing

<span id="_Ref101763853" class="anchor"></span>Figure . CP Environment Check option—User prompts

Select CP Tools Manager Menu Option: <span class="mark">STA \<Enter\></span> CP Environment Check

Check Capacity Planning Environment

Select one of the following:

H HL7

R RUM

S SAGG

T Timing

Enter response:

#### HL7 Data

Users can use the CP Environment Check option \[KMPD STATUS\] to display the current Health Level Seven (HL7)-related statistics by choosing HL7 or H from the option list, as shown in <u>Figure 6</u>:

<span id="_Ref439164080" class="anchor"></span>Figure . CP Environment Check option: HL7—User prompts

Check Capacity Planning Environment

Select one of the following:

H HL7

R RUM

S SAGG

T Timing

Enter response: <span class="mark">HL7</span>

For both the HL7 and Timing options (see <u>Figure 7</u> and <u>Figure 19</u>), the CP Environment Check option \[KMPD STATUS\] displays the following information regarding the scheduled CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\]:

<table>
<caption><p><span id="_Toc439222305" class="anchor"></span>Table . CP Environment Check option—CM Tools Background Driver option statistics</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CM Tools Background Driver</td>
<td>Indicates the name of the CM Tools Background Driver option [KMPD BACKGROUND DRIVER].</td>
</tr>
<tr class="even">
<td>QUEUED TO RUN AT WHAT TIME</td>
<td><p>Indicates the date and time that the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] is scheduled to first run at the site. The job runs at this scheduled time depending on the Rescheduling Frequency indicated.</p>
<p>![](capacity-management-tools-version-3-user-manual/016.png) <strong>NOTE:</strong> The installation of the CM Tools software creates and sets this field automatically. It does the same thing as TaskMan’s Schedule/Unschedule Option, which saves the installer the job of having to set up the CM Tools Background Driver job later.</p></td>
</tr>
<tr class="odd">
<td>RESCHEDULING FREQUENCY</td>
<td>Indicates the frequency at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] is run (e.g., 1 day).</td>
</tr>
<tr class="even">
<td>TASK ID</td>
<td>This is the TaskMan task ID scheduled to run the CM Tools Background Driver option [KMPD BACKGROUND DRIVER].</td>
</tr>
<tr class="odd">
<td>QUEUED BY</td>
<td><p>This is the person who schedules the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] to run via TaskMan.</p>
<p>![](capacity-management-tools-version-3-user-manual/017.png) <strong>NOTE:</strong> The installation of the CM Tools software creates and sets this field automatically. It sets it to the name of the person doing the installation of the CM Tools software.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc439222305" class="anchor"></span>Table . CP Environment Check option—CM Tools Background Driver option statistics

If the CP Environment Check option \[KMPD STATUS\] detects that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER \] has *not* been scheduled, it only displays the following statement:

The CM Tools Background Driver \[KMPD BACKGROUND DRIVER\] is *not* scheduled

This alerts users to schedule the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] to run daily at 1:30 a.m. To schedule this option, use TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], which is located under the Taskman Management menu \[XUTM MGR\].

![](capacity-management-tools-version-3-user-manual/018.png) CAUTION: Capacity Planning Service *strongly* recommends that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:

- ^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- ^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.

In addition to the information regarding the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] (se Section <u>3.2</u>), the CP Environment Check option—HL7 \[KMPD STATUS\] displays the following HL7-specific and other general CM Tools report information (see <u>Table 4</u>, <u>Figure 7</u>, and <u>Figure 8</u>):

<table>
<caption><p><span id="_Ref102209357" class="anchor"></span>Table . CP Environment Check option: HL7—Report data fields</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>HL7 Dly Bckgrnd Last Start</td>
<td>Indicates the most recent date and time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] last daily run started HL7 data collection.</td>
</tr>
<tr class="even">
<td>HL7 Dly Bckgrnd Last Stop</td>
<td>Indicates the most recent date and time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] last daily run stopped HL7 data collection.</td>
</tr>
<tr class="odd">
<td>HL7 Dly Bkgrnd Total Time</td>
<td>Indicates the total time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] took in its most recent daily run of HL7 data collection.</td>
</tr>
<tr class="even">
<td>HL7 Wkly Backgrnd Last Start</td>
<td>Indicates the most recent date and time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] last weekly run started HL7 data collection.</td>
</tr>
<tr class="odd">
<td>HL7 Wkly Bckgrnd Last Stop</td>
<td>Indicates the most recent date and time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] last weekly run stopped HL7 data collection.</td>
</tr>
<tr class="even">
<td>HL7 Wkly Bckgrnd Total Time</td>
<td>Indicates the total time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] took in its most recent weekly run of HL7 data collection.</td>
</tr>
<tr class="odd">
<td>HL7 Purge Data After</td>
<td>Indicates the total time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] should purge HL7 data in the CM HL7 DATA file (#8973.1) (e.g., 2 weeks).</td>
</tr>
<tr class="even">
<td>HL7 Transmit Data to</td>
<td>Indicates the mail groups to which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] transmits HL7 data.</td>
</tr>
<tr class="odd">
<td>File Entries</td>
<td><p>Number of entries within the CM HL7 DATA file (#8973.1). This file is populated when the data collection is started. The report also includes the date range of data in this file from the oldest date to the most recent date.</p>
<p>![](capacity-management-tools-version-3-user-manual/019.png) <strong>REF:</strong> For more information on this file, see the Chapter 3, “Files,” in the <em>Capacity Management Tools Technical Manual</em>.</p></td>
</tr>
<tr class="even">
<td>CM Tools Routines</td>
<td>Number of CM TOOLS routines and problems, if any.</td>
</tr>
<tr class="odd">
<td>Node/CPU Data</td>
<td>List of nodes and CPU data. If sites believe this information is incorrect they should contact the Capacity Planning Team.</td>
</tr>
<tr class="even">
<td>KMP-CAPMAN Mail Group Members</td>
<td>List of KMP-CAPMAN mail group members. Sites should review this list and adjust membership in this mail group as necessary.</td>
</tr>
</tbody>
</table>

<span id="_Ref102209357" class="anchor"></span>Table . CP Environment Check option: HL7—Report data fields

<span id="_Ref102205913" class="anchor"></span>Figure . CP Environment Check option: HL7—Report (1 of 3)

<u>KMPD STATUS Apr 07, 2005@06:55:23 Page: 1 of 3</u>

Environment Check for HL7

CAPACITY MANAGEMENT TOOLS v3.0 \*\*1,2,3\*\*

CM Tools Background Driver.. KMPD BACKGROUND DRIVER

QUEUED TO RUN AT............ APR 08, 2005@01:30 (Friday)

RESCHEDULING FREQUENCY...... 1 day

TASK ID..................... 3334287

QUEUED BY................... CAPMANUSER,ONE A (Active)

Hl7 Dly Bckgrnd Last Start.. Apr 07, 2005@01:30:03

HL7 Dly Bckgrnd Last Stop... Apr 07, 2005@01:49:16

HL7 Dly Bkgrnd Total Time... 00:19:13

HL7 Wkly Backgrnd Last Start Apr 03, 2005@01:33:03

HL7 Wkly Bckgrnd Last Stop.. Apr 03, 2005@01:33:18

HL7 Wkly Bckgrnd Total Time. 00:00:15

HL7 Purge Data After........ 2 weeks

HL7 Transmit Data to........ CAPACITY,MANAGEMENT@REDACTED

S.KMP4-CM-SERVER@REDACTED

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span>

<span id="_Ref102205809" class="anchor"></span>Figure . CP Environment Check option: HL7—Report (2 of 3)

<u>KMPD STATUS Apr 07, 2005@06:56:23 Page: 2 of 3</u>

Environment Check for HL7

CAPACITY MANAGEMENT TOOLS v3.0 \*\*1,2,3\*\*

<u>+</u>

\# of Oldest Recent

File Entries Date Date

------------------------- ------- ------- -------

8973.1 - CM HL7 DATA 4,560 3/20/05 4/6/05

CM TOOLS routines........... 50 Routines - No Problems

Node/CPU Data............... 573A01 hp AlphaServer ES80 7/1000 (6)

573A02 hp AlphaServer ES80 7/1000 (6)

573A03 hp AlphaServer ES80 7/1000 (6)

573A04 hp AlphaServer ES80 7/1000 (6)

KMP-CAPMAN Mail Group....... CAPMANUSER,TWO

CAPMANUSER,THREE R

CAPMANUSER,FOUR A

CAPMANUSER,FIVE E

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span>

<span id="_Toc169674106" class="anchor"></span>Figure . CP Environment Check option: HL7—Report (3 of 3)

<u>KMPD STATUS Apr 07, 2005@06:56:43 Page: 3 of 3</u>

Environment Check for HL7

CAPACITY MANAGEMENT TOOLS v3.0 \*\*1,2,3\*\*

<u>+</u>

HL7 = Health Level Seven

Enter ?? for more actions

Select Action:Quit//

#### RUM Data

Users can use the CP Environment Check option \[KMPD STATUS\] to display the current Resource Usage Monitor (RUM)-related statistics by choosing RUM or R from the option list, as shown below:

<span id="_Toc169674107" class="anchor"></span>Figure . CP Environment Check option: RUM—User prompts

Check Capacity Planning Environment

Select one of the following:

H HL7

R RUM

S SAGG

T Timing

Enter response: <span class="mark">R \<Enter\></span> RUM

The CP Environment Check option—RUM \[KMPD STATUS\] displays the following information regarding the RUM Background Driver option \[KMPR BACKGROUND DRIVER\]:

<table>
<caption><p><span id="_Ref103069339" class="anchor"></span>Table . CP Environment Check option—RUM Background Driver option statistics</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RUM Background Driver</td>
<td>Indicates the name of the RUM Background Driver option [KMPR BACKGROUND DRIVER].</td>
</tr>
<tr class="even">
<td>QUEUED TO RUN AT WHAT TIME</td>
<td><p>Indicates the date and time that the RUM Background Driver option [KMPR BACKGROUND DRIVER] is scheduled to first run at the site. The job runs at this scheduled time depending on the Rescheduling Frequency indicated.</p>
<p>![](capacity-management-tools-version-3-user-manual/020.png) <strong>NOTE:</strong> The installation of the RUM software creates and sets this field automatically. It does the same thing as TaskMan’s Schedule/Unschedule Option, which saves the installer the job of having to set up the RUM Background Driver job later.</p></td>
</tr>
<tr class="odd">
<td>RESCHEDULING FREQUENCY</td>
<td>Indicates the frequency at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] is run (e.g., 1 day).</td>
</tr>
<tr class="even">
<td>TASK ID</td>
<td>This is the TaskMan task ID scheduled to run the RUM Background Driver option [KMPR BACKGROUND DRIVER].</td>
</tr>
<tr class="odd">
<td>QUEUED BY</td>
<td><p>This is the person who schedules the RUM Background Driver option [KMPR BACKGROUND DRIVER] to run via TaskMan.</p>
<p>![](capacity-management-tools-version-3-user-manual/021.png) <strong>NOTE:</strong> The installation of the RUM software creates and sets this field automatically. It sets it to the name of the person doing the installation of the RUM software.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref103069339" class="anchor"></span>Table . CP Environment Check option—RUM Background Driver option statistics

If the CP Environment Check option—RUM \[KMPD STATUS\] detects that the RUM Background Driver option \[KMPR BACKGROUND DRIVER \] has *not* been scheduled, it only displays the following statement:

The RUM Background Driver \[KMPD BACKGROUND DRIVER\] is *not* scheduled

This alerts users to schedule the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] to run daily at 1:00 a.m. To schedule this option, use TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], which is located under the Taskman Management menu \[XUTM MGR\].

![](capacity-management-tools-version-3-user-manual/022.png) CAUTION: Capacity Planning (CP) Service *strongly* recommends that the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] be scheduled to run daily at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP(“KMPR”) temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.  
  
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP(“KMPR”) temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file (#8971.1).

![](capacity-management-tools-version-3-user-manual/023.png) REF: For more information on the RUM software, see the [RUM documentation on the VA Software Document Library (VDL)](http://www4.va.gov/vdl/application.asp?appid=130).

In addition to the information regarding the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] (<u>Table 5</u>), the CP Environment Check option—RUM \[KMPD STATUS\] also displays the following additional RUM and general information (see <u>Figure 12</u> and <u>Figure 13</u>):

<table>
<caption><p><span id="_Toc439222308" class="anchor"></span>Table . CP Environment Check option: RUM—Report data fields</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RUM Dly Bckgrnd Last Start</td>
<td>Indicates the most recent date and time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] last daily run started RUM data collection.</td>
</tr>
<tr class="even">
<td>RUM Dly Bckgrnd Last Stop</td>
<td>Indicates the most recent date and time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] last daily run stopped RUM data collection.</td>
</tr>
<tr class="odd">
<td>RUM Dly Bkgrnd Total Time</td>
<td>Indicates the total time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] took in its most recent daily run of RUM data collection.</td>
</tr>
<tr class="even">
<td>RUM Wkly Backgrnd Last Start</td>
<td>Indicates the most recent date and time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] last weekly run started RUM data collection.</td>
</tr>
<tr class="odd">
<td>RUM Wkly Bckgrnd Last Stop</td>
<td>Indicates the most recent date and time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] last weekly run stopped RUM data collection.</td>
</tr>
<tr class="even">
<td>RUM Wkly Bckgrnd Total Time</td>
<td>Indicates the total time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] took in its most recent weekly run of RUM data collection.</td>
</tr>
<tr class="odd">
<td>RUM Purge Data After</td>
<td>Indicates the total time at which the RUM Background Driver option [KMPR BACKGROUND DRIVER] should purge RUM data in the RESOURCE USAGE MONITOR file (#8971.1) (e.g., 2 weeks).</td>
</tr>
<tr class="even">
<td>RUM Transmit Data to</td>
<td>Indicates the mail groups to which the RUM Background Driver option [KMPR BACKGROUND DRIVER] transmits RUM data.</td>
</tr>
<tr class="odd">
<td>RUM Routines</td>
<td>Number of RUM routines and any problems, if any.</td>
</tr>
<tr class="even">
<td>File Entries</td>
<td><p>Number of entries within the RESOURCE USAGE MONITOR file (#8971.1). This file is populated when the data collection is started. The report also includes the date range of data in this file from the oldest date to the most recent date.</p>
<p>![](capacity-management-tools-version-3-user-manual/024.png) <strong>REF:</strong> For more information on this file, see the Chapter 3, “Files,” in the <em>Capacity Management Tools Technical Manual</em>.</p></td>
</tr>
<tr class="odd">
<td>Node/CPU Data</td>
<td>List of nodes and CPU data. If sites believe this information is incorrect they should contact the Capacity Planning Team.</td>
</tr>
<tr class="even">
<td>KMP-CAPMAN Mail Group Members</td>
<td>List of KMP-CAPMAN mail group members. Sites should review this list and adjust membership in this mail group as necessary.</td>
</tr>
</tbody>
</table>

<span id="_Toc439222308" class="anchor"></span>Table . CP Environment Check option: RUM—Report data fields

<span id="_Toc169674109" class="anchor"></span>Figure . CP Environment Check option: RUM—Report (1 of 3)

<u>KMPD STATUS Apr 07, 2005@06:57:06 Page: 1 of 3</u>

Environment Check for RUM

CAPACITY MANAGEMENT - RUM v3.0 \*\*1\*\*

RUM Background Driver....... KMPR BACKGROUND DRIVER

QUEUED TO RUN AT............ APR 08, 2005@01:31 (Friday)

RESCHEDULING FREQUENCY...... 1 day

TASK ID..................... 3334332

QUEUED BY................... CAPMANUSER,TWO (Active)

Temporary collection global..

^KMPTMP(“KMPR”).............. Present

RUM Dly Bckgrnd Last Start... Apr 07, 2005@01:31

RUM Dly Bckgrnd Last Stop.... Apr 07, 2005@01:42:57

RUM Dly Bkgrnd Total Time.... 00:11:57

RUM Wkly Backgrnd Last Start. Apr 03, 2005@01:33:56

RUM Wkly Bckgrnd Last Stop... Apr 03, 2005@01:42:04

RUM Wkly Bckgrnd Total Time.. 00:08:08

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span>

<span id="_Ref102206524" class="anchor"></span>Figure . CP Environment Check option: RUM—Report (2 of 3)

<u>KMPD STATUS Apr 07, 2005@06:57:25 Page: 2 of 3</u>

Environment Check for RUM

CAPACITY MANAGEMENT - RUM v3.0 \*\*1\*\*

<u>+</u>

RUM Purge Data After......... 2 weeks

RUM Transmit Data to......... CAPACITY,MANAGEMENT@REDACTED

S.KMP2-RUM-SERVER@REDACTED

\# of Oldest Recent

File Entries Date Date

------------------------- ------- ------- -------

8971.1-RESOURCE USAGE MONITOR 231,257 3/20/05 4/6/05

RUM routines................ 17 Routines - No Problems

Node/CPU Data............... 573A01 hp AlphaServer ES80 7/1000 (6)

573A02 hp AlphaServer ES80 7/1000 (6)

573A03 hp AlphaServer ES80 7/1000 (6)

573A04 hp AlphaServer ES80 7/1000 (6)

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span>

<span id="_Ref102206549" class="anchor"></span>Figure . CP Environment Check option: RUM—Report (3 of 3)

<u>KMPD STATUS Apr 07, 2005@06:57:41 Page: 3 of 3</u>

Environment Check for RUM

CAPACITY MANAGEMENT - RUM v3.0 \*\*1\*\*

<u>+</u>

KMP-CAPMAN Mail Group....... CAPMANUSER,TWO

CAPMANUSER,THREE R

CAPMANUSER,FOUR A

CAPMANUSER,FIVE E

RUM = Resource Usage Monitor

Enter ?? for more actions

Select Action:Quit//

#### SAGG Data

Users can use the CP Environment Check option \[KMPD STATUS\] to display the current Statistical Analysis of Global Growth (SAGG)-related statistics by choosing SAGG or S from the option list, as shown below:

<span id="_Toc169674112" class="anchor"></span>Figure . CP Environment Check option: SAGG—User prompts

Check Capacity Planning Environment

Select one of the following:

H HL7

R RUM

S SAGG

T Timing

Enter response: <span class="mark">S \<Enter\></span> SAGG

The CP Environment Check option—SAGG \[KMPD STATUS\] displays the following information regarding the SAGG Master Background Task option \[KMPS SAGG REPORT\]:

<table>
<caption><p><span id="_Ref103069598" class="anchor"></span>Table . CP Environment Check option—SAGG Master Background Task option statistics</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Current Status</td>
<td><p>Indicates the scheduling status of the SAGG Master Background Task option [KMPS SAGG REPORT]. Values are:</p>
<ul>
<li><p>Scheduled</p></li>
<li><p>Unscheduled</p></li>
</ul></td>
</tr>
<tr class="even">
<td>SAGG Master Background Task</td>
<td>Indicates the name of the SAGG Master Background Task option [KMPS SAGG REPORT].</td>
</tr>
<tr class="odd">
<td>QUEUED TO RUN AT</td>
<td><p>Indicates the date and time that the SAGG Master Background Task option [KMPS SAGG REPORT] is scheduled to first run at the site. The job runs at this scheduled time depending on the Rescheduling Frequency indicated.</p>
<p>![](capacity-management-tools-version-3-user-manual/025.png) <strong>NOTE:</strong> The installation of the SAGG software creates and sets this field automatically. It does the same thing as TaskMan’s Schedule/Unschedule Option, which saves the installer the job of having to set up the SAGG Master Background Task job later.</p></td>
</tr>
<tr class="even">
<td>RESCHEDULING FREQUENCY</td>
<td>Indicates the frequency at which the SAGG Master Background Task option [KMPS SAGG REPORT] is run (e.g., 28 days).</td>
</tr>
<tr class="odd">
<td>TASK ID</td>
<td>This is the TaskMan task ID scheduled to run the SAGG Master Background Task option [KMPS SAGG REPORT].</td>
</tr>
<tr class="even">
<td>QUEUED BY</td>
<td><p>This is the person who schedules the SAGG Master Background Task option [KMPS SAGG REPORT] to run via TaskMan.</p>
<p>![](capacity-management-tools-version-3-user-manual/026.png) <strong>NOTE:</strong> The installation of the SAGG software creates and sets this field automatically. It sets it to the name of the person doing the installation of the SAGG software.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref103069598" class="anchor"></span>Table . CP Environment Check option—SAGG Master Background Task option statistics

If the CP Environment Check option—SAGG \[KMPD STATUS\] detects that the SAGG Master Background Task option \[KMPS SAGG REPORT\] has *not* been scheduled, it only displays the following statement:

The SAGG Master Background Task \[KMPS SAGG REPORT\] is *not* scheduled

This alerts users to schedule the SAGG Master Background Task option \[KMPS SAGG REPORT\] to run every 28 days on Friday, Saturday, or Sunday. The specific time to run is left up to the site. To schedule this option, use TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], which is located under the Taskman Management menu \[XUTM MGR\].

![](capacity-management-tools-version-3-user-manual/027.png) REF: For more information on the SAGG software, see the [SAGG documentation on the VA Software Document Library (VDL)](http://www4.va.gov/vdl/application.asp?appid=115).

In addition to the information regarding the SAGG Master Background Task option \[KMPS SAGG REPORT\] (<u>Table 7</u>), the CP Environment Check option—SAGG \[KMPD STATUS\] also displays the following additional SAGG and general information (see <u>Figure 15</u> and <u>Figure 16</u>):

<table>
<caption><p><span id="_Toc439222310" class="anchor"></span>Table . CP Environment Check option: SAGG—Report data fields</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Temporary Collection Global</td>
<td>^XTMP(“KMPS”) temporary global status (i.e., Present or NOT Present).</td>
</tr>
<tr class="even">
<td>VMS Disk Drives</td>
<td>List of VMS disk drives and directories that the SAGG Project collection routines are monitoring.</td>
</tr>
<tr class="odd">
<td>File Entries</td>
<td><p>Number of entries within the SAGG PROJECT file (#8970.1). This file is populated when the data collection is started.</p>
<p>![](capacity-management-tools-version-3-user-manual/028.png) <strong>REF:</strong> For more information on this file, see the Chapter 3, “Files,” in the <em>Capacity Management Tools Technical Manual</em>.</p></td>
</tr>
<tr class="even">
<td>SAGG Routines</td>
<td>Number of SAGG routines and any problems, if any.</td>
</tr>
<tr class="odd">
<td>Node/CPU Data</td>
<td>List of nodes and CPU data. If sites believe this information is incorrect they should contact the Capacity Planning Team.</td>
</tr>
<tr class="even">
<td>KMP-CAPMAN Mail Group Members</td>
<td>List of KMP-CAPMAN mail group members. Sites should review this list and adjust membership in this mail group as necessary.</td>
</tr>
</tbody>
</table>

<span id="_Toc439222310" class="anchor"></span>Table . CP Environment Check option: SAGG—Report data fields

<span id="_Ref102209505" class="anchor"></span>Figure . CP Environment Check option: SAGG—Report (1 of 3)

<u>KMPD STATUS Apr 07, 2005@06:57:59 Page: 1 of 3</u>

Environment Check for SAGG

SAGG PROJECT v1.8 \*\*1,2,3\*\*

Current Status.............. SCHEDULED

SAGG Master Background Task. KMPS SAGG REPORT

QUEUED TO RUN AT............ APR 15, 2005@21:00 (Friday)

RESCHEDULING FREQUENCY...... 28 days

TASK ID..................... 9201441

QUEUED BY................... CAPMANUSER,TWO (Active)

Temporary collection global.

^XTMP(“KMPS”)............... NOT Present

SAGG Project will collect metrics on ALL volumes

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span>

<span id="_Ref102209549" class="anchor"></span>Figure . CP Environment Check option: SAGG—Report (2 of 3)

<u>KMPD STATUS Apr 07, 2005@06:58:15 Page: 2 of 3</u>

Environment Check for SAGG

SAGG PROJECT v1.8 \*\*1,2,3\*\*

<u>+</u>

\# of

File Entries

------------------------- -------

8970.1-SAGG PROJECT 1

SAGG routines............... 7 Routines - No Problems

Node/CPU Data............... 573A01 hp AlphaServer ES80 7/1000 (6)

573A02 hp AlphaServer ES80 7/1000 (6)

573A03 hp AlphaServer ES80 7/1000 (6)

573A04 hp AlphaServer ES80 7/1000 (6)

KMP-CAPMAN Mail Group....... CAPMANUSER,TWO

\+ Enter ?? for more actions

Select Action: Next Screen// <span class="mark">\<Enter\></span>

<span id="_Toc169674116" class="anchor"></span>Figure . CP Environment Check option: SAGG—Report (3 of 3)

<u>KMPD STATUS Apr 07, 2005@06:58:29 Page: 3 of 3</u>

Environment Check for SAGG

SAGG PROJECT v1.8 \*\*1,2,3\*\*

<u>+</u>

CAPMANUSER,THREE R

CAPMANUSER,FOUR A

CAPMANUSER,FIVE E

SAGG = Statistical Analysis of Global Growth

Enter ?? for more actions

Select Action:Quit//

#### Timing Data

Users can use the CP Environment Check option \[KMPD STATUS\] to display the current Timing-related statistics by choosing Timing or T from the option list, as shown in <u>Figure 18</u>:

<span id="_Ref439165064" class="anchor"></span>Figure . CP Environment Check option: Timing—User prompts

Check Capacity Planning Environment

Select one of the following:

H HL7

R RUM

S SAGG

<span class="mark">T Timing</span>

Enter response: <span class="mark">TIMING</span>

For both the HL7 and Timing options (see <u>Figure 7</u> and <u>Figure 19</u>), the CP Environment Check option \[KMPD STATUS\] displays statistical information regarding the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER \] (see Section <u>3.2)</u>.

In addition to the information regarding the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER \] (see Section <u>3.2</u>), the CP Environment Check option—Timing \[KMPD STATUS\] displays the following Timing-specific and general report information (see <u>Table 9</u>, <u>Figure 19</u>, and <u>Figure 20</u>):

<table>
<caption><p><span id="_Ref103074422" class="anchor"></span>Table . CP Environment Check option: Timing—Report data fields</p></caption>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>TMG Collection Status</td>
<td>Indicates whether or not the Timing data is being collected (e.g., Running or Stopped).</td>
</tr>
<tr class="even">
<td>TMG Dly Bckgrnd Last Start</td>
<td>Indicates the most recent date and time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] last daily run started Timing data collection.</td>
</tr>
<tr class="odd">
<td>TIMING Dly Bckgrnd Last Stop</td>
<td>Indicates the most recent date and time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] last daily run stopped Timing data collection.</td>
</tr>
<tr class="even">
<td>TMG Dly Bkgrnd Total Time</td>
<td>Indicates the total time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] took in its most recent daily run of Timing data collection.</td>
</tr>
<tr class="odd">
<td>TMG Purge Data After</td>
<td>Indicates the total time at which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] should purge Timing data in the CP TIMING file (#8973.2) (e.g., 4 weeks).</td>
</tr>
<tr class="even">
<td>TMG Transmit Data to</td>
<td>Indicates the mail groups to which the CM Tools Background Driver option [KMPD BACKGROUND DRIVER] transmits Timing data.</td>
</tr>
<tr class="odd">
<td>File Entries</td>
<td><p>Number of entries within the CP TIMING file (#8973.2). This file is populated when the data collection is started. The report also includes the date range of data in this file from the oldest date to the most recent date.</p>
<p>![](capacity-management-tools-version-3-user-manual/029.png) <strong>REF:</strong> For more information on this file, see the Chapter 3, “Files,” in the <em>Capacity Management Tools Technical Manual</em>.</p></td>
</tr>
<tr class="even">
<td>CM Tools Routines</td>
<td>Number of CM Tools routines and any problems, if any.</td>
</tr>
<tr class="odd">
<td>Node/CPU Data</td>
<td>List of nodes and CPU data. If sites believe this information is incorrect they should contact the Capacity Planning Team.</td>
</tr>
<tr class="even">
<td>KMP-CAPMAN Mail Group Members</td>
<td>List of KMP-CAPMAN mail group members. Sites should review this list and adjust membership in this mail group as necessary.</td>
</tr>
</tbody>
</table>

<span id="_Ref103074422" class="anchor"></span>Table . CP Environment Check option: Timing—Report data fields

<span id="_Ref102209050" class="anchor"></span>Figure . CP Environment Check option: Timing—User prompts and report (1 of 2)

Check Capacity Planning Environment

Select one of the following:

H HL7

R RUM

S SAGG

<span class="mark">T Timing</span>

Enter response: <span class="mark">TIMING</span>

<u>KMPD STATUS Apr 07, 2005@06:58:46 Page: 1 of 2</u>

Environment Check for Timing

CAPACITY MANAGEMENT TOOLS v3.0 \*\*1,2,3\*\*

CM Tools Background Driver.. KMPD BACKGROUND DRIVER

QUEUED TO RUN AT............ APR 08, 2005@01:30 (Friday)

RESCHEDULING FREQUENCY...... 1 day

TASK ID..................... 3334287

QUEUED BY................... CAPMANUSER,ONE A (Active)

TMG Collection Status....... Running

TMG Dly Bckgrnd Last Start.. Apr 07, 2005@01:49:16

TMG Dly Bckgrnd Last Stop... Apr 07, 2005@01:52:57

TMG Dly Bkgrnd Total Time... 00:03:41

TMG Purge Data After........ 4 weeks

TMG Transmit Data to........ CAPACITY,MANAGEMENT@REDACTED

S.KMP6-TIMING-SERVER@REDACTED

\# of Oldest Recent

File Entries Date Date

------------------------- ------- ------- -------

\+ Enter ?? for more actions

Select Action:Next Screen// <span class="mark">\<Enter\></span>

<span id="_Ref102209860" class="anchor"></span>Figure . CP Environment Check option: Timing—Report (2 of 2)

<u>KMPD STATUS Apr 07, 2005@06:59:06 Page: 2 of 2</u>

Environment Check for Timing

CAPACITY MANAGEMENT TOOLS v3.0 \*\*1,2,3\*\*

<u>+</u>

8973.2 - CP TIMING 686,245 3/6/05 4/6/05

CM TOOLS routines........... 50 Routines - No Problems

Node/CPU Data............... 573A01 hp AlphaServer ES80 7/1000 (6)

573A02 hp AlphaServer ES80 7/1000 (6)

573A03 hp AlphaServer ES80 7/1000 (6)

573A04 hp AlphaServer ES80 7/1000 (6)

KMP-CAPMAN Mail Group....... CAPMANUSER,TWO

CAPMANUSER,THREE R

CAPMANUSER,FOUR A

CAPMANUSER,FIVE E

TMG = Timing Data

Enter ?? for more actions

Select Action:Quit//

#### Start/Stop Timing Collection Option

The Start/Stop Timing Collection option \[KMPD TMG START/STOP; Synonym: SST\] is located under the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\]. It is used to start/stop the CM Tools collection routines to start/stop collecting VistA HL7 workload data.

![](capacity-management-tools-version-3-user-manual/030.png) NOTE: This option requires that Patch OR\*3.0\*209 be installed in order to start collecting timing data and enable the data collection and report-related CM Tools software options..

Users should first invoke the CP Environment Check option \[KMPD STATUS\] to ensure that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is scheduled to run daily at 1:30 a.m.

![](capacity-management-tools-version-3-user-manual/031.png) REF: For more information on the CP Environment Check option, see the “<u>CP Environment Check</u>” section.

If the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is *not* shown as being scheduled to run in the future, use TaskMan’s Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], to schedule the KMPD BACKGROUND DRIVER option to run daily at 1:30 a.m.

![](capacity-management-tools-version-3-user-manual/032.png) CAUTION: Capacity Planning Service *strongly* recommends that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:

- ^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- ^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.

#### Starting CM Tools Collection

To start the CM Tools collection, do the following:

<span id="_Toc169674121" class="anchor"></span>Figure . Starting timing collection—User prompts

Select CP Tools Manager Menu Option: <span class="mark">START/STOP TIMING COLLECTION</span><span class="mark">Timing Collection is currently \[ STOPPED \]</span>

Do you want to ‘Start’ the collection? N// <span class="mark">Y \<Enter\></span> YES

<span class="mark">Timing Collection has been \[ Started \]</span>

STA CP Environment Check

SST Start/Stop Timing Collection

PRM Edit CP Parameters File

TMT Timing Monitor

RPT CP Tools Reports ...

Select CP Tools Manager Menu Option:

#### Stopping CM Tools Collection

To stop the CM Tools collection, do the following:

<span id="_Toc169674122" class="anchor"></span>Figure . Stopping timing collection—User prompts

Select CP Tools Manager Menu Option: <span class="mark">START/STOP TIMING COLLECTION</span><span class="mark">Timing Collection is currently \[ Running \]</span>

Do you want to ‘Stop’ the collection? N// <span class="mark">Y \<Enter\></span> YES

<span class="mark">Timing Collection has been \[ Stopped \]</span>

STA CP Environment Check

SST Start/Stop Timing Collection

PRM Edit CP Parameters File

TMT Timing Monitor

RPT CP Tools Reports ...

Select CP Tools Manager Menu Option:

#### TIMING^KMPDTU11 API

As of Patch KMPD\*2.0\*6, the TIMING^KMPDTU11() API is used to start/stop gathering CM Tools Timing data, allowing application developers to put hooks directly into a VistA software routine.

- Reference Type: Supported
- Category: Capacity Management Tools
- Integration Agreement (IA) \#: 5003
- Description: This API is designed to allow packages to put hooks into a routine to gather timing data (how long it takes to run).
- Format: TIMING^KMPDTU11(“ORWCV”,”673AAA”,1,\$H,\$G(DUZ))
- Input Parameters:
- KMPDSS: (Required) Subscript (free text) used to identify timing data.
- KMPDNODE: (Required) Node name (free text).
- KMPDST: (Required) Start/Stop - 1 = start timing, 2 = stop timing.
- KMPDHTM: (Optional) Current time in \$H format.
- KMPDUZ: (Optional) Current DUZ of user.
- KMPDCL: (Optional) Client name (free text). If *not* defined the current IO(“CLNM”) is used.

#### Examples

#### Example to Start TIMING:

\>D TIMING^KMPDTU11(“ORWCV”,”673AAA”,1,\$H,\$G(DUZ))

#### Example to Stop TIMING:

\>D TIMING^KMPDTU11(“ORWCV”,”673AAA”,2)

#### Edit CP Parameters File Option

The Edit CP Parameters File option \[KMPD PARAM EDIT; Synonym: PRM\] is located on the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\] (<u>Figure 4</u>). It allows editing of the Capacity Planning (CP) parameters in the CP PARAMETERS file (#8973).

![](capacity-management-tools-version-3-user-manual/033.png) REF: For more information on the CP Environment Check option, see the “<u>CP Environment Check</u>” section.

This option allows users to edit the following parameters:

<table>
<caption><p><span id="_Ref67461599" class="anchor"></span>Table . CP parameters/fields, stored in the CP PARAMETERS file (#8973)</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Field Name (Number)<br />
(in File #8973)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Purge HL7 Data After</td>
<td>HL7 WEEKS TO KEEP DATA field (#3.11)</td>
<td>HL7 Monitor Program—This is the number of weeks that HL7 data is retained in the CM HL7 DATA file (#8973.1) before purging. Enter a whole number between 2 and 19 (i.e., 2 weeks minimum and 19 weeks maximum). However, it is recommended that 2 weeks of data be retained.</td>
</tr>
<tr class="even">
<td>Purge RUM Data After</td>
<td>RUM WEEKS TO KEEP DATA field (#2.11)</td>
<td>RUM Monitor Program—This is the number of weeks that RUM data is retained in the RESOURCE USAGE MONITOR file (#8971.1) before purging. Enter a whole number between 2 and 20 (i.e., 2 weeks minimum and 20 weeks maximum). However, it is recommended that 2 weeks of data be retained.</td>
</tr>
<tr class="odd">
<td>Purge Timing Data After</td>
<td>TIMING WEEKS TO KEEP DATA field (#4.11)</td>
<td>Timing Monitor Program—This is the number of weeks that Timing data is retained in the CP TIMING file (#8973.2) before purging. Enter a whole number between 2 and 40 (i.e., 2 weeks minimum and 40 weeks maximum). However, it is recommended that 4 weeks of data be retained.</td>
</tr>
<tr class="even">
<td>Timing Monitor Alert - Seconds</td>
<td>MONITOR ALERT - SECONDS field (#19.02)</td>
<td>Timing Monitor Program—When the Timing Monitor is running, if the average time-to-load (TTL) a CPRS Coversheet exceeds this value, an alert appears on the Timing Monitor screen. Enter a whole number between 10 and 999.</td>
</tr>
<tr class="odd">
<td>Timing Monitor Update Rate - Min</td>
<td>MONITOR UPDATE RATE - MINUTES field (#19.01)</td>
<td>Timing Monitor Program—When the Timing Monitor is running, this is the number of minutes between automatic updates. Enter a whole number between 5 and 60.</td>
</tr>
<tr class="even">
<td>Scheduled Down Time Start</td>
<td>SCHEDULED DOWN TIME START (#5.01)</td>
<td>VistA Monitor Program—It is the date and time that the system scheduled down time is to begin. You <em>cannot</em> enter a value in the Scheduled Down Time Stop field unless this field has an entry.</td>
</tr>
<tr class="odd">
<td>Scheduled Down Time Stop</td>
<td>SCHEDULED DOWN TIME STOP (#5.02)</td>
<td>VistA Monitor Program—It is the date and time that the system scheduled down time is to end. You <em>cannot</em> enter a value in this field unless the Scheduled Down Time Start field has an entry.</td>
</tr>
<tr class="even">
<td>Reason for Down Time</td>
<td>REASON FOR DOWN TIME (#5.03)</td>
<td>VistA Monitor Program—It is the reason for the scheduled down time. The text in this field <em>must</em> be from 1 to 65 characters in length.</td>
</tr>
</tbody>
</table>

<span id="_Ref67461599" class="anchor"></span>Table . CP parameters/fields, stored in the CP PARAMETERS file (#8973)

<u>Figure 23</u>, <u>Figure 24</u>, and <u>Figure 25</u> show the prompts and user responses for the Edit CP Parameters File option:

<span id="_Ref67460668" class="anchor"></span>Figure . Running the Edit CP Parameters option—User prompts

CPG Capacity Planning Mail Group Edit

RUM RUM Manager Menu ...

TLS CP Tools Manager Menu ...

VPM VAX/ALPHA Capacity Management ...

Move Host File to Mailman

Response Time Log Menu ...

Select Capacity Planning Option: <span class="mark">CP TOOLS MANAGER MENU</span>

STA CP Environment Check

SST Start/Stop Timing Collection

PRM Edit CP Parameters File

TMT Timing Monitor

RPT CP Tools Reports ...

Select CP Tools Manager Menu Option: <span class="mark">EDIT CP PARAMETERS FILE</span>

After selecting the Edit CP Parameters File option, the user is automatically placed into the following ScreenMan form:

<span id="_Ref67460683" class="anchor"></span>Figure . Edit CP Parameters File option (ScreenMan)—User Prompts (*default* values)

CM Tools Parameters Edit Page 1

N. FLORIDA/S. GEORGIA HCS

Current Version: 3.0 Version Installed: MAR 11,2004@10:55

Current Patch: \*\*1,2,3,4,5\*\* Patch Installed: MAY 11,2006@15:08

Purge HL7 Data After: 2 Weeks Timing Monitor Update Rate - Min:

Purge Timing Data after: 4 Weeks Timing Monitor Alert - Seconds:

Purge RUM Data After: Weeks

Scheduled Down Time Start:

Scheduled Down Time Stop:

Reason for Down Time:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or ‘^’ followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

This screen (<u>Figure 24</u>) allows users to edit the parameter values that are stored in the CP PARAMETERS file (#8973), see <u>Table 10</u>.

#### Data Purges and Timing Monitor

<u>Figure 25</u> shows the parameters *after* the user has entered new values for data purges and the Timing Monitor:

<span id="_Ref67460695" class="anchor"></span>Figure . Edit CP Parameters File option (ScreenMan)—User Prompts when scheduling data purges and Timing Monitor (*updated* values)

CM Tools Parameters Edit Page 1

N. FLORIDA/S. GEORGIA HCS

Current Version: 3.0 Version Installed: MAR 11,2004@10:55

Current Patch: \*\*1,2,3,4,5\*\* Patch Installed: MAY 11,2006@15:08

Purge HL7 Data After: <span class="mark">2 Weeks</span> Timing Monitor Update Rate - Min: <span class="mark">30</span>

Purge Timing Data after: <span class="mark">4 Weeks</span> Timing Monitor Alert - Seconds: <span class="mark">10</span>

Purge RUM Data After: <span class="mark">2 Weeks</span>

Scheduled Down Time Start:

Scheduled Down Time Stop:

Reason for Down Time:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Refresh

Enter a command or ‘^’ followed by a caption to jump to a specific field.

COMMAND: Press \<PF1\>H for help Insert

In this example (<u>Figure 25</u>), the user has made entries for the data purge and Timing Monitor parameters only. In most cases, the recommended value was entered (see <u>Table 10</u>). Specifically, the user made the following entries:

- Purge HL7 Data After: 2 weeks (default)
- Purge Timing Data after: 4 weeks (default)
- Purge RUM Data After: 2 weeks (recommended)
- Timing Monitor Update Rate - Min: 30
- Timing Monitor Alert - Seconds: 10

After making the entries, the user saved and exited the screen.

#### Vista Monitor

The VistA Monitor allows Health Systems Implementation Training and Enterprise Support (HSITES) to determine if a site is down (*not* operating). The process is as follows:

1.  A message is sent from the Capacity Planning National Database to each site every 20 minutes, regardless of whether or not a reply is received back from the site.

![](capacity-management-tools-version-3-user-manual/034.png) NOTE: The current 20 minute time frame for polling a site was determined by the Capacity Planning (CP) Service. It is subject to change at the discretion of the CP Service or Office of Information & Technology (OI&T).

10. The message is received at the site via the CP Echo Server server-type option \[KMPD ECHO\].

<u>Figure 26</u> is a sample message that is sent from the Capacity Planning National Database to the KMPD ECHO server option at a site:

> <span id="_Ref231286913" class="anchor"></span>Figure . Sample message sent by the Capacity Planning National Database to the KMPD ECHO server option at the site

Subj: CP ECHO~5/15/06-30~REDACTED.VA.GOV  \[#8198307\] 05/15/06@10:02  1 line

From: MASTER CP ECHO SERVER  In ‘IN’ basket.   Page 1

-------------------------------------------------------------------------------

ECHO FROM REDACTED TO REDACTED.VA.GOV

Enter message action (in IN basket): Ignore//

11. The KMPD ECHO server option at the site then triggers a bulletin that sends an e-mail message back to the Capacity Planning National Database.

<u>Figure 27</u> is a sample bulletin returned from a site to the Capacity Planning National Database:

> <span id="_Ref135547652" class="anchor"></span>Figure . Sample bulletin sent by the KMPD ECHO server option at the site to the Capacity Planning National Database

> Subj: CP ECHO~5/15/06-31~REDACTED VHS (573)~  \[#63014754\]

> 05/15/06@10:03  2 lines

> From: ECHO BACK FROM REDACTED VHS  In ‘IN’ basket.   Page 1  \*New\*

> -------------------------------------------------------------------------------

> START=

> STOP=

> Enter message action (in IN basket): Ignore//

The START and STOP entries in the message body represent the values stored in the SCHEDULED DOWN TIME START (#5.01) and SCHEDULED DOWN TIME STOP (#5.02) fields in the CP PARAMETERS file (#8973). In this example (<u>Figure 27</u>), both fields are blank.

12. If the Capacity Planning National Database has *not* received a return message from the site after a certain period of time (e.g., one hour) and there are no entries in the SCHEDULED DOWN TIME START (#5.01) and SCHEDULED DOWN TIME STOP (#5.02) fields (see <u>Figure 27</u>), then a routine on the Capacity Planning National Database runs in the background and determines that the site is down or late reporting. When the site is considered to be in an unscheduled down time state, the Capacity Planning National Database automatically sends a message (alert) to a mail group notifying members of the situation and to take appropriate action.

![](capacity-management-tools-version-3-user-manual/035.png) NOTE: The current time frame used to determine when a site is considered in an unscheduled down time state is set by the Capacity Planning (CP) Service. It is subject to change at the discretion of the CP Service or Office of Information & Technology (OI&T).

<u>Figure 28</u> shows the parameters *after* the user has entered new values for scheduled down time:

> <span id="_Ref135549841" class="anchor"></span>Figure . Edit CP Parameters File option (ScreenMan)—User Prompts when scheduling system down time (*updated* values)

> CM Tools Parameters Edit Page 1

> N. FLORIDA/S. GEORGIA HCS

> Current Version: 3.0 Version Installed: MAR 11,2004@10:55

> Current Patch: \*\*1,2,3,4,5\*\* Patch Installed: MAY 11,2006@15:08

> Purge HL7 Data After: 2 Weeks Timing Monitor Update Rate - Min: 30

> Purge Timing Data after: 4 Weeks Timing Monitor Alert - Seconds: 10

> Purge RUM Data After: 2 Weeks

> Scheduled Down Time Start: <span class="mark">MAY 15,2006@17:00</span>

> Scheduled Down Time Stop: <span class="mark">MAY 15,2006@17:30</span>

> Reason for Down Time: <span class="mark">Test Schedule</span>

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> Enter a command or ‘^’ followed by a caption to jump to a specific field.

> COMMAND: Press \<PF1\>H for help Insert

In this example (<u>Figure 28</u>), the user has made entries for the scheduled down time parameters only. Specifically, the user made the following entries:

- Scheduled Down Time Start: MAY 15,2006@17:00
- Scheduled Down Time Stop: MAY 15,2006@17:30
- Reason for Down Time : Test Schedule

After making the entries, the user saved and exited the screen.

The next bulletin returned from a site to the Capacity Planning National Database would show the following:

> <span id="_Toc169674131" class="anchor"></span>Figure . Sample bulletin sent by the KMPD ECHO server option at the site to the Capacity Planning National Database

> Subj: CP ECHO~5/15/06-31~N. REDACTED VHS (573)~  \[#63014754\]

> 05/15/06@10:23  2 lines

> From: ECHO BACK FROM REDACTED VHS  In ‘IN’ basket.  Page 1  \*New\*

> ------------------------------------------------------------------------------<span class="mark">START=3060515.17</span>

> <span class="mark">STOP=3060515.1730</span>FT

> Enter message action (in IN basket): Ignore//

Since this is a scheduled down time for the site, no other additional alert message needs to be sent out.

#### Timing Monitor Option

The Timing Monitor option \[KMPD TMG MONITOR; Synonym: TMT\] is located on the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\] (<u>Figure 4</u>). This option updates itself automatically and displays the average number of seconds it takes Computerized Patient record System (CPRS) coversheets to load in a period of time. Data is displayed in a bar graph. The x-axis of the bar graph indicates the hours of the day (from 0 up to 23) and the y-axis indicates the average number of seconds it takes to load CPRS coversheets. This option can be left running on a terminal continuously collecting data.

The Timing Monitor displays data for each hour of the day and each new hour as it comes up (i.e., 0 – 23 hours). It updates the data according to the value in the MONITOR UPDATE RATE - MINUTES field (#19.01) in the CP PARAMETERS file (#8973). If there is no entry in Field \#19.01, the default is every 10 minutes. The CPRS coversheet load data is displayed in a bar graph for each hour the Timing Monitor is running. If the Timing Monitor is run continuously, the cycle repeats every 24 hours overlaying/replacing previous data and adjusting the bar graph accordingly. The bar graph is also adjusted for the latest information gathered based on the value in the MONITOR UPDATE RATE - MINUTES field (#19.01) in the CP PARAMETERS file (#8973).

The Timing Monitor also displays an Alert Message near the bottom of the screen if the average number of seconds to load a CPRS coversheet exceeds the value of the MONITOR ALERT - SECONDS field (#19.02) in the CP PARAMETERS file (#8973). If there is no entry in Field \#19.02, the default is 30 seconds. Both of these parameters can be edited using the Edit CP Parameters File option \[KMPD PARAM EDIT\].

<span id="_Toc169674132" class="anchor"></span>Figure . Running the Timing Monitor option—User prompts and report, *no* data

STA CP Environment Check

SST Start/Stop Timing Collection

PRM Edit CP Parameters File

<span class="mark">TMT Timing Monitor</span>

RPT CP Tools Reports ...

Select CP Tools Manager Menu Option: <span class="mark">TMT \<Enter\></span> Timing Monitor

Timing Data Monitor

\*\*\* There is currently no data in global ^KMPKMPUTMP(“KMPDT”,”ORWCV”) \*\*\*

<span id="_Toc169674133" class="anchor"></span>Figure . Running the Timing Monitor option—User prompts, *with* data

Timing Data Monitor

This option displays CPRS Coversheet time-to-load data, as a

bar graph, for the current day. This option can be left

running on a terminal (if desired). The monitor is updated

every 10 minutes (site configurable through the \[KMPD PARAM

EDIT\] Edit CP Parameters File option), and displays current

average time-to-load data starting at midnight. An alarm

message is displayed if the average time-to-load exceeds 30

seconds (site configurable through the \[KMPD PARAM EDIT\] Edit

CP Parameters File option).

Continue? YES// <span class="mark">\<Enter\></span>

Compiling timing stats.......

<u>Figure 32</u> shows a snapshot in time of average CPRS coversheet loads at a site over a 13-hour time span. The data is displayed in a bar graph format (bar graph colors have been enhanced for clarity in the display):

<span id="_Ref67806052" class="anchor"></span>Figure . Running the Timing Monitor option—Report, *no* alert

![](capacity-management-tools-version-3-user-manual/036.png)

(Bar graph colors have been enhanced for display purposes only)

In this example (<u>Figure 32</u>), the Timing Monitor option has been running for 13+ hours at a site. Thus, the sample graph displays the average CPRS coversheet loads from midnight (0 hour) to 1:00 p.m. (13:00 hour). If the Timing Monitor is left running, eventually a full 24-hour range of data would be displayed.

For this example, the site has set the Timing Monitor Alert - Seconds parameter (i.e., MONITOR ALERT - SECONDS field \[#19.02\] in the CP PARAMETERS file \[#8973\]) to 30 seconds. The graph shows that the average CPRS coversheet loads did *not* exceed the 30 second threshold except at the 11<sup>th</sup> hour. During the 11<sup>th</sup> hour the average CPRS coversheet load was approximately 36 seconds. If the user had checked the monitor at the 11<sup>th</sup> hour he/she would have gotten an alert message displayed at the bottom of the screen.

![](capacity-management-tools-version-3-user-manual/037.png) REF: For an example of an alert message due to coversheet loads exceeding the Timing Monitor Alert - Seconds parameter, see <u>Figure 33</u>.

Sites can set the Timing Monitor Alert - Seconds parameter from 10 to 999 seconds via the MONITOR ALERT - SECONDS field (#19.02) in the CP PARAMETERS file (#8973).

To quit/stop the Timing Monitor, enter a “Q” after the “\[Q\]uit \[U\]pdate” prompt. To refresh the data/bar graph, enter a “U” after the “\[Q\]uit \[U\]pdate” prompt.

![](capacity-management-tools-version-3-user-manual/038.png) REF: For more information on the CP parameters, see the “<u>Edit CP Parameters File</u>” section and <u>Table 10</u>.

<u>Figure 33</u> shows a sample report with an alert message displayed:

<span id="_Ref67808807" class="anchor"></span>Figure . Running the Timing Monitor option—Report, *with* alert

![](capacity-management-tools-version-3-user-manual/039.png)

In this example (<u>Figure 33</u>), the Timing Monitor option has been running for 13+ hours at a site. Thus, the sample graph displays the average CPRS coversheet loads from midnight (0 hour) to 1:00 p.m. (13:00 hour).

For this example, the site has set the Timing Monitor Alert - Seconds parameter (i.e., MONITOR ALERT - SECONDS field \[#19.02\] in the CP PARAMETERS file \[#8973\]) to 10 seconds. The graph shows that the average CPRS coversheet loads exceeded the 10 second threshold during the 1<sup>st</sup> through the 13<sup>th</sup> hour. Since the user is checking the monitor at the 13<sup>th</sup> hour, where the CPRS coversheet load took approximately 15 seconds, he/she saw the alert message displayed at the bottom of the screen:

ALERT!!! – Current Average Time-To-Load exceeds ‘10 seconds’

Sites can set the Timing Monitor Alert - Seconds parameter from 10 to 999 seconds via the MONITOR ALERT - SECONDS field (#19.02) in the CP PARAMETERS file (#8973).

![](capacity-management-tools-version-3-user-manual/040.png) REF: For more information on the CP parameters, see the “<u>Edit CP Parameters File</u>” section and <u>Table 10</u>.

#### CP Tools Reports Menu

The CP Tools Reports menu \[KMPD CM TOOLS REPORTS; Synonym: RPT\] is available on the CP Tools Manager Menu \[KMPD CM TOOLS MANAGER MENU\], as shown below:

<span id="_Toc169674136" class="anchor"></span>Figure . Accessing the CP Tools Reports—Menu option

Select CP Tools Manager Menu Option: <span class="mark">CP TOOLS REPORTS</span>

TMG Timing Reports ...

Select CP Tools Reports Option:

The CP Tools Reports menu \[KMPD CM TOOLS REPORTS\] contains a report option that generates report information for a variety of Computerized Patient Record System (CPRS) event statistics accumulated within the CP TIMING file (#8973.2).

The CP Tools Reports menu contains the following sub-menu option:

<span id="_Toc169674137" class="anchor"></span>Figure . CP Tools Reports—Menu option

TMG Timing Reports ... \[KMPD TMG REPORTS\]

This sub-menu option is discussed in greater detail in Section <u>3.1.2.5.1</u>.

#### Timing Reports Menu

The Timing Reports menu \[KMPD TMG REPORTS; Synonym: TMG\] is located under the CP Tools Reports menu \[KMPD CM TOOLS REPORTS\]. It contains the following report options:

<span id="_Toc169674138" class="anchor"></span>Figure . Timing Reports—Menu option

Select CP Tools Reports Option: <span class="mark">TIMING REPORTS</span>

AVD Average Daily Coversheet Load \[KMPD TMG AVG TTL\]

AVH Average Hourly Coversheet Load \[KMPD TMG HRLY TTL\]

DTD Detailed Daily Coversheet Load \[KMPD TMG DLY TTL DETAIL\]

DTH Detailed Hourly Coversheet Load \[KMPD TMG HRLY TTL DETAIL\]

TAL Threshold Alert \[KMPD TMG TTL ALERT\]

RTA Real-Time Threshold Alert \[KMPD TMG TTL ALERT RT\]

RAV Real-Time Average Hourly Coversheet Load \[KMPD TMG HRLY TTL RT\]

Select Timing Reports Option:

The options on this menu generate report information for a variety of Computerized Patient Record System (CPRS) event statistics accumulated within the CP TIMING file (#8973.2). These report options display CPRS coversheet load time data. The CPRS coversheet is the main CPRS software page, which is a screen of the CPRS patient chart that displays an overview of the patient’s record.

Each of these options is discussed in greater detail in the sections that follow.

#### Average Daily Coversheet Load Option

The Average Daily Coversheet Load option \[KMPD TMG AVG TTL; Synonym: AVD\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the daily average time-to-load (TTL) value for the coversheet at a site. Average time-to-load values are given for either daily prime time or non-prime time periods.

<u>Figure 37</u> shows the prompts and user responses for the Average Daily Coversheet Load option:

<span id="_Ref231287002" class="anchor"></span>Figure . Average Daily Coversheet Load option—User prompts

Select Timing Reports Option: <span class="mark">AVERAGE DAILY COVERSHEET LOAD</span>

Average Coversheet Time-to-Load (TTL) Report

This report displays the daily average time-to-load value for

the coversheet at this site. Average time-to-load values are

given for either daily prime time or non-prime time periods.

Select End Date: (9/20/2009 - 05/19/2009): May 19, 2009// <span class="mark">\<Enter\></span> (MAY 19, 2009)

Select \# of Days Review: (1-30): 7// <span class="mark">\<Enter\></span>

Select one of the following:

1 Prime Time

2 Non-Prime Time

Select Time Frame: 1// <span class="mark">\<Enter\></span> Prime Time

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats..........................................................

...............

<u>Figure 38</u> shows the actual report generated from the Average Daily Coversheet Load option:

<span id="_Ref231287024" class="anchor"></span>Figure . Average Daily Coversheet Load option—Report

Average Coversheet Time-to-Load (TTL) Report

<span class="mark">Prime Time - FOREGROUND</span>

May 13, 2009 - May 19, 2009 Printed: 05/20/09

\|---------------Seconds---------------\|

Date Average TTL Minimum TTL Maximum TTL \# of CV Loads

--------------------------------------------------------------------------------

05/13/09 0 0 0 0

05/14/09 14 3 500 16,465

05/15/09 14 3 615 18,674

05/16/09 14 3 288 18,123

05/17/09 12 3 436 16,955

05/18/09 0 0 0 0

05/19/09 0 0 0 0

Incomplete: 0

CV = Coversheet

TTL = Time-to-Load

Press RETURN to continue:

This report provides the following data regarding coversheet loads at a site for a specified number of days:

- Header Second Line—Denotes if the coversheet load was executed in the Foreground, Background, or both. Reports display metrics for Foreground, Background, and Combined timings.
- Date—Specific day that the coversheet load began.
- Average TTL—Average time-to-load (in seconds) for each day.
- Minimum TTL—Minimum time-to-load (in seconds) for each day.
- Maximum TTL—Maximum time-to-load (in seconds) for each day.
- \# of CV Loads—Total number of coversheet loads for each day.
- Incomplete—Total number of coversheets where the report option was unable to determine the coversheet end load time, so it was unable to calculate the time to load the coversheet.

Sites can use this report to track average coversheet load times. It also indicates the shortest and longest coversheets time-to-load (TTL). If some of the longer load times are extreme, sites can run any of the other Timing Report options to find out more specific information. For example, sites can then run the Detailed Hourly Coversheet Load report option \[KMPD TMG HRLY TTL DETAIL\] to see how many loads were over 90 seconds, etc., and also run the Threshold Alert report option \[KMPD TMG TTL ALERT\] to get a breakdown of which user/client/IP address had slow times.

![](capacity-management-tools-version-3-user-manual/041.png) REF: For more information on the Detailed Hourly Coversheet Load report option \[KMPD TMG HRLY TTL DETAIL\], see the “<u>Detailed Hourly Coversheet Load</u>” section.  
  
For more information on the Threshold Alert report option \[KMPD TMG TTL ALERT\], see the “<u>Threshold Alert</u>” section.

For this report, the user chose to report on the last 7 days of coversheet load data from 05/13/09 to 05/19/09. From the report, on 05/15/09, for example, there were a total of 18,674 coversheets loaded with an average time-to-load (TTL) for each coversheet of 14 seconds. On that same day the shortest coversheet time-to-load (TTL) took only 3 seconds and the longest coversheet time-to-load (TTL) took 615 seconds (10 minutes and 15 seconds). Zeroes under the “Average TTL,” “Minimum TTL,” “Maximum TTL,” and “# of CV Loads” columns indicates that the coversheets took less than one second to load (see report data for 05/13/09, 05/18/09, and 05/19/09).

#### Average Hourly Coversheet Load Option

The Average Hourly Coversheet Load option \[KMPD TMG HRLY TTL; Synonym: AVH\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the hourly average time-to-load (TTL) value for the coversheet at a site over a 24-hour period.

<u>Figure 39</u> shows the prompts and user responses for the Average Hourly Coversheet Load option:

<span id="_Ref231287038" class="anchor"></span>Figure . Average Hourly Coversheet Load option—User prompts

Select Timing Reports Option: <span class="mark">AVERAGE HOURLY COVERSHEET LOAD</span>

Hourly Coversheet Time-to-Load (TTL) Report

This report displays the hourly average time-to-load value for

the coversheet at this site over 24 hours.

Select End Date: (9/20/2009 - 05/19/2009): May 19, 2009// <span class="mark">\<Enter\></span> (MAY 19, 2009)

Select \# of Days Review: (1-30): 1// <span class="mark">\<Enter\></span>

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats......

<u>Figure 40</u> shows the actual report generated from the Average Hourly Coversheet Load option:

<span id="_Ref231287060" class="anchor"></span>Figure . Average Hourly Coversheet Load option—Report

Hourly Coversheet Time-to-Load (TTL) Report

<span class="mark">Combined FOREGROUND and BACKGROUND Coversheet Loads</span>

May 19, 2009 - May 19, 2009 Printed: 05/20/09

\|---------------Seconds---------------\|

Date Hour TTL Average TTL Minimum TTL Maximum \# of CV Loads

--------------------------------------------------------------------------------

05/19/09 00 14 6 79 52

01 16 5 83 90

02 16 5 100 131

03 10 5 39 69

04 26 5 150 77

05 14 5 86 98

06 13 5 65 77

07 11 5 44 134

08 10 4 42 167

09 9 4 55 161

10 10 4 53 254

11 10 5 69 225

12 11 4 166 210

13 9 4 43 203

14 12 4 59 245

Enter RETURN to continue or ‘^’ to exit: <span class="mark">\<Enter\></span>

Hourly Coversheet Time-to-Load (TTL) Report

May 19, 2009 - May 19, 2009 Printed: 05/20/09

\|---------------Seconds---------------\|

Date Hour TTL Average TTL Minimum TTL Maximum \# of CV Loads

--------------------------------------------------------------------------------

15 11 4 60 213

16 11 5 38 137

17 10 5 67 217

18 12 4 64 172

19 11 5 58 154

20 11 5 43 112

21 13 5 72 139

22 12 5 58 94

23 12 5 58 132

----------

3,563

Incomplete: 0

CV = Coversheet

TTL = Time-to-Load

Press RETURN to continue:

This report provides the following data regarding coversheet loads at a site for each hour of the specified number of days:

- Header Second Line—Denotes if the coversheet load was executed in the Foreground, Background, or both. Reports display metrics for Foreground, Background, and Combined timings.
- Date—Specific day that the coversheet load began.
- Hour—Specific hour that the coversheet load began (00 - 23).
- TTL Average—Average time-to-load (in seconds) for each hour of a day.
- TTL Minimum—Minimum time-to-load (in seconds) for each hour of a day.
- TTL Maximum—Maximum time-to-load (in seconds) for each hour of a day.
- \# of CV Loads—Total number of coversheet loads for:
- Each hour of the day.
- Grand total for the entire day.
- Incomplete—Total number of coversheets where the report option was unable to determine the coversheet end load time, so it was unable to calculate the time to load the coversheet.

This report allows sites to identify times of the day when the most coversheet loads are taking place, and when the longest times to load are taking place. Sites can run any of the other Timing Report options to find out more specific information.

For this report, the user chose to report on 24 hours of coversheet load data for a single day, 05/19/09. From the report, at 12:00 p.m. to 12:59 p.m. on 05/19/09, for example, there were a total of 210 coversheets loaded with an average time-to-load (TTL) for each coversheet of 11 seconds. At that same hour the shortest coversheet time-to-load (TTL) took only 4 seconds and the longest coversheet time-to-load (TTL) took 166 seconds (2 minutes and 46 seconds).

#### Detailed Daily Coversheet Load Option

The Detailed Daily Coversheet Load option \[KMPD TMG DLY TTL DETAIL; Synonym: DTD\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the daily time-to-load (TTL) values for the coversheet at a site. The report breaks the time-to-load (TTL) metrics into ten second groupings.

<u>Figure 41</u> shows the prompts and user responses for the Detailed Daily Coversheet Load option:

<span id="_Ref231287077" class="anchor"></span>Figure . Detailed Daily Coversheet Load option—User prompts

Select Timing Reports Option: <span class="mark">DETAILED DAILY COVERSHEET LOAD</span>

Daily Coversheet Time-to-Load (TTL) Detailed Report

This detailed report displays daily time-to-load values for the

coversheet at this site. The report breaks the time-to-load

metrics into ten second groupings.

Select End Date: (9/20/2009 - 05/19/2009): May 19, 2009// <span class="mark">T-3 \<Enter\></span> (MAY 17, 2009)

Select \# of Days Review: (1-28): 1// <span class="mark">\<Enter\></span>

Select one of the following:

1 Prime Time

2 Non-Prime Time

Select Time Frame: 1// <span class="mark">\<Enter\></span> Prime Time

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats...................

<u>Figure 42</u> shows the actual report generated from the Detailed Daily Coversheet Load option:

<span id="_Ref231287097" class="anchor"></span>Figure . Detailed Daily Coversheet Load option—Report

Prime Time

May 17, 2009 - May 17, 2009 Printed: 05/20/09

Date TTL Seconds \# of CV Loads CV Percent

--------------------------------------------------------------------------------

05/17/09 0 to \<10 8,682 51.2%

10 to \<20 6,273 37.0%

20 to \<30 1,238 7.3%

30 to \<40 374 2.2%

40 to \<50 175 1.0%

50 to \<60 77 0.5%

60 to \<70 51 0.3%

70 to \<80 30 0.2%

80 to \<90 18 0.1%

90 or greater 37 0.2%

---------- ----------

16,955 100%

Incomplete 0

CV = Coversheet Coversheet sections run in :

TTL = Time-to-Load <span class="mark">Both Foreground and Background</span>

Press RETURN to continue:

This report provides the following data regarding detailed daily coversheet load data at a site in 10-second intervals for the specified days:

- Date—Specific day that the coversheet load began.
- TTL Seconds—Time-To-Load 10-second interval ranges.
- \# of CV Loads—Total number of coversheet loads in the specified days within each 10-second time interval.
- CV Percent—Total percentage of coversheet loads in the specified days within each 10-second time interval.
- Total—Grand total of coversheet loads for the specified days.
- Incomplete—Total number of coversheets where the report option was unable to determine the coversheet end load time, so it was unable to calculate the time to load the coversheet.
- Report Footer—Denotes if the coversheet load was executed in the Foreground, Background, or both.

If the report indicates an “excessive” time-to-load (TTL) for a large percentage of coversheets, sites can run any of the other Timing Report options to get more specific information. What is considered “excessive” is site-specific (e.g., over 60 seconds or over 90 seconds, etc.).

For this report, the user chose to report detailed daily coversheet load data for a single day, 05/17/09 during prime time hours. The report shows that 51.2% (i.e., 8,682 coversheets) took less than 10 seconds to load. The report also shows that on that same day .2% (i.e., 37 coversheets) took 90 seconds or more to load. Overall, the report further shows that 95.5% of the coversheets loaded in less than 30 seconds.

#### Detailed Hourly Coversheet Load Option

The Detailed Hourly Coversheet Load option \[KMPD TMG HRLY TTL DETAIL; Synonym: DTH\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the hourly time-to-load (TTL) values for the coversheet at a site. The report breaks the time-to-load metrics into ten second groupings.

<u>Figure 43</u> shows the prompts and user responses for the Detailed Hourly Coversheet Load option:

<span id="_Ref231287110" class="anchor"></span>Figure . Detailed Hourly Coversheet Load option—User prompts

Select Timing Reports Option: <span class="mark">DETAILED HOURLY COVERSHEET LOAD</span>

Hourly Coversheet Time-to-Load (TTL) Detail Report

This detail report displays the hourly time-to-load values

for the coversheet at this site. The report breaks the

time-to-load metrics into ten second groupings.

Select End Date: (9/20/2009 - 05/19/2009): May 19, 2009// <span class="mark">\<Enter\></span> (MAY 19, 2009)

Select Hour(s) to Review: (0-23): 8// <span class="mark">\<Enter\></span>

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats...

<u>Figure 44</u> shows the actual report generated from the Detailed Hourly Coversheet Load option:

<span id="_Ref231287126" class="anchor"></span>Figure . Detailed Hourly Coversheet Load option—Report

Hourly Coversheet Time-to-Load (TTL) Detail Report

May 19, 2009 - May 19, 2009 Printed: 05/20/09

Date Hr TTL Seconds \# CV Loads CV Percent

--------------------------------------------------------------------------------

05/19/09 8 0 to \<10 104 62.3%

10 to \<20 53 31.7%

20 to \<30 6 3.6%

30 to \<40 3 1.8%

40 to \<50 1 0.6%

50 to \<60 0 0.0%

60 to \<70 0 0.0%

70 to \<80 0 0.0%

80 to \<90 0 0.0%

90 or greater 0 0.0%

---------- ----------

167 100%

Incomplete 0

CV = Coversheet Coversheet sections run in :

TTL = Time-to-Load <span class="mark">Foreground Only</span>

Press RETURN to continue:

This report provides the following data regarding detailed hourly coversheet load data at a site in 10-second intervals for the specified hours:

- Date—Specific day that the coversheet load began.
- HR—Specific hour that the coversheet load began.
- TTL Seconds—Time-To-Load 10-second interval ranges.
- \# CV Loads—Total number of coversheet loads in the specified hours within each 10-second time interval.
- CV Percent—Total percentage of coversheet loads in the specified hours within each 10-second time interval.
- Total—Grand total of coversheet loads for the specified hours.
- Incomplete—Total number of coversheets where the report option was unable to determine the coversheet end load time, so it was unable to calculate the time to load the coversheet.
- Report Footer—Denotes if coversheet load was executed in the Foreground, Background, or both.

As with all Timing Report options, sites can run any of the other Timing Report options to find out more specific information.

For this report, the user chose to report detailed hourly coversheet load data for a single hour, 8:00:00 a.m. to 8:59:59 a.m. on 05/19/09. The report shows that within that hour 62.3% (i.e., 104 coversheets) took less than 10 seconds to load. The report also shows that within that hour on the same day .6% (i.e., 37 coversheets) took less than 50 seconds to load. Overall, the report further shows that 97.6% of the coversheets loaded in less than 30 seconds within that hour. Finally, the report shows that no coversheet took more than 50 seconds total to load within that hour.

#### Threshold Alert Option

The Threshold Alert option \[KMPD TMG TTL ALERT; Synonym: TAL\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the particular coversheet loads that had excessive time-to-load (TTL) values. This report searches for a particular person, client name, or Internet Protocol (IP) address. There is no upper limit on the Time-To-Load (TTL) Threshold.

<u>Figure 45</u> shows the prompts and user responses for the Threshold Alert option:

<span id="_Ref231287138" class="anchor"></span>Figure . Threshold Alert option—User prompts

Select Timing Reports Option: <span class="mark">THRESHOLD ALERT</span>

Coversheet Time-to-Load (TTL) Alert Report

This alerting report shows the particular coversheet loads

that had excessive time-to-load values. This report will

search for a particular person, a particular client name or

IP address.

Select End Date: (9/20/2009 - 05/19/2009): May 19, 2009// <span class="mark">T-3 \<Enter\></span> (MAY 17, 2009)

Select Hour(s) to Review: (0-23): 8// <span class="mark">\<Enter\></span>

Select Time-To-Load Threshold (Seconds): 60// <span class="mark">\<Enter\></span>

Select one of the following:

1 User Name

2 Client Name

3 IP Address

4 Any Occurrence

Search By: 4// <span class="mark">\<Enter\></span> Any Occurrence

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats.....

<u>Figure 46</u> shows the actual report generated from the Threshold Alert option:

<span id="_Ref231287153" class="anchor"></span>Figure . Threshold Alert option—Report

Coversheet Time-to-Load (TTL) Alert Report

May 17, 2009 - May 17, 2009 Printed: 05/20/09

Any Occurrence:

Threshold: 60 seconds

Date Time User Name Client Name IP Address Time-to-Load

--------------------------------------------------------------------------------

05/17/09 08:11 KMPDUSER,THREE xxx-xx57738.v08 99.99.99.16 71

08:21 KMPDUSER,FOUR xxx-xx56313.v08 99.99.9.108 63

08:29 KMPDUSER,FIVE xxx-xx45760.gai 99.99.9.19 78

08:30 KMPDUSER,SIX xxx-xx59283.v08 99.99.99.54 76

08:32 KMPDUSER,SEVEN L xxx-xx57703.v08 99.99.99.33 64

08:35 KMPDUSER,EIGHT xxx-xx48247.gai 99.99.9.225 63

08:37 KMPDUSER,NINE xxx-xx57710.v08 99.99.9.229 87

08:38 KMPDUSER,NINE xxx-xx57710.v08 99.99.9.229 87

08:39 KMPDUSER,TEN C xxx-xx02.gaines 99.99.9.14 64

08:40 KMPDUSER,11 xxx-xx43202.gai 99.99.99.237 104

08:43 KMPDUSER,12 xxx-xx56231.v08 99.99.9.114 65

08:52 KMPDUSER,12 xxx-xx56231.v08 99.99.9.114 123

08:56 KMPDUSER,12 xxx-xx56231.v08 99.99.9.114 117

Press RETURN to continue:

This report provides the following data regarding threshold alert data at a site listing only those coversheet loads exceeding the threshold interval chosen by the user for the specified hours on the specified days:

- Date—Specific day that the coversheet load began.
- Time—Specific time that the coversheet load began (hours and minutes).
- User name—Name of the person signed on to the client workstation loading the coversheet.
- Client Workstation—Name of the client workstation that loaded the coversheet.
- IP Address—Internet Protocol (IP) address of the client workstation that loaded the coversheet.
- Time-To-Load—Total elapsed time to load the coversheet; loads that went beyond the threshold interval. Displayed metrics include the sum of Foreground and Background timings.

This report allows sites to find “out of line” load times. They can then track down the problem (e.g., network problem, individual CPRS setting problems, etc.). Again, as with all Timing Reports, sites can run any of the other Timing Report options to find out more specific information.

For this report, the user chose to report on coversheet loads that exceeded 60 seconds between 8:00:00 a.m. and 8:59:59 a.m. on 05/17/09. The report shows that the longest coversheet load took 123 seconds at 8:52 a.m. KMPDUSER,12 signed onto the client workstation identified as “xxx-xx56231.v08” with an IP address of 99.99.9.114 and loaded that particular coversheet.

#### Real-Time Threshold Alert Option

The Real-Time Threshold Alert option \[KMPD TMG TTL ALERT RT; Synonym: RTA\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the particular coversheet loads that have excessive time-to-load (TTL) values for TODAY (real-time). This report searches for a particular person, client name, or Internet Protocol (IP) address.

<u>Figure 47</u> shows the prompts and user responses for the Real-Time Threshold Alert option:

<span id="_Ref231287168" class="anchor"></span>Figure . Real-Time Threshold Alert option—User prompts

Select Timing Reports Option: <span class="mark">REAL-TIME THRESHOLD ALERT</span>

Coversheet Time-to-Load Alert Report \> Real-Time

This alerting report shows the particular coversheet loads

that have excessive time-to-load values for TODAY (Real-Time).

This report will search for a particular person, a particular

client name or IP address.

==\> building Hours list......

Select Hour(s): (0-8): <span class="mark">0-8</span>

Select Time-To-Load Threshold (Seconds): 60// <span class="mark">\<Enter\></span>

Select one of the following:

1 User Name

2 Client Name

3 IP Address

4 Any Occurrence

Search By: 4// <span class="mark">\<Enter\></span> Any Occurrence

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats......

This is a real-time report option. Thus, if it is 8:30 a.m. when the site runs this report option, the data is only available from midnight to 8:00 a.m. However, if the option is run at 2:00 p.m. (14:00) the data is available from midnight to 1400 hours.

<u>Figure 48</u> show the actual report generated from the Real-Time Threshold Alert option:

<span id="_Ref231287184" class="anchor"></span>Figure . Real-Time Threshold Alert option—Report (1 of 3)

Coversheet Time-to-Load Alert Report \> Real-Time

Hour(s): 0,1,2,3,4,5,6,7,8, Printed: 05/20/09

Any Occurrence:

Threshold: 60 seconds

Date Time User Name Client Name IP Address Time-to-Load

--------------------------------------------------------------------------------

05/20/09 00:24 KMPDUSER,13 xxx-xx57694.v08 99.99.99.238 70

00:41 KMPDUSER,TEN C xxx-xx02.gaines 99.99.91.14 72

00:57 KMPDUSER,TEN C xxx-xx02.gaines 99.99.9.14 78

00:59 KMPDUSER,14 xxx-xx45112.gai 99.99.9.59 143

02:01 KMPDUSER,15 xxx-xx50691.gai 99.99.9.232 69

03:45 KMPDUSER,13 xxx-xx50606.gai 99.99.9.154 74

03:51 KMPDUSER,16 xxx-xx.v08. 99.99.99.17 65

03:57 KMPDUSER,16 xxx-xx.v08. 99.99.99.17 61

04:02 KMPDUSER,17 xxx-xx45098.gai 99.99.99.15 161

04:10 KMPDUSER,18 xxx-xx55788.v08 99.99.9.120 437

Enter RETURN to continue or ‘^’ to exit: <span class="mark">\<Enter\></span>

Coversheet Time-to-Load Alert Report \> Real-Time

Hour(s): 0,1,2,3,4,5,6,7,8, Printed: 05/20/09

Any Occurrence:

Threshold: 60 seconds

Date Time User Name Client Name IP Address Time-to-Load

--------------------------------------------------------------------------------

05/20/09 04:19 KMPDUSER,19 xxx-xx47466.gai 99.99.99.82 113

04:22 KMPDUSER,23 S xxx-xx50606.gai 99.99.9.154 82

04:39 KMPDUSER,16 xxx-xx.v08. 99.99.99.17 68

04:56 KMPDUSER,19 xxx-xx55831.gai 99.99.99.86 75

05:19 KMPDUSER,16 xxx-xx.v08. 99.99.99.17 62

07:07 KMPDUSER,THREE xxx-xx57738.v08 99.99.99.16 98

07:18 KMPDUSER,20 xxx-xx51177.gai 99.99.999.33 64

07:43 KMPDUSER,21 xxx-xx57678.v08 99.99.9.55 72

07:59 KMPDUSER,22 xxx-xx50903.v08 99.99.99.13 96

08:01 KMPDUSER,24 xxx-xx55771.v08 99.99.9.157 108

Enter RETURN to continue or ‘^’ to exit: <span class="mark">\<Enter\></span>

<span id="_Toc439222296" class="anchor"></span>Figure . Real-Time Threshold Alert option—Report (2 of 3)

Coversheet Time-to-Load Alert Report \> Real-Time

Hour(s): 0,1,2,3,4,5,6,7,8, Printed: 05/20/09

Any Occurrence:

Threshold: 60 seconds

Date Time User Name Client Name IP Address Time-to-Load

--------------------------------------------------------------------------------

05/20/09 08:04 KMPDUSER,25 xxx-xx57600.v08 99.99.99.18 91

08:06 KMPDUSER,26 xxx-xx45092.v08 99.99.99.111 111

08:10 KMPDUSER,27 xxx-xx56195.v08 99.99.9.106 203

08:11 KMPDUSER,28 A xxx-xx45078.gai 99.99.9.153 73

08:14 KMPDUSER,27 xxx-xx56195.v08 99.99.9.106 82

08:15 KMPDUSER,29 xxx-xx45753.gai 99.99.9.93 156

08:16 KMPDUSER,30 L xxx-xx55831.gai 99.99.99.86 75

08:17 KMPDUSER,28 A xxx-xx45078.gai 99.99.9.153 61

08:18 KMPDUSER,31 xxx-xx57094.v08 99.99.99.91 70

08:19 KMPDUSER,FOUR xxx-xx57656.v08 99.99.9.17 95

08:20 KMPDUSER,32 xxx-xx59301.v08 99.99.9.234 66

08:20 KMPDUSER,24 xxx-xx55771.v08 99.99.9.157 63

08:21 KMPDUSER,33 M xxx-xx57893.v08 99.99.9.134 193

Enter RETURN to continue or ‘^’ to exit: <span class="mark">\<Enter\></span>

Coversheet Time-to-Load Alert Report \> Real-Time

Hour(s): 0,1,2,3,4,5,6,7,8, Printed: 05/20/09

Any Occurrence:

Threshold: 60 seconds

Date Time User Name Client Name IP Address Time-to-Load

--------------------------------------------------------------------------------

05/20/09 08:25 KMPDUSER,NINE xxx-xx57710.v08 99.99.9.229 69

08:26 KMPDUSER,34 N xxx-xx53033.gai 99.99.999.244 68

08:27 KMPDUSER,FIVE xxx-xx45760.gai 99.99.9.19 61

08:28 KMPDUSER,22 xxx-xx50903.v08 99.99.99.13 72

08:31 KMPDUSER,25 xxx-xx57600.v08 99.99.99.18 68

08:32 KMPDUSER,33 M xxx-xx57893.v08 99.99.9.134 273

08:33 KMPDUSER,35 xxx-xxrx.gaines 99.99.9.54 61

08:35 KMPDUSER,26 xxx-xx45092.v08 99.99.99.111 162

08:37 KMPDUSER,36 xxx-xx56665.v08 99.99.9.91 65

08:39 KMPDUSER,37 xxx-xx51734.gai 99.99.999.110 69

08:40 KMPDUSER,38 xxx-xx54233.gai 99.99.99.82 70

08:41 KMPDUSER,39 xxx-xx50701.gai 99.99.9.71 66

08:44 KMPDUSER,12 xxx-xx56231.v08 99.99.9.114 117

Enter RETURN to continue or ‘^’ to exit: <span class="mark">\<Enter\></span>

<span id="_Toc169674150" class="anchor"></span>Figure . Real-Time Threshold Alert option—Report (3 of 3)

Coversheet Time-to-Load Alert Report \> Real-Time

Hour(s): 0,1,2,3,4,5,6,7,8, Printed: 05/20/09

Any Occurrence:

Threshold: 60 seconds

Date Time User Name Client Name IP Address Time-to-Load

--------------------------------------------------------------------------------

05/20/09 08:45 KMPDUSER,40 xxx-xx57078.v08 99.99.9.129 106

08:47 KMPDUSER,41 L xxx-xx50888.gai 99.99.99.86 61

08:49 KMPDUSER,42 xxx-xx49015.gai 99.99.9.181 84

08:51 KMPDUSER,43 xxx-xx59924.v08 99.99.9.219 71

Total Count: 50

Press RETURN to continue:

This report provides the following data regarding threshold alert data at a site listing only those coversheet loads exceeding the threshold interval chosen by the user for the specified hours on the day the report was run (real-time):

- Date—Today’s date that the coversheet load began (real-time).
- Time—Specific time that the coversheet load began (hours and minutes, real time).
- User name—Name of the person signed on to the client workstation loading the coversheet (real-time).
- Client Workstation—Name of the client workstation that loaded the coversheet (real-time).
- IP Address—Internet Protocol (IP) address of the client workstation that loaded the coversheet (real-time).
- Time-To-Load—Total elapsed time to load the coversheet; loads that went beyond the threshold interval (real-time). Displayed metrics include the sum of Foreground and Background timings.
- Total—Grand total of report line items listed (real-time).

As with the Threshold Alert report option \[KMPD TMG TTL ALERT\], problems can be identified. However, because this is real-time report, sites can track what is going on throughout the day.

![](capacity-management-tools-version-3-user-manual/042.png) REF: For more information on the Threshold Alert report option \[KMPD TMG TTL ALERT\], see the “<u>Threshold Alert</u>” section.

For this report, the user chose to report on coversheet loads that exceeded 60 seconds between the hours of 00:00:00 a.m. and 8:59:59 a.m. on 05/20/09. The report shows that the longest coversheet load took 437 seconds at 4:10 a.m. KMPDUSER,18 signed onto the client workstation identified as “xxx-xx55788.v08” with an IP address of 99.99.9.120 and loaded that particular coversheet.

#### Real-Time Average Hourly Coversheet Load Option

The Real-Time Average Hourly Coversheet Load option \[KMPD TMG HRLY TTL RT; Synonym: RAV\] is located on the Timing Reports menu \[KMPD TMG REPORTS\]. It produces a report that displays the hourly average time-to-load (TTL) value for the coversheet at a site over a 24-hour period.

<u>Figure 51</u> shows the prompts and user responses for the Real-Time Average Hourly Coversheet Load option:

<span id="_Ref231287196" class="anchor"></span>Figure . Real-Time Average Hourly Coversheet Load option—User prompts

Select Timing Reports Option: <span class="mark">REAL-TIME AVERAGE HOURLY COVERSHEET LOAD</span>

Real-Time Hourly Coversheet Time-to-Load (TTL) Report

This report displays the hourly average time-to-load value for

the coversheet at this site over 24 hours.

Device: HOME// <span class="mark">\<Enter\></span> TELNET DEVICE

Compiling timing stats......

This is a real-time report option. Data is only available from midnight to 8:00 a.m.

<u>Figure 52</u> shows the actual report generated from the Real-Time Average Hourly Coversheet Load option:

<span id="_Ref231287213" class="anchor"></span>Figure . Real-Time Average Hourly Coversheet Load option—Report

Real-Time Hourly Coversheet Time-to-Load (TTL) Report

May 20, 2009 Printed: 05/20/09

\|---------------Seconds---------------\|

Date Hour TTL Average TTL Minimum TTL Maximum \# of CV Loads

--------------------------------------------------------------------------------

05/20/09 00 15 6 143 73

01 14 6 52 103

02 16 5 69 97

03 17 5 74 93

04 25 5 437 78

05 10 5 62 139

06 11 4 59 270

07 12 4 98 963

08 16 5 273 2,028

----------

3,844

Incomplete: 68

CV = Coversheet

TTL = Time-to-Load

Press RETURN to continue:

This report provides the following data regarding coversheet loads at a site for each hour of the specified number of days:

- Date—Today’s date that the coversheet load began (real-time).
- Hour—Specific hour that the coversheet load began (00 - 23, real-time).
- TTL Average—Average time-to-load (in seconds) for each hour of the day (real-time).
- TTL Minimum—Minimum time-to-load (in seconds) for each hour of the day (real-time).
- TTL Maximum—Maximum time-to-load (in seconds) for each hour of the day (real-time).
- \# of CV Loads—Total number of coversheet loads for:
- Each hour of the day.
- Grand total for the entire day.
- Incomplete—Total number of coversheets where the report option was unable to determine the coversheet end load time, so it was unable to calculate the time to load the coversheet.

![](capacity-management-tools-version-3-user-manual/043.png) NOTE: TTL metrics include the sum of Foreground and Background timings.

For this report, the user chose to report on the current day (05/20/09, midnight to 8:00 a.m.) of coversheet load data (real-time). The report shows that at 08:00 a.m. on 05/20/09, for example, there were a total of 2,028 coversheets loaded with an average time-to-load (TTL) for each coversheet of 16 seconds. At that same hour the report also shows that the shortest coversheet time-to-load (TTL) took only 5 seconds and the longest coversheet time-to-load (TTL) took 273 seconds (4 minutes and 55 seconds). Also, the report shows that there were a total of 68 coversheets that did *not* load to completion.

## CM Tools Background Driver Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On a nightly basis, the CM Tools Background Driver option \[KMPR BACKGROUND DRIVER\] does the following:

- Moves the data within the ^TMP(“KMPDH”,\$J) collection global to the CM HL7 DATA file (#8973.1).
- Moves the data within the ^KMPTMP(“KMPDT”) collection global to the CP TIMING file (#8973.2)

Upon completion, the data within both the ^TMP(“KMPDH”,\$J) and ^KMPTMP(“KMPDT”) temporary collection globals is purged.

Every Sunday night, the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] monitors and trims (records deleted) the following files to ensure that the correct maximum number of day’s data is maintained as determined by the appropriate CP parameters:

- CM HL7 DATA file (#8973.1)—The maximum amount of data collected is determined by the Purge HL7 Data After CP parameter.
- CP TIMING file (#8973.2)—The maximum amount of data collected is determined by the Purge Timing Data After CP parameter.

Also, each Sunday night, the CM Tools Background Driver option automatically compresses the information contained within the CM HL7 DATA file (#8973.1) into weekly statistics. These weekly statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes.

The CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] is *not* assigned to any menu. This option is scheduled through TaskMan to start the Capacity Management Tools software’s background driver routine.

This option should be (re)scheduled with TaskMan’s Schedule/Unschedule Options \[XUTM SCHEDULE\] located under the Taskman Management menu \[XUTM MGR\], see <span class="mark"></span><u>Figure 53</u>.

![](capacity-management-tools-version-3-user-manual/044.png) NOTE: The installation of the CM Tools software automatically sets the Background Driver job to run daily at 1:30 a.m. It does the same thing as TaskMan’s Schedule/Unschedule Option, which saves the installer the job of having to set up the Background Driver job later.

This option lets users set the following TaskMan parameters in the OPTION SCHEDULING file (#19.2, see <span class="mark"></span><u>Figure 54</u> and <span class="mark"></span><u>Figure 55</u>):

<table style="width:100%;">
<caption><p><span id="_Toc169674153" class="anchor"></span>Table . TaskMan parameters/fields, stored in the OPTION SCHEDULING file (#19.2)</p></caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>Parameter</th>
<th>Field Name (Number)<br />
(in File #19.2)</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>QUEUED TO RUN AT WHAT TIME</td>
<td>QUEUED TO RUN AT WHAT TIME field (#2)</td>
<td>This is the date and time the user wants this option to be started by TaskMan. It should be scheduled to run daily at 1:30 a.m.</td>
</tr>
<tr class="even">
<td>DEVICE FOR QUEUED JOB OUTPUT</td>
<td>DEVICE FOR QUEUED JOB OUTPUT field (#3)</td>
<td>The field is the name of the device on which the specified option is queued to print by TaskMan. At the time of queuing, If TaskMan <em>cannot</em> identify a device by this name the job does <em>not</em> run. Only enter a device if the job needs an output device.</td>
</tr>
<tr class="odd">
<td>QUEUED TO RUN ON VOLUME SET</td>
<td>QUEUED TO RUN ON VOLUME SET field (#5)</td>
<td>This field is used to let the Task Manager know where to run the queued job. It is the Volume set [:node] upon which the user wants the job to run. Answer <em>must</em> be 2-15 characters.</td>
</tr>
<tr class="even">
<td>RESCHEDULING FREQUENCY</td>
<td>RESCHEDULING FREQUENCY field (#6)</td>
<td>This is the frequency at which the user wants the job to automatically run. For the CM Tools Background Driver, this should be set to “1D” so that it runs daily. If this field is left blank, then the job runs only once.</td>
</tr>
</tbody>
</table>

<span id="_Toc169674153" class="anchor"></span>Table . TaskMan parameters/fields, stored in the OPTION SCHEDULING file (#19.2)

![](capacity-management-tools-version-3-user-manual/045.png) REF: For more information on TaskMan, see the *Kernel Systems Management Guide*.

![](capacity-management-tools-version-3-user-manual/046.png) CAUTION: Capacity Planning Service *strongly* recommends that the CM Tools Background Driver option \[KMPD BACKGROUND DRIVER\] be scheduled to run daily at 1:30 a.m., because this background driver is the main mechanism by which the following sub-globals are purged nightly:

- ^KMPD(8973.1)—CM HL7 DATA file (#8973.1): Records are purged as prescribed by the Purge HL7 Data After CP parameter, which is stored in the HL7 WEEKS TO KEEP DATA field (#3.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].
- ^KMPD(8973.2)—CP TIMING file (#8973.2): Records are purged as prescribed by the Purge Timing Data After CP parameter, which is stored in the TIMING WEEKS TO KEEP DATA field (#4.11) in the CP PARAMETERS file (#8973). This parameter is edited via the Edit CP Parameters File option \[KMPD PARAM EDIT\].

Modification of the frequency and time may have adverse effects on the size of the temporary ^KMPD(8973.1) and ^KMPD(8973.2) sub-globals and on the number of entries within the CM HL7 DATA file (#8973.1) and CP TIMING (#8973.2) files.

The following examples show typical displays when using TaskMan’s Schedule/Unschedule Options option:

<span id="_Ref44298006" class="anchor"></span>Figure . Running TaskMan’s Schedule/Unschedule Options option to set up the CM Tools Background Driver—User prompts

Select Systems Manager Menu Option: <span class="mark">TASKMAN MANAGEMENT</span>

Schedule/Unschedule Options

One-time Option Queue

Taskman Management Utilities ...

List Tasks

Dequeue Tasks

Requeue Tasks

Delete Tasks

Print Options that are Scheduled to run

Cleanup Task List

Print Options Recommended for Queueing

Select Taskman Management Option: <span class="mark">SCHEDULE/UNSCHEDULE OPTIONS</span>

Select OPTION to schedule or reschedule: <span class="mark">KMPD BACKGROUND DRIVER \<Enter\></span> CM Tools Background Driver

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

\(R\)

After selecting the specific option in TaskMan’s Schedule/Unschedule Options option, the user is automatically placed into the following ScreenMan form:

<span id="_Ref33497127" class="anchor"></span>Figure . Sample TaskMan’s Schedule/Unschedule Options option (ScreenMan)—User prompts, *before* scheduling the CM Tools Background Driver

Edit Option Schedule

Option Name: KMPD BACKGROUND DRIVER

Menu Text: CM Tools Background Driver TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref44297916" class="anchor"></span>Figure . Sample TaskMan’s Schedule/Unschedule Options option (ScreenMan) —User prompts, *after* scheduling the CM Tools Background Driver

Edit Option Schedule

Option Name: KMPD BACKGROUND DRIVER

Menu Text: CM Tools Background Driver TASK ID: 2156701

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: MAY 2,2009@01:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert <span id="_Toc423486600" class="anchor"></span>

Glossary

| Term              | Description                                                                                                                                                                                                |
|-------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CAPACITY PLANNING | The process of assessing a system’s capacity and evaluating its efficiency relative to workload in an attempt to optimize system performance. (Formerly known as Capacity Management.)                     |
| CM TOOLS          | Capacity Management Tools. A fully automated support tool developed by Capacity Planning (CP) Service, which entails the daily capture of VistA HL7 workload information from participating sites. |
| COVERSHEET        | The Computerized Patient Record System (CPRS) coversheet, which is the main CPRS page. This main page is a screen of the CPRS patient chart that displays an overview of the patient’s record.             |
| PRIME TIME HOURS  | Prime time hours are 8:00 a.m. to 5:00 p.m. (17:00) Monday through Friday, *excluding* holidays. Non-prime time hours are all other hours (i.e., weekends, nights and holidays).                           |

<span id="_Toc439222314" class="anchor"></span>Table 12. Capacity Management Tools glossary terms

![](capacity-management-tools-version-3-user-manual/047.png) REF: For a list of commonly used terms and definitions, see the OI&T Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

<span id="_Toc439222247" class="anchor"></span>Index

A

Acronyms

Intranet Website, 58

APIs

TIMING^KMPDTU11, 26

Assumptions, x

Average Daily Coversheet Load Option, 38

Average Hourly Coversheet Load Option, 40

C

Callout Boxes, ix

Capacity Planning

Mail Group Edit, 4

Menu, 3, 4, 7

National Database, 1, 2, 3, 31, 32, 54

Projections Website, 3

Statistics Website, 2, 3

CM HL7 DATA File (#8973.1), 2, 3, 10, 11, 25, 27, 54, 55

CM Tools

Functional Description, 2

Options, 4

Overview and Use of Software, 2

Software Management, 3

Software Overview and Use, 2

Startup/Stop Process, 24

CM Tools Background Driver

Field, 9

Option, 3, 9, 10, 21, 54

Rescheduling Frequency, 24

RESCHEDULING FREQUENCY Field (#6), 9, 25

CM Tools Background Driver Option, 2, 54

HL7 Daily Run Time, 10

HL7 Dly Bckgrnd Last Start Field, 10

HL7 Dly Bckgrnd Last Stop Field, 10

HL7 Dly Bkgrnd Total Time Field, 10

HL7 Last Daily Start, 10

HL7 Last Daily Stop, 10

HL7 Purge, 11

HL7 Purge Data After Field, 11

HL7 Transmit, 11

HL7 Transmit Data to Field, 11

HL7 Weekly Last Start, 10

HL7 Weekly Last Stop, 10

HL7 Weekly Run Time, 11

HL7 Wkly Backgrnd Last Start Field, 10

HL7 Wkly Bckgrnd Last Stop Field, 10

HL7 Wkly Bckgrnd Total Time Field, 11

Purge HL7 Data After Parameter, 3, 10, 25, 54, 55

Purge Timing Data After Parameter, 3, 10, 25, 54, 55

QUEUED BY Field, 9

QUEUED TO RUN AT WHAT TIME Field (#2), 9

RESCHEDULING FREQUENCY Field (#6), 9, 55

RUM Dly Bckgrnd Last Start Field, 15

Scheduling, 9

Scheduling Frequency, 10, 25, 55

TASK ID Field, 9

Timing Daily Run Time, 22

TIMING Dly Bckgrnd Last Stop Field, 22

Timing Last Daily Start, 21

Timing Last Daily Stop, 22

Timing Purge, 22

Timing Transmit, 22

TMG Collection Status Field, 21

TMG Dly Bckgrnd Last Start Field, 21

TMG Dly Bkgrnd Total Time Field, 22

TMG Purge Data After Field, 22

TMG Transmit Data to Field, 22

Collection Global

KMPTMP(”KMPR”), 14

Collection Globals

KMPTMP(”KMPDT”), 2, 54

TMP(”KMPDH”,\$J), 2, 54

Contents, iii

Conventions

Documentation, viii

Coversheets

CPRS Coversheet Load Times, 33, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 52, 53

CP Echo Server Option, 31

CP Environment Check Option, 7, 9, 24

HL7, 8, 10

RUM, 13, 14, 15

SAGG, 18, 19

Timing, 21

CP PARAMETERS File (#8973), 10, 25, 27, 29, 31, 33, 35, 36, 55

CP TIMING File (#8973.2), 2, 3, 10, 22, 25, 27, 37, 54, 55

CP Tools Manager Menu, 3, 7, 24, 27, 33, 37

CP Tools Reports Menu, 37

CPE

Website, xi

CPRS

Coversheet Load Times, 33, 37, 38, 39, 40, 42, 43, 44, 45, 46, 47, 48, 49, 52, 53

Patch OR\*3.0\*209, 24

Timing Data, 24

D

Data

HL7, 8

RUM, 13

SAGG, 18

Timing, 21

Data Collection Process, 2

Data Dictionary

Data Dictionary Utilities Menu, x

Listings, x

Data Purges, 30

Databases

Capacity Planning National Database, 1, 2, 3, 31, 32, 54

Detailed Daily Coversheet Load Option, 43

Detailed Hourly Coversheet Load Option, 39, 45

DEVICE FOR QUEUED JOB OUTPUT Field (#3), 55

Disclaimers

Documentation, vii

Software, vii

Documentation

Conventions, viii

Revisions, ii

Symbols, viii

Documentation Disclaimer, vii

Documentation Navigation, ix

E

Edit CP Parameters File Option, 27

Eve Menu, 3, 4

F

Fields

CM Tools Background Driver, 9

DEVICE FOR QUEUED JOB OUTPUT (#3), 55

HL7 Dly Bckgrnd Last Start, 10

HL7 Dly Bckgrnd Last Stop, 10

HL7 Dly Bkgrnd Total Time, 10

HL7 Purge Data After, 11

HL7 Transmit Data to, 11

HL7 WEEKS TO KEEP DATA (#3.11), 10, 25, 27, 55

HL7 Wkly Backgrnd Last Start, 10

HL7 Wkly Bckgrnd Last Stop, 10

HL7 Wkly Bckgrnd Total Time, 11

MONITOR ALERT - SECONDS (#19.02), 27, 33, 35, 36

MONITOR UPDATE RATE - MINUTES (#19.01), 28, 33

QUEUED BY, 9, 14, 19

QUEUED TO RUN AT WHAT TIME (#2), 9, 13, 18, 55

QUEUED TO RUN ON VOLUME SET (#5), 55

REASON FOR DOWN TIME (#5.03), 28

RESCHEDULING FREQUENCY (#6), 9, 14, 18, 55

RUM Background Driver, 13

RUM Dly Bckgrnd Last Start, 15

RUM Dly Bckgrnd Last Stop, 15

RUM Dly Bkgrnd Total Time, 15

RUM Purge Data After, 15

RUM Transmit Data to, 15

RUM WEEKS TO KEEP DATA (#2.11), 27

RUM Wkly Backgrnd Last Start, 15

RUM Wkly Bckgrnd Last Stop, 15

RUM Wkly Bckgrnd Total Time, 15

SAGG Master Background Task, 18

Status, 18

SCHEDULED DOWN TIME START (#5.01), 28, 31

SCHEDULED DOWN TIME STOP (#5.02), 28, 31

TASK ID, 9, 14, 18

TIMING Dly Bckgrnd Last Stop, 22

TIMING WEEKS TO KEEP DATA (#4.11), 10, 25, 27, 55

TMG Collection Status, 21

TMG Dly Bckgrnd Last Start, 21

TMG Dly Bkgrnd Total Time, 22

TMG Purge Data After, 22

TMG Transmit Data to, 22

Figures, iv

Files

CM HL7 DATA (#8973.1), 2, 3, 10, 11, 25, 27, 54, 55

CP PARAMETERS (#8973), 10, 25, 27, 29, 31, 33, 35, 36, 55

CP TIMING (#8973.2), 2, 3, 10, 22, 25, 27, 37, 54, 55

OPTION SCHEDULING (#19.2), 55

RESOURCE USAGE MONITOR (#8971.1), 14, 15, 27

SAGG PROJECT (#8970.1), 19

Functional Description, 2

G

Globals

KMPD(8973.1) Sub-global, 10, 25, 55

KMPD(8973.2) Sub-global, 10, 25, 55

KMPTMP(”KMPDT”) Collection Global, 2, 54

KMPTMP(”KMPR”) Collection Global, 14

TMP(”KMPDH”,\$J) Collection Global, 2, 54

Glossary, 58

Intranet Website, 58

H

Help

At Prompts, x

Online, x

Question Marks, x

History

Revisions, ii

HL7

Data, 8

HL7 Dly Bckgrnd Last Start Field, 10

HL7 Dly Bckgrnd Last Stop Field, 10

HL7 Dly Bkgrnd Total Time Field, 10

HL7 Monitor, 8

HL7 Purge Data After Field, 11

HL7 Transmit Data to Field, 11

HL7 WEEKS TO KEEP DATA Field (#3.11), 10, 25, 27, 55

HL7 Wkly Backgrnd Last Start Field, 10

HL7 Wkly Bckgrnd Last Stop Field, 10

HL7 Wkly Bckgrnd Total Time Field, 11

Home Pages

Acronyms Intranet Website, 58

Adobe Website, xi

Capacity Planning

Projections Website, 3

Statistics Website, 2, 3

CPE Website, xi

Glossary Intranet Website, 58

RUM Documentation Website, 14

VA Software Document Library (VDL), xi

How to

Obtain Technical Information Online, x

Use this Manual, vii

I

Intended Audience, vii

Introduction, 1

K

KMP MAIL GROUP EDIT, 4

KMP-CAPMAN Mail Group, 4, 11, 16, 19, 22

KMPD BACKGROUND DRIVER Option, 2, 3, 9, 10, 21, 54

HL7 Daily Run Time, 10

HL7 Last Daily Start, 10

HL7 Last Daily Stop, 10

HL7 Purge, 11

HL7 Transmit, 11

HL7 Weekly Last Start, 10

HL7 Weekly Last Stop, 10

HL7 Weekly Run Time, 11

RESCHEDULING FREQUENCY Field (#6), 9, 24, 25

Scheduling, 9

Timing Daily Run Time, 22

Timing Last Daily Start, 21

Timing Last Daily Stop, 22

Timing Purge, 22

Timing Transmit, 22

KMPD CM TOOLS MANAGER MENU, 3, 7, 24, 27, 33, 37

KMPD CM TOOLS REPORTS Menu, 37

KMPD ECHO Server Option, 31

KMPD PARAM EDIT Option, 27

KMPD STATUS Option, 7, 9, 24

HL7, 8, 10

RUM, 13, 14, 15

SAGG, 18, 19

Timing, 21

KMPD TMG AVG TTL Option, 38

KMPD TMG DLY TTL DETAIL Option, 43

KMPD TMG HRLY TTL DETAIL Option, 39, 45

KMPD TMG HRLY TTL Option, 40

KMPD TMG HRLY TTL RT Option, 52

KMPD TMG MONITOR Option, 33

KMPD TMG REPORTS Menu, 37, 38, 40, 43, 45, 47, 49, 52

KMPD TMG START/STOP Option, 24

KMPD TMG TTL ALERT Option, 39, 47, 52

KMPD TMG TTL ALERT RT Option, 49

KMPD(8973.1) Sub-global, 10, 25, 55

KMPD(8973.2) Sub-global, 10, 25, 55

KMPDTU11

TIMING^KMPDTU11 API, 26

KMPR BACKGROUND DRIVER Option, 13, 14, 15

RESCHEDULING FREQUENCY Field (#6), 14

RUM Daily Run Time, 15

RUM Last Daily Start, 15

RUM Last Daily Stop, 15

RUM Purge, 15

RUM Transmit, 15

RUM Weekly Last Start, 15

RUM Weekly Last Stop, 15

RUM Weekly Run Time, 15

KMPS SAGG REPORT Option, 18, 19

KMPTMP(”KMPDT”) Collection Global, 2, 54

KMPTMP(”KMPR”) Collection Global, 14

L

List File Attributes Option, x

M

Mail Groups

KMP-CAPMAN, 4, 11, 16, 19, 22

Management of the CM Tools Software, 3

Menus

Capacity Planning, 3, 4, 7

CP Tools Manager Menu, 3, 7, 24, 27, 33, 37

CP Tools Reports, 37

Data Dictionary Utilities, x

Eve, 3, 4

KMPD CM TOOLS MANAGER MENU, 3, 7, 24, 27, 33, 37

KMPD CM TOOLS REPORTS, 37

KMPD TMG REPORTS, 37, 38, 40, 43, 45, 47, 49, 52

Operations Management, 4

Systems Manager Menu, 4

Taskman Management, 9, 14, 19, 25, 54

Timing Reports, 37, 38, 40, 43, 45, 47, 49, 52

XTCM MAIN, 3, 4, 7

XUSITEMGR, 4

XUTM MGR, 9, 14, 19, 25, 54

MONITOR ALERT - SECONDS Field (#19.02), 27, 33, 35, 36

MONITOR UPDATE RATE - MINUTES Field (#19.01), 28, 33

Monitors

HL7, 8

RUM, 13

SAGG, 18

Timing, 21, 30

VistA, 31

N

National Database

Capacity Planning, 1, 2, 3, 31, 32, 54

O

Obtaining

Data Dictionary Listings, x

Online

Documentation, x

Technical Information, How to Obtain, x

Operations Management Menu, 4

OPTION SCHEDULING File (#19.2), 55

Options

Average Daily Coversheet Load, 38

Average Hourly Coversheet Load, 40

Capacity Planning, 4, 7

Capacity Planning Mail Group Edit, 4

Capacity Planning Menu, 3

CM Tools, 4

CM Tools Background Driver, 2, 3, 9, 10, 21, 54

HL7 Daily Run Time, 10

HL7 Last Daily Start, 10

HL7 Last Daily Stop, 10

HL7 Purge, 11

HL7 Transmit, 11

HL7 Weekly Last Start, 10

HL7 Weekly Last Stop, 10

HL7 Weekly Run Time, 11

RESCHEDULING FREQUENCY Field (#6), 9, 24, 25

Scheduling, 9

Timing Daily Run Time, 22

Timing Last Daily Start, 21

Timing Last Daily Stop, 22

Timing Purge, 22

Timing Transmit, 22

CP Environment Check, 7, 9, 10, 24

HL7, 8

RUM, 13, 14, 15

SAGG, 18, 19

Timing, 21

CP Tools Manager Menu, 3, 7, 24, 27, 33, 37

CP Tools Reports, 37

Data Dictionary Utilities, x

Detailed Daily Coversheet Load, 43

Detailed Hourly Coversheet Load, 39, 45

Edit CP Parameters File, 27

Eve Menu, 3, 4

KMP MAIL GROUP EDIT, 4

KMPD BACKGROUND DRIVER, 2, 3, 9, 10, 21, 54

HL7 Daily Run Time, 10

HL7 Last Daily Start, 10

HL7 Last Daily Stop, 10

HL7 Purge, 11

HL7 Transmit, 11

HL7 Weekly Last Start, 10

HL7 Weekly Last Stop, 10

HL7 Weekly Run Time, 11

RESCHEDULING FREQUENCY Field (#6), 9, 24, 25

Scheduling, 9

Timing Daily Run Time, 22

Timing Last Daily Start, 21

Timing Last Daily Stop, 22

Timing Purge, 22

Timing Transmit, 22

KMPD CM TOOLS MANAGER MENU, 3, 7, 24, 27, 33, 37

KMPD CM TOOLS REPORTS, 37

KMPD PARAM EDIT, 27

KMPD STATUS, 7, 9, 24

HL7, 8, 10

RUM, 13, 14, 15

SAGG, 18, 19

Timing, 21

KMPD TMG AVG TTL, 38

KMPD TMG DLY TTL DETAIL, 43

KMPD TMG HRLY TTL, 40

KMPD TMG HRLY TTL DETAIL, 39, 45

KMPD TMG HRLY TTL RT, 52

KMPD TMG MONITOR, 33

KMPD TMG REPORTS, 37, 38, 40, 43, 45, 47, 49, 52

KMPD TMG START/STOP, 24

KMPD TMG TTL ALERT, 39, 47, 52

KMPD TMG TTL ALERT RT, 49

KMPR BACKGROUND DRIVER, 13, 14, 15

RESCHEDULING FREQUENCY Field (#6), 14

RUM Daily Run Time, 15

RUM Last Daily Start, 15

RUM Last Daily Stop, 15

RUM Purge, 15

RUM Transmit, 15

RUM Weekly Last Start, 15

RUM Weekly Last Stop, 15

RUM Weekly Run Time, 15

KMPS SAGG REPORT, 18, 19

List File Attributes, x

Operations Management, 4

Real-Time Average Hourly Coversheet Load, 52

Real-Time Threshold Alert, 49

RUM Background Driver, 13, 14, 15

RESCHEDULING FREQUENCY Field (#6), 14

RUM Daily Run Time, 15

RUM Last Daily Start, 15

RUM Last Daily Stop, 15

RUM Purge, 15

RUM Transmit, 15

RUM Weekly Last Start, 15

RUM Weekly Last Stop, 15

RUM Weekly Run Time, 15

SAGG Master Background Task, 18, 19

Schedule/Unschedule Options, 9, 14, 19, 25, 54

Server

CP Echo Server, 31

KMPD ECHO, 31

Start/Stop Timing Collection, 24

Systems Manager Menu, 4

Taskman Management, 9, 14, 19, 25, 54

Threshold Alert, 39, 47, 52

Timing Monitor, 33

Timing Reports, 37, 38, 40, 43, 45, 47, 49, 52

XTCM MAIN, 3, 4, 7

XUSITEMGR, 4

XUTM MGR, 9, 14, 19, 25, 54

XUTM SCHEDULE, 9, 14, 19, 25, 54

OR\*3.0\*209, 24

Orientation, vii

Overview

CM Tools Software, 2

P

Parameters

DEVICE FOR QUEUED JOB OUTPUT, 55

Purge HL7 Data After, 3, 10, 25, 54, 55

PURGE HL7 DATA AFTER, 27

Purge RUM Data After, 27

Purge Timing Data After, 3, 10, 25, 27, 54, 55

QUEUED TO RUN AT WHAT TIME, 55

QUEUED TO RUN ON VOLUME SET, 55

Reason for Down Time, 28

RESCHEDULING FREQUENCY, 55

Scheduled Down Time Start, 28

Scheduled Down Time Stop, 28

Timing Monitor Alert - Seconds, 27

Timing Monitor Update Rate - Min, 28

Patches

OR\*3.0\*209, 24

Revisions, ii

Projections and Statistics, 3

PS Anonymous Directories, xi

Purge HL7 Data After Parameter, 3, 10, 25, 27, 54, 55

Purge RUM Data After Parameter, 27

Purge Timing Data After Parameter, 3, 10, 25, 27, 54, 55

Purging

Data, 30

Q

Question Mark Help, x

QUEUED BY Field, 9, 14, 19

QUEUED TO RUN AT WHAT TIME Field (#2), 9, 13, 18, 55

QUEUED TO RUN ON VOLUME SET Field (#5), 55

R

Real-Time Average Hourly Coversheet Load Option, 52

Real-Time Threshold Alert Option, 49

REASON FOR DOWN TIME Field (#5.03), 28

Reason for Down Time Parameter, 28

Reference Materials, xi

Reference Type, Supported

TIMING^KMPDTU11, 26

RESCHEDULING FREQUENCY Field (#6), 9, 14, 18, 55

RESOURCE USAGE MONITOR File (#8971.1), 14, 15, 27

Revision History, ii

Documentation, ii

Patches, ii

RUM

Data, 13

RUM Background Driver

Field, 13

Option, 13, 14, 15

QUEUED BY Field, 14

QUEUED TO RUN AT WHAT TIME Field (#2), 13

RESCHEDULING FREQUENCY Field (#6), 14

TASK ID Field, 14

RUM Background Driver Option

RESCHEDULING FREQUENCY Field (#6), 14

RUM Daily Run Time, 15

RUM Dly Bckgrnd Last Stop Field, 15

RUM Dly Bkgrnd Total Time Field, 15

RUM Last Daily Start, 15

RUM Last Daily Stop, 15

RUM Purge, 15

RUM Purge Data After Field, 15

RUM Transmit, 15

RUM Transmit Data to Field, 15

RUM Weekly Last Start, 15

RUM Weekly Last Stop, 15

RUM Weekly Run Time, 15

RUM Wkly Backgrnd Last Start Field, 15

RUM Wkly Bckgrnd Last Stop Field, 15

RUM Wkly Bckgrnd Total Time Field, 15

RUM Dly Bckgrnd Last Start Field, 15

RUM Dly Bckgrnd Last Stop Field, 15

RUM Dly Bkgrnd Total Time Field, 15

RUM Documentation

Website, 14

RUM Monitor, 13

RUM Purge Data After Field, 15

RUM Transmit Data to Field, 15

RUM WEEKS TO KEEP DATA Field (#2.11), 27

RUM Wkly Backgrnd Last Start Field, 15

RUM Wkly Bckgrnd Last Stop Field, 15

RUM Wkly Bckgrnd Total Time Field, 15

S

SAGG

Data, 18

SAGG Master Background Task Field, 18

Status, 18

SAGG Master Background Task Option, 18, 19

QUEUED BY Field, 19

QUEUED TO RUN AT WHAT TIME Field (#2), 18

RESCHEDULING FREQUENCY Field (#6), 18

TASK ID Field, 18

SAGG Monitor, 18

SAGG PROJECT File (#8970.1), 19

Schedule/Unschedule Options Option, 9, 14, 19, 25, 54

SCHEDULED DOWN TIME START Field (#5.01), 28, 31

Scheduled Down Time Start Parameter, 28

SCHEDULED DOWN TIME STOP Field (#5.02), 28, 31

Scheduled Down Time Stop Parameter, 28

Server Options

CP Echo Server, 31

KMPD ECHO, 31

Software

Management, 3

Overview and Use, 2

Software Disclaimer, vii

Start/Stop Gathering CM Tools Timing Data

TIMING^KMPDTU11, 26

Start/Stop Timing Collection Option, 24

Startup/Stop Process

CM Tools, 24

Statistics and Projections, 3

Symbols

Found in the Documentation, viii

Systems Manager Menu, 4

T

Tables, vi

TASK ID Field, 9, 14, 18

Taskman Management Menu, 9, 14, 19, 25, 54

Threshold Alert Option, 39, 47, 52

Time-To-Load Values, 38, 40, 43, 45, 47, 49, 52

Timing

Data, 21

TIMING Dly Bckgrnd Last Stop Field, 22

Timing Monitor, 21, 30

Timing Monitor Alert – Seconds Parameter, 27

Timing Monitor Option, 33

Timing Monitor Update Rate – Min Parameter, 28

Timing Reports Menu, 37, 38, 40, 43, 45, 47, 49, 52

TIMING WEEKS TO KEEP DATA Field (#4.11), 10, 25, 27, 55

TIMING^KMPDTU11 API, 26

TMG Collection Status Field, 21

TMG Dly Bckgrnd Last Start Field, 21

TMG Dly Bkgrnd Total Time Field, 22

TMG Purge Data After Field, 22

TMG Transmit Data to Field, 22

TMP(”KMPDH”,\$J) Collection Global, 2, 54

U

URLs

Acronyms Intranet Website, 58

Adobe Website, xi

CPE Website, xi

Glossary Intranet Website, 58

VA Software Document Library (VDL), xi

Use of the CM Tools Software, 2

V

VA Software Document Library (VDL)

Website, xi

Vista Monitor, 31

W

Web Pages

Capacity Planning

Projections Website, 3

Statistics Website, 2, 3

RUM Documentation Website, 14

Websites

Acronyms Intranet Website, 58

Adobe Website, xi

CPE, xi

Glossary Intranet Website, 58

VA Software Document Library (VDL), xi

X

XTCM MAIN Menu, 3, 4, 7

XUSITEMGR Menu, 4

XUTM MGR Menu, 9, 14, 19, 25, 54

XUTM SCHEDULE Option, 9, 14, 19, 25, 54