---
title: XU*8*671 Assigning Person Class to Providers User Guide
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Assigning Person Class to Providers
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*671
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - class
  - active
  - providers
  - even
  - physicians
  - allopathic
  - osteopathic
  - service
  - person
  - span
page_count: 0
word_count: 41564
section_count: 19
table_count: 4
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: December 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_8_0p671sp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/xu_8_0p671sp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0

  Assigning Person Class to Providers User Guide

  Patch Supplement: XU\*8.0\*27, 377, 531, and 671
---

![](xu-8-671-assigning-person-class-to-providers-user-guide/001.png)

December 2017

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

<span id="_Toc501609565" class="anchor"></span>Revision History

<table>
<caption><blockquote>
<p><span id="_Ref488739455" class="anchor"></span>Table 1: Documentation Symbol Descriptions</p>
</blockquote></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 41%" />
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
<td>12/21/2017</td>
<td>4.4</td>
<td><p>VA tech writer review:</p>
<ul>
<li><p>Correct Section 508 issues on existing content unrelated to Kernel Patch XU*8*671.</p></li>
<li><p>Verify all organization references, and adherence to current documentation standards, styles, and formatting.</p></li>
</ul></td>
<td>VA Technical Writer: REDACTED</td>
</tr>
<tr class="even">
<td>10/26/2017</td>
<td>4.3</td>
<td>Tech writer review and Section 508 compliance check of the added sections.</td>
<td>Technical Writer: REDACTED (ManTech Mission Solutions &amp; Services Group)</td>
</tr>
<tr class="odd">
<td>07/25/2017</td>
<td>4.2</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Revised Title page and footer dates.</p></li>
<li><p>Document is no longer structured for double-sided printing: removed Odd and Even section breaks and section headers.</p></li>
<li><p>Reformatted document to follow current documentation styles and style guidelines.</p></li>
<li><p>Updated organizational references throughout.</p></li>
<li><p>Updated the “<a href="#_Toc482517694">Orientation</a>” section. Includes replacing the “Legal Requirement” section with the “<a href="#Disclaimers">Disclaimers</a>” section.</p></li>
</ul></td>
<td>VA Technical Writer: REDACTED</td>
</tr>
<tr class="even">
<td>07/20/2017</td>
<td>4.1</td>
<td><p>Technical Updates:</p>
<ul>
<li><p>Updated Overview to include <a href="#XU_80_671">XU*8.0*671</a> patch and continued <a href="#Note">maintenance note</a>.</p></li>
<li><p>Added <a href="#patch-xu8.0671">Section 4.2.3</a> with active terms in XU*8.0*671.</p></li>
<li><p>Added <a href="#patch-xu8.0671-1">Section 4.4.3</a> with inactivated terms in XU*8.0*671.</p></li>
</ul></td>
<td><p>Developers: REDACTED (ManTech Mission Solutions &amp; Services Group)</p>
<p>Technical Writer: REDACTED (ManTech Mission Solutions &amp; Services Group)</p></td>
</tr>
<tr class="odd">
<td>02/10/2014</td>
<td>4.0</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Reformatted document to follow current template and style guide.</p></li>
<li><p>Updated/Merged procedural steps in the "<u>Enter/Edit Person Class Data</u>" section.</p></li>
<li><p>Added the "<u>Identify Providers with Inactive Person Class Entries</u>" section.</p></li>
<li><p>Added the "<u>Special Handling—Correcting Person Class Data</u>" section.</p></li>
<li><p>Added tables for Kernel Patch XU*8.0*531 in "<u>Appendix A—Person Class Codes: New, Updated, Inactivated, and Reactivated</u>."</p></li>
<li><p>Added new "<u>Appendix B—Printing VA Person Class Data</u>."</p></li>
<li><p>Added references to Kernel Patch XU*8.0*531 throughout.</p></li>
<li><p>Added references to other Taxonomy Code websites throughout.</p></li>
<li><p>Deleted the "Developer's Guide" section from this document, since that same information is included in the <em>Kernel Developer's Guide</em>.</p></li>
<li><p>Deleted the "Systems Management Guide", "Implementation and Maintenance," and "Software Product Security" sections from this document, since that information is included in the <em>Kernel Technical Manual</em>.</p></li>
</ul></td>
<td><p>Enterprise System Engineering (ESE): REDACTED</p>
<p>Developer: REDACTED</p>
<p>VA Technical Writer: REDACTED</p></td>
</tr>
<tr class="even">
<td>05/31/2006</td>
<td>3.1</td>
<td><p>Assigning Person Class to Providers Patch Supplement renamed and updated based on Kernel Patch XU*8.0*377 and feedback from developer, Ba Tran.</p>
<p>This version also includes content updates as per E. F.</p>
<p>![](xu-8-671-assigning-person-class-to-providers-user-guide/002.png) <strong>NOTE:</strong> The original Person Class Kernel Patch was XU*8.0*27 released on 08/14/1996.</p></td>
<td><p>Maintenance Development Team, Oakland, CA OIFO:</p>
<ul>
<li><p>Project Manager: REDACTED</p></li>
<li><p>Developer: REDACTED</p></li>
<li><p>SQA: REDACTED</p></li>
<li><p>Technical Writer: REDACTED</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>01/27/2005</td>
<td>2.0</td>
<td><p>Reformatted document to follow ISS Style Guide.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p></li>
<li><p>Patient or user names are formatted as follows: KRNPATIENT,[N] or KRNUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KRNPATIENT, ONE, KRNPATIENT, TWO, etc.).</p></li>
<li><p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>VA Technical Writer: REDACTED</td>
</tr>
<tr class="even">
<td>08/1996</td>
<td>1.0</td>
<td>Initial Assigning Person Class to Providers Patch Supplement (i.e., Kernel Patch XU*8.0*27) documentation creation.</td>
<td>Kernel Development Team, San Francisco, CA OIFO</td>
</tr>
</tbody>
</table>

<span id="_Ref488739455" class="anchor"></span>Table 1: Documentation Symbol Descriptions

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc501609566" class="anchor"></span>List of Figures

[Figure 14: Printing Person Class File Entries—Sorted by Provider Type: Sample User  
Dialogue [178](#_Ref378843260)](#_Ref378843260)

<span id="_Toc501609567" class="anchor"></span>List of Tables

<span id="_Toc482517694" class="anchor"></span>

Orientation

How to Use this Manual

Throughout this *Assigning Person Class to Providers User Guide* (i.e., Patch Supplement for Kernel Patches XU\*8.0\*27, 377, 531, and 671), advice and instructions are offered regarding the use of the Assigning Person Class to Providers and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA).

![](xu-8-671-assigning-person-class-to-providers-user-guide/003.png) REF: Consult the Kernel documents for the following information related to the Assigning Person Class to Providers software (i.e., Kernel Patches XU\*8.0\*27, 377, 531, and 671):

- *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*—Implementation and maintenance for Assigning Person Class to Providers (e.g., routines, files, options, interfaces, software product security)
- *Kernel 8.0 and Kernel Toolkit 7.3 Developer's Guide*—Application Program Interfaces (APIs).

All Kernel documentation is available on the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/application.asp?appid=10>

Intended Audience

The intended audience of this manual is the following stakeholders:

- Users responsible for assigning person class to providers.
- Enterprise Program Management Office (EPMO)—VistA legacy development teams.
- System Administrators—System administrators at Department of Veterans Affairs (VA) sites who are responsible for computer management and system security on the VistA M Servers.
- Product Support (PS)—Personnel who support Kernel-related products.

<span id="Disclaimers" class="anchor"></span>Disclaimers

Software Disclaimer

This software was developed at the Department of Veterans Affairs (VA) by employees of the Federal Government in the course of their official duties. Pursuant to title 17 Section 105 of the United States Code this software is *not* subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We would appreciate acknowledgement if the software is used. This software can be redistributed freely provided that any derivative works bear some notice that they are derived from it.

![](xu-8-671-assigning-person-class-to-providers-user-guide/004.png) CAUTION: Kernel routines should *never* be modified at the site. If there is an immediate national requirement, the changes should be made by emergency Kernel patch. Kernel software is subject to FDA regulations requiring Blood Bank Review, among other limitations. Line 3 of all Kernel routines states:  
  
Per VHA Directive 2004-038, this routine should not be modified.

Documentation Disclaimers

This manual provides an overall explanation of the use, maintenance, and implementation of the Assigning Person Class to Providers software (Kernel Patches XU\*8.0\*27, 377, 531, and 671); however, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the Internet and VA Intranet for a general orientation to VistA. For example, go to the Office of Information and Technology (OIT) VistA Development Intranet Website.

The appearance of external hyperlink references in this manual does not constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

Documentation Conventions

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. <u>Table 1</u> gives a description of each of these symbols:

| Symbol                                                                                                            | Description                                                                                                           |
|-------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![](xu-8-671-assigning-person-class-to-providers-user-guide/005.png)      | NOTE / REF: Used to inform the reader of general information including references to additional reading material. |
| ![](xu-8-671-assigning-person-class-to-providers-user-guide/006.png) | CAUTION / RECOMMENDATION / DISCLAIMER: Used to caution the reader to take special notice of critical information. |

<span id="_Ref488674633" class="anchor"></span>Table 2: New Person Class Codes—Kernel Patch XU\*8.0\*377

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
- The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
- Patient and user names are formatted as follows:
- *\<Application Name/Abbreviation/Namespace\>*PATIENT,*\<N\>*
- *\<Application Name/Abbreviation/Namespace\>*USER,*\<N\>*

Where:

- *\<Application Name/Abbreviation/Namespace\>* is defined in the Approved Application Abbreviations document.
- *\<N\>* represents the first name as a number spelled out and incremented with each new entry.

For example, in Kernel (XU or KRN) test patient and user names would be documented as follows:

KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; … KRNPATIENT,14; etc.

KRNUSER,ONE; KRNUSER,TWO; KRNUSER,THREE; … KRNUSER,14; etc.

- "Snapshots" of computer commands and online displays (i.e., screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and may be enclosed within a box.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., roll-and-scroll screen or character-based screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be bold typeface and highlighted in yellow (e.g., <span class="mark">\<Enter\></span>).
- Emphasis within a dialogue box will be bold typeface and highlighted in blue (e.g.,<span class="mark"> STANDARD LISTENER: RUNNING</span>).
- Some software code reserved/key words will be bold typeface with alternate color font.
- References to "\<Enter\>" within these snapshots indicate that the user should press the \<Enter\> key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments are displayed in italics or as "callout" boxes.

![](xu-8-671-assigning-person-class-to-providers-user-guide/007.png) NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image.

- This manual refers to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M "\>" prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

\><span class="mark">D ^XUP</span>

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE security key).

Documentation Navigation

This document uses Microsoft<sup>®</sup> Word's built-in navigation for internal hyperlinks. To add Back and Forward navigation buttons to your toolbar, do the following:

1.  Right-click anywhere on the customizable Toolbar in Word 2007 (not the Ribbon section).
1.  Select Customize Quick Access Toolbar from the secondary menu.
2.  Select the drop-down arrow in the "Choose commands from:" box.
3.  Select All Commands from the displayed list.
4.  Scroll through the command list in the left column until you see the Back command (circle with arrow pointing left).
5.  Select/Highlight the Back command and select Add to add it to your customized toolbar.
6.  Scroll through the command list in the left column until you see the Forward command (circle with arrow pointing right).
7.  Select/Highlight the Forward command and select Add to add it to your customized toolbar.
8.  Select OK.

You can now use these Back and Forward command buttons in your Toolbar to navigate back and forth in your Word document when clicking on hyperlinks within the document.

![](xu-8-671-assigning-person-class-to-providers-user-guide/008.png) NOTE: This is a one-time setup and is automatically available in any other Word document once you install it on the Toolbar.

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

![](xu-8-671-assigning-person-class-to-providers-user-guide/009.png) NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate section.  
  
REF: For further information, see the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

![](xu-8-671-assigning-person-class-to-providers-user-guide/010.png) REF: For details about obtaining data dictionaries and about the formats available, see the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*.

Assumptions

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
  - Kernel—VistA M Server software
  - VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

Reference Materials

Readers who wish to learn more about Kernel should consult the following:

- *Assigning Person Class to Providers, Supplement to Patch Description (Kernel Patches XU\*8.0\*27, 377, 531, and 671)* (this manual)
- *Kernel Release Notes*
- *Kernel Installation Guide*
- *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*
- *Kernel 8.0 and Kernel Toolkit 7.3 Developer's Guide*
- *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*
- *Kernel Security Tools Manual*
- Kernel VA Intranet Website

This site contains other information and provides links to additional documentation.

- The Health Information Management team maintains the PERSON CLASS (#8932.1) file and updates to related documents, such as the Department of Veterans Affairs' (VA) version of the Person Class Taxonomy Codes.
- [VHA DIRECTIVE 2012-003; January 12, 2012: Person Class File Taxonomy](http://www.va.gov/vhapublications/ViewPublication.asp?pub_ID=2477): <http://www.va.gov/vhapublications/ViewPublication.asp?pub_ID=2477>  
    
  (Document/link maintained on the VHA Forms, Publications and Record Management website.)
- Washington Publishing Company (WPC) Code Lists and X12 Registry (reference website): <http://www.wpc-edi.com/reference/>

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader, which is freely distributed by Adobe Systems Incorporated at the following Website: <http://www.adobe.com/>

VistA documentation can be downloaded from the VA Software Document Library (VDL) Website: <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Product Support (PS) Anonymous directories.

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [HCFA Provider Codes](#hcfa-provider-codes)
  - [Interfaces](#interfaces)
- [Enter/Edit Person Class Data](#enteredit-person-class-data)
  - [Identify All Active Providers](#identify-all-active-providers)
    - [Overview](#overview-1)
    - [Procedure](#procedure)
  - [Identify Providers with Inactive Person Class Entries](#identify-providers-with-inactive-person-class-entries)
    - [Overview](#overview-2)
    - [Procedure](#procedure-1)
  - [Assign Person Class to Providers](#assign-person-class-to-providers)
    - [Overview](#overview-3)
    - [Procedure](#procedure-2)
  - [Deactivate/Reactivate a User](#deactivatereactivate-a-user)
- [Special Handling—Correcting Person Class Data](#special-handlingcorrecting-person-class-data)
  - [Removing Person Class Entries](#removing-person-class-entries)
  - [Reactivating Person Class Entries](#reactivating-person-class-entries)
    - [Overview](#overview-4)
    - [Procedure](#procedure-3)
  - [Editing Reactivated Person Class Data](#editing-reactivated-person-class-data)
- [Appendix A—Person Class Codes: New, Updated, Inactivated, and Reactivated](#appendix-aperson-class-codes-new-updated-inactivated-and-reactivated)
  - [Person Class Code Changes](#person-class-code-changes)
  - [New Person Class Codes](#new-person-class-codes)
    - [Patch XU\8.0\377](#patch-xu80377)
    - [Patch XU\8.0\531](#patch-xu80531)
    - [Patch XU\8.0\671](#patch-xu80671)
  - [Updated Person Class Codes](#updated-person-class-codes)
  - [Inactivated Person Class Codes](#inactivated-person-class-codes)
    - [Patch XU\8.0\377](#patch-xu80377-1)
    - [Patch XU\8.0\531](#patch-xu80531-1)
    - [Patch XU\8.0\671](#patch-xu80671-1)
  - [Reactivated Person Class Codes](#reactivated-person-class-codes)
- [Appendix B—Printing VA Person Class Data](#appendix-bprinting-va-person-class-data)
  - [Report Sorted by Provider Type](#report-sorted-by-provider-type)
  - [Report Sorted by VA Code](#report-sorted-by-va-code)
  - [Report of Classifications Only](#report-of-classifications-only)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document is the *Assigning Person Class to Providers User Guide*. It provides the required steps to enter Person Class data.

In order to use the Assigning Person Class to Providers software, the following Veterans Health Information Systems and Technology Architecture (VistA) M Server Kernel patches *must* be installed (listed in patch number order):

- XU\*8.0\*27—Originally, developed to provide the functionality that enabled facilities to assign Person Class information. This patch was released on 08/14/1996.
- XU\*8.0\*377—Developed in order to update the Person Class data and related documentation. This patch was released on 10/24/2005.
- XU\*8.0\*531—Developed in order to update the Person Class data and related documentation. This patch was released on 02/17/2010.
- <span id="XU_80_671" class="anchor"></span>XU\*8.0\*671—Developed in order to lock down the file and transition the continued maintenance of the file to Standards & Terminology Services (STS). This patch was released on 08/17/2017.

As of October 1996, VHA facilities were required to report each ambulatory encounter and/or ancillary service. Provider, procedure, and diagnosis information is included in the minimum data set reported to the National Patient Care Database (NPCD). The provider information reported is the "Person Class" defined for all providers associated with ambulatory care delivery.

To comply with this requirement, all VA Medical Center (VAMC) providers were assigned a Profession/Occupation code (i.e., Person Class), so that a Person Class could be associated with each ambulatory patient encounter by October 1, 1996.

![](xu-8-671-assigning-person-class-to-providers-user-guide/011.png) <span id="Note" class="anchor"></span>NOTE: Standards & Terminology Services (STS) team maintains the PERSON CLASS (#8932.1) file and updates to related documents, such as the Department of Veterans Affairs' (VA) version of the Person Class Taxonomy Codes.

![](xu-8-671-assigning-person-class-to-providers-user-guide/012.png) REF: For a list of new, updated, inactivated, and reactivated VA Person Class codes released with Kernel Patches XU\*8.0\*377, XU\*8.0\*531and XU\*8.0\*671, see "<u>Appendix A—Person Class Codes: New, Updated, Inactivated, and Reactivated</u>."

![](xu-8-671-assigning-person-class-to-providers-user-guide/013.png) REF: For a list of the latest Provider Taxonomy Codes, see the Washington Publishing Company (WPC) Code Lists and X12 Registry (reference website): <http://www.wpc-edi.com/reference/>

## HCFA Provider Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Health Care Financing Administration (HCFA) provider classification system or taxonomy adopted by VHA is hierarchical and classifies providers into aggregate groupings:

- Services
- Provider types
- Areas of specialization or focus

The taxonomy represents a one-to-many relationship to the individual provider. Many occurrences of the taxonomy may apply to a single provider. For example, a provider who trains in Internal Medicine and specializes in Cardiology may appear with specialties in both Internal Medicine and Cardiology (two occurrences of the taxonomy relating to one provider). VHA assigns only one-Person Class to each provider, and in the example above, Cardiology would be the assigned Person Class as it is the more specific.

The PERSON CLASS Multiple field (200.05#) in the NEW PERSON (#200) file contains entries that reflect the assignment of HCFA taxonomy to providers. Each entry contains three data elements:

- PERSON CLASS (#.01) field—Pointer to PERSON CLASS (#8932.1) file.
- EFFECTIVE DATE (#.02) field—Date the code took effect.
- EXPIRATION DATE (#.03) field—Date the code ceased/expired/was replaced.

Entry of a new person in the NEW PERSON (#200) file asks for input of the following information:

- PERSON CLASS Multiple.
- Current Occupation/Profession.
- (optional) History.

## Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Assigning Person Class to Providers software (i.e., Kernel Patches XU\*8.0\*27, 377, 531, and 671) allows for interfaces with the entire VistA clinical software developed in-house. It also allows for interfaces with the QuadraMed Encoder Product Suite, which is a Commercial-Off-The-Shelf (COTS; *non*-VA) software product.

![](xu-8-671-assigning-person-class-to-providers-user-guide/014.png) REF: For more information on QuadraMed products, see the QuadraMed website at: [http://www.quadramed.com](http://www.quadramed.com/)

# Enter/Edit Person Class Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patches XU\*8.0\*27, 377, 531, and 671 enable users to enter or edit Person Class data for providers in three easy steps:

1.  <u>Identify All Active Providers</u>.
2.  <u>Identify Providers with Inactive Person Class Entries</u>.
1.  <u>Assign Person Class to Providers</u>.

## Identify All Active Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Identify all active providers currently associated with VA clinics (e.g., physicians, nurses, psychologists, social workers, etc.) for whom you need to enter Person Class information.

Use the User PC build Print option \[XUSER PC BUILD\] to print a list of active providers who need to have the Person Class data entered:

- This option is *not* attached to a menu.
- This option can be assigned to any user by adding it to the secondary menu of those users who will be working on this project; it can then be removed when the project is complete.

This option prints a list of users in the NEW PERSON (#200) file who are both a provider and active on the system, which means the user *must*:

- Hold the PROVIDER security key.
- Have a current Verify code.

The report from this option displays the following data for each individual listed:

- Name
- Provider Class
- Provider Type

![](xu-8-671-assigning-person-class-to-providers-user-guide/015.png) REF: To list providers with Inactive Person Class entries in the PERSON CLASS (#8932.1) file, see the "<u>Identify Providers with Inactive Person Class Entries</u>" section.

![](xu-8-671-assigning-person-class-to-providers-user-guide/016.png) REF: To print entries in the PERSON CLASS (#8932.1) file, see "<u>Appendix B—Printing VA Person Class Data</u>."

![](xu-8-671-assigning-person-class-to-providers-user-guide/017.png) REF: To view the current Health Care Provider Taxonomy Code Set, see the Washington Publishing Company (WPC) Code Lists and X12 Registry (reference website):  
<http://www.wpc-edi.com/reference/>  
  
The lists on this site are maintained by the following organizations:

- Centers for Medicare and Medicaid Services (CMS)
- National Uniform Claim Committee (NUCC)
- Committees that meet during standing X12 meetings

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To identify all active providers, perform the following procedure:

![](xu-8-671-assigning-person-class-to-providers-user-guide/018.png) NOTE: This procedure is done only once. It is only needed for the printout of a worksheet to record information on paper for faster data entry later.

1.  At the "Select OPTION NAME:" prompt, select the User PC build Print option \[XUSER PC BUILD\].
2.  At the "DEVICE:" prompt, press Enter to display the report directly to the screen or enter a specific device.
3.  The system displays the report as shown in <u>Figure 1</u>:

<span id="_Ref378839723" class="anchor"></span>Figure 1: User PC build Print Option—Sample User Dialogue and Report

Select OPTION NAME: <span class="mark">USER PC BUILD PRINT \<Enter\></span> User PC build Print

DEVICE: <span class="mark">\<Enter\></span> Network

NEW PERSON PROVIDER LIST JAN 30,2014 11:01 PAGE 1

PROVIDER

NAME PROVIDER CLASS TYPE

--------------------------------------------------------------------------------

KRNUSER,ONE D PHYSICIAN FULL TIME

<span class="mark">KRNUSER,TWO</span>

KRNUSER,THREE L DENTIST FULL TIME

KRNUSER,FOUR A PHARMACIST PART TIME

KRNUSER,FIVE W PHYSICIAN

KRNUSER,SIX L NURSE PRACTITIONER FULL TIME

In this example (<u>Figure 1</u>), the KRNUSER,TWO provider entry is missing the Provider Class information.

## Identify Providers with Inactive Person Class Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the List Inactive Person Class Users option \[XU-INACTIVE PERSON CLASS USERS\] to list providers who currently have inactive Person Classes and need to be assigned new Person Classes. This option is located under the User Management menu \[XUSER\]

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list providers with inactive Person Class entries, perform the following procedure:

![](xu-8-671-assigning-person-class-to-providers-user-guide/019.png) NOTE: This procedure is done only once. It is only needed for the printout of a worksheet to record information on paper for faster data entry later.

1.  From the User Management menu \[XUSER\], select the List Inactive Person Class Users option \[XU-INACTIVE PERSON CLASS USERS\].
2.  At the "Do you want to list active users only? NO//" prompt, enter YES.
3.  At the "DEVICE: HOME//" prompt, press Enter to display the report directly to the screen or enter a specific device.
4.  The system displays a list of providers, if any, with inactive Person Class entries (<u>Figure 2</u>).

> <span id="_Ref379441078" class="anchor"></span>Figure 2: List Inactive Person Class Users option—Sample User Dialogue and Report

Select User Management \<TEST ACCOUNT\> Option: <span class="mark">LIST INACTIVE \<Enter\></span> Person Class Users

Do you want to list active users only? NO// <span class="mark">YES</span>

DEVICE: HOME// <span class="mark">\<Enter\></span> Network

Report on Feb 06, 2014 Page 1

User name: Currently has the inactive Person Class IEN^NAME:

---------- -------------------------------------------------

<span class="mark">Number of users: 0</span>

## Assign Person Class to Providers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assign the appropriate Person Class to each provider associated with the clinics.

Use the Person Class Edit option \[XU-PERSON CLASS EDIT\] to enter or edit the Person Class for a provider. This option is located under the User Management menu \[XUSER\].

Once the Person Class has been entered for any provider, you can enter an additional or new Person Class by using the Person Class Edit option:

- The data input task is a simple one and can be assigned to anyone who will perform this task.
- This function allows only one active provider type during any one period of time.
- If the Enter on Duty Date is known, it should be entered in the Effective Date field. If the Enter on Duty Date is *not* known and the individual has been at the facility at least a year, we suggest that you enter a date one year prior to the current date.
- When you add a new Person Class entry to a provider who already has one defined, it is not necessary to enter the Expired Date of the previous Person Class. The application automatically inserts the Effective Date of the new Person Class as the Expired Date of the previous Person Class.
- Previous entries *must* remain on file for historical and legal purposes. You *cannot* delete or replace old entries. That is, you *cannot* modify the Person Class field itself.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enter or edit Person Class data, perform the following procedure:

1.  From the User Management menu \[XUSER\], select the Person Class Edit option \[XU-PERSON CLASS EDIT\].
2.  At the "Select NEW PERSON NAME:" prompt, enter the name of the provider whose Person Class data you wish to edit, as shown in <u>Figure 3</u>:

> <span id="_Ref378834612" class="anchor"></span>Figure 3: Person Class Edit Option—Sample User Dialogue

Select NEW PERSON NAME: <span class="mark">KRNUSER,TWO</span>

3.  The system opens the Edit of Person Class ScreenMan form, as shown in <u>Figure 4</u>:

> <span id="_Ref378834587" class="anchor"></span>Figure 4: Edit of Person Class ScreenMan Form—Displaying Current Person Class Data for a Provider

Edit of Person Class

<span class="mark">NAME: KRNUSER,TWO</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Person Class Effective Expired

Technologists, Technicians & Other Tec DEC 7,2005 JAN 7,2006

Emergency Medical Service Providers JAN 7,2006 DEC 7,2007

Other Service Providers DEC 7,2007 JAN 8,2008

<span class="mark">Allopathic and Osteopathic Physicians JAN 8,2008</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Technologists, Technicians and Other Technical Service Providers

Spec/Tech, Pathology

Laboratory Management, Diplomate

Press \<PF1\>H for help Insert

In this case, the provider has four assigned Person Classes. The most recent and currently active Person Class is *Allopathic and Osteopathic Physicians*.

1.  In the ScreenMan form, use the Arrow or Tab keys to select the Person Class data line.
2.  Once the line is highlighted, expanded descriptive text for that Person Class appears near the bottom of the screen (<u>Figure 4</u>).
4.  To add a new Person Class:
1.  Use the Arrow or Tab keys to navigate to the first blank Person Class line.
2.  Enter the name or the number of the specialty, as shown in <u>Figure 5</u>:

> <span id="_Ref378686175" class="anchor"></span>Figure 5: Edit of Person Class ScreenMan Form—Adding a New Specialty (1 of 3)

Edit of Person Class

<span class="mark">NAME: KRNUSER,TWO</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Person Class Effective Expired

Technologists, Technicians & Other Tec DEC 7,2005 JAN 7,2006

Emergency Medical Service Providers JAN 7,2006 DEC 7,2007

Other Service Providers DEC 7,2007 JAN 8,2008

Allopathic and Osteopathic Physicians JAN 8,2008

<span class="mark">193</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

*Podiatric Medicine and Surgery Service Providers 213ES0000XPodiatristSports Medicine*

...OK? Yes// <span class="mark">\<Enter\></span>

Are you adding '*Podiatric Medicine and Surgery Service Providers*' as

a new PERSON CLASS? No// <span class="mark">YES</span>

![](xu-8-671-assigning-person-class-to-providers-user-guide/020.png) NOTE: To enter duplicate entries you *must* enter the Person Class number in quotes (e.g., "213ES0000X"), this forces the duplicate entry into the field.  
  
For example, when a provider had left and comes back, there is a lapse in coverage. In order to enter the same Person Class entry, you have to enter the code within quotes. If you do not, the system takes you to the previous entry, which is expired.

3.  The system displays messages at the bottom of the screen (<u>Figure 5</u>) confirming that you want to add a new Person Class.
4.  At the "...OK? Yes//" prompt enter YES.
5.  At the "Are you adding *'xxxxxxxx*' as a new PERSON CLASS? No//" prompt, enter YES.
6.  The screen displays that specialty added under Person Class. The system automatically inserts today's date in the Effective date field, as shown in <u>Figure 6</u>. You can edit that date or leave it as is.

> <span id="_Ref378845948" class="anchor"></span>Figure 6: Edit of Person Class ScreenMan Form—Adding a New Specialty (2 of 3)

Edit of Person Class

<span class="mark">NAME: KRNUSER,TWO</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Person Class Effective Expired

Technologists, Technicians and Other TecDEC 7,2005JAN 7,2006Emergency Medical Service ProvidersJAN 7,2006DEC 7,2007Other Service ProvidersDEC 7,2007JAN 8,2008Allopathic and Osteopathic PhysiciansJAN 8,2008

<span class="mark">Podiatric Medicine and Surgery Service P</span> JAN 30,2014

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

7.  Tab over to the Expired date field of the *new* Person Class. The system automatically inserts today's date in the Expired date field of the *previously active* Person Class, as shown in <u>Figure 7</u>. You can edit that date or leave it as is.

> <span id="_Ref378846452" class="anchor"></span>Figure 7: Edit of Person Class ScreenMan Form—Adding a New Specialty (3 of 3)

Edit of Person Class

<span class="mark">NAME: KRNUSER,TWO</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Person Class Effective Expired

Technologists, Technicians and Other TecDEC 7,2005JAN 7,2006Emergency Medical Service ProvidersJAN 7,2006DEC 7,2007Other Service ProvidersDEC 7,2007JAN 8,2008Allopathic and Osteopathic PhysiciansJAN 8,2008<span class="mark">JAN 30, 2014</span>Podiatric Medicine and Surgery Service PJAN 30,2014

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

![](xu-8-671-assigning-person-class-to-providers-user-guide/021.png) NOTE: When re-entering previous (old) entries you *must* first save the Effective date, and then go back in to enter the Expired Date. For example, if you used the Remove a person class entry option \[XU-PERSON CLASS REMOVE\] and have to re-enter old entries, you *must*:

1.  Enter an Effective date.
2.  Save it.
3.  Enter an Expired date.
4.  Save it.

REF: For more information on re-entering previous (old) entries, see Section <u>3.1</u>.

## Deactivate/Reactivate a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deactivate or reactivate a user, use the following options located on the User Management menu \[XUSER\]:

- Reactivate a User option \[XUSERREACT\]—Used when a provider returns to a VA site.
- Deactivate a User option \[XUSERDEACT\]—Used when a provider leaves a VA site.

For example, when a provider (e.g., a medical student) rotates out, you can deactivate their account via the Deactivate a User option \[XUSERDEACT\]. The Reactivate a User option \[XUSERREACT\] gives you the opportunity to edit a provider's Person Class information. If the provider rotates in again, their Person Class information can be updated when they are reactivated.

![](xu-8-671-assigning-person-class-to-providers-user-guide/022.png) REF: For more information on deactivating and reactivating users, see the "Deactivating and Reactivating Users" section in th*e Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*, which is located on the VA Software Document Library (VDL) at: <http://www.va.gov/vdl/application.asp?appid=10>

# Special Handling—Correcting Person Class Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](xu-8-671-assigning-person-class-to-providers-user-guide/023.png) CAUTION: The tasks in this section should only be performed by authorized users or Information Resource Management (IRM) personnel!  
  
Most of these options are meant to be used for only critical Person Class data errors.

## Removing Person Class Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To remove incorrect Person Class entries from the Person Class Multiple in the NEW PERSON (#200) file, system administrators should use the Remove a person class entry option \[XU-PERSON CLASS REMOVE\] to delete all of the Person Class entries and then have the user re-enter them correctly (Section <u>2.2</u>).

![](xu-8-671-assigning-person-class-to-providers-user-guide/024.png) CAUTION: The PERSON CLASS Multiple holds a history, and under normal use, entries should *not* be removed.  
  
Also, if the Person Class entries go back a few years the previous Person Class entries could be inactive, which prevents the user from entering it. In this case, the old Person Class entry would have to be re-activated via VA FileMan.  
  
You can log a Remedy ticket to get assistance from the Health Systems Platform (HSP) team.

## Reactivating Person Class Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users *cannot* select "Inactive" entries in the PERSON CLASS (#8932.1) file. If an entry needs to be re-activated it requires special handling.

### Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To manually reactivate a Person Class entry, perform the following procedure:

1.  In Programmer Mode in VistA, retrieve the Internal Entry Number (IEN) for the Person Class entry to be reactivated.

> <span id="_Toc501605853" class="anchor"></span>Figure 8: Retrieving the IEN for the Person Class File Entry to be Reactivated

\><span class="mark">D ^%G</span>

Device: <span class="mark">\<Enter\></span>

Right margin: 80 =\> <span class="mark">\<Enter\></span>

Screen size for paging (0=nopaging)? 24 =\> <span class="mark">\<Enter\></span>

For help on global specifications DO HELP^%G

Global ^<span class="mark">USC(8932.1,"G","203BP0103Y "</span>

^USC(8932.1,"G","203BP0103Y ",<span class="mark">79</span>)=""

2.  In Programmer Mode in VistA, set the Person Class entry back to Active:

> <span id="_Toc501605854" class="anchor"></span>Figure : Setting Person Class File Entry to "a" (Active)

\>S \$P(^USC(8932.1,<span class="mark">79</span>,0),”^”,4)=”<span class="mark">a</span>”

4.  Perform the following field edits:
- "Stuff "a value in the X12 CODE field.
- Delete the DATE INACTIVATED field.
1.  From VA FileMan, select the Enter or Edit File Entries option \[DIEDIT\].
2.  At the "INPUT TO WHAT FILE: *PERSON CLASS*//", enter PERSON CLASS.
3.  At the "EDIT WHICH FIELD: ALL//" prompt, enter 6////*203BP0103Y*. This stuffs an X12 CODE value in the X12 CODE field.
4.  At the "THEN EDIT FIELD:" prompt, enter DATE INACTIVATED.
5.  At the "THEN EDIT FIELD:" prompt, press Enter when your entries are complete.
6.  At the "Select PERSON CLASS PROVIDER TYPE:" prompt, enter the Provider Type (e.g., using the IEN).
7.  At the "...OK? Yes//" prompt, verify it is the correct entry and enter YES.
8.  At the "DATE INACTIVATED: *MAY 30,2006*//" prompt:
1.  Save/Notate (write down) the current date value for re-use in Step 5j.
2.  Enter an At-Sign (@) to delete the date.
9.  At the "SURE YOU WANT TO DELETE?" prompt, enter YES.

> <span id="_Toc501605855" class="anchor"></span>Figure 10: Stuffing the X12 CODE and Deleting the DATE INACTIVATED Fields

Select OPTION: <span class="mark">ENTER OR EDIT FILE ENTRIES</span>

INPUT TO WHAT FILE: *PERSON CLASS*// <span class="mark">\<Enter\></span>

EDIT WHICH FIELD: ALL// <span class="mark">6////*203BP0103Y* \<Enter\></span> X12 CODE

THEN EDIT FIELD: <span class="mark">DATE INACTIVATED</span>

THEN EDIT FIELD: <span class="mark">\<Enter\></span>

Select PERSON CLASS PROVIDER TYPE: <span class="mark">\`79 \<Enter\></span> Physicians (M.D. and D.O.)

Physician/Osteopath

Pathology, Anatomic & Laboratory Medicine

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

DATE INACTIVATED: *MAY 30,2006*// <span class="mark">@</span>

SURE YOU WANT TO DELETE? <span class="mark">Y \<Enter\></span> (Yes)

5.  The user should re-add the entry by following the procedure in Section <u>2.3.2</u>.

> <span id="_Toc501605856" class="anchor"></span>Figure 11: Adding the Entry Using the Person Class Edit Option

Select NEW PERSON NAME: <span class="mark">KRNUSER,FIFTY</span>

Edit of Person Class

NAME: <span class="mark">KRNUSER,FIFTY</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Person Class Effective Expired

Physicians (M.D. and D.O.) JUL 17,2013

6.  Once complete, re-edit the entry STATUS, DATE INACTIVATED, and X12 CODE fields:
1.  From VA FileMan, select the Enter or Edit File Entries option \[DIEDIT\].
2.  At the "INPUT TO WHAT FILE: *PERSON CLASS*//" prompt, enter PERSON CLASS.
3.  At the "EDIT WHICH FIELD: ALL//" prompt, enter STATUS.
4.  At the "THEN EDIT FIELD:" prompt, enter DATE INACTIVATED.
5.  At the "THEN EDIT FIELD:" prompt, enter X12 CODE.
6.  At the "THEN EDIT FIELD:" prompt, press Enter when your entries are complete.
7.  At the "Select PERSON CLASS PROVIDER TYPE:" prompt, enter the Provider Type. Pressing the \<Spacebar\>\<Enter\> keys inserts the last used Provider Type.
8.  At the "...OK? Yes//" prompt, verify it is the correct entry and enter YES.
9.  At the "STATUS: Active//" prompt, enter INACTIVE.
10. At the "DATE INACTIVATED: *JUL 17,2013*//" prompt, enter the saved date value from Step 3h.
11. At the "X12 CODE: *203BP0103Y*//" prompt, enter an At-Sign (@) to delete the X12 CODE.
12. At the "SURE YOU WANT TO DELETE?" prompt, confirm the delete by entering YES.

> <span id="_Toc501605857" class="anchor"></span>Figure 12: Editing the Entry Fields: STATUS, DATE INACTIVATED, and X12 CODE

Select OPTION: <span class="mark">ENTER OR EDIT FILE ENTRIES</span>

INPUT TO WHAT FILE: *PERSON CLASS*// <span class="mark">\<Enter\></span>

EDIT WHICH FIELD: ALL// <span class="mark">STATUS</span>

THEN EDIT FIELD: <span class="mark">DATE INACTIVATED</span>

THEN EDIT FIELD: <span class="mark">X12 CODE</span>

THEN EDIT FIELD: <span class="mark">\<Enter\></span>

Select PERSON CLASS PROVIDER TYPE: <span class="mark">\<Spacebar\>\<Enter\></span> Physicians (M.D. and D.O.) 203BP0103Y

Physician/Osteopath

Pathology, Anatomic & Laboratory Medicine

...OK? Yes// <span class="mark">\<Enter\></span> (Yes)

STATUS: Active// <span class="mark">I \<Enter\></span> Inactive

DATE INACTIVATED: *JUL 17,2013*// <span class="mark">*5 30 06* \<Enter\></span> (MAY 30, 2006)

X12 CODE: *203BP0103Y*// <span class="mark">@</span>

SURE YOU WANT TO DELETE? <span class="mark">Y \<Enter\></span> (Yes)

## Editing Reactivated Person Class Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To edit Person Class data for reactivated entries, you can use the Person Class Edit option \[XU-PERSON CLASS EDIT\] (Section <u>2.3.2</u>) or Edit an Existing User option \[XUSEREDIT\] on the User Management menu \[XUSER\]. If you are using the Edit an Existing User option \[XUSEREDIT\], the Person Class data is located on the third screen, as shown in <u>Figure 13</u>:

<span id="_Ref378858322" class="anchor"></span>Figure 13: Edit an Existing User Option (Screen 3)—Sample User Dialogue

Edit an Existing User

<span class="mark">NAME: KRNUSER,TWO</span> Page 3 of 5

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

PROHIBITED TIMES FOR SIGN-ON:

PHONE: 999-555-5555 OFFICE PHONE: 999-555-5555

COMMERCIAL PHONE: FAX NUMBER:

VOICE PAGER: DIGITAL PAGER:

LANGUAGE:

<span class="mark">Person Class Effective Expired</span>

<span class="mark">Technologists, Technicians and Other TecDEC 7,2005JAN 7,2006 </span>

<span class="mark">Emergency Medical Service ProvidersJAN 7,2006DEC 7,2007 </span>

<span class="mark">Other Service ProvidersDEC 7,2007JAN 8,2008 </span>

<span class="mark">Allopathic and Osteopathic PhysiciansJAN 8,2008JAN 30,2014 </span>

<span class="mark">Podiatric Medicine and Surgery Service PJAN 30,2014</span>

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

# Appendix A—Person Class Codes: New, Updated, Inactivated, and Reactivated

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Person Class Code Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix contains a list of the new, updated, inactivated, and reactivated Person Class codes as of Kernel Patch XU\*8.0\*671 (released on 08/17/2017).

- <u>New Person Class Codes</u>
- <u>Updated Person Class Codes</u>
- <u>Inactivated Person Class Codes</u>
- <u>Reactivated Person Class Codes</u>

![](xu-8-671-assigning-person-class-to-providers-user-guide/025.png) REF: For a list of the latest Provider Taxonomy Codes, see the Washington Publishing Company (WPC) Code Lists and X12 Registry (reference website): <http://www.wpc-edi.com/reference/>

![](xu-8-671-assigning-person-class-to-providers-user-guide/026.png) REF: To print entries in the PERSON CLASS (#8932.1) file, see "<u>Appendix B—Printing VA Person Class Data</u>."

## New Person Class Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Patch XU\*8.0\*377</u>
- <u>Patch XU\*8.0\*531</u>
- <u>Patch XU\*8.0\*671</u>

### Patch XU\*8.0\*377

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 2</u> lists all *new* Person Class codes released with Kernel Patch XU\*8.0\*377 (released on 10/24/2005):

<table>
<caption><p><span id="_Ref378837660" class="anchor"></span>Table 3: New Person Class Codes—Kernel Patch XU*8.0*531</p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>Status</th>
<th>VA Code</th>
<th>NUCC<br />
X12 Code</th>
<th>Provider Type</th>
<th>Classification</th>
<th>Area of Specialization</th>
<th>CMS Specialty Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>735</td>
<td>Active</td>
<td>V010421</td>
<td>103TP0814X</td>
<td>Behavioral Health and Social Service Providers</td>
<td>Psychologist</td>
<td>Psychoanalysis</td>
<td></td>
</tr>
<tr class="even">
<td>736</td>
<td>Active</td>
<td>V030510</td>
<td>1223X0008X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Oral and Maxillofacial Radiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>737</td>
<td>Active</td>
<td>V050500</td>
<td>146D00000X</td>
<td>Emergency Medical Service Providers</td>
<td>Personal Emergency Response Attendant</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>738</td>
<td>Active</td>
<td>V060807</td>
<td>152WC0802X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Corneal and Contact Management</td>
<td>41</td>
</tr>
<tr class="odd">
<td>739</td>
<td>Active</td>
<td>V070807</td>
<td>167G00000X</td>
<td>Nursing Service Providers</td>
<td>Licensed Psychiatric Technician</td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>740</td>
<td>Active</td>
<td>V080502</td>
<td>171WV0202X</td>
<td>Other Service Providers</td>
<td>Contractor</td>
<td>Vehicle Modifications</td>
<td></td>
</tr>
<tr class="odd">
<td>741</td>
<td>Active</td>
<td>V082300</td>
<td>177F00000X</td>
<td>Other Service Providers</td>
<td>Lodging</td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>742</td>
<td>Active</td>
<td>V090300</td>
<td>183700000X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacy Technician</td>
<td> </td>
<td></td>
</tr>
<tr class="odd">
<td>949</td>
<td>Active</td>
<td>V100700</td>
<td>367H00000X</td>
<td>Physician Assistants and Advanced Practice Nursing Providers</td>
<td>Anesthesiologist Assistant</td>
<td> </td>
<td>32</td>
</tr>
<tr class="even">
<td>915</td>
<td>Active</td>
<td>V130701</td>
<td>2278C0205X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Critical Care</td>
<td></td>
</tr>
<tr class="odd">
<td>917</td>
<td>Active</td>
<td>V130702</td>
<td>2278E1000X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Educational</td>
<td></td>
</tr>
<tr class="even">
<td>916</td>
<td>Active</td>
<td>V130703</td>
<td>2278E0002X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Emergency Care</td>
<td></td>
</tr>
<tr class="odd">
<td>919</td>
<td>Active</td>
<td>V130704</td>
<td>2278G1100X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>General Care</td>
<td></td>
</tr>
<tr class="even">
<td>918</td>
<td>Active</td>
<td>V130705</td>
<td>2278G0305X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Geriatric Care</td>
<td></td>
</tr>
<tr class="odd">
<td>920</td>
<td>Active</td>
<td>V130706</td>
<td>2278H0200X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Home Health</td>
<td></td>
</tr>
<tr class="even">
<td>925</td>
<td>Active</td>
<td>V130707</td>
<td>2278P3900X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Neonatal/Pediatrics</td>
<td></td>
</tr>
<tr class="odd">
<td>924</td>
<td>Active</td>
<td>V130708</td>
<td>2278P3800X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Palliative/Hospice</td>
<td></td>
</tr>
<tr class="even">
<td>926</td>
<td>Active</td>
<td>V130709</td>
<td>2278P4000X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Patient Transport</td>
<td></td>
</tr>
<tr class="odd">
<td>921</td>
<td>Active</td>
<td>V130710</td>
<td>2278P1004X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Pulmonary Diagnostics</td>
<td></td>
</tr>
<tr class="even">
<td>923</td>
<td>Active</td>
<td>V130711</td>
<td>2278P1006X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Pulmonary Function Technologist</td>
<td></td>
</tr>
<tr class="odd">
<td>922</td>
<td>Active</td>
<td>V130712</td>
<td>2278P1005X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Pulmonary Rehabilitation</td>
<td></td>
</tr>
<tr class="even">
<td>927</td>
<td>Active</td>
<td>V130713</td>
<td>2278S1500X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>SNF/Subacute Care</td>
<td></td>
</tr>
<tr class="odd">
<td>928</td>
<td>Active</td>
<td>V130801</td>
<td>2279C0205X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Critical Care</td>
<td></td>
</tr>
<tr class="even">
<td>930</td>
<td>Active</td>
<td>V130802</td>
<td>2279E1000X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Educational</td>
<td></td>
</tr>
<tr class="odd">
<td>929</td>
<td>Active</td>
<td>V130803</td>
<td>2279E0002X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Emergency Care</td>
<td></td>
</tr>
<tr class="even">
<td>932</td>
<td>Active</td>
<td>V130804</td>
<td>2279G1100X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>General Care</td>
<td></td>
</tr>
<tr class="odd">
<td>931</td>
<td>Active</td>
<td>V130805</td>
<td>2279G0305X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Geriatric Care</td>
<td></td>
</tr>
<tr class="even">
<td>933</td>
<td>Active</td>
<td>V130806</td>
<td>2279H0200X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Home Health</td>
<td></td>
</tr>
<tr class="odd">
<td>938</td>
<td>Active</td>
<td>V130807</td>
<td>2279P3900X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Neonatal/Pediatrics</td>
<td></td>
</tr>
<tr class="even">
<td>937</td>
<td>Active</td>
<td>V130808</td>
<td>2279P3800X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Palliative/Hospice</td>
<td></td>
</tr>
<tr class="odd">
<td>939</td>
<td>Active</td>
<td>V130809</td>
<td>2279P4000X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Patient Transport</td>
<td></td>
</tr>
<tr class="even">
<td>934</td>
<td>Active</td>
<td>V130810</td>
<td>2279P1004X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Pulmonary Diagnostics</td>
<td></td>
</tr>
<tr class="odd">
<td>936</td>
<td>Active</td>
<td>V130811</td>
<td>2279P1006X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Pulmonary Function Technologist</td>
<td></td>
</tr>
<tr class="even">
<td>935</td>
<td>Active</td>
<td>V130812</td>
<td>2279P1005X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Pulmonary Rehabilitation</td>
<td></td>
</tr>
<tr class="odd">
<td>940</td>
<td>Active</td>
<td>V130813</td>
<td>2279S1500X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>SNF/Subacute Care</td>
<td></td>
</tr>
<tr class="even">
<td>945</td>
<td>Active</td>
<td>V130901</td>
<td>2471B0102X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Bone Densitometry</td>
<td></td>
</tr>
<tr class="odd">
<td>946</td>
<td>Active</td>
<td>V130902</td>
<td>2471C1106X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Cardiac-Interventional Technology</td>
<td></td>
</tr>
<tr class="even">
<td>947</td>
<td>Active</td>
<td>V130903</td>
<td>2471V0105X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Vascular Sonography</td>
<td></td>
</tr>
<tr class="odd">
<td>948</td>
<td>Active</td>
<td>V130904</td>
<td>2471V0106X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Vascular-Interventional Technology</td>
<td></td>
</tr>
<tr class="even">
<td>941</td>
<td>Active</td>
<td>V151200</td>
<td>246X00000X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td> </td>
<td></td>
</tr>
<tr class="odd">
<td>942</td>
<td>Active</td>
<td>V151201</td>
<td>246XC2901X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td>Cardiovascular Invasive Specialist</td>
<td></td>
</tr>
<tr class="even">
<td>944</td>
<td>Active</td>
<td>V151202</td>
<td>246XS1301X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td>Sonography</td>
<td></td>
</tr>
<tr class="odd">
<td>943</td>
<td>Active</td>
<td>V151203</td>
<td>246XC2903X</td>
<td>Technologists, Technicians and Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td>Vascular Specialist</td>
<td></td>
</tr>
<tr class="even">
<td>953</td>
<td>Active</td>
<td>V170602</td>
<td>3747A0650X</td>
<td>Nursing Service Related Providers</td>
<td>Technician</td>
<td>Attendant Care Provider</td>
<td></td>
</tr>
<tr class="odd">
<td>951</td>
<td>Active</td>
<td>V170700</td>
<td>372600000X</td>
<td>Nursing Service Related Providers</td>
<td>Adult Companion</td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>950</td>
<td>Active</td>
<td>V170800</td>
<td>372500000X</td>
<td>Nursing Service Related Providers</td>
<td>Chore Provider</td>
<td> </td>
<td></td>
</tr>
<tr class="odd">
<td>952</td>
<td>Active</td>
<td>V170900</td>
<td>373H00000X</td>
<td>Nursing Service Related Providers</td>
<td>Day Training/Habilitation Specialist</td>
<td> </td>
<td></td>
</tr>
<tr class="even">
<td>747</td>
<td>Active</td>
<td>V180100</td>
<td>207K00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Allergy and Immunology</td>
<td> </td>
<td>3</td>
</tr>
<tr class="odd">
<td>748</td>
<td>Active</td>
<td>V180101</td>
<td>207KA0200X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Allergy and Immunology</td>
<td>Allergy</td>
<td>3</td>
</tr>
<tr class="even">
<td>749</td>
<td>Active</td>
<td>V180102</td>
<td>207KI0005X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Allergy and Immunology</td>
<td>Clinical and Laboratory Immunology</td>
<td>3</td>
</tr>
<tr class="odd">
<td>750</td>
<td>Active</td>
<td>V180200</td>
<td>207L00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td> </td>
<td>5</td>
</tr>
<tr class="even">
<td>751</td>
<td>Active</td>
<td>V180201</td>
<td>207LA0401X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Addiction Medicine</td>
<td>5</td>
</tr>
<tr class="odd">
<td>752</td>
<td>Active</td>
<td>V180202</td>
<td>207LC0200X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Critical Care Medicine</td>
<td>5</td>
</tr>
<tr class="even">
<td>753</td>
<td>Active</td>
<td>V180203</td>
<td>207LP2900X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Pain Medicine</td>
<td>5</td>
</tr>
<tr class="odd">
<td>911</td>
<td>Active</td>
<td>V180300</td>
<td>208U00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Clinical Pharmacology</td>
<td> </td>
<td>1</td>
</tr>
<tr class="even">
<td>907</td>
<td>Active</td>
<td>V180400</td>
<td>208C00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Colon and Rectal Surgery</td>
<td> </td>
<td>28</td>
</tr>
<tr class="odd">
<td>754</td>
<td>Active</td>
<td>V180500</td>
<td>207N00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Dermatology</td>
<td> </td>
<td>7</td>
</tr>
<tr class="even">
<td>757</td>
<td>Active</td>
<td>V180501</td>
<td>207NI0002X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Clinical and Laboratory Dermatological Immunology</td>
<td>7</td>
</tr>
<tr class="odd">
<td>759</td>
<td>Active</td>
<td>V180502</td>
<td>207NS0135X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Dermatological Surgery</td>
<td>7</td>
</tr>
<tr class="even">
<td>756</td>
<td>Active</td>
<td>V180503</td>
<td>207ND0900X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Dermatopathology</td>
<td>7</td>
</tr>
<tr class="odd">
<td>755</td>
<td>Active</td>
<td>V180504</td>
<td>207ND0101X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Dermatology</td>
<td>MOHS-Micrographic Surgery</td>
<td>7</td>
</tr>
<tr class="even">
<td>758</td>
<td>Active</td>
<td>V180505</td>
<td>207NP0225X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Pediatric Dermatology</td>
<td>7</td>
</tr>
<tr class="odd">
<td>760</td>
<td>Active</td>
<td>V180600</td>
<td>207P00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td> </td>
<td>93</td>
</tr>
<tr class="even">
<td>761</td>
<td>Active</td>
<td>V180601</td>
<td>207PE0004X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Emergency Medical Services</td>
<td>93</td>
</tr>
<tr class="odd">
<td>765</td>
<td>Active</td>
<td>V180602</td>
<td>207PT0002X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Medical Toxicology</td>
<td>93</td>
</tr>
<tr class="even">
<td>763</td>
<td>Active</td>
<td>V180603</td>
<td>207PP0204X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Pediatric Emergency Medicine</td>
<td>93</td>
</tr>
<tr class="odd">
<td>764</td>
<td>Active</td>
<td>V180604</td>
<td>207PS0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Sports Medicine</td>
<td>93</td>
</tr>
<tr class="even">
<td>762</td>
<td>Active</td>
<td>V180605</td>
<td>207PE0005X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Undersea and Hyperbaric Medicine</td>
<td>93</td>
</tr>
<tr class="odd">
<td>766</td>
<td>Active</td>
<td>V180700</td>
<td>207Q00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Family Practice</td>
<td> </td>
<td>8</td>
</tr>
<tr class="even">
<td>768</td>
<td>Active</td>
<td>V180701</td>
<td>207QA0401X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Family Practice</td>
<td>Addiction Medicine</td>
<td>8</td>
</tr>
<tr class="odd">
<td>767</td>
<td>Active</td>
<td>V180702</td>
<td>207QA0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Family Practice</td>
<td>Adolescent Medicine</td>
<td>8</td>
</tr>
<tr class="even">
<td>769</td>
<td>Active</td>
<td>V180703</td>
<td>207QA0505X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Family Practice</td>
<td>Adult Medicine</td>
<td>8</td>
</tr>
<tr class="odd">
<td>770</td>
<td>Active</td>
<td>V180704</td>
<td>207QG0300X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Family Practice</td>
<td>Geriatric Medicine</td>
<td>8</td>
</tr>
<tr class="even">
<td>771</td>
<td>Active</td>
<td>V180705</td>
<td>207QS0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Family Practice</td>
<td>Sports Medicine</td>
<td>8</td>
</tr>
<tr class="odd">
<td>908</td>
<td>Active</td>
<td>V180800</td>
<td>208D00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>General Practice</td>
<td> </td>
<td>1</td>
</tr>
<tr class="even">
<td>910</td>
<td>Active</td>
<td>V180900</td>
<td>208M00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Hospitalist</td>
<td> </td>
<td>1</td>
</tr>
<tr class="odd">
<td>772</td>
<td>Active</td>
<td>V181000</td>
<td>207R00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td> </td>
<td>11</td>
</tr>
<tr class="even">
<td>775</td>
<td>Active</td>
<td>V181001</td>
<td>207RA0401X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Addiction Medicine</td>
<td>11</td>
</tr>
<tr class="odd">
<td>773</td>
<td>Active</td>
<td>V181002</td>
<td>207RA0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Adolescent Medicine</td>
<td>11</td>
</tr>
<tr class="even">
<td>774</td>
<td>Active</td>
<td>V181003</td>
<td>207RA0201X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Allergy and Immunology</td>
<td>11</td>
</tr>
<tr class="odd">
<td>776</td>
<td>Active</td>
<td>V181004</td>
<td>207RC0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Cardiovascular Disease</td>
<td>6</td>
</tr>
<tr class="even">
<td>784</td>
<td>Active</td>
<td>V181005</td>
<td>207RI0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Clinical and Laboratory Immunology</td>
<td>11</td>
</tr>
<tr class="odd">
<td>777</td>
<td>Active</td>
<td>V181006</td>
<td>207RC0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Clinical Cardiac Electrophysiology</td>
<td>6</td>
</tr>
<tr class="even">
<td>778</td>
<td>Active</td>
<td>V181007</td>
<td>207RC0200X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Critical Care Medicine</td>
<td>81</td>
</tr>
<tr class="odd">
<td>779</td>
<td>Active</td>
<td>V181008</td>
<td>207RE0101X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Endocrinology, Diabetes and Metabolism</td>
<td>46</td>
</tr>
<tr class="even">
<td>780</td>
<td>Active</td>
<td>V181009</td>
<td>207RG0100X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Gastroenterology</td>
<td>10</td>
</tr>
<tr class="odd">
<td>781</td>
<td>Active</td>
<td>V181010</td>
<td>207RG0300X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Geriatric Medicine</td>
<td>38</td>
</tr>
<tr class="even">
<td>782</td>
<td>Active</td>
<td>V181011</td>
<td>207RH0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hematology</td>
<td>82</td>
</tr>
<tr class="odd">
<td>783</td>
<td>Active</td>
<td>V181012</td>
<td>207RH0003X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hematology and Oncology</td>
<td>83</td>
</tr>
<tr class="even">
<td>785</td>
<td>Active</td>
<td>V181013</td>
<td>207RI0008X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hepatology</td>
<td>11</td>
</tr>
<tr class="odd">
<td>787</td>
<td>Active</td>
<td>V181014</td>
<td>207RI0200X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Infectious Disease</td>
<td>44</td>
</tr>
<tr class="even">
<td>786</td>
<td>Active</td>
<td>V181015</td>
<td>207RI0011X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Interventional Cardiology</td>
<td>6</td>
</tr>
<tr class="odd">
<td>788</td>
<td>Active</td>
<td>V181016</td>
<td>207RM1200X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Magnetic Resonance Imaging (MRI)</td>
<td>11</td>
</tr>
<tr class="even">
<td>793</td>
<td>Active</td>
<td>V181017</td>
<td>207RX0202X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Medical Oncology</td>
<td>90</td>
</tr>
<tr class="odd">
<td>789</td>
<td>Active</td>
<td>V181018</td>
<td>207RN0300X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Nephrology</td>
<td>39</td>
</tr>
<tr class="even">
<td>790</td>
<td>Active</td>
<td>V181019</td>
<td>207RP1001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Pulmonary Disease</td>
<td>29</td>
</tr>
<tr class="odd">
<td>791</td>
<td>Active</td>
<td>V181020</td>
<td>207RR0500X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Rheumatology</td>
<td>66</td>
</tr>
<tr class="even">
<td>792</td>
<td>Active</td>
<td>V181021</td>
<td>207RS0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Sports Medicine</td>
<td>11</td>
</tr>
<tr class="odd">
<td>914</td>
<td>Active</td>
<td>V181100</td>
<td>209800000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Legal Medicine</td>
<td> </td>
<td>11</td>
</tr>
<tr class="even">
<td>796</td>
<td>Active</td>
<td>V181200</td>
<td>207SG0202X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Biochemical Genetics</td>
<td></td>
</tr>
<tr class="odd">
<td>794</td>
<td>Active</td>
<td>V181301</td>
<td>207SC0300X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Cytogenetic</td>
<td></td>
</tr>
<tr class="even">
<td>795</td>
<td>Active</td>
<td>V181302</td>
<td>207SG0201X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Genetics (M.D.)</td>
<td></td>
</tr>
<tr class="odd">
<td>797</td>
<td>Active</td>
<td>V181303</td>
<td>207SG0203X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Molecular Genetics</td>
<td></td>
</tr>
<tr class="even">
<td>799</td>
<td>Active</td>
<td>V181304</td>
<td>207SM0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Molecular Genetic Pathology</td>
<td></td>
</tr>
<tr class="odd">
<td>798</td>
<td>Active</td>
<td>V181305</td>
<td>207SG0205X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Ph.D. Medical Genetics</td>
<td></td>
</tr>
<tr class="even">
<td>800</td>
<td>Active</td>
<td>V181400</td>
<td>207T00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Neurological Surgery</td>
<td> </td>
<td>14</td>
</tr>
<tr class="odd">
<td>744</td>
<td>Active</td>
<td>V181500</td>
<td>204D00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Neuromusculoskeletal Medicine and OMM</td>
<td> </td>
<td>12</td>
</tr>
<tr class="even">
<td>743</td>
<td>Active</td>
<td>V181600</td>
<td>204C00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Neuromusculoskeletal Medicine, Sports Medicine</td>
<td> </td>
<td>12</td>
</tr>
<tr class="odd">
<td>801</td>
<td>Active</td>
<td>V181700</td>
<td>207U00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td> </td>
<td>36</td>
</tr>
<tr class="even">
<td>804</td>
<td>Active</td>
<td>V181701</td>
<td>207UN0903X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td>In Vivo and In Vitro Nuclear Medicine</td>
<td>36</td>
</tr>
<tr class="odd">
<td>802</td>
<td>Active</td>
<td>V181702</td>
<td>207UN0901X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td>Nuclear Cardiology</td>
<td>36</td>
</tr>
<tr class="even">
<td>803</td>
<td>Active</td>
<td>V181703</td>
<td>207UN0902X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td>Nuclear Imaging and Therapy</td>
<td>36</td>
</tr>
<tr class="odd">
<td>805</td>
<td>Active</td>
<td>V181800</td>
<td>207V00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td> </td>
<td>16</td>
</tr>
<tr class="even">
<td>806</td>
<td>Active</td>
<td>V181801</td>
<td>207VC0200X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td>Critical Care Medicine</td>
<td>16</td>
</tr>
<tr class="odd">
<td>811</td>
<td>Active</td>
<td>V181802</td>
<td>207VX0201X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td>Gynecologic Oncology</td>
<td>16</td>
</tr>
<tr class="even">
<td>808</td>
<td>Active</td>
<td>V181803</td>
<td>207VG0400X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td>Gynecology</td>
<td>16</td>
</tr>
<tr class="odd">
<td>809</td>
<td>Active</td>
<td>V181804</td>
<td>207VM0101X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td>Maternal and Fetal Medicine</td>
<td>16</td>
</tr>
<tr class="even">
<td>810</td>
<td>Active</td>
<td>V181805</td>
<td>207VX0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td>Obstetrics</td>
<td>16</td>
</tr>
<tr class="odd">
<td>807</td>
<td>Active</td>
<td>V181806</td>
<td>207VE0102X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Obstetrics and Gynecology</td>
<td>Reproductive Endocrinology</td>
<td>16</td>
</tr>
<tr class="even">
<td>812</td>
<td>Active</td>
<td>V181900</td>
<td>207W00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td> </td>
<td>18</td>
</tr>
<tr class="odd">
<td>745</td>
<td>Active</td>
<td>V182000</td>
<td>204E00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Oral and Maxillofacial Surgery</td>
<td> </td>
<td>85</td>
</tr>
<tr class="even">
<td>813</td>
<td>Active</td>
<td>V182100</td>
<td>207X00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td> </td>
<td>20</td>
</tr>
<tr class="odd">
<td>815</td>
<td>Active</td>
<td>V182101</td>
<td>207XS0114X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Adult Reconstructive Orthopaedic Surgery</td>
<td>20</td>
</tr>
<tr class="even">
<td>817</td>
<td>Active</td>
<td>V182102</td>
<td>207XX0004X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Foot and Ankle Orthopaedics</td>
<td>20</td>
</tr>
<tr class="odd">
<td>814</td>
<td>Active</td>
<td>V182103</td>
<td>207XS0106X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Hand Surgery</td>
<td>40</td>
</tr>
<tr class="even">
<td>816</td>
<td>Active</td>
<td>V182104</td>
<td>207XS0117X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Orthopaedic Surgery of the Spine</td>
<td>20</td>
</tr>
<tr class="odd">
<td>819</td>
<td>Active</td>
<td>V182105</td>
<td>207XX0801X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Orthopaedic Trauma</td>
<td>20</td>
</tr>
<tr class="even">
<td>818</td>
<td>Active</td>
<td>V182106</td>
<td>207XX0005X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Sports Medicine</td>
<td>20</td>
</tr>
<tr class="odd">
<td>820</td>
<td>Active</td>
<td>V182200</td>
<td>207Y00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td> </td>
<td>4</td>
</tr>
<tr class="even">
<td>822</td>
<td>Active</td>
<td>V182201</td>
<td>207YS0123X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Facial Plastic Surgery</td>
<td>24</td>
</tr>
<tr class="odd">
<td>824</td>
<td>Active</td>
<td>V182202</td>
<td>207YX0602X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Otolaryngic Allergy</td>
<td>4</td>
</tr>
<tr class="even">
<td>826</td>
<td>Active</td>
<td>V182203</td>
<td>207YX0905X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Otolaryngology/Facial Plastic Surgery</td>
<td>24</td>
</tr>
<tr class="odd">
<td>825</td>
<td>Active</td>
<td>V182204</td>
<td>207YX0901X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Otology and Neurotology</td>
<td>4</td>
</tr>
<tr class="even">
<td>821</td>
<td>Active</td>
<td>V182205</td>
<td>207YP0228X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Pediatric Otolaryngology</td>
<td>4</td>
</tr>
<tr class="odd">
<td>823</td>
<td>Active</td>
<td>V182206</td>
<td>207YX0007X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Plastic Surgery within the Head and Neck</td>
<td>4</td>
</tr>
<tr class="even">
<td>913</td>
<td>Active</td>
<td>V182301</td>
<td>208VP0014X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pain Medicine</td>
<td>Interventional Pain Medicine</td>
<td>9</td>
</tr>
<tr class="odd">
<td>912</td>
<td>Active</td>
<td>V182302</td>
<td>208VP0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pain Medicine</td>
<td>Pain Medicine</td>
<td>72</td>
</tr>
<tr class="even">
<td>836</td>
<td>Active</td>
<td>V182401</td>
<td>207ZP0101X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Anatomic Pathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>837</td>
<td>Active</td>
<td>V182402</td>
<td>207ZP0102X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Anatomic Pathology and Clinical Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>827</td>
<td>Active</td>
<td>V182403</td>
<td>207ZB0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Blood Banking and Transfusion Medicine</td>
<td>22</td>
</tr>
<tr class="odd">
<td>838</td>
<td>Active</td>
<td>V182404</td>
<td>207ZP0104X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Chemical Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>839</td>
<td>Active</td>
<td>V182405</td>
<td>207ZP0105X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Clinical Pathology/Laboratory Medicine</td>
<td>22</td>
</tr>
<tr class="odd">
<td>828</td>
<td>Active</td>
<td>V182406</td>
<td>207ZC0500X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Cytopathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>829</td>
<td>Active</td>
<td>V182407</td>
<td>207ZD0900X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Dermatopathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>830</td>
<td>Active</td>
<td>V182408</td>
<td>207ZF0201X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Forensic Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>831</td>
<td>Active</td>
<td>V182409</td>
<td>207ZH0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Hematology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>832</td>
<td>Active</td>
<td>V182410</td>
<td>207ZI0100X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Immunopathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>833</td>
<td>Active</td>
<td>V182411</td>
<td>207ZM0300X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Medical Microbiology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>835</td>
<td>Active</td>
<td>V182412</td>
<td>207ZP0007X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Molecular Genetic Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>834</td>
<td>Active</td>
<td>V182413</td>
<td>207ZN0500X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Neuropathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>840</td>
<td>Active</td>
<td>V182414</td>
<td>207ZP0213X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Pediatric Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>841</td>
<td>Active</td>
<td>V182500</td>
<td>208000000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td> </td>
<td>37</td>
</tr>
<tr class="odd">
<td>842</td>
<td>Active</td>
<td>V182501</td>
<td>2080A0000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Adolescent Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>843</td>
<td>Active</td>
<td>V182502</td>
<td>2080I0007X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Clinical and Laboratory Immunology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>845</td>
<td>Active</td>
<td>V182503</td>
<td>2080P0006X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Developmental - Behavioral Pediatrics</td>
<td>37</td>
</tr>
<tr class="even">
<td>859</td>
<td>Active</td>
<td>V182504</td>
<td>2080T0002X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Medical Toxicology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>844</td>
<td>Active</td>
<td>V182505</td>
<td>2080N0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Neonatal-Perinatal Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>846</td>
<td>Active</td>
<td>V182506</td>
<td>2080P0008X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Neurodevelopmental Disabilities</td>
<td>37</td>
</tr>
<tr class="odd">
<td>847</td>
<td>Active</td>
<td>V182507</td>
<td>2080P0201X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Allergy and Immunology</td>
<td>37</td>
</tr>
<tr class="even">
<td>848</td>
<td>Active</td>
<td>V182508</td>
<td>2080P0202X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Cardiology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>849</td>
<td>Active</td>
<td>V182509</td>
<td>2080P0203X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Critical Care Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>850</td>
<td>Active</td>
<td>V182510</td>
<td>2080P0204X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Emergency Medicine</td>
<td>37</td>
</tr>
<tr class="odd">
<td>851</td>
<td>Active</td>
<td>V182511</td>
<td>2080P0205X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Endocrinology</td>
<td>37</td>
</tr>
<tr class="even">
<td>852</td>
<td>Active</td>
<td>V182512</td>
<td>2080P0206X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Gastroenterology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>853</td>
<td>Active</td>
<td>V182513</td>
<td>2080P0207X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Hematology-Oncology</td>
<td>37</td>
</tr>
<tr class="even">
<td>854</td>
<td>Active</td>
<td>V182514</td>
<td>2080P0208X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Infectious Diseases</td>
<td>37</td>
</tr>
<tr class="odd">
<td>855</td>
<td>Active</td>
<td>V182515</td>
<td>2080P0210X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Nephrology</td>
<td>37</td>
</tr>
<tr class="even">
<td>856</td>
<td>Active</td>
<td>V182516</td>
<td>2080P0214X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Pulmonology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>857</td>
<td>Active</td>
<td>V182517</td>
<td>2080P0216X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Rheumatology</td>
<td>37</td>
</tr>
<tr class="even">
<td>858</td>
<td>Active</td>
<td>V182518</td>
<td>2080S0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Sports Medicine</td>
<td>37</td>
</tr>
<tr class="odd">
<td>860</td>
<td>Active</td>
<td>V182600</td>
<td>208100000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Physical Medicine and Rehabilitation</td>
<td> </td>
<td>25</td>
</tr>
<tr class="even">
<td>863</td>
<td>Active</td>
<td>V182601</td>
<td>2081P2900X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Physical Medicine and Rehabilitation</td>
<td>Pain Medicine</td>
<td>25</td>
</tr>
<tr class="odd">
<td>862</td>
<td>Active</td>
<td>V182602</td>
<td>2081P0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Physical Medicine and Rehabilitation</td>
<td>Pediatric Rehabilitation Medicine</td>
<td>25</td>
</tr>
<tr class="even">
<td>861</td>
<td>Active</td>
<td>V182603</td>
<td>2081P0004X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Physical Medicine and Rehabilitation</td>
<td>Spinal Cord Injury Medicine</td>
<td>25</td>
</tr>
<tr class="odd">
<td>864</td>
<td>Active</td>
<td>V182604</td>
<td>2081S0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Physical Medicine and Rehabilitation</td>
<td>Sports Medicine</td>
<td>25</td>
</tr>
<tr class="even">
<td>865</td>
<td>Active</td>
<td>V182700</td>
<td>208200000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Plastic Surgery</td>
<td> </td>
<td>24</td>
</tr>
<tr class="odd">
<td>866</td>
<td>Active</td>
<td>V182701</td>
<td>2082S0099X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Plastic Surgery</td>
<td>Plastic Surgery Within the Head and Neck</td>
<td>24</td>
</tr>
<tr class="even">
<td>867</td>
<td>Active</td>
<td>V182702</td>
<td>2082S0105X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Plastic Surgery</td>
<td>Surgery of the Hand</td>
<td>40</td>
</tr>
<tr class="odd">
<td>868</td>
<td>Active</td>
<td>V182801</td>
<td>2083A0100X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Aerospace Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>873</td>
<td>Active</td>
<td>V182802</td>
<td>2083T0002X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Medical Toxicology</td>
<td>84</td>
</tr>
<tr class="odd">
<td>874</td>
<td>Active</td>
<td>V182803</td>
<td>2083X0100X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Occupational Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>870</td>
<td>Active</td>
<td>V182804</td>
<td>2083P0500X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Preventive Medicine/Occupational Environmental Medicine</td>
<td>84</td>
</tr>
<tr class="odd">
<td>871</td>
<td>Active</td>
<td>V182805</td>
<td>2083P0901X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Public Health and General Preventive Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>872</td>
<td>Active</td>
<td>V182806</td>
<td>2083S0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Sports Medicine</td>
<td>84</td>
</tr>
<tr class="odd">
<td>869</td>
<td>Active</td>
<td>V182807</td>
<td>2083P0011X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Undersea and Hyperbaric Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>875</td>
<td>Active</td>
<td>V182901</td>
<td>2084A0401X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Addiction Medicine</td>
<td>86</td>
</tr>
<tr class="odd">
<td>882</td>
<td>Active</td>
<td>V182902</td>
<td>2084P0802X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Addiction Psychiatry</td>
<td>86</td>
</tr>
<tr class="even">
<td>883</td>
<td>Active</td>
<td>V182903</td>
<td>2084P0804X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Child and Adolescent Psychiatry</td>
<td>86</td>
</tr>
<tr class="odd">
<td>879</td>
<td>Active</td>
<td>V182904</td>
<td>2084N0600X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Clinical Neurophysiology</td>
<td>86</td>
</tr>
<tr class="even">
<td>876</td>
<td>Active</td>
<td>V182905</td>
<td>2084F0202X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Forensic Psychiatry</td>
<td>86</td>
</tr>
<tr class="odd">
<td>884</td>
<td>Active</td>
<td>V182906</td>
<td>2084P0805X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Geriatric Psychiatry</td>
<td>86</td>
</tr>
<tr class="even">
<td>880</td>
<td>Active</td>
<td>V182907</td>
<td>2084P0005X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Neurodevelopmental Disabilities</td>
<td>86</td>
</tr>
<tr class="odd">
<td>877</td>
<td>Active</td>
<td>V182908</td>
<td>2084N0400X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Neurology</td>
<td>13</td>
</tr>
<tr class="even">
<td>878</td>
<td>Active</td>
<td>V182909</td>
<td>2084N0402X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Neurology with Special Qualifications in Child Neurology</td>
<td>86</td>
</tr>
<tr class="odd">
<td>885</td>
<td>Active</td>
<td>V182910</td>
<td>2084P2900X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Pain Medicine</td>
<td>86</td>
</tr>
<tr class="even">
<td>881</td>
<td>Active</td>
<td>V182911</td>
<td>2084P0800X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Psychiatry</td>
<td>26</td>
</tr>
<tr class="odd">
<td>886</td>
<td>Active</td>
<td>V182912</td>
<td>2084S0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Sports Medicine</td>
<td>86</td>
</tr>
<tr class="even">
<td>887</td>
<td>Active</td>
<td>V182913</td>
<td>2084V0102X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Psychiatry and Neurology</td>
<td>Vascular Neurology</td>
<td>86</td>
</tr>
<tr class="odd">
<td>888</td>
<td>Active</td>
<td>V183001</td>
<td>2085B0100X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Body Imaging</td>
<td>30</td>
</tr>
<tr class="even">
<td>893</td>
<td>Active</td>
<td>V183002</td>
<td>2085R0202X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Diagnostic Radiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>897</td>
<td>Active</td>
<td>V183003</td>
<td>2085U0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Diagnostic Ultrasound</td>
<td>30</td>
</tr>
<tr class="even">
<td>889</td>
<td>Active</td>
<td>V183004</td>
<td>2085N0700X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Neuroradiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>890</td>
<td>Active</td>
<td>V183005</td>
<td>2085N0904X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Nuclear Radiology</td>
<td>30</td>
</tr>
<tr class="even">
<td>891</td>
<td>Active</td>
<td>V183006</td>
<td>2085P0229X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Pediatric Radiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>892</td>
<td>Active</td>
<td>V183007</td>
<td>2085R0001X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Radiation Oncology</td>
<td>92</td>
</tr>
<tr class="even">
<td>896</td>
<td>Active</td>
<td>V183008</td>
<td>2085R0205X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Radiological Physics</td>
<td>30</td>
</tr>
<tr class="odd">
<td>894</td>
<td>Active</td>
<td>V183009</td>
<td>2085R0203X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Therapeutic Radiology</td>
<td>30</td>
</tr>
<tr class="even">
<td>895</td>
<td>Active</td>
<td>V183010</td>
<td>2085R0204X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Radiology</td>
<td>Vascular and Interventional Radiology</td>
<td>94</td>
</tr>
<tr class="odd">
<td>898</td>
<td>Active</td>
<td>V183100</td>
<td>208600000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td> </td>
<td>2</td>
</tr>
<tr class="even">
<td>901</td>
<td>Active</td>
<td>V183101</td>
<td>2086S0120X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Pediatric Surgery</td>
<td>2</td>
</tr>
<tr class="odd">
<td>902</td>
<td>Active</td>
<td>V183102</td>
<td>2086S0122X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Plastic and Reconstructive Surgery</td>
<td>24</td>
</tr>
<tr class="even">
<td>900</td>
<td>Active</td>
<td>V183103</td>
<td>2086S0105X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgery of the Hand</td>
<td>40</td>
</tr>
<tr class="odd">
<td>899</td>
<td>Active</td>
<td>V183104</td>
<td>2086S0102X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgical Critical Care</td>
<td>2</td>
</tr>
<tr class="even">
<td>905</td>
<td>Active</td>
<td>V183105</td>
<td>2086X0206X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgical Oncology</td>
<td>91</td>
</tr>
<tr class="odd">
<td>903</td>
<td>Active</td>
<td>V183106</td>
<td>2086S0127X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Trauma Surgery</td>
<td>2</td>
</tr>
<tr class="even">
<td>904</td>
<td>Active</td>
<td>V183107</td>
<td>2086S0129X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Vascular Surgery</td>
<td>78</td>
</tr>
<tr class="odd">
<td>909</td>
<td>Active</td>
<td>V183200</td>
<td>208G00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Thoracic Surgery (Cardiothoracic Vascular Surgery)</td>
<td> </td>
<td>33</td>
</tr>
<tr class="even">
<td>746</td>
<td>Active</td>
<td>V183300</td>
<td>204F00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Transplant Surgery</td>
<td> </td>
<td>2</td>
</tr>
<tr class="odd">
<td>906</td>
<td>Active</td>
<td>V183400</td>
<td>208800000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Urology</td>
<td> </td>
<td>34</td>
</tr>
</tbody>
</table>

<span id="_Ref378837660" class="anchor"></span>Table 3: New Person Class Codes—Kernel Patch XU\*8.0\*531

### Patch XU\*8.0\*531

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 3</u> lists all *new* Person Class codes released with Kernel Patch XU\*8.0\*531 (released on 02/17/2010):

<table style="width:100%;">
<caption><p><span id="_Ref488674606" class="anchor"></span>Table 4: Active Person Class Codes—Kernel Patch XU*8.0*671</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>Status</th>
<th>VA Code</th>
<th>NUCC<br />
X12 Code</th>
<th>Provider Type</th>
<th>Classification</th>
<th>Specialty</th>
<th>CMS Specialty Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1153</td>
<td>Active</td>
<td>V081902</td>
<td>174H00000X</td>
<td>Other Service</td>
<td>Health Educator</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1154</td>
<td>Active</td>
<td>V180506</td>
<td>2080C0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Child Abuse Pediatrics</td>
<td>37</td>
</tr>
<tr class="odd">
<td>1155</td>
<td>Active</td>
<td>V170603</td>
<td>374J00000X</td>
<td>Nursing Service Related</td>
<td>Doula</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1156</td>
<td>Active</td>
<td>V170101</td>
<td>374K00000X</td>
<td>Nursing Service Related</td>
<td>Religious Nonmedical Practitioner</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1157</td>
<td>Active</td>
<td>V182415</td>
<td>202K00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Phlebology</td>
<td></td>
<td>22</td>
</tr>
<tr class="even">
<td>1158</td>
<td>Active</td>
<td>V182416</td>
<td>207ZC0006X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Clinical Pathology</td>
<td>22</td>
</tr>
</tbody>
</table>

<span id="_Ref488674606" class="anchor"></span>Table 4: Active Person Class Codes—Kernel Patch XU\*8.0\*671

### Patch XU\*8.0\*671

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 4</u> lists all *Active* Person Class codes released with Kernel Patch XU\*8.0\*671 (released on 08/17/2017):

<table>
<caption><p><span id="_Ref379295371" class="anchor"></span>Table : Updated Person Class Codes—Kernel Patch XU*8.0*531</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 20%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>Status</th>
<th>VA Code</th>
<th>NUCC<br />
X12 Code</th>
<th>Provider Type</th>
<th>Classification</th>
<th>Specialty</th>
<th>CMS Specialty Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>144</td>
<td>Active</td>
<td>V115500</td>
<td>390200000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Resident, Allopathic (includes Interns, Residents, Fellows)</td>
<td></td>
<td>01</td>
</tr>
<tr class="even">
<td>145</td>
<td>Active</td>
<td>V115600</td>
<td>390200000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Resident, Osteopathic (includes Interns, Residents, Fellows)</td>
<td></td>
<td>01</td>
</tr>
<tr class="odd">
<td>180</td>
<td>Active</td>
<td>V120100</td>
<td>211D00000X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Assistant, Podiatric</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>181</td>
<td>Active</td>
<td>V120200</td>
<td>213E00000X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td></td>
<td>48</td>
</tr>
<tr class="odd">
<td>185</td>
<td>Active</td>
<td>V120204</td>
<td>213ES0103X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td>Foot &amp; Ankle Surgery</td>
<td>48</td>
</tr>
<tr class="even">
<td>186</td>
<td>Active</td>
<td>V120205</td>
<td>213ES0131X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td>Foot Surgery</td>
<td>48</td>
</tr>
<tr class="odd">
<td>190</td>
<td>Active</td>
<td>V120209</td>
<td>213EP1101X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td>Primary Podiatric Medicine</td>
<td>48</td>
</tr>
<tr class="even">
<td>191</td>
<td>Active</td>
<td>V120210</td>
<td>213EP0504X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td>Public Medicine</td>
<td>48</td>
</tr>
<tr class="odd">
<td>192</td>
<td>Active</td>
<td>V120211</td>
<td>213ER0200X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td>Radiology</td>
<td>48</td>
</tr>
<tr class="even">
<td>193</td>
<td>Active</td>
<td>V120212</td>
<td>213ES0000X</td>
<td>Podiatric Medicine &amp; Surgery Service Providers</td>
<td>Podiatrist</td>
<td>Sports Medicine</td>
<td>48</td>
</tr>
<tr class="odd">
<td>194</td>
<td>Active</td>
<td>V020000</td>
<td>111N00000X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td></td>
<td>35</td>
</tr>
<tr class="even">
<td>195</td>
<td>Active</td>
<td>V020100</td>
<td>111NI0900X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Internist</td>
<td>35</td>
</tr>
<tr class="odd">
<td>196</td>
<td>Active</td>
<td>V020200</td>
<td>111NN0400X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Neurology</td>
<td>35</td>
</tr>
<tr class="even">
<td>197</td>
<td>Active</td>
<td>V020300</td>
<td>111NN1001X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Nutrition</td>
<td>35</td>
</tr>
<tr class="odd">
<td>198</td>
<td>Active</td>
<td>V020400</td>
<td>111NX0100X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Occupational Health</td>
<td>35</td>
</tr>
<tr class="even">
<td>199</td>
<td>Active</td>
<td>V020500</td>
<td>111NX0800X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Orthopedic</td>
<td>35</td>
</tr>
<tr class="odd">
<td>200</td>
<td>Active</td>
<td>V020600</td>
<td>111NR0200X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Radiology</td>
<td>35</td>
</tr>
<tr class="even">
<td>201</td>
<td>Active</td>
<td>V020700</td>
<td>111NS0005X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Sports Physician</td>
<td>35</td>
</tr>
<tr class="odd">
<td>202</td>
<td>Active</td>
<td>V020800</td>
<td>111NT0100X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Thermography</td>
<td>35</td>
</tr>
<tr class="even">
<td>203</td>
<td>Active</td>
<td>V100000</td>
<td>363A00000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Physician Assistant</td>
<td></td>
<td>97</td>
</tr>
<tr class="odd">
<td>204</td>
<td>Active</td>
<td>V100200</td>
<td>363AS0400X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Physician Assistant</td>
<td>Surgical Technologist</td>
<td>97</td>
</tr>
<tr class="even">
<td>205</td>
<td>Active</td>
<td>V100100</td>
<td>363AM0700X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Physician Assistant</td>
<td>Medical</td>
<td>97</td>
</tr>
<tr class="odd">
<td>207</td>
<td>Active</td>
<td>V030100</td>
<td>126800000X</td>
<td>Dental Providers</td>
<td>Dental Assistant</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>208</td>
<td>Active</td>
<td>V030200</td>
<td>124Q00000X</td>
<td>Dental Providers</td>
<td>Dental Hygienist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>209</td>
<td>Active</td>
<td>V030300</td>
<td>390200000X</td>
<td>Dental Providers</td>
<td>Dental Resident</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>210</td>
<td>Active</td>
<td>V030400</td>
<td>126900000X</td>
<td>Dental Providers</td>
<td>Dental Laboratory Technician</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>211</td>
<td>Active</td>
<td>V030500</td>
<td>122300000X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td></td>
<td>C5</td>
</tr>
<tr class="even">
<td>212</td>
<td>Active</td>
<td>V030501</td>
<td>1223E0200X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Endodontics</td>
<td>C5</td>
</tr>
<tr class="odd">
<td>213</td>
<td>Active</td>
<td>V030502</td>
<td>1223G0001X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>General Practice</td>
<td>C5</td>
</tr>
<tr class="even">
<td>214</td>
<td>Active</td>
<td>V030504</td>
<td>1223S0112X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Oral and Maxillofacial Surgery</td>
<td>19</td>
</tr>
<tr class="odd">
<td>215</td>
<td>Active</td>
<td>V030503</td>
<td>1223P0106X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Oral and Maxillofacial Pathology</td>
<td>C5</td>
</tr>
<tr class="even">
<td>216</td>
<td>Active</td>
<td>V030505</td>
<td>1223X0400X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Orthodontics and Dentofacial Orthopedics</td>
<td>C5</td>
</tr>
<tr class="odd">
<td>217</td>
<td>Active</td>
<td>V030506</td>
<td>1223P0221X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Pediatric Dentistry</td>
<td>C5</td>
</tr>
<tr class="even">
<td>218</td>
<td>Active</td>
<td>V030507</td>
<td>1223P0300X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Periodontics</td>
<td>C5</td>
</tr>
<tr class="odd">
<td>219</td>
<td>Active</td>
<td>V030508</td>
<td>1223P0700X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Prosthodontics</td>
<td>C5</td>
</tr>
<tr class="even">
<td>220</td>
<td>Active</td>
<td>V030509</td>
<td>1223D0001X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Dental Public Health</td>
<td>C5</td>
</tr>
<tr class="odd">
<td>221</td>
<td>Active</td>
<td>V030600</td>
<td>122400000X</td>
<td>Dental Providers</td>
<td>Denturist</td>
<td></td>
<td>19</td>
</tr>
<tr class="even">
<td>223</td>
<td>Active</td>
<td>V060100</td>
<td>156FC0801X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Contact Lens Fitter</td>
<td></td>
</tr>
<tr class="odd">
<td>224</td>
<td>Active</td>
<td>V060200</td>
<td>156FC0800X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Contact Lens</td>
<td></td>
</tr>
<tr class="even">
<td>225</td>
<td>Active</td>
<td>V060300</td>
<td>156FX1700X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Ocularist</td>
<td></td>
</tr>
<tr class="odd">
<td>226</td>
<td>Active</td>
<td>V060400</td>
<td>156FX1101X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Ophthalmic Assistant</td>
<td></td>
</tr>
<tr class="even">
<td>227</td>
<td>Active</td>
<td>V060500</td>
<td>156FX1100X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Ophthalmic</td>
<td></td>
</tr>
<tr class="odd">
<td>228</td>
<td>Active</td>
<td>V060600</td>
<td>156FX1800X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Optician</td>
<td>96</td>
</tr>
<tr class="even">
<td>230</td>
<td>Active</td>
<td>V060800</td>
<td>152W00000X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td></td>
<td>41</td>
</tr>
<tr class="odd">
<td>231</td>
<td>Active</td>
<td>V060802</td>
<td>152WL0500X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Low Vision Rehabilitation</td>
<td>41</td>
</tr>
<tr class="even">
<td>232</td>
<td>Active</td>
<td>V060805</td>
<td>152WS0006X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Sports Vision</td>
<td>41</td>
</tr>
<tr class="odd">
<td>234</td>
<td>Active</td>
<td>V060804</td>
<td>152WP0200X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Pediatrics</td>
<td>41</td>
</tr>
<tr class="even">
<td>235</td>
<td>Active</td>
<td>V060803</td>
<td>152WX0102X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Occupational Vision</td>
<td>41</td>
</tr>
<tr class="odd">
<td>236</td>
<td>Active</td>
<td>V060806</td>
<td>152WV0400X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Vision Therapy</td>
<td>41</td>
</tr>
<tr class="even">
<td>237</td>
<td>Active</td>
<td>V060900</td>
<td>156FX1900X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Orthoptist</td>
<td></td>
</tr>
<tr class="odd">
<td>239</td>
<td>Active</td>
<td>V140100</td>
<td>231H00000X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Audiologist</td>
<td></td>
<td>64</td>
</tr>
<tr class="even">
<td>240</td>
<td>Active</td>
<td>V140200</td>
<td>237600000X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Audiologist-Hearing Aid Fitter</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>241</td>
<td>Active</td>
<td>V140300</td>
<td>237700000X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Hearing Instrument Specialist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>243</td>
<td>Active</td>
<td>V140500</td>
<td>235Z00000X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Speech-Language Pathologist</td>
<td></td>
<td>15</td>
</tr>
<tr class="odd">
<td>244</td>
<td>Active</td>
<td>V140600</td>
<td>2355S0801X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Specialist/Technologist</td>
<td>Speech-Language Assistant</td>
<td></td>
</tr>
<tr class="even">
<td>246</td>
<td>Active</td>
<td>V090100</td>
<td>183500000X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td></td>
<td>87</td>
</tr>
<tr class="odd">
<td>248</td>
<td>Active</td>
<td>V090102</td>
<td>1835N0905X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Nuclear</td>
<td>87</td>
</tr>
<tr class="even">
<td>249</td>
<td>Active</td>
<td>V090103</td>
<td>1835N1003X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Nutrition Support</td>
<td>87</td>
</tr>
<tr class="odd">
<td>250</td>
<td>Active</td>
<td>V090104</td>
<td>1835P1200X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Pharmacotherapy</td>
<td>87</td>
</tr>
<tr class="even">
<td>251</td>
<td>Active</td>
<td>V090105</td>
<td>1835P1300X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Psychiatric</td>
<td>87</td>
</tr>
<tr class="odd">
<td>259</td>
<td>Active</td>
<td>V070101</td>
<td>163WP0809X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Psych/Mental Health, Adult</td>
<td></td>
</tr>
<tr class="even">
<td>260</td>
<td>Active</td>
<td>V070600</td>
<td>163WA2000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Administrator</td>
<td></td>
</tr>
<tr class="odd">
<td>264</td>
<td>Active</td>
<td>V070300</td>
<td>163WM1400X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Nurse Massage Therapist (NMT)</td>
<td></td>
</tr>
<tr class="even">
<td>274</td>
<td>Active</td>
<td>V070900</td>
<td>163W00000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>275</td>
<td>Active</td>
<td>V070901</td>
<td>163WA0400X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Addiction (Substance Use Disorder)</td>
<td></td>
</tr>
<tr class="even">
<td>276</td>
<td>Active</td>
<td>V070902</td>
<td>163WP2201X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Ambulatory Care</td>
<td></td>
</tr>
<tr class="odd">
<td>277</td>
<td>Active</td>
<td>V070903</td>
<td>163WW0101X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Women's Health Care, Ambulatory</td>
<td></td>
</tr>
<tr class="even">
<td>278</td>
<td>Active</td>
<td>V070904</td>
<td>163WC3500X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Cardiac Rehabilitation</td>
<td></td>
</tr>
<tr class="odd">
<td>279</td>
<td>Active</td>
<td>V070905</td>
<td>163WC0400X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Case Management</td>
<td></td>
</tr>
<tr class="even">
<td>280</td>
<td>Active</td>
<td>V070906</td>
<td>163WC1400X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>College Health</td>
<td></td>
</tr>
<tr class="odd">
<td>281</td>
<td>Active</td>
<td>V070907</td>
<td>163WC1500X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Community Health</td>
<td></td>
</tr>
<tr class="even">
<td>282</td>
<td>Active</td>
<td>V070908</td>
<td>163WC2100X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Continence Care</td>
<td></td>
</tr>
<tr class="odd">
<td>283</td>
<td>Active</td>
<td>V070909</td>
<td>163WC0200X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Critical Care Medicine</td>
<td></td>
</tr>
<tr class="even">
<td>284</td>
<td>Active</td>
<td>V070910</td>
<td>163WD0400X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Diabetes Educator</td>
<td></td>
</tr>
<tr class="odd">
<td>285</td>
<td>Active</td>
<td>V070911</td>
<td>163WE0003X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Emergency</td>
<td></td>
</tr>
<tr class="even">
<td>286</td>
<td>Active</td>
<td>V070912</td>
<td>163WE0900X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Enterostomal Therapy</td>
<td></td>
</tr>
<tr class="odd">
<td>287</td>
<td>Active</td>
<td>V070913</td>
<td>163WF0300X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Flight</td>
<td></td>
</tr>
<tr class="even">
<td>288</td>
<td>Active</td>
<td>V070914</td>
<td>163WG0100X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Gastroenterology</td>
<td></td>
</tr>
<tr class="odd">
<td>289</td>
<td>Active</td>
<td>V070915</td>
<td>163WG0000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>General Practice</td>
<td></td>
</tr>
<tr class="even">
<td>290</td>
<td>Active</td>
<td>V070916</td>
<td>163WG0600X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Gerontology</td>
<td></td>
</tr>
<tr class="odd">
<td>291</td>
<td>Active</td>
<td>V070917</td>
<td>163WH0500X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Hemodialysis</td>
<td></td>
</tr>
<tr class="even">
<td>292</td>
<td>Active</td>
<td>V070918</td>
<td>163WX0002X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Obstetric, High-Risk</td>
<td></td>
</tr>
<tr class="odd">
<td>293</td>
<td>Active</td>
<td>V070919</td>
<td>163WH0200X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Home Health</td>
<td>A4</td>
</tr>
<tr class="even">
<td>294</td>
<td>Active</td>
<td>V070920</td>
<td>163WH1000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Hospice</td>
<td>A4</td>
</tr>
<tr class="odd">
<td>295</td>
<td>Active</td>
<td>V070921</td>
<td>163WI0600X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Infection Control</td>
<td></td>
</tr>
<tr class="even">
<td>296</td>
<td>Active</td>
<td>V070922</td>
<td>163WX0003X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Obstetric, Inpatient</td>
<td></td>
</tr>
<tr class="odd">
<td>297</td>
<td>Active</td>
<td>V070923</td>
<td>163WI0500X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Infusion Therapy</td>
<td></td>
</tr>
<tr class="even">
<td>298</td>
<td>Active</td>
<td>V070924</td>
<td>163WL0100X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Lactation Consultant</td>
<td></td>
</tr>
<tr class="odd">
<td>299</td>
<td>Active</td>
<td>V070925</td>
<td>163WN0003X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Neonatal, Low-Risk</td>
<td></td>
</tr>
<tr class="even">
<td>300</td>
<td>Active</td>
<td>V070926</td>
<td>163WM0102X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Maternal Newborn</td>
<td></td>
</tr>
<tr class="odd">
<td>301</td>
<td>Active</td>
<td>V070927</td>
<td>163WM0705X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Medical-Surgical</td>
<td></td>
</tr>
<tr class="even">
<td>302</td>
<td>Active</td>
<td>V070928</td>
<td>163WN0002X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Neonatal Intensive Care</td>
<td></td>
</tr>
<tr class="odd">
<td>303</td>
<td>Active</td>
<td>V070929</td>
<td>163WN0300X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Nephrology</td>
<td></td>
</tr>
<tr class="even">
<td>304</td>
<td>Active</td>
<td>V070930</td>
<td>163WN0800X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Neuroscience</td>
<td></td>
</tr>
<tr class="odd">
<td>305</td>
<td>Active</td>
<td>V070931</td>
<td>163WC1600X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Continuing Education/Staff Development</td>
<td></td>
</tr>
<tr class="even">
<td>306</td>
<td>Active</td>
<td>V070932</td>
<td>163WN1003X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Nutrition Support</td>
<td></td>
</tr>
<tr class="odd">
<td>307</td>
<td>Active</td>
<td>V070933</td>
<td>163WX0106X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Occupational Health</td>
<td></td>
</tr>
<tr class="even">
<td>308</td>
<td>Active</td>
<td>V070934</td>
<td>163WX0200X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Oncology</td>
<td></td>
</tr>
<tr class="odd">
<td>310</td>
<td>Active</td>
<td>V070936</td>
<td>163WX1100X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Ophthalmic</td>
<td></td>
</tr>
<tr class="even">
<td>311</td>
<td>Active</td>
<td>V070937</td>
<td>163WX0800X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Orthopedic</td>
<td></td>
</tr>
<tr class="odd">
<td>312</td>
<td>Active</td>
<td>V070938</td>
<td>163WX1500X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Ostomy Care</td>
<td></td>
</tr>
<tr class="even">
<td>313</td>
<td>Active</td>
<td>V070939</td>
<td>163WX0601X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Otorhinolaryngology &amp; Head-Neck</td>
<td></td>
</tr>
<tr class="odd">
<td>314</td>
<td>Active</td>
<td>V070940</td>
<td>163WP0000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Pain Management</td>
<td></td>
</tr>
<tr class="even">
<td>315</td>
<td>Active</td>
<td>V070941</td>
<td>163WP0200X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Pediatrics</td>
<td></td>
</tr>
<tr class="odd">
<td>316</td>
<td>Active</td>
<td>V070942</td>
<td>163WP0218X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Pediatric Oncology</td>
<td></td>
</tr>
<tr class="even">
<td>317</td>
<td>Active</td>
<td>V070943</td>
<td>163WP1700X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Perinatal</td>
<td></td>
</tr>
<tr class="odd">
<td>318</td>
<td>Active</td>
<td>V070944</td>
<td>163WD1100X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Dialysis, Peritoneal</td>
<td></td>
</tr>
<tr class="even">
<td>319</td>
<td>Active</td>
<td>V070945</td>
<td>163WS0121X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Plastic Surgery</td>
<td></td>
</tr>
<tr class="odd">
<td>321</td>
<td>Active</td>
<td>V070947</td>
<td>163WP0808X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Psych/Mental Health</td>
<td></td>
</tr>
<tr class="even">
<td>322</td>
<td>Active</td>
<td>V070948</td>
<td>163WR0400X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Rehabilitation</td>
<td></td>
</tr>
<tr class="odd">
<td>323</td>
<td>Active</td>
<td>V070949</td>
<td>163WR1000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Reproductive Endocrinology/Infertility</td>
<td></td>
</tr>
<tr class="even">
<td>324</td>
<td>Active</td>
<td>V070950</td>
<td>163WS0200X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>School</td>
<td></td>
</tr>
<tr class="odd">
<td>325</td>
<td>Active</td>
<td>V070951</td>
<td>163WU0100X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Urology</td>
<td></td>
</tr>
<tr class="even">
<td>326</td>
<td>Active</td>
<td>V070952</td>
<td>163WW0000X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Wound Care</td>
<td></td>
</tr>
<tr class="odd">
<td>330</td>
<td>Active</td>
<td>V070804</td>
<td>164W00000X</td>
<td>Nursing Service Providers</td>
<td>Licensed Practical Nurse</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>332</td>
<td>Active</td>
<td>V070805</td>
<td>164X00000X</td>
<td>Nursing Service Providers</td>
<td>Licensed Vocational Nurse</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>333</td>
<td>Active</td>
<td>V070802</td>
<td>390200000X</td>
<td>Nursing Service Providers</td>
<td>Other Nursing Services (Non-R.N.s)</td>
<td>Graduate Nurse</td>
<td></td>
</tr>
<tr class="even">
<td>337</td>
<td>Active</td>
<td>V040300</td>
<td>133N00000X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Nutritionist</td>
<td></td>
<td>71</td>
</tr>
<tr class="odd">
<td>338</td>
<td>Active</td>
<td>V040301</td>
<td>133NN1002X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Nutritionist</td>
<td>Nutrition, Education</td>
<td>71</td>
</tr>
<tr class="even">
<td>339</td>
<td>Active</td>
<td>V040200</td>
<td>136A00000X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Dietetic Technician, Registered</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>340</td>
<td>Active</td>
<td>V040400</td>
<td>133V00000X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Dietitian, Registered</td>
<td></td>
<td>71</td>
</tr>
<tr class="even">
<td>341</td>
<td>Active</td>
<td>V040401</td>
<td>133VN1006X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Dietitian, Registered</td>
<td>Nutrition, Metabolic</td>
<td>71</td>
</tr>
<tr class="odd">
<td>342</td>
<td>Active</td>
<td>V040402</td>
<td>133VN1004X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Dietitian, Registered</td>
<td>Nutrition, Pediatric</td>
<td>71</td>
</tr>
<tr class="even">
<td>343</td>
<td>Active</td>
<td>V040403</td>
<td>133VN1005X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Dietitian, Registered</td>
<td>Nutrition, Renal</td>
<td>71</td>
</tr>
<tr class="odd">
<td>345</td>
<td>Active</td>
<td>V050100</td>
<td>146N00000X</td>
<td>Emergency Medical Service Providers</td>
<td>Emergency Medical Technician, Basic</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>346</td>
<td>Active</td>
<td>V050200</td>
<td>146M00000X</td>
<td>Emergency Medical Service Providers</td>
<td>Emergency Medical Technician, Intermediate</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>347</td>
<td>Active</td>
<td>V050300</td>
<td>146L00000X</td>
<td>Emergency Medical Service Providers</td>
<td>Emergency Medical Technician, Paramedic</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>350</td>
<td>Active</td>
<td>V010400</td>
<td>103T00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td></td>
<td>62</td>
</tr>
<tr class="odd">
<td>351</td>
<td>Active</td>
<td>V010401</td>
<td>103TB0200X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Cognitive &amp; Behavioral</td>
<td>62</td>
</tr>
<tr class="even">
<td>352</td>
<td>Active</td>
<td>V010403</td>
<td>103TC0700X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Clinical</td>
<td>68</td>
</tr>
<tr class="odd">
<td>354</td>
<td>Active</td>
<td>V010404</td>
<td>103TC1900X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Counseling</td>
<td>62</td>
</tr>
<tr class="even">
<td>355</td>
<td>Active</td>
<td>V010405</td>
<td>103TF0000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Family</td>
<td>62</td>
</tr>
<tr class="odd">
<td>356</td>
<td>Active</td>
<td>V010406</td>
<td>103TF0200X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Forensic</td>
<td>62</td>
</tr>
<tr class="even">
<td>357</td>
<td>Active</td>
<td>V010407</td>
<td>103TH0100X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Health Service</td>
<td>62</td>
</tr>
<tr class="odd">
<td>358</td>
<td>Active</td>
<td>V010408</td>
<td>103TS0200X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>School</td>
<td>62</td>
</tr>
<tr class="even">
<td>362</td>
<td>Active</td>
<td>V010200</td>
<td>101Y00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Counselor</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>363</td>
<td>Active</td>
<td>V010201</td>
<td>101YA0400X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Counselor</td>
<td>Addiction (Substance Use Disorder)</td>
<td></td>
</tr>
<tr class="even">
<td>364</td>
<td>Active</td>
<td>V010202</td>
<td>106H00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Marriage &amp; Family Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>365</td>
<td>Active</td>
<td>V010203</td>
<td>101YM0800X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Counselor</td>
<td>Mental Health</td>
<td></td>
</tr>
<tr class="even">
<td>366</td>
<td>Active</td>
<td>V010204</td>
<td>101YP1600X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Counselor</td>
<td>Pastoral</td>
<td></td>
</tr>
<tr class="odd">
<td>367</td>
<td>Active</td>
<td>V010205</td>
<td>101YP2500X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Counselor</td>
<td>Professional</td>
<td></td>
</tr>
<tr class="even">
<td>368</td>
<td>Active</td>
<td>V010206</td>
<td>101YS0200X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Counselor</td>
<td>School</td>
<td></td>
</tr>
<tr class="odd">
<td>369</td>
<td>Active</td>
<td>V010600</td>
<td>104100000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Social Worker</td>
<td></td>
<td>80</td>
</tr>
<tr class="even">
<td>370</td>
<td>Active</td>
<td>V010100</td>
<td>1041C0700X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Social Worker</td>
<td>Clinical</td>
<td>80</td>
</tr>
<tr class="odd">
<td>371</td>
<td>Active</td>
<td>V010500</td>
<td>1041S0200X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Social Worker</td>
<td>School</td>
<td>80</td>
</tr>
<tr class="even">
<td>375</td>
<td>Active</td>
<td>V130506</td>
<td>225B00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Pulmonary Function Technologist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>383</td>
<td>Active</td>
<td>V130300</td>
<td>225100000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td></td>
<td>65</td>
</tr>
<tr class="even">
<td>384</td>
<td>Active</td>
<td>V130301</td>
<td>2251C2600X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Cardiopulmonary</td>
<td>65</td>
</tr>
<tr class="odd">
<td>385</td>
<td>Active</td>
<td>V130302</td>
<td>2251E1300X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Electrophysiology, Clinical</td>
<td>65</td>
</tr>
<tr class="even">
<td>386</td>
<td>Active</td>
<td>V130303</td>
<td>2251G0304X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Geriatrics</td>
<td>65</td>
</tr>
<tr class="odd">
<td>387</td>
<td>Active</td>
<td>V130305</td>
<td>2251N0400X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Neurology</td>
<td>65</td>
</tr>
<tr class="even">
<td>388</td>
<td>Active</td>
<td>V130306</td>
<td>2251X0800X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Orthopedic</td>
<td>65</td>
</tr>
<tr class="odd">
<td>389</td>
<td>Active</td>
<td>V130307</td>
<td>2251P0200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Pediatrics</td>
<td>65</td>
</tr>
<tr class="even">
<td>390</td>
<td>Active</td>
<td>V130309</td>
<td>2251S0007X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Sports</td>
<td>65</td>
</tr>
<tr class="odd">
<td>391</td>
<td>Active</td>
<td>V130304</td>
<td>2251H1200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Hand</td>
<td>65</td>
</tr>
<tr class="even">
<td>392</td>
<td>Active</td>
<td>V130308</td>
<td>225200000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapy Assistant</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>393</td>
<td>Active</td>
<td>V130400</td>
<td>225400000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Rehabilitation Practitioner</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>396</td>
<td>Active</td>
<td>V130405</td>
<td>390200000X</td>
<td>Respiratory, Rehabilitative and Restorative Service Providers</td>
<td>Rehabilitation Practitioner</td>
<td>Rehabilitation Intern</td>
<td></td>
</tr>
<tr class="odd">
<td>398</td>
<td>Active</td>
<td>V130404</td>
<td>225C00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Rehabilitation Counselor</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>399</td>
<td>Active</td>
<td>V130100</td>
<td>225X00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td></td>
<td>67</td>
</tr>
<tr class="odd">
<td>400</td>
<td>Active</td>
<td>V130101</td>
<td>224Z00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapy Assistant</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>402</td>
<td>Active</td>
<td>V130102</td>
<td>225XH1200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Hand</td>
<td>67</td>
</tr>
<tr class="odd">
<td>404</td>
<td>Active</td>
<td>V130201</td>
<td>221700000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Art Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>405</td>
<td>Active</td>
<td>V130202</td>
<td>2255A2300X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Specialist/Technologist</td>
<td>Athletic Trainer</td>
<td></td>
</tr>
<tr class="odd">
<td>406</td>
<td>Active</td>
<td>V130203</td>
<td>225600000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Dance Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>407</td>
<td>Active</td>
<td>V130204</td>
<td>225700000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Massage Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>408</td>
<td>Active</td>
<td>V130205</td>
<td>225A00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Music Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>409</td>
<td>Active</td>
<td>V130206</td>
<td>2255R0406X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Specialist/Technologist</td>
<td>Rehabilitation, Blind</td>
<td></td>
</tr>
<tr class="odd">
<td>410</td>
<td>Active</td>
<td>V130207</td>
<td>225000000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Orthotic Fitter</td>
<td></td>
<td>57</td>
</tr>
<tr class="even">
<td>412</td>
<td>Active</td>
<td>V130209</td>
<td>225800000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Recreation Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>421</td>
<td>Active</td>
<td>V150104</td>
<td>246QL0901X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Laboratory Management, Diplomate</td>
<td></td>
</tr>
<tr class="even">
<td>422</td>
<td>Active</td>
<td>V150105</td>
<td>246QH0401X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Hemapheresis Practitioner</td>
<td></td>
</tr>
<tr class="odd">
<td>423</td>
<td>Active</td>
<td>V150106</td>
<td>246RH0600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Pathology</td>
<td>Histology</td>
<td></td>
</tr>
<tr class="even">
<td>424</td>
<td>Active</td>
<td>V150107</td>
<td>246QH0600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Histology</td>
<td></td>
</tr>
<tr class="odd">
<td>425</td>
<td>Active</td>
<td>V150108</td>
<td>246RM2200X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Pathology</td>
<td>Medical Laboratory</td>
<td></td>
</tr>
<tr class="even">
<td>426</td>
<td>Active</td>
<td>V150109</td>
<td>246QM0706X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Medical Technologist</td>
<td></td>
</tr>
<tr class="odd">
<td>427</td>
<td>Active</td>
<td>V150110</td>
<td>246RP1900X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Pathology</td>
<td>Phlebotomy</td>
<td></td>
</tr>
<tr class="even">
<td>428</td>
<td>Active</td>
<td>V150111</td>
<td>246QB0000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Blood Banking</td>
<td></td>
</tr>
<tr class="odd">
<td>429</td>
<td>Active</td>
<td>V150112</td>
<td>246QC1000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Chemistry</td>
<td></td>
</tr>
<tr class="even">
<td>430</td>
<td>Active</td>
<td>V150113</td>
<td>246QC2700X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Cytotechnology</td>
<td></td>
</tr>
<tr class="odd">
<td>431</td>
<td>Active</td>
<td>V150114</td>
<td>246QH0000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Hematology</td>
<td></td>
</tr>
<tr class="even">
<td>432</td>
<td>Active</td>
<td>V150115</td>
<td>246QM0900X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Microbiology</td>
<td></td>
</tr>
<tr class="odd">
<td>436</td>
<td>Active</td>
<td>V150119</td>
<td>246QI0000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Immunology</td>
<td></td>
</tr>
<tr class="even">
<td>439</td>
<td>Active</td>
<td>V150201</td>
<td>246ZB0301X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Biomedical Engineering</td>
<td></td>
</tr>
<tr class="odd">
<td>440</td>
<td>Active</td>
<td>V150202</td>
<td>2472B0301X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Other</td>
<td>Biomedical Engineering</td>
<td></td>
</tr>
<tr class="even">
<td>447</td>
<td>Active</td>
<td>V150209</td>
<td>2472E0500X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Other</td>
<td>EEG</td>
<td></td>
</tr>
<tr class="odd">
<td>448</td>
<td>Active</td>
<td>V150210</td>
<td>246ZE0500X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>EEG</td>
<td></td>
</tr>
<tr class="even">
<td>449</td>
<td>Active</td>
<td>V150211</td>
<td>246ZE0600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Electroneurodiagnostic</td>
<td></td>
</tr>
<tr class="odd">
<td>450</td>
<td>Active</td>
<td>V150212</td>
<td>246ZG0701X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Graphics Methods</td>
<td></td>
</tr>
<tr class="even">
<td>452</td>
<td>Active</td>
<td>V150214</td>
<td>246ZG1000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Geneticist, Medical (PhD)</td>
<td></td>
</tr>
<tr class="odd">
<td>454</td>
<td>Active</td>
<td>V150216</td>
<td>2472R0900X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Other</td>
<td>Renal Dialysis</td>
<td></td>
</tr>
<tr class="even">
<td>459</td>
<td>Active</td>
<td>V150301</td>
<td>2471C1101X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Cardiovascular-Interventional Technology</td>
<td></td>
</tr>
<tr class="odd">
<td>461</td>
<td>Active</td>
<td>V150303</td>
<td>2472D0500X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Other</td>
<td>Darkroom</td>
<td></td>
</tr>
<tr class="even">
<td>464</td>
<td>Active</td>
<td>V150306</td>
<td>2471S1302X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Sonography</td>
<td></td>
</tr>
<tr class="odd">
<td>466</td>
<td>Active</td>
<td>V150308</td>
<td>2471M2300X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Mammography</td>
<td></td>
</tr>
<tr class="even">
<td>468</td>
<td>Active</td>
<td>V150310</td>
<td>2471N0900X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Nuclear Medicine Technology</td>
<td></td>
</tr>
<tr class="odd">
<td>470</td>
<td>Active</td>
<td>V150312</td>
<td>2471R0002X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Radiation Therapy</td>
<td></td>
</tr>
<tr class="even">
<td>479</td>
<td>Active</td>
<td>V150403</td>
<td>246ZB0302X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Biomedical Photographer</td>
<td></td>
</tr>
<tr class="odd">
<td>480</td>
<td>Active</td>
<td>V150404</td>
<td>246ZB0600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Biostatistician</td>
<td></td>
</tr>
<tr class="even">
<td>482</td>
<td>Active</td>
<td>V150406</td>
<td>246ZA2600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Art, Medical</td>
<td></td>
</tr>
<tr class="odd">
<td>483</td>
<td>Active</td>
<td>V150407</td>
<td>246ZI1000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Illustration, Medical</td>
<td></td>
</tr>
<tr class="even">
<td>490</td>
<td>Active</td>
<td>V150414</td>
<td>2472V0600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Other</td>
<td>Veterinary</td>
<td></td>
</tr>
<tr class="odd">
<td>492</td>
<td>Active</td>
<td>V080100</td>
<td>171100000X</td>
<td>Other Service Providers</td>
<td>Acupuncturist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>493</td>
<td>Active</td>
<td>V080200</td>
<td>172A00000X</td>
<td>Other Service Providers</td>
<td>Driver</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>499</td>
<td>Active</td>
<td>V080500</td>
<td>171WH0202X</td>
<td>Other Service Providers</td>
<td>Contractor</td>
<td>Home Modifications</td>
<td></td>
</tr>
<tr class="even">
<td>501</td>
<td>Active</td>
<td>V080700</td>
<td>175L00000X</td>
<td>Other Service Providers</td>
<td>Homeopath</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>504</td>
<td>Active</td>
<td>V081000</td>
<td>175M00000X</td>
<td>Other Service Providers</td>
<td>Midwife, Lay</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>505</td>
<td>Active</td>
<td>V081100</td>
<td>175F00000X</td>
<td>Other Service Providers</td>
<td>Naturopath</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>512</td>
<td>Active</td>
<td>V010409</td>
<td>103TA0400X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Addiction (Substance Use Disorder)</td>
<td>62</td>
</tr>
<tr class="even">
<td>513</td>
<td>Active</td>
<td>V010410</td>
<td>103TA0700X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Adult Development &amp; Aging</td>
<td>62</td>
</tr>
<tr class="odd">
<td>514</td>
<td>Active</td>
<td>V010411</td>
<td>103TC2200X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Clinical Child &amp; Adolescent</td>
<td>62</td>
</tr>
<tr class="even">
<td>516</td>
<td>Active</td>
<td>V010413</td>
<td>103TE1100X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Exercise &amp; Sports</td>
<td>62</td>
</tr>
<tr class="odd">
<td>518</td>
<td>Active</td>
<td>V010415</td>
<td>103TM1800X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Mental Retardation &amp; Developmental Disabilities</td>
<td>62</td>
</tr>
<tr class="even">
<td>520</td>
<td>Active</td>
<td>V010417</td>
<td>103TP2701X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Group Psychotherapy</td>
<td>62</td>
</tr>
<tr class="odd">
<td>521</td>
<td>Active</td>
<td>V010418</td>
<td>103TR0400X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Rehabilitation</td>
<td>62</td>
</tr>
<tr class="even">
<td>523</td>
<td>Active</td>
<td>V060701</td>
<td>156FX1201X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Optometric Assistant</td>
<td></td>
</tr>
<tr class="odd">
<td>524</td>
<td>Active</td>
<td>V060702</td>
<td>156FX1202X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td>Optometric Technician</td>
<td></td>
</tr>
<tr class="even">
<td>525</td>
<td>Active</td>
<td>V100301</td>
<td>364SA2100X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Acute Care</td>
<td>89</td>
</tr>
<tr class="odd">
<td>526</td>
<td>Active</td>
<td>V100302</td>
<td>364SA2200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Adult Health</td>
<td>89</td>
</tr>
<tr class="even">
<td>527</td>
<td>Active</td>
<td>V100305</td>
<td>364SC0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Critical Care Medicine</td>
<td>89</td>
</tr>
<tr class="odd">
<td>528</td>
<td>Active</td>
<td>V100303</td>
<td>364SC2300X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Chronic Care</td>
<td>89</td>
</tr>
<tr class="even">
<td>529</td>
<td>Active</td>
<td>V100306</td>
<td>364SE0003X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Emergency</td>
<td>89</td>
</tr>
<tr class="odd">
<td>530</td>
<td>Active</td>
<td>V100307</td>
<td>364SE1400X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Ethics</td>
<td>89</td>
</tr>
<tr class="even">
<td>531</td>
<td>Active</td>
<td>V100308</td>
<td>364SF0001X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Family Health</td>
<td>89</td>
</tr>
<tr class="odd">
<td>532</td>
<td>Active</td>
<td>V100311</td>
<td>364SH0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Home Health</td>
<td>89</td>
</tr>
<tr class="even">
<td>533</td>
<td>Active</td>
<td>V100310</td>
<td>364SH1100X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Holistic</td>
<td>89</td>
</tr>
<tr class="odd">
<td>534</td>
<td>Active</td>
<td>V100312</td>
<td>364SI0800X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Informatics</td>
<td>89</td>
</tr>
<tr class="even">
<td>535</td>
<td>Active</td>
<td>V100313</td>
<td>364SL0600X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Long-Term Care</td>
<td>89</td>
</tr>
<tr class="odd">
<td>536</td>
<td>Active</td>
<td>V100315</td>
<td>364SN0000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Neonatal</td>
<td>89</td>
</tr>
<tr class="even">
<td>538</td>
<td>Active</td>
<td>V100317</td>
<td>364SN0800X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Neuroscience</td>
<td>89</td>
</tr>
<tr class="odd">
<td>539</td>
<td>Active</td>
<td>V100321</td>
<td>364SP0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Pediatrics</td>
<td>89</td>
</tr>
<tr class="even">
<td>540</td>
<td>Active</td>
<td>V100324</td>
<td>364SP0808X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health</td>
<td>89</td>
</tr>
<tr class="odd">
<td>541</td>
<td>Active</td>
<td>V100325</td>
<td>364SP0809X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health, Adult</td>
<td>89</td>
</tr>
<tr class="even">
<td>542</td>
<td>Active</td>
<td>V100327</td>
<td>364SP0810X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health, Child &amp; Family</td>
<td>89</td>
</tr>
<tr class="odd">
<td>543</td>
<td>Active</td>
<td>V100328</td>
<td>364SP0811X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health, Chronically Ill</td>
<td>89</td>
</tr>
<tr class="even">
<td>544</td>
<td>Active</td>
<td>V100329</td>
<td>364SP0812X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health, Community</td>
<td>89</td>
</tr>
<tr class="odd">
<td>545</td>
<td>Active</td>
<td>V100330</td>
<td>364SP0813X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health, Geropsychiatric</td>
<td>89</td>
</tr>
<tr class="even">
<td>546</td>
<td>Active</td>
<td>V100322</td>
<td>364SP1700X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Perinatal</td>
<td>89</td>
</tr>
<tr class="odd">
<td>547</td>
<td>Active</td>
<td>V100323</td>
<td>364SP2800X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Perioperative</td>
<td>89</td>
</tr>
<tr class="even">
<td>548</td>
<td>Active</td>
<td>V100331</td>
<td>364SR0400X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Rehabilitation</td>
<td>89</td>
</tr>
<tr class="odd">
<td>550</td>
<td>Active</td>
<td>V100333</td>
<td>364SS0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>School</td>
<td>89</td>
</tr>
<tr class="even">
<td>551</td>
<td>Active</td>
<td>V100334</td>
<td>364ST0500X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Transplantation</td>
<td>89</td>
</tr>
<tr class="odd">
<td>552</td>
<td>Active</td>
<td>V100335</td>
<td>364SW0102X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Women's Health</td>
<td>89</td>
</tr>
<tr class="even">
<td>553</td>
<td>Active</td>
<td>V100318</td>
<td>364SX0106X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Occupational Health</td>
<td>89</td>
</tr>
<tr class="odd">
<td>554</td>
<td>Active</td>
<td>V100319</td>
<td>364SX0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Oncology</td>
<td>89</td>
</tr>
<tr class="even">
<td>555</td>
<td>Active</td>
<td>V100320</td>
<td>364SX0204X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Oncology, Pediatrics</td>
<td>89</td>
</tr>
<tr class="odd">
<td>556</td>
<td>Active</td>
<td>V100601</td>
<td>363LA2100X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Acute Care</td>
<td>50</td>
</tr>
<tr class="even">
<td>557</td>
<td>Active</td>
<td>V100604</td>
<td>363LC0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Critical Care Medicine</td>
<td>50</td>
</tr>
<tr class="odd">
<td>558</td>
<td>Active</td>
<td>V100603</td>
<td>363LC1500X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Community Health</td>
<td>50</td>
</tr>
<tr class="even">
<td>559</td>
<td>Active</td>
<td>V100608</td>
<td>363LN0005X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Neonatal, Critical Care</td>
<td>50</td>
</tr>
<tr class="odd">
<td>560</td>
<td>Active</td>
<td>V100613</td>
<td>363LP0222X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Pediatrics, Critical Care</td>
<td>50</td>
</tr>
<tr class="even">
<td>562</td>
<td>Active</td>
<td>V100616</td>
<td>363LP0808X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Psych/Mental Health</td>
<td>50</td>
</tr>
<tr class="odd">
<td>563</td>
<td>Active</td>
<td>V100614</td>
<td>363LP1700X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Perinatal</td>
<td>50</td>
</tr>
<tr class="even">
<td>564</td>
<td>Active</td>
<td>V100615</td>
<td>363LP2300X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Primary Care</td>
<td>50</td>
</tr>
<tr class="odd">
<td>565</td>
<td>Active</td>
<td>V100618</td>
<td>363LW0102X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Women's Health</td>
<td>50</td>
</tr>
<tr class="even">
<td>566</td>
<td>Active</td>
<td>V100610</td>
<td>363LX0106X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Occupational Health</td>
<td>50</td>
</tr>
<tr class="odd">
<td>567</td>
<td>Active</td>
<td>V070953</td>
<td>163WP0807X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Psych/Mental Health, Child &amp; Adolescent</td>
<td></td>
</tr>
<tr class="even">
<td>568</td>
<td>Active</td>
<td>V081700</td>
<td>176P00000X</td>
<td>Other Service Providers</td>
<td>Funeral Director</td>
<td></td>
<td>59</td>
</tr>
<tr class="odd">
<td>609</td>
<td>Active</td>
<td>V130213</td>
<td>222Z00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Orthotist</td>
<td></td>
<td>55</td>
</tr>
<tr class="even">
<td>610</td>
<td>Active</td>
<td>V130214</td>
<td>224P00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Prosthetist</td>
<td></td>
<td>56</td>
</tr>
<tr class="odd">
<td>612</td>
<td>Active</td>
<td>V130311</td>
<td>2251E1200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Ergonomics</td>
<td>65</td>
</tr>
<tr class="even">
<td>613</td>
<td>Active</td>
<td>V130312</td>
<td>2251H1300X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Physical Therapist</td>
<td>Human Factors</td>
<td>65</td>
</tr>
<tr class="odd">
<td>615</td>
<td>Active</td>
<td>V130406</td>
<td>225CA2400X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Rehabilitation Counselor</td>
<td>Assistive Technology Practitioner</td>
<td></td>
</tr>
<tr class="even">
<td>616</td>
<td>Active</td>
<td>V130407</td>
<td>225CA2500X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Rehabilitation Counselor</td>
<td>Assistive Technology Supplier</td>
<td></td>
</tr>
<tr class="odd">
<td>618</td>
<td>Active</td>
<td>V130105</td>
<td>225XE1200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Ergonomics</td>
<td>67</td>
</tr>
<tr class="even">
<td>619</td>
<td>Active</td>
<td>V130106</td>
<td>225XH1300X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Human Factors</td>
<td>67</td>
</tr>
<tr class="odd">
<td>620</td>
<td>Active</td>
<td>V130107</td>
<td>225XN1300X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Neurorehabilitation</td>
<td>67</td>
</tr>
<tr class="even">
<td>621</td>
<td>Active</td>
<td>V130108</td>
<td>225XP0200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Pediatrics</td>
<td>67</td>
</tr>
<tr class="odd">
<td>622</td>
<td>Active</td>
<td>V130109</td>
<td>225XR0403X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Driving and Community Mobility</td>
<td>67</td>
</tr>
<tr class="even">
<td>623</td>
<td>Active</td>
<td>V130600</td>
<td>226300000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Kinesiotherapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>624</td>
<td>Active</td>
<td>V140101</td>
<td>231HA2400X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Audiologist</td>
<td>Assistive Technology Practitioner</td>
<td>64</td>
</tr>
<tr class="even">
<td>625</td>
<td>Active</td>
<td>V140102</td>
<td>231HA2500X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Audiologist</td>
<td>Assistive Technology Supplier</td>
<td></td>
</tr>
<tr class="odd">
<td>626</td>
<td>Active</td>
<td>V140701</td>
<td>2355A2700X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Specialist/Technologist</td>
<td>Audiology Assistant</td>
<td></td>
</tr>
<tr class="even">
<td>627</td>
<td>Active</td>
<td>V081905</td>
<td>1744P3200X</td>
<td>Other Service Providers</td>
<td>Specialist</td>
<td>Prosthetics Case Management</td>
<td></td>
</tr>
<tr class="odd">
<td>628</td>
<td>Active</td>
<td>V150601</td>
<td>246QL0900X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td>Laboratory Management</td>
<td></td>
</tr>
<tr class="even">
<td>633</td>
<td>Active</td>
<td>V150901</td>
<td>246YC3301X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Health Info</td>
<td>Coding Specialist, Hospital Based</td>
<td></td>
</tr>
<tr class="odd">
<td>634</td>
<td>Active</td>
<td>V150902</td>
<td>246YC3302X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Health Info</td>
<td>Coding Specialist, Physician Office Based</td>
<td></td>
</tr>
<tr class="even">
<td>635</td>
<td>Active</td>
<td>V151001</td>
<td>246ZB0500X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Biochemist</td>
<td></td>
</tr>
<tr class="odd">
<td>637</td>
<td>Active</td>
<td>V151003</td>
<td>246ZN0300X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Nephrology</td>
<td></td>
</tr>
<tr class="even">
<td>639</td>
<td>Active</td>
<td>V150318</td>
<td>2471C3401X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Computed Tomography</td>
<td></td>
</tr>
<tr class="odd">
<td>640</td>
<td>Active</td>
<td>V150319</td>
<td>2471C3402X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Radiography</td>
<td></td>
</tr>
<tr class="even">
<td>642</td>
<td>Active</td>
<td>V150321</td>
<td>2471M1202X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Magnetic Resonance Imaging</td>
<td></td>
</tr>
<tr class="odd">
<td>643</td>
<td>Active</td>
<td>V150322</td>
<td>2471Q0001X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Quality Management</td>
<td></td>
</tr>
<tr class="even">
<td>647</td>
<td>Active</td>
<td>V081800</td>
<td>173000000X</td>
<td>Other Service Providers</td>
<td>Legal Medicine</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>648</td>
<td>Active</td>
<td>V081901</td>
<td>1744G0900X</td>
<td>Other Service Providers</td>
<td>Specialist</td>
<td>Graphics Designer</td>
<td></td>
</tr>
<tr class="even">
<td>649</td>
<td>Active</td>
<td>V081903</td>
<td>1744R1103X</td>
<td>Other Service Providers</td>
<td>Specialist</td>
<td>Research Data Abstracter/Coder</td>
<td></td>
</tr>
<tr class="odd">
<td>650</td>
<td>Active</td>
<td>V081904</td>
<td>1744R1102X</td>
<td>Other Service Providers</td>
<td>Specialist</td>
<td>Research Study</td>
<td></td>
</tr>
<tr class="even">
<td>651</td>
<td>Active</td>
<td>V082001</td>
<td>174MM1900X</td>
<td>Other Service Providers</td>
<td>Veterinarian</td>
<td>Medical Research</td>
<td></td>
</tr>
<tr class="odd">
<td>652</td>
<td>Active</td>
<td>V150903</td>
<td>246YR1600X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Health Info</td>
<td>Registered Record Administrator</td>
<td></td>
</tr>
<tr class="even">
<td>653</td>
<td>Active</td>
<td>V151101</td>
<td>2470A2800X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Health Information</td>
<td>Assistant Record Technician</td>
<td></td>
</tr>
<tr class="odd">
<td>654</td>
<td>Active</td>
<td>V100300</td>
<td>364S00000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td></td>
<td>89</td>
</tr>
<tr class="even">
<td>655</td>
<td>Active</td>
<td>V100304</td>
<td>364SC1501X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Community Health/Public Health</td>
<td>89</td>
</tr>
<tr class="odd">
<td>656</td>
<td>Active</td>
<td>V100309</td>
<td>364SG0600X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Gerontology</td>
<td>89</td>
</tr>
<tr class="even">
<td>657</td>
<td>Active</td>
<td>V100314</td>
<td>364SM0705X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Medical-Surgical</td>
<td>89</td>
</tr>
<tr class="odd">
<td>658</td>
<td>Active</td>
<td>V100326</td>
<td>364SP0807X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Clinical Nurse Specialist</td>
<td>Psych/Mental Health, Child &amp; Adolescent</td>
<td>89</td>
</tr>
<tr class="even">
<td>660</td>
<td>Active</td>
<td>V100500</td>
<td>367500000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Anesthetist, Certified Registered</td>
<td></td>
<td>43</td>
</tr>
<tr class="odd">
<td>661</td>
<td>Active</td>
<td>V100600</td>
<td>363L00000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td></td>
<td>50</td>
</tr>
<tr class="even">
<td>662</td>
<td>Active</td>
<td>V100602</td>
<td>363LA2200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Adult Health</td>
<td>50</td>
</tr>
<tr class="odd">
<td>663</td>
<td>Active</td>
<td>V100605</td>
<td>363LF0000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Family</td>
<td>50</td>
</tr>
<tr class="even">
<td>664</td>
<td>Active</td>
<td>V100606</td>
<td>363LG0600X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Gerontology</td>
<td>50</td>
</tr>
<tr class="odd">
<td>665</td>
<td>Active</td>
<td>V100607</td>
<td>363LN0000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Neonatal</td>
<td>50</td>
</tr>
<tr class="even">
<td>666</td>
<td>Active</td>
<td>V100609</td>
<td>363LX0001X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Obstetrics &amp; Gynecology</td>
<td>50</td>
</tr>
<tr class="odd">
<td>667</td>
<td>Active</td>
<td>V100611</td>
<td>363LP0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>Pediatrics</td>
<td>50</td>
</tr>
<tr class="even">
<td>668</td>
<td>Active</td>
<td>V100617</td>
<td>363LS0200X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Nurse Practitioner</td>
<td>School</td>
<td>50</td>
</tr>
<tr class="odd">
<td>669</td>
<td>Active</td>
<td>V170100</td>
<td>374T00000X</td>
<td>Nursing Service Related Providers</td>
<td>Religious Nonmedical Nursing Personnel</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>670</td>
<td>Active</td>
<td>V170200</td>
<td>374U00000X</td>
<td>Nursing Service Related Providers</td>
<td>Home Health Aide</td>
<td></td>
<td>A4</td>
</tr>
<tr class="odd">
<td>671</td>
<td>Active</td>
<td>V170300</td>
<td>376J00000X</td>
<td>Nursing Service Related Providers</td>
<td>Homemaker</td>
<td></td>
<td>A4</td>
</tr>
<tr class="even">
<td>672</td>
<td>Active</td>
<td>V170400</td>
<td>376K00000X</td>
<td>Nursing Service Related Providers</td>
<td>Nurse's Aide</td>
<td></td>
<td>A4</td>
</tr>
<tr class="odd">
<td>673</td>
<td>Active</td>
<td>V170600</td>
<td>3747P1801X</td>
<td>Nursing Service Related Providers</td>
<td>Technician</td>
<td>Personal Care Attendant</td>
<td></td>
</tr>
<tr class="even">
<td>674</td>
<td>Active</td>
<td>V170500</td>
<td>376G00000X</td>
<td>Nursing Service Related Providers</td>
<td>Nursing Home Administrator</td>
<td></td>
<td>A1</td>
</tr>
<tr class="odd">
<td>675</td>
<td>Active</td>
<td>V010420</td>
<td>103G00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Clinical Neuropsychologist</td>
<td></td>
<td>68</td>
</tr>
<tr class="even">
<td>676</td>
<td>Active</td>
<td>V040102</td>
<td>132700000X</td>
<td>Dietary &amp; Nutritional Service Providers</td>
<td>Dietary Manager</td>
<td></td>
<td>71</td>
</tr>
<tr class="odd">
<td>677</td>
<td>Active</td>
<td>V060201</td>
<td>156F00000X</td>
<td>Eye and Vision Services Providers</td>
<td>Technician/Technologist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>678</td>
<td>Active</td>
<td>V082100</td>
<td>170100000X</td>
<td>Other Service Providers</td>
<td>Medical Genetics, Ph.D. Medical Genetics</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>679</td>
<td>Active</td>
<td>V080501</td>
<td>171W00000X</td>
<td>Other Service Providers</td>
<td>Contractor</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>681</td>
<td>Active</td>
<td>V081900</td>
<td>174400000X</td>
<td>Other Service Providers</td>
<td>Specialist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>682</td>
<td>Active</td>
<td>V082000</td>
<td>174M00000X</td>
<td>Other Service Providers</td>
<td>Veterinarian</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>683</td>
<td>Active</td>
<td>V081001</td>
<td>176B00000X</td>
<td>Other Service Providers</td>
<td>Midwife</td>
<td></td>
<td>42</td>
</tr>
<tr class="odd">
<td>719</td>
<td>Active</td>
<td>V130215</td>
<td>225500000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Specialist/Technologist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>720</td>
<td>Active</td>
<td>V130512</td>
<td>227800000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>721</td>
<td>Active</td>
<td>V130513</td>
<td>227900000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>722</td>
<td>Active</td>
<td>V140601</td>
<td>235500000X</td>
<td>Speech, Language and Hearing Service Providers</td>
<td>Specialist/Technologist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>723</td>
<td>Active</td>
<td>V150121</td>
<td>246Q00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Pathology</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>724</td>
<td>Active</td>
<td>V150122</td>
<td>246R00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Pathology</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>726</td>
<td>Active</td>
<td>V150220</td>
<td>246W00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Cardiology</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>727</td>
<td>Active</td>
<td>V150900</td>
<td>246Y00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Health Info</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>728</td>
<td>Active</td>
<td>V151000</td>
<td>246Z00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>729</td>
<td>Active</td>
<td>V151100</td>
<td>247000000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Health Information</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>730</td>
<td>Active</td>
<td>V150324</td>
<td>247100000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>731</td>
<td>Active</td>
<td>V150221</td>
<td>247200000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Technician, Other</td>
<td></td>
<td>75</td>
</tr>
<tr class="odd">
<td>733</td>
<td>Active</td>
<td>V100401</td>
<td>367A00000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Advanced Practice Midwife</td>
<td></td>
<td>42</td>
</tr>
<tr class="even">
<td>734</td>
<td>Active</td>
<td>V170601</td>
<td>374700000X</td>
<td>Nursing Service Related Providers</td>
<td>Technician</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>735</td>
<td>Active</td>
<td>V010421</td>
<td>103TP0814X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Psychoanalysis</td>
<td>62</td>
</tr>
<tr class="even">
<td>736</td>
<td>Active</td>
<td>V030510</td>
<td>1223X0008X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Oral and Maxillofacial Radiology</td>
<td>C5</td>
</tr>
<tr class="odd">
<td>737</td>
<td>Active</td>
<td>V050500</td>
<td>146D00000X</td>
<td>Emergency Medical Service Providers</td>
<td>Personal Emergency Response Attendant</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>738</td>
<td>Active</td>
<td>V060807</td>
<td>152WC0802X</td>
<td>Eye and Vision Services Providers</td>
<td>Optometrist</td>
<td>Corneal and Contact Management</td>
<td>41</td>
</tr>
<tr class="odd">
<td>739</td>
<td>Active</td>
<td>V070807</td>
<td>167G00000X</td>
<td>Nursing Service Providers</td>
<td>Licensed Psychiatric Technician</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>740</td>
<td>Active</td>
<td>V080502</td>
<td>171WV0202X</td>
<td>Other Service Providers</td>
<td>Contractor</td>
<td>Vehicle Modifications</td>
<td></td>
</tr>
<tr class="odd">
<td>742</td>
<td>Active</td>
<td>V090300</td>
<td>183700000X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacy Technician</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>743</td>
<td>Active</td>
<td>V181600</td>
<td>204C00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Neuromusculoskeletal Medicine, Sports Medicine</td>
<td></td>
<td>12</td>
</tr>
<tr class="odd">
<td>744</td>
<td>Active</td>
<td>V181500</td>
<td>204D00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Neuromusculoskeletal Medicine &amp; OMM</td>
<td></td>
<td>12</td>
</tr>
<tr class="even">
<td>745</td>
<td>Active</td>
<td>V182000</td>
<td>204E00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Oral &amp; Maxillofacial Surgery</td>
<td></td>
<td>85</td>
</tr>
<tr class="odd">
<td>746</td>
<td>Active</td>
<td>V183300</td>
<td>204F00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Transplant Surgery</td>
<td></td>
<td>02</td>
</tr>
<tr class="even">
<td>747</td>
<td>Active</td>
<td>V180100</td>
<td>207K00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Allergy &amp; Immunology</td>
<td></td>
<td>03</td>
</tr>
<tr class="odd">
<td>748</td>
<td>Active</td>
<td>V180101</td>
<td>207KA0200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Allergy &amp; Immunology</td>
<td>Allergy</td>
<td>03</td>
</tr>
<tr class="even">
<td>749</td>
<td>Active</td>
<td>V180102</td>
<td>207KI0005X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Allergy &amp; Immunology</td>
<td>Clinical &amp; Laboratory Immunology</td>
<td>03</td>
</tr>
<tr class="odd">
<td>750</td>
<td>Active</td>
<td>V180200</td>
<td>207L00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td></td>
<td>05</td>
</tr>
<tr class="even">
<td>751</td>
<td>Active</td>
<td>V180201</td>
<td>207LA0401X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Addiction Medicine</td>
<td>05</td>
</tr>
<tr class="odd">
<td>752</td>
<td>Active</td>
<td>V180202</td>
<td>207LC0200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Critical Care Medicine</td>
<td>05</td>
</tr>
<tr class="even">
<td>753</td>
<td>Active</td>
<td>V180203</td>
<td>207LP2900X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Pain Medicine</td>
<td>05</td>
</tr>
<tr class="odd">
<td>754</td>
<td>Active</td>
<td>V180500</td>
<td>207N00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Dermatology</td>
<td></td>
<td>07</td>
</tr>
<tr class="even">
<td>755</td>
<td>Active</td>
<td>V180504</td>
<td>207ND0101X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Dermatology</td>
<td>MOHS-Micrographic Surgery</td>
<td>07</td>
</tr>
<tr class="odd">
<td>756</td>
<td>Active</td>
<td>V180503</td>
<td>207ND0900X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Dermatopathology</td>
<td>07</td>
</tr>
<tr class="even">
<td>757</td>
<td>Active</td>
<td>V180501</td>
<td>207NI0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Clinical &amp; Laboratory Dermatological Immunology</td>
<td>07</td>
</tr>
<tr class="odd">
<td>758</td>
<td>Active</td>
<td>V180505</td>
<td>207NP0225X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Pediatric Dermatology</td>
<td>07</td>
</tr>
<tr class="even">
<td>759</td>
<td>Active</td>
<td>V180502</td>
<td>207NS0135X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Dermatology</td>
<td>Procedural Dermatology</td>
<td>07</td>
</tr>
<tr class="odd">
<td>760</td>
<td>Active</td>
<td>V180600</td>
<td>207P00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td></td>
<td>93</td>
</tr>
<tr class="even">
<td>761</td>
<td>Active</td>
<td>V180601</td>
<td>207PE0004X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Emergency Medical Services</td>
<td>93</td>
</tr>
<tr class="odd">
<td>762</td>
<td>Active</td>
<td>V180605</td>
<td>207PE0005X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Undersea and Hyperbaric Medicine</td>
<td>93</td>
</tr>
<tr class="even">
<td>763</td>
<td>Active</td>
<td>V180603</td>
<td>207PP0204X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Pediatric Emergency Medicine</td>
<td>93</td>
</tr>
<tr class="odd">
<td>764</td>
<td>Active</td>
<td>V180604</td>
<td>207PS0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Sports Medicine</td>
<td>93</td>
</tr>
<tr class="even">
<td>765</td>
<td>Active</td>
<td>V180602</td>
<td>207PT0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Medical Toxicology</td>
<td>93</td>
</tr>
<tr class="odd">
<td>766</td>
<td>Active</td>
<td>V180700</td>
<td>207Q00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td></td>
<td>08</td>
</tr>
<tr class="even">
<td>767</td>
<td>Active</td>
<td>V180702</td>
<td>207QA0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Adolescent Medicine</td>
<td>08</td>
</tr>
<tr class="odd">
<td>768</td>
<td>Active</td>
<td>V180701</td>
<td>207QA0401X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Addiction Medicine</td>
<td>08</td>
</tr>
<tr class="even">
<td>769</td>
<td>Active</td>
<td>V180703</td>
<td>207QA0505X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Adult Medicine</td>
<td>08</td>
</tr>
<tr class="odd">
<td>770</td>
<td>Active</td>
<td>V180704</td>
<td>207QG0300X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Geriatric Medicine</td>
<td>08</td>
</tr>
<tr class="even">
<td>771</td>
<td>Active</td>
<td>V180705</td>
<td>207QS0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Sports Medicine</td>
<td>08</td>
</tr>
<tr class="odd">
<td>772</td>
<td>Active</td>
<td>V181000</td>
<td>207R00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td></td>
<td>11</td>
</tr>
<tr class="even">
<td>773</td>
<td>Active</td>
<td>V181002</td>
<td>207RA0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Adolescent Medicine</td>
<td>11</td>
</tr>
<tr class="odd">
<td>774</td>
<td>Active</td>
<td>V181003</td>
<td>207RA0201X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Allergy &amp; Immunology</td>
<td>11</td>
</tr>
<tr class="even">
<td>775</td>
<td>Active</td>
<td>V181001</td>
<td>207RA0401X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Addiction Medicine</td>
<td>11</td>
</tr>
<tr class="odd">
<td>776</td>
<td>Active</td>
<td>V181004</td>
<td>207RC0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Cardiovascular Disease</td>
<td>06</td>
</tr>
<tr class="even">
<td>777</td>
<td>Active</td>
<td>V181006</td>
<td>207RC0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Clinical Cardiac Electrophysiology</td>
<td>21</td>
</tr>
<tr class="odd">
<td>778</td>
<td>Active</td>
<td>V181007</td>
<td>207RC0200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Critical Care Medicine</td>
<td>81</td>
</tr>
<tr class="even">
<td>779</td>
<td>Active</td>
<td>V181008</td>
<td>207RE0101X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Endocrinology, Diabetes &amp; Metabolism</td>
<td>46</td>
</tr>
<tr class="odd">
<td>780</td>
<td>Active</td>
<td>V181009</td>
<td>207RG0100X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Gastroenterology</td>
<td>10</td>
</tr>
<tr class="even">
<td>781</td>
<td>Active</td>
<td>V181010</td>
<td>207RG0300X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Geriatric Medicine</td>
<td>38</td>
</tr>
<tr class="odd">
<td>782</td>
<td>Active</td>
<td>V181011</td>
<td>207RH0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hematology</td>
<td>82</td>
</tr>
<tr class="even">
<td>783</td>
<td>Active</td>
<td>V181012</td>
<td>207RH0003X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hematology &amp; Oncology</td>
<td>83</td>
</tr>
<tr class="odd">
<td>784</td>
<td>Active</td>
<td>V181005</td>
<td>207RI0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Clinical &amp; Laboratory Immunology</td>
<td>11</td>
</tr>
<tr class="even">
<td>785</td>
<td>Active</td>
<td>V181013</td>
<td>207RI0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hepatology</td>
<td>11</td>
</tr>
<tr class="odd">
<td>786</td>
<td>Active</td>
<td>V181015</td>
<td>207RI0011X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Interventional Cardiology</td>
<td>C3</td>
</tr>
<tr class="even">
<td>787</td>
<td>Active</td>
<td>V181014</td>
<td>207RI0200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Infectious Disease</td>
<td>44</td>
</tr>
<tr class="odd">
<td>788</td>
<td>Active</td>
<td>V181016</td>
<td>207RM1200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Magnetic Resonance Imaging (MRI)</td>
<td>11</td>
</tr>
<tr class="even">
<td>789</td>
<td>Active</td>
<td>V181018</td>
<td>207RN0300X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Nephrology</td>
<td>39</td>
</tr>
<tr class="odd">
<td>790</td>
<td>Active</td>
<td>V181019</td>
<td>207RP1001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Pulmonary Disease</td>
<td>29</td>
</tr>
<tr class="even">
<td>791</td>
<td>Active</td>
<td>V181020</td>
<td>207RR0500X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Rheumatology</td>
<td>66</td>
</tr>
<tr class="odd">
<td>792</td>
<td>Active</td>
<td>V181021</td>
<td>207RS0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Sports Medicine</td>
<td>11</td>
</tr>
<tr class="even">
<td>793</td>
<td>Active</td>
<td>V181017</td>
<td>207RX0202X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Medical Oncology</td>
<td>90</td>
</tr>
<tr class="odd">
<td>794</td>
<td>Active</td>
<td>V181301</td>
<td>207SC0300X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Cytogenetic</td>
<td></td>
</tr>
<tr class="even">
<td>795</td>
<td>Active</td>
<td>V181302</td>
<td>207SG0201X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Genetics (M.D.)</td>
<td></td>
</tr>
<tr class="odd">
<td>796</td>
<td>Active</td>
<td>V181200</td>
<td>207SG0202X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Biochemical Genetics</td>
<td></td>
</tr>
<tr class="even">
<td>797</td>
<td>Active</td>
<td>V181303</td>
<td>207SG0203X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Clinical Molecular Genetics</td>
<td></td>
</tr>
<tr class="odd">
<td>798</td>
<td>Active</td>
<td>V181305</td>
<td>207SG0205X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Ph.D. Medical Genetics</td>
<td></td>
</tr>
<tr class="even">
<td>799</td>
<td>Active</td>
<td>V181304</td>
<td>207SM0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Medical Genetics</td>
<td>Molecular Genetic Pathology</td>
<td></td>
</tr>
<tr class="odd">
<td>800</td>
<td>Active</td>
<td>V181400</td>
<td>207T00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Neurological Surgery</td>
<td></td>
<td>14</td>
</tr>
<tr class="even">
<td>801</td>
<td>Active</td>
<td>V181700</td>
<td>207U00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td></td>
<td>36</td>
</tr>
<tr class="odd">
<td>802</td>
<td>Active</td>
<td>V181702</td>
<td>207UN0901X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td>Nuclear Cardiology</td>
<td>36</td>
</tr>
<tr class="even">
<td>803</td>
<td>Active</td>
<td>V181703</td>
<td>207UN0902X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td>Nuclear Imaging &amp; Therapy</td>
<td>36</td>
</tr>
<tr class="odd">
<td>804</td>
<td>Active</td>
<td>V181701</td>
<td>207UN0903X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Nuclear Medicine</td>
<td>In Vivo &amp; In Vitro Nuclear Medicine</td>
<td>36</td>
</tr>
<tr class="even">
<td>805</td>
<td>Active</td>
<td>V181800</td>
<td>207V00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td></td>
<td>16</td>
</tr>
<tr class="odd">
<td>806</td>
<td>Active</td>
<td>V181801</td>
<td>207VC0200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Critical Care Medicine</td>
<td>16</td>
</tr>
<tr class="even">
<td>807</td>
<td>Active</td>
<td>V181806</td>
<td>207VE0102X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Reproductive Endocrinology</td>
<td>16</td>
</tr>
<tr class="odd">
<td>808</td>
<td>Active</td>
<td>V181803</td>
<td>207VG0400X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Gynecology</td>
<td>16</td>
</tr>
<tr class="even">
<td>809</td>
<td>Active</td>
<td>V181804</td>
<td>207VM0101X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Maternal &amp; Fetal Medicine</td>
<td>16</td>
</tr>
<tr class="odd">
<td>810</td>
<td>Active</td>
<td>V181805</td>
<td>207VX0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Obstetrics</td>
<td>16</td>
</tr>
<tr class="even">
<td>811</td>
<td>Active</td>
<td>V181802</td>
<td>207VX0201X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Gynecologic Oncology</td>
<td>16</td>
</tr>
<tr class="odd">
<td>812</td>
<td>Active</td>
<td>V181900</td>
<td>207W00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td></td>
<td>18</td>
</tr>
<tr class="even">
<td>813</td>
<td>Active</td>
<td>V182100</td>
<td>207X00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td></td>
<td>20</td>
</tr>
<tr class="odd">
<td>814</td>
<td>Active</td>
<td>V182103</td>
<td>207XS0106X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Hand Surgery</td>
<td>40</td>
</tr>
<tr class="even">
<td>815</td>
<td>Active</td>
<td>V182101</td>
<td>207XS0114X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Adult Reconstructive Orthopaedic Surgery</td>
<td>20</td>
</tr>
<tr class="odd">
<td>816</td>
<td>Active</td>
<td>V182104</td>
<td>207XS0117X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Orthopaedic Surgery of the Spine</td>
<td>20</td>
</tr>
<tr class="even">
<td>817</td>
<td>Active</td>
<td>V182102</td>
<td>207XX0004X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Foot and Ankle Surgery</td>
<td>20</td>
</tr>
<tr class="odd">
<td>818</td>
<td>Active</td>
<td>V182106</td>
<td>207XX0005X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Sports Medicine</td>
<td>20</td>
</tr>
<tr class="even">
<td>819</td>
<td>Active</td>
<td>V182105</td>
<td>207XX0801X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Orthopaedic Trauma</td>
<td>20</td>
</tr>
<tr class="odd">
<td>820</td>
<td>Active</td>
<td>V182200</td>
<td>207Y00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td></td>
<td>04</td>
</tr>
<tr class="even">
<td>821</td>
<td>Active</td>
<td>V182205</td>
<td>207YP0228X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Pediatric Otolaryngology</td>
<td>04</td>
</tr>
<tr class="odd">
<td>822</td>
<td>Active</td>
<td>V182201</td>
<td>207YS0123X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Facial Plastic Surgery</td>
<td>04</td>
</tr>
<tr class="even">
<td>823</td>
<td>Active</td>
<td>V182206</td>
<td>207YX0007X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Plastic Surgery within the Head &amp; Neck</td>
<td>04</td>
</tr>
<tr class="odd">
<td>824</td>
<td>Active</td>
<td>V182202</td>
<td>207YX0602X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Otolaryngic Allergy</td>
<td>04</td>
</tr>
<tr class="even">
<td>825</td>
<td>Active</td>
<td>V182204</td>
<td>207YX0901X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Otology &amp; Neurotology</td>
<td>04</td>
</tr>
<tr class="odd">
<td>826</td>
<td>Active</td>
<td>V182203</td>
<td>207YX0905X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Otolaryngology/Facial Plastic Surgery</td>
<td>04</td>
</tr>
<tr class="even">
<td>827</td>
<td>Active</td>
<td>V182403</td>
<td>207ZB0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Blood Banking &amp; Transfusion Medicine</td>
<td>22</td>
</tr>
<tr class="odd">
<td>828</td>
<td>Active</td>
<td>V182406</td>
<td>207ZC0500X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Cytopathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>829</td>
<td>Active</td>
<td>V182407</td>
<td>207ZD0900X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Dermatopathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>830</td>
<td>Active</td>
<td>V182408</td>
<td>207ZF0201X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Forensic Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>831</td>
<td>Active</td>
<td>V182409</td>
<td>207ZH0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Hematology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>832</td>
<td>Active</td>
<td>V182410</td>
<td>207ZI0100X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Immunopathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>833</td>
<td>Active</td>
<td>V182411</td>
<td>207ZM0300X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Medical Microbiology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>834</td>
<td>Active</td>
<td>V182413</td>
<td>207ZN0500X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Neuropathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>835</td>
<td>Active</td>
<td>V182412</td>
<td>207ZP0007X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Molecular Genetic Pathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>836</td>
<td>Active</td>
<td>V182401</td>
<td>207ZP0101X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Anatomic Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>837</td>
<td>Active</td>
<td>V182402</td>
<td>207ZP0102X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Anatomic Pathology &amp; Clinical Pathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>838</td>
<td>Active</td>
<td>V182404</td>
<td>207ZP0104X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Chemical Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>839</td>
<td>Active</td>
<td>V182405</td>
<td>207ZP0105X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Clinical Pathology/Laboratory Medicine</td>
<td>22</td>
</tr>
<tr class="odd">
<td>840</td>
<td>Active</td>
<td>V182414</td>
<td>207ZP0213X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Pediatric Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>841</td>
<td>Active</td>
<td>V182500</td>
<td>208000000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td></td>
<td>37</td>
</tr>
<tr class="odd">
<td>842</td>
<td>Active</td>
<td>V182501</td>
<td>2080A0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Adolescent Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>843</td>
<td>Active</td>
<td>V182502</td>
<td>2080I0007X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Clinical &amp; Laboratory Immunology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>844</td>
<td>Active</td>
<td>V182505</td>
<td>2080N0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Neonatal-Perinatal Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>845</td>
<td>Active</td>
<td>V182503</td>
<td>2080P0006X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Developmental - Behavioral Pediatrics</td>
<td>37</td>
</tr>
<tr class="odd">
<td>846</td>
<td>Active</td>
<td>V182506</td>
<td>2080P0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Neurodevelopmental Disabilities</td>
<td>37</td>
</tr>
<tr class="even">
<td>847</td>
<td>Active</td>
<td>V182507</td>
<td>2080P0201X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Allergy/Immunology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>848</td>
<td>Active</td>
<td>V182508</td>
<td>2080P0202X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Cardiology</td>
<td>37</td>
</tr>
<tr class="even">
<td>849</td>
<td>Active</td>
<td>V182509</td>
<td>2080P0203X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Critical Care Medicine</td>
<td>37</td>
</tr>
<tr class="odd">
<td>850</td>
<td>Active</td>
<td>V182510</td>
<td>2080P0204X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Emergency Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>851</td>
<td>Active</td>
<td>V182511</td>
<td>2080P0205X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Endocrinology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>852</td>
<td>Active</td>
<td>V182512</td>
<td>2080P0206X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Gastroenterology</td>
<td>37</td>
</tr>
<tr class="even">
<td>853</td>
<td>Active</td>
<td>V182513</td>
<td>2080P0207X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Hematology-Oncology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>854</td>
<td>Active</td>
<td>V182514</td>
<td>2080P0208X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Infectious Diseases</td>
<td>37</td>
</tr>
<tr class="even">
<td>855</td>
<td>Active</td>
<td>V182515</td>
<td>2080P0210X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Nephrology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>856</td>
<td>Active</td>
<td>V182516</td>
<td>2080P0214X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Pulmonology</td>
<td>37</td>
</tr>
<tr class="even">
<td>857</td>
<td>Active</td>
<td>V182517</td>
<td>2080P0216X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Rheumatology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>858</td>
<td>Active</td>
<td>V182522</td>
<td>2080S0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Sports Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>859</td>
<td>Active</td>
<td>V182504</td>
<td>2080T0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Medical Toxicology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>860</td>
<td>Active</td>
<td>V182600</td>
<td>208100000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td></td>
<td>25</td>
</tr>
<tr class="even">
<td>861</td>
<td>Active</td>
<td>V182603</td>
<td>2081P0004X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Spinal Cord Injury Medicine</td>
<td>25</td>
</tr>
<tr class="odd">
<td>862</td>
<td>Active</td>
<td>V182602</td>
<td>2081P0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Pediatric Rehabilitation Medicine</td>
<td>25</td>
</tr>
<tr class="even">
<td>863</td>
<td>Active</td>
<td>V182601</td>
<td>2081P2900X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Pain Medicine</td>
<td>25</td>
</tr>
<tr class="odd">
<td>864</td>
<td>Active</td>
<td>V182604</td>
<td>2081S0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Sports Medicine</td>
<td>25</td>
</tr>
<tr class="even">
<td>865</td>
<td>Active</td>
<td>V182700</td>
<td>208200000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Plastic Surgery</td>
<td></td>
<td>24</td>
</tr>
<tr class="odd">
<td>866</td>
<td>Active</td>
<td>V182701</td>
<td>2082S0099X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Plastic Surgery</td>
<td>Plastic Surgery Within the Head and Neck</td>
<td>24</td>
</tr>
<tr class="even">
<td>867</td>
<td>Active</td>
<td>V182702</td>
<td>2082S0105X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Plastic Surgery</td>
<td>Surgery of the Hand</td>
<td>40</td>
</tr>
<tr class="odd">
<td>868</td>
<td>Active</td>
<td>V182801</td>
<td>2083A0100X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Aerospace Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>869</td>
<td>Active</td>
<td>V182807</td>
<td>2083P0011X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Undersea and Hyperbaric Medicine</td>
<td>84</td>
</tr>
<tr class="odd">
<td>870</td>
<td>Active</td>
<td>V182804</td>
<td>2083P0500X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Preventive Medicine/Occupational Environmental Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>871</td>
<td>Active</td>
<td>V182805</td>
<td>2083P0901X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Public Health &amp; General Preventive Medicine</td>
<td>84</td>
</tr>
<tr class="odd">
<td>872</td>
<td>Active</td>
<td>V182806</td>
<td>2083S0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Sports Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>873</td>
<td>Active</td>
<td>V182802</td>
<td>2083T0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Medical Toxicology</td>
<td>84</td>
</tr>
<tr class="odd">
<td>874</td>
<td>Active</td>
<td>V182803</td>
<td>2083X0100X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Occupational Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>875</td>
<td>Active</td>
<td>V182901</td>
<td>2084A0401X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Addiction Medicine</td>
<td>86</td>
</tr>
<tr class="odd">
<td>876</td>
<td>Active</td>
<td>V182905</td>
<td>2084F0202X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Forensic Psychiatry</td>
<td>86</td>
</tr>
<tr class="even">
<td>877</td>
<td>Active</td>
<td>V182908</td>
<td>2084N0400X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Neurology</td>
<td>13</td>
</tr>
<tr class="odd">
<td>878</td>
<td>Active</td>
<td>V182909</td>
<td>2084N0402X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Neurology with Special Qualifications in Child Neurology</td>
<td>86</td>
</tr>
<tr class="even">
<td>879</td>
<td>Active</td>
<td>V182904</td>
<td>2084N0600X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Clinical Neurophysiology</td>
<td>86</td>
</tr>
<tr class="odd">
<td>880</td>
<td>Active</td>
<td>V182907</td>
<td>2084P0005X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Neurodevelopmental Disabilities</td>
<td>86</td>
</tr>
<tr class="even">
<td>881</td>
<td>Active</td>
<td>V182911</td>
<td>2084P0800X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Psychiatry</td>
<td>26</td>
</tr>
<tr class="odd">
<td>882</td>
<td>Active</td>
<td>V182902</td>
<td>2084P0802X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Addiction Psychiatry</td>
<td>86</td>
</tr>
<tr class="even">
<td>883</td>
<td>Active</td>
<td>V182903</td>
<td>2084P0804X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Child &amp; Adolescent Psychiatry</td>
<td>86</td>
</tr>
<tr class="odd">
<td>884</td>
<td>Active</td>
<td>V182906</td>
<td>2084P0805X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Geriatric Psychiatry</td>
<td>86</td>
</tr>
<tr class="even">
<td>885</td>
<td>Active</td>
<td>V182910</td>
<td>2084P2900X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Pain Medicine</td>
<td>86</td>
</tr>
<tr class="odd">
<td>886</td>
<td>Active</td>
<td>V182912</td>
<td>2084S0010X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Sports Medicine</td>
<td>86</td>
</tr>
<tr class="even">
<td>887</td>
<td>Active</td>
<td>V182913</td>
<td>2084V0102X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Vascular Neurology</td>
<td>86</td>
</tr>
<tr class="odd">
<td>888</td>
<td>Active</td>
<td>V183001</td>
<td>2085B0100X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Body Imaging</td>
<td>30</td>
</tr>
<tr class="even">
<td>889</td>
<td>Active</td>
<td>V183004</td>
<td>2085N0700X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Neuroradiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>890</td>
<td>Active</td>
<td>V183005</td>
<td>2085N0904X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Nuclear Radiology</td>
<td>30</td>
</tr>
<tr class="even">
<td>891</td>
<td>Active</td>
<td>V183006</td>
<td>2085P0229X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Pediatric Radiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>892</td>
<td>Active</td>
<td>V183007</td>
<td>2085R0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Radiation Oncology</td>
<td>92</td>
</tr>
<tr class="even">
<td>893</td>
<td>Active</td>
<td>V183002</td>
<td>2085R0202X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Diagnostic Radiology</td>
<td>30</td>
</tr>
<tr class="odd">
<td>894</td>
<td>Active</td>
<td>V183009</td>
<td>2085R0203X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Therapeutic Radiology</td>
<td>30</td>
</tr>
<tr class="even">
<td>895</td>
<td>Active</td>
<td>V183010</td>
<td>2085R0204X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Vascular &amp; Interventional Radiology</td>
<td>94</td>
</tr>
<tr class="odd">
<td>896</td>
<td>Active</td>
<td>V183008</td>
<td>2085R0205X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Radiological Physics</td>
<td>30</td>
</tr>
<tr class="even">
<td>897</td>
<td>Active</td>
<td>V183003</td>
<td>2085U0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Diagnostic Ultrasound</td>
<td>30</td>
</tr>
<tr class="odd">
<td>898</td>
<td>Active</td>
<td>V183100</td>
<td>208600000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td></td>
<td>02</td>
</tr>
<tr class="even">
<td>899</td>
<td>Active</td>
<td>V183104</td>
<td>2086S0102X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgical Critical Care</td>
<td>02</td>
</tr>
<tr class="odd">
<td>900</td>
<td>Active</td>
<td>V183103</td>
<td>2086S0105X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgery of the Hand</td>
<td>40</td>
</tr>
<tr class="even">
<td>901</td>
<td>Active</td>
<td>V183101</td>
<td>2086S0120X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Pediatric Surgery</td>
<td>02</td>
</tr>
<tr class="odd">
<td>902</td>
<td>Active</td>
<td>V183102</td>
<td>2086S0122X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Plastic and Reconstructive Surgery</td>
<td>02</td>
</tr>
<tr class="even">
<td>903</td>
<td>Active</td>
<td>V183106</td>
<td>2086S0127X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Trauma Surgery</td>
<td>02</td>
</tr>
<tr class="odd">
<td>904</td>
<td>Active</td>
<td>V183107</td>
<td>2086S0129X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Vascular Surgery</td>
<td>77</td>
</tr>
<tr class="even">
<td>905</td>
<td>Active</td>
<td>V183105</td>
<td>2086X0206X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgical Oncology</td>
<td>91</td>
</tr>
<tr class="odd">
<td>906</td>
<td>Active</td>
<td>V183400</td>
<td>208800000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Urology</td>
<td></td>
<td>34</td>
</tr>
<tr class="even">
<td>907</td>
<td>Active</td>
<td>V180400</td>
<td>208C00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Colon &amp; Rectal Surgery</td>
<td></td>
<td>28</td>
</tr>
<tr class="odd">
<td>908</td>
<td>Active</td>
<td>V180800</td>
<td>208D00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>General Practice</td>
<td></td>
<td>01</td>
</tr>
<tr class="even">
<td>909</td>
<td>Active</td>
<td>V183200</td>
<td>208G00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Thoracic Surgery (Cardiothoracic Vascular Surgery)</td>
<td></td>
<td>33</td>
</tr>
<tr class="odd">
<td>910</td>
<td>Active</td>
<td>V180900</td>
<td>208M00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Hospitalist</td>
<td></td>
<td>01</td>
</tr>
<tr class="even">
<td>911</td>
<td>Active</td>
<td>V180300</td>
<td>208U00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Clinical Pharmacology</td>
<td></td>
<td>01</td>
</tr>
<tr class="odd">
<td>912</td>
<td>Active</td>
<td>V182302</td>
<td>208VP0000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pain Medicine</td>
<td>Pain Medicine</td>
<td>72</td>
</tr>
<tr class="even">
<td>913</td>
<td>Active</td>
<td>V182301</td>
<td>208VP0014X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pain Medicine</td>
<td>Interventional Pain Medicine</td>
<td>09</td>
</tr>
<tr class="odd">
<td>914</td>
<td>Active</td>
<td>V181100</td>
<td>209800000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Legal Medicine</td>
<td></td>
<td>11</td>
</tr>
<tr class="even">
<td>915</td>
<td>Active</td>
<td>V130701</td>
<td>2278C0205X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Critical Care</td>
<td></td>
</tr>
<tr class="odd">
<td>916</td>
<td>Active</td>
<td>V130703</td>
<td>2278E0002X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Emergency Care</td>
<td></td>
</tr>
<tr class="even">
<td>917</td>
<td>Active</td>
<td>V130702</td>
<td>2278E1000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Educational</td>
<td></td>
</tr>
<tr class="odd">
<td>918</td>
<td>Active</td>
<td>V130705</td>
<td>2278G0305X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Geriatric Care</td>
<td></td>
</tr>
<tr class="even">
<td>919</td>
<td>Active</td>
<td>V130704</td>
<td>2278G1100X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>General Care</td>
<td></td>
</tr>
<tr class="odd">
<td>920</td>
<td>Active</td>
<td>V130706</td>
<td>2278H0200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Home Health</td>
<td></td>
</tr>
<tr class="even">
<td>921</td>
<td>Active</td>
<td>V130710</td>
<td>2278P1004X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Pulmonary Diagnostics</td>
<td></td>
</tr>
<tr class="odd">
<td>922</td>
<td>Active</td>
<td>V130712</td>
<td>2278P1005X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Pulmonary Rehabilitation</td>
<td></td>
</tr>
<tr class="even">
<td>923</td>
<td>Active</td>
<td>V130711</td>
<td>2278P1006X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Pulmonary Function Technologist</td>
<td></td>
</tr>
<tr class="odd">
<td>924</td>
<td>Active</td>
<td>V130708</td>
<td>2278P3800X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Palliative/Hospice</td>
<td></td>
</tr>
<tr class="even">
<td>925</td>
<td>Active</td>
<td>V130707</td>
<td>2278P3900X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Neonatal/Pediatrics</td>
<td></td>
</tr>
<tr class="odd">
<td>926</td>
<td>Active</td>
<td>V130709</td>
<td>2278P4000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>Patient Transport</td>
<td></td>
</tr>
<tr class="even">
<td>927</td>
<td>Active</td>
<td>V130713</td>
<td>2278S1500X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Certified</td>
<td>SNF/Subacute Care</td>
<td></td>
</tr>
<tr class="odd">
<td>928</td>
<td>Active</td>
<td>V130801</td>
<td>2279C0205X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Critical Care</td>
<td></td>
</tr>
<tr class="even">
<td>929</td>
<td>Active</td>
<td>V130803</td>
<td>2279E0002X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Emergency Care</td>
<td></td>
</tr>
<tr class="odd">
<td>930</td>
<td>Active</td>
<td>V130802</td>
<td>2279E1000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Educational</td>
<td></td>
</tr>
<tr class="even">
<td>931</td>
<td>Active</td>
<td>V130805</td>
<td>2279G0305X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Geriatric Care</td>
<td></td>
</tr>
<tr class="odd">
<td>932</td>
<td>Active</td>
<td>V130804</td>
<td>2279G1100X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>General Care</td>
<td></td>
</tr>
<tr class="even">
<td>933</td>
<td>Active</td>
<td>V130806</td>
<td>2279H0200X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Home Health</td>
<td></td>
</tr>
<tr class="odd">
<td>934</td>
<td>Active</td>
<td>V130810</td>
<td>2279P1004X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Pulmonary Diagnostics</td>
<td></td>
</tr>
<tr class="even">
<td>935</td>
<td>Active</td>
<td>V130812</td>
<td>2279P1005X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Pulmonary Rehabilitation</td>
<td></td>
</tr>
<tr class="odd">
<td>936</td>
<td>Active</td>
<td>V130811</td>
<td>2279P1006X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Pulmonary Function Technologist</td>
<td></td>
</tr>
<tr class="even">
<td>937</td>
<td>Active</td>
<td>V130808</td>
<td>2279P3800X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Palliative/Hospice</td>
<td></td>
</tr>
<tr class="odd">
<td>938</td>
<td>Active</td>
<td>V130807</td>
<td>2279P3900X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Neonatal/Pediatrics</td>
<td></td>
</tr>
<tr class="even">
<td>939</td>
<td>Active</td>
<td>V130809</td>
<td>2279P4000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>Patient Transport</td>
<td></td>
</tr>
<tr class="odd">
<td>940</td>
<td>Active</td>
<td>V130813</td>
<td>2279S1500X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Respiratory Therapist, Registered</td>
<td>SNF/Subacute Care</td>
<td></td>
</tr>
<tr class="even">
<td>941</td>
<td>Active</td>
<td>V151200</td>
<td>246X00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>942</td>
<td>Active</td>
<td>V151201</td>
<td>246XC2901X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td>Cardiovascular Invasive Specialist</td>
<td></td>
</tr>
<tr class="even">
<td>943</td>
<td>Active</td>
<td>V151203</td>
<td>246XC2903X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td>Vascular Specialist</td>
<td></td>
</tr>
<tr class="odd">
<td>944</td>
<td>Active</td>
<td>V151202</td>
<td>246XS1301X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Spec/Tech, Cardiovascular</td>
<td>Sonography</td>
<td></td>
</tr>
<tr class="even">
<td>945</td>
<td>Active</td>
<td>V130901</td>
<td>2471B0102X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Bone Densitometry</td>
<td></td>
</tr>
<tr class="odd">
<td>946</td>
<td>Active</td>
<td>V130902</td>
<td>2471C1106X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Cardiac-Interventional Technology</td>
<td></td>
</tr>
<tr class="even">
<td>947</td>
<td>Active</td>
<td>V130903</td>
<td>2471V0105X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Vascular Sonography</td>
<td></td>
</tr>
<tr class="odd">
<td>948</td>
<td>Active</td>
<td>V130904</td>
<td>2471V0106X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiologic Technologist</td>
<td>Vascular-Interventional Technology</td>
<td></td>
</tr>
<tr class="even">
<td>949</td>
<td>Active</td>
<td>V100700</td>
<td>367H00000X</td>
<td>Physician Assistants &amp; Advanced Practice Nursing Providers</td>
<td>Anesthesiologist Assistant</td>
<td></td>
<td>32</td>
</tr>
<tr class="odd">
<td>950</td>
<td>Active</td>
<td>V170800</td>
<td>372500000X</td>
<td>Nursing Service Related Providers</td>
<td>Chore Provider</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>951</td>
<td>Active</td>
<td>V170700</td>
<td>372600000X</td>
<td>Nursing Service Related Providers</td>
<td>Adult Companion</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>952</td>
<td>Active</td>
<td>V170900</td>
<td>373H00000X</td>
<td>Nursing Service Related Providers</td>
<td>Day Training/Habilitation Specialist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>953</td>
<td>Active</td>
<td>V170602</td>
<td>3747A0650X</td>
<td>Nursing Service Related Providers</td>
<td>Technician</td>
<td>Attendant Care Provider</td>
<td></td>
</tr>
<tr class="odd">
<td>954</td>
<td>Active</td>
<td></td>
<td>282N00000X</td>
<td>Hospitals</td>
<td>General Acute Care Hospital</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>962</td>
<td>Active</td>
<td></td>
<td>251E00000X</td>
<td>Agencies</td>
<td>Home Health</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>964</td>
<td>Active</td>
<td></td>
<td>251G00000X</td>
<td>Agencies</td>
<td>Hospice Care, Community Based</td>
<td></td>
<td>B4</td>
</tr>
<tr class="even">
<td>967</td>
<td>Active</td>
<td></td>
<td>251K00000X</td>
<td>Agencies</td>
<td>Public Health or Welfare</td>
<td></td>
<td>60</td>
</tr>
<tr class="odd">
<td>969</td>
<td>Active</td>
<td></td>
<td>251V00000X</td>
<td>Agencies</td>
<td>Voluntary or Charitable</td>
<td></td>
<td>61</td>
</tr>
<tr class="even">
<td>970</td>
<td>Active</td>
<td></td>
<td>261Q00000X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td></td>
<td>70</td>
</tr>
<tr class="odd">
<td>976</td>
<td>Active</td>
<td></td>
<td>261QA1903X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Ambulatory Surgical</td>
<td>49</td>
</tr>
<tr class="even">
<td>987</td>
<td>Active</td>
<td></td>
<td>261QE0700X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>End-Stage Renal Disease (ESRD) Treatment</td>
<td>B4</td>
</tr>
<tr class="odd">
<td>989</td>
<td>Active</td>
<td></td>
<td>261QF0400X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Federally Qualified Health Center (FQHC)</td>
<td>B4</td>
</tr>
<tr class="even">
<td>998</td>
<td>Active</td>
<td></td>
<td>261QM0801X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Mental Health (Including Community Mental Health Center)</td>
<td>B4</td>
</tr>
<tr class="odd">
<td>1005</td>
<td>Active</td>
<td></td>
<td>261QM1300X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Multi-Specialty</td>
<td>70</td>
</tr>
<tr class="even">
<td>1012</td>
<td>Active</td>
<td></td>
<td>261QP2000X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Physical Therapy</td>
<td>70</td>
</tr>
<tr class="odd">
<td>1018</td>
<td>Active</td>
<td></td>
<td>261QR0200X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Radiology</td>
<td>74</td>
</tr>
<tr class="even">
<td>1020</td>
<td>Active</td>
<td></td>
<td>261QR0208X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Radiology, Mobile</td>
<td>45</td>
</tr>
<tr class="odd">
<td>1021</td>
<td>Active</td>
<td></td>
<td>261QR0207X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Radiology, Mobile Mammography</td>
<td>45</td>
</tr>
<tr class="even">
<td>1023</td>
<td>Active</td>
<td></td>
<td>261QR0400X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Rehabilitation</td>
<td></td>
</tr>
<tr class="odd">
<td>1025</td>
<td>Active</td>
<td></td>
<td>261QR0401X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Rehabilitation, Comprehensive Outpatient Rehabilitation Facility (CORF)</td>
<td>B4</td>
</tr>
<tr class="even">
<td>1028</td>
<td>Active</td>
<td></td>
<td>261QR1300X</td>
<td>Ambulatory Health Care Facilities</td>
<td>Clinic/Center</td>
<td>Rural Health</td>
<td>B4</td>
</tr>
<tr class="odd">
<td>1033</td>
<td>Active</td>
<td></td>
<td>275N00000X</td>
<td>Hospital Units</td>
<td>Medicare Defined Swing Bed Unit</td>
<td></td>
<td>A0</td>
</tr>
<tr class="even">
<td>1034</td>
<td>Active</td>
<td></td>
<td>273R00000X</td>
<td>Hospital Units</td>
<td>Psychiatric Unit</td>
<td></td>
<td>A0</td>
</tr>
<tr class="odd">
<td>1035</td>
<td>Active</td>
<td></td>
<td>273Y00000X</td>
<td>Hospital Units</td>
<td>Rehabilitation Unit</td>
<td></td>
<td>A0</td>
</tr>
<tr class="even">
<td>1040</td>
<td>Active</td>
<td></td>
<td>282NC2000X</td>
<td>Hospitals</td>
<td>General Acute Care Hospital</td>
<td>Children</td>
<td>A0</td>
</tr>
<tr class="odd">
<td>1041</td>
<td>Active</td>
<td></td>
<td>282NC0060X</td>
<td>Hospitals</td>
<td>General Acute Care Hospital</td>
<td>Critical Access</td>
<td>A0</td>
</tr>
<tr class="even">
<td>1044</td>
<td>Active</td>
<td></td>
<td>282E00000X</td>
<td>Hospitals</td>
<td>Long Term Care Hospital</td>
<td></td>
<td>A0</td>
</tr>
<tr class="odd">
<td>1049</td>
<td>Active</td>
<td></td>
<td>283Q00000X</td>
<td>Hospitals</td>
<td>Psychiatric Hospital</td>
<td></td>
<td>A0</td>
</tr>
<tr class="even">
<td>1050</td>
<td>Active</td>
<td></td>
<td>283X00000X</td>
<td>Hospitals</td>
<td>Rehabilitation Hospital</td>
<td></td>
<td>A0</td>
</tr>
<tr class="odd">
<td>1052</td>
<td>Active</td>
<td></td>
<td>282J00000X</td>
<td>Hospitals</td>
<td>Religious Nonmedical Health Care Institution</td>
<td></td>
<td>B4</td>
</tr>
<tr class="even">
<td>1053</td>
<td>Active</td>
<td></td>
<td>284300000X</td>
<td>Hospitals</td>
<td>Special Hospital</td>
<td></td>
<td>A0</td>
</tr>
<tr class="odd">
<td>1054</td>
<td>Active</td>
<td></td>
<td>291U00000X</td>
<td>Laboratories</td>
<td>Clinical Medical Laboratory</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1056</td>
<td>Active</td>
<td></td>
<td>291900000X</td>
<td>Laboratories</td>
<td>Military Clinical Medical Laboratory</td>
<td></td>
<td>B4</td>
</tr>
<tr class="odd">
<td>1057</td>
<td>Active</td>
<td></td>
<td>293D00000X</td>
<td>Laboratories</td>
<td>Physiological Laboratory</td>
<td></td>
<td>47</td>
</tr>
<tr class="even">
<td>1072</td>
<td>Active</td>
<td></td>
<td>313M00000X</td>
<td>Nursing &amp; Custodial Care Facilities</td>
<td>Nursing Facility/Intermediate Care Facility</td>
<td></td>
<td>A3</td>
</tr>
<tr class="odd">
<td>1073</td>
<td>Active</td>
<td></td>
<td>314000000X</td>
<td>Nursing &amp; Custodial Care Facilities</td>
<td>Skilled Nursing Facility</td>
<td></td>
<td>A1</td>
</tr>
<tr class="even">
<td>1089</td>
<td>Active</td>
<td></td>
<td>332B00000X</td>
<td>Suppliers</td>
<td>Durable Medical Equipment &amp; Medical Supplies</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1093</td>
<td>Active</td>
<td></td>
<td>332BX2000X</td>
<td>Suppliers</td>
<td>Durable Medical Equipment &amp; Medical Supplies</td>
<td>Oxygen Equipment &amp; Supplies</td>
<td>B1</td>
</tr>
<tr class="even">
<td>1103</td>
<td>Active</td>
<td></td>
<td>335U00000X</td>
<td>Suppliers</td>
<td>Organ Procurement Organization</td>
<td></td>
<td>B4</td>
</tr>
<tr class="odd">
<td>1104</td>
<td>Active</td>
<td></td>
<td>333600000X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1105</td>
<td>Active</td>
<td></td>
<td>3336C0002X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Clinic Pharmacy</td>
<td></td>
</tr>
<tr class="odd">
<td>1106</td>
<td>Active</td>
<td></td>
<td>3336C0003X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Community/Retail Pharmacy</td>
<td></td>
</tr>
<tr class="even">
<td>1107</td>
<td>Active</td>
<td></td>
<td>3336C0004X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Compounding Pharmacy</td>
<td></td>
</tr>
<tr class="odd">
<td>1108</td>
<td>Active</td>
<td></td>
<td>3336H0001X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Home Infusion Therapy Pharmacy</td>
<td></td>
</tr>
<tr class="even">
<td>1109</td>
<td>Active</td>
<td></td>
<td>3336I0012X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Institutional Pharmacy</td>
<td></td>
</tr>
<tr class="odd">
<td>1110</td>
<td>Active</td>
<td></td>
<td>3336L0003X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Long Term Care Pharmacy</td>
<td></td>
</tr>
<tr class="even">
<td>1111</td>
<td>Active</td>
<td></td>
<td>3336M0002X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Mail Order Pharmacy</td>
<td></td>
</tr>
<tr class="odd">
<td>1112</td>
<td>Active</td>
<td></td>
<td>3336M0003X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Managed Care Organization Pharmacy</td>
<td></td>
</tr>
<tr class="even">
<td>1113</td>
<td>Active</td>
<td></td>
<td>3336N0007X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Nuclear Pharmacy</td>
<td></td>
</tr>
<tr class="odd">
<td>1114</td>
<td>Active</td>
<td></td>
<td>3336S0011X</td>
<td>Suppliers</td>
<td>Pharmacy</td>
<td>Specialty Pharmacy</td>
<td></td>
</tr>
<tr class="even">
<td>1115</td>
<td>Active</td>
<td></td>
<td>335V00000X</td>
<td>Suppliers</td>
<td>Portable X-ray and/or Other Portable Diagnostic Imaging Supplier</td>
<td></td>
<td>63</td>
</tr>
<tr class="odd">
<td>1116</td>
<td>Active</td>
<td></td>
<td>335E00000X</td>
<td>Suppliers</td>
<td>Prosthetic/Orthotic Supplier</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1117</td>
<td>Active</td>
<td></td>
<td>341600000X</td>
<td>Transportation Services</td>
<td>Ambulance</td>
<td></td>
<td>59</td>
</tr>
<tr class="odd">
<td>1118</td>
<td>Active</td>
<td></td>
<td>3416A0800X</td>
<td>Transportation Services</td>
<td>Ambulance</td>
<td>Air Transport</td>
<td>59</td>
</tr>
<tr class="even">
<td>1119</td>
<td>Active</td>
<td></td>
<td>3416L0300X</td>
<td>Transportation Services</td>
<td>Ambulance</td>
<td>Land Transport</td>
<td>59</td>
</tr>
<tr class="odd">
<td>1120</td>
<td>Active</td>
<td></td>
<td>3416S0300X</td>
<td>Transportation Services</td>
<td>Ambulance</td>
<td>Water Transport</td>
<td>59</td>
</tr>
<tr class="even">
<td>1132</td>
<td>Active</td>
<td>V020900</td>
<td>111NP0017X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Pediatric Chiropractor</td>
<td>35</td>
</tr>
<tr class="odd">
<td>1133</td>
<td>Active</td>
<td>V082400</td>
<td>173C00000X</td>
<td>Other Service Providers</td>
<td>Reflexologist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1134</td>
<td>Active</td>
<td>V082500</td>
<td>173F00000X</td>
<td>Other Service Providers</td>
<td>Sleep Specialist, PhD</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1135</td>
<td>Active</td>
<td>V090106</td>
<td>1835P0018X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Pharmacist Clinician (PhC)/ Clinical Pharmacy Specialist</td>
<td></td>
</tr>
<tr class="even">
<td>1137</td>
<td>Active</td>
<td>V180707</td>
<td>207QS1201X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Sleep Medicine</td>
<td>08</td>
</tr>
<tr class="odd">
<td>1138</td>
<td>Active</td>
<td>V010700</td>
<td>103K00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Behavioral Analyst</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1139</td>
<td>Active</td>
<td>V130110</td>
<td>225XG0600X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Gerontology</td>
<td>67</td>
</tr>
<tr class="odd">
<td>1140</td>
<td>Active</td>
<td>V130111</td>
<td>225XM0800X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Mental Health</td>
<td>67</td>
</tr>
<tr class="even">
<td>1141</td>
<td>Active</td>
<td>V130112</td>
<td>225XP0019X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Physical Rehabilitation</td>
<td>67</td>
</tr>
<tr class="odd">
<td>1142</td>
<td>Active</td>
<td>V130113</td>
<td>225XE0001X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Environmental Modification</td>
<td>67</td>
</tr>
<tr class="even">
<td>1143</td>
<td>Active</td>
<td>V130114</td>
<td>225XF0002X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Feeding, Eating &amp; Swallowing</td>
<td>67</td>
</tr>
<tr class="odd">
<td>1144</td>
<td>Active</td>
<td>V130115</td>
<td>225XL0004X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapist</td>
<td>Low Vision</td>
<td>67</td>
</tr>
<tr class="even">
<td>1145</td>
<td>Active</td>
<td>V130116</td>
<td>224ZF0002X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapy Assistant</td>
<td>Feeding, Eating &amp; Swallowing</td>
<td>67</td>
</tr>
<tr class="odd">
<td>1146</td>
<td>Active</td>
<td>V130117</td>
<td>224ZL0004X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapy Assistant</td>
<td>Low Vision</td>
<td>67</td>
</tr>
<tr class="even">
<td>1147</td>
<td>Active</td>
<td>V130118</td>
<td>224ZR0403X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapy Assistant</td>
<td>Driving and Community Mobility</td>
<td>67</td>
</tr>
<tr class="odd">
<td>1148</td>
<td>Active</td>
<td>V130119</td>
<td>224ZE0001X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Occupational Therapy Assistant</td>
<td>Environmental Modification</td>
<td>67</td>
</tr>
<tr class="even">
<td>1149</td>
<td>Active</td>
<td>V153000</td>
<td>243U00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Radiology Practitioner Assistant</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1151</td>
<td>Active</td>
<td>V010422</td>
<td>103TH0004X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Health</td>
<td>62</td>
</tr>
<tr class="even">
<td>1152</td>
<td>Active</td>
<td>V182605</td>
<td>2081H0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Hospice and Palliative Medicine</td>
<td>25</td>
</tr>
<tr class="odd">
<td>1153</td>
<td>Active</td>
<td>V081902</td>
<td>174H00000X</td>
<td>Other Service Providers</td>
<td>Health Educator</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1154</td>
<td>Active</td>
<td>V180506</td>
<td>2080C0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Child Abuse Pediatrics</td>
<td>37</td>
</tr>
<tr class="odd">
<td>1155</td>
<td>Active</td>
<td>V170603</td>
<td>374J00000X</td>
<td>Nursing Service Related Providers</td>
<td>Doula</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1156</td>
<td>Active</td>
<td>V170101</td>
<td>374K00000X</td>
<td>Nursing Service Related Providers</td>
<td>Religious Nonmedical Practitioner</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1157</td>
<td>Active</td>
<td>V182415</td>
<td>202K00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Phlebology</td>
<td></td>
<td>22</td>
</tr>
<tr class="even">
<td>1158</td>
<td>Active</td>
<td>V182416</td>
<td>207ZC0006X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Clinical Pathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>1159</td>
<td>Active</td>
<td>V090108</td>
<td>1835X0200X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Oncology</td>
<td>87</td>
</tr>
<tr class="even">
<td>1160</td>
<td>Active</td>
<td>V090107</td>
<td>1835G0303X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Geriatric</td>
<td>87</td>
</tr>
<tr class="odd">
<td>1162</td>
<td>Active</td>
<td>V151002</td>
<td>242T00000X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Perfusionist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1163</td>
<td>Active</td>
<td>V130216</td>
<td>224900000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Mastectomy Fitter</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1164</td>
<td>Active</td>
<td>V130313</td>
<td>224L00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Pedorthist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1166</td>
<td>Active</td>
<td>V182107</td>
<td>207XP3100X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Orthopaedic Surgery</td>
<td>Pediatric Orthopaedic Surgery</td>
<td></td>
</tr>
<tr class="odd">
<td>1167</td>
<td>Active</td>
<td>V070850</td>
<td>174N00000X</td>
<td>Other Service Providers</td>
<td>Lactation Consultant, Non-RN</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1168</td>
<td>Active</td>
<td>V081810</td>
<td>174V00000X</td>
<td>Other Service Providers</td>
<td>Clinical Ethicist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1169</td>
<td>Active</td>
<td>V181550</td>
<td>204R00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Electrodiagnostic Medicine</td>
<td></td>
<td>13</td>
</tr>
<tr class="even">
<td>1170</td>
<td>Active</td>
<td>V082201</td>
<td>170300000X</td>
<td>Other Service Providers</td>
<td>Genetic Counselor, MS</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1172</td>
<td>Active</td>
<td>V130601</td>
<td>224Y00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Clinical Exercise Physiologist</td>
<td></td>
<td>25</td>
</tr>
<tr class="even">
<td>1174</td>
<td>Active</td>
<td>V060808</td>
<td>390200000X</td>
<td>Optometry</td>
<td>Optometry Resident</td>
<td></td>
<td>41</td>
</tr>
<tr class="odd">
<td>1175</td>
<td>Active</td>
<td>V120213</td>
<td>390200000X</td>
<td>Podiatry</td>
<td>Podiatry Resident</td>
<td></td>
<td>48</td>
</tr>
<tr class="even">
<td>1176</td>
<td>Active</td>
<td>V181807</td>
<td>207VF0040X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Female Pelvic Medicine and Reconstructive Surgery</td>
<td>16</td>
</tr>
<tr class="odd">
<td>1177</td>
<td>Active</td>
<td>V182914</td>
<td>2084B0040X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Behavioral Neurology &amp; Neuropsychiatry</td>
<td>26</td>
</tr>
<tr class="even">
<td>1178</td>
<td>Active</td>
<td>V183401</td>
<td>2088F0040X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Urology</td>
<td>Female Pelvic Medicine and Reconstructive Surgery</td>
<td>34</td>
</tr>
<tr class="odd">
<td>1180</td>
<td>Active</td>
<td>V010423</td>
<td>102L00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychoanalyst</td>
<td></td>
<td>26</td>
</tr>
<tr class="even">
<td>1181</td>
<td>Active</td>
<td>V010701</td>
<td>102X00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Poetry Therapist</td>
<td></td>
<td>26</td>
</tr>
<tr class="odd">
<td>1182</td>
<td>Active</td>
<td>V020601</td>
<td>111NR0400X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Rehabilitation</td>
<td>35</td>
</tr>
<tr class="even">
<td>1183</td>
<td>Active</td>
<td>V180204</td>
<td>207LH0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Hospice and Palliative Medicine</td>
<td>05</td>
</tr>
<tr class="odd">
<td>1184</td>
<td>Active</td>
<td>V180205</td>
<td>207LP3000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Anesthesiology</td>
<td>Pediatric Anesthesiology</td>
<td>05</td>
</tr>
<tr class="even">
<td>1185</td>
<td>Active</td>
<td>V180606</td>
<td>207PH0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Emergency Medicine</td>
<td>Hospice and Palliative Medicine</td>
<td>93</td>
</tr>
<tr class="odd">
<td>1186</td>
<td>Active</td>
<td>V180708</td>
<td>207QB0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Obesity Medicine</td>
<td>08</td>
</tr>
<tr class="even">
<td>1187</td>
<td>Active</td>
<td>V180709</td>
<td>207QH0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Family Medicine</td>
<td>Hospice and Palliative Medicine</td>
<td>08</td>
</tr>
<tr class="odd">
<td>1188</td>
<td>Active</td>
<td>V181022</td>
<td>207RB0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Obesity Medicine</td>
<td>11</td>
</tr>
<tr class="even">
<td>1189</td>
<td>Active</td>
<td>V181023</td>
<td>207RH0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hospice and Palliative Medicine</td>
<td>11</td>
</tr>
<tr class="odd">
<td>1190</td>
<td>Active</td>
<td>V181024</td>
<td>207RS0012X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Sleep Medicine</td>
<td>11</td>
</tr>
<tr class="even">
<td>1191</td>
<td>Active</td>
<td>V181025</td>
<td>207RT0003X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Transplant Hepatology</td>
<td>11</td>
</tr>
<tr class="odd">
<td>1192</td>
<td>Active</td>
<td>V181808</td>
<td>207VB0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Obesity Medicine</td>
<td>16</td>
</tr>
<tr class="even">
<td>1193</td>
<td>Active</td>
<td>V181809</td>
<td>207VH0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Obstetrics &amp; Gynecology</td>
<td>Hospice and Palliative Medicine</td>
<td>16</td>
</tr>
<tr class="odd">
<td>1194</td>
<td>Active</td>
<td>V182207</td>
<td>207YS0012X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Otolaryngology</td>
<td>Sleep Medicine</td>
<td>04</td>
</tr>
<tr class="even">
<td>1195</td>
<td>Active</td>
<td>V182518</td>
<td>2080H0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Hospice and Palliative Medicine</td>
<td>37</td>
</tr>
<tr class="odd">
<td>1196</td>
<td>Active</td>
<td>V182519</td>
<td>2080S0012X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Sleep Medicine</td>
<td>37</td>
</tr>
<tr class="even">
<td>1197</td>
<td>Active</td>
<td>V182520</td>
<td>2080T0004X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Pediatric Transplant Hepatology</td>
<td>37</td>
</tr>
<tr class="odd">
<td>1199</td>
<td>Active</td>
<td>V182915</td>
<td>2084B0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Obesity Medicine</td>
<td>86</td>
</tr>
<tr class="even">
<td>1201</td>
<td>Active</td>
<td>V182917</td>
<td>2084D0003X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Diagnostic Neuroimaging</td>
<td>86</td>
</tr>
<tr class="odd">
<td>1202</td>
<td>Active</td>
<td>V182918</td>
<td>2084H0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Hospice and Palliative Medicine</td>
<td>86</td>
</tr>
<tr class="even">
<td>1203</td>
<td>Active</td>
<td>V182919</td>
<td>2084N0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Neuromuscular Medicine</td>
<td>86</td>
</tr>
<tr class="odd">
<td>1204</td>
<td>Active</td>
<td>V182920</td>
<td>2084P0015X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Psychosomatic Medicine</td>
<td>86</td>
</tr>
<tr class="even">
<td>1205</td>
<td>Active</td>
<td>V182921</td>
<td>2084S0012X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Sleep Medicine</td>
<td>86</td>
</tr>
<tr class="odd">
<td>1206</td>
<td>Active</td>
<td>V183011</td>
<td>2085D0003X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Diagnostic Neuroimaging</td>
<td>94</td>
</tr>
<tr class="even">
<td>1207</td>
<td>Active</td>
<td>V183012</td>
<td>2085H0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Radiology</td>
<td>Hospice and Palliative Medicine</td>
<td>94</td>
</tr>
<tr class="odd">
<td>1208</td>
<td>Active</td>
<td>V183108</td>
<td>2086H0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Surgery</td>
<td>Hospice and Palliative Medicine</td>
<td>02</td>
</tr>
<tr class="even">
<td>1209</td>
<td>Active</td>
<td>V183402</td>
<td>2088P0231X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Urology</td>
<td>Pediatric Urology</td>
<td>34</td>
</tr>
<tr class="odd">
<td>1210</td>
<td>Active</td>
<td>V030101</td>
<td>125J00000X</td>
<td>Dental Providers</td>
<td>Dental Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1211</td>
<td>Active</td>
<td>V030102</td>
<td>125K00000X</td>
<td>Dental Providers</td>
<td>Advanced Practice Dental Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1212</td>
<td>Active</td>
<td>V080101</td>
<td>171M00000X</td>
<td>Other Service Providers</td>
<td>Case Manager/Care Coordinator</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1213</td>
<td>Active</td>
<td>V080400</td>
<td>172V00000X</td>
<td>Other Service Providers</td>
<td>Community Health Worker</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1214</td>
<td>Active</td>
<td>V080300</td>
<td>171R00000X</td>
<td>Other Service Providers</td>
<td>Interpreter</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1215</td>
<td>Active</td>
<td>V080600</td>
<td>172M00000X</td>
<td>Other Service Providers</td>
<td>Mechanotherapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1216</td>
<td>Active</td>
<td>V030490</td>
<td>1223D0004X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>Dentist Anesthesiologist</td>
<td>C5</td>
</tr>
<tr class="even">
<td>1301</td>
<td>Active</td>
<td>V180905</td>
<td>202C00000X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Independent Medical Examiner</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1303</td>
<td>Active</td>
<td>V181027</td>
<td>207RA0001X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Advanced Heart Failure and Transplant Cardiology</td>
<td>11</td>
</tr>
<tr class="even">
<td>1306</td>
<td>Active</td>
<td>V181026</td>
<td>207RH0005X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Internal Medicine</td>
<td>Hypertension Specialist</td>
<td>11</td>
</tr>
<tr class="odd">
<td>1307</td>
<td>Active</td>
<td>V183414</td>
<td>207ZC0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pathology</td>
<td>Clinical Informatics</td>
<td></td>
</tr>
<tr class="even">
<td>1308</td>
<td>Active</td>
<td>V113002</td>
<td>207WX0009X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td>Glaucoma Specialist</td>
<td>18</td>
</tr>
<tr class="odd">
<td>1309</td>
<td>Active</td>
<td>V113003</td>
<td>207WX0107X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td>Retina Specialist</td>
<td>18</td>
</tr>
<tr class="even">
<td>1310</td>
<td>Active</td>
<td>V113004</td>
<td>207WX0108X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td>Uveitis and Ocular Inflammatory Disease</td>
<td>18</td>
</tr>
<tr class="odd">
<td>1311</td>
<td>Active</td>
<td>V181901</td>
<td>207WX0200X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td>Ophthalmic Plastic and Reconstructive Surgery</td>
<td>18</td>
</tr>
<tr class="even">
<td>1312</td>
<td>Active</td>
<td>V182523</td>
<td>2080B0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Pediatrics</td>
<td>Obesity Medicine</td>
<td>37</td>
</tr>
<tr class="odd">
<td>1314</td>
<td>Active</td>
<td>V182609</td>
<td>2081N0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Neuromuscular Medicine</td>
<td>25</td>
</tr>
<tr class="even">
<td>1315</td>
<td>Active</td>
<td>V182606</td>
<td>2081P0301X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Physical Medicine &amp; Rehabilitation</td>
<td>Brain Injury Medicine</td>
<td>23</td>
</tr>
<tr class="odd">
<td>1316</td>
<td>Active</td>
<td>V182808</td>
<td>2083B0002X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Obesity Medicine</td>
<td>84</td>
</tr>
<tr class="even">
<td>1317</td>
<td>Active</td>
<td>V183415</td>
<td>2083C0008X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Preventive Medicine</td>
<td>Clinical Informatics</td>
<td></td>
</tr>
<tr class="odd">
<td>1318</td>
<td>Active</td>
<td>V114811</td>
<td>2084A2900X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Neurocritical Care</td>
<td>13</td>
</tr>
<tr class="even">
<td>1319</td>
<td>Active</td>
<td>V182922</td>
<td>2084P0301X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Psychiatry &amp; Neurology</td>
<td>Brain Injury Medicine</td>
<td>26</td>
</tr>
<tr class="odd">
<td>1324</td>
<td>Active</td>
<td>V010702</td>
<td>106E00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Assistant Behavior Analyst</td>
<td></td>
<td>62</td>
</tr>
<tr class="even">
<td>1325</td>
<td>Active</td>
<td>V010703</td>
<td>106S00000X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Behavior Technician</td>
<td></td>
<td>62</td>
</tr>
<tr class="odd">
<td>1326</td>
<td>Active</td>
<td>V183403</td>
<td>103TP0016X</td>
<td>Behavioral Health &amp; Social Service Providers</td>
<td>Psychologist</td>
<td>Prescribing (Medical)</td>
<td>62</td>
</tr>
<tr class="even">
<td>1330</td>
<td>Active</td>
<td>V183404</td>
<td>111NI0013X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Independent Medical Examiner</td>
<td>35</td>
</tr>
<tr class="odd">
<td>1331</td>
<td>Active</td>
<td>V183405</td>
<td>125Q00000X</td>
<td>Dental Providers</td>
<td>Oral Medicinist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1334</td>
<td>Active</td>
<td>V183411</td>
<td>193200000X</td>
<td>Group</td>
<td>Multi-Specialty</td>
<td></td>
<td>70</td>
</tr>
<tr class="odd">
<td>1335</td>
<td>Active</td>
<td>V183412</td>
<td>193400000X</td>
<td>Group</td>
<td>Single Specialty</td>
<td></td>
<td>70</td>
</tr>
<tr class="even">
<td>1341</td>
<td>Active</td>
<td>V183406</td>
<td>163WR0006X</td>
<td>Nursing Service Providers</td>
<td>Registered Nurse</td>
<td>Registered Nurse First Assistant</td>
<td></td>
</tr>
<tr class="odd">
<td>1343</td>
<td>Active</td>
<td>V183407</td>
<td>171000000X</td>
<td>Other Service Providers</td>
<td>Military Health Care Provider</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1344</td>
<td>Active</td>
<td>V183408</td>
<td>1710I1002X</td>
<td>Other Service Providers</td>
<td>Military Health Care Provider</td>
<td>Independent Duty Corpsman</td>
<td></td>
</tr>
<tr class="odd">
<td>1345</td>
<td>Active</td>
<td>V183409</td>
<td>1710I1003X</td>
<td>Other Service Providers</td>
<td>Military Health Care Provider</td>
<td>Independent Duty Medical Technicians</td>
<td></td>
</tr>
<tr class="even">
<td>1347</td>
<td>Active</td>
<td>V183410</td>
<td>172P00000X</td>
<td>Other Service Providers</td>
<td>Naprapath</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1348</td>
<td>Active</td>
<td>V081501</td>
<td>175T00000X</td>
<td>Other Service Providers</td>
<td>Peer Specialist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1350</td>
<td>Active</td>
<td>V081906</td>
<td>405300000X</td>
<td>Other Service Providers</td>
<td>Prevention Professional</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1354</td>
<td>Active</td>
<td>V090110</td>
<td>1835C0205X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Critical Care</td>
<td>A5</td>
</tr>
<tr class="even">
<td>1355</td>
<td>Active</td>
<td>V090111</td>
<td>1835P0200X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Pediatrics</td>
<td>A5</td>
</tr>
<tr class="odd">
<td>1356</td>
<td>Active</td>
<td>V090109</td>
<td>1835P2201X</td>
<td>Pharmacy Service Providers</td>
<td>Pharmacist</td>
<td>Ambulatory Care</td>
<td></td>
</tr>
<tr class="even">
<td>1599</td>
<td>Active</td>
<td>V183416</td>
<td>222Q00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Developmental Therapist</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>1600</td>
<td>Active</td>
<td>V183418</td>
<td>229N00000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Anaplastologist</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1604</td>
<td>Active</td>
<td>V183417</td>
<td>225CX0006X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Rehabilitation Counselor</td>
<td>Orientation and Mobility Training Provider</td>
<td></td>
</tr>
<tr class="odd">
<td>1606</td>
<td>Active</td>
<td>V130814</td>
<td>226000000X</td>
<td>Respiratory, Developmental, Rehabilitative and Restorative Service Providers</td>
<td>Recreational Therapist Assistant</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1613</td>
<td>Active</td>
<td>V150223</td>
<td>246ZC0007X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Surgical Assistant</td>
<td></td>
</tr>
<tr class="odd">
<td>1614</td>
<td>Active</td>
<td>V150224</td>
<td>246ZS0410X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Surgical Technologist</td>
<td></td>
</tr>
<tr class="even">
<td>1615</td>
<td>Active</td>
<td>V150222</td>
<td>246ZX2200X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Specialist/Technologist, Other</td>
<td>Orthopedic Assistant</td>
<td></td>
</tr>
<tr class="odd">
<td>1618</td>
<td>Active</td>
<td>V183413</td>
<td>247ZC0005X</td>
<td>Technologists, Technicians &amp; Other Technical Service Providers</td>
<td>Pathology</td>
<td>Clinical Laboratory Director, Non-physician</td>
<td></td>
</tr>
<tr class="even">
<td>1637</td>
<td>Active</td>
<td>V181903</td>
<td>207WX0109X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td>Neuro-ophthalmology</td>
<td></td>
</tr>
<tr class="odd">
<td>1638</td>
<td>Active</td>
<td>V181902</td>
<td>207WX0110X</td>
<td>Allopathic &amp; Osteopathic Physicians</td>
<td>Ophthalmology</td>
<td>Pediatric Ophthalmology and Strabismus Specialist</td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Ref379295371" class="anchor"></span>Table : Updated Person Class Codes—Kernel Patch XU\*8.0\*531

## Updated Person Class Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 5</u> lists all updated Person Class codes released with Kernel Patch XU\*8.0\*531 (released on 02/17/2010). Updated data includes the following:

- Definition (indicated by superscript "<sup>1</sup>" in the IEN column; data not displayed in <u>Table 5</u>)
- Classification (indicated by superscript "<sup>2</sup>" in the IEN column)
- Area of Specialization (indicated by superscript "<sup>3</sup>" in the IEN column)
- CMS Specialty Code (indicated by superscript "<sup>4</sup>" in the IEN column)

![](xu-8-671-assigning-person-class-to-providers-user-guide/027.png) NOTE: Some entries may have multiple updates; for those items, there will be multiple superscripts separated by a comma.

<table>
<caption><p><span id="_Ref488675001" class="anchor"></span>Table 6: Inactivated Person Class Codes—Kernel Patch XU*8.0*377</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 19%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>Status</th>
<th>VA Code</th>
<th>NUCC<br />
X12 Code</th>
<th>Provider Type</th>
<th>Classification</th>
<th>Area of Specialization</th>
<th>CMS Specialty Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>195<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V020100</td>
<td>111NI0900X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Internist</td>
<td>35</td>
</tr>
<tr class="even">
<td>196<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V020200</td>
<td>111NN0400X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Neurology</td>
<td>35</td>
</tr>
<tr class="odd">
<td>197<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V020300</td>
<td>111NN1001X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Nutrition</td>
<td>35</td>
</tr>
<tr class="even">
<td>198<strong><sup>1,3</sup></strong></td>
<td>Active</td>
<td>V020400</td>
<td>111NX0100X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Occupational Health</td>
<td>35</td>
</tr>
<tr class="odd">
<td>199<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V020500</td>
<td>111NX0800X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Orthopedic</td>
<td>35</td>
</tr>
<tr class="even">
<td>200<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V020600</td>
<td>111NR0200X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Radiology</td>
<td>35</td>
</tr>
<tr class="odd">
<td>201<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V020700</td>
<td>111NS0005X</td>
<td>Chiropractic Providers</td>
<td>Chiropractor</td>
<td>Sports Physician</td>
<td>35</td>
</tr>
<tr class="even">
<td>369<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V010600</td>
<td>104100000X</td>
<td>Behavioral Health and Social Service Providers</td>
<td>Social Worker</td>
<td></td>
<td>80</td>
</tr>
<tr class="odd">
<td>370<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V010100</td>
<td>1041C0700X</td>
<td>Behavioral Health and Social Service Providers</td>
<td>Social Worker</td>
<td>Clinical</td>
<td>80</td>
</tr>
<tr class="even">
<td>669<strong><sup>1,2</sup></strong></td>
<td>Active</td>
<td>V170100</td>
<td>374T00000X</td>
<td>Nursing Service Related Providers</td>
<td>Religious Nonmedical Nursing Personnel</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>836<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V182401</td>
<td>207ZP0101X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Anatomic Pathology</td>
<td>22</td>
</tr>
<tr class="even">
<td>837<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V182402</td>
<td>207ZP0102X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Pathology</td>
<td>Anatomic Pathology and Clinical Pathology</td>
<td>22</td>
</tr>
<tr class="odd">
<td>864<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V182604</td>
<td>2081S0010X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Physical Medicine and Rehabilitation</td>
<td>Sports Medicine</td>
<td>25</td>
</tr>
<tr class="even">
<td>904<strong><sup>4</sup></strong></td>
<td>Active</td>
<td>V183107</td>
<td>2086S0129X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Vascular Surgery</td>
<td>77</td>
</tr>
<tr class="odd">
<td>905<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V183105</td>
<td>2086X0206X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Surgery</td>
<td>Surgical Oncology</td>
<td>91</td>
</tr>
<tr class="even">
<td>910<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V180900</td>
<td>208M00000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Hospitalist</td>
<td></td>
<td>01</td>
</tr>
<tr class="odd">
<td>914<strong><sup>1</sup></strong></td>
<td>Active</td>
<td>V181100</td>
<td>209800000X</td>
<td>Allopathic and Osteopathic Physicians</td>
<td>Legal Medicine</td>
<td></td>
<td>11</td>
</tr>
</tbody>
</table>

<span id="_Ref488675001" class="anchor"></span>Table 6: Inactivated Person Class Codes—Kernel Patch XU\*8.0\*377

## Inactivated Person Class Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- <u>Patch XU\*8.0\*377</u>
- <u>Patch XU\*8.0\*531</u>
- <u>Patch XU\*8.0\*671</u>

### Patch XU\*8.0\*377

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 6</u> lists all inactivated Person Class codes released with Kernel Patch XU\*8.0\*377 (released on 10/24/2005):

| IEN | VA Code | X12 Code   | Provider Type                                          | Classification                      | Area of Specialization                                                | Date Inactivated |
|-----|---------|------------|--------------------------------------------------------|-------------------------------------|-----------------------------------------------------------------------|------------------|
| 359 | V010300 | 103S00000N | Behavioral Health and Social Service                   | Psychoanalyst                       |                                                                       | 7/1/2005         |
| 360 | V010301 | 103SA1800N | Behavioral Health and Social Service                   | Psychoanalyst                       | Affiliate                                                             | 7/1/2005         |
| 361 | V010302 | 103SA1400N | Behavioral Health and Social Service                   | Psychoanalyst                       | Associate                                                             | 7/1/2005         |
| 335 | V040100 | 1327D0700N | Dietary and Nutritional Service                        | Dietary Manager                     | Dietary Management                                                    | 7/1/2005         |
| 233 | V060801 | 152WC0800N | Eye and Vision Services                                | Optometrist                         | Contact Lens                                                          | 7/1/2005         |
| 309 | V070935 | 163WX1000N | Nursing Service                                        | Registered Nurse                    | Operating Room                                                        | 7/1/2005         |
| 320 | V070946 | 163WP2200N | Nursing Service                                        | Registered Nurse                    | Post-Anesthesia                                                       | 7/1/2005         |
| 680 | V082200 | 173W00000X | Other Service                                          | Registered Nurse                    |                                                                       | 7/1/2005         |
| 252 | V090200 | 1847P3400N | Pharmacy Service                                       | Technician                          | Pharmacy                                                              | 7/1/2005         |
| 684 | V090201 | 184700000X | Pharmacy Service                                       | Technician                          |                                                                       | 7/1/2005         |
| 537 | V100316 | 364SN0004N | Physician Assistants & Advanced Practice Nursing       | Clinical Nurse Specialist           | Neonatal, High-Risk                                                   | 7/1/2005         |
| 549 | V100332 | 364SR1300N | Physician Assistants & Advanced Practice Nursing       | Clinical Nurse Specialist           | Rural Health                                                          | 7/1/2005         |
| 561 | V100612 | 363LP0223N | Physician Assistants & Advanced Practice Nursing       | Nurse Practitioner                  | Pediatrics: Acute Care                                                | 7/1/2005         |
| 1   | V110000 | 203B00000N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 |                                                                       | 7/1/2005         |
| 2   | V110100 | 203BA0401N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Addiction Medicine                                                    | 7/1/2005         |
| 5   | V110200 | 203BA0200N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Allergy                                                               | 7/1/2005         |
| 3   | V110300 | 203BA0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Allergy & Immunology                                                  | 7/1/2005         |
| 4   | V110301 | 203BI0005N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology, Clinical & Laboratory: Allergy & Immunology               | 7/1/2005         |
| 6   | V110400 | 203BA0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Anesthesiology                                                        | 7/1/2005         |
| 7   | V110401 | 203BC0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Critical Care Medicine: Anesthesiology                                | 7/1/2005         |
| 8   | V110402 | 203BP0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pain Management - Anesthesiology                                      | 7/1/2005         |
| 685 | V110403 | 203BA0004X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Anesthesiology: Pediatric Anesthesiology                              | 7/1/2005         |
| 695 | V110404 | 203BP0000X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pain Management                                                       | 7/1/2005         |
| 9   | V110500 | 203BB0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Body Imaging                                                          | 7/1/2005         |
| 10  | V110600 | 203BC0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Cardiology                                                            | 7/1/2005         |
| 11  | V110700 | 203BD0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Dermatology                                                           | 7/1/2005         |
| 12  | V110701 | 203BI0002N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology, Clinical & Laboratory Dermatological                      | 7/1/2005         |
| 13  | V110702 | 203BD0901N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Dermatopathology: Dermatology                                         | 7/1/2005         |
| 686 | V110703 | 203BD0002X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Dermatology: Pediatric Dermatology                                    | 7/1/2005         |
| 14  | V110800 | 203BE0004Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Emergency Medicine                                                    | 7/1/2005         |
| 15  | V110801 | 203BT0002Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Toxicology, Medical: Emergency Medicine                               | 7/1/2005         |
| 17  | V110803 | 203BS0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Sports Medicine: Emergency Medicine                                   | 7/1/2005         |
| 687 | V110804 | 203BE0005X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Emergency Medicine: Undersea and Hyperbaric Medicine                  | 7/1/2005         |
| 18  | V110900 | 203BF0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Family Practice                                                       | 7/1/2005         |
| 19  | V110901 | 203BG0301Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Geriatric Medicine: Family Practice                                   | 7/1/2005         |
| 20  | V110902 | 203BS0002Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Sports Medicine: Family Practice                                      | 7/1/2005         |
| 21  | V111000 | 203BG0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | General Practice                                                      | 7/1/2005         |
| 22  | V111100 | 203BG0302Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Geriatric Medicine: General Practice                                  | 7/1/2005         |
| 23  | V111200 | 203BH0003Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Hematology & Oncology                                                 | 7/1/2005         |
| 26  | V111500 | 203BI0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Internal Medicine                                                     | 7/1/2005         |
| 27  | V111501 | 203BA0002Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Adolescent Medicine: Internal Medicine                                | 7/1/2005         |
| 28  | V111502 | 203BC0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Cardiac Electrophysiology                                             | 7/1/2005         |
| 29  | V111503 | 203BC2500Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Cardiovascular Disease                                                | 7/1/2005         |
| 30  | V111504 | 203BI0006N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology, Clinical & Laboratory: Internal Medicine                  | 7/1/2005         |
| 31  | V111505 | 203BC0202Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Critical Care Medicine: Internal Medicine                             | 7/1/2005         |
| 32  | V111506 | 203BE0101Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Endocrinology, Diabetes & Metabolism                                  | 7/1/2005         |
| 33  | V111507 | 203BG0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Gastroenterology                                                      | 7/1/2005         |
| 34  | V111508 | 203BG0303Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Geriatric Medicine: Internal Medicine                                 | 7/1/2005         |
| 35  | V111509 | 203BH0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Hematology: Internal Medicine                                         | 7/1/2005         |
| 36  | V111510 | 203BI0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Infectious Diseases                                                   | 7/1/2005         |
| 37  | V111511 | 203BX0202Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Oncology, Medical                                                     | 7/1/2005         |
| 38  | V111512 | 203BN0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Nephrology                                                            | 7/1/2005         |
| 39  | V111513 | 203BP1001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pulmonary Diseases                                                    | 7/1/2005         |
| 40  | V111514 | 203BP1003Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pulmonary Medicine                                                    | 7/1/2005         |
| 41  | V111515 | 203BR0500Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Rheumatology                                                          | 7/1/2005         |
| 42  | V111516 | 203BS0003Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Sports Medicine: Internal Medicine                                    | 7/1/2005         |
| 688 | V111517 | 203BI0008X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Internal Medicine: Hepatology                                         | 7/1/2005         |
| 691 | V111518 | 203BI0011X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Internal Medicine: Interventional Cardiology                          | 7/1/2005         |
| 689 | V111519 | 203BI0009X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Internal Medicine: Pediatrics                                         | 7/1/2005         |
| 708 | V111520 | 203BP3700X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Internal Medicine: Peripheral Vascular Disease                        | 7/1/2005         |
| 690 | V111521 | 203BI0010X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Internal Medicine: Pulmonary Critical Care Medicine                   | 7/1/2005         |
| 43  | V111600 | 203BL0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Laboratory Medicine                                                   | 7/1/2005         |
| 692 | V111610 | 203BL0001X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Legal Medicine                                                        | 7/1/2005         |
| 45  | V111800 | 203BM0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Medical Diseases of the Chest                                         | 7/1/2005         |
| 46  | V111900 | 203BG0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Genetics, Medical                                                     | 7/1/2005         |
| 47  | V111901 | 203BG0202Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Genetics, Clinical Biochemical                                        | 7/1/2005         |
| 48  | V111902 | 203BG0204Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Genetics, Clinical Biochemical/ Molecular                             | 7/1/2005         |
| 49  | V111903 | 203BC0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Cytogenetics, Clinical                                                | 7/1/2005         |
| 50  | V111904 | 203BG0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Genetics, Clinical (M.D.)                                             | 7/1/2005         |
| 51  | V111905 | 203BG0203Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Genetics, Clinical Molecular                                          | 7/1/2005         |
| 693 | V111906 | 203BM0001X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Medical Genetics: Molecular Genetic Pathology                         | 7/1/2005         |
| 52  | V112000 | 203BN0200N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neopathology                                                          | 7/1/2005         |
| 53  | V112100 | 203BN0400Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neurology                                                             | 7/1/2005         |
| 694 | V112101 | 203BN0006X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neurological Surgery: Pediatric Neurological Surgery                  | 7/1/2005         |
| 55  | V112200 | 203BN0402Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neurology, Child                                                      | 7/1/2005         |
| 54  | V112300 | 203BN0700Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neuroradiology                                                        | 7/1/2005         |
| 58  | V112400 | 203BN0901Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Nuclear Cardiology                                                    | 7/1/2005         |
| 59  | V112500 | 203BN0902Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Nuclear Imaging & Therapy                                             | 7/1/2005         |
| 56  | V112600 | 203BN0900Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Nuclear Medicine                                                      | 7/1/2005         |
| 57  | V112601 | 203BN0903Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Nuclear Medicine, In Vivo & In Vitro                                  | 7/1/2005         |
| 66  | V112800 | 203BX0000N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Obstetrics                                                            | 7/1/2005         |
| 61  | V112900 | 203BX0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Obstetrics & Gynecology                                               | 7/1/2005         |
| 62  | V112901 | 203BC0203Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Critical Care Medicine: OB/GYN                                        | 7/1/2005         |
| 63  | V112902 | 203BX0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Oncology, Gynecologic                                                 | 7/1/2005         |
| 64  | V112903 | 203BM0101Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Maternal & Fetal Medicine                                             | 7/1/2005         |
| 65  | V112904 | 203BE0102Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Endocrinology, Reproductive                                           | 7/1/2005         |
| 67  | V113000 | 203BX0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Ophthalmology                                                         | 7/1/2005         |
| 718 | V113001 | 203BX0006X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Opthalmology: Pediatric Opthalmology                                  | 7/1/2005         |
| 69  | V113200 | 203BX2100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Osteopathic Manipulative Medicine, Special Proficiency                | 7/1/2005         |
| 70  | V113300 | 203BX0500Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Otolaryngology                                                        | 7/1/2005         |
| 71  | V113301 | 203BX0901N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Otology & Neurotology                                                 | 7/1/2005         |
| 72  | V113302 | 203BP0212Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Otolaryngology                                              | 7/1/2005         |
| 73  | V113400 | 203BX0900N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Otology                                                               | 7/1/2005         |
| 74  | V113500 | 203BX0600Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Otorhinolaryngology                                                   | 7/1/2005         |
| 75  | V113600 | 203BS0130Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Otorhinolaryngology & Facial Plastic Surgery                 | 7/1/2005         |
| 76  | V113700 | 203BP0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology                                                             | 7/1/2005         |
| 77  | V113701 | 203BP0102Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology, Anatomic & Clinical                                        | 7/1/2005         |
| 78  | V113702 | 203BP0101Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology, Anatomic                                                   | 7/1/2005         |
| 79  | V113703 | 203BP0103Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology, Anatomic & Laboratory Medicine                             | 7/1/2005         |
| 80  | V113704 | 203BB0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Blood Banking & Transfusion Medicine                                  | 7/1/2005         |
| 81  | V113705 | 203BP0104Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology, Chemical                                                   | 7/1/2005         |
| 82  | V113706 | 203BP0105Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology, Clinical                                                   | 7/1/2005         |
| 83  | V113707 | 203BC0500Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Cytopathology                                                         | 7/1/2005         |
| 84  | V113708 | 203BD0900Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Dermatopathology                                                      | 7/1/2005         |
| 85  | V113709 | 203BF0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Forensic Pathology                                                    | 7/1/2005         |
| 86  | V113710 | 203BH0002Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Hematology: Pathology                                                 | 7/1/2005         |
| 87  | V113711 | 203BI0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunopathology                                                       | 7/1/2005         |
| 88  | V113712 | 203BM0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Medical Microbiology                                                  | 7/1/2005         |
| 89  | V113713 | 203BN0500Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neuropathology                                                        | 7/1/2005         |
| 90  | V113714 | 203BP0213Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Pathology                                                   | 7/1/2005         |
| 697 | V113715 | 203BP0003X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology: Selective Pathology                                        | 7/1/2005         |
| 701 | V113716 | 203BP0007X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology: Molecular Genetic Pathology                                | 7/1/2005         |
| 91  | V113800 | 203BP0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Allergy & Immunology                                        | 7/1/2005         |
| 92  | V113900 | 203BP0209Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Intensive Care                                              | 7/1/2005         |
| 93  | V114000 | 203BP0211Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Neurology                                                   | 7/1/2005         |
| 702 | V114001 | 203BP0008X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatrics: Neurodevelopmental Disabilities                           | 7/1/2005         |
| 700 | V114002 | 203BP0006X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatrics: Developmental - Behavioral Pediatrics                     | 7/1/2005         |
| 94  | V114100 | 203BP0806N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry, Pediatric                                                 | 7/1/2005         |
| 96  | V114200 | 203BP0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatrics                                                            | 7/1/2005         |
| 97  | V114201 | 203BA0003Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Adolescent Medicine: Pediatrics                                       | 7/1/2005         |
| 98  | V114202 | 203BI0007N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology, Clinical & Laboratory: Pediatric                          | 7/1/2005         |
| 99  | V114203 | 203BP0220N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Medical Toxocology                                          | 7/1/2005         |
| 100 | V114204 | 203BN0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neonatal-Perinatal Medicine                                           | 7/1/2005         |
| 101 | V114205 | 203BP0202Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Cardiology                                                  | 7/1/2005         |
| 102 | V114206 | 203BP0203Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Critical Care Medicine                                      | 7/1/2005         |
| 103 | V114207 | 203BP0204Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Emergency Medicine                                          | 7/1/2005         |
| 104 | V114208 | 203BP0205Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Endocrinology                                               | 7/1/2005         |
| 105 | V114209 | 203BP0206Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Gastroenterology                                            | 7/1/2005         |
| 106 | V114210 | 203BP0207Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Hematology Oncology                                         | 7/1/2005         |
| 107 | V114211 | 203BP0208Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Infectious Diseases                                         | 7/1/2005         |
| 108 | V114212 | 203BP0210Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Nephrology                                                  | 7/1/2005         |
| 109 | V114213 | 203BP0214Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Pulmonology                                                 | 7/1/2005         |
| 110 | V114215 | 203BP0216Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Rheumatology                                                | 7/1/2005         |
| 111 | V114216 | 203BS0004Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Sports Medicine: Pediatrics                                           | 7/1/2005         |
| 95  | V114300 | 203BP0215N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pediatric Radiology                                                   | 7/1/2005         |
| 112 | V114400 | 203BP2600N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pharmacology, Clinical                                                | 7/1/2005         |
| 113 | V114500 | 203BP0400Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Physical Medicine & Rehabilitation                                    | 7/1/2005         |
| 703 | V114501 | 203BP0009X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Physical Medicine & Rehabilitation: Pain Management                   | 7/1/2005         |
| 704 | V114502 | 203BP0010X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Physical Medicine & Rehabilitation: Pediatric Rehabilitation Medicine | 7/1/2005         |
| 713 | V114503 | 203BS0010X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Physical Medicine & Rehabilitation: Sports Medicine                   | 7/1/2005         |
| 698 | V114504 | 203BP0004X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Physical Medicine and Rehabilitation: Spinal Cord Injury              | 7/1/2005         |
| 114 | V114600 | 203BP0500Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Preventive Medicine, General                                          | 7/1/2005         |
| 115 | V114601 | 203BA0101Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Aerospace Medicine: Preventive Medicine                               | 7/1/2005         |
| 116 | V114602 | 203BT0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Toxicology, Medical: Preventive Medicine                              | 7/1/2005         |
| 117 | V114603 | 203BX0104Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Occupational Medicine: Preventive Medicine                            | 7/1/2005         |
| 118 | V114604 | 203BX0105Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Occupational-Environmental Medicine: Preventive Medicine              | 7/1/2005         |
| 119 | V114605 | 203BP0901N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Public Health & General Preventive Medicine                           | 7/1/2005         |
| 120 | V114606 | 203BU0300Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Underseas Medicine: Preventive Medicine                               | 7/1/2005         |
| 712 | V114607 | 203BS0009X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Preventive Medicine: Sports Medicine                                  | 7/1/2005         |
| 705 | V114608 | 203BP0011X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Preventive Medicine: Undersea and Hyperbaric Medicine                 | 7/1/2005         |
| 121 | V114700 | 203BP0600Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Proctology                                                            | 7/1/2005         |
| 123 | V114800 | 203BP0801Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry & Neurology                                                | 7/1/2005         |
| 124 | V114801 | 203BP0802Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry, Addiction                                                 | 7/1/2005         |
| 125 | V114802 | 203BP0804Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry, Child & Adolescent                                        | 7/1/2005         |
| 126 | V114803 | 203BN0600Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neurophysiology, Clinical                                             | 7/1/2005         |
| 127 | V114804 | 203BF0202N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Forensic Psychiatry                                                   | 7/1/2005         |
| 128 | V114805 | 203BP0805Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry, Geriatric                                                 | 7/1/2005         |
| 131 | V114808 | 203BP0800Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry                                                            | 7/1/2005         |
| 699 | V114809 | 203BP0005X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry & Neurology: Neurodevelopmental Disabilities               | 7/1/2005         |
| 707 | V114810 | 203BP0014X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry & Neurology: Pain Management                               | 7/1/2005         |
| 122 | V114900 | 203BP0803Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychiatry, Child                                                     | 7/1/2005         |
| 133 | V115100 | 203BR0002Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiation Therapy                                                     | 7/1/2005         |
| 142 | V115200 | 203BP0107N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pathology, Radioisotopic                                              | 7/1/2005         |
| 134 | V115300 | 203BR0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology                                                             | 7/1/2005         |
| 135 | V115301 | 203BR0202Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology, Diagnostic                                                 | 7/1/2005         |
| 136 | V115302 | 203BN0904Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Nuclear Radiology                                                     | 7/1/2005         |
| 138 | V115304 | 203BR0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiation Oncology                                                    | 7/1/2005         |
| 139 | V115305 | 203BR0205N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiological Physics                                                  | 7/1/2005         |
| 141 | V115307 | 203BR0204N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology, Vascular & Interventional                                  | 7/1/2005         |
| 709 | V115308 | 203BR0004X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology: Abdominal Radiology                                        | 7/1/2005         |
| 710 | V115309 | 203BR0005X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology: Musculoskeletal Radiology                                  | 7/1/2005         |
| 143 | V115400 | 203BR0402Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Rehabilitation Medicine                                               | 7/1/2005         |
| 168 | V115701 | 203BS0129Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, General Vascular                                             | 7/1/2005         |
| 170 | V115703 | 203BS0120Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Pediatric                                                    | 7/1/2005         |
| 171 | V115704 | 203BS0105Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Hand                                                         | 7/1/2005         |
| 172 | V115705 | 203BS0102Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgical Critical Care: Surgery                                       | 7/1/2005         |
| 146 | V115800 | 203BS0133N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Cardiovascular                                               | 7/1/2005         |
| 147 | V115900 | 203BS0101Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Colon & Rectal Surgery                                       | 7/1/2005         |
| 148 | V116000 | 203BD0101Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Dermatology Micrographic Surgery                                      | 7/1/2005         |
| 149 | V116100 | 203BS0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, General                                                      | 7/1/2005         |
| 150 | V116200 | 203BS0108N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Head & Neck                                                  | 7/1/2005         |
| 152 | V116400 | 203BS0110Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Neurological                                                 | 7/1/2005         |
| 154 | V116500 | 203BS0111Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Obstetric & Gynecologic                                      | 7/1/2005         |
| 155 | V116600 | 203BS0113Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Orthopedic                                                   | 7/1/2005         |
| 156 | V116700 | 203BS0114N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Orthopedic, Adult Reconstructive                             | 7/1/2005         |
| 157 | V116800 | 203BS0106Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Hand: Orthopedic Surgery                                     | 7/1/2005         |
| 714 | V116801 | 203BS0134X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery: Micrographic Surgery                                         | 7/1/2005         |
| 158 | V116900 | 203BS0115N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Orthopedic, Musculoskeletal Oncology                         | 7/1/2005         |
| 159 | V117000 | 203BS0116N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Orthopedic, Pediatric                                        | 7/1/2005         |
| 160 | V117100 | 203BS0117N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Orthopedic, Spine                                            | 7/1/2005         |
| 162 | V117300 | 203BS0119N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Orthopedic, Trauma                                           | 7/1/2005         |
| 165 | V117400 | 203BS0121Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Plastic                                                      | 7/1/2005         |
| 166 | V117401 | 203BS0107Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Hand: Plastic Surgery                                        | 7/1/2005         |
| 696 | V117402 | 203BP0002X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Plastic Surgery: Craniofacial Surgery                                 | 7/1/2005         |
| 706 | V117403 | 203BP0013X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Plastic Surgery: Plastic Surgery Within the Head and Neck             | 7/1/2005         |
| 163 | V117500 | 203BS0122Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Plastic & Reconstructive                                     | 7/1/2005         |
| 174 | V117700 | 203BS0125Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Thoracic                                                     | 7/1/2005         |
| 173 | V117800 | 203BS0126Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Thoracic Cardiovascular                                      | 7/1/2005         |
| 175 | V117900 | 203BS0127N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Traumatic                                                    | 7/1/2005         |
| 176 | V118000 | 203BS0128Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Urological                                                   | 7/1/2005         |
| 177 | V118100 | 203BU0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Ultrasound, Diagnostic                                                | 7/1/2005         |
| 178 | V118200 | 203BU0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Urology                                                               | 7/1/2005         |
| 715 | V118201 | 203BU0002X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Urology, Pediatric Urology                                            | 7/1/2005         |
| 569 | V118301 | 203BA0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Adolescent Medicine                                                   | 7/1/2005         |
| 570 | V118302 | 203BA0001N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Adolescent Medicine: Family Practice                                  | 7/1/2005         |
| 571 | V118303 | 203BA0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Aerospace Medicine                                                    | 7/1/2005         |
| 572 | V118304 | 203BA0202N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Allergy & Immunology: Internal Medicine                               | 7/1/2005         |
| 573 | V118305 | 203BA0501N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Adolescent Only, Under 16                                             | 7/1/2005         |
| 574 | V118306 | 203BA0502N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Adolescent Only, Under 21                                             | 7/1/2005         |
| 575 | V118307 | 203BA0503N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Age Specific, Greater than 1 Year Old                                 | 7/1/2005         |
| 576 | V118308 | 203BA0504N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Age Specific, Newborns Only                                           | 7/1/2005         |
| 577 | V118309 | 203BB0000N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Blood Banking                                                         | 7/1/2005         |
| 578 | V118310 | 203BC0001Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Cardiac Electrophysiology, Clinical                                   | 7/1/2005         |
| 579 | V118311 | 203BC0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Critical Care Medicine                                                | 7/1/2005         |
| 580 | V118312 | 203BD0300N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Diabetes                                                              | 7/1/2005         |
| 581 | V118313 | 203BE0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Endocrinology                                                         | 7/1/2005         |
| 582 | V118314 | 203BG0300N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Geriatric Medicine                                                    | 7/1/2005         |
| 583 | V118315 | 203BG0400N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Gynecology                                                            | 7/1/2005         |
| 584 | V118316 | 203BH0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Hematology                                                            | 7/1/2005         |
| 585 | V118317 | 203BI0001N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology, Clinical & Laboratory                                     | 7/1/2005         |
| 586 | V118318 | 203BI0003Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology, Dermatological                                            | 7/1/2005         |
| 587 | V118319 | 203BI0004Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Immunology: Laboratory, Diagnostic                                    | 7/1/2005         |
| 588 | V118320 | 203BI0400N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Infertility                                                           | 7/1/2005         |
| 589 | V118321 | 203BN0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Neonatology                                                           | 7/1/2005         |
| 590 | V118322 | 203BP0903Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Public Health: Preventive Medicine                                    | 7/1/2005         |
| 591 | V118323 | 203BP1200N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pharmacotherapy                                                       | 7/1/2005         |
| 592 | V118324 | 203BP1300N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Psychopharmacy                                                        | 7/1/2005         |
| 593 | V118325 | 203BP2900N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Pain Medicine                                                         | 7/1/2005         |
| 594 | V118326 | 203BR0201Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology, Angiography & Interventional                               | 7/1/2005         |
| 595 | V118327 | 203BR0203N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radiology, Therapeutic                                                | 7/1/2005         |
| 596 | V118328 | 203BR0300N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Radium Therapy                                                        | 7/1/2005         |
| 597 | V118329 | 203BR0600N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Rhinology                                                             | 7/1/2005         |
| 598 | V118330 | 203BR0700Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Roentgenology                                                         | 7/1/2005         |
| 599 | V118331 | 203BR0701Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Roentgenology, Diagnostic                                             | 7/1/2005         |
| 600 | V118332 | 203BS0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Sports Medicine                                                       | 7/1/2005         |
| 601 | V118333 | 203BS0104N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Abdominal                                                    | 7/1/2005         |
| 602 | V118334 | 203BS0123Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Surgery, Facial Plastic                                               | 7/1/2005         |
| 603 | V118335 | 203BT0000Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Toxicology, Medical                                                   | 7/1/2005         |
| 604 | V118336 | 203BT0100N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Thermography                                                          | 7/1/2005         |
| 605 | V118337 | 203BX0100Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Occupational Medicine                                                 | 7/1/2005         |
| 606 | V118338 | 203BX0200Y | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Oncology                                                              | 7/1/2005         |
| 607 | V118339 | 203BX0601N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Otorhinolaryngology & Head-Neck                                       | 7/1/2005         |
| 608 | V118340 | 203BX0800N | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Orthopedic                                                            | 7/1/2005         |
| 716 | V118341 | 203BX0004X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Orthopedic Surgery: Foot and Ankle Orthopedics                        | 7/1/2005         |
| 717 | V118342 | 203BX0005X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Orthopedic Surgery: Sports Medicine                                   | 7/1/2005         |
| 711 | V118343 | 203BS0008X | Physicians (M.D. and D.O.)                             | Physician/Osteopath                 | Sports Medicine - OMM                                                 | 7/1/2005         |
| 617 | V130104 | 225XC0400N | Respiratory, Rehabilitative and Restorative Service    | Occupational Therapist              | Case Management                                                       | 7/1/2005         |
| 611 | V130310 | 2251C0400N | Respiratory, Rehabilitative and Restorative Service    | Physical Therapist                  | Case Management                                                       | 7/1/2005         |
| 376 | V130508 | 225900000N | Respiratory, Rehabilitative and Restorative Service    | Respiratory Therapist               |                                                                       | 7/1/2005         |
| 614 | V130511 | 2259P1700N | Respiratory, Rehabilitative and Restorative Service    | Respiratory Therapist               | Perinatal                                                             | 7/1/2005         |
| 441 | V150203 | 246VC2901N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Cardiovascular: Invasive Technology                                   | 7/1/2005         |
| 442 | V150204 | 246VC0100N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Cardiology                                                            | 7/1/2005         |
| 443 | V150205 | 246VC2400N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Cardiopulmonary-Cardiovascular                                        | 7/1/2005         |
| 445 | V150207 | 246VP3600N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Perfusionist                                                          | 7/1/2005         |
| 446 | V150208 | 246WE0400N | Technologists, Technicians and Other Technical Service | Technician, Cardiology              | ECG                                                                   | 7/1/2005         |
| 462 | V150304 | 246VS1301N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Sonography, Diagnostic Cardiac                                        | 7/1/2005         |
| 469 | V150311 | 2471R0003N | Technologists, Technicians and Other Technical Service | Radiologic Technologist             | Radiation Physicist                                                   | 7/1/2005         |
| 471 | V150313 | 2471R1500N | Technologists, Technicians and Other Technical Service | Radiologic Technologist             | Radiographer                                                          | 7/1/2005         |
| 474 | V150316 | 2471D1300N | Technologists, Technicians and Other Technical Service | Radiologic Technologist             | Dosimetrist, Medical                                                  | 7/1/2005         |
| 641 | V150320 | 2471M1201N | Technologists, Technicians and Other Technical Service | Radiologic Technologist             | Magnetic Resonance Imaging (MRI): Radiation Therapy                   | 7/1/2005         |
| 644 | V150323 | 2471Q0002N | Technologists, Technicians and Other Technical Service | Radiologic Technologist             | Quality Management: Radiographer                                      | 7/1/2005         |
| 629 | V150701 | 246VC2902N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Cardiovascular: Noninvasive Technology                                | 7/1/2005         |
| 630 | V150702 | 246VC2903N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Cardiovascular: Vascular Technology                                   | 7/1/2005         |
| 631 | V150703 | 246VV0100N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology | Vascular                                                              | 7/1/2005         |
| 725 | V150704 | 246V00000X | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Cardiology |                                                                       | 7/1/2005         |
| 632 | V150801 | 246WC3000N | Technologists, Technicians and Other Technical Service | Technician, Cardiology              | Cardiographic                                                         | 7/1/2005         |
| 636 | V151002 | 246ZF0200N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Other      | Forensic                                                              | 7/1/2005         |
| 638 | V151004 | 246ZV0500N | Technologists, Technicians and Other Technical Service | Specialist/Technologist, Other      | Virology                                                              | 7/1/2005         |
| 732 | V160100 | 353B00000X | Physicians (Other Roles)                               | Physician/Osteopath (Other Roles)   |                                                                       | 7/1/2005         |
| 645 | V160101 | 353BL0002N | Physicians (Other Roles)                               | Physician/Osteopath                 | Laboratory Service Provider                                           | 7/1/2005         |
| 646 | V160102 | 353BS0900N | Physicians (Other Roles)                               | Physician/Osteopath                 | Supplier                                                              | 7/1/2005         |

<span id="_Ref488675103" class="anchor"></span>Table 7: Inactivated Person Class Codes—Kernel Patch XU\*8.0\*531

### Patch XU\*8.0\*531

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 7</u> lists all inactivated Person Class codes released with Kernel Patch XU\*8.0\*531 (released on 02/17/2010):

<table style="width:100%;">
<caption><p><span id="_Ref488675168" class="anchor"></span>Table 8: Inactivated Person Class Codes—Kernel Patch XU*8.0*671</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>VA Code</th>
<th>X12 Code</th>
<th>Provider Type</th>
<th>Classification</th>
<th>Area of Specialization</th>
<th>Date Inactivated</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1037</td>
<td><em>No VA CODE</em></td>
<td>287300000X</td>
<td>Hospitals</td>
<td></td>
<td></td>
<td>10/01/2009</td>
</tr>
<tr class="even">
<td>1066</td>
<td><em>No VA CODE</em></td>
<td><p>317400</p>
<p>000X</p></td>
<td>Christian Science Facility</td>
<td></td>
<td></td>
<td>10/01/2009</td>
</tr>
</tbody>
</table>

<span id="_Ref488675168" class="anchor"></span>Table 8: Inactivated Person Class Codes—Kernel Patch XU\*8.0\*671

### Patch XU\*8.0\*671

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 8</u> lists all inactivated Person Class codes released with Kernel Patch XU\*8.0\*671 (released on 08/17/2017):

| IEN  | VA Code | X12 Code   | Provider Type                                                                | Classification                                                                   | Area of Specialization                                                | Date Inactivated |
|------|---------|------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------------|-----------------------------------------------------------------------|------------------|
| 1    | V110000 | 203B00000N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              |                                                                       | 9/1/2016         |
| 2    | V110100 | 203BA0401N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Addiction Medicine                                                    | 9/1/2016         |
| 3    | V110300 | 203BA0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Allergy & Immunology                                                  | 9/1/2016         |
| 4    | V110301 | 203BI0005N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory: Allergy & Immunology               | 9/1/2016         |
| 5    | V110200 | 203BA0200N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Allergy                                                               | 9/1/2016         |
| 6    | V110400 | 203BA0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Anesthesiology                                                        | 9/1/2016         |
| 7    | V110401 | 203BC0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine: Anesthesiology                                | 7/12/2017        |
| 8    | V110402 | 203BP0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pain Management - Anesthesiology                                      | 7/12/2017        |
| 9    | V110500 | 203BB0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Body Imaging                                                          | 7/12/2017        |
| 10   | V110600 | 203BC0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiology                                                            | 7/12/2017        |
| 11   | V110700 | 203BD0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatology                                                           | 7/12/2017        |
| 12   | V110701 | 203BI0002N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory Dermatological                      | 7/12/2017        |
| 13   | V110702 | 203BD0901N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatopathology: Dermatology                                         | 7/12/2017        |
| 14   | V110800 | 203BE0004Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Emergency Medicine                                                    | 7/12/2017        |
| 15   | V110801 | 203BT0002Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Toxicology, Medical: Emergency Medicine                               | 7/12/2017        |
| 16   | V110802 |            | Physicians (M.D. and D.O.)                                                   | Emergency Medicine                                                               | Pediatric Emergency Medicine                                          | 10/20/1998       |
| 17   | V110803 | 203BS0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Emergency Medicine                                   | 7/12/2017        |
| 18   | V110900 | 203BF0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Family Practice                                                       | 7/12/2017        |
| 19   | V110901 | 203BG0301Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine: Family Practice                                   | 7/12/2017        |
| 20   | V110902 | 203BS0002Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Family Practice                                      | 7/12/2017        |
| 21   | V111000 | 203BG0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | General Practice                                                      | 7/12/2017        |
| 22   | V111100 | 203BG0302Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine: General Practice                                  | 7/12/2017        |
| 23   | V111200 | 203BH0003Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology & Oncology                                                 | 7/12/2017        |
| 24   | V111300 |            | Physicians (M.D. and D.O.)                                                   | Intern, Allopathic                                                               |                                                                       | 5/3/2005         |
| 25   | V111400 |            | Physicians (M.D. and D.O.)                                                   | Intern, Osteopathic                                                              |                                                                       | 5/3/2005         |
| 26   | V111500 | 203BI0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine                                                     | 7/12/2017        |
| 27   | V111501 | 203BA0002Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine: Internal Medicine                                | 7/12/2017        |
| 28   | V111502 | 203BC0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiac Electrophysiology                                             | 7/12/2017        |
| 29   | V111503 | 203BC2500Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiovascular Disease                                                | 7/12/2017        |
| 30   | V111504 | 203BI0006N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory: Internal Medicine                  | 7/12/2017        |
| 31   | V111505 | 203BC0202Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine: Internal Medicine                             | 7/12/2017        |
| 32   | V111506 | 203BE0101Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Endocrinology, Diabetes & Metabolism                                  | 7/12/2017        |
| 33   | V111507 | 203BG0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Gastroenterology                                                      | 7/12/2017        |
| 34   | V111508 | 203BG0303Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine: Internal Medicine                                 | 7/12/2017        |
| 35   | V111509 | 203BH0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology: Internal Medicine                                         | 7/12/2017        |
| 36   | V111510 | 203BI0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Infectious Diseases                                                   | 7/12/2017        |
| 37   | V111511 | 203BX0202Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Oncology, Medical                                                     | 7/12/2017        |
| 38   | V111512 | 203BN0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nephrology                                                            | 7/12/2017        |
| 39   | V111513 | 203BP1001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pulmonary Diseases                                                    | 7/12/2017        |
| 40   | V111514 | 203BP1003Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pulmonary Medicine                                                    | 7/12/2017        |
| 41   | V111515 | 203BR0500Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Rheumatology                                                          | 7/12/2017        |
| 42   | V111516 | 203BS0003Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Internal Medicine                                    | 7/12/2017        |
| 43   | V111600 | 203BL0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Laboratory Medicine                                                   | 7/12/2017        |
| 44   | V111700 |            | Physicians (M.D. and D.O.)                                                   | Legal Medicine                                                                   |                                                                       | 10/20/1998       |
| 45   | V111800 | 203BM0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Medical Diseases of the Chest                                         | 7/12/2017        |
| 46   | V111900 | 203BG0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Medical                                                     | 7/12/2017        |
| 47   | V111901 | 203BG0202Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical Biochemical                                        | 7/12/2017        |
| 48   | V111902 | 203BG0204Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical Biochemical/ Molecular                             | 7/12/2017        |
| 49   | V111903 | 203BC0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cytogenetics, Clinical                                                | 7/12/2017        |
| 50   | V111904 | 203BG0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical (M.D.)                                             | 7/12/2017        |
| 51   | V111905 | 203BG0203Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical Molecular                                          | 7/12/2017        |
| 52   | V112000 | 203BN0200N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neopathology                                                          | 7/12/2017        |
| 53   | V112100 | 203BN0400Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurology                                                             | 7/12/2017        |
| 54   | V112300 | 203BN0700Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neuroradiology                                                        | 7/12/2017        |
| 55   | V112200 | 203BN0402Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurology, Child                                                      | 7/12/2017        |
| 56   | V112600 | 203BN0900Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Medicine                                                      | 7/12/2017        |
| 57   | V112601 | 203BN0903Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Medicine, In Vivo & In Vitro                                  | 7/12/2017        |
| 58   | V112400 | 203BN0901Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Cardiology                                                    | 7/12/2017        |
| 59   | V112500 | 203BN0902Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Imaging & Therapy                                             | 7/12/2017        |
| 60   | V112700 |            | Physicians (M.D. and D.O.)                                                   | Nutrition                                                                        |                                                                       | 10/20/1998       |
| 61   | V112900 | 203BX0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Obstetrics & Gynecology                                               | 7/12/2017        |
| 62   | V112901 | 203BC0203Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine: OB/GYN                                        | 7/12/2017        |
| 63   | V112902 | 203BX0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Oncology, Gynecologic                                                 | 7/12/2017        |
| 64   | V112903 | 203BM0101Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Maternal & Fetal Medicine                                             | 7/12/2017        |
| 65   | V112904 | 203BE0102Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Endocrinology, Reproductive                                           | 7/12/2017        |
| 66   | V112800 | 203BX0000N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Obstetrics                                                            | 7/12/2017        |
| 67   | V113000 | 203BX0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Ophthalmology                                                         | 7/12/2017        |
| 68   | V113100 |            | Physicians (M.D. and D.O.)                                                   | Opthal-ot-laryngo-rhinlogy                                                       |                                                                       | 10/20/1998       |
| 69   | V113200 | 203BX2100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Osteopathic Manipulative Medicine, Special Proficiency                | 7/12/2017        |
| 70   | V113300 | 203BX0500Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otolaryngology                                                        | 7/12/2017        |
| 71   | V113301 | 203BX0901N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otology & Neurotology                                                 | 7/12/2017        |
| 72   | V113302 | 203BP0212Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Otolaryngology                                              | 7/12/2017        |
| 73   | V113400 | 203BX0900N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otology                                                               | 7/12/2017        |
| 74   | V113500 | 203BX0600Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otorhinolaryngology                                                   | 7/12/2017        |
| 75   | V113600 | 203BS0130Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Otorhinolaryngology & Facial Plastic Surgery                 | 7/12/2017        |
| 76   | V113700 | 203BP0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology                                                             | 7/12/2017        |
| 77   | V113701 | 203BP0102Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Anatomic & Clinical                                        | 7/12/2017        |
| 78   | V113702 | 203BP0101Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Anatomic                                                   | 7/12/2017        |
| 79   | V113703 | 203BP0103Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Anatomic & Laboratory Medicine                             | 7/12/2017        |
| 80   | V113704 | 203BB0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Blood Banking & Transfusion Medicine                                  | 7/12/2017        |
| 81   | V113705 | 203BP0104Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Chemical                                                   | 7/12/2017        |
| 82   | V113706 | 203BP0105Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Clinical                                                   | 7/12/2017        |
| 83   | V113707 | 203BC0500Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cytopathology                                                         | 7/12/2017        |
| 84   | V113708 | 203BD0900Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatopathology                                                      | 7/12/2017        |
| 85   | V113709 | 203BF0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Forensic Pathology                                                    | 7/12/2017        |
| 86   | V113710 | 203BH0002Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology: Pathology                                                 | 7/12/2017        |
| 87   | V113711 | 203BI0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunopathology                                                       | 7/12/2017        |
| 88   | V113712 | 203BM0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Medical Microbiology                                                  | 7/12/2017        |
| 89   | V113713 | 203BN0500Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neuropathology                                                        | 7/12/2017        |
| 90   | V113714 | 203BP0213Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Pathology                                                   | 7/12/2017        |
| 91   | V113800 | 203BP0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Allergy & Immunology                                        | 7/12/2017        |
| 92   | V113900 | 203BP0209Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Intensive Care                                              | 7/12/2017        |
| 93   | V114000 | 203BP0211Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Neurology                                                   | 7/12/2017        |
| 94   | V114100 | 203BP0806N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Pediatric                                                 | 7/12/2017        |
| 95   | V114300 | 203BP0215N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Radiology                                                   | 7/12/2017        |
| 96   | V114200 | 203BP0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatrics                                                            | 7/12/2017        |
| 97   | V114201 | 203BA0003Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine: Pediatrics                                       | 7/12/2017        |
| 98   | V114202 | 203BI0007N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory: Pediatric                          | 7/12/2017        |
| 99   | V114203 | 203BP0220N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Medical Toxocology                                          | 7/12/2017        |
| 100  | V114204 | 203BN0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neonatal-Perinatal Medicine                                           | 7/12/2017        |
| 101  | V114205 | 203BP0202Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Cardiology                                                  | 7/12/2017        |
| 102  | V114206 | 203BP0203Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Critical Care Medicine                                      | 7/12/2017        |
| 103  | V114207 | 203BP0204Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Emergency Medicine                                          | 7/12/2017        |
| 104  | V114208 | 203BP0205Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Endocrinology                                               | 7/12/2017        |
| 105  | V114209 | 203BP0206Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Gastroenterology                                            | 7/12/2017        |
| 106  | V114210 | 203BP0207Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Hematology Oncology                                         | 7/12/2017        |
| 107  | V114211 | 203BP0208Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Infectious Diseases                                         | 7/12/2017        |
| 108  | V114212 | 203BP0210Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Nephrology                                                  | 7/12/2017        |
| 109  | V114213 | 203BP0214Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Pulmonology                                                 | 7/12/2017        |
| 110  | V114215 | 203BP0216Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Rheumatology                                                | 7/12/2017        |
| 111  | V114216 | 203BS0004Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Pediatrics                                           | 7/12/2017        |
| 112  | V114400 | 203BP2600N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pharmacology, Clinical                                                | 7/12/2017        |
| 113  | V114500 | 203BP0400Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation                                    | 7/12/2017        |
| 114  | V114600 | 203BP0500Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Preventive Medicine, General                                          | 7/12/2017        |
| 115  | V114601 | 203BA0101Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Aerospace Medicine: Preventive Medicine                               | 7/12/2017        |
| 116  | V114602 | 203BT0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Toxicology, Medical: Preventive Medicine                              | 7/12/2017        |
| 117  | V114603 | 203BX0104Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Occupational Medicine: Preventive Medicine                            | 7/12/2017        |
| 118  | V114604 | 203BX0105Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Occupational-Environmental Medicine: Preventive Medicine              | 7/12/2017        |
| 119  | V114605 | 203BP0901N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Public Health & General Preventive Medicine                           | 7/12/2017        |
| 120  | V114606 | 203BU0300Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Underseas Medicine: Preventive Medicine                               | 7/12/2017        |
| 121  | V114700 | 203BP0600Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Proctology                                                            | 7/12/2017        |
| 122  | V114900 | 203BP0803Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Child                                                     | 7/12/2017        |
| 123  | V114800 | 203BP0801Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry & Neurology                                                | 7/12/2017        |
| 124  | V114801 | 203BP0802Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Addiction                                                 | 7/12/2017        |
| 125  | V114802 | 203BP0804Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Child & Adolescent                                        | 7/12/2017        |
| 126  | V114803 | 203BN0600Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurophysiology, Clinical                                             | 7/12/2017        |
| 127  | V114804 | 203BF0202N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Forensic Psychiatry                                                   | 7/12/2017        |
| 128  | V114805 | 203BP0805Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Geriatric                                                 | 7/12/2017        |
| 129  | V114806 |            | Physicians (M.D. and D.O.)                                                   | Psychiatry and Neurology                                                         | Neurology                                                             | 10/20/1998       |
| 130  | V114807 |            | Physicians (M.D. and D.O.)                                                   | Psychiatry and Neurology                                                         | Neurology, Child                                                      | 10/20/1998       |
| 131  | V114808 | 203BP0800Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry                                                            | 7/12/2017        |
| 132  | V115000 |            | Physicians (M.D. and D.O.)                                                   | Psychoanalysis                                                                   |                                                                       | 10/20/1998       |
| 133  | V115100 | 203BR0002Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiation Therapy                                                     | 7/12/2017        |
| 134  | V115300 | 203BR0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology                                                             | 7/12/2017        |
| 135  | V115301 | 203BR0202Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Diagnostic                                                 | 7/12/2017        |
| 136  | V115302 | 203BN0904Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Radiology                                                     | 7/12/2017        |
| 137  | V115303 |            | Physicians (M.D. and D.O.)                                                   | Radiology                                                                        | Pediatric Radiology                                                   | 10/20/1998       |
| 138  | V115304 | 203BR0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiation Oncology                                                    | 7/12/2017        |
| 139  | V115305 | 203BR0205N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiological Physics                                                  | 7/12/2017        |
| 140  | V115306 |            | Physicians (M.D. and D.O.)                                                   | Radiology                                                                        | Radiology                                                             | 10/20/1998       |
| 141  | V115307 | 203BR0204N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Vascular & Interventional                                  | 7/12/2017        |
| 142  | V115200 | 203BP0107N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Radioisotopic                                              | 7/12/2017        |
| 143  | V115400 | 203BR0402Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Rehabilitation Medicine                                               | 7/12/2017        |
| 146  | V115800 | 203BS0133N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Cardiovascular                                               | 7/12/2017        |
| 147  | V115900 | 203BS0101Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Colon & Rectal Surgery                                       | 7/12/2017        |
| 148  | V116000 | 203BD0101Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatology Micrographic Surgery                                      | 7/12/2017        |
| 149  | V116100 | 203BS0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, General                                                      | 7/12/2017        |
| 150  | V116200 | 203BS0108N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Head & Neck                                                  | 7/12/2017        |
| 151  | V116300 |            | Physicians (M.D. and D.O.)                                                   | Surgery, Maxillofacial                                                           |                                                                       | 10/20/1998       |
| 152  | V116400 | 203BS0110Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Neurological                                                 | 7/12/2017        |
| 153  | V116401 |            | Physicians (M.D. and D.O.)                                                   | Surgery, Neurological                                                            | Critical Care Medicine                                                | 10/20/1998       |
| 154  | V116500 | 203BS0111Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Obstetric & Gynecologic                                      | 7/12/2017        |
| 155  | V116600 | 203BS0113Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic                                                   | 7/12/2017        |
| 156  | V116700 | 203BS0114N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Adult Reconstructive                             | 7/12/2017        |
| 157  | V116800 | 203BS0106Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Hand: Orthopedic Surgery                                     | 7/12/2017        |
| 158  | V116900 | 203BS0115N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Musculoskeletal Oncology                         | 7/12/2017        |
| 159  | V117000 | 203BS0116N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Pediatric                                        | 7/12/2017        |
| 160  | V117100 | 203BS0117N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Spine                                            | 7/12/2017        |
| 161  | V117200 |            | Physicians (M.D. and D.O.)                                                   | Surgery, Orthopaedic, Sports Medicine                                            |                                                                       | 10/20/1998       |
| 162  | V117300 | 203BS0119N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Trauma                                           | 7/12/2017        |
| 163  | V117500 | 203BS0122Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Plastic & Reconstructive                                     | 7/12/2017        |
| 164  | V117600 |            | Physicians (M.D. and D.O.)                                                   | Surgery, Plastic Facial, Otolaryngology                                          |                                                                       | 10/20/1998       |
| 165  | V117400 | 203BS0121Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Plastic                                                      | 7/12/2017        |
| 166  | V117401 | 203BS0107Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Hand: Plastic Surgery                                        | 7/12/2017        |
| 167  | V115700 |            | Physicians (M.D. and D.O.)                                                   | Surgery                                                                          |                                                                       | 10/20/1998       |
| 168  | V115701 | 203BS0129Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, General Vascular                                             | 7/12/2017        |
| 169  | V115702 |            | Physicians (M.D. and D.O.)                                                   | Surgery                                                                          | Oncology                                                              | 10/20/1998       |
| 170  | V115703 | 203BS0120Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Pediatric                                                    | 7/12/2017        |
| 171  | V115704 | 203BS0105Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Hand                                                         | 7/12/2017        |
| 172  | V115705 | 203BS0102Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgical Critical Care: Surgery                                       | 7/12/2017        |
| 173  | V117800 | 203BS0126Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Thoracic Cardiovascular                                      | 7/12/2017        |
| 174  | V117700 | 203BS0125Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Thoracic                                                     | 7/12/2017        |
| 175  | V117900 | 203BS0127N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Traumatic                                                    | 7/12/2017        |
| 176  | V118000 | 203BS0128Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Urological                                                   | 7/12/2017        |
| 177  | V118100 | 203BU0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Ultrasound, Diagnostic                                                | 7/12/2017        |
| 178  | V118200 | 203BU0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Urology                                                               | 7/12/2017        |
| 179  | V120000 |            | Podiatric Medicine and Surgery Service                                       |                                                                                  |                                                                       | 10/20/1998       |
| 182  | V120201 |            | Podiatric Medicine and Surgery Service                                       | Podiatrist                                                                       | Dermatology                                                           | 10/20/1998       |
| 183  | V120202 |            | Podiatric Medicine and Surgery Service                                       | Podiatrist                                                                       | Foot and Ankle Orthopaedics/Biomechanics                              | 10/20/1998       |
| 184  | V120203 |            | Podiatric Medicine and Surgery Service                                       | Podiatrist                                                                       | Foot and Ankle Pediatrics                                             | 10/20/1998       |
| 187  | V120206 | 213EG0000X | Podiatric Medicine & Surgery Service Providers                               | Podiatrist                                                                       | General Practice                                                      | 1/26/2009        |
| 188  | V120207 |            | Podiatric Medicine and Surgery Service                                       | Podiatrist                                                                       | Podiatric Medicine/Primary Care                                       | 10/20/1998       |
| 189  | V120208 |            | Podiatric Medicine and Surgery Service                                       | Podiatrist                                                                       | Podiatric Orthopedics                                                 | 10/20/1998       |
| 206  | V030000 |            | Dental Service                                                               |                                                                                  |                                                                       | 10/20/1998       |
| 222  | V060000 |            | Eye and Vision Services                                                      |                                                                                  |                                                                       | 10/20/1998       |
| 229  | V060700 |            | Eye and Vision Services                                                      | Optometric Assistant/Technician                                                  |                                                                       | 10/20/1998       |
| 233  | V060801 | 152WC0800N | Eye and Vision Services                                                      | Optometrist                                                                      | Contact Lens                                                          | 7/12/2017        |
| 238  | V140000 |            | Speech, Language and Hearing Service                                         |                                                                                  |                                                                       | 10/20/1998       |
| 242  | V140400 |            | Speech, Language and Hearing Service                                         | Speech and Hearing Therapist                                                     |                                                                       | 10/20/1998       |
| 245  | V090000 |            | Pharmacy Service                                                             |                                                                                  |                                                                       | 10/20/1998       |
| 247  | V090101 | 1835G0000X | Pharmacy Service Providers                                                   | Pharmacist                                                                       | General Practice                                                      | 1/26/2009        |
| 252  | V090200 | 1847P3400N | Pharmacy Service                                                             | Technician                                                                       | Pharmacy                                                              | 7/12/2017        |
| 253  | V070000 |            | Nursing Service                                                              |                                                                                  |                                                                       | 10/20/1998       |
| 254  | V070100 |            | Nursing Service                                                              | Clinical Specialist                                                              |                                                                       | 10/20/1998       |
| 255  | V070102 |            | Nursing Service                                                              | Clinical Specialist                                                              | Child and Adolescent Psychiatric and Mental Health                    | 10/20/1998       |
| 256  | V070103 |            | Nursing Service                                                              | Clinical Specialist                                                              | Community Health Nursing                                              | 10/20/1998       |
| 257  | V070104 |            | Nursing Service                                                              | Clinical Specialist                                                              | Gerontological Nursing                                                | 10/20/1998       |
| 258  | V070105 |            | Nursing Service                                                              | Clinical Specialist                                                              | Medical-Surgical Nursing                                              | 10/20/1998       |
| 261  | V070601 |            | Nursing Service                                                              | Nursing Administrator                                                            | Nursing Administration, Advanced                                      | 10/20/1998       |
| 262  | V070700 |            | Nursing Service                                                              | Nursing Administrator, Long-Term Care                                            |                                                                       | 10/20/1998       |
| 263  | V070200 |            | Nursing Service                                                              | Nurse Anesthetist (CRNA)                                                         |                                                                       | 10/20/1998       |
| 265  | V070400 |            | Nursing Service                                                              | Nurse Midwife (CNM)                                                              |                                                                       | 10/20/1998       |
| 266  | V070500 |            | Nursing Service                                                              | Nurse Practitioner                                                               |                                                                       | 10/20/1998       |
| 267  | V070501 |            | Nursing Service                                                              | Nurse Practitioner                                                               | Adult Nurse Practitioner                                              | 10/20/1998       |
| 268  | V070502 |            | Nursing Service                                                              | Nurse Practitioner                                                               | Family Nurse Practitioner                                             | 10/20/1998       |
| 269  | V070503 |            | Nursing Service                                                              | Nurse Practitioner                                                               | Gerontological Nurse Practitioner                                     | 10/20/1998       |
| 270  | V070504 |            | Nursing Service                                                              | Nurse Practitioner                                                               | Neonatal Nurse Practitioner                                           | 10/20/1998       |
| 271  | V070505 |            | Nursing Service                                                              | Nurse Practitioner                                                               | Obstetrical/Gynecological Nurse Practitioner                          | 10/20/1998       |
| 272  | V070506 |            | Nursing Service                                                              | Nurse Practitioner                                                               | Pediatric Nurse Practitioner (PNP)                                    | 10/20/1998       |
| 273  | V070507 |            | Nursing Service                                                              | Nurse Practitioner                                                               | School Nurse Practitioner                                             | 10/20/1998       |
| 309  | V070935 | 163WX1000N | Nursing Service                                                              | Registered Nurse                                                                 | Operating Room                                                        | 7/12/2017        |
| 320  | V070946 | 163WP2200N | Nursing Service                                                              | Registered Nurse                                                                 | Post-Anesthesia                                                       | 7/12/2017        |
| 327  | V070800 |            | Nursing Service                                                              | Other Nursing Services (Non-R.N.s)                                               |                                                                       | 10/20/1998       |
| 328  | V070801 |            | Nursing Service                                                              | Other Nursing Services (Non-R.N.s)                                               | Christian Science Nurse                                               | 10/20/1998       |
| 329  | V070803 |            | Nursing Service                                                              | Other Nursing Services (Non-R.N.s)                                               | Home Health Aide                                                      | 10/20/1998       |
| 331  | V070806 |            | Nursing Service                                                              | Other Nursing Services (Non-R.N.s)                                               | Nurse's Aide                                                          | 10/20/1998       |
| 334  | V040000 |            | Dietary and Nutritional Service                                              |                                                                                  |                                                                       | 10/20/1998       |
| 335  | V040100 | 1327D0700N | Dietary and Nutritional Service                                              | Dietary Manager                                                                  | Dietary Management                                                    | 7/12/2017        |
| 336  | V040101 |            | Dietary and Nutritional Service                                              | Dietary Manager                                                                  | Certified Dietary Manager                                             | 10/20/1998       |
| 344  | V050000 |            | Emergency Medical Service                                                    |                                                                                  |                                                                       | 10/20/1998       |
| 348  | V050400 |            | Emergency Medical Service                                                    | First Responder (lower skill level)                                              |                                                                       | 10/20/1998       |
| 349  | V010000 |            | Behavioral Health and Social Service                                         |                                                                                  |                                                                       | 10/20/1998       |
| 353  | V010402 | 103GC0700X | Behavioral Health & Social Service Providers                                 | Clinical Neuropsychologist                                                       | Clinical                                                              | 1/26/2009        |
| 359  | V010300 | 103S00000N | Behavioral Health and Social Service                                         | Psychoanalyst                                                                    |                                                                       | 7/12/2017        |
| 360  | V010301 | 103SA1800N | Behavioral Health and Social Service                                         | Psychoanalyst                                                                    | Affiliate                                                             | 7/12/2017        |
| 361  | V010302 | 103SA1400N | Behavioral Health and Social Service                                         | Psychoanalyst                                                                    | Associate                                                             | 7/12/2017        |
| 372  | V130000 |            | Respiratory, Rehabilitative and Restorative Service                          |                                                                                  |                                                                       | 10/20/1998       |
| 373  | V130504 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Inhalation Therapist                                                  | 10/20/1998       |
| 374  | V130505 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Pulmonary Function Technician                                         | 10/20/1998       |
| 376  | V130508 | 225900000N | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Therapist                                                            |                                                                       | 7/12/2017        |
| 377  | V130501 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Certified Respiratory Therapy Technician                              | 10/20/1998       |
| 378  | V130502 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Graduate Respiratory Therapist                                        | 10/20/1998       |
| 379  | V130503 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Graduate Respiratory Therapy Technician                               | 10/20/1998       |
| 380  | V130507 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Registered Respiratory Therapist                                      | 10/20/1998       |
| 381  | V130509 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Respiratory Therapy Assistant                                         | 10/20/1998       |
| 382  | V130510 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    | Respiratory Therapy Technician                                        | 10/20/1998       |
| 394  | V130401 |            | Respiratory, Rehabilitative and Restorative Service                          | Rehabilitation Practitioner                                                      | Associate Rehabilitation Practitioner                                 | 10/20/1998       |
| 395  | V130402 |            | Respiratory, Rehabilitative and Restorative Service                          | Rehabilitation Practitioner                                                      | Professional Rehabilitation Practitioner                              | 10/20/1998       |
| 397  | V130403 |            | Respiratory, Rehabilitative and Restorative Service                          | Rehabilitation Practitioner                                                      | Rehabilitation Coordinator                                            | 10/20/1998       |
| 401  | V130103 |            | Respiratory, Rehabilitative and Restorative Service                          | Occupational Therapist                                                           | Registered Occupational Therapist                                     | 10/20/1998       |
| 403  | V130200 |            | Respiratory, Rehabilitative and Restorative Service                          | Other                                                                            |                                                                       | 10/20/1998       |
| 411  | V130208 |            | Respiratory, Rehabilitative and Restorative Service                          | Other                                                                            | Orthotist-Prosthetist                                                 | 10/20/1998       |
| 413  | V130212 |            | Respiratory, Rehabilitative and Restorative Service                          | Other                                                                            | Vocational Specialist                                                 | 10/20/1998       |
| 414  | V130210 |            | Respiratory, Rehabilitative and Restorative Service                          | Other                                                                            | Rehabilitation Coordinator                                            | 10/20/1998       |
| 415  | V130211 |            | Respiratory, Rehabilitative and Restorative Service                          | Other                                                                            | Rehabilitation Counselor                                              | 10/20/1998       |
| 416  | V150000 |            | Technologists, Technicians and Other Technical Service                       |                                                                                  |                                                                       | 10/20/1998       |
| 417  | V150100 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               |                                                                       | 10/20/1998       |
| 418  | V150101 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Clinical Chemist                                                      | 10/20/1998       |
| 419  | V150102 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Clinical Chemistry Technologist                                       | 10/20/1998       |
| 420  | V150103 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Cytotechnologist                                                      | 10/20/1998       |
| 433  | V150116 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Technologist in Blood Banking                                         | 10/20/1998       |
| 434  | V150117 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Technologist in Chemistry                                             | 10/20/1998       |
| 435  | V150118 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Technologist in Hematology                                            | 10/20/1998       |
| 437  | V150120 |            | Technologists, Technicians and Other Technical Service                       | Clinical Pathology                                                               | Technologist in Microbiology                                          | 10/20/1998       |
| 438  | V150200 |            | Technologists, Technicians and Other Technical Service                       | Clinical Services                                                                |                                                                       | 10/20/1998       |
| 441  | V150203 | 246VC2901N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiovascular: Invasive Technology                                   | 7/12/2017        |
| 442  | V150204 | 246VC0100N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiology                                                            | 7/12/2017        |
| 443  | V150205 | 246VC2400N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiopulmonary-Cardiovascular                                        | 7/12/2017        |
| 444  | V150206 |            | Technologists, Technicians and Other Technical Service                       | Clinical Services                                                                | Cardiothoracic Technician                                             | 10/20/1998       |
| 445  | V150207 | 246VP3600N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Perfusionist                                                          | 7/12/2017        |
| 446  | V150208 | 246WE0400N | Technologists, Technicians and Other Technical Service                       | Technician, Cardiology                                                           | ECG                                                                   | 7/12/2017        |
| 451  | V150213 |            | Technologists, Technicians and Other Technical Service                       | Clinical Services                                                                | IV Therapist                                                          | 10/20/1998       |
| 453  | V150215 |            | Technologists, Technicians and Other Technical Service                       | Clinical Services                                                                | Pulmonary Clinician                                                   | 10/20/1998       |
| 455  | V150217 |            | Technologists, Technicians and Other Technical Service                       | Clinical Services                                                                | Renal Dialysis Technologist                                           | 10/20/1998       |
| 456  | V150218 | 246ZS0400X | Technologists, Technicians and Other Technical Service Providers             | Specialist/Technologist, Other                                                   | Surgical                                                              | 7/12/2017        |
| 457  | V150219 |            | Technologists, Technicians and Other Technical Service                       | Clinical Services                                                                | Ultrasound Technologist                                               | 10/20/1998       |
| 458  | V150300 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              |                                                                       | 10/20/1998       |
| 460  | V150302 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Computed Tomography Technologist                                      | 10/20/1998       |
| 462  | V150304 | 246VS1301N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Sonography, Diagnostic Cardiac                                        | 7/12/2017        |
| 463  | V150305 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Diagnostic Imaging Operation Technologist                             | 10/20/1998       |
| 465  | V150307 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Magnetic Resonance Technologist                                       | 10/20/1998       |
| 467  | V150309 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Nuclear Medicine Technician                                           | 10/20/1998       |
| 469  | V150311 | 2471R0003N | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Radiation Physicist                                                   | 7/12/2017        |
| 471  | V150313 | 2471R1500N | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Radiographer                                                          | 7/12/2017        |
| 472  | V150314 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Radiologic Technician - Limited                                       | 10/20/1998       |
| 473  | V150315 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Radiologic Technologist                                               | 10/20/1998       |
| 474  | V150316 | 2471D1300N | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Dosimetrist, Medical                                                  | 7/12/2017        |
| 475  | V150317 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Sciences                                                              | Vascular Technologist                                                 | 10/20/1998       |
| 476  | V150400 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         |                                                                       | 10/20/1998       |
| 477  | V150401 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Animal Care Technician                                                | 10/20/1998       |
| 478  | V150402 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Animal Room Attendant                                                 | 10/20/1998       |
| 481  | V150405 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Graphics Designer                                                     | 10/20/1998       |
| 484  | V150408 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Medical Media Manager                                                 | 10/20/1998       |
| 485  | V150409 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Research Data Abstracter/Coder                                        | 10/20/1998       |
| 486  | V150410 |            | Technologists, Technicians & Other Technical Services                        | Research                                                                         | Research Study Specialist                                             | 10/20/1998       |
| 487  | V150411 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Research Technician                                                   | 10/20/1998       |
| 488  | V150412 |            | Technologists, Technicians and Other Technical Service                       | Research                                                                         | Research Technologist                                                 | 10/20/1998       |
| 489  | V150413 |            | Technologists, Technicians & Other Technical Services                        | Research                                                                         | Veterinarian                                                          | 10/20/1998       |
| 491  | V080000 |            | Other Service                                                                |                                                                                  |                                                                       | 10/20/1998       |
| 494  | V080212 |            | Other Service                                                                | Driver                                                                           | Taxi Driver                                                           | 10/20/1998       |
| 495  | V080203 |            | Other Service                                                                | Driver                                                                           | Volunteer Driver                                                      | 10/20/1998       |
| 496  | V080201 |            | Other Service                                                                | Driver                                                                           | Paid Driver                                                           | 10/20/1998       |
| 497  | V080300 |            | Other Service                                                                | Electrologist                                                                    |                                                                       | 10/20/1998       |
| 498  | V080400 |            | Other Service                                                                | Home Health Aide                                                                 |                                                                       | 10/20/1998       |
| 500  | V080600 |            | Other Service                                                                | Homemaker                                                                        |                                                                       | 10/20/1998       |
| 502  | V080800 |            | Other Service                                                                | Medical Record Administrator                                                     |                                                                       | 10/20/1998       |
| 503  | V080900 |            | Other Service                                                                | Medical Record Technician                                                        |                                                                       | 10/20/1998       |
| 506  | V081200 |            | Other Service                                                                | Nursing Home Administrator                                                       |                                                                       | 10/20/1998       |
| 507  | V081400 |            | Other Service                                                                | Perfusionist                                                                     |                                                                       | 10/20/1998       |
| 508  | V081500 |            | Other Service                                                                | Personal Care Attendant                                                          |                                                                       | 10/20/1998       |
| 509  | V081600 |            | Other Service                                                                | Phlebotomist (non-nurse)                                                         |                                                                       | 10/20/1998       |
| 510  | V081300 |            | Other Service                                                                | Other (as specified)                                                             |                                                                       | 10/20/1998       |
| 511  | V130500 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Care Practitioner                                                    |                                                                       | 10/20/1998       |
| 515  | V010412 | 103TE1000X | Behavioral Health & Social Service Providers                                 | Psychologist                                                                     | Educational                                                           | 1/26/2009        |
| 517  | V010414 | 103TM1700X | Behavioral Health & Social Service Providers                                 | Psychologist                                                                     | Men & Masculinity                                                     | 1/26/2009        |
| 519  | V010416 | 103TP2700X | Behavioral Health & Social Service Providers                                 | Psychologist                                                                     | Psychotherapy                                                         | 1/26/2009        |
| 522  | V010419 | 103TW0100X | Behavioral Health & Social Service Providers                                 | Psychologist                                                                     | Women                                                                 | 1/26/2009        |
| 537  | V100316 | 364SN0004N | Physician Assistants & Advanced Practice Nursing                             | Clinical Nurse Specialist                                                        | Neonatal, High-Risk                                                   | 7/12/2017        |
| 549  | V100332 | 364SR1300N | Physician Assistants & Advanced Practice Nursing                             | Clinical Nurse Specialist                                                        | Rural Health                                                          | 7/12/2017        |
| 561  | V100612 | 363LP0223N | Physician Assistants & Advanced Practice Nursing                             | Nurse Practitioner                                                               | Pediatrics: Acute Care                                                | 7/12/2017        |
| 569  | V118301 | 203BA0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine                                                   | 7/12/2017        |
| 570  | V118302 | 203BA0001N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine: Family Practice                                  | 7/12/2017        |
| 571  | V118303 | 203BA0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Aerospace Medicine                                                    | 7/12/2017        |
| 572  | V118304 | 203BA0202N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Allergy & Immunology: Internal Medicine                               | 7/12/2017        |
| 573  | V118305 | 203BA0501N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Only, Under 16                                             | 7/12/2017        |
| 574  | V118306 | 203BA0502N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Only, Under 21                                             | 7/12/2017        |
| 575  | V118307 | 203BA0503N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Age Specific, Greater than 1 Year Old                                 | 7/12/2017        |
| 576  | V118308 | 203BA0504N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Age Specific, Newborns Only                                           | 7/12/2017        |
| 577  | V118309 | 203BB0000N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Blood Banking                                                         | 7/12/2017        |
| 578  | V118310 | 203BC0001Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiac Electrophysiology, Clinical                                   | 7/12/2017        |
| 579  | V118311 | 203BC0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine                                                | 7/12/2017        |
| 580  | V118312 | 203BD0300N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Diabetes                                                              | 7/12/2017        |
| 581  | V118313 | 203BE0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Endocrinology                                                         | 7/12/2017        |
| 582  | V118314 | 203BG0300N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine                                                    | 7/12/2017        |
| 583  | V118315 | 203BG0400N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Gynecology                                                            | 7/12/2017        |
| 584  | V118316 | 203BH0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology                                                            | 7/12/2017        |
| 585  | V118317 | 203BI0001N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory                                     | 7/12/2017        |
| 586  | V118318 | 203BI0003Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Dermatological                                            | 7/12/2017        |
| 587  | V118319 | 203BI0004Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology: Laboratory, Diagnostic                                    | 7/12/2017        |
| 588  | V118320 | 203BI0400N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Infertility                                                           | 7/12/2017        |
| 589  | V118321 | 203BN0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neonatology                                                           | 7/12/2017        |
| 590  | V118322 | 203BP0903Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Public Health: Preventive Medicine                                    | 7/12/2017        |
| 591  | V118323 | 203BP1200N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pharmacotherapy                                                       | 7/12/2017        |
| 592  | V118324 | 203BP1300N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychopharmacy                                                        | 7/12/2017        |
| 593  | V118325 | 203BP2900N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pain Medicine                                                         | 7/12/2017        |
| 594  | V118326 | 203BR0201Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Angiography & Interventional                               | 7/12/2017        |
| 595  | V118327 | 203BR0203N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Therapeutic                                                | 7/12/2017        |
| 596  | V118328 | 203BR0300N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radium Therapy                                                        | 7/12/2017        |
| 597  | V118329 | 203BR0600N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Rhinology                                                             | 7/12/2017        |
| 598  | V118330 | 203BR0700Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Roentgenology                                                         | 7/12/2017        |
| 599  | V118331 | 203BR0701Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Roentgenology, Diagnostic                                             | 7/12/2017        |
| 600  | V118332 | 203BS0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine                                                       | 7/12/2017        |
| 601  | V118333 | 203BS0104N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Abdominal                                                    | 7/12/2017        |
| 602  | V118334 | 203BS0123Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Facial Plastic                                               | 7/12/2017        |
| 603  | V118335 | 203BT0000Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Toxicology, Medical                                                   | 7/12/2017        |
| 604  | V118336 | 203BT0100N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Thermography                                                          | 7/12/2017        |
| 605  | V118337 | 203BX0100Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Occupational Medicine                                                 | 7/12/2017        |
| 606  | V118338 | 203BX0200Y | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Oncology                                                              | 7/12/2017        |
| 607  | V118339 | 203BX0601N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otorhinolaryngology & Head-Neck                                       | 7/12/2017        |
| 608  | V118340 | 203BX0800N | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Orthopedic                                                            | 7/12/2017        |
| 611  | V130310 | 2251C0400N | Respiratory, Rehabilitative and Restorative Service                          | Physical Therapist                                                               | Case Management                                                       | 7/12/2017        |
| 614  | V130511 | 2259P1700N | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Therapist                                                            | Perinatal                                                             | 7/12/2017        |
| 617  | V130104 | 225XC0400N | Respiratory, Rehabilitative and Restorative Service                          | Occupational Therapist                                                           | Case Management                                                       | 7/12/2017        |
| 629  | V150701 | 246VC2902N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiovascular: Noninvasive Technology                                | 7/12/2017        |
| 630  | V150702 | 246VC2903N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiovascular: Vascular Technology                                   | 7/12/2017        |
| 631  | V150703 | 246VV0100N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Vascular                                                              | 7/12/2017        |
| 632  | V150801 | 246WC3000N | Technologists, Technicians and Other Technical Service                       | Technician, Cardiology                                                           | Cardiographic                                                         | 7/12/2017        |
| 636  | V151002 | 246ZF0200N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Other                                                   | Forensic                                                              | 7/12/2017        |
| 638  | V151004 | 246ZV0500N | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Other                                                   | Virology                                                              | 7/12/2017        |
| 641  | V150320 | 2471M1201N | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Magnetic Resonance Imaging (MRI): Radiation Therapy                   | 7/12/2017        |
| 644  | V150323 | 2471Q0002N | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Quality Management: Radiographer                                      | 7/12/2017        |
| 645  | V160101 | 353BL0002N | Physicians (Other Roles)                                                     | Physician/Osteopath                                                              | Laboratory Service Provider                                           | 7/12/2017        |
| 646  | V160102 | 353BS0900N | Physicians (Other Roles)                                                     | Physician/Osteopath                                                              | Supplier                                                              | 7/12/2017        |
| 659  | V100400 | 366B00000N | Physician Assistants & Advanced Practice Nursing                             | Midwife, Certified                                                               |                                                                       | 12/20/2002       |
| 680  | V082200 | 173W00000X | Other Service                                                                | Registered Nurse                                                                 |                                                                       | 7/12/2017        |
| 684  | V090201 | 184700000X | Pharmacy Service                                                             | Technician                                                                       |                                                                       | 7/12/2017        |
| 685  | V110403 | 203BA0004X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Anesthesiology: Pediatric Anesthesiology                              | 7/12/2017        |
| 686  | V110703 | 203BD0002X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatology: Pediatric Dermatology                                    | 7/12/2017        |
| 687  | V110804 | 203BE0005X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Emergency Medicine: Undersea and Hyperbaric Medicine                  | 7/12/2017        |
| 688  | V111517 | 203BI0008X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Hepatology                                         | 7/12/2017        |
| 689  | V111519 | 203BI0009X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Pediatrics                                         | 7/12/2017        |
| 690  | V111521 | 203BI0010X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Pulmonary Critical Care Medicine                   | 7/12/2017        |
| 691  | V111518 | 203BI0011X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Interventional Cardiology                          | 7/12/2017        |
| 692  | V111610 | 203BL0001X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Legal Medicine                                                        | 7/12/2017        |
| 693  | V111906 | 203BM0001X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Medical Genetics: Molecular Genetic Pathology                         | 7/12/2017        |
| 694  | V112101 | 203BN0006X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurological Surgery: Pediatric Neurological Surgery                  | 7/12/2017        |
| 695  | V110404 | 203BP0000X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pain Management                                                       | 7/12/2017        |
| 696  | V117402 | 203BP0002X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Plastic Surgery: Craniofacial Surgery                                 | 7/12/2017        |
| 697  | V113715 | 203BP0003X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology: Selective Pathology                                        | 7/12/2017        |
| 698  | V114504 | 203BP0004X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine and Rehabilitation: Spinal Cord Injury              | 7/12/2017        |
| 699  | V114809 | 203BP0005X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry & Neurology: Neurodevelopmental Disabilities               | 7/12/2017        |
| 700  | V114002 | 203BP0006X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatrics: Developmental - Behavioral Pediatrics                     | 7/12/2017        |
| 701  | V113716 | 203BP0007X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology: Molecular Genetic Pathology                                | 7/12/2017        |
| 702  | V114001 | 203BP0008X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatrics: Neurodevelopmental Disabilities                           | 7/12/2017        |
| 703  | V114501 | 203BP0009X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation: Pain Management                   | 7/12/2017        |
| 704  | V114502 | 203BP0010X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation: Pediatric Rehabilitation Medicine | 7/12/2017        |
| 705  | V114608 | 203BP0011X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Preventive Medicine: Undersea and Hyperbaric Medicine                 | 7/12/2017        |
| 706  | V117403 | 203BP0013X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Plastic Surgery: Plastic Surgery Within the Head and Neck             | 7/12/2017        |
| 707  | V114810 | 203BP0014X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry & Neurology: Pain Management                               | 7/12/2017        |
| 708  | V111520 | 203BP3700X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Peripheral Vascular Disease                        | 7/12/2017        |
| 709  | V115308 | 203BR0004X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology: Abdominal Radiology                                        | 7/12/2017        |
| 710  | V115309 | 203BR0005X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology: Musculoskeletal Radiology                                  | 7/12/2017        |
| 711  | V118343 | 203BS0008X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine - OMM                                                 | 7/12/2017        |
| 712  | V114607 | 203BS0009X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Preventive Medicine: Sports Medicine                                  | 7/12/2017        |
| 713  | V114503 | 203BS0010X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation: Sports Medicine                   | 7/12/2017        |
| 714  | V116801 | 203BS0134X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery: Micrographic Surgery                                         | 7/12/2017        |
| 715  | V118201 | 203BU0002X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Urology, Pediatric Urology                                            | 7/12/2017        |
| 716  | V118341 | 203BX0004X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Orthopedic Surgery: Foot and Ankle Orthopedics                        | 7/12/2017        |
| 717  | V118342 | 203BX0005X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Orthopedic Surgery: Sports Medicine                                   | 7/12/2017        |
| 718  | V113001 | 203BX0006X | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Opthalmology: Pediatric Opthalmology                                  | 7/12/2017        |
| 725  | V150704 | 246V00000X | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              |                                                                       | 7/12/2017        |
| 732  | V160100 | 353B00000X | Physicians (Other Roles)                                                     | Physician/Osteopath (Other Roles)                                                |                                                                       | 7/12/2017        |
| 741  | V082300 | 177F00000X | Other Service Providers                                                      | Lodging                                                                          |                                                                       | 7/12/2017        |
| 956  |         | 332100000X | Suppliers                                                                    | Department of Veterans Affairs (VA) Pharmacy                                     |                                                                       | 7/12/2017        |
| 957  |         | 251300000X | Agencies                                                                     | Local Education Agency (LEA)                                                     |                                                                       | 7/12/2017        |
| 958  |         | 251B00000X | Agencies                                                                     | Case Management                                                                  |                                                                       | 7/12/2017        |
| 959  |         | 251S00000X | Agencies                                                                     | Community/Behavioral Health                                                      |                                                                       | 7/12/2017        |
| 960  |         | 251C00000X | Agencies                                                                     | Day Training, Developmentally Disabled Services                                  |                                                                       | 7/12/2017        |
| 961  |         | 252Y00000X | Agencies                                                                     | Early Intervention Provider Agency                                               |                                                                       | 7/12/2017        |
| 963  |         | 251F00000X | Agencies                                                                     | Home Infusion                                                                    |                                                                       | 7/12/2017        |
| 966  |         | 251T00000X | Agencies                                                                     | PACE Provider Organization                                                       |                                                                       | 7/12/2017        |
| 971  |         | 261QM0855X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Adolescent and Children Mental Health                                 | 7/12/2017        |
| 972  |         | 261QA0600X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Adult Day Care                                                        | 7/12/2017        |
| 974  |         | 261QA0005X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Ambulatory Family Planning Facility                                   | 7/12/2017        |
| 978  |         | 261QA3000X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Augmentative Communication                                            | 7/12/2017        |
| 979  |         | 261QB0400X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Birthing                                                              | 7/12/2017        |
| 980  |         | 261QC1500X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Community Health                                                      | 7/12/2017        |
| 981  |         | 261QC1800X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Corporate Health                                                      | 7/12/2017        |
| 982  |         | 261QC0050X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Critical Access Hospital                                              | 7/12/2017        |
| 984  |         | 261QD1600X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Developmental Disabilities                                            | 7/12/2017        |
| 985  |         | 261QE0002X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Emergency Care                                                        | 7/12/2017        |
| 986  |         | 261QE0800X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Endoscopy                                                             | 7/12/2017        |
| 988  |         | 261QF0050X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Family Planning, Non-Surgical                                         | 7/12/2017        |
| 990  |         | 261QG0250X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Genetics                                                              | 7/12/2017        |
| 991  |         | 261QH0100X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Health Service                                                        | 7/12/2017        |
| 992  |         | 261QH0700X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Hearing and Speech                                                    | 7/12/2017        |
| 993  |         | 261QI0500X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Infusion Therapy                                                      | 7/12/2017        |
| 994  |         | 261QL0400X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Lithotripsy                                                           | 7/12/2017        |
| 995  |         | 261QM1200X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Magnetic Resonance Imaging (MRI)                                      | 7/12/2017        |
| 997  |         | 261QM3000X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Medically Fragile Intants and Children Day Care                       | 7/12/2017        |
| 1000 |         | 261QM1000X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Migrant Health                                                        | 7/12/2017        |
| 1001 |         | 261QM1103X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Military Ambulatory Procedure Visits Operational (Transportable)      | 7/12/2017        |
| 1002 |         | 261QM1101X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Military and U.S. Coast Guard Ambulatory Procedure                    | 7/12/2017        |
| 1003 |         | 261QM1102X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Military Outpatient Operational (Transportable) Component             | 7/12/2017        |
| 1004 |         | 261QM1100X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Military/U.S. Coast Guard Outpatient                                  | 7/12/2017        |
| 1006 |         | 261QX0100X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Occupational Medicine                                                 | 7/12/2017        |
| 1007 |         | 261QX0200X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Oncology                                                              | 7/12/2017        |
| 1008 |         | 261QX0203X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Oncology, Radiation                                                   | 7/12/2017        |
| 1010 |         | 261QS0112X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Oral and Maxillofacial Surgery                                        | 7/12/2017        |
| 1011 |         | 261QP3300X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Pain                                                                  | 7/12/2017        |
| 1013 |         | 261QP1100X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Podiatric                                                             | 7/12/2017        |
| 1014 |         | 261QP2300X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Primary Care                                                          | 7/12/2017        |
| 1015 |         | 261QP2400X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Prison Health                                                         | 7/12/2017        |
| 1016 |         | 261QP0904X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Public Health, Federal                                                | 7/12/2017        |
| 1019 |         | 261QR0206X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Radiology, Mammography                                                | 7/12/2017        |
| 1022 |         | 261QR0800X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Recovery Care                                                         | 7/12/2017        |
| 1024 |         | 261QR0404X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Rehabilitation, Cardiac Facilities                                    | 7/12/2017        |
| 1026 |         | 261QR0405X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Rehabilitation, Substance Use Disorder                                | 7/12/2017        |
| 1027 |         | 261QR1100X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Research                                                              | 7/12/2017        |
| 1029 |         | 261QS1200X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Sleep Disorder Diagnostic                                             | 7/12/2017        |
| 1031 |         | 261QU0200X | Ambulatory Health Care Facilities                                            | Clinic/Center                                                                    | Urgent Care                                                           | 7/12/2017        |
| 1032 |         | 273100000X | Hospital Units                                                               | Epilepsy Unit                                                                    |                                                                       | 7/12/2017        |
| 1036 |         | 276400000X | Hospital Units                                                               | Rehabilitation, Substance Use Disorder Unit                                      |                                                                       | 7/12/2017        |
| 1037 |         | 287300000X | Hospitals                                                                    | Christian Science Sanitorium                                                     |                                                                       | 10/1/2009        |
| 1038 |         | 281P00000X | Hospitals                                                                    | Chronic Disease Hospital                                                         |                                                                       | 7/12/2017        |
| 1042 |         | 282NR1301X | Hospitals                                                                    | General Acute Care Hospital                                                      | Rural                                                                 | 7/12/2017        |
| 1046 |         | 2865C1500X | Hospitals                                                                    | Military Hospital                                                                | Community Health                                                      | 4/1/2005         |
| 1048 |         | 2865X1600X | Hospitals                                                                    | Military Hospital                                                                | Military General Acute Care Hospital. Operational (Transportable)     | 7/12/2017        |
| 1055 |         | 292200000X | Laboratories                                                                 | Dental Laboratory                                                                |                                                                       | 7/12/2017        |
| 1058 |         | 302F00000X | Managed Care Organizations                                                   | Exclusive Provider Organization                                                  |                                                                       | 7/12/2017        |
| 1060 |         | 305S00000X | Managed Care Organizations                                                   | Point of Service                                                                 |                                                                       | 7/12/2017        |
| 1061 |         | 305R00000X | Managed Care Organizations                                                   | Preferred Provider Organization                                                  |                                                                       | 7/12/2017        |
| 1062 |         | 311500000X | Nursing & Custodial Care Facilities                                          | Alzheimer Center (Dementia Center)                                               |                                                                       | 7/12/2017        |
| 1063 |         | 310400000X | Nursing & Custodial Care Facilities                                          | Assisted Living Facility                                                         |                                                                       | 7/12/2017        |
| 1067 |         | 311Z00000X | Nursing & Custodial Care Facilities                                          | Custodial Care Facility                                                          |                                                                       | 7/12/2017        |
| 1068 |         | 311ZA0620X | Nursing & Custodial Care Facilities                                          | Custodial Care Facility                                                          | Adult Care Home                                                       | 7/12/2017        |
| 1069 |         | 315D00000X | Nursing & Custodial Care Facilities                                          | Hospice, Inpatient                                                               |                                                                       | 7/12/2017        |
| 1070 |         | 310500000X | Nursing & Custodial Care Facilities                                          | Intermediate Care Facility, Mental Illness                                       |                                                                       | 7/12/2017        |
| 1075 |         | 320800000X | Residential Treatment Facilities                                             | Community Based Residential Treatment Facility, Mental Illness                   |                                                                       | 7/12/2017        |
| 1076 |         | 320900000X | Residential Treatment Facilities                                             | Community Based Residential Treatment, Mental Retardation and/or Developmental D |                                                                       | 7/12/2017        |
| 1078 |         | 322D00000X | Residential Treatment Facilities                                             | Psychiatric Residential Treatment Facility                                       |                                                                       | 7/12/2017        |
| 1079 |         | 320600000X | Residential Treatment Facilities                                             | Residential Treatment Facility, Emotionally Disturbed Children                   |                                                                       | 7/12/2017        |
| 1080 |         | 320700000X | Residential Treatment Facilities                                             | Residential Treatment Facility, Mental Retardation and/or Developmental Disabili |                                                                       | 7/12/2017        |
| 1081 |         | 324500000X | Residential Treatment Facilities                                             | ties                                                                             |                                                                       | 7/12/2017        |
| 1084 |         | 385HR2050X | Respite Care Facility                                                        | Substance Abuse Rehabilitation Facility                                          | Respite Care Camp                                                     | 7/12/2017        |
| 1088 |         | 331L00000X | Suppliers                                                                    | Respite Care                                                                     |                                                                       | 7/12/2017        |
| 1092 |         | 332BN1400X | Suppliers                                                                    | Durable Medical Equipment & Medical Supplies                                     | Nursing Facility Supplies                                             | 7/12/2017        |
| 1094 |         | 332BP3500X | Suppliers                                                                    | Durable Medical Equipment & Medical Supplies                                     | Parenteral & Enteral Nutrition                                        | 7/12/2017        |
| 1095 |         | 333300000X | Suppliers                                                                    | Durable Medical Equipment & Medical Supplies                                     |                                                                       | 7/12/2017        |
| 1096 |         | 332G00000X | Suppliers                                                                    | Durable Medical Equipment & Medical Supplies                                     |                                                                       | 7/12/2017        |
| 1097 |         | 332H00000X | Suppliers                                                                    | Emergency Response System Companies                                              |                                                                       | 7/12/2017        |
| 1098 |         | 332S00000X | Suppliers                                                                    | Eye Bank                                                                         |                                                                       | 7/12/2017        |
| 1099 |         | 332U00000X | Suppliers                                                                    | Eyewear Supplier (Equipment, not the service)                                    |                                                                       | 7/12/2017        |
| 1100 |         | 332800000X | Suppliers                                                                    | Hearing Aid Equipment                                                            |                                                                       | 7/12/2017        |
| 1101 |         | 332000000X | Suppliers                                                                    | Home Delivered Meals                                                             |                                                                       | 7/12/2017        |
| 1102 |         | 332900000X | Suppliers                                                                    | Indian Health Service/Tribal/Urban Indian Health (I/T/U) Pharmacy                |                                                                       | 7/12/2017        |
| 1121 |         | 347B00000X | Transportation Services                                                      | Military/U.S. Coast Guard Pharmacy                                               |                                                                       | 7/12/2017        |
| 1122 |         | 341800000X | Transportation Services                                                      | Non-Pharmacy Dispensing Site                                                     |                                                                       | 7/12/2017        |
| 1123 |         | 3418M1120X | Transportation Services                                                      | Bus                                                                              | Military or U.S. Coast Guard Ambulance, Air Transport                 | 7/12/2017        |
| 1124 |         | 3418M1110X | Transportation Services                                                      | Military/U.S. Coast Guard Transport                                              | Military or U.S. Coast Guard Ambulance, Ground Transport              | 7/12/2017        |
| 1127 |         | 347C00000X | Transportation Services                                                      | Military/U.S. Coast Guard Transport                                              |                                                                       | 7/12/2017        |
| 1128 |         | 343800000X | Transportation Services                                                      | Non-emergency Medical Transport (VAN)                                            |                                                                       | 7/12/2017        |
| 1129 |         | 344600000X | Transportation Services                                                      | Private Vehicle                                                                  |                                                                       | 7/12/2017        |
| 1130 |         | 347D00000X | Transportation Services                                                      | Secured Medical Transport (VAN)                                                  |                                                                       | 7/12/2017        |
| 1131 |         | 347E00000X | Transportation Services                                                      | Taxi                                                                             |                                                                       | 7/12/2017        |
| 1136 |         | 253J00000X | Agencies                                                                     | Train                                                                            |                                                                       | 7/12/2017        |
| 1150 |         | 253Z00000X | Agencies                                                                     | Transportation Broker                                                            |                                                                       | 7/12/2017        |
| 1161 |         | 344800000X | Transportation Services                                                      | Foster Care Agency                                                               |                                                                       | 7/12/2017        |
| 1165 |         | 174200000X | Other Service Providers                                                      | In Home Supportive Care                                                          |                                                                       | 7/12/2017        |
| 1171 | V182605 | 207RH0005X | Allopathic & Osteopathic Physicians                                          | Air Carrier                                                                      | Hypertension Specialist                                               | 7/12/2017        |
| 1173 |         | 335G00000X | Suppliers                                                                    | Meals                                                                            |                                                                       | 7/12/2017        |
| 1179 | V110403 | 207LP3000X | Allopathic & Osteopathic Physicians                                          | Internal Medicine                                                                | Pediatric Anesthesiology                                              | 7/12/2017        |
| 1198 | V182605 | 2081N0008X | Allopathic & Osteopathic Physicians                                          | Medical Foods Supplier                                                           | Neuromuscular Medicine                                                | 7/12/2017        |
| 1200 | V182916 | 2084B0040X | Allopathic & Osteopathic Physicians                                          | Anesthesiology                                                                   | Behavioral Neurology & Neuropsychiatry                                | 7/12/2017        |
| 1217 |         | 261QB0400X | Ambulatory Health Care Facilities                                            | Physical Medicine & Rehabilitation                                               | Birthing                                                              | 7/12/2017        |
| 1302 | V110000 | 207R00000X | Allopathic & Osteopathic Physicians                                          | Clinic/Center                                                                    |                                                                       | 7/12/2017        |
| 1304 | V111500 | 207RG0100X | Allopathic & Osteopathic Physicians                                          | Local Education Agency (LEA)                                                     | Gastroenterology                                                      | 7/12/2017        |
| 1305 | V111507 | 207RG0100X | Allopathic & Osteopathic Physicians                                          | Internal Medicine                                                                | Gastroenterology                                                      | 7/12/2017        |
| 1320 | V183009 | 2085R0001X | Allopathic & Osteopathic Physicians                                          | Internal Medicine                                                                | Radiation Oncology                                                    | 7/12/2017        |
| 1321 | V115500 | 2085R0202X | Allopathic & Osteopathic Physicians                                          | Pediatrics                                                                       | Diagnostic Radiology                                                  | 7/12/2017        |
| 1322 | V183001 | 2085R0202X | Allopathic & Osteopathic Physicians                                          | Radiology                                                                        | Diagnostic Radiology                                                  | 7/12/2017        |
| 1323 | V183004 | 2085R0202X | Allopathic & Osteopathic Physicians                                          | Radiology                                                                        | Diagnostic Radiology                                                  | 7/12/2017        |
| 1327 | V010300 |            | Behavioral Health and Social Service                                         | Radiology                                                                        |                                                                       | 7/12/2017        |
| 1328 | V010301 |            | Behavioral Health and Social Service                                         | Radiology                                                                        | Affiliate                                                             | 7/12/2017        |
| 1329 | V010302 |            | Behavioral Health and Social Service                                         | Psychoanalyst                                                                    | Associate                                                             | 7/12/2017        |
| 1332 | V040100 |            | Dietary and Nutritional Service                                              | Psychoanalyst                                                                    | Dietary Management                                                    | 7/12/2017        |
| 1364 | V110100 |            | Physicians (M.D. and D.O.)                                                   |                                                                                  | Addiction Medicine                                                    | 7/12/2017        |
| 1365 | V110200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Allergy                                                               | 7/12/2017        |
| 1366 | V110300 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Allergy & Immunology                                                  | 7/12/2017        |
| 1367 | V110400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Anesthesiology                                                        | 7/12/2017        |
| 1368 | V110401 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine: Anesthesiology                                | 7/12/2017        |
| 1369 | V110403 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Anesthesiology: Pediatric Anesthesiology                              | 7/12/2017        |
| 1370 | V110500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Body Imaging                                                          | 7/12/2017        |
| 1371 | V110600 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiology                                                            | 7/12/2017        |
| 1372 | V110700 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatology                                                           | 7/12/2017        |
| 1373 | V110702 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatopathology: Dermatology                                         | 7/12/2017        |
| 1374 | V110703 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatology: Pediatric Dermatology                                    | 7/12/2017        |
| 1375 | V111501 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine: Internal Medicine                                | 7/12/2017        |
| 1376 | V111502 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiac Electrophysiology                                             | 7/12/2017        |
| 1377 | V111503 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiovascular Disease                                                | 7/12/2017        |
| 1378 | V111505 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine: Internal Medicine                             | 7/12/2017        |
| 1379 | V111903 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cytogenetics, Clinical                                                | 7/12/2017        |
| 1380 | V112901 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine: OB/GYN                                        | 7/12/2017        |
| 1381 | V113704 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Blood Banking & Transfusion Medicine                                  | 7/12/2017        |
| 1382 | V113707 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cytopathology                                                         | 7/12/2017        |
| 1383 | V113708 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatopathology                                                      | 7/12/2017        |
| 1384 | V114201 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine: Pediatrics                                       | 7/12/2017        |
| 1385 | V114601 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Aerospace Medicine: Preventive Medicine                               | 7/12/2017        |
| 1386 | V116000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Dermatology Micrographic Surgery                                      | 7/12/2017        |
| 1387 | V118301 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine                                                   | 7/12/2017        |
| 1388 | V118302 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Medicine: Family Practice                                  | 7/12/2017        |
| 1389 | V118303 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Aerospace Medicine                                                    | 7/12/2017        |
| 1390 | V118304 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Allergy & Immunology: Internal Medicine                               | 7/12/2017        |
| 1391 | V118305 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Only, Under 16                                             | 7/12/2017        |
| 1392 | V118306 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Adolescent Only, Under 21                                             | 7/12/2017        |
| 1393 | V118307 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Age Specific, Greater than 1 Year Old                                 | 7/12/2017        |
| 1394 | V118308 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Age Specific, Newborns Only                                           | 7/12/2017        |
| 1395 | V118309 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Blood Banking                                                         | 7/12/2017        |
| 1396 | V118310 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Cardiac Electrophysiology, Clinical                                   | 7/12/2017        |
| 1397 | V118311 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Critical Care Medicine                                                | 7/12/2017        |
| 1398 | V118312 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Diabetes                                                              | 7/12/2017        |
| 1399 | V110301 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory: Allergy & Immunology               | 7/12/2017        |
| 1400 | V110402 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pain Management - Anesthesiology                                      | 7/12/2017        |
| 1401 | V110404 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pain Management                                                       | 7/12/2017        |
| 1402 | V110701 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory Dermatological                      | 7/12/2017        |
| 1403 | V110800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Emergency Medicine                                                    | 7/12/2017        |
| 1404 | V110804 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Emergency Medicine: Undersea and Hyperbaric Medicine                  | 7/12/2017        |
| 1405 | V110900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Family Practice                                                       | 7/12/2017        |
| 1406 | V110901 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine: Family Practice                                   | 7/12/2017        |
| 1407 | V111000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | General Practice                                                      | 7/12/2017        |
| 1408 | V111100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine: General Practice                                  | 7/12/2017        |
| 1409 | V111200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology & Oncology                                                 | 7/12/2017        |
| 1410 | V111500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine                                                     | 7/12/2017        |
| 1411 | V111504 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory: Internal Medicine                  | 7/12/2017        |
| 1412 | V111506 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Endocrinology, Diabetes & Metabolism                                  | 7/12/2017        |
| 1413 | V111507 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Gastroenterology                                                      | 7/12/2017        |
| 1414 | V111508 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine: Internal Medicine                                 | 7/12/2017        |
| 1415 | V111509 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology: Internal Medicine                                         | 7/12/2017        |
| 1416 | V111510 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Infectious Diseases                                                   | 7/12/2017        |
| 1417 | V111511 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Oncology, Medical                                                     | 7/12/2017        |
| 1418 | V111512 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nephrology                                                            | 7/12/2017        |
| 1419 | V111517 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Hepatology                                         | 7/12/2017        |
| 1420 | V111518 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Interventional Cardiology                          | 7/12/2017        |
| 1421 | V111519 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Pediatrics                                         | 7/12/2017        |
| 1422 | V111520 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Peripheral Vascular Disease                        | 7/12/2017        |
| 1423 | V111521 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Internal Medicine: Pulmonary Critical Care Medicine                   | 7/12/2017        |
| 1424 | V111600 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Laboratory Medicine                                                   | 7/12/2017        |
| 1425 | V111610 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Legal Medicine                                                        | 7/12/2017        |
| 1426 | V111800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Medical Diseases of the Chest                                         | 7/12/2017        |
| 1427 | V111900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Medical                                                     | 7/12/2017        |
| 1428 | V111901 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical Biochemical                                        | 7/12/2017        |
| 1429 | V111902 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical Biochemical/ Molecular                             | 7/12/2017        |
| 1430 | V111904 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical (M.D.)                                             | 7/12/2017        |
| 1431 | V111905 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Genetics, Clinical Molecular                                          | 7/12/2017        |
| 1432 | V111906 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Medical Genetics: Molecular Genetic Pathology                         | 7/12/2017        |
| 1433 | V112000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neopathology                                                          | 7/12/2017        |
| 1434 | V112100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurology                                                             | 7/12/2017        |
| 1435 | V112101 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurological Surgery: Pediatric Neurological Surgery                  | 7/12/2017        |
| 1436 | V112200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurology, Child                                                      | 7/12/2017        |
| 1437 | V112300 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neuroradiology                                                        | 7/12/2017        |
| 1438 | V112400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Cardiology                                                    | 7/12/2017        |
| 1439 | V112500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Imaging & Therapy                                             | 7/12/2017        |
| 1440 | V112600 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Medicine                                                      | 7/12/2017        |
| 1441 | V112601 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Medicine, In Vivo & In Vitro                                  | 7/12/2017        |
| 1442 | V112800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Obstetrics                                                            | 7/12/2017        |
| 1443 | V112900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Obstetrics & Gynecology                                               | 7/12/2017        |
| 1444 | V112902 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Oncology, Gynecologic                                                 | 7/12/2017        |
| 1445 | V112903 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Maternal & Fetal Medicine                                             | 7/12/2017        |
| 1446 | V112904 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Endocrinology, Reproductive                                           | 7/12/2017        |
| 1447 | V113000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Ophthalmology                                                         | 7/12/2017        |
| 1448 | V113001 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Opthalmology: Pediatric Opthalmology                                  | 7/12/2017        |
| 1449 | V113200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Osteopathic Manipulative Medicine, Special Proficiency                | 7/12/2017        |
| 1450 | V113300 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otolaryngology                                                        | 7/12/2017        |
| 1451 | V113301 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otology & Neurotology                                                 | 7/12/2017        |
| 1452 | V113302 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Otolaryngology                                              | 7/12/2017        |
| 1453 | V113400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otology                                                               | 7/12/2017        |
| 1454 | V113500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otorhinolaryngology                                                   | 7/12/2017        |
| 1455 | V113700 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology                                                             | 7/12/2017        |
| 1456 | V113701 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Anatomic & Clinical                                        | 7/12/2017        |
| 1457 | V113702 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Anatomic                                                   | 7/12/2017        |
| 1458 | V113703 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Anatomic & Laboratory Medicine                             | 7/12/2017        |
| 1459 | V113705 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Chemical                                                   | 7/12/2017        |
| 1460 | V113706 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Clinical                                                   | 7/12/2017        |
| 1461 | V113709 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Forensic Pathology                                                    | 7/12/2017        |
| 1462 | V113710 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology: Pathology                                                 | 7/12/2017        |
| 1463 | V113711 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunopathology                                                       | 7/12/2017        |
| 1464 | V113712 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Medical Microbiology                                                  | 7/12/2017        |
| 1465 | V113713 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neuropathology                                                        | 7/12/2017        |
| 1466 | V113714 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Pathology                                                   | 7/12/2017        |
| 1467 | V113715 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology: Selective Pathology                                        | 7/12/2017        |
| 1468 | V113716 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology: Molecular Genetic Pathology                                | 7/12/2017        |
| 1469 | V113800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Allergy & Immunology                                        | 7/12/2017        |
| 1470 | V113900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Intensive Care                                              | 7/12/2017        |
| 1471 | V114000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Neurology                                                   | 7/12/2017        |
| 1472 | V114001 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatrics: Neurodevelopmental Disabilities                           | 7/12/2017        |
| 1473 | V114002 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatrics: Developmental - Behavioral Pediatrics                     | 7/12/2017        |
| 1474 | V114200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatrics                                                            | 7/12/2017        |
| 1475 | V114202 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory: Pediatric                          | 7/12/2017        |
| 1476 | V114203 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Medical Toxocology                                          | 7/12/2017        |
| 1477 | V114204 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neonatal-Perinatal Medicine                                           | 7/12/2017        |
| 1478 | V114205 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Cardiology                                                  | 7/12/2017        |
| 1479 | V114206 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Critical Care Medicine                                      | 7/12/2017        |
| 1480 | V114207 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Emergency Medicine                                          | 7/12/2017        |
| 1481 | V114208 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Endocrinology                                               | 7/12/2017        |
| 1482 | V114209 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Gastroenterology                                            | 7/12/2017        |
| 1483 | V114210 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Hematology Oncology                                         | 7/12/2017        |
| 1484 | V114211 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Infectious Diseases                                         | 7/12/2017        |
| 1485 | V114212 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Nephrology                                                  | 7/12/2017        |
| 1486 | V114213 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Pulmonology                                                 | 7/12/2017        |
| 1487 | V114215 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Rheumatology                                                | 7/12/2017        |
| 1488 | V114300 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pediatric Radiology                                                   | 7/12/2017        |
| 1489 | V114603 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Occupational Medicine: Preventive Medicine                            | 7/12/2017        |
| 1490 | V114604 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Occupational-Environmental Medicine: Preventive Medicine              | 7/12/2017        |
| 1491 | V114803 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neurophysiology, Clinical                                             | 7/12/2017        |
| 1492 | V114804 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Forensic Psychiatry                                                   | 7/12/2017        |
| 1493 | V115200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pathology, Radioisotopic                                              | 7/12/2017        |
| 1494 | V115302 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Nuclear Radiology                                                     | 7/12/2017        |
| 1495 | V118313 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Endocrinology                                                         | 7/12/2017        |
| 1496 | V118314 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Geriatric Medicine                                                    | 7/12/2017        |
| 1497 | V118315 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Gynecology                                                            | 7/12/2017        |
| 1498 | V118316 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Hematology                                                            | 7/12/2017        |
| 1499 | V118317 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Clinical & Laboratory                                     | 7/12/2017        |
| 1500 | V118318 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology, Dermatological                                            | 7/12/2017        |
| 1501 | V118319 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Immunology: Laboratory, Diagnostic                                    | 7/12/2017        |
| 1502 | V118320 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Infertility                                                           | 7/12/2017        |
| 1503 | V118321 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Neonatology                                                           | 7/12/2017        |
| 1504 | V118325 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pain Medicine                                                         | 7/12/2017        |
| 1505 | V118337 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Occupational Medicine                                                 | 7/12/2017        |
| 1506 | V118338 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Oncology                                                              | 7/12/2017        |
| 1507 | V118339 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Otorhinolaryngology & Head-Neck                                       | 7/12/2017        |
| 1508 | V118340 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Orthopedic                                                            | 7/12/2017        |
| 1509 | V118341 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Orthopedic Surgery: Foot and Ankle Orthopedics                        | 7/12/2017        |
| 1510 | V118342 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Orthopedic Surgery: Sports Medicine                                   | 7/12/2017        |
| 1511 | V110801 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Toxicology, Medical: Emergency Medicine                               | 7/12/2017        |
| 1512 | V110803 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Emergency Medicine                                   | 7/12/2017        |
| 1513 | V110902 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Family Practice                                      | 7/12/2017        |
| 1514 | V111513 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pulmonary Diseases                                                    | 7/12/2017        |
| 1515 | V111514 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pulmonary Medicine                                                    | 7/12/2017        |
| 1516 | V111515 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Rheumatology                                                          | 7/12/2017        |
| 1517 | V111516 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Internal Medicine                                    | 7/12/2017        |
| 1518 | V113600 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Otorhinolaryngology & Facial Plastic Surgery                 | 7/12/2017        |
| 1519 | V114100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Pediatric                                                 | 7/12/2017        |
| 1520 | V114216 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine: Pediatrics                                           | 7/12/2017        |
| 1521 | V114400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pharmacology, Clinical                                                | 7/12/2017        |
| 1522 | V114500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation                                    | 7/12/2017        |
| 1523 | V114501 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation: Pain Management                   | 7/12/2017        |
| 1524 | V114502 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation: Pediatric Rehabilitation Medicine | 7/12/2017        |
| 1525 | V114503 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine & Rehabilitation: Sports Medicine                   | 7/12/2017        |
| 1526 | V114504 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Physical Medicine and Rehabilitation: Spinal Cord Injury              | 7/12/2017        |
| 1527 | V114600 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Preventive Medicine, General                                          | 7/12/2017        |
| 1528 | V114602 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Toxicology, Medical: Preventive Medicine                              | 7/12/2017        |
| 1529 | V114605 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Public Health & General Preventive Medicine                           | 7/12/2017        |
| 1530 | V114606 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Underseas Medicine: Preventive Medicine                               | 7/12/2017        |
| 1531 | V114607 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Preventive Medicine: Sports Medicine                                  | 7/12/2017        |
| 1532 | V114608 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Preventive Medicine: Undersea and Hyperbaric Medicine                 | 7/12/2017        |
| 1533 | V114700 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Proctology                                                            | 7/12/2017        |
| 1534 | V114800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry & Neurology                                                | 7/12/2017        |
| 1535 | V114801 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Addiction                                                 | 7/12/2017        |
| 1536 | V114802 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Child & Adolescent                                        | 7/12/2017        |
| 1537 | V114805 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Geriatric                                                 | 7/12/2017        |
| 1538 | V114808 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry                                                            | 7/12/2017        |
| 1539 | V114809 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry & Neurology: Neurodevelopmental Disabilities               | 7/12/2017        |
| 1540 | V114810 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry & Neurology: Pain Management                               | 7/12/2017        |
| 1541 | V114900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychiatry, Child                                                     | 7/12/2017        |
| 1542 | V115100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiation Therapy                                                     | 7/12/2017        |
| 1543 | V115300 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology                                                             | 7/12/2017        |
| 1544 | V115301 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Diagnostic                                                 | 7/12/2017        |
| 1545 | V115304 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiation Oncology                                                    | 7/12/2017        |
| 1546 | V115305 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiological Physics                                                  | 7/12/2017        |
| 1547 | V115307 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Vascular & Interventional                                  | 7/12/2017        |
| 1548 | V115308 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology: Abdominal Radiology                                        | 7/12/2017        |
| 1549 | V115309 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology: Musculoskeletal Radiology                                  | 7/12/2017        |
| 1550 | V115400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Rehabilitation Medicine                                               | 7/12/2017        |
| 1551 | V115701 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, General Vascular                                             | 7/12/2017        |
| 1552 | V115703 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Pediatric                                                    | 7/12/2017        |
| 1553 | V115704 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Hand                                                         | 7/12/2017        |
| 1554 | V115705 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgical Critical Care: Surgery                                       | 7/12/2017        |
| 1555 | V115800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Cardiovascular                                               | 7/12/2017        |
| 1556 | V115900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Colon & Rectal Surgery                                       | 7/12/2017        |
| 1557 | V116100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, General                                                      | 7/12/2017        |
| 1558 | V116200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Head & Neck                                                  | 7/12/2017        |
| 1559 | V116400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Neurological                                                 | 7/12/2017        |
| 1560 | V116500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Obstetric & Gynecologic                                      | 7/12/2017        |
| 1561 | V116600 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic                                                   | 7/12/2017        |
| 1562 | V116700 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Adult Reconstructive                             | 7/12/2017        |
| 1563 | V116800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Hand: Orthopedic Surgery                                     | 7/12/2017        |
| 1564 | V116801 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery: Micrographic Surgery                                         | 7/12/2017        |
| 1565 | V116900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Musculoskeletal Oncology                         | 7/12/2017        |
| 1566 | V117000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Pediatric                                        | 7/12/2017        |
| 1567 | V117100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Spine                                            | 7/12/2017        |
| 1568 | V117300 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Orthopedic, Trauma                                           | 7/12/2017        |
| 1569 | V117400 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Plastic                                                      | 7/12/2017        |
| 1570 | V117401 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Hand: Plastic Surgery                                        | 7/12/2017        |
| 1571 | V117402 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Plastic Surgery: Craniofacial Surgery                                 | 7/12/2017        |
| 1572 | V117403 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Plastic Surgery: Plastic Surgery Within the Head and Neck             | 7/12/2017        |
| 1573 | V117500 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Plastic & Reconstructive                                     | 7/12/2017        |
| 1574 | V117700 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Thoracic                                                     | 7/12/2017        |
| 1575 | V117800 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Thoracic Cardiovascular                                      | 7/12/2017        |
| 1576 | V117900 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Traumatic                                                    | 7/12/2017        |
| 1577 | V118000 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Urological                                                   | 7/12/2017        |
| 1578 | V118100 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Ultrasound, Diagnostic                                                | 7/12/2017        |
| 1579 | V118200 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Urology                                                               | 7/12/2017        |
| 1580 | V118201 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Urology, Pediatric Urology                                            | 7/12/2017        |
| 1581 | V118322 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Public Health: Preventive Medicine                                    | 7/12/2017        |
| 1582 | V118323 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Pharmacotherapy                                                       | 7/12/2017        |
| 1583 | V118324 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Psychopharmacy                                                        | 7/12/2017        |
| 1584 | V118326 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Angiography & Interventional                               | 7/12/2017        |
| 1585 | V118327 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radiology, Therapeutic                                                | 7/12/2017        |
| 1586 | V118328 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Radium Therapy                                                        | 7/12/2017        |
| 1587 | V118329 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Rhinology                                                             | 7/12/2017        |
| 1588 | V118330 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Roentgenology                                                         | 7/12/2017        |
| 1589 | V118331 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Roentgenology, Diagnostic                                             | 7/12/2017        |
| 1590 | V118332 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine                                                       | 7/12/2017        |
| 1591 | V118333 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Abdominal                                                    | 7/12/2017        |
| 1592 | V118334 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Surgery, Facial Plastic                                               | 7/12/2017        |
| 1593 | V118335 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Toxicology, Medical                                                   | 7/12/2017        |
| 1594 | V118336 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Thermography                                                          | 7/12/2017        |
| 1595 | V118343 |            | Physicians (M.D. and D.O.)                                                   | Physician/Osteopath                                                              | Sports Medicine - OMM                                                 | 7/12/2017        |
| 1596 | V160100 |            | Physicians (Other Roles)                                                     | Physician/Osteopath                                                              |                                                                       | 7/12/2017        |
| 1597 | V160101 |            | Physicians (Other Roles)                                                     | Physician/Osteopath                                                              | Laboratory Service Provider                                           | 7/12/2017        |
| 1598 | V160102 |            | Physicians (Other Roles)                                                     | Physician/Osteopath (Other Roles)                                                | Supplier                                                              | 7/12/2017        |
| 1601 | V130216 | 225200000X | Respiratory, Developmental, Rehabilitative and Restorative Service Providers | Physician/Osteopath                                                              |                                                                       | 7/12/2017        |
| 1602 | V130400 | 225200000X | Respiratory, Developmental, Rehabilitative and Restorative Service Providers | Physician/Osteopath                                                              |                                                                       | 7/12/2017        |
| 1603 | V130404 | 2255R0406X | Respiratory, Developmental, Rehabilitative and Restorative Service Providers | Physical Therapy Assistant                                                       | Rehabilitation, Blind                                                 | 7/12/2017        |
| 1605 | V130209 | 226000000X | Respiratory, Developmental, Rehabilitative and Restorative Service Providers | Physical Therapy Assistant                                                       |                                                                       | 7/12/2017        |
| 1607 | V130508 | 227900000X | Respiratory, Developmental, Rehabilitative and Restorative Service Providers | Specialist/Technologist                                                          |                                                                       | 7/12/2017        |
| 1608 | V130104 |            | Respiratory, Rehabilitative and Restorative Service                          | Recreational Therapist Assistant                                                 | Case Management                                                       | 7/12/2017        |
| 1609 | V130310 |            | Respiratory, Rehabilitative and Restorative Service                          | Respiratory Therapist, Registered                                                | Case Management                                                       | 7/12/2017        |
| 1610 | V130508 |            | Respiratory, Rehabilitative and Restorative Service                          | Occupational Therapist                                                           |                                                                       | 7/12/2017        |
| 1611 | V130511 |            | Respiratory, Rehabilitative and Restorative Service                          | Physical Therapist                                                               | Perinatal                                                             | 7/12/2017        |
| 1612 | V151002 | 246ZF0200X | Technologists, Technicians & Other Technical Service                         | Respiratory Therapist                                                            |                                                                       | 7/12/2017        |
| 1616 | V150313 | 247100000X | Technologists, Technicians & Other Technical Service Providers               | Respiratory Therapist                                                            |                                                                       | 7/12/2017        |
| 1617 | V150301 | 2471V0106X | Technologists, Technicians & Other Technical Service Providers               | Perfusionist                                                                     | Vascular-Interventional Technology                                    | 7/12/2017        |
| 1619 | V150203 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Cardiovascular: Invasive Technology                                   | 7/12/2017        |
| 1620 | V150204 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Cardiology                                                            | 7/12/2017        |
| 1621 | V150205 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiopulmonary-Cardiovascular                                        | 7/12/2017        |
| 1622 | V150207 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Perfusionist                                                          | 7/12/2017        |
| 1623 | V150208 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | ECG                                                                   | 7/12/2017        |
| 1624 | V150304 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Sonography, Diagnostic Cardiac                                        | 7/12/2017        |
| 1625 | V150311 |            | Technologists, Technicians and Other Technical Service                       | Technician, Cardiology                                                           | Radiation Physicist                                                   | 7/12/2017        |
| 1626 | V150313 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Radiographer                                                          | 7/12/2017        |
| 1627 | V150316 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Dosimetrist, Medical                                                  | 7/12/2017        |
| 1628 | V150320 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Magnetic Resonance Imaging (MRI): Radiation Therapy                   | 7/12/2017        |
| 1629 | V150323 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Quality Management: Radiographer                                      | 7/12/2017        |
| 1630 | V150701 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Cardiovascular: Noninvasive Technology                                | 7/12/2017        |
| 1631 | V150702 |            | Technologists, Technicians and Other Technical Service                       | Radiologic Technologist                                                          | Cardiovascular: Vascular Technology                                   | 7/12/2017        |
| 1632 | V150703 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Vascular                                                              | 7/12/2017        |
| 1633 | V150704 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              |                                                                       | 7/12/2017        |
| 1634 | V150801 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Cardiographic                                                         | 7/12/2017        |
| 1635 | V151002 |            | Technologists, Technicians and Other Technical Service                       | Specialist/Technologist, Cardiology                                              | Forensic                                                              | 7/12/2017        |
| 1636 | V151004 |            | Technologists, Technicians and Other Technical Service                       | Technician, Cardiology                                                           | Virology                                                              | 7/12/2017        |

<span id="_Ref488674716" class="anchor"></span>Table 9: Reactivated Person Class Codes—Kernel Patch XU\*8.0\*377

## Reactivated Person Class Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Table 9</u> lists all *reactivated* Person Class codes released with Kernel Patch XU\*8.0\*377 (released on 10/24/2005):

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 32%" />
<col style="width: 18%" />
<col style="width: 17%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th>IEN</th>
<th>VA Code</th>
<th>NUCC<br />
X12 Code</th>
<th>Provider Type</th>
<th>Classification</th>
<th>Area of Specialization</th>
<th>CMS Specialty Code</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>213</td>
<td>V030502</td>
<td>1223G0001X</td>
<td>Dental Providers</td>
<td>Dentist</td>
<td>General Practice</td>
<td></td>
</tr>
<tr class="even">
<td>221</td>
<td>V030600</td>
<td>122400000X</td>
<td>Dental Providers</td>
<td>Denturist</td>
<td></td>
<td>19</td>
</tr>
<tr class="odd">
<td>180</td>
<td>V120100</td>
<td>211D00000X</td>
<td>Podiatric Medicine and Surgery Service Providers</td>
<td>Assistant, Podiatric</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

# Appendix B—Printing VA Person Class Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have VA FileMan access, use VA FileMan's Print File Entries option \[DIPRINT\] to print the PERSON CLASS (#8932.1) file entries, so that you have the classifications and codes.

![](xu-8-671-assigning-person-class-to-providers-user-guide/028.png) NOTE: This task is done only once.

## Report Sorted by Provider Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print entries in the PERSON CLASS(#8932.1) file sorted by Provider Type, perform the following procedure:

1.  From VA FileMan, select the Print File Entries option \[DIPRINT\].
2.  At the "OUTPUT FROM WHAT FILE:" prompt, enter PERSON CLASS.
3.  At the "SORT BY: PROVIDER TYPE//" prompt, enter PROVIDER TYPE;S2;C1 and confirm by selecting the appropriate number.  
      
    The ";S2;C1" portion of the entry formats the report to display the Provider Type in the first column on the second line for each entry.
4.  At the "START WITH PROVIDER TYPE: FIRST//" prompt, press Enter to accept the default.
5.  At the "WITHIN PROVIDER TYPE, SORT BY:" prompt, press Enter to accept the default.
6.  *(Optional)* At the "FIRST PRINT FIELD:" prompt, enter a single question mark "?". Then, at the "Do you want the entire 15-Entry FIELD List?" enter YES to get a list of fields from which to choose.
7.  At the "FIRST PRINT FIELD:" prompt, enter NUMBER.
8.  At the "THEN PRINT FIELD:" prompt, enter AREA OF SPECIALIZATION;W25;"SPECIALTY" and confirm by selecting the appropriate number.  
      
    The ";W25;SPECIALTY" portion of the entry formats the report to title the data column as "SPECIALTY" and wrap the text to the next line after 25 characters.
9.  At the "THEN PRINT FIELD:" prompt, enter VA CODE.
10. At the "THEN PRINT FIELD:" prompt, enter X12 CODE.
11. At the "THEN PRINT FIELD:" prompt, enter STATUS;L8.  
      
    The ";L8" portion of the entry formats the report to left justify and truncate the length of the display to 8 characters.
12. At the "THEN PRINT FIELD:" prompt, press Enter to complete your entries.
13. At the "Heading (S/C): *PERSON CLASS LIST*//" prompt, press Enter to accept the default report heading or enter a DIFFERENT heading.
14. At the "STORE PRINT LOGIC IN TEMPLATE:" prompt, press Enter or enter a name of a print template to store your selections if you want to run this report again.
15. At the "DEVICE:" prompt, press Enter to display the report directly to the screen or enter a specific device.
16. The system displays the report as shown in <u>Figure 15</u>.

<span id="_Ref378843260" class="anchor"></span>Figure 14: Printing Person Class File Entries—Sorted by Provider Type: Sample User Dialogue

Select VA FileMan Option: <span class="mark">PRINT \<Enter\></span> File Entries

OUTPUT FROM WHAT FILE: *<span class="mark">PERSON CLASS</span>*// <span class="mark">\<Enter\></span>

SORT BY: <span class="mark">PROVIDER TYPE</span>// <span class="mark">PROVIDER TYPE;S2;C1</span>

<span class="mark">1 PROVIDER TYPE</span>

2 PROVIDER TYPE CODE

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> PROVIDER TYPE

START WITH PROVIDER TYPE: FIRST// <span class="mark">\<Enter\></span>

WITHIN PROVIDER TYPE, SORT BY: <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">?</span>

Answer with FIELD NUMBER, or LABEL

Do you want the entire 15-Entry FIELD List? <span class="mark">Y \<Enter\></span> (Yes)

Choose from:

.001 NUMBER

.01 PROVIDER TYPE

.011 PROVIDER TYPE CODE

1 CLASSIFICATION

1.1 CLASSIFICATION CODE

2 AREA OF SPECIALIZATION

2.1 AREA OF SPECIALIZATION CODE

3 STATUS

4 DATE INACTIVATED

5 VA CODE

6 X12 CODE

7 reserved

8 SPECIALTY CODE

11 DEFINITION (word-processing)

90002 INDIVIDUAL/NON

TYPE '&' IN FRONT OF FIELD NAME TO GET TOTAL FOR THAT FIELD,

'!' TO GET COUNT, '+' TO GET TOTAL & COUNT, '#' TO GET MAX & MIN,

'\]' TO FORCE SAVING PRINT TEMPLATE

TYPE '\[TEMPLATE NAME\]' IN BRACKETS TO USE AN EXISTING PRINT TEMPLATE

YOU CAN FOLLOW FIELD NAME WITH ';' AND FORMAT SPECIFICATION(S)

FIRST PRINT FIELD: <span class="mark">NUMBER</span>

THEN PRINT FIELD: <span class="mark">AREA OF SPECIALIZATION;W25;"SPECIALTY"</span>

<span class="mark">1 AREA OF SPECIALIZATION</span>

2 AREA OF SPECIALIZATION CODE

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> AREA OF SPECIALIZATION

THEN PRINT FIELD: <span class="mark">AREA OF SPECIALIZATION CODE;W5;"SPECIALTY CODE"</span>

THEN PRINT FIELD: <span class="mark">VA CODE</span>

THEN PRINT FIELD: <span class="mark">X12 CODE</span>

THEN PRINT FIELD: <span class="mark">STATUS;L8</span>

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

Heading (S/C): <span class="mark">PERSON CLASS LIST</span>// <span class="mark">\<Enter\></span>

STORE PRINT LOGIC IN TEMPLATE: <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Network

![](xu-8-671-assigning-person-class-to-providers-user-guide/029.png) NOTE: For display purposes only, the report in <u>Figure 15</u> has been abbreviated.

<span id="_Ref378843330" class="anchor"></span>Figure : Person Class List—Sample Report

PERSON CLASS LIST JAN 30,2014 10:51 PAGE 2

NUMBER SPECIALTY VA CODE X12 CODE STATUS

--------------------------------------------------------------------------------

PROVIDER TYPE: <span class="mark">Allopathic & Osteopathic Physicians</span>

1137 Sleep Medicine V180707 207QS1201X Active

1152 Hospice and Palliative V182605 2081H0002X Active

Medicine

1154 Child Abuse Pediatrics V180506 2080C0008X Active

1157 V182415 202K00000X Active

1158 Clinical Pathology V182416 207ZC0006X Active

1166 Pediatric Orthopaedic V182107 207XP3100X Active

Surgery

1169 V181550 204R00000X Active

1171 Hypertension Specialist V182605 207RH0005X Active

1176 Female Pelvic Medicine V181807 207VF0040X Active

and Reconstructive

Surgery

1177 Behavioral Neurology & V182914 2084B0040X Active

Neuropsychiatry

...

PROVIDER TYPE: <span class="mark">Behavioral Health and Social Service Providers</span>

350 V010400 103T00000X Active

351 Behavioral V010401 103TB0200X Active

352 Clinical V010403 103TC0700X Active

354 Counseling V010404 103TC1900X Active

355 Family V010405 103TF0000X Active

356 Forensic V010406 103TF0200X Active

357 Health V010407 103TH0100X Active

358 School V010408 103TS0200X Active

...

PROVIDER TYPE: <span class="mark">Chiropractic Providers</span>

194 V020000 111N00000X Active

195 Internist V020100 111NI0900X Active

196 Neurology V020200 111NN0400X Active

197 Nutrition V020300 111NN1001X Active

198 Occupational Health V020400 111NX0100X Active

199 Orthopedic V020500 111NX0800X Active

200 Radiology V020600 111NR0200X Active

201 Sports Physician V020700 111NS0005X Active

202 Thermography V020800 111NT0100X Active

1132 Pediatric Chiropractor V020900 111NP0017X Active

1182 Rehabilitation V020601 111NR0400X Active

...

## Report Sorted by VA Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print entries in the PERSON CLASS (#8932.1) file sorted by VA Code, perform the following procedure:

1.  From VA FileMan, select the Print File Entries option \[DIPRINT\].
17. At the "OUTPUT FROM WHAT FILE:" prompt, enter PERSON CLASS.
18. At the "SORT BY: PROVIDER TYPE//" prompt, enter VA CODE
19. At the "START WITH VA CODE: FIRST//" prompt, press Enter to accept the default.
20. At the "WITHIN VA CODE, SORT BY:" prompt, press Enter to accept the default.
21. At the "FIRST PRINT FIELD:" prompt, enter NUMBER.
22. At the "THEN PRINT FIELD:" prompt, enter STATUS;L8.
23. At the "THEN PRINT FIELD:" prompt, enter VA CODE.
24. At the "THEN PRINT FIELD:" prompt, enter X12 CODE.
25. At the "THEN PRINT FIELD:" prompt, enter SPECIALTY CODE.
26. At the "THEN PRINT FIELD:" prompt, enter PROVIDER TYPE;S1;C1 and confirm by selecting the appropriate number.
27. At the "THEN PRINT FIELD:" prompt, enter CLASSIFICATION;S1;C1 and confirm by selecting the appropriate number.
28. At the "THEN PRINT FIELD:" prompt, enter AREA OF SPECIALIZATION; S1;C1;"SPECIALTY" and confirm by selecting the appropriate number.
29. At the "THEN PRINT FIELD:" prompt, press Enter to complete your entries.
30. At the "Heading (S/C): PERSON CLASS LIST//" prompt, press Enter to accept the default report heading or enter a different heading.
31. At the "STORE PRINT LOGIC IN TEMPLATE:" prompt, press Enter or enter a name of a print template to store your selections if you want to run this report again.
32. At the "DEVICE:" prompt, press Enter to display the report directly to the screen or enter a specific device.
33. The system displays the report.

<span id="_Toc501605861" class="anchor"></span>Figure 16: Printing Person Class File Entries—Sorted by VA Code: Sample User Dialogue

Select OPTION: <span class="mark">PRINT FILE ENTRIES</span>

OUTPUT FROM WHAT FILE: *<span class="mark">PERSON CLASS</span>*// <span class="mark">\<Enter\></span>

SORT BY: PROVIDER TYPE// <span class="mark">VA CODE</span>

START WITH VA CODE: FIRST// <span class="mark">\<Enter\></span>

  WITHIN VA CODE, SORT BY: <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">NUMBER</span>

THEN PRINT FIELD: <span class="mark">STATUS;L8</span>

THEN PRINT FIELD: <span class="mark">VA CODE</span>

THEN PRINT FIELD: <span class="mark">X12 CODE</span>

THEN PRINT FIELD: <span class="mark">SPECIALTY CODE</span>

THEN PRINT FIELD: <span class="mark">PROVIDER TYPE;S1;C1</span>

1 PROVIDER TYPE

2 PROVIDER TYPE CODE

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> PROVIDER TYPE

THEN PRINT FIELD: <span class="mark">CLASSIFICATION;S1;C1</span>

1 CLASSIFICATION

2 CLASSIFICATION CODE

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> CLASSIFICATION

THEN PRINT FIELD: <span class="mark">AREA OF SPECIALIZATION;S1;C1;"SPECIALTY"</span>

1 AREA OF SPECIALIZATION

2 AREA OF SPECIALIZATION CODE

CHOOSE 1-2: <span class="mark">1 \<Enter\></span> AREA OF SPECIALIZATION

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

Heading (S/C): PERSON CLASS LIST// <span class="mark">\<Enter\></span>

STORE PRINT LOGIC IN TEMPLATE: <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Network

![](xu-8-671-assigning-person-class-to-providers-user-guide/030.png) REF: For sample data, see <u>Table 3</u>.

## Report of Classifications Only

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To print entries in the PERSON CLASS (#8932.1) file for Classification codes only, perform the following procedure:

1.  From VA FileMan, select the Print File Entries option \[DIPRINT\].
34. At the "OUTPUT FROM WHAT FILE:" prompt, enter PERSON CLASS.
35. At the "SORT BY: PROVIDER TYPE//" prompt, enter CLASSIFICATIONCODE.
36. At the "START WITH CLASSIFICATION CODE: FIRST//" prompt, press Enter to accept the default.
37. At the "WITHIN CLASSIFICATION CODE, SORT BY:" prompt, press Enter to accept the default.
38. At the "FIRST PRINT FIELD:" prompt, enter CLASSIFICATION CODE;N.  
      
    The ";N" portion of the entry formats the report to suppress consecutive duplicate values.
39. At the "THEN PRINT FIELD:" prompt, press Enter to complete your entries.
40. At the "Heading (S/C): PERSON CLASS LIST//" prompt, press Enter to accept the default report heading or enter a DIFFERENT heading.
41. At the "DEVICE:" prompt, press Enter to display the report directly to the screen or enter a specific device.
42. The system displays the report.

<span id="_Toc501605862" class="anchor"></span>Figure 17: Printing Person Class File Entries—Classification Codes: Sample User Dialogue

Select VA FileMan Option: <span class="mark">PRINT \<Enter\></span> File Entries

OUTPUT FROM WHAT FILE: *PERSON CLASS*// <span class="mark">\<Enter\></span>

SORT BY: PROVIDER TYPE// <span class="mark">CLASSIFICATION CODE</span>

START WITH CLASSIFICATION CODE: FIRST// <span class="mark">\<Enter\></span>

WITHIN CLASSIFICATION CODE, SORT BY: <span class="mark">\<Enter\></span>

FIRST PRINT FIELD: <span class="mark">CLASSIFICATION CODE;N</span>

THEN PRINT FIELD: <span class="mark">\<Enter\></span>

Heading (S/C): PERSON CLASS LIST// <span class="mark">\<Enter\></span>

DEVICE: <span class="mark">\<Enter\></span> Network

<span id="_Toc501609606" class="anchor"></span>Glossary

| Term  | Definition                                                      |
|-------|-----------------------------------------------------------------|
| CMS   | Centers for Medicare & Medicaid Services                        |
| HCFA  | Health Care Financing Administration                            |
| HSP   | Health Systems Platform                                         |
| IRM   | Information Resource Management                                 |
| NPCD  | National Patient Care Database                                  |
| NUCC  | National Uniform Claim Committee                                |
| VistA | Veterans Health Information Systems and Technology Architecture |

![](xu-8-671-assigning-person-class-to-providers-user-guide/031.png) REF: For a list of commonly used terms and definitions, see the OIT Master Glossary VA Intranet Website.  
  
For a list of commonly used acronyms, see the VA Acronym Lookup Intranet Website.

<span id="_Toc501609607" class="anchor"></span>Index

A

Acronyms

Intranet Website, 183

Appendix A—Person Class Codes

New, Updated, Inactivated, and Reactivated, 15

Appendix B—Printing VA Person Class Data, 177

Assigning Person Class to Providers

Introduction, 1

Overview, 5

Assumptions, x

C

Conventions

Documentation, vii

D

Data Dictionary

Data Dictionary Utilities Menu, x

Listings, x

Databases

National Patient Care Database (NPCD), 1

Deactivate a User, 9

Deactivate a User Option, 9

DIEDIT Option, 11, 12

DIPRINT Option, 177, 180, 181

Disclaimers

Documentation, vii

Software, vi

Documentation

Conventions, vii

Disclaimers, vii

Documentation Navigation, ix

E

Edit

Person Class

Procedure, 6

Edit an Existing User Option, 13

Edit Person Class

Overview, 5

Edits of Person Class Data

IRM, 13

EFFECTIVE DATE (#.02) Field, 2

Enter or Edit File Entries Option, 11, 12

Enter/Edit Person Class Data, 3

Examples

Edit Person Class, 6

EXPIRATION DATE (#.03) Field, 2

F

Fields

EFFECTIVE DATE (#.02), 2

EXPIRATION DATE (#.03), 2

PERSON CLASS (#.01), 2

PERSON CLASS Multiple (200.05#), 2

Files

NEW PERSON (#200), 2, 3

PERSON CLASS (#8932.1), x, 1, 2, 3, 10, 15, 177, 180, 181

G

Glossary, 183

Intranet Website, 183

H

HCFA Provider Codes, 1

Help

At Prompts, ix

Online, ix

Question Marks, ix

Home Pages

Acronyms Intranet Website, 183

Adobe Website, xi

Glossary Intranet Website, 183

Kernel Website, x

QuadraMed, 2

VA Software Document Library (VDL) Website, xi

VistA Development Website, vii

How to

Obtain Technical Information Online, ix

Use this Manual, vi

I

Identify All Active Providers

Overview, 3

Procedure, 4

Identify Providers with Inactive Person Class Entries

Overview, 4

Procedure, 4

Intended Audience, vi

Introduction

Assigning Person Class to Providers, 1

IRM

Edits of Person Class Data, 13

K

Kernel, 1

Patches

XU\*8.0\*27, 1

XU\*8.0\*377, 1

XU\*8.0\*531, 1

Website, x

L

List File Attributes Option, x

List Inactive Person Class Users Option, 4

M

Menus

Data Dictionary Utilities, x

User Management, 4, 5, 6, 9, 13

XUSER, 4, 5, 6, 9, 13

N

National Patient Care Database (NPCD), 1

NEW PERSON (#200) File, 2, 3

O

Obtaining

Data Dictionary Listings, x

Online

Documentation, ix

Technical Information, How to Obtain, ix

Options

Data Dictionary Utilities, x

Deactivate a User option, 9

DIEDIT, 11, 12

DIPRINT, 177, 180, 181

Edit an Existing User, 13

Enter or Edit File Entries, 11, 12

List File Attributes, x

List Inactive Person Class Users, 4

Person Class Edit, 5, 6, 13

Print File Entries, 177, 180, 181

Reactivate a User option, 9

Remove a person class entry, 9, 10

User Management, 4, 5, 6, 9, 13

User PC build Print, 3, 4

XU-INACTIVE PERSON CLASS USERS, 4

XU-PERSON CLASS EDIT, 5, 6, 13

XU-PERSON CLASS REMOVE, 9, 10

XUSER, 4, 5, 6, 9, 13

XUSER PC BUILD, 3, 4

XUSERDEACT, 9

XUSEREDIT, 13

XUSERREACT, 9

Orientation, vi

Overview

Edit Person Class, 5

Identify All Active Providers, 3

Identify Providers with Inactive Person Class Entries, 4

Reactivating Person Class Entries, 10

P

Patches

XU\*8.0\*27, 1

XU\*8.0\*377, 1

XU\*8.0\*531, 1

PERSON CLASS (#.01) Field, 2

PERSON CLASS (#8932.1) File, x, 1, 2, 3, 10, 15, 177, 180, 181

Person Class Codes Reactivated

Patch XU\*8.0\*377, 176

Person Class Edit Option, 5, 6, 13

PERSON CLASS Multiple Field (200.05#), 2

Print File Entries Option, 177, 180, 181

Printing VA Person Class Data, 177

Procedures

Assigning Person Class to Providers, 6

Edit Person Class, 6

Identify All Active Providers, 4

Identify Providers with Inactive Person Class Entries, 4

Reactivating Person Class Entries, 10

Report of Classifications Only, 181

Report Sorted by Provider Type, 177

Report Sorted by VA Code, 180

PROVIDER Security Key, 3

PS Anonymous Directories, xi

Q

QuadraMed Home Page, 2

Question Mark Help, ix

R

Reactivate a User, 9

Reactivate a User Option, 9

Reactivated

Person Class Codes

Patch XU\*8.0\*377, 176

Reactivating Person Class Entries

Overview, 10

Procedure, 10

Reference Materials, x

Relations

Assigning Person Class to Providers, 1

Kernel, 1

Remove a person class entry Option, 9, 10

Report of Classifications Only

Procedure, 181

Report Sorted by Provider Type

Procedure, 177

Report Sorted by VA Code

Procedure, 180

S

Security Keys

PROVIDER, 3

Software

Disclaimer, vi

Steps

Assigning Person Class to Providers, 6

Edit Person Class, 6

Identify All Active Providers, 4

U

URLs

Acronyms Intranet Website, 183

Adobe Website, xi

Glossary Intranet Website, 183

Kernel Website, x

QuadraMed Home Page, 2

VA Software Document Library (VDL) Website, xi

VistA Development Website, vii

Use this Manual, How to, vi

User Information

Enter/Edit Person Class Data, 3

User Management Menu, 4, 5, 6, 9, 13

User PC build Print Option, 3, 4

Users

Deactivate, 9

Reactivate, 9

V

VA Software Document Library (VDL)

Website, xi

W

Web Pages

QuadraMed Home Page, 2

Websites

Acronyms Intranet Website, 183

Adobe Website, xi

Glossary Intranet Website, 183

Kernel Website, x

VA Software Document Library (VDL) Website, xi

VistA Development Website, vii

X

XU-INACTIVE PERSON CLASS USERS Option, 4

XU-PERSON CLASS EDIT Option, 5, 6, 13

XU-PERSON CLASS REMOVE Option, 9, 10

XUSER Menu, 4, 5, 6, 9, 13

XUSER PC BUILD Option, 3, 4

XUSERDEACT Option, 9

XUSEREDIT Option, 13

XUSERREACT Option, 9