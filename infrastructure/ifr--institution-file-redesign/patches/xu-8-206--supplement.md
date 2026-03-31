---
title: IFR XU*8*206-416 Supplement to Patch Description
doc_type: PDD
doc_label: Patch Description Document
doc_layer: patch
doc_subject: 416 Supplement to Patch Description
app_code: IFR
app_name: Institution File Redesign
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*206
group_key: "IFR:XU:8"
file_numbers: []
security_keys: []
menu_options: 8
description: This supplemental documentation is intended for use in conjunction with the Institution File Redesign (IFR)-related software patches (i.e., Kernel Patch XU\8.0\206). It outlines the details of the work involved in the IFR software and gives guidelines for how the generic APIs can be used to standard
audience: 
keywords: 
  - institution
  - strong
  - class
  - xumf
  - facility
  - master
  - station
  - patch
  - number
  - kernel
page_count: 0
word_count: 30631
section_count: 8
table_count: 235
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: June 2001
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Institution_File_Redesign_(IFR)/krn8_0p416sp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Institution_File_Redesign_(IFR)/krn8_0p416sp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=9"
---

![](ifr-xu-8-206-416-supplement-to-patch-description/001.png)

INSTITUTION FILE REDESIGN (IFR)SUPPLEMENT TO PATCH DESCRIPTION

Patch XU\*8.0\*206

June 2001

Revised: February 2007

VHA OI Health Systems Design & Development (HSD&D)

Infrastructure & Security Services (ISS)

### Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 41%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>06/01</td>
<td>1.0</td>
<td><p>Initial Institution File Redesign (IFR) software supplemental patch documentation creation.</p>
<p>Kernel Patch XU*8.0*206</p></td>
<td><ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>09/01</td>
<td>1.1</td>
<td>Corrected references to CPRS and OE/RR software versions with regard to Patch OR*3.0*209.</td>
<td>Development Team Oakland, CA &amp; Bay Pines, FL OIFOs</td>
</tr>
<tr class="even">
<td>02/16/05</td>
<td>2.0</td>
<td><p>Kernel V. 8.0 documentation reformatting/revision.</p>
<p>Documentation content updated for the following Kernel Patches: XU*8.0*217, XU*8.0*218, XU*8.0*261, XU*8.0*287, XU*8.0*294, and XU*8.0*335.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: MMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>05/24/05</td>
<td>2.1</td>
<td>Updated file list for new MASTER FILE PARAMETERS file (#4.001) and added the HL7 Application Parameters, HL LOGICAL LINK entries, Protocols, and mail group for the new version of the Master File Server (XUMFX namespace) introduced with Kernel Patch XU*8.0*299.</td>
<td>Development Team Oakland, CA &amp; Bay Pines, FL OIFOs</td>
</tr>
<tr class="even">
<td>07/06/05</td>
<td>2.2</td>
<td><p>Updated references to the IMF address edit option to IMF edit.</p>
<p>Also, corrected missing table cross-reference.</p></td>
<td>Development Team Oakland, CA &amp; Bay Pines, FL OIFOs</td>
</tr>
<tr class="odd">
<td>06/20/06</td>
<td>2.3</td>
<td><p>Updates:</p>
<ul>
<li><blockquote>
<p>Corrected output array subscript in the F4^XUAF4 API from "STATION NUMER" to "STATION NUMBER. (Remedy #HD0000000147298)</p>
</blockquote></li>
<li><blockquote>
<p>Updated document format to follow latest ISS Guidelines and SOP.</p>
</blockquote></li>
</ul></td>
<td><p>Institution File Redesign Development Team Bay Pines, FL and Oakland, CA OIFOs:</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>02/21/07</td>
<td>3.0</td>
<td><p>Updates:</p>
<ul>
<li><blockquote>
<p>Updated document format to follow latest ISS Guidelines and SOP.</p>
</blockquote></li>
<li><blockquote>
<p>Added major section header breaks. Also, moved chapters and appendices around throughout the document. Updated all Table of Contents (TOC), Table of Figures and Tables, and Index entries.</p>
</blockquote></li>
<li><blockquote>
<p>Updated content for new/modified options, routines, etc. with the release of Kernel Patch XU*8.0*416.</p>
</blockquote></li>
<li><blockquote>
<p>Corrected spelling, grammar, and other content changes based on review by Kathleen Barnett.</p>
</blockquote></li>
</ul></td>
<td><p>Institution File Redesign Development Team Bay Pines, FL and Oakland, CA OIFOs:</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc159835394" class="anchor"></span>Table i. Documentation revision history

Patch Revisions

For the current patch history related to the Kernel software, please refer to the Patch Module on FORUM.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/002.png)</td>
<td><p><strong>NOTE:</strong> Kernel is the designated custodial software application for the Institution File Redesign (IFR)-related software. Kernel Patch XU*8.0*206 is designated as the primary Kernel patch for the IFR software and is referenced throughout this documentation.</p>
<p>Originally, the IFR software was released to the field as Kernel Patch XU*8.0*126 but was re-released and is superseded by Kernel Patch XU*8.0*206. In addition, through the years subsequent IFR-related software patches have been released in order to continually maintain and update the IFR software. The documentation is continually updated to reflect the latest changes due to these patches and supersedes any previous documentation.</p></td>
</tr>
</tbody>
</table>

Contents

### Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Figure 2‑19. Using the Delete local/dup. station \# (DSTA) action—Deleting local and duplicate  
entries [2-29](#_Ref159820558)](#_Ref159820558)

[Figure 2‑20. Using the Delete local/dup. station \# (DSTA) action—Unresolved duplicates [2-30](#_Ref159820904)](#_Ref159820904)

[Figure 2‑21. Using the Delete local/dup. station \# (DSTA) action—No unresolved duplicates [2-30](#_Ref159820948)](#_Ref159820948)

[Figure 2‑22. Using the Resolve duplicate station numbers (RDSN) action—Resolving  
duplicates (1) [2-31](#_Ref159821353)](#_Ref159821353)

[Figure 2‑23. Using the Resolve duplicate station numbers (RDSN) action—Resolving  
duplicates (2) [2-33](#_Ref159821457)](#_Ref159821457)

[Figure 2‑24. Using the Resolve duplicate station numbers (RDSN) action—All duplicates resolved [2-35](#_Ref159821363)](#_Ref159821363)

[Figure 2‑25. Using the Auto update with national data (AUTO) action—After eliminating  
duplicates [2-36](#_Ref159821731)](#_Ref159821731)

[Figure 3‑5. Sample INSTITUTION file update message sent to the XUMF INSTITUTION mail  
group [3-7](#_Ref159823180)](#_Ref159823180)

[Table 6‑12. Associated patches required for installation prior to installing Kernel Patch  
XU\*8.0\*206 [6-20](#_Toc159835458)](#_Toc159835458)

[Table 6‑13. Supported references for the IFR-related software—Alphabetized by entry point [6-23](#_Toc159835459)](#_Toc159835459)

[Table 6‑14. Controlled subscription references for the IFR-related software—Alphabetized by entry  
point [6-23](#_Toc159835460)](#_Toc159835460)

### Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Institution File Redesign (IFR) Project Team consists of the following Infrastructure & Security Services (ISS) personnel:

- REDACTED

The IFR Project Team would like to thank the following sites/organizations for their assistance in reviewing and/or testing the IFR-related software (i.e., Kernel Patch XU\*8.0\*206) and documentation (listed alphabetically):

- Austin Automation Center (AAC)
- Battle Creek Veterans Affairs Medical Center (VAMC)
- Birmingham Office of Information Field Office (OIFO)
- Dayton, OH VAMC
- Independent Verification & Validation (IV&V)
- Montana Health Care System (HCS)
- VA North Texas HCS
- National Database Integration (NDBI)
- Application Structure and Integration Services (ASIS)
- Washington, D.C. VAMC

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/003.png) | REF: For a list of other supporting documents that were reviewed and contributors that were consulted throughout this project, please refer to "Appendix A—Reference Materials" in this manual. |

### Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instruction are offered about the numerous tools and functionality that Institution File Redesign (IFR)-related software (Kernel V. 8.0) provides for overall Veterans Health Information Systems and Technology Architecture (VistA) management. For example, site parameters are discussed in various topics throughout this manual.

This supplemental documentation to the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) is organized into several major sections based on the following functional divisions, portions of which may also be included in the Kernel V. 8.0 documentation:

> 1\. User Guide Information

> A. Local Site IMF Administrator Duties

> B. FORUM (Production) IMF Administrator Duties

> 2\. Programmer Manual Information

> 3\. Technical Manual Information

There are no special legal requirements involved in the use of IFR-related software.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                     |
| ![](ifr-xu-8-206-416-supplement-to-patch-description/004.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](ifr-xu-8-206-416-supplement-to-patch-description/005.png)                                                              | CAUTION or DISCLAIMER: Used to caution the reader to take special notice of critical information.               |

<span id="_Ref345831418" class="anchor"></span>Table ii. Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., roll-and-scroll screen or character-based screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface.
- References to "\<Enter\>" within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within angle brackets (\< \>). For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/006.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- This manual refers in many places to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and M will be considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M "\>" prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

> \>D ^XUP

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/007.png) | NOTE: Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of the software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/008.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" topic of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

This manual provides an overall explanation of the use, maintenance, and implementation of the Institution File Redesign (IFR)-related software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) and VA Intranet for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about Kernel should consult the following:

- *Kernel Release Notes*
- *Kernel Installation Guide*
- *Kernel Technical Manual*
- *Kernel Systems Management Guide*
- *Kernel Developer's Guide*
- *Kernel Security Tools Manual*
- The following Web pages:
- Institution File Redesign (IFR) Home Page:

> <http://vista.med.va.gov/kernel/index.asp#ifr>

- Kernel Home Page:

> <http://vista.med.va.gov/kernel/index.asp>

> These sites contain other information and provide links to additional documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/009.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the Adobe Acrobat Reader, please refer to the "Adobe Acrobat Quick Guide" at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

VistA documentation can be downloaded from the Health Systems Design and Development (HSD&D) VistA Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Enterprise VistA Support (EVS) anonymous directories:

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED
- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/010.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# User Guide


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Revision History](#revision-history)
    - [Figures and Tables](#figures-and-tables)
    - [Acknowledgements](#acknowledgements)
    - [Orientation](#orientation)
- [User Guide](#user-guide)
  - [Introduction](#introduction)
  - [Local Site IMF Administrator Duties](#local-site-imf-administrator-duties)
  - [FORUM (Production) IMF Administrator Duties](#forum-production-imf-administrator-duties)
- [Developer's Guide](#developers-guide)
  - [Data Dictionary Modifications](#data-dictionary-modifications)
  - [Application Program Interfaces (APIs)](#application-program-interfaces-apis)
- [Systems Management Guide](#systems-management-guide)
  - [Implementation and Maintenance](#implementation-and-maintenance)
  - [Software Product Security](#software-product-security)
    - [Glossary](#glossary)
    - [Appendix A—Reference Materials](#appendix-areference-materials)
    - [Appendix B—Facility Type Acronyms](#appendix-bfacility-type-acronyms)
    - [Index](#index)
This is the User Guide section of this supplemental documentation for the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206). It details the user-related IFR documentation (e.g., overview of the IFR, Local and FORUM Administrator duties, management of IFR-related software, etc.).

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This supplemental documentation is intended for use in conjunction with the Institution File Redesign (IFR)-related software patches (i.e., Kernel Patch XU\*8.0\*206). It outlines the details of the work involved in the IFR software and gives guidelines for how the generic APIs can be used to standardize the collection and storage of Institution data across Veterans Health Administration (VHA).

The intended audience for this documentation is Veterans Health Information Systems and Technology Architecture (VistA) sites' Information Resource Management (IRM) and the Automated Data Processing Application Coordinators (ADPACS). However, it can also be helpful to the Master Patient Index/Patient Demographics (MPI/PD) Team, the Messaging & Interface Services (M&IS) Team, others in VHA Office of Information (OI) Health Systems Design & Development (HSD&D), Enterprise VistA Support (EVS), the OI EVS National Data Base Integration (NDBI) Team, the Program Office, and Application Structure and Integration Services (ASIS).

#### Master Files—What is the Problem?

In an open-architecture healthcare environment, there often exists a set of common reference files used by one or more applications. These files are called "master files." The INSTITUTION (#4) and FACILITY TYPE (#4.1) files are two examples of Veterans Health Information Systems and Technology Architecture (VistA) master files. With the advent of VA-wide data exchange initiatives, such as Master Patient Index/Patient Demographics (MPI/PD), the need to maintain reliable and accurate data within these master files across all Veterans Health Administration (VHA) sites has become more apparent.

Currently, the VHA does *not* automate updates and synchronization of *national* entries in standard master files utilized VHA-wide. Each individual VHA site is responsible for updating and maintaining the INSTITUTION and FACILITY TYPE master files located at their site. Through time and due to many unforeseen circumstances, these master files no longer contain accurate, synchronized *national* data. Thus, there is a need to provide a mechanism to automatically maintain reliable, accurate, and synchronized *national* data within the INSTITUTION and FACILITY TYPE master files across all sites VHA-wide.

#### Purpose

The Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) provides the mechanism to standardize *national* entries in VistA's INSTITUTION (#4) and FACILITY TYPE (#4.1) master files and automatically update and maintain synchronization of these files at all sites VHA-wide. It also provides the baseline software to maintain other master files in the future. Thus, Kernel Patch XU\*8.0\*206 ensures that the data in the INSTITUTION and the FACILITY TYPE master files is reliable, accurate, and consistent VHA-wide. This allows sites to easily establish data sharing relationships without the overhead of researching each other's INSTITUTION and FACILITY TYPE file's data. This in turn ensures that future CIO initiatives involving multi-site data exchange will operate more effectively and efficiently.

In addition, Kernel Patch XU\*8.0\*206 does *not* alter the currently existing procedures for the following:

- Requesting a New Station Number—The Information Management Service (045A4) will continue to approve the official Station Numbers. Non-VA Institutions *must* receive a Station Number to be included in the Institution Master File; VISN directors will continue to request new Station Numbers from the Chief Network Officer (10N).
- Austin Automation Center (AAC) Coordination Requirements—The coordination requirements currently placed on sites by the Austin Automation Center (AAC) are *not* affected by this patch. The Institution Master File (IMF) on FORUM will immediately be updated upon notification from the Information Management Service (045A4). That updated data will then be immediately transmitted to all local INSTITUTION files (#4) VHA-wide via the Master File Server (MFS). This patch does *not* require any additional coordination with the AAC. The same, current procedures will be followed when the AAC has *not yet* updated its tables to include new Station Numbers stored in the INSTITUTION file (#4).
- National Data Base Integration (NDBI) Procedures—NDBI will create new integrated sites *after* a new Station Number has been added to the Institution Master File (IMF) on FORUM and that information has been transmitted VHA-wide. Subsequent procedures followed by NDBI will remain the same.

#### Detailed Solution

Infrastructure & Security Services (ISS) released Kernel Patches XU\*8.0\*206, 209, and other subsequent patches to automate the update and synchronization of the INSTITUTION (#4) and FACILITY TYPE (#4.1) master files VHA-wide.

#### IFR Software-related Kernel Patches—Components

#### Kernel Patch XU\*8.0\*206

Kernel Patch XU\*8.0\*206 establishes the following components, which are described in greater detail in the topics that follow:

- Institution Master File (IMF)—A coordinated and synchronized INSTITUTION file (#4). The INSTITUTION file located on FORUM serves as the IMF that originates the data entries flagged as "National" and approved by Information Management Service (045A4) that are transmitted to and synchronized with each local site's INSTITUTION file VHA-wide.

|                                                                                                                |                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/011.png) | NOTE: Local-based Institution data is not stored in the INSTITUTION file located on FORUM. |

- Facility Type Master File (FMF)—A coordinated and synchronized FACILITY TYPE file (#4.1). The FACILITY TYPE file located on FORUM serves as the FMF that originates the data entries flagged as "National" and approved by Information Management Service (045A4) that are transmitted to and synchronized with each local site's FACILITY TYPE file VHA-wide.

|                                                                                                                |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/012.png) | NOTE: Local-based Facility Type data is *not* stored in the FACILITY TYPE file (#4.1) located on FORUM. |

- Master File Server (MFS)—A server mechanism that does the following:
- Broadcasts updated *national* entries in the master files on FORUM (e.g., IMF) for update and synchronization VHA-wide.
- Allows local sites to query the INSTITUTION (#4) and FACILITY TYPE (#4.1) master files on FORUM for cleanup of the local site's master files (see the following bulleted item).

> One or more FORUM Institution Master File Administrators will be assigned to maintain and update the INSTITUTION (#4) and FACILITY TYPE (#4.1) master files on FORUM for propagation VHA-wide.

- Cleanup Utilities—Utilities to help sites "clean up" their local INSTITUTION file (#4) and FACILITY TYPE file (#4.1). This "cleanup" includes resolution of duplicate Station Numbers and a merge of *national* data from the Institution Master File (IMF) located on FORUM with the data in a local site's INSTITUTION file (#4). In the background, it also merges *national* data from the Facility Type Master File (IMF) located on FORUM with the data in a local site's FACILITY TYPE file.

|                                                                                                                |                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/013.png) | REF: For more specific information on the Cleanup Utilities, please refer to the "Institution File Cleanup Process" topic in Chapter 2, "Local Site IMF Administrator Duties," in this manual. |

- Historical Institution Data—Kernel Patch XUY\*8.0\*206 adds the HISTORY Multiple field (#999) to the INSTITUTION file (#4). It contains historical data with effective dates regarding *national* Institution Station Number and Name changes.

|                                                                                                                |                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/014.png) | REF: For more specific information on the historical data, please refer to the "HISTORY Multiple Field (#999) in the INSTITUTION File (#4)" topic in Chapter 4, "Data Dictionary Modifications," in this manual. |

- Application Program Interfaces (APIs)—Provide entry points for programmers in order to:
- Customize the Master File Server (MFS).
- Return time-sensitive (historical) information from the INSTITUTION file (#4).

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/015.png) | REF: For more information on the APIs, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

####### FORUM Institution Master File (IMF)

Kernel Patch XU\*8.0\*206 establishes the INSTITUTION file (#4) located on FORUM as the Institution Master File (IMF). The IMF on FORUM (or "Gold" file) provides the following:

- Storage of all *national* Station Numbers approved by Information Management Service (045A4), regardless of their current status (e.g., active, inactive, etc.). The software does *not* allow duplicate Station Numbers. Sites *cannot* edit the STATION NUMBER field nor can they edit certain other fields of a *national* entry in their local INSTITUTION file (#4); the software locks them out.

|                                                                                                                |                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/016.png) | REF: For more information on editing local or National entries in the INSTITUTION file, please refer to the "Local Sites Step-By-Step Procedures—Institution File Data Review/Check" topic in Chapter 2,"Local Site IMF Administrator Duties," in this manual. |

- Storage of new *national* Health Care facility names.
- Standardized Institution names VHA-wide for IMF entries.

Per VHA DIRECTIVE 97-058, which provides guidance for the assignment of Station Number suffix identifiers for outpatient clinic facilities, all outpatient clinic facilities will be given a Station Number suffix identifier. Requests to add or delete an outpatient clinic are submitted to the Director, Information Management Service (045A4) through the Chief Network Office (10N) at VHA Headquarters. The Network Management Support Office (10NA) notifies the respective VISN of approved Station Number suffix identifier.

VHA Health Systems Design & Development's Infrastructure & Security Services (ISS) Team was added to the Information Management Service distribution list (i.e., 045A4). Members of the Enterprise VistA Support (EVS) serve as the FORUM Institution Master File (IMF) Administrators. If a site has a request or requires an update to the IMF, they should log a Remedy ticket. The Remedy category is Application-VistA; the Remedy Type is Institution File Redesign. Also, the IMF Administrators can be contacted on FORUM via the following e-mail group: REDACTED

The FORUM IMF Administrators are responsible for updating the Institution Master File (i.e., the INSTITUTION file \[#4\] located on FORUM) with *national* Station Number, Name, and other *national* Institution data changes.

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/017.png) | REF: The duties of the FORUM Institution Master File Administrators are explained in greater detail in Chapter 3, "FORUM (Production) IMF Administrator Duties," in this manual. |

####### FORUM Facility Type Master File (FMF)

Kernel Patch XU\*8.0\*206 establishes the FACILITY TYPE file (#4.1) located on FORUM as the Facility Type Master File (FMF). The FMF on FORUM provides the following:

- Storage of all *national* Facility Types approved by Information Management Service (045A4).
- Storage of new *national* Health Care Facility Types.
- Standardized Facility Types VHA-wide for FMF entries.

VHA Health Systems Design & Development's Infrastructure & Security Services (ISS) Team was added to the Information Management Service distribution list (i.e., 045A4). Members of the Enterprise VistA Support (EVS) serve as the FORUM Institution Master File (IMF) Administrators. If a site has a request or requires an update to the IMF, they should log a Remedy ticket. The Remedy category is Application-VistA; the Remedy Type is Institution File Redesign. Also, the IMF Administrators can be contacted on FORUM via the following e-mail group: [REDACTED](mailto:G.XUMF%20INSTITUTION@FORUM.VA.GOV).

The FORUM IMF Administrators are responsible for updating the Facility Type Master File (i.e., the FACILITY TYPE file \[#4.1\] located on FORUM) with *national* Facility Type data changes.

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/018.png) | REF: The duties of the FORUM Institution Master File Administrators are explained in greater detail in Chapter 3, "FORUM (Production) IMF Administrator Duties," in this manual. |

####### Master File Server (MFS)

The INSTITUTION (#4) and FACILITY TYPE (#4.1) files, as well as other master files, are integral components of VistA and are referenced by numerous applications. Once a master file has been standardized VHA-wide, measures *must* be taken to maintain uniformity and synchronicity. The current method of update notifications cannot keep up with today's messaging requirements. Thus, in order to maintain uniformity and synchronicity of master files VHA-wide, Kernel Patch XU\*8.0\*206 creates a Master File Server (MFS) that specifically processes the INSTITUTION and FACILITY TYPE master files. As of Kernel Patch XU\*8.0\*299, the Master File Server (MFS) mechanism was extended to support multiple standard files. Kernel Patch XU\*8.0\*299 also introduced the MASTER FILE PARAMETERS file (#4.001) and XUMF ERROR mail group.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/019.png) | REF: For more information on the MASTER FILE PARAMETERS file (#4.001), please refer to the "Files" topic in Chapter 6, "Implementation and Maintenance," in this manual. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/020.png) | NOTE: The need to standardize other master files has also been identified. Although the Standard Data Service (SDS) Team will address those files directly, the server mechanism interface implemented via the IFR software (i.e., Kernel Patch XU\*8.0\*206) was designed to support additional standard files, which will cut development time for SDS significantly. |

Once the Cleanup of the local site's INSTITUTION file (#4) has been performed and the Institution Master File data from FORUM is merged with the local INSTITUTION file (#4), further updates to the INSTITUTION file (#4) are handled automatically by the Master File Server mechanism.

|                                                                                                                |                                                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/021.png) | REF: For more information on the Cleanup of the local site's INSTITUTION file (#4), please refer to the "Institution File Cleanup Process—Initial" topic in Chapter 2,"Local Site IMF Administrator Duties," in this manual. |

The FORUM Institution Master File Administrators receives update notifications (e.g., new CBOC Station Numbers) directly from the Information Management Service via the 045A4 distribution list.

The FORUM Institution Master File Administrators add/edit the INSTITUTION file (#4) entries on FORUM (i.e., IMF). This results in the building of an HL7 message containing the updates, which are sent to all VistA sites. The message is processed automatically at the sites, updating the local INSTITUTION file with the new/updated entries from the FORUM IMF.

|                                                                                                                |                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/022.png) | REF: For more information on the duties of the FORUM Institution Master File Administrators, please refer to Chapter 3, "FORUM (Production) IMF Administrator Duties," in this manual. |

An HL7 (Messaging & Interface Services \[M&IS\]) interface specification for interaction with the Master File Server (MFS) has been defined. VistA's VA MailMan and HL7 (Messaging & Interface Services \[M&IS\]) software, utilizing bi-directional data transmission of HL7 messages over TCP/IP, provides support for communication between the FORUM (server) and VHA site (client) applications. The Master File Server (MFS) uses HL7 (Messaging & Interface Services \[M&IS\]) software to deliver updates from the master files on FORUM to the sites' local files.

The MFS and VistA's HL7 software provide the following functionality, which is described in greater detail in the topics that follow:

- Broadcast Updates—Implements a server mechanism to broadcast FORUM's Institution Master File (IMF) updates VHA-wide.
- Handle Update Message—Implements a message handler to update the local site's INSTITUTION file (#4).
- Query Server—Provides functionality to query FORUM's Institution Master File and Facility Type Master File.
- Handle Query Response—Provides functionality to handle query responses.
- Track Station Number Changes—Tracks Station Number changes in the INSTITUTION file (#4) via bulletins/e-mail messages and the VistA HL7 software.
- Application Program Interfaces (APIs)—Provides Application Program Interfaces (APIs) to set up required parameter entries and to build and send HL7 messages.

Broadcast Updates

The Master File Server (MFS) on FORUM implements a server mechanism to broadcast FORUM's Institution Master File (IMF) updates VHA-wide.

- Updates to the Institution Master File (IMF) trigger an HL7 unsolicited update event message.
- The Master File Notification (MFN) message is broadcast VHA-wide.

Handle Update Message

The HL7 (Messaging & Interface Services \[M&IS\]) software at the VistA site (client), upon receipt of an HL7 Master File message, invokes a Handler routine to do the following:

- Process the Master File Notification (MFN) message type sent by the Master File Server (MFS) on FORUM.
- Add/Update the local site's INSTITUTION file (#4) entries with the *national* entries transmitted from the FORUM master files.

Query Server

The MFS provides functionality to query FORUM's Institution Master File (IMF) and Facility Type Master File (FMF). Specifically, the Master File Server Query process:

- MFS at the site (client)—Builds Master File Query (MFQ) messages to send to FORUM (server).
- MFS on FORUM (server)—Handles Master File Query (MFQ) message types sent by the site (client).
- MFS on FORUM (server)—Sends an appropriate Master File Response (MFR) message in return back to the site (client).

Handle Query Response

The HL7 (Messaging & Interface Services \[M&IS\]) software at the VistA site (client) invokes a Handler routine to:

- Process the Master File Response (MFR) message from FORUM (server). The query definition in the HL7 QRD segment, based on parameters passed to a Master File Server interface, specifies the method of processing.
- Add/Update the INSTITUTION (#4) and FACILITY TYPE (#4.1) file entries or store the tables in a global array.

Track Station Number Changes

The INSTITUTION file (#4) Station Number changes are tracked.

- Tracking occurs via the existing functionality of the HL7 (Messaging & Interface Services \[M&IS\]) software (i.e., HL7 MESSAGE TEXT file \[#772\]).
- Kernel Patch XU\*8.0\*206 establishes the XUMF INSTITUTION mail group). This mail group receives bulletins regarding updates to the INSTITUTION file (#4). Sites are notified via a VistA MailMan bulletin when their local INSTITUTION file has been updated with *national* entries from the Institution Master File (IMF) on FORUM via the Master File Server (MFS).
- If an error occurs, a bulletin is sent to the FORUM Institution Master File Administrators.

MFS Application Program Interfaces (APIs)

Kernel Patch XU\*8.0\*206 provides APIs that set up required parameter entries and build and send HL7 messages:

- Interface to set up parameters used by the interface that builds and sends the message and the HL7 Master File Message Handler routine:

> MAIN^XUMFP(IFN,IEN,TYPE,PARAM,ERROR)

- Interface to build and send the HL7 message:

> MAIN^XUMFI(IFN,IEN,TYPE,PARAM,ERROR)

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/023.png) | REF: For more information on the APIs, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

####### Institution File Enhancements

Kernel Patch XU\*8.0\*206 incorporates modifications to the INSTITUTION file (#4) Data Dictionary and provides Application Program Interfaces (APIs).

Institution File Data Dictionary Modifications

Modifications to the INSTITUTION file (#4) Data Dictionary provide the following functionality:

- Prevents editing of *national* data in the INSTITUTION file (#4) via an Input Transform.
- Provides an Inactive Facility Flag identifier with an Effective Date.
- Requires all *national* entries in the INSTITUTION file (#4) be flagged as "National."
- Enhances the INSTITUTION file (#4) by adding a HISTORY Multiple field (#999) to record integrations (realignments), merge, deactivation, and Name updates. Creates a HISTORY Multiple field (#999) to record the following date-sensitive information:
- Integrations (Realignments)
- Name Changes/Updates
- Deactivations
- Activations

Institution File Application Program Interfaces (APIs)

Due to site integrations, Name changes, Station Number deactivations/activations, legacy Station Numbers, and new facilities, a need to return Institution time-sensitive (historical) information has been identified.

- Return historical time-sensitive information.
- Return realignment and merge pointers.

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/024.png) | REF: For more information on the APIs, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

#### Kernel Patch XU\*8.0\*217

Kernel Patch XU\*8.0\*217 modified the INSTITUTION file (#4) data dictionary to provide the following functionality:

- Added the ST. ADDR. 1 (MAILING) field (#4.01) to the INSTITUTION file (#4). It is the first line of the street address (mailing) of the facility.
- Added the ST. ADDR. 2 (MAILING) field (#4.02) to the INSTITUTION file (#4). It is the second line of the street address (mailing) of the facility.
- Added the CITY (MAILING) field (#4.03) to the INSTITUTION file (#4). It is the city (mailing) of the facility.
- Added the STATE (MAILING) field (#4.04) to the INSTITUTION file (#4). It is the state (mailing) of the facility.
- Added the ZIP (MAILING) field (#4.05) to the INSTITUTION file (#4). It is the ZIP/Postal Code (mailing) of the facility.
- Modified the STREET ADDR. 1 field (#1.01) in the INSTITUTION file (#4). It is the first line of the street address (physical) in the facility.
- Modified the STREET ADDR. 2 field (#1.02) in the INSTITUTION file (#4). It is the second line of the street address (physical) in the facility.
- Modified the CITY field (#1.03) in the INSTITUTION file (#4). It is the city (physical) of the facility.
- Modified the STATE field (#.02) in the INSTITUTION file (#4). It is the state (physical) of the facility.
- Modified the ZIP field (#1.04) in the INSTITUTION file (#4). It is the ZIP/Postal Code (physical) of the facility.

#### Kernel Patch XU\*8.0\*287

Kernel Patch XU\*8.0\*287 modified the NEW PERSON file (#200) data dictionary to provide the following functionality:

- The Input Transform of the DIVISION field (#.01) of the DIVISION Multiple field (#16) of the NEW PERSON file (#200) was modified to prevent users in the NEW PERSON file (#200) from being associated with an inactive/non-treating facility.
- Holders of the XUMGR security key can override the Input Transform and assign other facility types (other than medical) as "divisions" to a User.

#### Kernel Patch XU\*8.0\*299

Kernel Patch XU\*8.0\*299 modified or added the following components:

- Modified the Master File Server (MFS) mechanism to support multiple standard files.
- Added the MASTER FILE PARAMETERS file (#4.001) in the ^DIC(4.001, global.

|                                                                                                                |                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/025.png) | REF: For more information on the MASTER FILE PARAMETERS file (#4.001), please refer to the "Files" topic in Chapter 6, "Implementation and Maintenance," in this manual. |

- Added the XUMF ERROR mail group.

|                                                                                                                |                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/026.png) | REF: For more information on the mail groups exported with the IFR-related software, please refer to the "Mail Groups" topic Chapter 7,"Software Product Security," in this manual. |

#### Kernel Patch XU\*8.0\*335

Kernel Patch XU\*8.0\*335 establishes the following components, which are described in greater detail in the topics that follow:

- Facility Type File Data Dictionary Modifications
- Institution File Data Dictionary Modifications

Facility Type File Data Dictionary Modifications

Kernel Patch XU\*8.0\*335 added a new STATUS field (#3) to the FACILITY TYPE file (#4.1).

Institution File Data Dictionary Modifications

Kernel Patch XU\*8.0\*335 added an Input Transform to the FACILITY TYPE field (#13) in the INSTITUTION file (#4) to prevent the selection of non-standard facility types from "national" INSTITUTION file (#4) entries.

#### Kernel Patch XU\*8.0\*416

Kernel Patch XU\*8.0\*416 modified or added the following components:

- Loaded National Provider Identifier (NPI) values into the INSTITUTION file (#4) during the post install.
- Added the Load Institution NPI values option \[XUMF LOAD NPI\] to FORUM. This option is located on the Kernel Management Menu \[XUKERNEL\]. This option is to be used only in the case the NPI values fail to load in the post install or if it should become necessary to reload the NPI values (e.g., NPI values become corrupt or the data otherwise needs to be refreshed).  
    
  This option is used to edit institution data, including NPI and Taxonomy codes, selectable by coding system (e.g., NPI, Department of Defense \[DOD\], or Clinical Laboratory Improvement Amendments \[CLIA\]) and Identifier pair (for beta testing made target site, for Health Level seven \[HL7\] unsolicited update message, selectable rather than publish nationally).
- Executed an HL7 query to the Institution Master File (IMF) on FORUM using the Master File Server (MFS) mechanism. The subsequent response message automatically updated the local INSTITUTION file (#4) with the new values. In the event the post install failed, a MailMan message would be sent to notify the installer of the patch and the XUMF NPI mail group that the NPI values did not update correctly. This mail group has a remote member "REDACTED" Users can optionally add members to this mail group after installation of this patch.
- Modified the MFS Institution handler to:
- Identify a record by alternate coding system (other than station number).
- Handle NPI and Taxonomy code updates as special case (due to constraints and special processing required).
- Update coding system and ID in Identifier multiple when appropriate.
- Corrected the \$\$ADDNPI^XUSNPI API.

#### Maintaining the Local IMF—Step-By-Step Procedures

For detailed step-by-step procedures in maintaining/troubleshooting a sites' local Institution Master File (IMF), FORUM's production IMF, and Bay Pines' Test IMF, please refer to the following chapters:

- Local Site IMF Administrator Duties
- FORUM (Production) IMF Administrator Duties

## Local Site IMF Administrator Duties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

Kernel Patches XU\*8.0\*209 (i.e., original IFR patch and initial cleanup) and XU\*8.0\*335 (i.e., Health*e*Vet cleanup) require that sites assign one or more Local Site Institution Master File (IMF) Administrators to clean up, maintain, and monitor the master files located at a site. These administrators are most likely members of the site's Information Resource Management (IRM) Team.

The following duties are the responsibility of the Local Site Institution Master File Administrators of the INSTITUTION (#4) and FACILITY TYPE (#4.1) master files located at a site:

- Perform a Review/Check of the INSTITUTION File Data Prior to the Cleanup.
- Perform INSTITUTION File Cleanup (includes a background cleanup of the FACILITY TYPE file as well).
- Add/Modify Local Institution Data.
- Maintenance & Troubleshooting Master Files.

This section provides the step-by-step procedures and general information describing the day-to-day duties and maintenance requirements of the master files at a local site, as performed by the Local Site Institution Master File Administrators.

#### Institution File Data Review/Check

Sites should review/check their Institution and Institution-related data in the FORUM Institution Master File (IMF) prior to performing the cleanup at their site.

|                                                                                                                |                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/027.png) | REF: For more information on the Institution Master File Cleanup Process, please refer to the "Institution File Cleanup Process" topic that follows in this section. |

This review helps make the data in the FORUM IMF more accurate for your Parent Facility and all associated facilities. The primary goals of these data checks include the verification of the following:

- All Station Numbers associated with your Parent Facility are included.
- All data for your Parent Facility and its associated facilities are correct (e.g., Station Number, State, Type, and if appropriate, an Inactive Facility Flag with an Effective Date).
- No invalid Station Numbers are associated with your Parent Facility.
- All legacy facility data is correct (e.g., data contains an Inactive Facility Flag with an Effective Date).
- (Recommended) All Institutions of Type Veterans Affairs Medical Center (VAMC) and/or Medical and Regional Office Center (M&ROC) have unique naming conventions in order to ease data entry.

#### Kernel Patch XU\*8.0\*206—Initial Cleanup Patch

The following data fields need to be checked in the FORUM INSTITUTION file (#4). They are the primary focus of Kernel Patch XU\*8.0\*206 and should be checked for accuracy:

- NAME (#.01)—This name should be a unique name for VAMC facilities.
- STATE (#.02)—Write Identifier
- STATUS (#11)
- FACILITY TYPE (#13)—Write Identifier
- ASSOCIATIONS Multiple (#14)—The valid Association Types are:
- VISN
- Primary Facility (Parent Facility) Station Number

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/028.png)</td>
<td><strong>NOTE:</strong> Kernel Patch XU*8.0*294 prevents the adding of a VISN or PARENT FACILITY association to an Institution entry that does not have a corresponding PARENT OF ASSOCIATION.<br />
<br />
Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup) pointed all child facilities to their administrative parent. The parent, or primary facility, points to its parent (HCS or VISN). The HCS entries point to a VISN entry. All parent relationships eventually resolve to a VISN.</td>
</tr>
</tbody>
</table>

- STATION NUMBER (#99)—Write Identifier
- OFFICIAL VA NAME (#100)
- INACTIVE FACILITY FLAG (#101)—Write Identifier (used in conjunction with the EFFECTIVE DATE under the HISTORY Multiple field \[#999\])
- HISTORY Multiple (#999)
- EFFECTIVE DATE (#.01)
- REALIGNED TO (#.05)
- REALIGNED FROM (#.06)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/029.png) | NOTE: The Master File Server (MFS) uses the HL7 protocol for messaging. The above fields are currently included in the HL7 Interface Specification for the INSTITUTION file (#4). The IFR Project Team is not addressing any other fields in the HL7 Interface Specification at this time. However, the team will address any data issues related to those additional fields, if needed, at a future date. |

#### Kernel Patch XU\*8.0\*335—Health*e*Vet Cleanup Patch

The following data fields need to be checked in the local INSTITUTION file (#4). They are the primary focus of Kernel Patch XU\*8.0\*335 (i.e., Health*e*Vet cleanup) and should be checked for accuracy (listed in field number order):

- NAME (#.01)
- STATE (#.02)
- Address Information:
- ST. ADDR. 1 (MAILING) field (#4.01)
- ST. ADDR. 2 (MAILING) field (#4.02)
- CITY (MAILING) field (#4.03)
- STATE (MAILING) field (#4.04)
- ZIP (MAILING) field (#4.05)
- STREET ADDR. 1 field (#1.01)
- STREET ADDR. 2 field (#1.02)
- CITY field (#1.03)
- STATE field (#.02)
- ZIP field (#1.04)
- FACILITY TYPE (#13)
- ASSOCIATIONS Multiple (#14)—VISN association type
- PARENT OF ASSOCIATION (#1)
- AGENCY CODE (#95)
- OFFICIAL VA NAME (#100)
- INACTIVE FACILITY FLAG (#101)

#### Local Sites Step-By-Step Procedures—Institution File Data Review/Check

The following steps are recommended:

> 1. Log on to FORUM. This is the host (production) Institution Master File (IMF) server.

> 2. Select the DBA menu \[DBA\], as shown in Figure 2‑1:

> Select Software Services Primary Menu Option: dba

> List Package file by Name

> List Package file by Prefix

> Find lo-high range of filenumbers

> Package file inquire

> Package file inquire by \#

> Institution file inquire

> VISN Institution List by VISN

> PRNT Institution List by Parent

> SACC Exemptions ...

> Domain file inquire

> Integration Agreements Menu ...

> Standards and Conventions

> MOP-UP ...

> TCP Print TCP/IP Domain Data Summary

> Children of a package

> GUI Standard Guidelines

> List Manager Standards ...

> Port Assignments for TCP

> SAGG Access to Albany CIOFO

> You have PENDING ALERTS

> Enter "VA VIEW ALERTS to review alerts

> Select DBA Option:

<span id="_Ref159820236" class="anchor"></span>Figure 2‑1. DBA Menu on FORUM

> The three options that are used to assist sites in reviewing/checking their data in the FORUM IMF are:

- Institution file inquire \[DBA INSTITUTION INQUIRE\]
- VISN—Institution List by Vision \[XUMF IMF BY VISN\]
- PRNT—Institution List by Parent \[XUMF IMF BY PRNT\]

> These options are described in greater detail in the steps that follow.

> 3. Verify Facility Station Numbers and Naming Conventions

> a. From the DBA menu on FORUM, select the Institution file inquire option \[DBA INSTITUTION INQUIRE\]. This option (Figure 2‑2) displays all the facilities associated with the Institution name or Station Number entered.

> Select DBA Option: insti

> 1 Institution file inquire

> 2 Institution List by Parent

> 3 Institution List by VISN

> CHOOSE 1-31: 1 \<Enter\> Institution file inquire

> Select INSTITUTION NAME:

> <span id="_Ref159820252" class="anchor"></span>Figure 2‑2. Using the Institution file inquire option to verify facility naming conventions

> b. Enter the Primary Facility three-digit STATION NUMBER (#99) after the "Select INSTITUTION NAME:" prompt. This produces a list of all associated facilities as stored in the FORUM IMF, as shown in Figure 2‑3:

> Select INSTITUTION NAME: 442

> 1 442 CHEYENNE WY M&ROC 442

> 2 4429AA WICHITA KS VANB 4429AA

> 3 442DT SCOTTSBLUFF ANNEX NE STNB 442DT

> 4 442GA CASPER WY CBOC 442GA INACTIVE

> 5 442GB SIDNEY NE CBOC 442GB

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: \<Enter\>

> 6 442GC FT. COLLINS CO CBOC 442GC

> 7 442GD CHEYENNE WY CBOC 442GD

> CHOOSE 1-7: 1 \<Enter\> CHEYENNE WY M&ROC 442

> DEVICE: \<Enter\> UCX DEVICE Right Margin: 80// \<Enter\>

> INSTITUTION LIST AUG 30,2001 19:22 PAGE 1

> --------------------------------------------------------------------------------

> NAME: CHEYENNE STATE: WYOMING

> DISTRICT: 23 VA TYPE CODE: MC&RO

> REGION: 4 STATUS: National

> STREET ADDR. 1: VA Medical and Regional Office Center

> STREET ADDR. 2: 2360 East Pershing Boulevard

> CITY: CHEYENNE ZIP: 82001

> FACILITY TYPE: M&ROC

> ASSOCIATIONS: VISN PARENT OF ASSOCIATION: VISN 19

> ASSOCIATIONS: PARENT FACILITY PARENT OF ASSOCIATION: CHEYENNE

> STATION NUMBER: 442

> EFFECTIVE DATE: JAN 12, 2001 NAME (CHANGED FROM): CHEYENNE-VAMC

> EFFECTIVE DATE: JAN 25, 2001 NAME (CHANGED FROM): CHEYENNE-VAMC

> NAMESPACE: AAV

> NAMESPACE: AAW

> NAMESPACE: AAX

> NUMBERSPACE HIGH: 442999 NUMBERSPACE LOW: 442000

> SUPPORTING ISC: SLC VISN: 19

> Select INSTITUTION NAME:

> <span id="_Ref159820271" class="anchor"></span>Figure 2‑3. Sample list of a Primary Facility with its associated Institutions in the FORUM INSTITUTION File (#4)

|                                                                                                                |                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/030.png) | NOTE: The Primary Facility Station Number consists of only three digits and no suffix. |

> c. Verify that the list of associated facilities displayed is accurate for your Primary Facility:

- Are all of the Station Numbers associated with your Primary Facility listed? If not, notate those Station Numbers that are missing.
- Are there any Station Numbers listed that are not associated with your Primary Facility? If so, notate those Station Numbers that are incorrectly associated with your Primary Facility.

> d. Verify that the VAMC/M&ROC names displayed are unique when compared to the associated facilities. Notate any Station Numbers that are not unique.

> To speed data entry (avoid having to choose from a list), it is best if VAMC/M&ROC Institution names are unique. For example, prior to any updates to the FORUM IMF, the North Chicago facilities were named as follows:

> Select INSTITUTION NAME: north ch

> 1 NORTH CHICAGO IL D 556BU

> 2 NORTH CHICAGO IL VANB 5569AA

> 3 NORTH CHICAGO IL PRRTP 556PA

> 4 NORTH CHICAGO IL VAMC 556

> CHOOSE 1-4: ^

> Select INSTITUTION NAME:

> <span id="_Ref159820289" class="anchor"></span>Figure 2‑4. North Chicago facilities naming convention before data updated in the FORUM IMF

> In the example in Figure 2‑4, the VAMC Primary Facility name is *not* unique. It has the same name as its associated facilities (i.e., "NORTH CHICAGO").

> After reviewing the FORUM IMF data, Station Number 556's associated facilities' names were changed from "NORTH CHICAGO" to "NORTH CHGO." This made the VAMC Primary Facility name unique from the associated facilities' names, as shown in Figure 2‑5:

> Select INSTITUTION NAME: north ch

> 1 NORTH CHGO IL D 556BU

> 2 NORTH CHGO IL VANB 5569AA

> 3 NORTH CHGO IL PRRTP 556PA

> 4 NORTH CHICAGO IL VAMC 556

> CHOOSE 1-4: ^

> Select INSTITUTION NAME:

> <span id="_Ref159820300" class="anchor"></span>Figure 2‑5. North Chicago facilities naming conventions after data updated in the FORUM IMF

> The example shown in Figure 2‑6 further illustrates names in the FORUM IMF that are *not* unique and should be notated:

> Select INSTITUTION NAME: knoxville

> 1 KNOXVILLE IA VAMC 592 INACTIVE Oct 01, 1997

> 2 KNOXVILLE TN NC 855

> 3 KNOXVILLE IA VANB 5929AA

> 4 KNOXVILLE IA VAMC 555A4 INACTIVE Apr 01, 2000

> 5 KNOXVILLE IA D 555BV INACTIVE Apr 01, 2000

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: \<Enter\>

> 6 KNOXVILLE IA PRRTP 592PA

> 7 KNOXVILLE TN SOC 626BY

> 8 KNOXVILLE IA VAMC 636A7

> 9 KNOXVILLE IA D 636BV

> CHOOSE 1-9: \<Enter\>

> Select INSTITUTION NAME:

> <span id="_Ref159820316" class="anchor"></span>Figure 2‑6. Sample list of Institutions in the FORUM INSTITUTION File (#4) that are not uniquely named

> e. Verify that any VAMC/M&ROC that is the Primary Facility Health Care System (HCS) name contains the letters "HCS." If not, notate the Station Numbers. For example:

> Select INSTITUTION NAME: 663

> 1 663 PUGET SOUND HCS WA VAMC 663

> 2 6639AA SEATTLE WA VANB 6639AA

> 3 6639AF SEATTLE WA STNB 6639AF

> 4 6639AG SEATTLE WA STNB 6639AG

> 5 663A4 AMERICAN LAKE WA VAMC 663A4

> Press \<RETURN\> to see more, '^' to exit this list, OR

> CHOOSE 1-5: ^

> Select INSTITUTION NAME:

> <span id="_Toc159835402" class="anchor"></span>Figure 2‑7. Sample of a Health Care System (HCS) Naming Convention

> f. Print out a copy of the MEDICAL CENTER DIVISION file (#40.8) at your site. This printout is used to verify data in the FORUM IMF (See Step \#3g). For example, use VA FileMan to display/print the entries in File \#40.8, as shown in Figure 2‑8:

> VA FileMan 22.0

> Select OPTION: INQUIRE TO FILE ENTRIES

> OUTPUT FROM WHAT FILE: HL LOGICAL LINK// 40.8 \<Enter\> MEDICAL CENTER DIVISION

> (5 entries)

> Select MEDICAL CENTER DIVISION NAME: ??

> Choose from:

> 1 CHEYENNE VAMROC 442

> 2 CASPER 442GA

> 3 FORT COLLINS 442GC

> 4 GREELEY 442GD

> 5 SIDNEY 442GB

> Select MEDICAL CENTER DIVISION NAME:

> <span id="_Ref159820332" class="anchor"></span>Figure 2‑8. Sample list of Institutions in the MEDICAL CENTER DIVISION file (#40.8)

> g. Compare each facility name in the MEDICAL CENTER DIVISION file (#40.8):

- Verify that all the facilities in File \#40.8 are listed in the IMF. If not, notate the missing Station Numbers.

|                                                                                                                |                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/031.png) | REF: For an example of missing Station Numbers, please refer to Step \#6c. |

- Compare the names of all the facilities in File \#40.8 against the names listed in the FORUM IMF. If the names don't match and should, notate those Station Numbers where name modifications are required.  
  >   
  > For example, when you compare the entries displayed in Figure 2‑8 with the entries in Figure 2‑3, you see that Station Number 442GC's name doesn't match. It is "FORT COLLINS" in File \#40.8 and "FT. COLLINS" in the FORUM IMF, which is correct?

> 4. Verify any Legacy Site Data, if any.

> All legacy facilities that have been realigned should have a corresponding Station Number where the first three digits are the same as the legacy Primary Facility Station Number. Each of these realigned facilities *must* have a TO value unless that facility was inactivated and does not physically exist anymore. Also, any legacy facility that has been previously realigned *must* have a FROM value.

> a. From the DBA menu on FORUM, select the PRNT—Institution List by Parent option \[XUMF IMF BY PRNT\]. This option displays all the facilities associated with a particular parent facility (i.e., Primary Facility).

> b. Enter the legacy site's STATION NUMBER (#99) after the "Enter parent facility station number:" prompt, as shown in Figure 2‑9:

> Select DBA Option: prnt \<Enter\> Institution List by Parent

> Enter parent facility station number: 555

> Institution list Aug 21, 2001@13:24:03 Page: 1 of 1

> STA \# INSTITUTION NAME ST TYPE FROM TO INACTIVE DATE

> 555 CENTRAL IOWA HCS IA VAMC 636A6 Apr 01, 2000

> 555A4 KNOXVILLE IA VAMC 592 636A7 Apr 01, 2000

> 555BU DES MOINES IA D 636BU Apr 01, 2000

> 555BV KNOXVILLE IA D 636BV Apr 01, 2000

> 555DT MARSHALLTOWN IA STDM 636DW Apr 01, 2000

> 555EL MARSHALLTOWN IA STNB 636EL Apr 01, 2000

> 555GA MASON CITY IA CBOC

> 555HA MARSHALLTOWN IA ORC

> 555HB MASON CITY IL ORC

> 555HC OTTUMWA IA ORC 592HA 636GE Apr 01, 2000

> 555HD MARSHALLTOWN IA ORC 592HB 636GD Apr 01, 2000

> Enter ?? for more actions

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159820369" class="anchor"></span>Figure 2‑9. Using the PRNT—Institution List by Parent option to verify legacy site data

> c. Check the validity of the legacy data in the following fields/columns:

- ST—This is the State, is it correct for the listed facility?
- TYPE—This is the Facility Type, is it correct?

|                                                                                                                |                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/032.png) | REF: For a list of TYPEs and their acronym definitions, please refer to "Appendix B—Facility Type Acronyms" in this manual. |

- FROM— If applicable, is it correct?

|                                                                                                                |                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/033.png) | NOTE: Any legacy facility that has been previously realigned *must* have a FROM value. |

- TO—This is the new Station Number, is it correct?

|                                                                                                                |                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/034.png) | NOTE: Any legacy facility that has been realigned *must* have a TO value unless that facility was inactivated and does not physically exist. |

- INACTIVE DATE—All legacy Station Numbers should have an inactive date.

> In the example in Figure 2‑9, the user can see that Station Number 555 is a legacy facility and was realigned under Station Number 636 (i.e., 636A6). However, it appears that Station Numbers 555GA, 555HA, and 555HB do not indicate any values in the TO and INACTIVE DATE columns. If these entries have been realigned, they should have values entered in those fields. Otherwise, the missing TO Station Number indicates that those facilities no longer exist. If that is incorrect, notate that information.

> d. Verify that all the legacy facilities are listed. If not, notate the missing legacy Station Numbers.

> e. Verify that all the legacy facilities listed are valid. If not, notate the invalid legacy Station Numbers.

> 5. Verify your Primary Facility Association Data.

> a. From the DBA menu on FORUM, select the PRNT—Institution List by Parent option \[XUMF IMF BY PRNT\]. This option displays all the facilities associated with a particular parent facility (i.e., Primary Facility).

> b. Enter your Primary Facility's STATION NUMBER (#99) after the "Enter parent facility station number:" prompt, as shown in Figure 2‑10:

> Select DBA Option: prnt \<Enter\> Institution List by Parent

> Enter parent facility station number: 442

> Institution list Sep 05, 2001@12:34:53 Page: 1 of 1

> STA \# INSTITUTION NAME ST TYPE FROM TO INACTIVE DATE

> 442 CHEYENNE WY M&ROC

> 442DT SCOTTSBLUFF ANNEX NE STNB

> 442GA CASPER WY CBOC

> 442GB SIDNEY NE CBOC

> 442GC FT. COLLINS CO CBOC

> 442GD CHEYENNE WY CBOC

> Enter ?? for more actions

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159820402" class="anchor"></span>Figure 2‑10. Using the PRNT—Institution List by Parent option to verify Primary Facility data

> c. Check the validity of the data in the following fields/columns:

- ST—This is the State, is it correct for the listed facility? If not, notate the correct State (ST).
- TYPE—This is the Facility Type, is it correct? If not, notate the correct TYPE.

|                                                                                                                |                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/035.png) | REF: For a list of TYPEs and their acronym definitions, please refer to "Appendix B—Facility Type Acronyms" in this manual. |

- FROM—This is the facility realigned from–the legacy Station Number for the associated facility/type.
- TO—This field should be blank.
- INACTIVE DATE—Only/All inactive facilities *must* have an inactive date.

> d. Verify that all the associated facilities are listed. If not, notate the missing Station Numbers. For example, when you compare this list of facilities associated with Station Number 442 shown in Figure 2‑10 with the list of facilities in Figure 2‑3, you'll notice that Station Number 4429AA generated by the Institution file inquire option is missing from the list generated by the PRNT—Institution List by Parent option (Figure 2‑10). In this case, Station Number 4429AA should change its association to the Primary Facility Station Number 442 and should be notated by the site.

|                                                                                                                |                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/036.png) | NOTE: Six-character numbers (e.g., 4429AA) are Patient Treatment File (PTF) numbers assigned to Nursing Home facilities. They are an exception to the business rule that only Station Numbers approved by 045A4 (Central Office) are stored in the STATION NUMBER field (#99) in the IMF. |

> e. Verify that all the associated facilities listed are valid. If not, notate the invalid Station Numbers. For example, if a facility is listed using this option, and it shouldn't be associated with that Parent/Primary Facility, notate the Station Number.

> 6. Verify the VISN data.

> a. From the DBA menu on FORUM, select the VISN—Institution List by VISN option \[XUMF IMF BY VISN\]. This option shows all the facilities associated with a particular Veterans Integrated Service Network (VISN).

> b. Enter the VISN number after the "Select VISN:" prompt, as shown in Figure 2‑11:

> Select DBA Option: visn \<Enter\> Institution List by VISN

> Select VISN: 19

> 436 MONTANA HCS MT M&ROC

> 436GA ANACONDA CBOC MT CBOC

> 436GB GREAT FALLS CBOC MT CBOC

> 436GC MISSOULA CBOC MT CBOC

> 436GD BOZEMAN CBOC MT CBOC

> 436GF WHITEFISH CBOC MT CBOC

> 436GH BILLINGS CBOC MT CBOC 617GA

> 436GJ MILES CITY CBOC MT CBOC

> 436GK SIDNEY CBOC MT CBOC

> 442 CHEYENNE WY M&ROC

> 442GB SIDNEY NE CBOC

> 442GC FT. COLLINS CO CBOC

> 554 DENVER CO VAMC

> 554CP FT. CARSON CO RO-OC

> 554DU FLORENCE CO CIVH

> 554GB AURORA CO CBOC

> 554GC LAKEWOOD CO CBOC

> Select Action:Next Screen// \<Enter\> NEXT SCREEN

> 567 SOUTHERN COLORADO HCS CO VAMC

> 567GA PUEBLO CO CBOC

> 567GB COLORADO SPRINGS CO CBOC

> 567GC ALAMOSA CO CBOC

> 567GD LAMAR CO CBOC

> 567GE LA JUNTA CO CBOC

> 575 GRAND JUNCTION CO VAMC

> 575GA MONTROSE CO CBOC

> 617 MILES CITY MT VAMC 436A4 Oct 01, 1998

> 660 SALT LAKE CITY HCS UT VAMC

> 660GA POCATELLO ID CBOC

> 660GB OGDEN UT CBOC

> 660GD ROOSEVELT UT CBOC

> 660GG SAINT GEORGE UT CBOC

> 660GH TOOELE UT CBOC

> 660GI NEPHI UT CBOC

> 666 SHERIDAN WY VAMC

> Select Action:Next Screen// \<Enter\> NEXT SCREEN

> Institution list Aug 30, 2001@19:23:47 Page: 3 of 3

> +STA \# INSTITUTION NAME ST TYPE FROM TO INACTIVE DATE

> 666GB CASPER WY CBOC

> 666GC RIVERTON WY CBOC

> 666GD POWELL WY CBOC

> 666GE GILLETTE WY CBOC

> Enter ?? for more actions

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159820465" class="anchor"></span>Figure 2‑11. Using the VISN—Institution List by VISN option to verify VISN Data

> c. Verify that all the associated facilities are listed. If not, notate the missing Station Numbers.  

> For example, when you compare the entries displayed in Figure 2‑8 with the entries in Figure 2‑11, you see that Station Numbers 442GA and 442GD are missing from the FORUM IMF and should be notated.

> d. Verify that all the associated facilities listed are valid. If not, notate the invalid Station Numbers.

> 7. Send all noted items from Steps 1-6 to the following FORUM mail group:

> REDACTED

> The FORUM IMF Administrators process any modifications notated and may contact the sites for further clarification, if needed.

#### Institution File Cleanup Process—Initial

Over time the INSTITUTION file (#4) has evolved into a collection of file entries, which could loosely be considered institution-like, and each file varies greatly from site to site. Since the INSTITUTION file (#4) is referenced by numerous VistA applications, the cleanup process is required to achieve a level of standardization of national entries in support of data exchange initiatives while avoiding a conversion of file references from a vast array of applications. For example, many VistA applications use the INSTITUTION file (#4) STATION NUMBER field (#99) to resolve the logical link used in VistA's HL7 software. However, problems occur when two or more INSTITUTION file (#4) entries have the same STATION NUMBER value or when STATION NUMBER field values are missing from INSTITUTION files altogether.

The Institution file cleanup process does the following:

- Achieves a level of standardization and synchronization of *national* entries in support of data exchange initiatives.
- Avoids a conversion of file references from the vast array of VistA applications that currently reference the INSTITUTION file (#4).

Kernel Patch XU\*8.0\*209 provides the Institution File Query / Update option \[XUMF INSTITUTION\] that used a List Manager interface to provide utilities/actions to help the Local Site Institution Master File Administrators "clean up" the INSTITUTION (#4) and FACILITY TYPE (#4.1) files located at their sites.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/037.png) | NOTE: The Institution File Query / Update option \[XUMF INSTITUTION\] was disabled with Kernel Patch XU\*8.0\*335 to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA instance that has never done the cleanup and needs to load the full Institution table. |

These utilities should be run at the initial implementation of Kernel Patch XU\*8.0\*209 as well as whenever the Local Site Institution Master File Administrators and/or IRM personnel deem it necessary.

Specifically, the cleanup process provides:

- Capability to compare Institution data in the site's (local) INSTITUTION file (#4) vs. FORUM's (national) Institution Master File (IMF, "Gold" file) through several list options.
- Functionality to resolve duplicate STATION NUMBER field values.
- Functionality to automatically merge FORUM's Institution Master File (IMF) *national* data with the local site's INSTITUTION file (#4).
- Functionality to automatically merge FORUM's Facility Type Master File (FMF) *national* data with the local site's FACILITY TYPE file (#4.1).

|                                                                                                                |                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/038.png) | NOTE: This is a background job; no user interface is required. |

The Cleanup utilities utilize the query functionality provided by the Master File Server (MFS) mechanism to query the FORUM IMF *national* data. The data is returned to the local site that stores the IMF data in a temporary global. The Cleanup utilities use this stored information to compare and display the *national* data entries in the Institution Master File (IMF) on FORUM with *local* data entries in the INSTITUTION file (#4) at the site. The comparison process matches on STATION NUMBER (#99, duplicates *not* allowed) rather than on NAME (#.01, duplicates allowed). The cleanup process uses List Manager to display a side-by-side comparison list, sorted by STATION NUMBER.

The cleanup process requires that sites resolve duplicate STATION NUMBER field (#99) values before merging *national* data from the Institution Master File (IMF) located on FORUM with the data found in a local site's INSTITUTION file (#4), such as deleting the duplicate STATION NUMBER field value from the site's INSTITUTION file (#4). However, the INSTITUTION file entry of the duplicate is *not* deleted.

#### Institution File Query / Update \[XUMF INSTITUTION\]

The Institution File Query / Update option \[XUMF INSTITUTION\] provides the following List Manager actions:

- LLCL—List local station numbers.
- NATL—List national data to merge.
- DSTA—Delete local/dup. station \#.
- RDSN—Resolve duplicate station numbers.
- AUTO—Auto update with national data.
- CHCK—Required clean up actions.

|                                                                                                                |                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/039.png) | REF: These List Manager actions are described in greater detail in the topics that follow. |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/040.png) | NOTE: The Institution File Query / Update option \[XUMF INSTITUTION\] was disabled with Kernel Patch XU\*8.0\*335 to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA instance that has never done the cleanup and needs to load the full Institution table. |

The software, through this option, automatically connects with the Master File Server (MFS) and obtains the Institution Master File (IMF) and Facility Type Master File (FMF) data on FORUM and stores them in a temporary global on the local system. This process can take approximately five minutes. It then displays the INSTITUTION file (#4) data in a List Manager screen for comparison purposes. If the software fails to connect to the Master File Server (MFS), an error message is displayed.

#### List local station numbers

The List local station numbers (LLCL) List Manager action checks for and displays any STATION NUMBER field values that are in the site's local INSTITUTION file (#4) but *not* in the FORUM IMF; these are *local* entries.

Specifically, this action does the following:

- Checks for local INSTITUTION file (#4) entries that are *not* in the FORUM IMF.

|                                                                                                                |                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/041.png) | NOTE: The cleanup process eventually deletes these STATION NUMBER field values. |

- Displays an informational list of local INSTITUTION file (#4) entries that are *not* in the FORUM IMF. The following INSTITUTION file (#4) data is displayed:
- Station Number
- Institution Name
- Internal Entry Number (IEN)
- Facility Type

|                                                                                                                |                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/042.png) | NOTE: Sites may wish to print this list before running the Auto update with national data (AUTO) List Manager action to see which Station Number entries will be deleted from the local site's INSTITUTION file (#4). |

|                                                                                                                |                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/043.png) | NOTE: All local Station Numbers *must* be deleted using the Delete local/dup. station \# (DSTA) and/or Resolve duplicate station numbers (RDSN) List Manager actions before the Auto update with national data (AUTO) List Manager action allows the site to auto update its INSTITUTION file (#4) with the IMF data. |

#### List national data to merge

The List national data to merge List Manager action checks for and displays any *national* STATION NUMBER field values that are in the FORUM IMF that will be added to the site's local INSTITUTION file (#4). Users should notate and/or print this list because the STATION NUMBER field values indicated will be added to the site's local INSTITUTION file (#4) when the Auto update with national data List Manager action is run.

Specifically, this action does the following:

- Checks for FORUM *national* IMF entries that are *not* in the local site's INSTITUTION file (#4).

|                                                                                                                |                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/044.png) | NOTE: The cleanup process merges these FORUM IMF entries with the local site's INSTITUTION file (#4). |

- Displays an informational list of the FORUM *national* IMF entries that are *not* in the local site's INSTITUTION file. The following INSTITUTION file (#4) information is displayed (see Figure 2‑16):
- Station Number
- Institution Name
- State
- Facility Type

|                                                                                                                |                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/045.png) | NOTE: Sites may wish to print this list before running the Auto update with national data (AUTO) List Manager action to see which entries will be merged with the local site's INSTITUTION file (#4). |

#### Delete local/dup. station \#

The Delete local/dup. station# List Manager action deletes local and certain duplicate STATION NUMBER field values from the site's local INSTITUTION file (#4). All duplicate STATION NUMBER field values *must* be resolved before the Auto update with national data List Manager action allows the site to automatically update its local INSTITUTION file (#4) with the *national* FORUM IMF entries.

Specifically, this action does the following:

- Deletes all *local* STATION NUMBER field values from the local site's INSTITUTION file (#4) that are *not* found in the FORUM IMF. However, it does *not* delete entire entries from the local file.

|                                                                                                                |                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/046.png) | NOTE: To get a list of local Station Numbers to be deleted prior to actually deleting them, use the List local station numbers (LLCL) List Manager action prior to running this action (see the "List national data to merge" topic shown previously). |

- Displays those entries for which the local STATION NUMBER field (#99) value was deleted in the Action Area of the List Manager screen to denote processing (i.e., located in the bottom area of the List Manager screen where the action menu is displayed). The following INSTITUTION file (#4) information is displayed:
- Station Number
- Internal Entry Number (IEN)
- Deletes duplicate STATION NUMBER field values that can be automatically resolved. However, it does *not* delete entire entries from the local file. For each set of duplicates, the action checks to see if just *one* entry in the set is pointed to by the HL7 LOGICAL LINK file (#870); if so, that entry is kept and the values of the STATION NUMBER field (#99) of the other duplicate entries are deleted.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/047.png) | NOTE: To resolve those duplicate entries that are *not* automatically deleted, use the Resolve duplicate station numbers List Manager action (RDSN, description follows). |

- Displays those entries for which the duplicate STATION NUMBER field (#99) values were automatically resolved and deleted in the Action Area of the List Manager screen to denote processing (i.e., located in the bottom area of the List Manager screen where the action menu is displayed). The following INSTITUTION file (#4) information is displayed (see Figure 2‑19):
- Station Number
- Internal Entry Number (IEN)
- Displays any duplicate sets of STATION NUMBER field values in the local INSTITUTION file (#4) that require manual review and resolution (i.e., the set of duplicates having no pointer from File \#870). The following INSTITUTION file (#4) information is displayed:
- Line Number
- Station Number
- Institution Name
- Internal Entry Number (IEN)

|                                                                                                                |                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/048.png) | NOTE: After reviewing these duplicates and deciding which ones to delete, use the Resolve duplicate station numbers (RDSN) List Manager action to remove the duplicates from the local site's INSTITUTION file (#4). |

- Provides an additional List Manager action, Resolve duplicate station numbers (RDSN), to resolve the duplicates that require manual intervention.
- Creates a new cross-reference ^DIC(4,"AOLD99",IEN,station_number) for all deleted STATION NUMBER field (#99) values.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/049.png) | NOTE: All local and duplicate Station Numbers *must* be deleted using the Delete local/dup. station \# (DSTA) and/or Resolve duplicate station numbers (RDSN) List Manager actions before the Auto update with national data (AUTO) List Manager action allows the site to automatically update its local INSTITUTION file (#4) with the FORUM IMF data. |

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/050.png)</td>
<td>CAUTION: If the site's own STATION NUMBER (#99) is a duplicate, then extreme caution must be exercised when selecting the STATION NUMBER entry to delete, since the INSTITUTION file (#4) is referenced by other standard files, such as the HL LOGICAL LINK (#870), MEDICAL CENTER DIVISION (#40.8), and STATION NUMBER (TIME SENSITIVE) (#389.9) files. These file entries should be checked <em>before</em> and <em>after</em> performing the cleanup process to verify that they point to a valid INSTITUTION file entry, complete with STATION NUMBER.<br />
<br />
Also, please note that other VistA applications (including Automated Medical Information Exchange [AMIE], Record Tracking, and MPI/PD) may be negatively affected, if their pointers to an INSTITUTION file entry do not have valid STATION NUMBERs.</td>
</tr>
</tbody>
</table>

#### Resolve duplicate station numbers

The Resolve duplicate station numbers List Manager action allows users to select the duplicate STATION NUMBER field value to delete from the site's local INSTITUTION file (#4). All duplicate STATION NUMBER field values *must* be resolved before the Auto update with national data List Manager action allows the site to automatically update its local INSTITUTION file (#4) with the *national* FORUM IMF entries.

Specifically, this action does the following:

- Allows selection from a list of duplicates.
- Deletes the STATION NUMBER field (#99) value of the selected duplicate; however, it does *not* delete the entire file entry for the selected duplicate.

The Resolve duplicate station numbers (RDSN) List Manager action is available only *after* running the Delete local/dup. station \# (DSTA) List Manager action (see Delete local/dup. station \# shown previously). Users *must* continuously select this action until *all* unresolved duplicates have been reviewed and deleted from the local site's INSTITUTION file (#4). Users *must* resolve all duplicates *before* running the Auto update with national data (AUTO) List Manager action.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/051.png)</td>
<td>CAUTION: If the site's own STATION NUMBER (#99) is a duplicate, then extreme caution must be exercised when selecting the STATION NUMBER entry to delete, since the INSTITUTION file (#4) is referenced by other standard files, such as the HL LOGICAL LINK (#870), MEDICAL CENTER DIVISION (#40.8), and STATION NUMBER (TIME SENSITIVE) (#389.9) files. These file entries should be checked <em>before</em> and <em>after</em> performing the cleanup process to verify that they point to a valid INSTITUTION file entry, complete with STATION NUMBER.<br />
<br />
Also, please note that other VistA applications (including Automated Medical Information Exchange [AMIE], Record Tracking, and MPI/PD) may be negatively affected, if their pointers to an INSTITUTION file entry don't have a valid STATION NUMBER.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/052.png) | NOTE: All duplicate Station Numbers *must* be deleted using the Delete local/dup. station \# (DSTA) and/or Resolve duplicate station numbers (RDSN) List Manager actions before the Auto update with national data (AUTO) List Manager action allows the site to automatically update their INSTITUTION file (#4) with the FORUM IMF data. |

If a problem in a specific software application should arise, that issue may have to be dealt with on a case-by-case basis. Kernel Patch XU\*8.0\*209 implements the \$\$O99^XUAF4(IEN) API and "O99" cross-reference, which can be used to resolve (re-point) any software-specific issues.

|                                                                                                                |                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/053.png) | REF: For more information on the \$\$O99^XUAF4(IEN) API, please refer to the "\$\$O99^XUAF4(): IEN of Merged Station Number" topic in Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

#### Auto update with national data

The Auto update with national data List Manager action merges the FORUM IMF *national* entries into the site's local INSTITUTION file (#4).

Specifically, this action does the following:

- Checks for local and duplicate STATION NUMBER field values:
- Local or Duplicate Entries Exist—Notifies the user and suspends the update until the duplicates are resolved.
- No Local or Duplicate Entries Exist—Updates the local site's INSTITUTION file (#4) data with FORUM *national* data.
- Flags the STATUS field (#11) based on the appropriate record type:
- *National* Entries—Sets the STATUS field (#11) to "National" in the local site's INSTITUTION file.
- *Local* Entries—Sets the STATUS field (#11) to "Local" in the local site's INSTITUTION file (#4).

Specifically, the Auto Update process does the following:

> A. Cleans out any data stored in the STATION NAME field (#7).

> B. Sets the INACTIVE FACILITY FLAG field (#101) and deletes the STATUS field (#11) value for any entry with a STATUS field (#11) of INACTIVE.

> C. Merges the FORUM IMF data with the local site's INSTITUTION file (#4).

> 1. Sets the STATUS field (#11) flag to "National" for *national* entries and to "Local" for *local* entries.

> 2. Populates the following INSTITUTION file (#4) fields (listed in field number order):

- NAME (#.01)
- STATE (#.02)
- FACILITY TYPE (#13)
- STATION NUMBER (#99)
- OFFICIAL VA NAME (#100)

> D. Sets the INACTIVE FACILITY FLAG (#101) for inactive facilities and deactivated Station Numbers.

> E. Sets a pointer to/from the new/old INSTITUTION file (#4) entry together with the effective date for Integrated/realigned facilities; these values are stored in the following HISTORY Multiple field (#999) fields (listed in field number order):

- EFFECTIVE DATE (#.01).
- REALIGNED TO (#.05).
- REALIGNED FROM (#.06).

> The Auto update with national data (AUTO) List Manager action takes approximately 5-10 minutes to run and the terminal will "hang" until complete. When this action is completed, the cleanup of the local site's INSTITUTION file (#4) is done. However, users should run the Required clean up actions (CHCK) List Manager action to verify that there are no further duplicates and that all IMF data merged correctly.

#### Required clean up actions (CHCK)

The Required clean up actions (CHCK) List Manager action verifies that all required cleanup actions have been taken prior to initiating the Auto update with national data (AUTO) List Manager action.

#### Local Sites Step-by-Step Procedures—Initial Institution File Cleanup Process

The following is the *suggested* order of the step-by-step procedures to initially clean up the local site's INSTITUTION file (required steps are notated):

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/054.png)</td>
<td>CAUTION: Prior to performing the Cleanup, users <em>must</em> review/check the data in the FORUM IMF file.<br />
<br />
For more information on reviewing/checking data, please refer to the "Institution File Data Review/Check" topic in this chapter.</td>
</tr>
</tbody>
</table>

> 1. (Required) Log on to the system.

> 2. (Required) Choose the Institution File Query / Update option \[XUMF INSTITUTION\], as shown in Figure 2‑12:

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/055.png) | NOTE: The Institution File Query / Update option \[XUMF INSTITUTION\] was disabled with Kernel Patch XU\*8.0\*335 to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA instance that has never done the cleanup and needs to load the full Institution table. |

> Select OPTION NAME: XUMF

> 1 XUMF FORUM INSTITUTION Institution Master File edit

> 2 XUMF INSTITUTION Institution File Query / Update

> CHOOSE 1-2: 2\<Enter\> XUMF INSTITUTION Institution File Query / Update

> Institution File Query / Update

> ...connecting with master file server...

> ...please wait...(approx. 5 minutes)...

> ...getting FACILITY TYPE file...

> ...getting INSTITUTION file...................

> <span id="_Ref159820577" class="anchor"></span>Figure 2‑12. Initial dialogue when using the Institution File Query / Update option \[XUMF INSTITUTION\]

> As the example in Figure 2‑12 shows, to initiate the cleanup process the user chose the XUMF INSTITUTION option (i.e., Institution File Query / Update) by entering "2" at the "CHOOSE 1-2:" prompt.

> The software automatically connected to the Master File Server (MFS) in order to obtain both the FACILITY TYPE (#4.1) and INSTITUTION (#4) master files on FORUM. The following messages were displayed notifying the user that this process was taking place and that it could take several minutes to complete:

> ...connecting with master file server...

> ...please wait...(approx. 5 minutes)...

> When both master files on FORUM were obtained and stored in a temporary global on the local system, the following was displayed:

> ...getting FACILITY TYPE file...

> ...getting INSTITUTION file...................

> At this point the user was ready to proceed to the next step in the cleanup process (see Step \#3).

> 3. (Optional) Visually compare the local site's INSTITUTION file (#4) data in the List Manager column headed "INSTITUTION NAME" with FORUM's national Institution Master File (IMF) data in the List Manager column headed "GOLD NAME," as shown in Figure 2‑13:

> INSTITUTION name vs GOLD name Jan 29, 2001 15:48:20 Page: 1 of 129

> STA \# INSTITUTION NAME GOLD NAME

> 16 ISC SAN FRANCISCO

> 101 CENTRAL OFFICE CENTRAL OFFICE

> 102 TOPEKA

> 103 WASHINGTON

> 104 AUSTIN FINANCE CENTER

> 105 VBA MORTGAGE LOAN

> 123 WASHINGTON

> 200 AUSTIN DPC AUSTIN

> 201 HINES

> 202 LOS ANGELES

> 203 PHILADELPHIA

> 204 ST. PAUL

> 205 WASHINGTON

> 209 WASHINGTON

> 207 WASHINGTON

> \+ Enter ?? for more actions

> LLCL List local station numbers AUTO Auto update with national data

> DSTA Delete local/dup. station \# CHCK Required clean up actions

> NATL List national data to merge

> Select Action:Next Screen//

> <span id="_Ref159820608" class="anchor"></span>Figure 2‑13. Sample INSTITUTION file data at a site compared with data on FORUM

> This main screen (Figure 2‑13) displays a side-by-side view of the current INSTITUTION file (#4) entries at the site (middle column) along with the corresponding IMF entries on FORUM (right column), sorted by Station Number (left column). As you can see, some items are missing an Institution Name or an IMF Name and some items' Names are not the same.

> For example, see Station Number 102 in Figure 2‑13. As you can see, there is no Name displayed under the "INSTITUTION NAME" column, however, "TOPEKA" is displayed under the "GOLD NAME" column in the display.

> Missing or different Name entries may be due to one of the following:

- Name listed in the "INSTITUTION NAME" column, but missing in the "GOLD NAME" column—These are the site's INSTITUTION file (#4) Station Number entries that are missing in the IMF (i.e., "Gold"). For example, see Station Number 16 in Figure 2‑13. The cleanup process deletes these Station Number field entries from the local site's INSTITUTION file (#4).

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/056.png) | NOTE: To get a specific list of these entries, use the List local station numbers (LLCL) List Manager action (see Step \#4). |

- Name listed in the "GOLD NAME" column, but missing in the "INSTITUTION NAME" column—These are the IMF Station Number (i.e., "Gold") entries that are missing in the site's INSTITUTION file (#4). For example, see Station Number 103 in Figure 2‑13. The cleanup process adds these FORUM IMF Station Number entries to the local site's INSTITUTION file (#4).

|                                                                                                                |                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/057.png) | NOTE: To get a specific list of these entries, use the List national data to merge (NATL) List Manager action (see Step \#5). |

- Name found in both the "GOLD NAME" and "INSTITUTION NAME" columns, but different—In this case the FORUM IMF entry Name is assumed correct and is used to update the local site's INSTITUTION file (#4) when the Cleanup Process Auto update with national data (AUTO) List Manager action is run (see Step \#8). For example, see Station Number 200 in Figure 2‑13.

> The purpose of this list is to compare the local site's INSTITUTION file (#4) vs. the FORUM IMF. If duplicate Station Numbers exist in the local file, they are *not* displayed twice in the list. However, the Delete local/dup. station \# (DSTA) List Manager action lists all duplicates deleted or requiring manual review for resolution (see Step \#6). The Resolve duplicate station numbers (RDSN) List Manager action is used to review/resolve these duplicates (see Step \#7).

> 4. (Optional but recommended) Choose the List local station numbers (LLCL) List Manager action to visually notate those STATION NUMBER field (#99) values in the local site's INSTITUTION file (#4) that will be deleted when the Delete local/dup. station \# (DSTA) List Manager action is run (see Step \#6).

> If users select the List local station numbers (LLCL) List Manager action *before* running either the Delete local/dup. station \# (DSTA) or Auto update with national data (AUTO) List Manager actions and users have Station Numbers unique to their site, they might be presented with a list (List Manager screen) similar to the following:

> Select Action:Next Screen// LLCL \<Enter\> List local station numbers

> <u>List local station numbers Jan 29, 2001 15:48:44 Page: 1 of 2</u>

> <u>STA \# INSTITUTION NAME IEN FACILITY TYPE</u>

> 16 ISC SAN FRANCISCO 16

> 998 SFVDC.VA 998

> 999 SFVDC-B.VA 999

> 1000 REGION 1 1000

> 2000 REGION 2 2000

> 3000 REGION 3 3000

> 4000 REGION 4 4000

> 5000 REGION 5 5000

> 6000 REGION 6 6000

> 14610 HINESCIRNTEST 6030

> 15000 ISC SALT LAKE CITY 6018

> 18610 BPMARION 6028

> 18655 BPSAGINAW 6029

> 16000AO ISC SF OTHER DIVISION 6022 VAMC

> 516ZZ Bay Pines 6032 MC(M)

> 662B3 ISC SOC 6020 VAMC

> 677HM EMPORIA KS 6481

> \+ Enter ?? for more actions

> Select Action:Next Screen// \<Enter\> NEXT SCREEN

> <u>List local station numbers Jan 29, 2001 15:48:44 Page: 2 of 2</u>

> <u>+STA \# INSTITUTION NAME IEN FACILITY TYPE</u>

> 677HO ABILENE KS 6482

> Enter ?? for more actions

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159820689" class="anchor"></span>Figure 2‑14. Using the List local station numbers (LLCL) action

> In the example in Figure 2‑14, the user wanted to list the local entries that would be deleted during the cleanup process. Thus, the user entered "LLCL" (List local station numbers) at the "Select Action:Next Screen//" prompt.

> As you can see, ListMan displayed 18 local Station Numbers unique to this site that were *not* found in the FORUM IMF. To see the complete list, the user had to press the \<Enter\> key at the "Select Action:Next Screen//" prompt. After viewing the entire list, the user pressed the \<Enter\> key at the "Select Action:Quit//" prompt to accept the "Quit" Default.

> Cleanup of the local site's INSTITUTION file requires that all of these local STATION NUMBER field (#99) values be deleted from the file. The entries are deleted using the Delete local/dup. station \# (DSTA) List Manager action (see Step \#6).

> If users select the List local station numbers (LLCL) List Manager action again *after* running the Auto update with national data (AUTO) List Manager action or there are no unique local Station Numbers, users are presented with the following List Manager screen:

> Select Action:Next Screen// LLCL \<Enter\> List local station numbers

> <u>List local station numbers Jan 30, 2001 15:22:23 Page: 1 of 1</u>

> <u>STA \# INSTITUTION NAME IEN FACILITY TYPE</u>

> \*\*\*None found\*\*\*

> Enter ?? for more actions

> Select Action:Quit//

> <span id="_Ref159820705" class="anchor"></span>Figure 2‑15. Using the List local station numbers (LLCL) action after running the AUTO action

> In the example in Figure 2‑15, the local site's INSTITUTION file (#4) has already been updated (i.e., all local Station Numbers have been deleted); thus, there won't be any local Station Number entries to display when the user runs the List local station numbers (LLCL) List Manager action again.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/058.png) | NOTE: Generally, users also will not find any local Station Numbers after running the Delete local/dup. station \# (DSTA) List Manager action. However, there may still be some unresolved duplicate local Station Numbers that will continue to be displayed until they are reviewed by the user and resolved using the Resolve duplicate station numbers (RDSN) List Manager action (see Step \#7). |

> 5. (Optional) Choose the List national data to merge (NATL) List Manager action to visually notate those entries that will be merged with the local site's INSTITUTION file (#4) when the Auto update with national data List Manager action is run (see Step \#8).

> If users select the List national data to merge (NATL) List Manager action, they are presented with a list (List Manager screen) similar to the following:

> Select Action:Next Screen// NATL\<Enter\> List national data to merge

> <u>List national data to merge Jan 29, 2001 15:48:54 Page: 1 of 79</u>

> <u>STA \# INSTITUTION NAME STATE FACILITY TYPE</u>

> 102 TOPEKA KANSAS DPC

> 103 WASHINGTON DISTRICT OF COL CO

> 104 AUSTIN FINANCE CENTER TEXAS CO

> 105 VBA MORTGAGE LOAN VBAML

> 123 WASHINGTON DISTRICT OF COL CO

> 201 HINES ILLINOIS DPC

> 202 LOS ANGELES CALIFORNIA DPC

> 203 PHILADELPHIA PENNSYLVANIA DPC

> 204 ST. PAUL MINNESOTA DPC

> 205 WASHINGTON DISTRICT OF COL DPC

> 209 WASHINGTON DISTRICT OF COL DPC

> 207 WASHINGTON DISTRICT OF COL DPC

> 281 AUSTIN TEXAS SDC

> 282 HINES ILLINOIS BDC

> 283 HINES ILLINOIS SDC

> 284 PHILADELPHIA PENNSYLVANIA BDC

> \+ Enter ?? for more actions

> Select Action:Next Screen// \<Enter\> NEXT SCREEN

> <u>List national data to merge Jan 29, 2001 15:48:56 Page: 2 of 79</u>

> <u>+ STA \# INSTITUTION NAME STATE FACILITY TYPE</u>

> 285 PHILADELPHIA PENNSYLVANIA SDC

> 355 SAN JUAN PUERTO RICO RO

> 359 HONOLULU HAWAII VBA

> ....

> ....

> ....

> \+ Enter ?? for more actions

> Select Action:Next Screen// ^

<span id="_Ref159820503" class="anchor"></span>Figure 2‑16. Using the List national data to merge (NATL) action

> In the example in Figure 2‑16, the user wanted to see the FORUM IMF entries that would be merged with the local site's INSTITUTION file. Thus, the user entered "NATL" (List national data to merge) at the "Select Action:Next Screen//" prompt.

> The software automatically displays all of the FORUM IMF entries. In the example illustrated by Figure 2‑16, 79 pages of data were displayed. (For the sake of brevity, we have only shown a page and half of data.) To see all of the entries on the subsequent pages, the user would need to press the \<Enter\> key at the "Select Action:Next Screen//" prompt until the last page (screen) of the list was reached.

> If users select the List national data to merge (NATL) List Manager action again *after* running the Auto update with national data (AUTO) List Manager action, they are presented with the following List Manager screen:

> List national data to merge Feb 01, 2001 08:51:36 Page: 1 of 1

> STA \# INSTITUTION NAME STATE FACILITY TYPE

> \*\*\*None found\*\*\*

> Enter ?? for more actions

> Select Action:Quit//

> <span id="_Ref159820750" class="anchor"></span>Figure 2‑17. Using the List national data to merge (NATL) action after running the AUTO action

> In the example in Figure 2‑17, the local site's INSTITUTION file (#4) has already been updated (i.e., all FORUM IMF data has been merged into the local site's INSTITUTION file). Thus, there will not be any FORUM IMF entries to display when users again run the List national data to merge (NATL) List Manager action.

> 6. (Required) Choose the Delete local/dup. station \# (DSTA) List Manager action when you wish to delete duplicate and *local* STATION NUMBER field values from the local site's INSTITUTION file (#4), as shown in Figure 2‑18:

> INSTITUTION name vs GOLD name Jan 29, 2001 15:48:58 Page: 1 of 129

> STA \# INSTITUTION NAME GOLD NAME

> 16 ISC SAN FRANCISCO

> 101 CENTRAL OFFICE CENTRAL OFFICE

> 102 TOPEKA

> 103 WASHINGTON

> 104 AUSTIN FINANCE CENTER

> 105 VBA MORTGAGE LOAN

> 123 WASHINGTON

> 200 AUSTIN DPC AUSTIN

> 201 HINES

> 202 LOS ANGELES

> 203 PHILADELPHIA

> 204 ST. PAUL

> 205 WASHINGTON

> 209 WASHINGTON

> 207 WASHINGTON

> \+ Enter ?? for more actions

> LLCL List local station numbers AUTO Auto update with national data

> DSTA Delete local/dup. station \# CHCK Required clean up actions

> NATL List national data to merge

> Select Action:Next Screen// DSTA \<Enter\> Delete local/dup. station \#

> This action will auto-delete local/duplicate station numbers.

> Do you wish to proceed? YES// \<Enter\>

> <span id="_Ref159820765" class="anchor"></span>Figure 2‑18. Using the Delete local/dup. station \# (DSTA) action

> After reviewing the local entries (see Step \#4 and Figure 2‑14), the user decided to delete the local and duplicate Station Numbers from the local site's INSTITUTION file (#4) by entering "DSTA" (Delete local/dup. station \#) at the "Select Action:Next Screen//" prompt.

> The software immediately warned the user that "This action will auto-delete local/duplicate station numbers." The user pressed the \<Enter\> key to accept the default of "YES" at the "Do you wish to proceed? YES//" prompt.

> As shown in Figure 2‑19, the software began displaying the entries that were being deleted in the "Action Area" of the List Manager display (i.e., you can also see this area at the bottom area of the List Manager screen where the action menu is displayed in Figure 2‑13:

> deleting local station number 16 from IEN: 16

> deleting local station number 998 from IEN: 998

> deleting local station number 999 from IEN: 999

> deleting local station number 1000 from IEN: 1000

> deleting local station number 2000 from IEN: 2000

> deleting local station number 3000 from IEN: 3000

> deleting local station number 4000 from IEN: 4000

> deleting local station number 5000 from IEN: 5000

> deleting local station number 6000 from IEN: 6000

> deleting local station number 14610 from IEN: 6030

> deleting local station number 15000 from IEN: 6018

> deleting local station number 18610 from IEN: 6028

> deleting local station number 18655 from IEN: 6029

> deleting local station number 16000AO from IEN: 6022

> deleting local station number 516ZZ from IEN: 6032

> deleting local station number 516ZZ from IEN: 6033

> deleting local station number 662B3 from IEN: 6020

> deleting local station number 677HM from IEN: 6481

> deleting local station number 677HO from IEN: 6482

> Enter RETURN to continue or '^' to exit: \<Enter\>

> .......

> <span id="_Ref159820558" class="anchor"></span>Figure 2‑19. Using the Delete local/dup. station \# (DSTA) action—Deleting local and duplicate entries

> Figure 2‑19 displays those entries for which the local and duplicate STATION NUMBER field (#99) values were automatically resolved and deleted (i.e., the set where only *one* of the duplicate entries had a valid pointer from File \#870). This list is displayed in the Action Area of the List Manager screen. As you can see, for example, the duplicate Station Number 516ZZ was automatically resolved and deleted along with the other local entries in the local site's INSTITUTION file (#4).

> The software, however, was unable to resolve *all* of the duplicates in the local site's INSTITUTION file (#4). The duplicate sets of STATION NUMBER field (#99) values in the local INSTITUTION file (#4) that required review and resolution (i.e., the set having no pointer from File \#870) are shown in Figure 2‑20:

> Duplicate station numbers Jan 30, 2001 14:48:39 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> 1 519HB FT STOCKTON 6164

> 2 519HB FT. STOCKTON 6538

> 3 519HB FORT STOCKTON 6539

> 4 688GA ALEXANDRIA VA 6491

> 5 688GA Alexandria 6540

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit//

> <span id="_Ref159820904" class="anchor"></span>Figure 2‑20. Using the Delete local/dup. station \# (DSTA) action—Unresolved duplicates

> Since there are unresolved duplicate sets of entries in the INSTITUTION file (Figure 2‑20), the software presents the Resolve duplicate station numbers (RDSN) List Manager action to be used after the user reviews the duplicates and determines which ones should be deleted.

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/059.png) | REF: For more information on the Resolve duplicate station numbers (RDSN) List Manager action, please refer to Step \#7. |

> If users select the Delete local/dup. station \# (DSTA) List Manager action again *after* running the Delete local/dup. station \# (DSTA) and Resolve duplicate station numbers (RDSN) List Manager actions (when all duplicates have been resolved) or the Auto update with national data (AUTO) List Manager action, they are presented with the List Manager screen in Figure 2‑21:

> Duplicate station numbers Jan 29, 2001 15:50 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> \*\*\*No duplicates\*\*\*

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159820948" class="anchor"></span>Figure 2‑21. Using the Delete local/dup. station \# (DSTA) action—No unresolved duplicates

> In the example in Figure 2‑21, the local site's INSTITUTION file (#4) had already been updated to remove local and duplicate entries. Thus, there were no duplicate entries to display when users ran the Delete local/dup. station \# (DSTA) List Manager action.

> 7. (Required if duplicates still exist after Step \#6) Choose the Resolve duplicate station numbers (RDSN) List Manager action when user review is required to resolve duplicates in the local site's INSTITUTION file (see Step \#6).

> The use of the Resolve duplicate station numbers (RDSN) List Manager action is illustrated in Figure 2‑22 through Figure 2‑24:

> Duplicate station numbers Jan 30, 2001 15:03:38 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> 1 519HB FT STOCKTON 6164

> 2 519HB FT. STOCKTON 6538

> 3 519HB FORT STOCKTON 6539

> 4 688GA ALEXANDRIA VA 6491

> 5 688GA Alexandria 6540

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit// rdsn \<Enter\> Resolve duplicate station numbers

> Select Duplicate Station \#: (1-5): 2

> This action will auto-delete local/duplicate station numbers.

> Do you wish to proceed? YES// \<Enter\> ......

> Duplicate station numbers Jan 30, 2001 15:05:09 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> 1 519HB FT STOCKTON 6164

> 2 519HB FORT STOCKTON 6539

> 3 688GA ALEXANDRIA VA 6491

> 4 688GA Alexandria 6540

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit//

> <span id="_Ref159821353" class="anchor"></span>Figure 2‑22. Using the Resolve duplicate station numbers (RDSN) action—Resolving duplicates (1)

> In the example in Figure 2‑22, after running the Delete local/dup. station \# (DSTA) List Manager action (see Figure 2‑20), there were two duplicate sets of Station Numbers that couldn't be resolved automatically.

> The user reviewed the list of unresolved duplicates to determine which of the duplicates should be deleted from the local site's INSTITUTION file (#4). One set of duplicates had three duplicate Station Numbers (519HB) and another set had two duplicate Station Numbers (688GA).

> For this example, the user decided that the following Station Numbers (from the first list displayed in Figure 2‑22) needed to be deleted:

|             |                |                      |         |
|-------------|----------------|----------------------|---------|
| Line \# | Station \# | Institution Name | IEN |
| 2           | 519HB          | FT. STOCKTON         | 6538    |
| 3           | 519HB          | FORT STOCKTON        | 6539    |
| 5           | 688GA          | Alexandria           | 6540    |

> To remove these selected Station Number field values, the user ran the Resolve duplicate station numbers List Manager action by entering "RDSN" at the "Select Action:Quit//" prompt (see Figure 2‑22).

> To delete the first duplicate record in the first set of STATION NUMBER 519HB duplicates (i.e., Line \#2), the user entered a "2" at the "Select Duplicate Station \#: (1-5):" prompt. The RDSN action displayed the following message:

> "This action will auto-delete local/duplicate station numbers."

> The user pressed the \<Enter\> key to accept the default of "YES" at the "Do you wish to proceed? YES//" prompt.

> The RDSN action then automatically deleted the FT. STOCKTON (i.e., IEN 6538) STATION NUMBER field (#99) value from the local site's INSTITUTION file. The resulting, updated List Manager screen was redisplayed, as shown in Figure 2‑23:

> Duplicate station numbers Jan 30, 2001 15:05:09 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> 1 519HB FT STOCKTON 6164

> 2 519HB FORT STOCKTON 6539

> 3 688GA ALEXANDRIA VA 6491

> 4 688GA Alexandria 6540

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit// rdsn\<Enter\> Resolve duplicate station numbers

> Select Duplicate Station \#: (1-4): 2

> This action will auto-delete local/duplicate station numbers.

> Do you wish to proceed? YES// \<Enter\> ......

> Duplicate station numbers Jan 30, 2001 15:05:09 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> 1 688GA ALEXANDRIA VA 6491

> 2 688GA Alexandria 6540

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit// rdsn\<Enter\> Resolve duplicate station numbers

> Select Duplicate Station \#: (1-2): 2

> This action will auto-delete local/duplicate station numbers.

> Do you wish to proceed? YES// \<Enter\> ......

> Duplicate station numbers Jan 30, 2001 15:07:19 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> \*\*\*No duplicates\*\*\*

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit//

> <span id="_Ref159821457" class="anchor"></span>Figure 2‑23. Using the Resolve duplicate station numbers (RDSN) action—Resolving duplicates (2)

> When you compare the first list in Figure 2‑23 with the first list in Figure 2‑22, you see that the FT. STOCKTON duplicate entry was removed (deleted) from both the list and the local site's INSTITUTION file.

> To delete the second and last duplicate record in the first set of STATION NUMBER 519HB duplicates (i.e., Line \#2), the user entered a "2" at the "Select Duplicate Station \#: (1-4):" prompt. The RDSN action displayed the following message:

> "This action will auto-delete local/duplicate station numbers."

> The user then pressed the \<Enter\> key to accept the default of "YES" at the "Do you wish to proceed? YES//" prompt.

> Again, the list was updated and redisplayed. However, at that point, all of the first set of STATION NUMBER 519HB duplicates had been resolved, and thus, were no longer listed.

> The user was then left with the last pair of duplicates for STATION NUMBER 688GA.

> To delete the second and last duplicate record in the second set of STATION NUMBER 688GA duplicates (i.e., Line \#2), the user entered a "2" at the "Select Duplicate Station \#: (1-2):" prompt. The RDSN action displayed the following message:

> "This action will auto-delete local/duplicate station numbers."

> The user pressed the \<Enter\> key to accept the default of "YES" at the "Do you wish to proceed? YES//" prompt.

> Again, the list was updated and redisplayed. However, at that point, *all* of the duplicates had been resolved, and thus, there were no more entries to display in the list.

> If the user again selects the Resolve duplicate station numbers (RDSN) List Manager action, the screen in Figure 2‑24 is displayed:

> Duplicate station numbers Jan 29, 2001 15:50 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> \*\*\*No duplicates\*\*\*

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit// RDSN \<Enter\> QUIT

> No duplicates to select from!

> Duplicate station numbers Jan 29, 2001 15:50:11 Page: 1 of 1

> STA \# INSTITUTION NAME IEN

> \*\*\*No duplicates\*\*\*

> Enter ?? for more actions

> RDSN Resolve duplicate station numbers

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159821363" class="anchor"></span>Figure 2‑24. Using the Resolve duplicate station numbers (RDSN) action—All duplicates resolved

> At this point all of the duplicate records have been resolved, so running the Resolve duplicate station numbers (RDSN) again is unnecessary.

> 8. (Required) Choose the Auto update with national data (AUTO) List Manager action when you are ready to merge the FORUM IMF *national* entries with the local site's INSTITUTION file (#4).

> After performing Steps \#4 - \#7, you are ready to run the Auto update with national data (AUTO) List Manager action, as shown in Figure 2‑25:

> Select Action:Next Screen// AUTO \<Enter\> Auto update with national data ...working

> ............................................................................

> ............................................................................

> ............................................................................

> <u>INSTITUTION name vs GOLD name Jan 29, 2001 15:56:50 Page: 1 of 128</u>

> STA \# INSTITUTION NAME GOLD NAME

> 101 CENTRAL OFFICE CENTRAL OFFICE

> 102 TOPEKA TOPEKA

> 103 WASHINGTON WASHINGTON

> 104 AUSTIN FINANCE CENTER AUSTIN FINANCE CENTER

> 105 VBA MORTGAGE LOAN VBA MORTGAGE LOAN

> 123 WASHINGTON WASHINGTON

> 200 AUSTIN AUSTIN

> 201 HINES HINES

> 202 LOS ANGELES LOS ANGELES

> 203 PHILADELPHIA PHILADELPHIA

> 204 ST. PAUL ST. PAUL

> 205 WASHINGTON WASHINGTON

> 209 WASHINGTON WASHINGTON

> 207 WASHINGTON WASHINGTON

> 281 AUSTIN AUSTIN

> \+ Enter ?? for more actions

> LLCL List local station numbers AUTO Auto update with national data

> DSTA Delete local/dup. station \# CHCK Required clean up actions

> NATL List national data to merge

> Select Action:Next Screen//

> <span id="_Ref159821731" class="anchor"></span>Figure 2‑25. Using the Auto update with national data (AUTO) action—After eliminating duplicates

> As you can see from Figure 2‑25, the user chose to run the update, *after* all previous tasks had been completed (see Steps \#4 - \#7), by entering "AUTO" (Auto update with national data) at the "Select Action:Next Screen//" prompt.

> The software indicates that the update is taking place by displaying the word "working" and a series of dots while it merges the FORUM IMF entries with the local site's INSTITUTION file (#4).

> When the update has completed, the list of entries is updated and redisplayed. Compare this list to the original list displayed in Figure 2‑13—entries in both columns now match each other exactly. The user has now successfully cleaned the local site's INSTITUTION file (#4).

> Users should run the Required clean up actions (CHCK) List Manager action to confirm that the update completed successfully (see Step \#9 and Figure 2‑29).

> If the user runs the Auto update with national data (AUTO) List Manager action *prior* to completing Steps \#6 - \#7, the List Manager screen in Figure 2‑26 is displayed:

> Select Action:Next Screen// AUTO \<Enter\> Auto update with national data

> <u>INSTITUTION name vs GOLD name Jan 30, 2001 14:20:28 Page: 1 of 129</u>

> STA \# INSTITUTION NAME GOLD NAME

> 16 ISC SAN FRANCISCO

> 101 CENTRAL OFFICE CENTRAL OFFICE

> 102 TOPEKA

> 103 WASHINGTON

> 104 AUSTIN FINANCE CENTER

> 105 VBA MORTGAGE LOAN

> 123 WASHINGTON

> 200 AUSTIN DPC AUSTIN

> 201 HINES

> 202 LOS ANGELES

> 203 PHILADELPHIA

> 204 ST. PAUL

> 205 WASHINGTON

> 209 WASHINGTON

> 207 WASHINGTON

> \+ Duplicates sta \#s exist! -- NOTHING UPDATED!!!

> LLCL List local station numbers AUTO Auto update with national data

> DSTA Delete local/dup. station \# CHCK Required clean up actions

> NATL List national data to merge

> Select Action:Next Screen//

> <span id="_Ref159821802" class="anchor"></span>Figure 2‑26. Using the Auto update with national data (AUTO) action—Prior to eliminating local and duplicate entries

> Users *cannot* run the Auto update with national data (AUTO) Action without first running the Delete local/dup. station \# (DSTA) and Resolve duplicate station numbers (RDSN) List Manager actions, if any local or duplicate entries still exist in the local site's INSTITUTION file.

> 9. (Required) Choose the Required clean up actions (CHCK) List Manager action to monitor the system status after you have initiated the Auto update with national data (AUTO) List Manager action. This action can be run at any time to determine which steps are required to successfully complete the local site's INSTITUTION file (#4) cleanup.

> Specifically, this action does the following:

- Checks for local and duplicate Station Numbers (see Steps \#4 and \#6 - \#7).
- Checks for missing FORUM IMF entries in the local site's INSTITUTION file (see Steps \#5 and \#8).
- Displays any discrepancies found with the appropriate resolving action.
- Notifies the user when the update is completed if no discrepancies are found.

> If the user runs the Required clean up actions (CHCK) List Manager action *prior* to completing Steps \#6 - \#8, the List Manager screen in Figure 2‑27 is displayed:

> Select Action:Next Screen// CHCK \<Enter\> Required clean up actions

> <u>Check if update is complete Jan 29, 2001 15:49:06 Page: 1 of 1</u>

> Local/Duplicate station \#s exist -- use DSTA

> INSTITUTION file not updated with NATIONAL data -- use AUTO

> Enter ?? for more actions

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159821816" class="anchor"></span>Figure 2‑27. Using the Required clean up actions (CHCK) action—Prior to running the DSTA and AUTO actions

> In the example in Figure 2‑27, the user chose to run the Required clean up actions (CHCK) List Manager Action by entering "CHCK" at the "Select Action:Next Screen//" prompt.

> Since the Delete local/dup. station \# (DSTA), Resolve duplicate station numbers (RDSN), or Auto update with national data (AUTO) List Manager actions had *not* been completed, the following two messages displayed to tell the user to complete required Steps \#6 - \#8:

> Local/Duplicate station \#s exist -- use DSTA

> INSTITUTION file not updated with NATIONAL data -- use AUTO

> If the user runs the Required clean up actions (CHCK) List Manager action *prior* to completing Step \#8 but *after* completing Steps \#6 and \#7, the List Manager screen in Figure 2‑28 is displayed:

> Check if update is complete Jan 30, 2001 15:09:16 Page: 1 of 1

> INSTITUTION file not updated with NATIONAL data -- use AUTO

> Enter ?? for more actions

> Select Action:Quit//

> <span id="_Ref159821845" class="anchor"></span>Figure 2‑28. Using the Required clean up actions (CHCK) action—After running the DSTA option but prior to running the AUTO action

> In the example in Figure 2‑28, since the Auto update with national data (AUTO) List Manager action has *not* been completed but the user has run the Delete local/dup. station \# (DSTA) and Resolve duplicate station numbers (RDSN) List Manager actions, the following message displays to tell the user to complete required Step \#8:

> INSTITUTION file not updated with NATIONAL data -- use AUTO

> If the user runs the Required clean up actions (CHCK) List Manager action *after* completing *all* of the required steps (i.e., Steps \#6 - \#8), the List Manager screen in Figure 2‑29 is displayed:

> Select Action:Next Screen// chck\<Enter\> Required clean up actions

> <u>Check if update is complete Jan 29, 2001 15:58:39 Page: 1 of 0</u>

> CONGRATULATIONS!!! Update complete!

> Enter ?? for more actions

> Select Action:Quit// \<Enter\> QUIT

> <span id="_Ref159821777" class="anchor"></span>Figure 2‑29. Using the Required clean up actions (CHCK) action—After running the DSTA and AUTO actions

> Since all required Steps \#6 - \#8 have been successfully completed, the user is finished with the local site's INSTITUTION file cleanup. The software display the following message:

> CONGRATULATIONS!!! Update complete!

> 10. Log off of the system after the cleanup process is completed.

#### Institution File Cleanup Process—Health*e*Vet

HealtheVet applications will soon be using Institution data supplied by Standards & Terminology Services (STS): Standard Data Service (SDS). SDS will extract data from the Institution Master File (IMF) on FORUM. Once this data has been extracted and loaded into an SQL database, Foreign Key Constraints will be applied and the Institution records will be permanent for the life of Health*e*Vet-VistA. It is extremely important that we start with quality data.

Kernel Patch XU\*8.0\*335 allows sites to *locally* update their Institution data including the following fields (listed in field number order):

- NAME (#.01)
- STATE (#.02)
- Address Information:
- ST. ADDR. 1 (MAILING) field (#4.01)
- ST. ADDR. 2 (MAILING) field (#4.02)
- CITY (MAILING) field (#4.03)
- STATE (MAILING) field (#4.04)
- ZIP (MAILING) field (#4.05)
- STREET ADDR. 1 field (#1.01)
- STREET ADDR. 2 field (#1.02)
- CITY field (#1.03)
- STATE field (#.02)
- ZIP field (#1.04)
- FACILITY TYPE (#13)
- ASSOCIATIONS Multiple (#14)—VISN association type
- PARENT OF ASSOCIATION (#1)
- AGENCY CODE (#95)
- OFFICIAL VA NAME (#100)
- INACTIVE FACILITY FLAG (#101)

These local updates automatically update the central Institution Master File (IMF) on FORUM. The IMF update in turn broadcasts an HL7 unsolicited update to all VistA instances. This means that local edits will be published to every facility—automatically updating a site's entries throughout the VHA. Sites are only allowed to edit their own Institution data.

In addition to updating the fields listed above, the goal of Kernel Patch XU\*8.0\*335 is to correctly identify parent/child facility relationships in the INSTITUTION file (#4). In order to do this, the medical center "divisions" *must* be separated from the Health Care System (HCS) entries. This means an entry *must* be added for every HCS. Kernel Patch XU\*8.0\*335 adds these entries automatically.

In the ASSOCIATIONS Multiple field (#14), child facilities now point to their administrative parent. The parent, or primary facility, points to its parent (HCS or VISN). The new HCS entries point to a VISN entry. All parent relationships eventually resolve to a VISN.

A STATUS field (#3) was added to the FACILITY TYPE file (#4.1). National entries are flagged. An Input Transform was added to the FACILITY TYPE field (#13) of the INSTITUTION file (#4) to prevent the selection of *non*-standard facility types from "national" INSTITUTION file (#4) entries.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/060.png)</td>
<td><p><strong>NOTE:</strong> When updating the Facility Type of one of your facilities, if the Facility Type you need is not selectable and should be, send a MailMan message to the XUMF INSTITUTION HSITES mail group. Members of that group will review the request and make any necessary updates to the Master FACILITY TYPE file. This update will then be broadcast to all VistA instances.</p>
<p>The goal is to standardize both Institution and Facility Type data throughout the VHA. Please do <em>not</em> bypass the updating mechanism. If you do, it will defeat the standardization efforts and cause your site to become out-of-sync with other medical centers. Subsequent patches and/or MFS updates will override these local modifications. This will invalidate the local measures and result in data synchronization issues between facilities, which will result in an endless cycle of updating and cleanups.</p></td>
</tr>
</tbody>
</table>

The following options were added/modified with Kernel Patch XU\*8.0\*335:

- IMF edit Option \[XUMF IMF ADD EDIT\]—Added
- IMF Display Cleanup Status Option \[XUMF IMF EDIT STATUS\]—Added
- Patch XU\*8\*335 clean 4.1 and 4 Option \[XUMF335 clean 4.1 and 4\]—Added
- Institution File Query / Update Option \[XUMF INSTITUTION\]—Disabled

#### IMF edit Option

The IMF edit option \[XUMF IMF ADD EDIT\] allows the site to edit their INSTITUTION file (#4) entries (i.e., those entries that share the same 3-digit Station Number as the current users logon division) and generate an HL7 update message to update the Institution Master File (IMF) on FORUM.

HL7 *must* be running before using the XUMF IMF ADD EDIT option.

This option is locked with the XUMF INSTITUTION security key.

#### IMF Display Cleanup Status Option

The IMF Display Cleanup Status option \[XUMF IMF EDIT STATUS\], in the XUKERNEL menu, lists all your facilities that need updating. It also lists the fields that are missing data. It's a good idea to list this information before editing your data.

#### Patch XU\*8\*335 clean 4.1 and 4 Option

The Patch XU\*8\*335 clean 4.1 and 4 option \[XUMF335 clean 4.1 and 4\] queries the IMF for the latest copy of Institution data—updating the local INSTITUTION file (#4). All INACTIVE facilities have the NAME (#.01) ZZ'd and the VISN and PARENT FACILITY associations removed. It removes facility types before getting new values, so it should be run after hours. This option should be run at a later date after all sites have completed editing.

#### Institution File Query / Update Option

The Institution File Query / Update option \[XUMF INSTITUTION\] was disabled as part of Kernel Patch XU\*8.0\*335 (i.e., Health*e*Vet cleanup) to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA instance that has never done the cleanup and needs to load the full Institution table.

#### Update/refresh Institution file with IMF data Option

The Update/refresh Institution file with IMF data option \[XUMF LOAD INSTITUTION\] loads the current IMF data into the INSTITUTION file (#4).

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/061.png) | NOTE: The XUMF LOAD INSTITUTION option will not be completely successful if there are duplicate station numbers. The cleanup (see the "Institution File Cleanup Process—Initial" topic in this chapter) fixes/removes duplicates. Thus, the cleanup is a required first step before you can get updates, get the national table, or use the XUMF LOAD INSTITUTION option. |

#### Load Institution NPI values Option

The Load Institution NPI values option \[XUMF LOAD NPI\] was added to FORUM with Kernel Patch XU\*8.0\*416. This option is located on the Kernel Management Menu \[XUKERNEL\]. This option is to be used only in the case the National Provider Identifier (NPI) values fail to load in the post install or if it should become necessary to reload the NPI values (e.g., NPI values become corrupt or the data otherwise needs to be refreshed).

This option is used to edit institution data, including NPI and Taxonomy codes, selectable by coding system (e.g., NPI, Department of Defense \[DOD\], or Clinical Laboratory Improvement Amendments \[CLIA\]) and Identifier pair (for beta testing made target site, for Health Level seven \[HL7\] unsolicited update message, selectable rather than publish nationally).

#### Local Sites Step-by-Step Procedures—Health*e*Vet Institution File Cleanup Process

The following is the *suggested* order of the step-by-step procedures to clean up the local site's INSTITUTION file (#4) for Health*e*Vet (required steps are notated):

|                                                   |                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/062.png) | CAUTION: Prior to performing the Cleanup, users must review/check the data in the FORUM IMF file. |

|                                                                                                                |                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/063.png) | REF: For more information on reviewing/checking data, please refer to the "Institution File Data Review/Check" topic in this chapter. |

> 1. (Required) Log on to the system.

> 2. (Recommended) Choose the IMF Display Cleanup Status option \[XUMF IMF EDIT STATUS\] to view and review required Institution updating. We recommend that you work with your Health Administration Services (HAS) ADPAC.

> 3. (Required) Choose the IMF edit option \[XUMF IMF ADD EDIT\] to make any necessary updates to your site's institution data.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/064.png)</td>
<td><p><strong>NOTE:</strong> Please note the following when using the XUMF IMF ADD EDIT Option:</p>
<ul>
<li><p>This option is locked with the XUMF INSTITUTION security key.</p></li>
<li><p>The "^" jump out is disabled. You <em>must</em> answer all required fields.</p></li>
<li><p>HL7 <em>must</em> be running before using the XUMF IMF ADD EDIT option.</p></li>
</ul>
<ul>
<li><p>In the XUMF FORUM entry in the HL LOGICAL LINK file (#870), verify the correct TCP/IP ADDRESS—contact the <a href="mailto:G.XUMF%20INSTITUTION@FORUM.VA.GOV">REDACTED</a> mail group to get the appropriate TCP/IP address.</p></li>
<li><p>In the XUMF TEST entry in the HL LOGICAL LINK file (#870), verify the correct TCP/IP ADDRESS—contact REDACTED mail group to get the appropriate TCP/IP address.</p></li>
</ul>
<ul>
<li><p>Ping (i.e., HL PING) the XUMF FORUM link to make sure it is up.</p></li>
<li><blockquote>
<p>After editing your data, verify that the XUMF FORUM link is up. Use the Start/Stop Links option [HL START] if your updates are waiting in the queue.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

> Edit any of the following fields in the INSTITUTION file (#4) as necessary (for guidelines on editing these fields, please refer to the "Guidelines" topic and [Table 2‑1](#table_b1) that follow):

- NAME (#.01)
- STATE (#.02)
- PARENT OF ASSOCIATION (#1)
- Address Information:
- ST. ADDR. 1 (MAILING) field (#4.01)
- ST. ADDR. 2 (MAILING) field (#4.02)
- CITY (MAILING) field (#4.03)
- STATE (MAILING) field (#4.04)
- ZIP (MAILING) field (#4.05)
- STREET ADDR. 1 field (#1.01)
- STREET ADDR. 2 field (#1.02)
- CITY field (#1.03)
- STATE field (#.02)
- ZIP field (#1.04)
- FACILITY TYPE (#13)
- ASSOCIATIONS Multiple (#14)—VISN association type
- AGENCY CODE (#95)
- OFFICIAL VA NAME (#100)
- INACTIVE FACILITY FLAG (#101)

#### Guidelines

> General guidelines that should be used by Automated Data Processing Application Coordinators (ADPACs) and/or Information Resource Management (IRM) personnel when updating the following key fields/information in the INSTITUTION file (#4) are provided in (listed in field number order):

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/065.png)</td>
<td><p><strong>NOTE:</strong> If any of these procedures/guidelines are unclear or you have specific issues/questions, do any of the following:</p>
<ul>
<li><p>Send a MailMan message to the XUMF INSTITUTION mail group on FORUM.</p></li>
<li><p>Log a Remedy ticket.</p></li>
</ul>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field (Number)</strong></th>
<th><strong>Guidelines</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>NAME (#.01)</td>
<td><ul>
<li><blockquote>
<p>Must be 30 characters or less.</p>
</blockquote></li>
<li><blockquote>
<p>Make it meaningful:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>City + [","State] + Facility Type (e.g., Albany, NY VAMC; Albany, GA CBOC).</p>
</blockquote></li>
<li><blockquote>
<p>State is optional. It is used to uniquely identify facilities with like named cities.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Don't start NAME with the Facility Type.</p>
</blockquote></li>
<li><blockquote>
<p>Avoid using names that would only identify the site locally and not across the country (e.g., GV Sonny Montgomery; WM S Middleton). These types of names should be noted in the OFFICIAL VA NAME field (#100) instead.</p>
</blockquote></li>
<li><blockquote>
<p>Enter a name that makes the most sense for your facility. If your users are trained to identify a facility by its HCS name, then continue to use that same name. This applies to all your entries. SDS wants to keep site impact to a minimum. The data belongs to your facility. Our goal is to standardize VHA-wide data to include your site data.</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Make it unique:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Avoid multiple entries with the same name (e.g., rename Washington to Washington VAMC).</p>
</blockquote></li>
<li><blockquote>
<p>The Standard Data Service (SDS) team (or other responsible entity) will edit non-VHA entries to ensure uniqueness with like-named entries.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>STATE (#.02)</td>
<td><ul>
<li><blockquote>
<p>A state is required in the STATE FIELD (#.02).</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>Address Fields</td>
<td><ul>
<li><blockquote>
<p>Enter address information for both a mailing and physical address for every facility associated with the primary facility, VAMC, HCS, and/or VISN for which you have responsibility:</p>
</blockquote></li>
</ul>
<ul>
<li><blockquote>
<p>Mailing Address:</p>
</blockquote></li>
</ul>
<ul>
<li><p>ST. ADDR. 1 (MAILING) field (#4.01)</p></li>
<li><p>(optional) ST. ADDR. 2 (MAILING) field (#4.02)</p></li>
<li><p>CITY (MAILING) field (#4.03)</p></li>
<li><p>STATE (MAILING) field (#4.04)</p></li>
<li><p>ZIP (MAILING) field (#4.05)</p></li>
</ul>
<ul>
<li><blockquote>
<p>Physical Address:</p>
</blockquote></li>
</ul>
<ul>
<li><p>STREET ADDR. 1 field (#1.01)</p></li>
<li><p>(optional) STREET ADDR. 2 field (#1.02)</p></li>
<li><p>CITY field (#1.03)</p></li>
<li><p>STATE field (#.02)</p></li>
<li><p>ZIP field (#1.04)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>FACILITY TYPE (#13)</td>
<td><ul>
<li><blockquote>
<p>Select the correct Facility Type.</p>
</blockquote></li>
<li><blockquote>
<p>Medical Centers, Medical Centers and Regional Offices, and Regional Offices-Outpatient Clinics should have one of the following Facility types:</p>
</blockquote></li>
</ul>
<blockquote>
<p>VAMC</p>
<p>M&amp;ROC</p>
<p>RO-OC</p>
</blockquote>
<ul>
<li><blockquote>
<p>Child facilities (relative to a medical center) should have one of the following Facility Types:</p>
</blockquote></li>
</ul>
<blockquote>
<p>CBOC COMMUNITY BASED OUTPATIENT CLINIC</p>
<p>CIVH CIVILIAN HOSPITAL</p>
<p>CMOP CONSOLIDATED MAIL OUTPATIENT PHARMACY</p>
<p>DOM DOMICILIARY</p>
<p>DENT DENTAL CLINIC</p>
<p>DOD DEPARTMENT OF DEFENSE</p>
<p>M&amp;ROC MEDICAL AND REGIONAL OFFFICE CENTER</p>
<p>MORC MOBILE OUTREACH CLINIC</p>
<p>NHC NURSING HOME CARE</p>
<p>OPC OUTPATIENT CLINIC</p>
<p>ORC OUTREACH CLINIC</p>
<p>OTHER OTHER</p>
<p>PHARM PHARMACY</p>
<p>PHS PUBLIC HEALTH SERVICE HOSPITAL</p>
<p>PRRTP PSYCHOLOGICAL RESIDENTIAL REHAB TREATMNT PRG</p>
<p>SARRTP SUBSTANCE ABUSE REHAB TREATMENT PROGRAM</p>
<p>STDM STATE DOMICILIARY</p>
<p>STHH STATE HH</p>
<p>STNB STATE NURSING BEDS</p>
<p>SVH STATE VETERANS HOME</p>
<p>USAF US AIR FORCE HOSPITAL</p>
<p>USAH US ARMY HOSPITAL</p>
<p>USCG US COAST GUARD HOSPITAL</p>
<p>USMC US MARINE CORP HOSPITAL</p>
<p>USNH US NAVAL HOSPITAL</p>
<p>VAMC VA MEDICAL CENTER</p>
<p>VANPH NEURAL PSYCHIATRIC HOSPITAL</p>
</blockquote>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/066.png) <strong>NOTE:</strong> If you require a Facility Type that is not listed, send a MailMan message to the XUMF INSTITUTION mail group on FORUM. Please do <em>not</em> take any other actions. The required Facility Type will be activated using the Master File Server (MFS) mechanism. This will keep all VistA instances standard.</p></td>
</tr>
<tr class="odd">
<td>ASSOCIATIONS Multiple (#14)</td>
<td><blockquote>
<p><strong>VISN Information—</strong>PARENT OF ASSOCIATION field (#1) of the ASSOCIATIONS multiple (#14). ASSOCIATIONS (#.01) type "VISN".</p>
</blockquote>
<ul>
<li><blockquote>
<p>Inactive facilities should be NULL.</p>
</blockquote></li>
<li><blockquote>
<p>Only treating facilities should have a VISN.</p>
</blockquote></li>
<li><blockquote>
<p>All active treating facilities must have a VISN.</p>
</blockquote></li>
</ul>
<p><strong>Parent Facility Information—</strong>PARENT OF ASSOCIATION field (#1) of the ASSOCIATIONS multiple (#14). ASSOCIATIONS (#.01) type "PARENT FACILITY".</p>
<ul>
<li><blockquote>
<p>Child facilities should point to the administrative parent—your CBOC, NHC, OPC, MORC, etc, points to its parent VAMC or "division."</p>
</blockquote></li>
</ul>
<blockquote>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/067.png) <strong>NOTE:</strong> If the child facility is a shared facility, then point to the appropriate HCS if applicable. If the facility is a special case (e.g., an unnamed multi-divisional aggregate), then send a MailMan message to the XUMF INSTITUTION mail group on FORUM for processing.</p>
</blockquote>
<ul>
<li><blockquote>
<p>The "division" (VAMC) points to its immediate parent, one of the following:</p>
</blockquote></li>
</ul>
<blockquote>
<p>VA GREATER LOS ANGELES (691)</p>
<p>VA HEARTLAND-EAST VISN15 (657)</p>
<p>VA HEARTLAND-WEST VISN15 (589)</p>
<p>VA CHICAGO HSC (537)</p>
<p>CENTRAL PLAINS NETWORK (636)</p>
<p>MONTANA HCS (436)</p>
<p>VA PACIFIC ISLANDS HCS (459)</p>
<p>NEW MEXICO HCS (501)</p>
<p>AMARILLO HCS (504)</p>
<p>MARYLAND HCS (512)</p>
<p>WEST TEXAS HCS (519)</p>
<p>BOSTON HCS (523)</p>
<p>UPSTATE NEW YORK HCS (528)</p>
<p>NORTH TEXAS HCS (549)</p>
<p>EASTERN COLORADO HCS (554)</p>
<p>NEW JERSEY HCS (561)</p>
<p>BLACK HILLS HCS (568)</p>
<p>CENTRAL CALIFORNIA HCS (570)</p>
<p>N FLORIDA/S GEORGIA HCS (573)</p>
<p>GREATER NEBRASKA HCS (597)</p>
<p>CENTRAL ARKANSAS HCS (598)</p>
<p>LONG BEACH HCS (600)</p>
<p>CENTRAL ALABAMA HCS (619)</p>
<p>HUDSON VALLEY HCS VAMC (620)</p>
<p>TENNESSEE VALLEY HCS (626)</p>
<p>PALO ALTO HCS (640)</p>
<p>PITTSBURGH HCS (646)</p>
<p>ROSEBURG HCS (653)</p>
<p>SIERRA NEVADA HCS (654)</p>
<p>SALT LAKE CITY HCS (660)</p>
<p>PUGET SOUND HCS (663)</p>
<p>SAN DIEGO HCS (664)</p>
<p>SOUTH TEXAS HCS (671)</p>
<p>CENTRAL TEXAS HCS (674)</p>
<p>EASTERN KANSAS HCS (677)</p>
<p>CONNECTICUT HCS (689)</p>
<p>EL PASO VA HCS (756)</p>
<p>NEW YORK HHS (630)</p>
<p>VISN 1</p>
<p>VISN 2</p>
<p>VISN 3</p>
<p>VISN 4</p>
<p>VISN 5</p>
<p>VISN 6</p>
<p>VISN 7</p>
<p>VISN 7</p>
<p>VISN 7</p>
<p>VISN 7</p>
<p>VISN 7</p>
<p>VISN 12</p>
<p>VISN 13</p>
<p>VISN 14</p>
<p>VISN 15</p>
<p>VISN 16</p>
<p>VISN 17</p>
<p>VISN 18</p>
<p>VISN 19</p>
<p>VISN 20</p>
<p>VISN 21</p>
<p>VISN 22</p>
<p>VISN 23</p>
</blockquote></td>
</tr>
<tr class="even">
<td>AGENCY CODE (#95)</td>
<td><ul>
<li><blockquote>
<p><strong>V</strong>—If Facility Type is Department of Veterans Affairs (VA)-related, then AGENCY CODE should be <strong>VA</strong> ("<strong>V</strong>").</p>
</blockquote></li>
<li><blockquote>
<p><strong>AF</strong>—If Facility Type is USAF, then AGENCY CODE should be <strong>AIR FORCE</strong> ("<strong>AF</strong>").</p>
</blockquote></li>
<li><blockquote>
<p><strong>I</strong>—If Facility Type is INDIAN HEALTH SERVICE (IHS), then AGENCY CODE should be <strong>IHS</strong> ("<strong>I</strong>").</p>
</blockquote></li>
<li><blockquote>
<p><strong>ARMY</strong>—If Facility Type is USAH, then AGENCY CODE should be "<strong>ARMY</strong>".</p>
</blockquote></li>
<li><blockquote>
<p><strong>N</strong>—If Facility Type is USNH, then AGENCY CODE should be <strong>NAVY</strong> ("<strong>N</strong>").</p>
</blockquote></li>
<li><blockquote>
<p><strong>O</strong>—Otherwise AGENCY CODE should be <strong>OTHER</strong> ("<strong>O</strong>").</p>
</blockquote></li>
<li><blockquote>
<p><strong>E</strong>—If Facility Type is Electronic Health Record (EHR), then AGENCY CODE should be <strong>EHR</strong> ("<strong>E</strong>"). This code added with Kernel Patch XU*8.0*394.</p>
</blockquote></li>
<li><blockquote>
<p><strong>USCG—</strong>If Facility Type is United States Coast Guard (USCG), then AGENCY CODE should be <strong>COAST GUARD</strong> ("<strong>USCG</strong>"). This code added with Kernel Patch XU*8.0*394.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>OFFICIAL VA NAME (#100)</td>
<td><ul>
<li><blockquote>
<p>The full name of the facility (i.e., 80 characters or less). For example, "VA Healthcare Network Upstate New York HCS-Buffalo Division" for 528 - Buffalo, NY VAMC.</p>
</blockquote></li>
<li><blockquote>
<p>If no official name exists, or you are not sure, enter the same value as the NAME field (#.01). It can be updated later, if necessary.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>INACTIVE FACILITY FLAG (#101)</td>
<td><ul>
<li><blockquote>
<p>If the institution/facility is inactive, then set the INACTIVE FACILITY FLAG field (#101).</p>
</blockquote></li>
<li><blockquote>
<p>The Inactive facility NAME should begin with "ZZ".</p>
</blockquote></li>
<li><blockquote>
<p>The VISN and PARENT FACILITY associations should be NULL.</p>
</blockquote></li>
<li><blockquote>
<p>If the facility you wish to inactivate/edit has a Station Number that does not begin with the same first three digits as your current "division"—the division you are logged into—then you <em>must</em> log in under the old Station Number "division" to be able to edit it or its children.</p>
</blockquote></li>
<li><blockquote>
<p>You must have a pointer in the DIVISION multiple of the NEW PERSON file (#200) in order to log into a division.</p>
</blockquote></li>
<li><blockquote>
<p>If your site has installed Kernel Patch XU*8.0*287, then the person assigning the division must have the XUMGR security key to override the input transform to assign an inactive facility.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref159820094" class="anchor"></span>Table 2‑1. Local field edit guidelines (Kernel Patch XU\*8.0\*335)

#### Add/Modify Local Institution Data

The Local Site Institution Master File Administrators will continue to use the Institution Edit option \[XU-INSTITUTION-E\] on the Kernel Management Menu \[XUKERNEL\] in order to add or modify *local* data entries (non-*national* data entries) in the INSTITUTION file (#4) at their sites.

Kernel Patch XU\*8.0\*209 prohibits local sites from directly adding, deleting, or editing certain fields in *national* data entries in the INSTITUTION file (#4):

- National Data Entries—Entries in the INSTITUTION file (#4) that have an assigned STATION NUMBER (#99) and a have a STATUS (#11) set to "National." Only the Institution Master File (IMF) on FORUM originates the *national* entries that are automatically disseminated to the field via the Master File Server (MFS). Only the FORUM Institution Master File Administrators have access to the FORUM IMF.
- Local Data Entries—Entries in the INSTITUTION file (#4) that do *not* have an assigned STATION NUMBER (#99) and a STATUS (#11) set to "Local." All other fields (e.g., NAME \[#.01\]), however, are available for editing by the sites to enter non-*national* Institutions into their local INSTITUTION files (#4).

#### Local Sites Step-by-Step Procedures—Add/Modify Local Institution Data

The following are the step-by-step procedures to add or modify *Local* data entries in a local site's INSTITUTION file (#4):

> 1. Log on to the system.

> 2. Navigate to the Kernel Management Menu \[XUKERNEL\], under the Operations Management menu \[XUSITEMGR\], as shown in Figure 2‑30:

> Select Systems Manager Menu Option: Operations Management

> System Status

> Introductory text edit

> CPU/Service/User/Device Stats

> RJD Kill off a users' job

> Alert Management ...

> Alpha/Beta Test Option Usage Menu ...

> Clean old Job Nodes in XUTL

> Delete Old (\>14 d) Alerts

> Kernel Management Menu ...

> Post sign-in Text Edit

> User Management Menu ...

> Select Operations Management Option: Kernel Management Menu

> Enter/Edit Kernel Site Parameters

> IMF edit

> Institution Edit

> Kernel New Features Help

> Select Kernel Management Menu Option:

> <span id="_Ref159821884" class="anchor"></span>Figure 2‑30. Navigating to the Kernel Management Menu

> 3. Kernel Patch XU\*8.0\*217 introduced the IMF address edit option and Kernel Patch XU\*8.0\*335 replaced this option as the IMF edit option. \[XUMF IMF ADD EDIT\]. This option is locked with the XUMF INSTITUTION security key. It allows sites to locally edit their address information and trigger a Health Level Seven (HL7) message to the Institution Master File (IMF.) A handler at the IMF server updates the master file and broadcasts the updated information to all subscriber medical centers/links. The Master File Server (MFS) mechanism handler at each medical center/site updates the local INSTITUTION file (#4) with the updated Institution data. A MailMan message notifies the XUMF INSTITUTION mail group about the updates (displaying old and new values for the affected entry), or an error message is sent to the XUMF SERVER mail group if there was a problem.

|                                                                                                                |                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/068.png) | REF: For a list of new address fields added/modified with Kernel Patch XU\*8.0\*217, please refer to the "Kernel Patch XU\*8.0\*217" topic in Chapter 1, "Introduction," in this manual. |

> a. Edit Address

> Choose the IMF edit option \[XUMF IMF ADD EDIT\] to update both the physical and mailing address information for your medical center and associated facilities (all your divisions and clinics.), as shown in Figure 2‑31:

> Enter/Edit Kernel Site Parameters

> IMF edit

> Institution Edit

> Kernel New Features Help

> Select Kernel Management Menu Option: IMF edit

> Enter Station Number: 662

> Physical address:

> STREET ADDR. 1: 123 MAIN ST. Replace \<Enter\>

> CITY: ANY TOWN// \<Enter\>

> STATE: CALIFORNIA// \<Enter\>

> ZIP: 99999// \<Enter\>

> Mailing address:

> ST. ADDR. 1 (MAILING): 123 MAIN ST.

> CITY (MAILING): ANY TOWN

> STATE (MAILING): CALIFORNIA

> ZIP (MAILING): 99999

> Are you ready to update the Institution Master File? YES// \<Enter\>

> ...send HL7 message to Master File Server...

> Sent.

> Select Kernel Management Menu Option:

<span id="_Ref159822424" class="anchor"></span>Figure 2‑31. Running the IMF edit option

> Answer "YES" at the "Are you ready to update the Institution Master File? YES//" prompt.

> b. (Optional) Verify Address Updates.

> Log on to FORUM and use the Institution file inquire option on the DBA menu to verify that the entry updated correctly.

> 4. Choose the Institution Edit option \[XU-INSTITUTION-E\], as shown in Figure 2‑32:

> Enter/Edit Kernel Site Parameters

> IMF edit

> Institution Edit

> Kernel New Features Help

> Select Kernel Management Menu Option: Institution Edit

> Select INSTITUTION NAME:

<span id="_Ref159822425" class="anchor"></span>Figure 2‑32. Choosing the Institution Edit option

> 5. Enter a new Institution NAME (see Step \#5a) or choose an existing Local entry for modifications (see Step \#5b).

|                                                                                                                |                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/069.png) | NOTE: Local entries can use the same name that is found in a national entry. However, sites should be aware that identical names in both a national and a local entry might cause confusion at the local level (e.g., when running local reports based on the Institution Name). |

> a. Adding a New *Local* Entry.

> Select INSTITUTION NAME: ?

> Answer with INSTITUTION NAME, or STATUS, or STATION NUMBER, or

> OFFICIAL VA NAME, or CURRENT LOCATION, or NAME (CHANGED FROM)

> Do you want the entire 1985-Entry INSTITUTION List? YES \<Enter\> (Yes)

> Choose from:

> 13TH & MISSSION CA D 662BU

> 516BAY PINES FL MC(M)

> ABILENE TX CBOC 519HC

> ABILENE TX ORC 519HA

> ABILENE KS CBOC 677GC

> ABILENE KS ORC 677HE INACTIVE

> ABILENE KS

> AIR FORCE USAF 381

> AKRON OH CBOC 541GG

> ALAMOGORDO NM CBOC 501GI

> ALBANY NY VAMC 500 INACTIVE Jul 01, 2000

> ALBANY GA CBOC 557GB

> ALBANY NY PRRTP 459PA

> ALBANY NY VANB 5009AA

> ALBANY NY CBOC 500GA

> ALBANY NY CBOC 500GD INACTIVE Jul 01, 2000

> ALBANY NY PRRTP 500PA INACTIVE Jul 01, 2000

> ALBANY NY VAMC 528A8

> ALBANY AREA NY NC 917

> ALBANY RURAL NY SL 803IU

> '^' TO STOP: ^

> You may enter a new INSTITUTION, if you wish

> Name must be 3-30 characters -- if national entry, do not edit!

> Select INSTITUTION NAME: TEST MEDICAL CENTER

> Are you adding 'TEST MEDICAL CENTER' as a new INSTITUTION (the 1985TH)? No// YES \<Enter\> (YES)

> <span id="_Ref159821920" class="anchor"></span>Figure 2‑33. Entering a new local Institution into the local site's INSTITUTION file

> In the example in Figure 2‑33, the user first entered a single question mark ("?") at the "Select INSTITUTION NAME:" prompt and then answered "YES" at the "Do you want the entire 1985-Entry INSTITUTION List?" prompt in order to see a list of current Institutions in the local INSTITUTION file.

> In Figure 2‑33, the user chose to enter a new *Local* Institution by entering "TEST MEDICAL CENTER" (i.e., a new Institution NAME) at the "Select INSTITUTION NAME:" prompt. The user answered "YES" at the "Are you adding 'TEST MEDICAL CENTER' as a new INSTITUTION (the 1985TH)? No//" prompt to confirm the new entry.

> After entering the new NAME, the user was automatically placed into a ScreenMan form, as shown in Figure 2‑34:

> <u>NAME</u>: TEST MEDICAL CENTER STATION NUMBER:

> STATE: ACOS HOSPITAL ID:

> FACILITY TYPE: DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS:

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: Press \<PF1\>H for help Insert

> <span id="_Ref159821961" class="anchor"></span>Figure 2‑34. ScreenMan form showing the new "TEST MEDICAL CENTER" Institution

> At this point, only the NAME field (#.01) has been completed. The user can now enter other required information about the new *Local* Institution (see Step \#5).

> If users enter only a new Institution NAME and then try to save their entries without making any other field entries, the software returns the error message displayed in Figure 2‑35:

> THE DATA COULD NOT BE FILED.

> Page 1, STATUS is a required field

> Press RETURN to continue:

> <span id="_Ref159821975" class="anchor"></span>Figure 2‑35. Sample error display screen

> b. Modifying an Existing Entry.

> If the user had entered an existing *Local* Institution NAME entry at the "Select INSTITUTION NAME:" prompt (e.g., 516BAY PINES, from the sample list of existing Institution NAMES in Figure 2‑33), the software would have opened a ScreenMan form similar to the form in Figure 2‑36:

> <u>NAME</u>: 516BAY PINES STATION NUMBER:

> STATE: FLORIDA ACOS HOSPITAL ID:

> FACILITY TYPE: MC(M) DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS: Local

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref159822036" class="anchor"></span>Figure 2‑36. Sample ScreenMan form of an existing local Institution entry

> Local sites *can* edit any of the following fields on a *Local* entry in the local site's INSTITUTION file (#4) while using the Institution Edit option \[XU-INSTITUTION-E\]. The following fields are listed in field number order:

- NAME (#.01, only on initial entry of a new Institution)

|                                                                                                                |                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/070.png) | NOTE: Local entries can use the same name that is found in a national entry. However, sites should be aware that identical names in both a national and a local entry might cause confusion at the local level (e.g., when running local reports based on the Institution Name). |

- STATE (#.02)
- STATUS (#11, valid value is "Local")
- FACILITY TYPE (#13)
- ASSOCIATIONS Multiple (#14)
- ASSOCIATIONS (#.01)
- PARENT OF ASSOCIATION (#1)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/071.png)</td>
<td><strong>NOTE:</strong> Kernel Patch XU*8.0*294 prevents the adding of a VISN or PARENT FACILITY association to an Institution entry that does not have a corresponding PARENT OF ASSOCIATION.<br />
<br />
Kernel Patch XU*8.0*335 pointed all child facilities to their administrative parents. The parent, or primary facility, points to its parent (HCS or VISN). The HCS entries point to a VISN entry. All parent relationships eventually resolve to a VISN.</td>
</tr>
</tbody>
</table>

- ACOS HOSPITAL ID (#51)
- DOMAIN (#60))
- AGENCY CODE (#95)
- OFFICIAL VA NAME (#100)

> Local sites *cannot* edit the following field on a *Local* entry in the local site's INSTITUTION file (#4) while using the Institution Edit option \[XU-INSTITUTION-E\]:

- STATION NUMBER (#99)

> If the user had entered an existing *National* Institution name entry at the "Select INSTITUTION NAME:" prompt (e.g., 13<sup>TH</sup> & MISSION from the sample list of existing Institution NAMES in Figure 2‑33), the software would have opened a ScreenMan form similar to the form in Figure 2‑37:

> NAME: 13TH & MISSSION STATION NUMBER: 662BU

> STATE: CALIFORNIA ACOS HOSPITAL ID:

> FACILITY TYPE: D DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS: National

> Association Parent

> VISN VISN 21

> PARENT FACILITY SAN FRANCISCO

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> COMMAND: Press \<PF1\>H for help Insert

> <span id="_Ref159822064" class="anchor"></span>Figure 2‑37. Sample ScreenMan form of an existing national Institution entry

> Local sites are *not permitted* to edit any of the following fields on a *National* entry in the local site's INSTITUTION file while using the Institution Edit option \[XU-INSTITUTION-E\]. The following fields are listed in field number order:

- NAME (#.01)
- STATE (#.02)
- STATUS (#11)
- FACILITY TYPE (#13)
- STATION NUMBER (#99)
- OFFICIAL VA NAME (#100)

> c. Deleting an Existing Entry.

> To delete a *Local* entry from the INSTITUTION file (#4), enter an at-sign (i.e., "@") in the NAME field (#.01), as shown in Figure 2‑38:

> NAME: @ STATION NUMBER:

> STATE: ACOS HOSPITAL ID:

> FACILITY TYPE: DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS:

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> WARNING: DELETIONS ARE DONE IMMEDIATELY!

> (EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

> Are you sure you want to delete this entire record (Y/N)? YES \<Enter\>

> <span id="_Ref159822114" class="anchor"></span>Figure 2‑38. Deleting a Local Institution

> The software presents the following warning:

> WARNING: DELETIONS ARE DONE IMMEDIATELY!

> (EXITING WITHOUT SAVING WILL NOT RESTORE DELETED RECORDS.)

|                                                   |                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/072.png) | CAUTION: It is *not* recommended that users delete an INSTITUTION file entry *unless* it was just immediately created in error. |

> After the user confirmed the deletion by entering "YES" at the "Are you sure you want to delete this entire record (Y/N)?" prompt, the ScreenMan form in Figure 2‑39 was displayed:

> STATE: ACOS HOSPITAL ID:

> FACILITY TYPE: DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS:

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Select INSTITUTION NAME:

> <span id="_Ref159822130" class="anchor"></span>Figure 2‑39. ScreenMan form displayed after a deletion

> 6. Add/Modify the following fields displayed in the ScreenMan form for *Local* entries (listed in field number order):

- NAME (#.01, only on the initial entry of a new Institution)
- STATE (#.02)
- STATUS (#11, valid value is "Local")
- FACILITY TYPE (#13)

|                                                                                                                |                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/073.png) | REF: For a list of TYPEs and their acronym definitions, please refer to "Appendix B—Facility Type Acronyms" in this manual. |

- ASSOCIATIONS Multiple (#14)
  - ASSOCIATIONS (#.01)
  - PARENT OF ASSOCIATION (#1)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/074.png)</td>
<td><strong>NOTE:</strong> Kernel Patch XU*8.0*294 prevents the adding of a VISN or PARENT FACILITY association to an Institution entry that does not have a corresponding PARENT OF ASSOCIATION.<br />
<br />
Kernel Patch XU*8.0*335 pointed all child facilities to their administrative parent. The parent, or primary facility, points to its parent (HCS or VISN). The HCS entries point to a VISN entry. All parent relationships eventually resolve to a VISN.</td>
</tr>
</tbody>
</table>

- ACOS HOSPITAL ID (#51)
- DOMAIN (#60)
- AGENCY CODE (#95)
- OFFICIAL VA NAME (#100)

> The software *prevents* users from entering or modifying the following fields of a record in the local INSTITUTION file with a STATUS field set to "National." The following fields are listed in field number order:

- NAME (#.01)
- STATE (#.02)
- STATUS (#11)
- FACILITY TYPE (#13)
- STATION NUMBER (#99)
- OFFICIAL VA NAME (#100)

> In the example in Figure 2‑40, the user tried to enter a STATION NUMBER for a *Local* entry, which is *not* allowed:

> <u>NAME</u>: TEST MEDICAL CENTER STATION NUMBER: 999999

> STATE: ACOS HOSPITAL ID:

> FACILITY TYPE: DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS:

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> No local station numbers allowed!

> Press \<PF1\>H for help Insert

> <span id="_Ref159822144" class="anchor"></span>Figure 2‑40. Trying to enter a STATION NUMBER field in a local Institution entry

> In the example in Figure 2‑40, after the user tried to enter *Local* STATION NUMBER "999999" at the "STATION NUMBER:" prompt in the ScreenMan form, the software displayed the following message:

> No local station numbers allowed!

> In the example in Figure 2‑41, the user tried to enter "National" as the STATUS; however, this is *not* allowed and the Help for that field was automatically generated:

> <u>NAME</u>: TEST MEDICAL CENTER STATION NUMBER:

> STATE: CALIFORNIA ACOS HOSPITAL ID: 123456

> FACILITY TYPE: DOMAIN: SANFRANCISCO.VA.

> AGENCY CODE: VA OFFICIAL VA NAME:

> STATUS: National

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Local or National -- if national, do not edit!

> Choose from:

> N National

> L Local

> Press \<PF1\>H for help Insert

> <span id="_Ref159822173" class="anchor"></span>Figure 2‑41. Trying to enter "National" in the STATUS field in a local Institution entry

> In the example in Figure 2‑41, after the user tried to enter "National" at the "STATUS:" prompt in the ScreenMan form, the software displayed the following Help message:

> Local or National -- if national, do not edit!

> Choose from:

> N National

> L Local

|                                                   |                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/075.png) | CAUTION: Even though "National" is shown in the list of choices, users can enter only "Local" as a STATUS for *Local* entries! |

> In the example in Figure 2‑42, the user tried to enter an invalid FACILITY TYPE for a *Local* entry, which automatically generated the Help for that field:

> <u>NAME</u>: TEST MEDICAL CENTER STATION NUMBER:

> STATE: ACOS HOSPITAL ID:

> FACILITY TYPE: TEST DOMAIN:

> AGENCY CODE: OFFICIAL VA NAME:

> STATUS: Local

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Enter Facility Type -- If national entry, do not edit!

> Answer with FACILITY TYPE NAME, or FULL NAME, or STATUS

> Do you want the entire 116-Entry FACILITY TYPE List?

> <span id="_Ref159822221" class="anchor"></span>Figure 2‑42. Entering an invalid FACILITY TYPE in a local Institution entry

> In the example in Figure 2‑42, after the user tried to enter invalid FACILITY TYPE "TEST" at the "FACILITY TYPE:" prompt in the ScreenMan form, the software displayed the following Help message:

> Enter Facility Type -- If national entry, do not edit!

> Answer with FACILITY TYPE NAME, or FULL NAME, or STATUS

|                                                                                                                |                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/076.png) | REF: For a list of TYPEs and their acronym definitions, please refer to "Appendix B—Facility Type Acronyms" in this manual. |

> After the user entered a valid FACILITY TYPE and values for the other fields to be populated (i.e., STATE, ACOS HOSPITAL ID, DOMAIN, AGENCY CODE, and OFFICIAL VA NAME), the final ScreenMan form looked like the form shown in Figure 2‑43:

> <u>NAME</u>: TEST MEDICAL CENTER STATION NUMBER:

> STATE: CALIFORNIA ACOS HOSPITAL ID: 123456

> FACILITY TYPE: VAMC DOMAIN: SANFRANCISCO.VA.

> AGENCY CODE: VA OFFICIAL VA NAME: VA TEST SITE

> STATUS: Local

> Association Parent

> \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

> Exit Save Refresh

> Enter a command or '^' followed by a caption to jump to a specific field.

> COMMAND: Press \<PF1\>H for help Insert

> <span id="_Ref159822251" class="anchor"></span>Figure 2‑43. Final ScreenMan form for the local Institution file entry

> At this point, all of the edits/updates were completed, so the user was ready to save the data and exit the Institution file entry.

> 7. When all of the edits/updates are completed, log off of the system.

#### Maintenance & Troubleshooting

Kernel Patch XU\*8.0\*209 created the XUMF INSTITUTION mail group at each site. The Local Site Institution Master File Administrators at a site are responsible for populating (i.e., Mail Group Coordinator), maintaining, and monitoring this mail group.

The XUMF INSTITUTION mail group receives bulletins sent via VistA's MailMan software regarding updates to the local site's INSTITUTION file (#4). The mail group at the site is notified when the local INSTITUTION file has been automatically updated with *national* entries from the Institution Master File (IMF) on FORUM via the Master File Server (MFS). The mail group should be populated with the appropriate personnel located at the site (e.g., Local Site Institution Master File Administrator\[s\], IRM Chief, ADPAC\[s\], etc.).

Kernel Patch XU\*8.0\*299 created the XUMF ERROR mail group at each site. The local site is responsible for populating (i.e., Mail Group Coordinator), maintaining, and monitoring this mail group.

Another duty of the Local Site Institution Master File Administrators is to serve as the point of contact that monitors and troubleshoots any problems with the INSTITUTION and FACILITY TYPE master files located at the site.

#### Local Sites Step-by-Step Procedures—Maintenance and Troubleshooting

The following are the suggested step-by-step procedures for monitoring and troubleshooting the master files at the site:

> 1. Monitor for Messages sent to the XUMF INSTITUTION and XUMF ERROR mail groups—When a message is received, the Local Site Institution Master File Administrators should do one or more of the following:

> a. Verify that the master files were successfully updated based on the information contained in the message.

> b. Process any error messages that are sent to the mail groups.

- Contact the FORUM Institution Master File Administrators, discuss the problem, and devise a solution.
- After the problem has been resolved, contact the FORUM Institution Master File Administrators to verify that the master file has been successfully updated.

> 2. Monitor any VistA HL7 error messages regarding transmission errors.

> 3. Process any HL7-type error messages.

> a. Try to resend an unsent HL7 message.

> b. If the problem persists, contact the VistA HL7 Team for assistance and advise the FORUM Institution Master File Administrators of the problem.

> c. After the problem has been resolved, contact the FORUM Institution Master File Administrators to verify that the master file has been successfully updated.

> 4. Return to Step \#1.

## FORUM (Production) IMF Administrator Duties

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Introduction

The IFR-related software (i.e., Kernel Patch XU\*8.0\*206) requires that one or more FORUM Institution Master File (IMF) Administrators be assigned to maintain and update the *national* entries in the master files located on FORUM that are transmitted VHA-wide via the Master File Server (MFS). Initially, these administrators were members of the VHA Health Systems Design & Development's Infrastructure & Security Services (ISS) Team. The current FORUM IMF Administrators are assigned by Enterprise VistA Support (EVS). Only the FORUM Institution Master File Administrators hold the XUMF INSTITUTION security key that allows them to edit the master files on FORUM.

The following option is available only to the FORUM Institution Master File Administrators of the INSTITUTION (#4) master file located on FORUM:

Institution Master File Edit Option \[XUMF FORUM INSTITUTION\]—Edit *national* entries in the INSTITUTION file (#4) located on FORUM.

The following duties are the responsibility of the FORUM Institution Master File Administrators of the INSTITUTION (#4) and FACILITY TYPE (#4.1) master files located on FORUM:

- Process the FORUM master file change notifications.
- Troubleshoot problems with the master files and the Master File Server (MFS) software.

This section provides the step-by-step procedures and general information describing the day-to-day duties and maintenance requirements of the master files on FORUM, as performed by the FORUM Institution Master File Administrators.

#### Processing Master Files Change Notifications

The primary duty of the FORUM Institution Master File Administrators is to process changes to the Institution Master file (IMF) and Facility Type Master File (FMF) on FORUM.

#### FORUM Step-By-Step Procedures—Processing Master File Changes

The following are the step-by-step procedures required for processing the master file change notifications on FORUM:

> 1. Monitor Microsoft Exchange for e-mail notifications from 045A4 regarding changes to the Institution Master File (IMF) and Facility Type Master File (FMF) on FORUM.

> 2. When a master file change notification is received, log on to FORUM.

> 3. Choose the appropriate master file edit option:

> a.Edits in the INSTITUTION file (#4) on FORUM—Use the Institution Master File Edit option \[XUMF FORUM INSTITUTION\] to edit the Institution Master File (IMF) on FORUM.

> b.Edits in the FACILITY TYPE file (#4.1) on FORUM—Use VA FileMan to edit the Facility Type Master File (FMF) on FORUM.

> In the example in Figure 3‑1, the user chose the Institution Master File Edit option \[XUMF FORUM INSTITUTION\] in order to enter a new STATION NUMBER into the FORUM Institution Master File (IMF):

> Select OPTION NAME: XUMF

> 1 XUMF FORUM INSTITUTION Institution Master File Edit

> 2 XUMF INSTITUTION Institution File Query / Update

> CHOOSE 1-2: 1 \<Enter\> XUMF FORUM INSTITUTION Institution Master File Edit

> Institution Master File Edit

> Enter Station Number:

> <span id="_Ref159823030" class="anchor"></span>Figure 3‑1. Initial dialogue when using the Institution Master File Edit option \[XUMF FORUM INSTITUTION\]

> As Figure 3‑1 shows, to add a new STATION NUMBER (#99) and its associated field values in the INSTITUTION file (#4) on FORUM, the user chose the XUMF FORUM INSTITUTION option (i.e., Institution Master File Edit) by entering "1" at the "CHOOSE 1-2:" prompt when given a list of XUMF options from which to choose.

> 4. Add/Update the specified fields for the file in question for the following scenarios.

- Adding a new INSTITUTION file (#4) Station Number and associated field values.
- Editing an existing INSTITUTION file (#4) Station Number and associated field values.
- Adding a new FACILITY TYPE file (#4.1) Facility Type and associated field values.
- Editing an existing FACILITY TYPE file (#4.1) Facility Type and associated field values.

> a. In the example in Figure 3‑2, the user chose to add a new STATION NUMBER (#99) and its associated fields to the INSTITUTION file (#4) on FORUM:

> Enter Station Number: 776

> Are you adding a new national entry? YES// \<Enter\>

> Enter Institution Name: OFFICE OF INFORMATION SRV CNTR

> NAME: OFFICE OF INFORMATION SRV CNTR Replace \<Enter\>

> STATION NUMBER: 776// \<Enter\>

> FACILITY TYPE: VAMC\<Enter\> VA MEDICAL CENTER

> OFFICIAL VA NAME: OFFICE OF INFORMATION SERVICE CENTER

> STATE: OHIO

> INACTIVE FACILITY FLAG: \<Enter\>

> Select ASSOCIATIONS: \<Enter\>

> Select EFFECTIVE DATE: \<Enter\>

> Are you ready to broadcast? YES// \<Enter\>

> ...broadcasting the Institution...

> Sent.

> Enter Station Number:

> <span id="_Ref159822615" class="anchor"></span>Figure 3‑2. Adding a new Station Number to the FORUM IMF

> As you can see in Figure 3‑1, the user entered a new Institution by entering values for the following fields (listed in the order of entry):

- STATION NUMBER (#99)—The user entered a new STATION NUMBER of "776" at the "Enter Station Number:" prompt.

> The user pressed the \<Enter\> key to accept the default of "YES" at the "Are you adding a new national entry? YES//" prompt.

- NAME (#.01)—The user entered a new NAME of "OFFICE OF INFORMATION SRV CNTR" that is associated with the new STATION NUMBER at the "Enter Institution Name:" prompt.

> The software echoed the NAME field value back to make sure the user had entered it correctly. To change the value at that point, the user would have entered any corrections at the "Replace" prompt. Since the entry was correct, the user pressed the \<Enter\> key at the "NAME: OFFICE OF INFORMATION SRV CNTR Replace" prompt to continue to the next field.

> The software then echoed the STATION NUMBER field value back to make sure the user had entered it correctly. Since the entry was correct, the user pressed the \<Enter\> key at the "STATION NUMBER: 776//" prompt to continue to the next field.

- FACILITY TYPE (#13)—The user entered "VAMC" as the FACILITY TYPE that is associated with the new STATION NUMBER at the "FACILITY TYPE:" prompt.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/077.png) | NOTE: The FACILITY TYPE field value entered *must* match a valid FACILITY TYPE entry in the FACILITY TYPE File (#4.1). |

- OFFICIAL VA NAME (#100)—The user entered a new OFFICIAL VA NAME of "OFFICE OF INFORMATION SERVICE CENTER" that is associated with the new STATION NUMBER at the "OFFICIAL VA NAME:" prompt.
- STATE (#.02)—The user entered "OHIO" as the STATE that is associated with the new STATION NUMBER at the "STATE:" prompt.
- INACTIVE FACILITY FLAG (#101)—Since the user did not want to enter an INACTIVE FACILITY FLAG, he/she pressed the \<Enter\> key at the "INACTIVE FACILITY FLAG:" prompt to continue to the next field.
- ASSOCIATIONS Multiple (#14)—Since the user did not want to enter any ASSOCIATIONS, he/she pressed the \<Enter\> key at the "Select ASSOCIATIONS:" prompt to continue to the next field.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/078.png)</td>
<td><p><strong>NOTE:</strong> The following are subfields in the ASSOCIATIONS Multiple field that can be edited using this option:</p>
<ul>
<li><blockquote>
<p>ASSOCIATIONS (#.01)</p>
</blockquote></li>
<li><blockquote>
<p>PARENT OF ASSOCIATION (#1)</p>
</blockquote></li>
</ul>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/079.png) <strong>NOTE:</strong> Kernel Patch XU*8.0*294 prevents the adding of a VISN or PARENT FACILITY association to an Institution entry that does not have a corresponding PARENT OF ASSOCIATION.<br />
<br />
Kernel Patch XU*8.0*335 pointed all child facilities to their administrative parents. The parent, or primary facility, points to its parent (HCS or VISN). The HCS entries point to a VISN entry. All parent relationships eventually resolve to a VISN.</p></td>
</tr>
</tbody>
</table>

- HISTORY Multiple (#999):
- EFFECTIVE DATE (#.01)—Since the user did not want to enter an EFFECTIVE DATE, he/she pressed the \<Enter\> key at the "Select EFFECTIVE DATE:" prompt to continue to the last step.

> Finally, after all of the entries were completed, the user was ready to broadcast the new Institution entries VHA-wide by pressing the \<Enter\> key to accept the default of "YES" at the "Are you ready to broadcast? YES//" prompt.

> The software displayed the following message:

> ...broadcasting the Institution...

> When the broadcast was complete, the following message was displayed:

> Sent.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/080.png) | NOTE: Additions and modifications of national entries in the Institution Master File (IMF) on FORUM are broadcast one at a time. |

> b. In the example in Figure 3‑3, the user chose to edit an existing STATION NUMBER (#99) and its associated field values in the INSTITUTION file on FORUM:

> Enter Station Number: 776

> NAME: OFFICE OF INFORMATION SRV CNTR Replace \<Enter\>

> STATION NUMBER: 776// \<Enter\>

> FACILITY TYPE: VAMC// \<Enter\>

> OFFICIAL VA NAME: OFFICE OF INFORMATION CENTER Replace CEN \<Enter\> With SERVICE CEN

> Replace \<Enter\>

> OFFICE OF INFORMATION SERVICE CENTER

> STATE: OHIO// ^

> Are you ready to broadcast? YES// \<Enter\>

> ...broadcasting the Institution...

> Sent.

> Enter Station Number:

> <span id="_Ref159822584" class="anchor"></span>Figure 3‑3. Editing an Existing Station Number in the FORUM IMF

> As you can see from the example shown in Figure 3‑3, the user wanted to modify the OFFICIAL VA NAME field (#100) value from "OFFICE OF INFORMATION CENTER" to "OFFICE OF INFORMATION SERVICE CENTER" for Station Number 776 that he/she had just entered in Step \#4a (see Figure 3‑2).

> After entering 776 at the "Enter Station Number:" prompt, the user pressed the \<Enter\> key until he/she arrived at the "OFFICIAL VA NAME: OFFICE OF INFORMATION CENTER Replace" prompt.

> To change only a portion of the name (i.e., "CENTER " to "SERVICE CENTER"), the user entered "CEN" at the "Replace" prompt and then entered "SERVICE CEN" at the "With" prompt.

> The software confirmed the change by redisplaying the newly modified OFFICIAL VA NAME field (#100). Since the modified name was correct, the user pressed the \<Enter\> key after the "Replace" prompt.

> The user didn't want to make any more changes, so he/she entered a caret ("^") at the "STATE: OHIO//" prompt.

> When all of the updates were completed, the user was ready to broadcast the updated Institution entries VHA-wide by pressing the \<Enter\> key to accept the default of "YES" at the "Are you ready to broadcast? YES//" prompt.

> The software displayed the following message:

> ...broadcasting the Institution...

> When the broadcast was complete, the following message was displayed:

> Sent.

|                                                                                                                |                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/081.png) | NOTE: Additions and modifications of national entries in the Institution Master File (IMF) on FORUM are broadcast one at a time. |

> 5. After an update is broadcasted, an HL7 MFN segment is generated. Figure 3‑4 shows an example of an HL7 MFN segment for a newly added Station Number (see Step \#4a):

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> DATE/TIME ENTERED: SEP 15, 2000@10:10:32

> SERVER APPLICATION: XUMF MFN TRANSMISSION TYPE: OUTGOING

> MESSAGE ID: 0126 PARENT MESSAGE: SEP 15, 2000@10:10:32

> PRIORITY: IMMEDIATE RELATED EVENT PROTOCOL: XUMF MFN

> MESSAGE TYPE: SINGLE MESSAGE

> MESSAGE TEXT:

> MFI^Z04^MFS^REP^20000915101032^20000915101032^NE

> MFE^MUP^^19000091^776~STATION NUMBER~D

> ZIN^OFFICE OF INFORMATION SRV CNTR^776^National^VAMC~FACILITY TYPE~VA^OFFICE OF

> INFORMATION SERVICE CENTER^^OHIO^^^^^^

> STATUS: SUCCESSFULLY COMPLETED

> DATE/TIME PROCESSED: SEP 15, 2000@10:10:36

> NO. OF CHARACTERS IN MESSAGE: 204 NO. OF EVENTS IN MESSAGE: 1

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> <span id="_Ref159823159" class="anchor"></span>Figure 3‑4. Sample HL7 MFN segment information

> A MailMan e-mail message is sent to the XUMF INSTITUTION mail group at all sites. Figure 3‑5 shows an example of the e-mail for a newly added Station Number (see Step \#4a):

> Subj: Master File Server - update notification - INSTITUTION file

> \[#56499\] 04 Aug 00 15:22 16 lines

> From: ADMINISTRATOR,ROGER In 'IN' basket. Page 1

> ----------------------------------------------------------------------------

> The following Master File Notification (MFN) message was

> received and processed by the Master File Server:

> MID: 037

> The following INSTITUTION (#4) file entry has been Updated:

> IEN: 7436

> NAME: OFFICE OF INFORMATION SRV CNTR

> OFFICIAL VA NAME: OFFICE OF INFORMATION SERVICE CENTER

> STATION NUMBER: VAMC

> 776

> OFFICE OF INFORMATION SRV CNTR

> OFFICE OF INFORMATION SERVICE CENTER

> Enter message action (in IN basket): Ignore//

> <span id="_Ref159823180" class="anchor"></span>Figure 3‑5. Sample INSTITUTION file update message sent to the XUMF INSTITUTION mail group

> 6. After all change notifications have been processed, log off of FORUM.

> 7. Return to Step \#1.

#### Troubleshooting

Another duty of the FORUM Institution Master File Administrators is to monitor and troubleshoot any problems with the Institution Master file (IMF) and Facility Type Master File (FMF) located at the sites and on FORUM. This includes troubleshooting of the Master File Server (MFS) software.

#### FORUM Step-By-Step Procedures—Troubleshooting

The following are the suggested step-by-step procedures for monitoring and troubleshooting the FORUM master files and the Master File Server (MFS) software:

> 1. Monitor the XUMF INSTITUTION and XUMF ERROR mail groups on FORUM—The FORUM Institution Master File Administrators should look for any error messages from sites that fail to successfully update their local master files.

> 2. Process any error messages sent to the XUMF INSTITUTION and XUMF ERROR mail groups on FORUM.

> a. Try to resend an unsent message to the site in question.

> b. If the problem persists, contact the Local Site Institution Master File Administrators at the site, discuss the problem, and devise a solution.

> c. After the problem has been resolved, contact the Local Site Institution Master File Administrators at the site to verify that the master file has been successfully updated.

> 3. Monitor any VistA HL7 error messages regarding transmission errors from FORUM to the sites.

> 4. Process any HL7-type error messages.

> a. Try to resend any unsent HL7 message.

> b. If the problem persists, contact the VistA HL7 Team for assistance and advise the Local Site Institution Master File Administrators at the site of the problem.

> c. After the problem has been resolved, contact the Local Site Institution Master File Administrators at the site to verify that the master file has been successfully updated.

> 5. Return to Step \#1.

# Developer's Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Developer's Guide section of this supplemental documentation for the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206).

The intended audience for this section is Information Resource Management (IRM). However, it can also be helpful to others in Technical Service, the Program Office, Enterprise VistA Support (EVS), and Application Structure and Integration Services (ASIS).

## Data Dictionary Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Institution File Data Dictionary Modifications

#### Modified/Added Fields in the INSTITUTION File (#4)

The following fields were modified or added to the INSTITUTION File (#4:

#### NAME (#.01)

Kernel Patch XU\*8.0\*206 modified the NAME field (#.01) to prevent *national* entries from being edited locally.

|                                                                                                                |                                                                                                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/082.png) | NOTE: Local entries can use the same name that is found in a national entry. However, sites should be aware that identical names in both a national and a local entry might cause confusion at the local level (e.g., when running local reports based on the Institution Name). |

#### STATE (#.02)

Kernel Patch XU\*8.0\*206 modified the STATE field (#.02) to prevent *national* entries from being edited locally. This field serves as a Write Identifier.

Kernel Patch XU\*8.0\*217 modified the STATE field (#.02) description in the INSTITUTION file (#4). It stores the State in which the institution is physically located.

#### STREET ADDR. 1 (#1.01)

Kernel Patch XU\*8.0\*217 modified the STREET ADDR. 1 field (#1.01) description in the INSTITUTION file (#4). This is the first line of the street address (*physical*) of the facility. The value *must* be 2-40 characters in length.

#### STREET ADDR. 2 (#1.02)

Kernel Patch XU\*8.0\*217 modified the STREET ADDR. 2 field (#1.02) description in the INSTITUTION file (#4). This is the second line of the street address (*physical*) of the facility. The value *must* be 2-40 characters in length.

#### CITY (#1.03)

Kernel Patch XU\*8.0\*217 modified the CITY field (#1.03) description in the INSTITUTION file (#4). It stores the City in which the facility is *physically* located. The value *must* be 2-40 characters in length.

#### ZIP (#1.04)

Kernel Patch XU\*8.0\*217 modified the ZIP field (#1.04) description in the INSTITUTION file (#4). It stores the postal ZIP code for the *physical* address of the facility (i.e., ZIP code or ZIP + 4).

#### ST. ADDR. 1 (MAILING) (#4.01)

Kernel Patch XU\*8.0\*217 added the ST. ADDR. 1 (MAILING) field (#4.01) to the INSTITUTION file (#4). This is the first line of the street address (*mailing*) of the facility. The value *must* be 2-40 characters in length.

#### ST. ADDR. 2 (MAILING) (#4.02)

Kernel Patch XU\*8.0\*217 added the ST. ADDR. 2 (MAILING) field (#4.02) to the INSTITUTION file (#4). This is the second line of the street address (*mailing*) of the facility. The value *must* be 2-40 characters in length.

#### CITY (MAILING) (#4.03)

Kernel Patch XU\*8.0\*217 added the CITY (MAILING) field (#4.03) to the INSTITUTION file (#4). It stores the City of the facility's *mailing* address. The value *must* be 2-40 characters in length.

#### STATE (MAILING) (#4.04)

Kernel Patch XU\*8.0\*217 added the STATE (MAILING) field (#4.04) to the INSTITUTION file (#4). It stores the State of the facility's *mailing* address. This field is a pointer to the STATE file (#5).

#### ZIP (MAILING) (#4.05)

Kernel Patch XU\*8.0\*217 added the ZIP (MAILING) field (#4.05) to the INSTITUTION file (#4). It stores the postal ZIP code for the *mailing* address of the facility (i.e., ZIP code or ZIP + 4).

#### STATUS (#11)

Kernel Patch XU\*8.0\*206 modified the STATUS field (#11). The Input Transform was modified to prevent setting of the STATUS field (#11) to National. Only the Cleanup Utilities of the local site's INSTITUTION file or the Master File Server (MFS) mechanism can flag *national* entries as "National." A site cannot create National entries or flag *local* entries as National. Also, since the INACTIVE FACILITY FLAG field (#101) flags Inactive entries, the current "INACTIVE" value for the STATUS field (#11) was removed from the SET OF CODES for this field. Another reason to remove INACTIVE from the SET OF CODES was due to the fact that an entry can be both INACTIVE and National (or Local for that matter). This field is required.

#### FACILITY TYPE (#13)

Kernel Patch XU\*8.0\*206 modified the FACILITY TYPE field (#13) to prevent *national* entries from being edited locally. This field serves as a Write Identifier.

Kernel Patch XU\*8.0\*335 (i.e., Health*e*Vet cleanup) added an Input Transform to the FACILITY TYPE field (#13) field in the INSTITUTION file (#4) to prevent the selection of non-standard facility types from "national" INSTITUTION file (#4) entries.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/083.png)</td>
<td><p><strong>NOTE:</strong> When updating the facility type of one of your facilities, if the facility type you need is not selectable and should be, send a MailMan message to the XUMF INSTITUTION mail group. Health Systems Implementation Training and Enterprise Support (HSITES) will review the request and make any necessary updates to the Master FACILITY TYPE file. This update will then be broadcast to all VistA instances.</p>
<p>The goal is to standardize both Institution and Facility Type data throughout the VHA. Please do <em>not</em> bypass the updating mechanism. Otherwise, it will defeat the standardization efforts, and cause your site to become out-of-sync with other medical centers. Subsequent patches and/or MFS updates will override these local modifications; this will invalidate the local measures and result in data synchronization issues between facilities and an endless cycle of updating and cleanups.</p></td>
</tr>
</tbody>
</table>

#### AGENCY CODE (#95)

Kernel Patch XU\*8.0\*261 added the AGENCY CODE field (#95) to the list of INSTITUTION file (#4) fields supported by the Master File Server (MFS) mechanism.

#### STATION NUMBER (#99)

Kernel Patch XU\*8.0\*206 modified the STATION NUMBER field (#99) to prevent it from being edited locally.

|                                                   |                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/084.png) | CAUTION: The STATION NUMBER field (#99) is reserved for *national* entries only! |

It is maintained by the Master File Server (MFS) mechanism. The Information Management Service (045A4) assigns Station Numbers (i.e., a three-digit number plus any modifiers). This field *must* be from 3 to 7 characters in length and *mustnot* contain an embedded caret ("^"). This field serves as a Write Identifier.

#### OFFICIAL VA NAME (#100)

Kernel Patch XU\*8.0\*206 renamed the OFFICAL VA NAME field (#100) to OFFICIAL VA NAME. It also modified this field to prevent *national* entries from being edited locally. In addition, the OFFICIAL VA NAME field (#100) was increased from a maximum of 30 characters of FREE TEXT to 80 characters. This is to allow for the longer, new health care system names.

#### INACTIVE FACILITY FLAG (#101)

Kernel Patch XU\*8.0\*206 modified the INACTIVE FACILITY FLAG field (#101) to prevent *national* entries from being edited locally. Also, the SET OF CODES for this field was changed from "Y" (YES) to "1" (INACTIVE). This field is used to help identify inactive entries during a file lookup. This field, along with the EFFECTIVE DATE (#.01) in the HISTORY Multiple (#999), also serves as a Write Identifier.

#### HISTORY Multiple Field (#999) in the INSTITUTION File (#4)

Kernel Patch XU\*8.0\*206 added the HISTORY Multiple field (#999) to the INSTITUTION file (#4). With site integrations, Name changes, Station Number deactivations/activations, legacy Station Numbers, and new facilities, a need to return Institution time-sensitive (i.e., historical) information was identified. This historical information is stored in the HISTORY Multiple field (#999).

The HISTORY Multiple field (#999) is composed of the following fields:

- EFFECTIVE DATE (#.01)  
  >   
  > The effective date related to the update (historical) event.
- NAME (CHANGED FROM) (#.02)  
  >   
  > If the event was a NAME change, then this field holds the Field \#.01 value *prior* to the edit that took place on the EFFECTIVE DATE (#.01, described previously).
- OFFICIAL VA NAME (CHANGED FROM) (#.03)  
  >   
  > If the event was an OFFICIAL VA NAME change, then this field holds the Field \#100 value *prior* to the edit that took place on the EFFECTIVE DATE (#.01, described previously).
- REALIGNED TO (#.05)  
  >   
  > If the facility was realigned due to integration, or some other reorganization, and a new STATION NUMBER (#99) was assigned, then this field holds a pointer to the INSTITUTION file entry with the *new* STATION NUMBER for this facility.
- REALIGNED FROM (#.06)  
  >   
  > If the facility was realigned due to integration, or some other reorganization, and a new STATION NUMBER (#99) was assigned, then this field holds a pointer to the INSTITUTION file entry with the *old* STATION NUMBER for this facility.
- DEACTIVATED FACILITY / STA \# (#.07)  
  >   
  > If the facility or STATION NUMBER (#99) was deactivated, then this flag is set to "1" for this EFFECTIVE DATE (#.01, described previously). A facility and/or STATION NUMBER can be deactivated and activated. An API uses this flag, together with the EFFECTIVE DATE (#.01, described previously), to determine the status of a facility/STATION NUMBER on a specific date.

|                                                                                                                |                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/085.png) | REF: For more information on the API, please refer to the "F4^XUAF4(): Institution Data for a Station Number" topic in Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

- ACTIVATED FACILITY (#.08)  
    
  If the facility or STATION NUMBER (#99) is new or was activated, then this flag is set (i.e., it is set to "1") for this EFFECTIVE DATE (#.01, described previously). A facility and/or STATION NUMBER can be deactivated and then activated. An API uses this flag, together with the EFFECTIVE DATE (#.01), to determine the status of a facility/STATION NUMBER on a specific date.

|                                                                                                                |                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/086.png) | REF: For more information on the API, please refer to the "F4^XUAF4(): Institution Data for a Station Number" topic in Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

#### IDENTIFIER (#9999)

Kernel Patch XU\*8.0\*218 added the IDENTIFIER Multiple field (#9999) to the INSTITUTION (#4) and FACILITY TYPE (#4.1) files.

|                                                                                                                |                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/087.png) | NOTE: Kernel Patch XU\*8.0\*261 modified the cross-references on this field. |

The IDENTIFIER Multiple field (#9999) is composed of the following fields:

- CODING SYSTEM (#.01)  
  >   
  > This is a Free Text field. The Coding System entered *must* be 2-20 characters in length (e.g., DMIS). To see existing coding systems in the file:

> \>D CDSYS^XUAF4(.Y)

- ID (#.02)  
  >   
  > This is a Free Text field. The ID entered *must* be 2-20 characters in length (e.g., 0037).

#### Write Identifiers

Four write identifiers are added with Kernel Patch XU\*8.0\*206, which replace the previous field identifiers. The XUMFPOST post-init routine deletes the previous field identifiers. The write identifiers are:

- STATE (#.02)
- FACILITY TYPE (#13)
- STATION NUMBER (#99)
- INACTIVE FACILITY FLAG (#101) with EFFECTIVE DATE (#.01 field of the HISTORY Multiple field \[#999\])

|                                                                                                                |                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/088.png) | REF: For more information on Write Identifiers, please refer to the "Write Identifiers" topic under the "Developer Tools" topic in the *VA FileMan Programmer Manual*. |

#### Obsolete Fields

The XUMFPOST post-init removes the following obsolete (asterisked) fields from the INSTITUTION file:

- \*OUTPUT HEADER (#.04)
- \*STATION NAME (#7)
- \*MAILMAN FLAG (#12)
- \*OLD AMIS NUMBER (#77)
- \*G&L HEADER (#10)
- \*PACKAGE X-REF (#30) subfile

#### Facility Type File Data Dictionary Modifications

#### Modified/Added Fields in the FACILITY TYPE File (#4.1)

The following fields were modified or added to the FACILITY TYPE File (#4.1):

#### STATUS (#3)

Kernel Patch XU\*8.0\*335 added the STATUS field (#3) to the FACILITY TYPE file (#4.1). It is a SET OF CODES field that consists of the following codes:

- "N"—Flags "National" entries.
- "L"—Flags "Local" entries.

## Application Program Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This topic lists and describes the Kernel callable routines provided by the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206). These calls are either Supported Reference Integration Agreements (IAs) or Controlled Subscription IAs.

- Supported References—Supported Reference APIs are open for use by any VistA application as defined by the IA. They have been recorded as a Supported Reference in the IA database on FORUM. It is not required that VistA application developers request an IA to use them.
- Controlled Subscription References—Controlled Subscription APIs contain attributes/functions that *must* be controlled in their use. They have been recorded as a Controlled subscription Reference in the IA database on FORUM. VistA application developers *must* request an IA to use them. Permission to use them is granted by the custodian package (i.e., Kernel) on a one-by-one basis.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/089.png)</td>
<td><strong>REF:</strong> For a list of the Integration Agreements (IAs) related to IFR-related software, please refer to the "<br />
Integration Agreements (IA)" topic in the "<br />
External Relations" topic in Chapter 6, "Implementation and Maintenance," in this manual.</td>
</tr>
</tbody>
</table>

The IFR APIs are listed alphabetically by Entry Point below.

#### \$\$ACTIVE^XUAF4(): Institution Active Facility (True/False)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function, given the Internal Entry Number (IEN) in the INSTITUTION file (#4), returns the Boolean value for the question—is this an active facility? It checks to see if the INACTIVE FACILITY FLAG field (#101) is <em>not</em> set.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$ACTIVE^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns a Boolean value:</p>
<ul>
<li><p>True (non-zero)—Station Number is an active facility.</p></li>
<li><p>False (zero)—Station Number is <em>not</em> an active facility. The INACTIVE FACILITY FLAG field (#101) has a value indicating it is inactive.</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### \$\$CIRN^XUAF4(): Institution CIRN-enabled Field Value

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the value of the CIRN-enabled field from the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$CIRN^XUAF4(inst[,value])</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>inst:</td>
<td><p>(required) Institution lookup value, any of the following:</p>
<ul>
<li><p>Internal Entry Number (IEN), will have the <strong>`</strong> in front of it.</p></li>
<li><p>Station Number</p></li>
<li><p>Station Name</p></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td>value:</td>
<td>(optional) Restricted to use by CIRN. This input parameter allows the setting of the field to a new value.</td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td>returns:</td>
<td>Returns the CIRN-enabled field value.</td>
</tr>
</tbody>
</table>

#### \$\$ID^XUAF4(): Institution Identifier

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the Identifier (ID) of an INSTITUTION file (#4) entry for a given Coding System and Internal Entry Number (IEN).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$ID^XUAF4(cdsys,ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>cdsys:</td>
<td><p>(required) CDSYS is an existing CODING SYSTEM field (#.01) in the IDENTIFIER Multiple field (#9999) of the INSTITUTION file (#4). To see existing coding systems in the file:</p>
<blockquote>
<p>&gt;<strong>D CDSYS^XUAF4(.Y)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td>returns:</td>
<td>Returns the INSTITUITION file (#4) Identifier (ID) associated with the given Coding System and IEN.</td>
</tr>
</tbody>
</table>

#### \$\$IDX^XUAF4(): Institution IEN (Using Coding System & ID)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the Internal Entry Number (IEN) of an INSTITUTION file (#4) entry for a given Coding System and Identifier (ID) pair.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$IDX^XUAF4(cdsys,id)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>cdsys:</td>
<td><p>(required) CDSYS is an existing CODING SYSTEM field (#.01) in the IDENTIFIER Multiple field (#9999) of the INSTITUTION file (#4). To see existing coding systems in the file:</p>
<blockquote>
<p>&gt;<strong>D CDSYS^XUAF4(.Y)</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td>id:</td>
<td>(required) ID is the ID field (#.02) in the IDENTIFIER Multiple field (#9999) of the INSTITUTION file (#4) that corresponds to the Coding System input (i.e., cdsys) as the first parameter.</td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td>returns:</td>
<td>Returns the INSTITUTION file (#4) Internal Entry Number (IEN) associated with the given coding system and Identifier (ID).</td>
</tr>
</tbody>
</table>

#### \$\$IEN^XUAF4(): IEN for Station Number

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the Internal Entry Number (IEN) of the entry for a given STATION NUMBER field (#99) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$IEN^XUAF4(sta)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>sta:</td>
<td>(required) Station Number.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns:</p>
<ul>
<li><p>IEN—Internal Entry Number.</p></li>
<li><p>NULL—Error.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Example

\>S X=\$\$IEN^XUAF4("528A5")

\>W X

532

#### \$\$IEN^XUMF(): Institution IEN (Using IFN, Coding System, & ID)

|                      |                                                                                                                                             |                                                                       |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                   |                                                                       |
| Category         | Institution File                                                                                                                            |                                                                       |
| IA \#            | 3795                                                                                                                                        |                                                                       |
| Description      | This extrinsic function returns the Internal Entry Number (IEN) for a given Internal File Number (IFN), Coding System, and Identifier (ID). |                                                                       |
| Format           | \$\$IEN^XUMF(ifn,cdsys,id)                                                                                                                  |                                                                       |
| Input Parameters | ifn:                                                                                                                                        | (required) Internal File Number (IFN).                                |
|                      | cdsys:                                                                                                                                      | (required) Coding System.                                             |
|                      | id:                                                                                                                                         | (required) Identifier.                                                |
| Output           | returns:                                                                                                                                    | Returns the Internal Entry Number (IEN) of the institution requested. |

#### \$\$LEGACY^XUAF4(): Institution Realigned/Legacy (True/False)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function, given the STATION NUMBER field (#99) in the INSTITUTION file (#4), returns the Boolean value for the question—has this station number been realigned? Is it a legacy Station Number?</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$LEGACY^XUAF4(sta)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>sta:</td>
<td>(required) The STATION NUMBER field (#99) value in the INSTITUTION file (#4) for the Station Number in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns a Boolean value:</p>
<ul>
<li><p>True (non-zero)—Station Number has been realigned; it is a legacy Station Number.</p></li>
<li><p>False (zero)—Station Number has <em>not</em> been realigned; it is <em>not</em> a legacy Station Number.</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### \$\$LKUP^XUAF4(): Institution Lookup

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the IEN or zero when doing a lookup on the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$LKUP^XUAF4(inst)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>inst:</td>
<td><p>(required) Institution lookup value, any of the following:</p>
<ul>
<li><p>Internal Entry Number (IEN), will have the <strong>`</strong> in front of it.</p></li>
<li><p>Station Number</p></li>
<li><p>Station Name</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns:</p>
<ul>
<li><p>IEN—Internal Entry Number.</p></li>
<li><p>Zero (0).</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### \$\$MADD^XUAF4(): Institution Mailing Address

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the mailing address information for an institution in a caret-delimited string (i.e., streetaddr^city^state^zip) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$MADD^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the institution mailing address in a caret-delimited string:</p>
<blockquote>
<p>streetaddr^city^state^zip</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### \$\$NAME^XUAF4(): Institution Official Name

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the OFFICIAL NAME field (#100) value in the INSTITUTION file (#4) for an institution given its Internal Entry Number (IEN). However, If Field #100 is null, the NAME field (#.01) in the INSTITUTION file (#4) is returned.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$NAME^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns either of the following:</p>
<ul>
<li><p>OFFICIAL NAME field (#100) value in the INSTITUTION file (#4)—If Field #100 is <em>not</em> null.</p></li>
<li><p>NAME field (#.01) value in the INSTITUTION file (#4)—If Field #100 is null.</p></li>
</ul></td>
</tr>
</tbody>
</table>

#### \$\$NNT^XUAF4(): Institution Station Number, Name, and Type

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the station information for an institution in a caret-delimited string (i.e., station_number^station_name^station_type) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$NNT^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the institution station information in a caret-delimited string:</p>
<blockquote>
<p>station_number^station_name^station_type</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### \$\$NS^XUAF4(): Institution Name and Station Number

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the institution information in a caret-delimited string (i.e., institution_name^station_number) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$NS^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the institution information in a caret-delimited string:</p>
<blockquote>
<p>institution_name^station_number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### \$\$O99^XUAF4(): IEN of Merged Station Number

|                      |                                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                                                                                                                                                                                                                                                                          |                                                                                                                                                                                                                                |
| Category         | Institution File                                                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                                                                                                |
| IA \#            | 2171                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                                                                                                                                                                |
| Description      | This extrinsic function returns the Internal Entry Number (IEN) of the valid STATION NUMBER in the INSTITUTION file (#4), if this entry was merged during the INSTITUTION file (#4) cleanup process (e.g., due to a duplicate STATION NUMBER field \[#99\]). This function may be used by application developers to re-point their INSTITUTION file (#4) references to a valid entry complete with Station Number. |                                                                                                                                                                                                                                |
| Format           | \$\$O99^XUAF4(ien)                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                |
| Input Parameters | ien:                                                                                                                                                                                                                                                                                                                                                                                                               | (required) Internal Entry Number (IEN) of the institution in question.                                                                                                                                                         |
| Output           | returns:                                                                                                                                                                                                                                                                                                                                                                                                           | Returns the Internal Entry Number (IEN) of the INSTITUTION file (#4) entry with a valid STATION NUMBER field (#99)—the Station Number deleted from the input IEN during the cleanup process (i.e., Kernel Patch XU\*8.0\*206). |

Example

\>S NEWIEN=\$\$O99^XUAF4(6538)

\>W NEWIEN

6164

\>W ^DIC(4,6164,99)

519HB^^^

#### \$\$PADD^XUAF4(): Institution Physical Address

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the physical address information for an institution in a caret-delimited string (streetaddr^city^state^zip) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$PADD^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the institution physical address in a caret-delimited string:</p>
<blockquote>
<p>streetaddr^city^state^zip</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### \$\$PRNT^XUAF4(): Institution Parent Facility

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the parent facility institution information in a caret-delimited string (ien^station_number^name) for a given child facility STATION NUMBER field (#99) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$PRNT^XUAF4(sta)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>sta:</td>
<td>(required) The STATION NUMBER field (#99) value in the INSTITUTION file (#4) for the child facility whose parent facility information is being requested.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the parent facility institution information in a caret-delimited string:</p>
<blockquote>
<p>ien^station_number^name</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### \$\$RF^XUAF4(): Realigned From Institution Information

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the information that is pointed to in the REALIGNED FROM field (#.06) in the HISTORY Multiple field (#999) in a caret-delimited string (ien^station_number^effective_date) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$RF^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the realigned from institution information in a caret-delimited string:</p>
<blockquote>
<p>ien^station_number^effective_date</p>
</blockquote></td>
</tr>
</tbody>
</table>

Example

\>S IEN=\$\$RF^XUAF4(7020)

\>W IEN

500^500^3000701

#### \$\$RT^XUAF4(): Realigned To Institution Information

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function returns the information that is pointed to in the REALIGNED TO field (#.05) in the HISTORY Multiple field (#999) in a caret-delimited string (ien^station_number^effective_date) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$RT^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the realigned to institution information in a caret-delimited string:</p>
<blockquote>
<p>ien^station_number^effective_date</p>
</blockquote></td>
</tr>
</tbody>
</table>

Example

\>S IEN=\$\$RT^XUAF4(500)

\>W IEN

7020^528A8^3000701

#### \$\$STA^XUAF4(): Station Number for IEN

|                      |                                                                                                                                             |                                                                        |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                   |                                                                        |
| Category         | Institution File                                                                                                                            |                                                                        |
| IA \#            | 2171                                                                                                                                        |                                                                        |
| Description      | This extrinsic function returns the STATION NUMBER (#99) for the entry of a given Internal Entry Number (IEN) in the INSTITUTION file (#4). |                                                                        |
| Format           | \$\$STA^XUAF4(ien)                                                                                                                          |                                                                        |
| Input Parameters | ien:                                                                                                                                        | (required) Internal Entry Number (IEN) of the institution in question. |
| Output           | returns:                                                                                                                                    | Returns the Station Number.                                            |

Example

\>S STA=\$\$STA^XUAF4(7020)

\>W STA

528A8

#### \$\$TF^XUAF4(): Treating Facility (True/False)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This extrinsic function, given the Internal Entry Number (IEN) in the INSTITUTION file (#4), returns the Boolean value for the question—is this a medical treating facility?</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">$$TF^XUAF4(ien)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>ien:</td>
<td>(required) Internal Entry Number (IEN) of the institution in question.</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns a Boolean value:</p>
<ul>
<li><blockquote>
<p>True (non-zero)—Treating facility.</p>
</blockquote></li>
<li><blockquote>
<p>False (zero)—Not a Treating facility.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

Example

\>S TF=\$\$TF^XUAF4(7020)

\>W TF

1

#### \$\$WHAT^XUAF4(): Institution Single Field Information

|                      |                                                                                                                                                                   |                                                                                                                    |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                         |                                                                                                                    |
| Category         | Institution File                                                                                                                                                  |                                                                                                                    |
| IA \#            | 2171                                                                                                                                                              |                                                                                                                    |
| Description      | This extrinsic function returns the data from a single field given the Internal Entry Number (IEN) and the specific field requested in the INSTITUTION file (#4). |                                                                                                                    |
| Format           | \$\$WHAT^XUAF4(ien,field)                                                                                                                                         |                                                                                                                    |
| Input Parameters | ien:                                                                                                                                                              | (required) Internal Entry Number (IEN) of the institution in question (pointer value to the INSTITUTION file (#4). |
|                      | field:                                                                                                                                                            | (required) field number of the field in question.                                                                  |
| Output           | returns:                                                                                                                                                          | Returns the value in the specified field.                                                                          |

#### CDSYS^XUAF4(): Coding System Name

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 15%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This API returns the Coding System name.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">CDSYS^XUAF4(y)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>y:</td>
<td><p>(required) Pass by reference, returns:</p>
<blockquote>
<p>Y(coding_system) =<br />
$D_of_local_system^ coding_system name</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><strong>Output Parameters</strong></td>
<td>y:</td>
<td><p>Passed by reference, returns:</p>
<blockquote>
<p>Y(coding_system) =<br />
$D_of_local_system^ coding_system name</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### CHILDREN^XUAF4(): List of Child Institutions for a Parent

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td>Description</td>
<td colspan="2">This API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the "parent" input parameter.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">CHILDREN^XUAF4(array,parent)</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>array</td>
<td>(required) $NAME reference to store the list of institutions that make up the parent VISN institution for the "parent" input parameter.</td>
</tr>
<tr class="odd">
<td></td>
<td>parent</td>
<td><p>(required) Parent (VISN) institution lookup value, any of the following:</p>
<ul>
<li><p>Internal Entry Number (IEN), will have the <strong>`</strong> in front of it.</p></li>
<li><p>Station Number</p></li>
<li><p>Station Name</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the array populated with the list of institutions that make up the parent VISN.</p>
<blockquote>
<p>Variable array ("c",ien)=station_name^station_number</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### F4^XUAF4(): Institution Data for a Station Number

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 31%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This API returns the Internal Entry Number (IEN) and other institution data, including historical information, for a given STATION NUMBER (#99) in the INSTITUTION file (#4).</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">F4^XUAF4(sta,[.]array[,flag][,date])</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>sta:</td>
<td>(required) Station Number.</td>
</tr>
<tr class="odd">
<td></td>
<td>[.]array:</td>
<td>(required) $NAME reference for return values.</td>
</tr>
<tr class="even">
<td></td>
<td>flag:</td>
<td><p>(optional) Flags that represent the Station Number Status. Possible values are:</p>
<ul>
<li><p>A—Active entries only.</p></li>
<li><p>M—Medical treating facilities only.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td>date:</td>
<td>(optional) Return name on this VA FileMan internal date.</td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td>array</td>
<td>IEN or "0^error message"</td>
</tr>
<tr class="odd">
<td></td>
<td>array("NAME")</td>
<td>Name</td>
</tr>
<tr class="even">
<td></td>
<td>array("VA NAME")</td>
<td>Official VA Name</td>
</tr>
<tr class="odd">
<td></td>
<td>array("STATION NUMBER")</td>
<td>Station Number</td>
</tr>
<tr class="even">
<td></td>
<td>array("TYPE")</td>
<td>Facility Type Name</td>
</tr>
<tr class="odd">
<td></td>
<td>array("INACTIVE")</td>
<td><p>Inactive Date (0=not inactive)</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/090.png) <strong>NOTE:</strong> If inactive date <em>not</em> available, then 1.</p></td>
</tr>
<tr class="even">
<td></td>
<td>array("REALIGNED TO")</td>
<td>IEN^station number^date</td>
</tr>
<tr class="odd">
<td></td>
<td>array("REALIGNED FROM")</td>
<td>IEN^station number^date</td>
</tr>
<tr class="even">
<td></td>
<td>array("MERGE",IEN")</td>
<td>Merged Records</td>
</tr>
</tbody>
</table>

Example

\>D F4^XUAF4("528A8",.ARRAY)

\>ZW ARRAY

ARRAY=7020

ARRAY("INACTIVE")=0

ARRAY("NAME")=ALBANY

ARRAY("REALIGNED FROM")=500^500^3000701

ARRAY("STATION NUMBER")=528A8

ARRAY("TYPE")=VAMC

ARRAY("VA NAME")=VA HEALTHCARE NETWORK UPSTATE NEW YORK SYSTEM VISN 2 - ALBANY DIVISION

#### LOOKUP^XUAF4(): Lookup Institution Identifier

|                      |                                                                                                                                                                                                                                                                                                                       |                                                                                                                                                                                                                                 |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                 |
| Category         | Institution File                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                 |
| IA \#            | 2171                                                                                                                                                                                                                                                                                                                  |                                                                                                                                                                                                                                 |
| Description      | This API lookup utility allows a user to select an Institution by Coding System and ID. It prompts a user for a Coding System and then prompts for an Identifier—it's an IX^DIC API call on a New Style cross-reference of the ID field (#.02) of the IDENTIFIER Multiple field (#9999) of the INSTITUTION file (#4). |                                                                                                                                                                                                                                 |
| Format           | LOOKUP^XUAF4()                                                                                                                                                                                                                                                                                                        |                                                                                                                                                                                                                                 |
| Input Parameters |                                                                                                                                                                                                                                                                                                                       | ![](ifr-xu-8-206-416-supplement-to-patch-description/091.png) REF: For input information, please refer to the IX^DIC documentation in the *VA FileMan Programmer Manual*.  |
| Output           |                                                                                                                                                                                                                                                                                                                       | ![](ifr-xu-8-206-416-supplement-to-patch-description/092.png) REF: For output information, please refer to the IX^DIC documentation in the *VA FileMan Programmer Manual*. |

Example

Select INSTITUTION CODING SYSTEM: DMIS

ID: 0037

DMIS 0037 WALTER REED DC USAH 688CN

#### MAIN^XUMFI(): HL7 Master File Message Builder

|                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                             |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Reference Type             | Controlled Subscription                                                                                                                                                                                                                                                                                                                                                                                                                              |                                                                                                                                                                                                                                                             |
| Category                   | Institution File                                                                                                                                                                                                                                                                                                                                                                                                                                     |                                                                                                                                                                                                                                                             |
| IA \#                      | 2171                                                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                             |
| Description                | This API implements an HL7 Master File Message Builder Interface that dynamically maps a VA FileMan field to an HL7 Master File sequence within a segment. The interface implements functionality to build Master File Notification (MFN), Master File Query (MFQ), and Master File Response (MFR) segments. The interface calls applicable VISTA HL7 GENERATE and GENACK interfaces to send/reply/broadcast an appropriate HL7 Master File message. |                                                                                                                                                                                                                                                             |
| Format                     | MAIN^XUMFI(ifn,ien,type,param,error)                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                                                                                                                                             |
| Input Parameters           |                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ![](ifr-xu-8-206-416-supplement-to-patch-description/093.png) REF: For a description of the Input parameters for this API, please refer to the "MAIN^XUMFP(): Master File Parameters" API.             |
| Output Parameters & Output |                                                                                                                                                                                                                                                                                                                                                                                                                                                      | ![](ifr-xu-8-206-416-supplement-to-patch-description/094.png) REF: For a description of the Output Parameters and Output for this API, please refer to the "MAIN^XUMFP(): Master File Parameters" API. |

Details

This interface should be called after the Master File Parameter API. The Master File Parameter API sets up the required parameters in the PARAM array.

The Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) implements several Application Programmer Interfaces (APIs). After the IFR patch has been installed and the Cleanup performed, the STATION NUMBER field (#99) will be a unique key to the INSTITUTION file (#4).

Example

\>D MAIN^XUMFI(4,18723,1,.PARAM,.ERROR)

From the HL7 MESSAGE TEXT file (#772), you would see the following:

DATE/TIME ENTERED: JAN 12, 2001@09:17:29

SERVER APPLICATION: XUMF MFN TRANSMISSION TYPE: OUTGOING

MESSAGE ID: 0259 PARENT MESSAGE: JAN 12, 2001@09:17:29

PRIORITY: DEFERRED RELATED EVENT PROTOCOL: XUMF MFN

MESSAGE TYPE: SINGLE MESSAGE

MESSAGE TEXT:  

MFI^Z04^MFS^REP^20010112091729^20010112091729^NE

MFE^MUP^^19001011^631GD~STATION NUMBER~D

ZIN^GREENFIELD^631GD^National^CBOC~FACILITY TYPE~VA^^^MASSACHUSETTS^^^^^^

STATUS: SUCCESSFULLY COMPLETED

DATE/TIME PROCESSED: JAN 12, 2001@09:17:29

NO. OF CHARACTERS IN MESSAGE: 161     NO. OF EVENTS IN MESSAGE: 1

#### MAIN^XUMFP(): Master File Parameters

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 0%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 51%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="4">Controlled Subscription</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="4">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="4">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="4"><p>This API sets up required parameters used by the HL7 Master File Message Builder Interface and the HL7 Master File message handler. The interface defines required parameters and serves as a common interface for parameter initialization. This interface is the enabling component of the Master File Server (MFS) mechanism that allows the server to maintain VA FileMan Master Files, including files with multiple fields and extended references.</p>
<p>The programmer may set any PARAM parameter before or after the interface call and override the default value.</p></td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="4">MAIN^XUMFP(ifn,ien,type,param,error)</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Input Parameters</strong></td>
<td>ifn:</td>
<td colspan="2">(required) Internal File Number (IFN).</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td>ien:</td>
<td colspan="2"><p>(required) Internal Entry Number (IEN).</p>
<p>Single entry (pass by value).</p>
<p>Example:</p>
<ul>
<li><p>IEN=1</p></li>
</ul>
<p>Multiple entries (pass by reference).</p>
<p>Example:</p>
<ul>
<li><blockquote>
<p>IEN(1)=""</p>
</blockquote></li>
<li><p>IEN(2)=""</p></li>
</ul>
<p>ALL national entries (pass by value).</p>
<p>Example:</p>
<ul>
<li><p>IEN="ALL"</p></li>
</ul></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td>type:</td>
<td colspan="2"><p>(required) Message TYPE. Possible values are:</p>
<blockquote>
<p>0—MFN: Unsolicited update.</p>
<p>1—MFQ: Query particular record and file.</p>
<p>3—MFQ: Query particular record in array.</p>
<p>5—MFQ: Query group records file.</p>
<p>7—MFQ: Query group records array.</p>
<p>11—MFR: Query response particular record file.</p>
<p>13—MFR: Query response particular record array.</p>
<p>15—MFR: Query response group records file.</p>
<p>17—MFR: Query response group records array.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><strong>Output Parameters</strong></td>
<td colspan="2">param("PROTOCOL")</td>
<td>IEN Protocol file (#101).</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2">param("BROADCAST")</td>
<td>Broadcast message to all VistA sites.</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2">param("LLNK")</td>
<td>Logical link in HLL("LINKS",n) format.</td>
</tr>
<tr class="even">
<td colspan="2"><strong>Output</strong></td>
<td colspan="2">error</td>
<td>1^Error message text</td>
</tr>
</tbody>
</table>

Details

| <u>QRD -- Query definition</u> | <u>HL7 Sequence</u>         | <u>HL7 Data Type</u> |
|--------------------------------|-----------------------------|----------------------|
| param("QDT")                   | Query Date/Time             | TS                   |
| param("QFC")                   | Query Format Code           | ID                   |
| param("QP")                    | Query Priority              | ID                   |
| param("QID")                   | Query ID                    | ST                   |
| param("DRT")                   | Deferred Response Type      | ID                   |
| param("DRDT")                  | Deferred Response Date/Time | TS                   |
| param("QLR")                   | Quantity Limited Request    | CQ                   |
| param("WHO")                   | Who Subject Filter          | XCN                  |
| param("WHAT")                  | What Subject Filter         | CE                   |
| param("WDDC")                  | What Department Data Code   | CE                   |
| param("WDCVQ")                 | What Data Code Value Qual   | CM                   |
| param("QRL")                   | Query Results Level         | ID                   |

| <u>XCN data type of QRD WHO parameter</u> |       |                                                             |
|-------------------------------------------|-------|-------------------------------------------------------------|
| 1<sup>ST</sup> component                  |       | One of the following:                                       |
| NAME                                      |       | Value of NAME field (#.01) for Internal Entry Number (IEN). |
| ALL                                       |       | String represents all national entries.                     |
| IEN ARRAY                                 |       | String represents entries passed in IEN array.              |
| 9<sup>th</sup> component                  | D     | Source table (VA FileMan cross-reference).                  |
| 10<sup>th</sup> component                 | 045A4 | Assigning authority.                                        |

| <u>CE data type of QRD WHAT parameter</u> |       |                       |
|-------------------------------------------|-------|-----------------------|
| 1<sup>ST</sup> component                  | 4     | Identifier            |
| 2<sup>nd</sup> component                  | IFN   | Text                  |
| 3<sup>rd</sup> component                  | VA FM | Name of Coding System |

| <u>MFI—Master File Identification</u> |                                    |
|---------------------------------------|------------------------------------|
| PARAM("MFI")                          | Master File Identifier             |
| PARAM("MFAI")                         | Master File Application Identifier |
| PARAM("FLEC")                         | File-Level Event Code              |
| PARAM("ENDT")                         | Entered Data/Time                  |
| PARAM("MFIEDT")                       | Effective Date/Time                |
| PARAM("RLC")                          | Response Level Code                |

| <u>MFE—Master File Entry</u> |                         |
|------------------------------|-------------------------|
| PARAM("RLEC")                | Record-Level Event Code |
| PARAM("MFNCID")              | MFN Control ID          |
| PARAM("MFEEDT")              | Effective Date/Time     |
| PARAM("PKV")                 | Primary Key Value       |

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><u>[Z...] segment(s) parameters</u></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARAM("SEG",SEG)=""</td>
<td>HL7 segment name</td>
</tr>
<tr class="even">
<td>PARAM("SEG",SEG,"SEQ",SEQ,FLD#)</td>
<td>segment sequence # and field</td>
</tr>
<tr class="odd">
<td colspan="2"><p>![](ifr-xu-8-206-416-supplement-to-patch-description/095.png) <strong>NOTE:</strong> If any special processing is required, in addition to the external value passed by VA FileMan, set the FLD# node equal to a formatting function "n^$$TAG^RTN(X)".</p>
<ul>
<li><blockquote>
<p>"<strong>n</strong>" being the component sequence number.</p>
</blockquote></li>
<li><blockquote>
<p>"<strong>X</strong>" representing the external value from VA FileMan.</p>
</blockquote></li>
</ul>
<p>$P(segment_sequence,HLCS,n)=FM_external_value.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><u>Files involving sub-records and/or extended reference</u></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PARAM("SEG",SEG,"SEQ",SEQ,"FILE")</td>
<td>See VA FileMan documentation.</td>
</tr>
<tr class="even">
<td>PARAM("SEG",SEG,"SEQ",SEQ,"IENS")</td>
<td>$$GET1^DIQ() for value.</td>
</tr>
<tr class="odd">
<td>PARAM("SEG",SEG,"SEQ",SEQ,"FIELD")</td>
<td>of FILE, IENS, &amp; FIELD.</td>
</tr>
<tr class="even">
<td>PARAM("SEG",SEG,"SEQ",SEQ,"KEY")</td>
<td>.01 value.</td>
</tr>
<tr class="odd">
<td>PARAM("SEG",SEG,"SEQ",SEQ,"FORMAT")</td>
<td>format non ST data types.</td>
</tr>
<tr class="even">
<td colspan="2">![](ifr-xu-8-206-416-supplement-to-patch-description/096.png) <strong>NOTE:</strong> Query group records store PARAM in the ^TMP global with the following root: ^TMP("XUMF MFS",$J,"PARAM",IEN).<br />
<br />
Example: MFE PKV node is ^TMP("XUMF MFS",$J,"PARAM",IEN,"PKV")</td>
</tr>
</tbody>
</table>

Example

The following example is a query (MFQ) for a group records array:

\>D MAIN^XUMFP(4,"ALL",7,.PARAM,.ERROR)

Since query group records store PARAM in the ^TMP global, display the ^TMP global to see the PARAM values:

\>D ^%G

Global ^TMP("XUMF MFS",\$J

TMP("XUMF MFS",\$J

^TMP("XUMF MFS",539017563,"PARAM","DRDT") =

^TMP("XUMF MFS",539017563,"PARAM","DRT") =

^TMP("XUMF MFS",539017563,"PARAM","ENDT") =

^TMP("XUMF MFS",539017563,"PARAM","FLEC") = UPD

^TMP("XUMF MFS",539017563,"PARAM","MFAI") =

^TMP("XUMF MFS",539017563,"PARAM","MFEEDT") = 20010212110654

^TMP("XUMF MFS",539017563,"PARAM","MFI") = Z04

^TMP("XUMF MFS",539017563,"PARAM","MFIEDT") =

^TMP("XUMF MFS",539017563,"PARAM","MFNCID") =

^TMP("XUMF MFS",539017563,"PARAM","POST") = POST^XUMFP4C

^TMP("XUMF MFS",539017563,"PARAM","PRE") = PRE^XUMFP4C

^TMP("XUMF MFS",539017563,"PARAM","PROTOCOL") = 2233

^TMP("XUMF MFS",539017563,"PARAM","QDT") = 20010212110654

^TMP("XUMF MFS",539017563,"PARAM","QFC") = R

^TMP("XUMF MFS",539017563,"PARAM","QID") = Z04 ARRAY

^TMP("XUMF MFS",539017563,"PARAM","QLR") = RD~999

^TMP("XUMF MFS",539017563,"PARAM","QP") = I

^TMP("XUMF MFS",539017563,"PARAM","QRL") =

^TMP("XUMF MFS",539017563,"PARAM","RLC") = NE

^TMP("XUMF MFS",539017563,"PARAM","RLEC") = MUP

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",1,.01) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",2,99) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",3,11) = ID

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",4,13) = CE^~FACILITY TYPE~VA

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",5,100) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",6,101) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",7,.02) = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"DTYP") = CE^~VISN~VA

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"FIELD") = 1

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"FILE") = 4.014

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",8,"IENS") = 1,?+1,

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"DTYP") = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"FIELD") = 1:99

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"FILE") = 4.014

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",9,"IENS") = 2,?+1,

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",10,"DTYP") = DT

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",10,"FIELD") = .01

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",10,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",11,"DTYP") = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",11,"FIELD") = .06:99

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",11,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",12,"DTYP") = DT

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",12,"FIELD") = .01

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",12,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",13,"DTYP") = ST

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",13,"FIELD") = .05:99

^TMP("XUMF MFS",539017563,"PARAM","SEG","ZIN","SEQ",13,"FILE") = 4.999

^TMP("XUMF MFS",539017563,"PARAM","SEGMENT") = ZIN

^TMP("XUMF MFS",539017563,"PARAM","WDCVQ") =

^TMP("XUMF MFS",539017563,"PARAM","WDDC") = INFRASTRUCTURE~INFORMATION INFRASTRUCTURE ~VA TS

^TMP("XUMF MFS",539017563,"PARAM","WHAT") = 4~IFN~VA FM

^TMP("XUMF MFS",539017563,"PARAM","WHO") = ALL\~\~\~\~\~\~\~~D~045A4

#### PARENT^XUAF4(): Parent Institution Lookup

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the "lookup" input parameter.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">PARENT^XUAF4(array,lookup[,type])</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>array:</td>
<td>(required) $NAME reference to store the list of the parent (VISN) institution for the "lookup" input parameter institution.</td>
</tr>
<tr class="odd">
<td></td>
<td>lookup:</td>
<td><p>(required) Parent (VISN) institution lookup value, any of the following:</p>
<ul>
<li><p>Internal Entry Number (IEN), will have the <strong>`</strong> in front of it.</p></li>
<li><p>Station Number</p></li>
<li><p>Station Name</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td>type:</td>
<td>(optional) Type of institution from the INSTITUTION ASSOCIATION TYPES file (#4.05, default is VISN).</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the array populated with the list of parent (VISN) institutions.</p>
<blockquote>
<p>Variable array ("P",PIEN)=STATION_NAME^STATION_NUMBER</p>
</blockquote>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/097.png) <strong>NOTE:</strong> With the business rule that institutions can have only one parent per type, if you specify the input parameter type, you will get an array that will have only one PIEN in it. If the type parameter is left blank, it finds all parents for the institution and lists them in the array.</p></td>
</tr>
</tbody>
</table>

#### SIBLING^XUAF4(): Sibling Institution Lookup

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 15%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Reference Type</strong></td>
<td colspan="2">Supported</td>
</tr>
<tr class="even">
<td><strong>Category</strong></td>
<td colspan="2">Institution File</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2">2171</td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2">This API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the "child" input parameter.</td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">SIBLING^XUAF4(array,child[,type])</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>array:</td>
<td>(required) $NAME reference to store the list of all institutions of a parent (VISN) institution for the "child" input parameter institution.</td>
</tr>
<tr class="odd">
<td></td>
<td>child:</td>
<td><p>(required) Child institution lookup value, any of the following:</p>
<ul>
<li><p>Internal Entry Number (IEN), will have the <strong>`</strong> in front of it.</p></li>
<li><p>Station Number</p></li>
<li><p>Station Name</p></li>
</ul></td>
</tr>
<tr class="even">
<td></td>
<td>type:</td>
<td>(optional) Type of institution from the INSTITUTION ASSOCIATION TYPES file (#4.05, default is VISN).</td>
</tr>
<tr class="odd">
<td><strong>Output</strong></td>
<td>returns:</td>
<td><p>Returns the array populated with the list of all institutions of the parent (VISN) institution.</p>
<blockquote>
<p>Variable array<br />
("P",PIEN, "C",CIEN)=STATION_NAME^STATION_NUMBER</p>
</blockquote>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/098.png) <strong>NOTE:</strong> With the business rule that institutions can have only one parent per type, if you specify the input parameter type, you will get an array that will have only one PIEN in it. If the type parameter is left blank, it finds all parents for the institution and lists them in the array. Also, the input site (i.e., "child" input parameter) is included in the list.</p></td>
</tr>
</tbody>
</table>

# Systems Management Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is the Systems Management Guide section of this supplemental documentation for the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206). It details the technical-related IFR documentation (e.g., implementation and maintenance of IFR, routines, files, options, interfaces, product security, etc.)

The intended audience for this section is Information Resource Management (IRM). However, it can also be helpful to others in Technical Service, the Program Office, Enterprise VistA Support (EVS), and Application Structure and Integration Services (ASIS).

## Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel Patch XU\*8.0\*206 is a Kernel Installation and Distribution System (KIDS) software release.

#### Implementation

#### Installation Instructions

Kernel Patch XU\*8.0\*206 can be installed at any time. The installation time should not take more than two minutes. The actual cleanup of the local site's INSTALLATION file (#4), using the List Manager utilities, takes additional time.

|                                                                                                                |                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/099.png) | REF: For specific software requirements and the minimum VistA software and patches that are required with the IFR-relate software, please refer to the "Software Requirements" topic under the "External Relations" topic in this chapter. |

Since the INSTITUTION file (#4) is a standard file referenced by many software applications, we recommend that cleanup be performed with as few users on the system as possible; this includes running the Auto update with national data (AUTO) and Delete local/dup. station \# (DSTA) List Manager actions. The other actions (lists) can be run at any time. Resolving any duplicate entries is interactive and varies from site to site. The Auto update with national data (AUTO) List Manager action should take from 5 to 10 minutes.

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/100.png) | NOTE: The cleanup code queries the Master File Server (MFS) on FORUM to get a copy of the Institution Master File (IMF). The VistA HL7 software checks to determine whether a message is intended for production or training. The FORUM server's HL7 site parameter is set to "production," so attempting to install this patch in a test account with the site parameter set to "training" results in a response message containing an "Application Reject" due to "Processing ID Mismatch with Site Parameters." |

*Before* installing Kernel Patch XU\*8.0\*206, make copies of the INSTITUTION (#4) and FACILITY TYPE (#4.1) files.

To save copies of the INSTITUTION (#4) and FACILITY TYPE (#4.1) files for backup purposes, depending on your operating system, the site does the following:

- DSM—Use ^%GTO
- Caché—Use %GO)

The following is an example:

VAH\>D ^%GTO

This routine saves globals to be restored by %GTI

Output Device ? \> DIC4.GBL

Header comment... INSTITUTION (#4) file backup

global(s) ? \> ^DIC(4

global(s) ? \> ^DIC(4.1

global(s) ? \> ^

Global(s) Selected:

^DIC(4)

Output started for ^DIC at 8:19:50 AM

Global transfer finished at 8:19:51 AM

VAH\>

> <span id="_Toc159835445" class="anchor"></span>Figure 6‑1. Sample backup of the INSTALLATION and FACILITY TYPE files at a DSM site

To restore the backup copy in the event of some unforeseen problem (e.g., the site decides it needs to back out of the cleanup process), the site can do the following:

> 1. KILL ^DIC(4),^DIC(4.1

> 2. Depending on your operating system, the site does one of the following:

- DSM—DO ^%GTI
- Caché—DO ^%GI

This restores the data to its original state.

The Installation process includes the following steps/tips:

> 1. Users ARE allowed to be on the system during the installation.

> 2.DSM/AXP Sites—Kernel patch routines are *not* usually mapped, so you probably do *not* have to disable mapping.

> 3. You DO NOT need to stop TaskMan OR the background filers.

> 4. Use the INSTALL/CHECK MESSAGE option on the PackMan menu to load the patch into a Transport Global onto your system.

> 5. On the KIDS menu \[XPD MAIN\], select the Installation menu \[XPD INSTALLATION MENU\] and use the following options to install the Transport Global:

> Verify Checksums in Transport Global

> Print Transport Global

> Compare Transport Global to Current System

> Backup a Transport Global

> Install Package(s)

> INSTALL NAME: XU\*8.0\*206

> Want KIDS to INHIBIT LOGONs during the install? NO

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO

> <span id="_Toc159835446" class="anchor"></span>Figure 6‑2. Sample installation of a KIDS transport global at a site

> 6.DSM/AXP Sites—Answer "NO" to the question "Want to MOVE routines to other CPUs?"

> 7.DELETE the following routines:

- XUMFPOST—Post-init routine.
- XUMFENV—Environment check routine.

|                                                   |                                                     |
|---------------------------------------------------|-----------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/101.png) | CAUTION: Do *not* delete any other XUMF\* routines! |

> 8. Add members to the XUMF INSTITUTION mail group who should be notified of any new Station Numbers added to the INSTITUTION file (e.g., IRM, PIMS ADPACs, etc).

|                                                                                                                |                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/102.png) | REF: For more information on this mail group, please refer to the "Mail Groups" topic in Chapter 7, "Software Product Security," in this manual. |

> 9. Add members to the XUMF SERVER mail group who should be notified of any server bulletins. These bulletins can include error messages related to the server mechanism (MFS) and may require intervention by IRM.

|                                                                                                                |                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/103.png) | REF: For more information on this mail group, please refer to the "Mail Groups" topic in Chapter 7, "Software Product Security," in this manual. |

#### Post Installation Instructions

> 1. (Optional) Add the Institution File Query / Update option \[XUMF INSTITUTION\] to the Kernel Management Menu \[XUKERNEL\].

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/104.png) | NOTE: The Institution File Query / Update option \[XUMF INSTITUTION\] was disabled with Kernel Patch XU\*8.0\*335 (i.e., Health*e*Vet cleanup) to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at Consolidated Mail Outpatient Pharmacies (CMOPs), or at any VistA site that has never done the cleanup and needs to fully load the Institution table. |

> 2. After installing Kernel Patch XU\*8.0\*206, you should perform the Installation File Cleanup. To run the Cleanup, select the Institution File Query / Update option \[XUMF INSTITUTION\] in the Kernel Management Menu.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/105.png)</td>
<td><strong>NOTE:</strong> The Institution File Query / Update option [XUMF INSTITUTION] was disabled with Kernel Patch XU*8.0*335(i.e., Health<em>e</em>Vet cleanup) to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA site that has never done the cleanup and needs to fully load the Institution table.<br />
<br />
<strong>REF:</strong> For a complete description of the Institution File Cleanup, please refer to the "Institution File Cleanup Process—Initial" topic in Chapter 2, "Local Site IMF Administrator Duties," in this manual.</td>
</tr>
</tbody>
</table>

#### Memory Constraints

There are no special memory constraints, other than sites having sufficient space to allow for normal global growth.

#### Special Operations

There are no special operations required other than the normal backup and recovery operations.

#### Maintenance

#### Bulletins

The Master File Server (MFS) generates the following Bulletins (listed alphabetically):

| Bulletin     | Description                                                                                                                                                                                                                                                |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XUMF ERROR       | This bulletin is an error message that is generated if an error occurs on the Master File Server (MFS).                                                                                                                                                        |
| XUMF INSTITUTION | This bulletin is an update notification message that is generated at a site (client) when the local site's INSTITUTION file (#4) has been automatically updated with national entries from the Institution Master File (IMF) via the Master File Server (MFS). |

<span id="_Toc159835447" class="anchor"></span>Table 6‑1. MFS bulletins associated with the IFR-related software

|                                                                                                                |                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/106.png) | REF: For more information on this mail group, please refer to the "Mail Groups" topic in Chapter 7, "Software Product Security," in this manual. |

#### HL7 Application Parameters

The Master File Server (MFS) uses the following HL7 Application Parameters (listed alphabetically):

| Hl7 Application Parameters | Description                            |
|--------------------------------|--------------------------------------------|
| DS Pub Man\~~L                 | Master File Notification                   |
| DTS Term Srv\~~L               | DTS Terminology Server                     |
| XUMF MFK                       | Master File Application ACK.               |
| XUMF MFN                       | Master File Notification.                  |
| XUMF MFP MFQ                   | Master File Parameters.                    |
| XUMF MFP MFR                   | Master File Parameters Query Response.     |
| XUMF MFQ                       | MFS Query.                                 |
| XUMF MFR                       | MFS Query Response.                        |
| XUMF MFS                       | MFS Handler.                               |
| XUMF SERVER                    | Master File Notification (VistA-to-VistA). |

<span id="_Toc159835448" class="anchor"></span>Table 6‑2. MFS HL7 application parameters associated with the IFR-related software

#### HL7 Logical Link

The Master File Server (MFS) uses the following HL7 Logical Link:

| HL7 Logical Link | Description                                        |
|----------------------|--------------------------------------------------------|
| XUMF ACK             | The MFS application acknowledgement.                   |
| XUMF FORUM           | The HL7 LOGICAL LINK (#870) to the Master File Server. |

<span id="_Toc159835449" class="anchor"></span>Table 6‑3. MFS HL7 logical link associated with the IFR-related software

|                                                                                                                |                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/107.png) | NOTE: The link does not need to be started via the Start logical Links option because it is a real-time link. |

#### Protocols

The Master File Server (MFS) uses the following protocols (listed alphabetically):

| MFS Protocol | Description                            |
|------------------|--------------------------------------------|
| DS Pub Man\~~L   | Master File Notification                   |
| DTS Term Srv\~~L | DTS Terminology Server                     |
| XUMF MFK         | Master File Application ACK.               |
| XUMF MFN         | Master File Notification.                  |
| XUMF MFP MFQ     | Master File Parameters.                    |
| XUMF MFP MFR     | Master File Parameters Query Response.     |
| XUMF MFQ         | MFS Query.                                 |
| XUMF MFR         | MFS Query Response.                        |
| XUMF MFS         | MFS Handler.                               |
| XUMF SERVER      | Master File Notification (VistA-to-VistA). |

<span id="_Toc159835450" class="anchor"></span>Table 6‑4. MFS protocols associated with the IFR-related software

The cleanup process of the local site's INSTITUTION file (#4) uses the following protocols (listed alphabetically):

| Cleanup Protocol | Description                           |
|----------------------|-------------------------------------------|
| XUMF AUTO            | Auto update with national data.           |
| XUMF CHCK            | Required clean up actions (CHCK).         |
| XUMF DSTA            | Delete local/dup. station \# (DSTA).      |
| XUMF LLCL            | List local data (LLCL).                   |
| XUMF NAME            | Names INSTITUTION vs. national.           |
| XUMF NATL            | List national data to merge (NATL).       |
| XUMF RDSN            | Resolve duplicate station numbers (RDSN). |
| XUMF RDSN MENU       | Duplicate station number menu.            |

<span id="_Toc159835451" class="anchor"></span>Table 6‑5. Cleanup protocols associated with the IFR-related software

#### Templates

The cleanup process of the local site's INSTITUTION file (#4) uses the following list templates (listed alphabetically):

| List Template | Description                      |
|-------------------|--------------------------------------|
| XUMF CHCK         | Required clean up actions (CHCK).    |
| XUMF DSTA         | Delete local/dup. station \# (DSTA). |
| XUMF LLCL         | List local data (LLCL).              |
| XUMF NAME         | Names INSTITUTION vs. national.      |
| XUMF NATL         | List national data to merge.         |

<span id="_Toc159835452" class="anchor"></span>Table 6‑6. Cleanup list templates associated with the IFR-related software

#### Routines

This section provides information related to all executable XU\* routines exported with IFR-related software (i.e., Kernel Patch XU\*8.0\*206). Do *not* delete any XU\* routines.

All IFR-related software routines are prefixed with the namespace "XU."

The second line of these routines looks like:

> \<tab\>;;8.0;KERNEL;\<XU\*8\*nnn\>;Jul 10, 1995

> (Where "nnn" = the appropriate patch reference number.)

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/108.png) | NOTE: Other routine information, such as the Routine Size Histogram, the Routine %Index, etc., can be generated through the use of Kernel Utilities. |

| Routine | Description                                                                             |
|-------------|---------------------------------------------------------------------------------------------|
| XUAF4       | Institution File Access (APIs).                                                             |
| XUMF        | Institution File Cleanup.                                                                   |
| XUMF218     | Load DOD DMIS ID's (Kernel Patch XU\*8.0\*218).                                             |
| XUMF218A    | Load DMIS ID's (Kernel Patch XU\*8.0\*261).                                                 |
| XUMF261P    | Post Init (Kernel Patch XU\*8.0\*261).                                                      |
| XUMF299     | Query server for parameters (Kernel Patch XU\*8.0\*299).                                    |
| XUMF333     | Add HCS Data Types (Kernel Patch XU\*8.0\*335).                                             |
| XUMF4       | Institution File Cleanup—Main.                                                              |
| XUMF416     | Load National Provider Identifier (NPI; Kernel Patch XU\*8.0\*416).                         |
| XUMF4A      | Institution File Cleanup—Auto.                                                              |
| XUMF4F      | Institution Master File Edit.                                                               |
| XUMF4H      | Institution File Cleanup—Help.                                                              |
| XUMF4L0     | Load IMF (Kernel Patch XU\*8.0\*217).                                                       |
| XUMF4L1     | Load IMF (Kernel Patch XU\*8.0\*261).                                                       |
| XUMF4L2     | Load IMF (Kernel Patch XU\*8.0\*217).                                                       |
| XUMF512F    | Postal and County Code Master File Edit (Kernel Patch XU\*8.0\*246).                        |
| XUMFEIMF    | Edit IMF (Kernel Patches XU\*8.0\*217 and 335).                                             |
| XUMFENV     | Environment check.                                                                          |
| XUMFH       | Master File Hl7 Message Handler.                                                            |
| XUMFH4      | FORUM IMF Handler (Kernel Patches XU\*8.0\*217 and 218).                                    |
| XUMFHM      | MFS Handler Error Message (Kernel Patches XU\*8.0\*416).                                    |
| XUMFHPQ     | Build query message for parameters (Kernel Patch XU\*8.0\*299).                             |
| XUMFHPR     | Build query response for parameters (Kernel Patch XU\*8.0\*299).                            |
| XUMFI       | Master File Interface.                                                                      |
| XUMFI0      | Master File Interface (Kernel Patch XU\*8.0\*369 & 416)                                     |
| XUMFMFE     | HL7 MFE Segment (Kernel Patch XU\*8.0\*217).                                                |
| XUMFMFI     | HL7 MFI Segment (Kernel Patch XU\*8.0\*217).                                                |
| XUMFP       | Master File C/S Parameters.                                                                 |
| XUMFP4      | Master File C/S Params INSTITUTION.                                                         |
| XUMFP4C     | Master File C/S Params INSTITUTION (continued).                                             |
| XUMFP4Z     | Master File Common Services Parameters INSTITUTION file (#4; Kernel Patch XU\*8.0\*416).    |
| XUMFP512    | Master File Param POSTAL CODE (Kernel Patch XU\*8.0\*246).                                  |
| XUMFP513    | Master File Param COUNTY CODE (Kernel Patch XU\*8.0\*246).                                  |
| XUMFPFT     | Master File C/S Param FACILITY TYPE.                                                        |
| XUMFPMFS    | Master File C/S Param FACILITY TYPE.                                                        |
| XUMFPOST    | Post-INIT routine (protocol subscriber associations with event; Kernel Patch XU\*8.0\*299). |
| XUMFPZL7    | Master File Param ZL7 (Kernel Patches XU\*8.0\*262, 369).                                   |
| XUMFR       | Pre/Post Update Subroutines (Kernel Patch XU\*8.0\*335).                                    |
| XUMFX       | MFS internal API (Kernel Patch XU\*8.0\*299).                                               |
| XUMFXACK    | MFS acknowledgement (Kernel Patch XU\*8.0\*299).                                            |
| XUMFXH      | MFS handler (Kernel Patch XU\*8.0\*299).                                                    |
| XUMFXHL7    | Parse HL7 segment (Kernel Patch XU\*8.0\*299).                                              |
| XUMFXI      | Build HL7 message (Kernel Patch XU\*8.0\*299).                                              |
| XUMFXP      | MFS parameters (main; Kernel Patch XU\*8.0\*299).                                           |
| XUMFXP1     | MFS parameters (param array; Kernel Patch XU\*8.0\*299).                                    |
| XUMFXP2     | MFS parameters (query; Kernel Patch XU\*8.0\*299).                                          |
| XUMFXR      | Pre/post updating subroutines (Kernel Patch XU\*8.0\*299).                                  |

<span id="_Toc159835453" class="anchor"></span>Table 6‑7. List of routines exported with IFR-related software

#### Files

This section contains information on all files and globals exported with the Institution File Redesign (IFR)-related software patches (Kernel Patch XU\*8.0\*206). This information includes: file numbers, file names, global location, data with file indicator, and file descriptions. The Institution File Redesign (IFR)-related software file numbers range from 4 to 4.1.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/109.png)</td>
<td><strong>REF:</strong> File security access is described in the "File Security" topic in Chapter 7, "Software Product Security," in this manual.<br />
<br />
<strong>NOTE:</strong> Other pertinent file information, such as data dictionaries and relations with other files, can be generated online through the use of VA FileMan utilities.</td>
</tr>
</tbody>
</table>

| File Number | File Name          | Global Location | Data W/ File? | Description                                                                                                                                                                                                                                                                              |
|-----------------|------------------------|---------------------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 4               | INSTITUTION            | ^DIC(4,             | No                | This file contains a listing of VA institutions. It is cross-referenced by STATION NUMBER and NAME. The NUMBER field is no longer meaningful (it had previously referenced the STATION NUMBER).                                                                                              |
| 4.001           | MASTER FILE PARAMETERS | ^DIC(4.001,         | Yes               | This file holds data type (data type = a standard file) parameters such as mapping HL7 segment fields and components to VA FileMan fields, pre/post update sub-routine calls, post-processing logic, HL7 data types, and Primary Key value definitions.                                      |
| 4.1             | FACILITY TYPE          | ^DIC(4.1,           | No                | The INSTITUTION file (#4) points to this file. It contains a list of facility codes that were previously stored in the VA TYPE CODE field of the INSTITUTION file. This file is exported with data, and the new data should overwrite the old. It is cross-referenced by NAME and FULL NAME. |

<span id="_Toc159835454" class="anchor"></span>Table 6‑8. Files used by IFR-related software

#### Exported Options

#### Options—*Without* Parents

The following options are not assigned to any menu when the Institution File Redesign (IFR)-related software patches are exported. They can be assigned to a menu at the discretion of the System Manager at a site, if appropriate (options listed alphabetically):

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 31%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th><strong>Option Title</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUMF DMIS ID LOAD</td>
<td>Load DMIS ID's</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*218. It is used to queue a TaskMan task that queries the Institution Master File (IMF) using HL7 messaging to get a copy of the DoD facilities in the IMF. These facilities are then added to the local Institution file.</p>
<p>This option is locked with the XUMF INSTITUTION security key.</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/110.png) CAUTION: We recommend that only the VA CMOP facilities that require these DoD facilities use this option at this time.</p></td>
</tr>
<tr class="even">
<td>XUMF FORUM INSTITUTION</td>
<td>Institution Master File Edit</td>
<td>This option was introduced with Kernel Patch XU*8.0*206. It is available only on FORUM. It is locked with the XUMF INSTITUTION security key. This option is used to update entries in the FORUM Institution Master File (IMF).</td>
</tr>
<tr class="odd">
<td>XUMF IMF ADD EDIT</td>
<td>IMF edit</td>
<td>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup); it replaces the IMF address edit option [XUMF IMF ADD EDIT] introduced with Kernel Patch XU*8.0*217. It allows the site to edit their INSTITUTION file (#4) entries (i.e., those entries that share the same 3-digit Station Number as the current users logon division) and generates an HL7 update message to update the Institution Master File (IMF) on FORUM.</td>
</tr>
<tr class="even">
<td>XUMF IMF EDIT STATUS</td>
<td>IMF Display Cleanup Status</td>
<td>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup). It lists all your facilities that need updating. It also lists the fields that are missing data. It's a good idea to list this information before editing your data.</td>
</tr>
<tr class="odd">
<td>XUMF INSTITUTION</td>
<td>Institution File Query / Update</td>
<td><p>This option was disabled with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup) to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA site that has never done the cleanup and fully loaded the Institution table.</p>
<p>This option was originally introduced with Kernel Patch XU*8.0*206. It was used to update entries in the local site's INSTITUTION file (#4).</p></td>
</tr>
<tr class="even">
<td>XUMF LOAD INSTITUTION</td>
<td>Update/refresh Institution file with IMF data</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup). It loads the current IMF data into the INSTITUTION file (#4).</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/111.png) <strong>NOTE:</strong> The XUMF LOAD INSTITUTION option will not be completely successful if there are duplicate station numbers. The cleanup fixes/removes duplicates (see the "Institution File Cleanup Process—Initial" topic in Chapter 2,"Local Site IMF Administrator Duties," in this manual). Thus, the cleanup is a required first step before you can get updates, get the national table, or use the XUMF LOAD INSTITUTION option.</p></td>
</tr>
<tr class="odd">
<td>XUMF335 clean 4.1 and 4</td>
<td>Patch XU*8*335 clean 4.1 and 4</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup). It queries the IMF for the latest copy of Institution data—updating the local INSTITUTION file (#4). All INACTIVE facilities have the NAME (#.01) ZZ'd and the VISN and PARENT FACILITY associations removed. It removes facility types before getting new values, so it should be run after hours.</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/112.png) <strong>NOTE:</strong> This option should be run at a later date after all sites have completed editing.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc159835455" class="anchor"></span>Table 6‑9. Menu options without parents exported with IFR-related software

|                                                                                                                |                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/113.png) | NOTE: You can optionally attach these options to the Kernel Management Menu \[XUKERNEL\]. |

#### Options—*With* Parents

The following option is assigned to the Kernel Management Menu \[XUKERNEL\] on FORUM when the Institution File Redesign (IFR)-related software patches are installed:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 31%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th><strong>Option Title</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUMF LOAD NPI</td>
<td>Load Institution NPI values</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*416.</p>
<p>This option is to be used only in the case the National Provider Identifier (NPI) values fail to load in the post install or if it should become necessary to reload the NPI values (e.g., NPI values become corrupt or the data otherwise needs to be refreshed).</p>
<p>This option is used to edit institution data, including NPI and Taxonomy codes, selectable by coding system (e.g., NPI, Department of Defense [DOD], or Clinical Laboratory Improvement Amendments [CLIA]) and Identifier pair (for beta testing made target site, for Health Level seven [HL7] unsolicited update message, selectable rather than publish nationally).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc159835456" class="anchor"></span>Table 6‑10. Menu options with parents exported with IFR-related software

#### Archiving and Purging

There are no application-specific archiving and purging procedures or recommendations for IFR-related software (i.e., Kernel Patch XU\*8.0\*206).

#### Callable Routines

This topic lists all the APIs exported with the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206).

Every callable entry point (API) is described in Chapter 5, "Application Program Interfaces (APIs)," in this manual.

| Entry Point                      | Brief Description                                                                                                                                                                                                                                                                                                 |
|--------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \$\$ACTIVE^XUAF4(ien)                | This function, given the Internal Entry Number (IEN) in the INSTITUTION file (#4), returns the Boolean value for the question—is this an active facility? It checks to see if the INACTIVE FACILITY FLAG field (#101) is *not* set.                                                                                   |
| \$\$CIRN^XUAF4(inst\[,value\])       | This function returns the value of the CIRN-enabled field from the INSTITUTION file (#4).                                                                                                                                                                                                                             |
| \$\$ID^XUAF4(cdsys,ien)              | This function returns the Identifier (ID) of an INSTITUTION file (#4) entry for a given Coding System and Internal Entry Number (IEN).                                                                                                                                                                                |
| \$\$IDX^XUAF4(cdsys,id)              | This function returns the Internal Entry Number (IEN) of an INSTITUTION file (#4) entry for a given Coding System and Identifier (ID) pair.                                                                                                                                                                           |
| \$\$IEN^XUAF4(sta)                   | This function returns the INSTITUTION file (#4) IEN for a given Station Number.                                                                                                                                                                                                                                       |
| \$\$IEN^XUMF(ifn,cdsys,id)           | This function returns the INSTITUTION file (#4) IEN for a given Internal File Number (IFN), Coding System, and Identifier (ID).                                                                                                                                                                                       |
| \$\$LEGACY^XUAF4(sta)                | This function, given the STATION NUMBER field (#99) in the INSTITUTION file (#4), returns the Boolean value for the question—has this station number been realigned? Is it a legacy Station Number?                                                                                                                   |
| \$\$LKUP^XUAF4(inst)                 | This function returns the IEN or zero when doing a lookup on the INSTITUTION file (#4).                                                                                                                                                                                                                               |
| \$\$MADD^XUAF4(ien)                  | This function returns the mailing address information for an institution in a caret-delimited string (i.e., streetaddr^city^state^zip) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).                                                                                                          |
| \$\$NAME^XUAF4(ien)                  | This function returns the OFFICIAL NAME field (#100) value in the INSTITUTION file (#4) for an institution given its Internal Entry Number (IEN). However, If Field \#100 is null, the NAME field (#.01) in the INSTITUTION file (#4) is returned.                                                                    |
| \$\$NNT^XUAF4(ien)                   | This function returns the station information for an institution in a caret-delimited string (i.e., station_number^station_name^station_type) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).                                                                                                   |
| \$\$NS^XUAF4(ien)                    | This function returns the institution information in a caret-delimited string (i.e., institution_name^station_number) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).                                                                                                                           |
| \$\$O99^XUAF4(ien)                   | If this entry was merged due to a duplicate Station Number, this function returns a pointer to the new Station Number INSTITUTION file (#4) IEN.                                                                                                                                                                      |
| \$\$PADD^XUAF4(ien)                  | This function returns the physical address information for an institution in a caret-delimited string (streetaddr^city^state^zip) for a given Internal Entry Number (IEN) in the INSTITUTION file (#4).                                                                                                               |
| \$\$PRNT^XUAF4(sta)                  | This function returns the parent facility institution information in a caret-delimited string (ien^station_number^name) for a given child facility STATION NUMBER field (#99) in the INSTITUTION file (#4).                                                                                                           |
| \$\$RF^XUAF4(ien)                    | This function returns the realigned from "IEN^station number^date" for a given INSTITUTION file (#4) IEN.                                                                                                                                                                                                             |
| \$\$RT^XUAF4(ien)                    | This function returns the realigned to "IEN^station number^date" for a given INSTITUTION file (#4) IEN.                                                                                                                                                                                                               |
| \$\$STA^XUAF4(ien)                   | This function returns the Station Number for a given INSTITUTION file (#4) IEN.                                                                                                                                                                                                                                       |
| \$\$TF^XUAF4(ien)                    | This function determines if this is an active treating facility for a given INSTITUTION file (#4) IEN.                                                                                                                                                                                                                |
| \$\$WHAT^XUAF4(ien,field)            | This function returns the data from a single field given the Internal Entry Number (IEN) and the specific field requested in the INSTITUTION file (#4).                                                                                                                                                               |
| CDSYS^XUAF4(y)                       | This API returns the Coding System name.                                                                                                                                                                                                                                                                              |
| CHILDREN^XUAF4(array,parent)         | This API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the "parent" input parameter.                                                                                                                                              |
| F4^XUAF4(sta,array,flag,date)        | INSTITUTION file (#4) multipurpose API.                                                                                                                                                                                                                                                                               |
| LOOKUP^XUAF4()                       | This API lookup utility allows a user to select an Institution by Coding System and ID. It prompts a user for a Coding System and then prompts for an Identifier—it's an IX^DIC API call on a New Style cross-reference of the ID field (#.02) of the IDENTIFIER Multiple field (#9999) of the INSTITUTION file (#4). |
| MAIN^XUMFI(ifn,ien,type,param,error) | This API implements an HL7 Master File Message Builder Interface that dynamically maps a VA FileMan field to an HL7 Master File sequence within a segment.                                                                                                                                                            |
| MAIN^XUMFP(ifn,ien,type,param,error) | This API sets up required parameters used by the HL7 Master File Message Builder Interface and the HL7 Master File message handler.                                                                                                                                                                                   |
| PARENT^XUAF4(array,lookup\[,type\])  | This API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the "lookup" input parameter.                                                                                                                                              |
| SIBLING^XUAF4(array,child\[,type\])  | This API returns a list of all institutions that make up a given Veterans Integrated Service Network (VISN), parent institution entered in the "child" input parameter.                                                                                                                                               |

<span id="_Toc159835457" class="anchor"></span>Table 6‑11. Callable routines for IFR-related software—Alphabetized by entry point

#### External Interfaces

#### Hardware Interfaces

The INSTITUTION file (#4) and FACILITY TYPE file (#4.1) components continue to function on the standard hardware platforms employed by Department of Veterans Affairs healthcare facilities. These systems consist of Alpha AXP (running DSM) or Alpha/NT (running OpenM).

#### Software Interfaces

The INSTITUTION (#4) and FACILITY TYPE (#4.1) files, as well as other master files, are integral components of VistA and are referenced by numerous software applications. An HL7 (Messaging & Interface Services \[M&IS\]) interface specification for interaction with the Master File Server (MFS) has been defined with Kernel Patch XU\*8.0\*206.

The MFS and VistA's HL7 software provide the following functionality:

- Broadcast Updates—Implements a server mechanism to broadcast FORUM's Institution Master File (IMF) updates VHA-wide.
- Handle Update Message—Implements a message handler to update the site's local INSTITUTION file (#4).
- Query Server—Provides functionality to query FORUM's Institution Master File and Facility Type Master File.
- Handle Query Response—Provides functionality to handle query responses.
- Track Station Number Changes—Tracks Station Number changes in the INSTITUTION file (#4) via bulletins/e-mail messages and the VistA HL7 software.
- Application Program Interfaces (APIs)—Provides Application Program Interfaces (APIs) to set up required parameters to build and send HL7 messages.

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/114.png) | REF: For more information on the APIs, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/115.png) | REF: For more information on the Master File Server (MFS), please refer to the "Master File Server (MFS)" topic in Chapter 1, "Introduction," in this manual. |

|                                                                                                                |                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/116.png) | REF: For a list of HL7 Application Parameters, HL7 Logical Link, and Master File Server Protocols associated with the IFR-related software, please refer to the "Maintenance" topic in this chapter. |

#### Communications Interfaces

VistA's VA MailMan and HL7 (Messaging & Interface Services \[M&IS\]) software, utilizing bi-directional data transmission of HL7 messages over TCP/IP, provides support for communication between the VHA site (client) and FORUM (server) applications.

Kernel Patch XU\*8.0\*206 created the XUMF INSTITUTION mail group in MailMan to receive bulletins regarding updates to the INSTITUTION file (#4). Sites are responsible for populating this mail group with the appropriate personnel (e.g., IRM Chief, ADPAC, etc.).

Kernel Patch XU\*8.0\*299 created the XUMF ERROR mail group in MailMan. Members in this group will be notified of errors that may occur when the MFS is updating national entries in a standard table. Sites are responsible for populating this mail group with the appropriate personnel.

|                                                                                                                |                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/117.png) | REF: For more information on the mail groups exported with IFR-related software, please refer to the "Mail Groups" topic in Chapter 7, "Software Product Security," in this manual. |

|                                                                                                                |                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/118.png) | REF: For a list of Bulletins associated with IFR-related software, please refer to the "Bulletins" topic under the "Maintenance" topic in this chapter. |

#### External Relations

#### Software Requirements

The IFR-related software (i.e., Kernel Patch XU\*8.0\*206) requires a standard VistA operating environment in order to function correctly. Check your VistA environment for software and versions installed.

The minimum VistA software and patches that are required are listed as follows by:

1.  VistA software and current version number.
2.  Associated patch designations that need to be installed in addition to the VistA software.
3.  Brief description of the associated patch.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 26%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>VistA Software &amp; Version</strong></th>
<th><strong>Associated Patch Designations</strong></th>
<th><strong>Brief Patch Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Automated Med Info Exchange, V. 2.7</td>
<td>DVBA*2.7*32</td>
<td>User Station Number Check.</td>
</tr>
<tr class="even">
<td rowspan="2">Kernel, V. 8.0</td>
<td>XU*8.0*43</td>
<td>CIRN Institution file update—This patch is in support of MPI/PD (i.e. CIRN). It adds fields to the INSTITUTION file (#4), an entry to the FACILITY TYPE file (#4.1), and adds new INSTITUTION file (#4) associations.</td>
</tr>
<tr class="odd">
<td>XU*8.0*112</td>
<td>Remedy ticket fixes and APIs—XUAF4 routine fixed in the $$LKUP API.</td>
</tr>
<tr class="even">
<td>Master Patient Index VistA, V. 1.0</td>
<td>MPIF*1.0*16</td>
<td><p>CIRN Master of Record (CMOR) Not Updating.</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/119.png) <strong>NOTE:</strong> MPIF and RG patches should <em>not</em> be installed in Legacy systems to avoid issues with the legacy systems ending up as CMORs, Treating Facilities or Subscribers.</p></td>
</tr>
<tr class="odd">
<td>Registration, V. 5.3</td>
<td>DG*5.3.0*357</td>
<td>RAI MDS Institution Name Changing Problem.</td>
</tr>
<tr class="even">
<td>Remote Order/Entry System, V. 2.0</td>
<td>RMPF*2.0*16</td>
<td>ROES Facility Lookup Fix/Message Addressing/Print Problem.</td>
</tr>
</tbody>
</table>

<span id="_Toc159835458" class="anchor"></span>Table 6‑12. Associated patches required for installation prior to installing Kernel Patch XU\*8.0\*206

The Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) requires a standard VistA operating environment in order to function correctly. Check your VistA environment for software and versions installed.

#### Dependencies

The IFR-related software provides a common set of APIs for standardizing and retrieving Institution time-sensitive (historical) information.

|                                                                                                                |                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/120.png) | REF: For more information on the APIs associated with the IFR-related software, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

#### Integration Agreements (IA<span class="smallcaps">)</span>

#### Supported References

These are the Kernel Supported reference Integration Agreements (IAs) for Institution File Redesign (IFR)-related software. Supported reference APIs are open for use by any VistA application as defined by the IA. They have been recorded as Supported references in the IA database on FORUM. VistA software applications are not required to request an IA to use these APIs.

The Supported Integration Agreements (IAs) are listed alphabetically by entry point below:

| Entry Point Or Global Root | IA \# | Type | Name                                                      |
|--------------------------------|-----------|----------|---------------------------------------------------------------|
| \$\$ACTIVE^XUAF4               | \#2171    | Routine  | Institution Active Facility Function API                      |
| CDSYS^XUAF4                    | \#2171    | Routine  | Coding System Name API                                        |
| CHILDREN^XUAF4                 | \#2171    | Routine  | List of Child Institutions for a Parent API                   |
| \$\$CIRN^XUAF4                 | \#2171    | Routine  | Institution CIRN-enabled Field Value Function API             |
| F4^XUFA4                       | \#2171    | Routine  | Multipurpose API.                                             |
| \$\$ID^XUAF4                   | \#2171    | Routine  | Institution Identifier Function API                           |
| \$\$IDX^XUAF4                  | \#2171    | Routine  | Institution IEN (Using Coding System & ID) Function API       |
| \$\$IEN^XUAF4                  | \#2171    | Routine  | IEN for Station Number Function API.                          |
| \$\$IEN^XUMF                   | \#3795    | Routine  | Institution IEN (Using IFN, Coding System, & ID) Function API |
| \$\$LEGACY^XUAF4               | \#2171    | Routine  | Institution Realigned/Legacy Function API                     |
| \$\$LKUP^XUAF4                 | \#2171    | Routine  | Institution Lookup Function API                               |
| LOOKUP^XUAF4                   | \#2171    | Routine  | Lookup Institution Identifier API                             |
| \$\$MADD^XUAF4                 | \#2171    | Routine  | Institution Mailing Address Function API                      |
| \$\$NAME^XUAF4                 | \#2171    | Routine  | Institution Official Name Function API                        |
| \$\$NNT^XUAF4                  | \#2171    | Routine  | Institution Station Number, Name, and Type Function API       |
| \$\$NS^XUAF4                   | \#2171    | Routine  | Institution Name and Station Number Function API              |
| \$\$O99^XUAF4                  | \#2171    | Routine  | Merged Duplicates Function API.                               |
| \$\$PADD^XUAF4                 | \#2171    | Routine  | Institution Physical Address Function API                     |
| PARENT^XUAF4                   | \#2171    | Routine  | Parent Institution Lookup API                                 |
| \$\$PRNT^XUAF4                 | \#2171    | Routine  | Institution Parent Facility Function API                      |
| \$\$RF^XUAF4                   | \#2171    | Routine  | Realigned From Function API.                                  |
| \$\$RT^XUAF4                   | \#2171    | Routine  | Realigned To Function API.                                    |
| SIBLING^XUAF4                  | \#2171    | Routine  | Sibling Institution Lookup API                                |
| \$\$STA^XUAF4                  | \#2171    | Routine  | Return STATION NUMBER Function API.                           |
| \$\$TF^XUAF4                   | \#2171    | Routine  | Treating Facility Function API.                               |
| \$\$WHAT^XUAF4                 | \#2171    | Routine  | Institution Single Field Information Function API             |

<span id="_Toc159835459" class="anchor"></span>Table 6‑13. Supported references for the IFR-related software—Alphabetized by entry point

|                                                                                                                |                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/121.png) | REF: For more information on the APIs associated with the IFR-related software, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

#### Controlled Subscription References

These are the Kernel Controlled Subscription Integration Agreements for Institution File Redesign (IFR)-related software. They contain attributes/functions that *must* be controlled in their use. They have been recorded as a Controlled Subscription references in the IA database on FORUM. Permission to use them is granted by the custodian package (i.e., Kernel) on a one-by-one basis.

The Controlled Subscription Integration Agreements (IAs) are listed alphabetically by Entry Point below:

| Entry Point Or Global Root | IA \# | Type | Name                         |
|--------------------------------|-----------|----------|----------------------------------|
| MAIN^XUMFI                     | \#3354    | Routine  | Master File Message Builder API. |
| MAIN^XUMFP                     | \#3354    | Routine  | Master File Parameter API.       |

<span id="_Toc159835460" class="anchor"></span>Table 6‑14. Controlled subscription references for the IFR-related software—Alphabetized by entry point

|                                                                                                                |                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/122.png) | REF: For more information on the APIs associated with the IFR-related software, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

#### General Instructions for Obtaining Integration Agreements

To obtain the current list of active IAs of which Kernel, which includes Institution File Redesign (IFR), is a custodian:

> 1. Sign on to the FORUM system.

> 2. Select the DBA menu \[DBA\].

> 3. Select the Integration Agreements Menu \[DBA IA ISC\].

> 4. Select the Custodial Package Menu \[DBA IA CUSTODIAL MENU\].

> 5. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].

> 6. Enter KERNEL at the "Select PACKAGE NAME:" prompt. You may have to further refine your selection, if presented with a list of similarly named packages.

> 7. Choose the device to display the list of IAs.

> 8. All current active IAs for which the Kernel package is custodian are listed.

To obtain detailed information about a specific integration agreement:

> 1. Sign on to the FORUM system.

> 2. Select the DBA menu \[DBA\].

> 3. Select the Integration Agreements Menu \[DBA IA ISC\].

> 4. Choose the Inquire option \[DBA IA INQUIRY\].

> 5. Enter the integration agreement number of the IA you would like to display (e.g., DBIA2171) at the "Select INTEGRATION REFERENCES:" prompt.

> 6. Choose the device to display the IA.

> 7. The full text of the requested IA will be displayed.

To obtain the current list of IAs that Kernel, which includes Institution File Redesign (IFR), is a subscriber to:

> 1. Sign on to the FORUM system.

> 2. Select the DBA menu \[DBA\].

> 3. Select the Integration Agreements Menu \[DBA IA ISC\].

> 4. Select the Subscriber Package Menu \[DBA IA SUBSCRIBER MENU\].

> 5. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].

> 6. Enter KERNEL (in uppercase) at the "START WITH SUBSCRIBING PACKAGE: FIRST//" prompt.

> 7. Enter KERNEL (in uppercase) at the "GO TO SUBSCRIBING PACKAGE: LAST//" prompt.

> 8. Choose the device to display the list of IAs.

> 9. All current active IAs to which the Kernel package is a subscriber are listed.

#### Internal Relations

The following options were originally exported with the IFR-related software (i.e., Kernel Patch XU\*8.0\*206):

- Institution Master File Edit option \[XUMF FORUM INSTITUTION\]
- Institution File Query / Update option \[INSTITUTION FILE QUERY / UPDAT XUMF INSTITUTION\]

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/123.png) | NOTE: The Institution File Query / Update option \[XUMF INSTITUTION\] was disabled with Kernel Patch XU\*8.0\*335 (i.e., Health*e*Vet cleanup) to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA site that has never done the cleanup and fully loaded the Institution table. |

The following option is associated with the original IFR-related software release (i.e., Kernel Patch XU\*8.0\*206), however, it is *not* exported with nor modified by Kernel Patch XU\*8.0\*206:

- Institution Edit option \[XU-INSTITUTION-E\]

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/124.png) | REF: For a complete list of *all* options exported with the Institution File Redesign (IFR)-related software (including all IFR-related patches), please refer to Table 7‑2 in Chapter 7, "Software Product Security," in this manual. |

Also, the following List Manager actions are exported with Kernel Patch XU\*8.0\*206:

- LLCL—List local station numbers.
- NATL—List national data to merge.
- DSTA—Delete local/dup. station \#.
- RDSN—Resolve duplicate station numbers.
- AUTO—Auto update with national data.
- CHCK—Required clean up actions.

|                                                                                                                |                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/125.png) | REF: For the minimum VistA software and patches required before installing IFR-related software, please refer to the "Installation Instructions" topic in this chapter. |

#### Namespace

The Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) uses Kernel's XU namespace. All routines and globals used in Kernel Patch XU\*8.0\*206 begin with XUMF.

#### File Numbers

The following file numbers and global locations are established with the IFR-related software:

| File \# | Global  |
|-------------|-------------|
| 4           | ^DIC(4,     |
| 4.001       | ^DIC(4.001, |
| 4.1         | ^DIC(4.1,   |

<span id="_Toc159835461" class="anchor"></span>Table 6‑15. File and global information for the IFR-related software

The full Data Dictionaries for the INSTITUTION (#4) and the FACILITY TYPE (#4.1) files are being exported with Kernel Patch XU\*8.0\*206. The new field and changed field definitions are transported in the KIDS transport global and installed at the site.

|                                                                                                                |                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/126.png) | REF: For specific information on added, modified, and deleted fields, please refer to the "Institution File Data Dictionary Modifications" and "Facility Type File Data Dictionary Modifications" topics in Chapter 4, "Data Dictionary Modifications," in this manual. |

#### Software-wide Variables

The following software-wide variable is contained within the Institution File Redesign (IFR)-related software, as of Kernel Patch XU\*8.0\*299:

| Variable | Description                          |
|--------------|------------------------------------------|
| XUMF         | Flag to enable editing standard entries. |

<span id="_Toc159835462" class="anchor"></span>Table 6‑16. Software-wide variables for the IFR-related software

## Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Institution Master File (IMF) and Facility Type Master File (FMF) are only accessible on FORUM. All FORUM security protocols are followed.

- Only *national* entries are stored in the Institution Master File (IMF) and Facility Type Master File (FMF) on FORUM.
- Updates to the *national* entries in the IMF (i.e., INSTITUITION file \[#4\]) on FORUM can only be made with the Institution Master File Edit \[XUMF FORUM INSTITUTION\] option, which is available only on FORUM.
- The XUMF FORUM INSTITUTION option is locked with the XUMF INSTITUTION security key. The FORUM Institution Master File Administrators are the only people to hold this security key.

#### Mail Groups

The following mail groups are exported with the IFR-related software:

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>MAIL GROUP</strong></th>
<th><strong>DESCRIPTION</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUMF ERROR</td>
<td><p>As of Kernel Patch XU*8.0*299, the XUMF ERROR mail group receives Master File Server (MFS) update error notifications.</p>
<p>The Local Site is responsible for populating (i.e., Mail Group Coordinator), maintaining, and monitoring this mail group. The mail group should be populated with the appropriate personnel who are to be notified of any errors that may occur when the MFS is updating national entries in a standard table.</p></td>
</tr>
<tr class="even">
<td>XUMF INSTITUTION</td>
<td><p>The XUMF INSTITUTION mail group receives bulletins sent via VistA's MailMan software regarding updates to the site's INSTITUTION file (#4). The mail group at the site is notified when their local INSTITUTION file (#4) has been automatically updated with <em>national</em> entries from the Institution Master File (IMF) on FORUM via the Master File Server (MFS).</p>
<p>The Local Site Institution Master File Administrators are responsible for populating (i.e., Mail Group Coordinator), maintaining, and monitoring this mail group. The mail group should be populated with the appropriate personnel who are to be notified of any add/edits to national entries in the local site's INSTITUTION file (e.g., Local Site Institution Master File Administrator[s], IRM Chief, ADPAC[s], etc.).</p></td>
</tr>
<tr class="odd">
<td>XUMF SERVER</td>
<td><p>The XUMF SERVER mail group receives Master File Server (MFS)-related messages (on FORUM and at the site).</p>
<p>The Local Site Institution Master File Administrators are responsible for populating (i.e., Mail Group Coordinator), maintaining, and monitoring this mail group. The mail group should be populated with the appropriate personnel who are to be notified of any general server-related messages (e.g., errors).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc159835463" class="anchor"></span>Table 7‑1. Mail groups exported with the IFR-related software

|                                                                                                                |                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/127.png) | REF: For information regarding bulletins, please refer to the "Bulletins" topic under the "Maintenance" topic in Chapter 6, "Implementation and Maintenance," in this manual. |

#### Remote Systems

Kernel Patch XU\*8.0\*206 uses the Master File Server (MFS) to automatically transmit national INSTITUTION file data to update the INSTITUTION file (#4) located at all sites VHA-wide.

An HL7 (Messaging & Interface Services \[M&IS\]) interface specification for interaction with the Master File Server (MFS) has been defined. VistA's VA MailMan and HL7 (Messaging & Interface Services \[M&IS\]) software, utilizing bi-directional data transmission of HL7 messages over TCP/IP, provides support for communication between the FORUM (server) and VHA site (client) applications. The anticipated frequency for data transmission is approximately two to eight times per month. The data transmitted is *not* encrypted.

#### Archiving and Purging

There are no software-specific archiving and purging procedures or recommendations for the IFR-related software (i.e., Kernel Patch XU\*8.0\*206).

#### Interfaces

#### Hardware Interfaces

The INSTITUTION file (#4) and FACILITY TYPE file (#4.1) components continue to function on the standard hardware platforms employed by Department of Veterans Affairs healthcare facilities. These systems consist of Alpha AXP (running DSM) or Alpha/NT (running OpenM).

#### Software Interfaces

The INSTITUTION (#4) and FACILITY TYPE (#4.1) files, as well as other master files, are integral components of VistA and are referenced by numerous software applications. An HL7 (Messaging & Interface Services \[M&IS\]) interface specification for interaction with the Master File Server (MFS) has been defined with Kernel Patch XU\*8.0\*206.

The MFS and VistA's HL7 software provide the following functionality:

- Broadcast Updates—Implements a server mechanism to broadcast FORUM's Institution Master File (IMF) updates VHA-wide.
- Handle Update Message—Implements a message handler to update the site's local INSTITUTION file (#4).
- Query Server—Provides functionality to query FORUM's Institution Master File and Facility Type Master File.
- Handle Query Response—Provides functionality to handle query responses.
- Track Station Number Changes—Tracks Station Number changes in the INSTITUTION file (#4) via bulletins/e-mail messages and the VistA HL7 software.
- Application Program Interfaces (APIs)—Provides Application Program Interfaces (APIs) to set up required parameters to build and send HL7 messages.

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/128.png) | REF: For more information on the APIs, please refer to Chapter 5, "Application Program Interfaces (APIs)," in this manual. |

|                                                                                                                |                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/129.png) | REF: For more information on the Master File Server (MFS), please refer to the "Master File Server (MFS)" topic in Chapter 1, "Introduction," in this manual. |

|                                                                                                                |                                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/130.png) | REF: For a list of HL7 Application Parameters, HL7 Logical Link, and Master File Server Protocols associated with the IFR-related software, please refer to the "Maintenance" topic in Chapter 6, "Implementation and Maintenance," in this manual. |

#### Communications Interfaces

VistA's VA MailMan and HL7 (Messaging & Interface Services \[M&IS\]) software, utilizing bi-directional data transmission of HL7 messages over TCP/IP, provides support for communication between the VHA site (client) and FORUM (server) applications.

Kernel Patch XU\*8.0\*206 created the XUMF INSTITUTION mail group in MailMan to receive bulletins regarding updates to the INSTITUTION file (#4). Sites are responsible for populating this mail group with the appropriate personnel (e.g., IRM Chief, ADPAC, etc.).

Kernel Patch XU\*8.0\*299 created the XUMF ERROR mail group in MailMan. Members in this group will be notified of errors that may occur when the MFS is updating national entries in a standard table. Sites are responsible for populating this mail group with the appropriate personnel.

|                                                                                                                |                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/131.png) | REF: For more information on the mail groups exported with IFR-related software, please refer to the "Mail Groups" topic in this chapter. |

|                                                                                                                |                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/132.png) | REF: For a list of Bulletins associated with IFR-related software, please refer to the "Bulletins" topic under the "Maintenance" topic in Chapter 6, "Implementation and Maintenance," in this manual. |

#### Electronic Signatures

There are no electronic signatures used in the IFR-related software (i.e., Kernel Patch XU\*8.0\*206).

#### Menus/Options

The following options are exported with the IFR-related software:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 31%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th><strong>Option Title</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>XUMF DMIS ID LOAD</td>
<td>Load DMIS ID's</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*218. It is used to queue a TaskMan task that queries the Institution Master File (IMF) using HL7 messaging to get a copy of the DoD facilities in the IMF. These facilities are then added to the local Institution file.</p>
<p>This option is locked with the XUMF INSTITUTION security key.</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/133.png) CAUTION: We recommend that only the VA CMOP facilities that require these DoD facilities use this option at this time.</p></td>
</tr>
<tr class="even">
<td>XUMF FORUM INSTITUTION</td>
<td>Institution Master File Edit</td>
<td>This option was introduced with Kernel Patch XU*8.0*206. It is available only on FORUM. It is locked with the XUMF INSTITUTION security key. This option is used to update entries in the FORUM Institution Master File (IMF).</td>
</tr>
<tr class="odd">
<td>XUMF IMF ADD EDIT</td>
<td>IMF edit</td>
<td>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup); it replaces the IMF address edit option [XUMF IMF ADD EDIT] introduced with Kernel Patch XU*8.0*217. It allows the site to edit their INSTITUTION file (#4) entries (i.e., those entries that share the same 3-digit Station Number as the current users logon division) and generates an HL7 update message to update the Institution Master File (IMF) on FORUM.</td>
</tr>
<tr class="even">
<td>XUMF IMF EDIT STATUS</td>
<td>IMF Display Cleanup Status</td>
<td>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup). It lists all your facilities that need updating. It also lists the fields that are missing data. It's a good idea to list this information before editing your data.</td>
</tr>
<tr class="odd">
<td>XUMF INSTITUTION</td>
<td>Institution File Query / Update</td>
<td><p>This option was disabled with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup) to prevent sites that have already initially cleaned up their INSTITUTION file (#4) from running the option again. It should be used only in development accounts, at CMOPs, or at any VistA site that has never done the cleanup and fully loaded the Institution table.</p>
<p>This option was originally introduced with Kernel Patch XU*8.0*206. It was used to update entries in the local site's INSTITUTION file (#4).</p></td>
</tr>
<tr class="even">
<td>XUMF LOAD INSTITUTION</td>
<td>Update/refresh Institution file with IMF data</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup). It loads the current IMF data into the INSTITUTION file (#4).</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/134.png) <strong>NOTE:</strong> The XUMF LOAD INSTITUTION option will not be completely successful if there are duplicate station numbers. The cleanup fixes/removes duplicates (see the "Institution File Cleanup Process—Initial" topic in Chapter 2, "Local Site IMF Administrator Duties," in this manual). Thus, the cleanup is a required first step before you can get updates, get the national table, or use the XUMF LOAD INSTITUTION option.</p></td>
</tr>
<tr class="odd">
<td>XUMF LOAD NPI</td>
<td>Load Institution NPI values</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*416.</p>
<p>This option is to be used only in the case the National Provider Identifier (NPI) values fail to load in the post install or if it should become necessary to reload the NPI values (e.g., NPI values become corrupt or the data otherwise needs to be refreshed).</p>
<p>This option is used to edit institution data, including NPI and Taxonomy codes, selectable by coding system (e.g., NPI, Department of Defense [DOD], or Clinical Laboratory Improvement Amendments [CLIA]) and Identifier pair (for beta testing made target site, for Health Level seven [HL7] unsolicited update message, selectable rather than publish nationally).</p></td>
</tr>
<tr class="even">
<td>XUMF335 clean 4.1 and 4</td>
<td>Patch XU*8*335 clean 4.1 and 4</td>
<td><p>This option was introduced with Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup). It queries the IMF for the latest copy of Institution data—updating the local INSTITUTION file (#4). All INACTIVE facilities have the NAME (#.01) ZZ'd and the VISN and PARENT FACILITY associations removed. It removes facility types before getting new values, so it should be run after hours.</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/135.png) <strong>NOTE:</strong> This option should be run at a later date after all sites have completed editing.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref108424646" class="anchor"></span>Table 7‑2. Menu options exported with IFR-related software

#### Security Key

The following security key is exported with the IFR-related software (i.e., Kernel Patch XU\*8.0\*206):

| Security Key     | Description                                                                                                                                                                                                                                                                           |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XUMF INSTITUTION | The XUMF INSTITUTION security key is exported with Kernel Patch XU\*8.0\*206. The XUMF FORUM INSTITUTION option exported with Kernel Patch XU\*8.0\*206 is locked with this security key. The FORUM Institution Master File Administrators are the only people to hold this security key. |

<span id="_Toc159835465" class="anchor"></span>Table 7‑3. Security keys exported with IFR-related software

#### File Security

The following file security is established with the IFR-related software:

| File \# | File Name          | DD | RD | WR | DEL | LAYGO | AUDIT |
|-------------|------------------------|--------|--------|--------|---------|-----------|-----------|
| 4           | INSTITUTION            | \# | -- | -- | \#  | --    | --    |
| 4.001       | MASTER FILE PARAMETERS | @  | @  | @  | @   | @     | @     |
| 4.1         | FACILITY TYPE          | -- | -- | -- | --  | --    | --    |

<span id="_Toc159835466" class="anchor"></span>Table 7‑4. File security for files exported with IFR-related software

#### References

The following directive specifies Station Number distribution requirements with regards to the IMF file updates associated with the IFR-related software (i.e., Kernel Patch XU\*8.0\*206):
Per VHA DIRECTIVE 97-058, which provides guidance for the assignment of Station Number suffix identifiers for outpatient clinic facilities, all outpatient clinic facilities will be given a Station Number suffix identifier. Requests to add or delete an outpatient clinic are submitted to the Director, Information Management Service (045A4) through the Chief Network Office (10N) at VHA Headquarters. The Network Management Support Office (10NA) notifies the respective VISN of the approved Station Number suffix identifier.
|                                                                                                                |                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/136.png) | REF: For further reference information, please refer to "Appendix A—Reference Materials" in this manual. |

#### Official Policies

No additional legal requirements are imposed on VistA by the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) users, nor does the IFR-related software relieve users of any previously established requirements.

Distribution of the Institution File Redesign (IFR)-related software (i.e., Kernel Patch XU\*8.0\*206) is unrestricted.

### Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<tbody>
<tr class="odd">
<td>ADPAC</td>
<td><strong>A</strong>utomated <strong>D</strong>ata <strong>P</strong>rocessing <strong>A</strong>pplication <strong>C</strong>oordinator.</td>
</tr>
<tr class="even">
<td>ARRAY</td>
<td>An arrangement of elements in one or more dimensions. An M array is a set of nodes referenced by subscripts that share the same variable name.</td>
</tr>
<tr class="odd">
<td>CIRN</td>
<td><strong>C</strong>linical <strong>I</strong>nformation <strong>R</strong>esource <strong>N</strong>etwork.</td>
</tr>
<tr class="even">
<td>DATA DICTIONARY (DD)</td>
<td><p>The <strong>D</strong>ata <strong>D</strong>ictionary is a global containing a description of what kind of data is stored in the global corresponding to a particular file. VA FileMan uses the data internally for interpreting and processing files.</p>
<p>A Data Dictionary contains the definitions of a file's elements (fields or data attributes); its relationship to other files; and the file structure or design. Users generally review the definitions of a file's elements or data attributes; programmers review the definitions of a file's internal structure.</p></td>
</tr>
<tr class="odd">
<td>FACILITY</td>
<td>Geographic location at which VA business is performed.</td>
</tr>
<tr class="even">
<td>FMF</td>
<td><strong>F</strong>acility Type <strong>M</strong>aster <strong>F</strong>ile.</td>
</tr>
<tr class="odd">
<td>HEALTH LEVEL SEVEN (HL7)</td>
<td>National level standard for data exchange in all healthcare environments regardless of individual computer application systems.</td>
</tr>
<tr class="even">
<td>IMF</td>
<td><strong>I</strong>nstitution <strong>M</strong>aster <strong>F</strong>ile.</td>
</tr>
<tr class="odd">
<td>INSTITUTION</td>
<td>A Veterans Affairs (VA) facility assigned a number by headquarters, as defined by Directive 97-058. An entry in the INSTITUTION file (#4) that represents the Veterans Health Administration (VHA).</td>
</tr>
<tr class="even">
<td>INSTITUTION MASTER FILE ADMINISTRATORS</td>
<td>The person or persons responsible for the maintenance of and updates to the master files either on FORUM or at a local site.</td>
</tr>
<tr class="odd">
<td>LEGACY FACILITY</td>
<td>An integrated facility. When two or more facilities integrate, the legacy facilities become DIVISIONS of the primary facility.</td>
</tr>
<tr class="even">
<td>MASTER FILES</td>
<td>A set of common reference files used by one or more applications.</td>
</tr>
<tr class="odd">
<td>MFN</td>
<td><strong>M</strong>aster <strong>F</strong>ile <strong>N</strong>otification (HL7 segment).</td>
</tr>
<tr class="even">
<td>MFQ</td>
<td><strong>M</strong>aster <strong>F</strong>ile <strong>Q</strong>uery (HL7 segment).</td>
</tr>
<tr class="odd">
<td>MFR</td>
<td><strong>M</strong>aster <strong>F</strong>ile <strong>R</strong>esponse (HL7 segment)</td>
</tr>
<tr class="even">
<td>MFS</td>
<td><strong>M</strong>aster <strong>F</strong>ile <strong>S</strong>erver.</td>
</tr>
<tr class="odd">
<td>MPI/PD</td>
<td><strong>M</strong>aster <strong>P</strong>atient <strong>I</strong>ndex/<strong>P</strong>atient <strong>D</strong>emographics</td>
</tr>
<tr class="even">
<td>NDBI</td>
<td><strong>N</strong>ational <strong>D</strong>ata <strong>B</strong>ase <strong>I</strong>ntegration.</td>
</tr>
<tr class="odd">
<td>NPI</td>
<td><strong>N</strong>ational <strong>P</strong>rovider <strong>I</strong>dentifier (a.k.a. National Provider Identifier).</td>
</tr>
<tr class="even">
<td>PARENT FACILITY</td>
<td><p>A station that has one or more facilities under the auspices of its director.</p>
<p>![](ifr-xu-8-206-416-supplement-to-patch-description/137.png) <strong>NOTE:</strong> Kernel Patch XU*8.0*294 prevents the adding of a VISN or PARENT FACILITY association to an Institution entry that does not have a corresponding PARENT OF ASSOCIATION.<br />
<br />
Kernel Patch XU*8.0*335 (i.e., Health<em>e</em>Vet cleanup) pointed all child facilities to their administrative parent. The parent, or primary facility, points to its parent (HCS or VISN). The HCS entries point to a VISN entry. All parent relationships eventually resolve to a VISN.</p></td>
</tr>
<tr class="odd">
<td>STATION</td>
<td>A field facility or group of field facilities.</td>
</tr>
<tr class="even">
<td>STATION NUMBER</td>
<td>A unique identifier assigned to any organizationally meaningful grouping of stations or facilities.</td>
</tr>
<tr class="odd">
<td>VAST</td>
<td><strong>V</strong>eterans <strong>A</strong>ffairs <strong>S</strong>tation <strong>T</strong>racker.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](ifr-xu-8-206-416-supplement-to-patch-description/138.png)</td>
<td><p><strong>REF:</strong> For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the ISS Glossary Web page at the following Web address:</p>
<blockquote>
<p><a href="http://vaww.vista.med.va.gov/iss/glossary.asp">http://vaww.vista.med.va.gov/iss/glossary.asp</a></p>
</blockquote>
<p>For a comprehensive list of acronyms, please visit the ISS Acronyms Web site at the following Web address:</p>
<blockquote>
<p><a href="http://vaww.vista.med.va.gov/iss/acronyms/index.asp">http://vaww.vista.med.va.gov/iss/acronyms/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

### Appendix A—Reference Materials

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a list of supporting documents that were reviewed and contributors that were consulted throughout this project. Much of the content/information has been utilized/incorporated in the IFR (i.e., Kernel Patch XU\*8.0\*206) software and documentation (documents listed in date order—earliest to latest):

- <u>VHA DIRECTIVE 97-058</u>, Dated November 24, 1997
- Institution Identification Design Specification draft, Dated January 6, 1998
- <u>INSTITUTION FILE CLEAN-UP</u>, Exchange e-mail message thread initiated by DBA REDACTED
- <u>INSTITUTION FILE REDESIGN PROJECT</u>, Initial Requirements Analysis (IRA), Dated April 2, 1998, Revised July 11, 1998
- <u>REPORT OF TECHNICAL REVIEW: INSTITUTION FILE REDESIGN</u>, Exchange e-mail message thread initiated REDACTED December 21, 1998
- <u>Institution File Redesign Project</u> \[#28736294\] 08 Jan 99, From: REDACTED
- <u>INSTITUTION/FM DBIA</u> \[#29276272\] 24 Mar 99, From: REDACTED
- <u>REPORT OF TECHNICAL REVIEW: INSTITUTION FILE REDESIGN, PHASE 2</u>, e-mail message thread initiated by REDACTED
- <u>VAST STATIONS</u>, Exchange e-mail message thread initiated REDACTED of Office of Policy and Planning, Dated July 27, 1999
- <u>STATION NUMBER INVENTORY</u>, Exchange e-mail message thread initiated by REDACTED of CO, Dated September 22, 1999
- <u>STATION TABLE</u>, Exchange e-mail message thread initiated by REDACTED, Dated September 22, 1999
- <u>FYI: SHOULD BE PART OF FILE 4 CLEANUP</u>, Exchange e-mail message thread initiated by REDACTED, Dated November 15, 1999
- <u>INSTITUTION FILE PATCH ISSUES</u>, Exchange e-mail message thread initiated REDACTED
- <u>NED AND DATA QUALITY ISSUES</u>, Exchange e-mail message thread initiated by REDACTED
- <u>STATION NUMBERS/INSTITUTION FILE</u>, Exchange e-mail message thread initiated by REDACATED
- <u>INSTITUTION FILE UPDATES</u>, Exchange e-mail message thread initiated by REDACTED
- <u>2/18 INSTALL</u>, Exchange e-mail message thread initiated by REDACTED, Dated February 22, 2000
- <u>Institution GOLD file</u> \[#30950058\] 02 Mar 00, From: REDACTED
- <u>Institution file clean up</u> \[#30977229\] 08 Mar 00, From: REDACTED
- <u>INSTITUTION File (#4) Redesign project</u> \[#31043748\] 22 Mar 00,From: REDACTED
- <u>FORUM INSTITUTION FILE</u> \[#31069930\] 28 Mar 00, From: REDACTED
- <u>Problem with Record Tracking and CIRN</u>, Exchange e-mail message thread initiated by REDACTED
- <u>Institution file patch impacts on HEC</u>, Exchange e-mail message thread initiated by REDACTED

|                                                                                                                |                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](ifr-xu-8-206-416-supplement-to-patch-description/139.png) | REF: For a list of other acknowledgements for this project, please refer to the "Acknowledgements" section in this manual. |

### Appendix B—Facility Type Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the current TYPE acronyms/codes and their associated Full Name/Definition:

| Type (Acronym) | Full Name (Description)                                   |
|--------------------|---------------------------------------------------------------|
| AIMC               | ACADEMIC AFFAIRS INF. MGMT CENTER                             |
| AO                 | AREA OFFICE                                                   |
| AR                 | ACCOUNTS RECEIVABLE                                           |
| BDC                | BENEFITS DELIVERY CENTER                                      |
| BIRLS              | BENEFICIARY INFORMATION RECORD LOCATOR SYSTEM                 |
| CBOC               | COMMUNITY BASED OUTPATIENT CLINIC                             |
| CC                 | CONFEDERATE CEMETERY                                          |
| CHAMPUS            | CIVILIAN HEALTH AND MEDICAL PROGRAM OF THE UNIFORMED SERVICES |
| CHAMPVA            | CIVILIAN HEALTH AND MEDICAL PROGRAM VETERANS ADMINISTRATION   |
| CHEP               | COOPERATIVE HEALTH EDUCATION PROGRAM                          |
| CIVH               | CIVILIAN HOSPITAL                                             |
| CM                 | CONFEDERATE MONUMENT                                          |
| CMOPC              | CONSOLIDATED MAIL OUTPATIENT PHARMACY                         |
| CO                 | CENTRAL OFFICE                                                |
| CP                 | CONFEDERATE PLOT                                              |
| D                  | DOMICILIARY                                                   |
| DEC                | DENTAL EDUCATION CENTER                                       |
| DENT               | DENTAL CLINIC                                                 |
| DOD                | DEPARTMENT OF DEFENSE                                         |
| DPC                | VA DATA PROCESSING CENTER                                     |
| EES                | EMPLOYEE EDUCATION SYSTEMS                                    |
| ETC                | ENGINEERING TRAINING CENTER                                   |
| GC                 | GENERAL COUNSEL                                               |
| GL                 | GOVERNMENT LOT                                                |
| HOST               | HOSPITAL OPEN SYSTEMS TECHNOLOGY                              |
| IG                 | INSPECTOR GENERAL                                             |
| HIS                | INDIAN HEALTH SERVICE                                         |
| IHSD               | IHS DEVELOPMENT CENTER                                        |
| IVMP               | INCOME VERIFICATION MATCH PROGRAM                             |
| M&ROC              | MEDICAL AND REGIONAL OFFICE CENTER                            |
| MC(M)              | MEDICAL CENTER (MEDICAL LOCATION)                             |
| MORC               | MOBILE OUTREACH CLINIC                                        |
| MPI                | MASTER PATIENT INDEX                                          |
| MSN                | MEMORIAL SERVICE NETWORK                                      |
| MUG                | MUMPS USERS GROUP                                             |
| NAC                | NATIONAL ACQUISITION CENTER                                   |
| NC                 | NATIONAL CEMETERY                                             |
| NCSO               | NATIONAL CEMETERY STATION OFFICE                              |
| NHC                | NURSING HOME CARE                                             |
| NIB                | NATIONAL INDUSTRIES FOR THE BLIND                             |
| NOA                | NOTICE OF APPEAL                                              |
| NVA                | FEDERAL HOSPITAL (OTHER)                                      |
| OC                 | OUTPATIENT CLINIC (INDEPENDENT)                               |
| OCMC               | OUTPATIENT CLINIC (SUBORDINATE)                               |
| OCS                | OUTPATIENT CLINIC SUBSTATION                                  |
| OIFO               | OFFICE OF INFORMATION FIELD OFFICE                            |
| OIG/ROA            | REGIONAL OFFICE OF AUDIT                                      |
| OIG/ROI            | REGIONAL OFFICE OF INVESTIGATIONS                             |
| OIG/SOA            | SUB OFFICE OF AUDIT                                           |
| OPC                | OUT PATIENT CLINIC                                            |
| ORC                | OUTREACH CLINIC                                               |
| OTHER              | OTHER                                                         |
| PDC                | PROSTHETIC DISTRIBUTION CENTER                                |
| PHARM              | PHARMACY                                                      |
| PHS                | PUBLIC HEALTH SERVICE HOSPITAL                                |
| PRDC               | PROSTHETICS RESEARCH AND DEVELOPMENT CENTER                   |
| PRRTP              | PSYCHOLOGICAL RESIDENTIAL REHAB TREATMENT PROGRAM             |
| PUBH               | PUBLIC HOSPITAL                                               |
| RO                 | REGIONAL OFFICE                                               |
| RO&IC              | REGIONAL OFFICE AND INSURANCE CENTER                          |
| RO-OC              | REGIONAL OFFICE - OUTPATIENT CLINIC                           |
| RPC                | RECORDS PROCESSING CENTER                                     |
| RPVM               | REPUBLIC OF PHILIPPINES VETERANS MEMORIAL                     |
| SARRTP             | SUBSTANCE ABUSE REHAB TREATMENT PROGRAM                       |
| SD                 | SUPPLY DEPOT                                                  |
| SDC                | SYSTEMS DEVELOPMENT CENTER                                    |
| SL                 | SOLDIERS LOT                                                  |
| SOC                | SATELLITE OUTPATIENT CLINIC                                   |
| STDIR              | STATE DIRECTORS OF VA                                         |
| STDM               | STATE DOMICILIARY                                             |
| STHH               | STATE HH                                                      |
| STNB               | STATE NURSING BEDS                                            |
| SVH                | STATE VETERANS HOME                                           |
| USAF               | US AIR FORCE HOSPITAL                                         |
| USAH               | US ARMY HOSPITAL                                              |
| USCG               | US COAST GUARD HOSPITAL                                       |
| USMC               | US MARINE CORP HOSPITAL                                       |
| USNH               | US NAVAL HOSPITAL                                             |
| VAIP               | VA INSURANCE PAYMENT                                          |
| VAMC               | VA MEDICAL CENTER                                             |
| VANB               | VA NURSING BEDS                                               |
| VANPH              | NEURAL PSYCHIATRIC HOSPITAL                                   |
| VASDC              | VA SERVICE & DISTRIBUTION CENTER                              |
| VBA                | VETERANS BENEFITS ADMINISTRATION                              |
| VBAML              | VBA MORTGAGE LOAN                                             |
| VCSFC              | VETERANS CANTEEN SERVICE FINANCE CENTER                       |
| VCSFO              | VETERANS CANTEEN SERVICE FIELD OFFICE                         |
| VEND/CONS          | VENDOR/CONSULTANT                                             |
| VET CENTER         | VETERANS CENTER                                               |
| VISN               | VETERANS INTEGRATED SERVICE NETWORK                           |

<span id="table_d1" class="anchor"></span>Table B-1. Facility type acronyms

### Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$
\$\$ACTIVE^XUAF4, 5-1
\$\$ADDNPI^XUSNPI API, 1-11
\$\$CIRN^XUAF4, 5-2
\$\$ID^XUAF4, 5-3
\$\$IDX^XUAF4, 5-4
\$\$IEN^XUAF4, 5-4
\$\$IEN^XUMF, 5-5
\$\$LEGACY^XUAF4, 5-6
\$\$LKUP^XUAF4, 5-7
\$\$MADD^XUAF4, 5-7
\$\$NAME^XUAF4, 5-8
\$\$NNT^XUAF4, 5-8
\$\$NS^XUAF4, 5-9
\$\$O99^XUAF4, 5-9
\$\$PADD^XUAF4, 5-10
\$\$PRNT^XUAF4, 5-11
\$\$RF^XUAF4, 5-11
\$\$RT^XUAF4, 5-12
\$\$STA^XUAF4, 5-13
\$\$TF^XUAF4, 5-13
\$\$WHAT^XUAF4, 5-14
A
Acknowledgements, xv
ACOS HOSPITAL ID Field (#51), 2-54, 2-58
Acronyms
Facility Types
B, 1
TYPE
B, 1
Acronyms (ISS)
Home Page Web Address, Glossary, 2
Actions
Auto update with national data (AUTO), 2-19, 2-34
Delete local/dup. station \# (DSTA), 2-16, 2-27
List local station numbers (LLCL), 2-15, 2-23
List national data to merge (NATL), 2-16, 2-26
Required clean up actions (CHCK), 2-20, 2-35
Resolve duplicate station numbers (RDSN), 2-18, 2-30
ACTIVATED FACILITY Field (#.08), 4-5
ACTIVE by Custodial Package Option, 6-24
Add/Modify Local Institution Data, 2-48
Step-By-Step Procedures, 2-49
Added Fields
FACILITY TYPE File (#4.1), 4-7
INSTITUTION File (#4), 4-1
Adding a New *Local* Entry, 2-51
Address
Edit, 2-50
Verify Address Updates, 2-50
Adobe Acrobat Quick Guide Web Address, xx
Adobe Home Page Web Address, xx
AGENCY CODE Field (#95), 2-3, 2-38, 2-42, 2-46, 2-54, 2-58, 4-3
APIs
\$\$ADDNPI^XUSNPI, 1-11
Appendix A—Reference Materials
A, 1
Appendix B—Facility Type Acronyms
B, 1
Application Entry Points, 6-15
Application Program Interfaces (APIs), 5-1
INSTITUTION File (#4), 1-9
MFS, 1-8
Archiving, 6-14, 7-3
ASSOCIATIONS Field (#.01), 2-54, 2-58
ASSOCIATIONS Multiple Field (#14), 2-2, 2-3, 2-38, 2-39, 2-42, 2-45, 2-54, 2-58, 3-4
Assumptions About the Reader, xix
Austin Automation Center (AAC) Coordination Requirements, 1-2
Auto update with national data (AUTO)
Action, 2-19, 2-34
Protocol, 6-7
B
Broadcast Updates, 1-7
Bulletins, 6-5
XUMF ERROR, 6-5
XUMF INSTITUTION, 6-5
C
Callable Routines, 6-15
Callout Boxes, xviii
CDSYS^XUAF4, 5-14
Change Notifications
Processing Master Files, 3-1
CHILDREN^XUAF4, 5-15
CITY (MAILING) Field (#4.03), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
CITY Field (#1.03), 1-9, 2-3, 2-38, 2-42, 2-43, 4-1
Cleanup Process
Health*e*Vet
INSTITUTION File (#4), 2-38
Initial
INSTITUTION File (#4), 2-13
Kernel Patch XU\*8.0\*206
Initial Cleanup Patch, 2-2
Kernel Patch XU\*8.0\*335
Health*e*Vet Cleanup Patch, 2-3
Local Sites
Health*e*Vet Institution File Cleanup Process, 2-41
Initial Institution File Cleanup Process, 2-21
Protocols, 6-7
Templates, 6-7
CODING SYSTEM Field (#.01), 4-5
Communications Interfaces, 6-19, 7-4
Contents, vii
Controlled Subscription References, 5-1, 6-23
Custodial Package Menu, 6-24
D
Data Dictionary
Additions
INSTITUTION File (#4), 4-1
Data Dictionary Utilities Menu, xviii
Listings, xviii
Modifications, 4-1
FACILITY TYPE File (#4.1), 1-10, 4-7
INSTITUTION File (#4), 1-8, 1-9, 1-11, 4-1
NEW PERSON File (#200), 1-10
Data Review/Check
INSTITUTION File (#4), 2-1
DBA IA CUSTODIAL MENU, 6-24
DBA IA CUSTODIAL Option, 6-24
DBA IA INQUIRY Option, 6-24
DBA IA ISC Menu, 6-24
DBA IA SUBSCRIBER MENU, 6-24
DBA IA SUBSCRIBER Option, 6-24
DBA INSTITUTION INQUIRE Option, 2-5
DBA Menu, 6-24
DEACTIVATED FACILITY / STA \# Field (#.07), 4-5
Delete local/dup. station \# (DSTA)
Action, 2-16, 2-27
Protocol, 6-7
Template, 6-7
Deleting an Existing Entry, 2-56
Dependencies, 6-21
Detailed Solution
Kernel Patch XU\*8.0\*206, 1-2
Developer's Guide, II-1
Directives, 7-8
VHA DIRECTIVE 97-058, 1-4, 7-8
DIVISION Field (#.01), 1-10
DIVISION Multiple Field (#16), 1-10
Documentation
Revisions, iii
Symbols, xvii
DOMAIN Field (#60), 2-54, 2-58
DS Pub Man\~~L
HL7 Application Parameter, 6-5
Protocols, 6-6
DTS Term Srv\~~L
HL7 Application Parameter, 6-5
Protocols, 6-6
DTS Terminology Server
HL7 Application Parameters, 6-5
Protocols, 6-6
Duplicate station number menu
Protocol, 6-7
Duties
FORUM (Production) Institution Master File Administrators, 3-1
Local Site Institution Master File Administrator, 2-1
Local Site Institution Master File Administrators
Introduction, 2-1
Production (FORUM) Institution Master File Administrators, 3-1
E
Edit Address, 2-50
EFFECTIVE DATE Field (#.01), 3-4, 4-4
HISTORY Multiple Field (#999), 2-2, 2-20
Electronic Signatures, 7-4
Enhancements
INSTITUTION File (#4), 1-8
Entry Points, 6-15
EVS Anonymous Directories, xx
Exported Options, 6-11
External
Interfaces, 6-18
Relations, 6-20
F
F4^XUAF4, 5-16
FACILITY TYPE (#13), 3-3
Facility Type Acronyms
B, 1
FACILITY TYPE Field (#13), 1-11, 2-39, 4-3
INSTITUTION File (#4), 2-2, 2-3, 2-20, 2-38, 2-42, 2-44, 2-53, 2-55, 2-57, 2-58, 4-6
FACILITY TYPE file (#4.1), 3-3
FACILITY TYPE File (#4.1), 1-1, 1-2, 2-13, 2-14, 2-21, 3-1, 6-10
Cleanup Utilities, 1-3
Data Dictionary
Modifications, 1-10, 4-7
Editing the Master File on FORUM, 3-2
Fields, 4-7
Master File on FORUM, 1-2, 1-3, 1-5
Modified/Added Fields, 4-7
Security, 7-8
Fields
ACOS HOSPITAL ID (#51), 2-54, 2-58
ACTIVATED FACILITY (#.08), 4-5
AGENCY CODE (#95), 2-3, 2-38, 2-42, 2-46, 2-54, 2-58, 4-3
ASSOCIATIONS (#.01), 2-54, 2-58
ASSOCIATIONS Multiple (#14), 2-2, 2-3, 2-38, 2-39, 2-42, 2-45, 2-54, 2-58, 3-4
CITY (#1.03), 1-9, 2-3, 2-38, 2-42, 2-43, 4-1
CITY (MAILING) (#4.03), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
CODING SYSTEM (#.01), 4-5
DEACTIVATED FACILITY / STA \# (#.07), 4-5
DIVISION (#.01), 1-10
DIVISION Multiple (#16), 1-10
DOMAIN (#60), 2-54, 2-58
EFFECTIVE DATE (#.01), 2-20, 3-4, 4-4
HISTORY Multiple Field (#999), 2-2
FACILITY TYPE (#13), 1-11, 3-3, 4-3
INSTITUTION File (#4), 2-2, 2-3, 2-20, 2-38, 2-42, 2-44, 2-53, 2-55, 2-57, 2-58, 4-6
FACILITY TYPE File (#4.1), 4-7
HISTORY Multiple (#999), 1-3, 1-9, 2-2, 2-20, 3-4, 4-4, 4-6, 5-11, 5-12
ID (#.02), 4-5
IDENTIFIER Multiple (#9999), 4-5, 5-3, 5-4, 5-17, 6-16
INACTIVE FACILITY FLAG (#101), 2-2, 2-3, 2-20, 2-38, 2-42, 2-47, 3-4, 4-4, 4-6
NAME (#.01), 3-3, 4-1
INSTITUTION File (#4), 2-2, 2-3, 2-20, 2-38, 2-42, 2-43, 2-53, 2-55, 2-57, 2-58
NAME (CHANGED FROM) (#.02), 4-4
Obsolete
G&L HEADER (#10), 4-6
MAILMAN FLAG (#12), 4-6
OLD AMIS NUMBER (#77), 4-6
OUTPUT HEADER (#.04), 4-6
PACKAGE X-REF (#30), 4-6
STATION NAME (#7), 4-6
OFFICIAL VA NAME (#100), 2-2, 2-3, 2-20, 2-38, 2-42, 2-43, 2-47, 2-54, 2-55, 2-58, 3-4, 3-5, 4-4
OFFICIAL VA NAME (CHANGED FROM) (#.03), 4-4
PARENT OF ASSOCIATION (#1), 2-3, 2-38, 2-42, 2-54, 2-58
REALIGNED FROM (#.06), 2-20, 4-4
HISTORY Multiple Field (#999), 2-2
REALIGNED TO (#.05), 2-20, 4-4
HISTORY Multiple Field (#999), 2-2
Referenced
VA TYPE CODE, 6-10
ST. ADDR. 1 (MAILING) (#4.01), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
ST. ADDR. 2 (MAILING) (#4.02), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
STATE (#.02), 1-10, 2-3, 2-38, 2-42, 2-43, 3-4, 4-1
INSTITUTION File (#4), 2-2, 2-3, 2-20, 2-38, 2-42, 2-43, 2-53, 2-55, 2-57, 2-58, 4-6
STATE (MAILING) (#4.04), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
STATION NAME (#7), 2-20
STATION NUMBER (#99), 3-3
C, 3-3
INSTITUTION File (#4), 2-2, 2-5, 2-9, 2-10, 2-11, 2-13, 2-14, 2-17, 2-18, 2-20, 2-23, 2-24, 2-28, 2-29, 2-32, 2-48, 2-54, 2-55, 2-58, 2-59, 3-2, 3-3, 3-5, 4-3, 4-4, 4-5, 4-6, 5-4, 5-6, 5-9, 5-11, 5-13, 5-16, 5-18, 6-15, 6-16
STATUS (#11)
INSTITUTION File (#4), 2-2, 2-19, 2-20, 2-48, 2-53, 2-55, 2-57, 2-58, 4-2
STATUS (#3), 1-10, 2-39
FACILITY TYPE File (#4.1), 4-7
STREET ADDR. 1 (#1.01), 1-9, 2-3, 2-38, 2-42, 2-43, 4-1
STREET ADDR. 2 (#1.02), 1-9, 2-3, 2-38, 2-42, 2-43, 4-1
TCP/IP ADDRESS, 2-41
XUMF FORUM, 2-41
ZIP (#1.04), 1-10, 2-3, 2-38, 2-42, 2-43, 4-2
ZIP (MAILING) (#4.05), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
Figures and Tables, xi
Files, 6-10
Data Review
INSTITUTION File (#4), 2-1
FACILITY TYPE (#4.1), 2-13, 2-14, 2-21, 3-1, 3-3, 6-10
Editing the Master File on FORUM, 3-2
Master File on FORUM, 1-2, 1-3, 1-5
Security, 7-8
Health*e*Vet Cleanup Process
INSTITUTION File (#4), 2-38
HL LOGICAL LINK (#870), 2-41
HL7 MESSAGE TEXT (#772), 1-8, 5-19
Initial Cleanup Process
INSTITUTION File (#4), 2-13
INSTITUTION (#4), 1-3, 1-5, 1-6, 1-11, 2-2, 2-3, 2-13, 2-14, 2-15, 2-16, 2-17, 2-18, 2-19, 2-20, 2-21, 2-22, 2-23, 2-25, 2-26, 2-27, 2-28, 2-29, 2-30, 2-34, 2-35, 2-38, 2-39, 2-40, 2-41, 2-42, 2-48, 2-49, 2-54, 2-56, 2-63, 3-1, 3-2, 3-3, 5-1, 5-2, 5-3, 5-4, 5-6, 5-7, 5-8, 5-9, 5-10, 5-11, 5-12, 5-13, 5-14, 5-16, 5-17, 5-18, 6-10, 6-15, 6-16
Add/Modify Local Institution Data, 2-48
Data Review/Check, 2-1
Editing the Master File on FORUM, 3-2
Health*e*Vet Cleanup Utilities, 2-38
Initial Cleanup Utilities, 2-13
Maintenance
Site, 2-63
Master File on FORUM, 1-4, 1-5, 3-1
Security, 7-8
Troubleshooting
FORUM, 3-8
INSTITUTION ASSOCIATION TYPES (#4.05), 5-25, 5-26
MASTER FILE PARAMETERS (#4.001), 1-5, 1-10, 6-10
Security, 7-8
MEDICAL CENTER DIVISION (#40.8), 2-8
NEW PERSON (#200), 1-10, 2-47
Data Dictionary Modifications, 1-10
Numbers, 6-26
Security, 7-8
FORUM
Facility Type Master File (FMF), 1-5
Institution Master File (IMF), 1-4
Institution Master File Administrator Duties, 3-1
Step-By-Step Procedures
Processing Master File Changes, 3-1
Troubleshooting, 3-8
FTP, xx
G
REDACTED Mail Group, 2-13
General Instructions for Obtaining IAs on FORUM, 6-24
Global Locations, 6-26
Glossary, 1
ISS Home Page Web Address, Glossary, 2
Guidelines
Updates to the Local INSTITUION File (#4), 2-42
H
Handle
Query Response, 1-7
Update Message, 1-7
Hardware Interfaces, 6-18, 7-3
Health*e*Vet Institution File Cleanup Process
Step-By-Step Procedures, 2-41
Help
At Prompts, xviii
Online, xviii
Question Marks, xviii
HISTORY Multiple Field (#999), 1-3, 1-9, 2-2, 2-20, 3-4, 4-4, 4-6, 5-11, 5-12
HL LOGICAL LINK File (#870), 2-41
HL START Option, 2-41
HL7
Application Parameters, 6-5
DS Pub Man\~~L, 6-5
DTS Term Srv\~~L, 6-5
Master File Application ACK, 6-5
Master File Notification, 6-5
Master File Notification (VistA-to-VistA), 6-5
Master File Parameters, 6-5
Master File Parameters Query Response, 6-5
MFS Handler, 6-5
MFS Query, 6-5
MFS Query Response, 6-5
XUMF MFK, 6-5
XUMF MFN, 6-5
XUMF MFP MFQ, 6-5
XUMF MFP MFR, 6-5
XUMF MFQ, 6-5
XUMF MFR, 6-5
XUMF MFS, 6-5
XUMF SERVER, 6-5
Logical Link, 6-6
Master File Server (MFS), 6-6
XUMF ACK, 6-6
XUMF FORUM, 6-6
HL7 Application Parameters
DTS Terminology Server, 6-5
Master File Notification, 6-5
HL7 Logical Link
MFS Application Acknowledgement, 6-6
HL7 MESSAGE TEXT File (#772), 1-8, 5-19
Home Pages
Adobe Acrobat Quick Guide Web Address, xx
Adobe Web Address, xx
HSD&D Home Page Web Address, xix
IFR Home Page Web Address, xix
ISS
Acronyms Home Page Web Address, Glossary, 2
Glossary Home Page Web Address, Glossary, 2
Kernel Home Page Web Address, xix
VistA Documentation Library (VDL) Home Page Web Address, xx
How to
Obtain Technical Information Online, xviii
Use this Manual, xvii
HSD&D
Home Page Web Address, xix
I
ID Field (#.02), 4-5
IDENTIFIER Multiple Field (#9999), 4-5, 5-3, 5-4, 5-17, 6-16
IFR Home Page Web Address, xix
IMF Display Cleanup Status Option, 2-39, 2-41, 6-12, 7-6
IMF edit option, 6-12
IMF edit Option, 2-39, 2-41, 2-49, 2-50, 7-5
Implementation, 6-1
INACTIVE FACILITY FLAG Field (#101), 2-2, 2-3, 2-20, 2-38, 2-42, 2-47, 3-4, 4-4, 4-6
Initial Institution File Cleanup Process
Local Sites
Step-By-Step Procedures, 2-21
Input Transform, 1-8, 1-10, 1-11, 2-39, 4-2, 4-3
Inquire Option, 6-24
INSTALL/CHECK MESSAGE Option, 6-2
Installation Instructions, 6-1
Installation Menu (KIDS), 6-3
INSTITUTION ASSOCIATION TYPES File (#4.05), 5-25, 5-26
Institution Edit Option, 2-48, 2-50, 2-53, 6-25
INSTITUTION File (#4), 1-1, 1-2, 1-3, 1-5, 1-6, 1-11, 2-2, 2-3, 2-13, 2-14, 2-15, 2-16, 2-17, 2-18, 2-19, 2-20, 2-21, 2-22, 2-23, 2-25, 2-26, 2-27, 2-28, 2-29, 2-30, 2-34, 2-35, 2-38, 2-39, 2-40, 2-41, 2-42, 2-48, 2-49, 2-54, 2-56, 2-63, 3-1, 3-2, 3-3, 5-1, 5-2, 5-3, 5-4, 5-6, 5-7, 5-8, 5-9, 5-10, 5-11, 5-12, 5-13, 5-14, 5-16, 5-17, 5-18, 6-10, 6-15, 6-16
\$\$ACTIVE^XUAF4, 5-1
\$\$CIRN^XUAF4, 5-2
\$\$ID^XUAF4, 5-3
\$\$IDX^XUAF4, 5-4
\$\$IEN^XUAF4, 5-4
\$\$IEN^XUMF, 5-5
\$\$LEGACY^XUAF4, 5-6
\$\$LKUP^XUAF4, 5-7
\$\$MADD^XUAF4, 5-7
\$\$NAME^XUAF4, 5-8
\$\$NNT^XUAF4, 5-8
\$\$NS^XUAF4, 5-9
\$\$O99^XUAF4, 5-9
\$\$PADD^XUAF4, 5-10
\$\$PRNT^XUAF4, 5-11
\$\$RF^XUAF4, 5-11
\$\$RT^XUAF4, 5-12
\$\$STA^XUAF4, 5-13
\$\$TF^XUAF4, 5-13
\$\$WHAT^XUAF4, 5-14
Add/Modify Local Institution Data, 2-48
Application Program Interfaces (APIs), 1-9
CDSYS^XUAF4, 5-14
CHILDREN^XUAF4, 5-15
Cleanup Utilities, 1-3
Data Dictionary
Additions, 4-1
Modifications, 1-8, 1-9, 1-11, 4-1
Data Review/Check, 2-1
Editing the Master File on FORUM, 3-2
Enhancements, 1-8
F4^XUAF4, 5-16
Health*e*Vet Cleanup Utilities, 2-38
HISTORY Multiple Field (#999), 4-4
Initial Cleanup Utilities, 2-13
LOOKUP^XUAF4, 5-17
MAIN^XUMFI, 5-18
MAIN^XUMFP, 5-20
Maintenance
Site, 2-63
Master File on FORUM, 1-2, 1-3, 1-4, 1-5, 3-1
Modified/Added Fields, 4-1
Obsolete Fields Removed, 4-6
PARENT^XUAF4, 5-25
Pointer, 6-10
Security, 7-8
SIBLING^XUAF4, 5-26
Tracking, 1-8
Troubleshooting
FORUM, 3-8
Site, 2-63
Write Identifiers, 4-6
Institution File Data Review/Check
Step-By-Step Procedures, 2-4
Institution file inquire Option, 2-5, 2-11, 2-50
Institution File Query / Update Option, 2-13, 2-14, 2-15, 2-21, 2-39, 2-40, 6-4, 6-12, 6-25, 7-6
Institution File Redesign (IFR)
Application Program Interfaces (APIs), 5-1
Namespace, 6-26
Purpose, 1-1
Institution List by Parent Option, 2-9, 2-10
Institution List by VISN Option, 2-12
Institution Master File Edit Option, 3-1, 3-2, 6-11, 6-25, 7-1, 7-5, 7-8
Instructions
Installation, 6-1
Post Installation, 6-4
Integration Agreements (IAs), 6-22
Controlled Subscription References, 5-1, 6-23
General Instructions for Obtaining IAs from FORUM, 6-24
Integration Agreements Menu, 6-24
Supported References, 5-1, 6-22
Interfaces, 7-3
Communications, 6-19, 7-4
External, 6-18
Hardware, 6-18, 7-3
Software, 6-18, 7-3
Internal Relations, 6-25
Introduction, 1-1
Local Site Institution Master File Administrator Duties, 2-1
ISS
Acronyms
Home Page Web Address, Glossary, 2
Glossary
Home Page Web Address, Glossary, 2
K
Kernel
Home Page Web Address, xix
Kernel Management Menu, 2-48, 6-13
Namespace, 6-26
Patches
XU\*8.0\*206, 1-2
Detailed Solution, 1-2
Initial Cleanup Patch, 2-2
Purpose, 1-1
XU\*8.0\*217, 1-9
XU\*8.0\*287, 1-10
XU\*8.0\*299, 1-10
XU\*8.0\*335, 1-10
Health*e*Vet Cleanup Patch, 2-3
XU\*8.0\*416, 1-11, 2-40
Kernel Management Menu, 1-11, 2-40, 2-49, 6-14
Keys
Security, 7-8
KIDS Menu, 6-3
L
List File Attributes Option, xviii
List local data (LLCL)
Protocol, 6-7
Template, 6-7
List local station numbers (LLCL)
Action, 2-15, 2-23
List national data to merge (NATL)
Action, 2-16, 2-26
Protocol, 6-7
Template, 6-7
List Templates, 6-7
Load DMIS ID's Option, 6-11, 7-5
Load Institution (NPI) values Option, 1-11, 2-40, 6-14, 7-7
Local Data Entries, 2-48
Local Site Institution Master File Administrator Duties, 2-1
Introduction, 2-1
Local Sites
Step-By-Step Procedures
Add/Modify Local Institution Data, 2-49
Health*e*Vet Institution File Cleanup Process, 2-41
Initial Institution File Cleanup Process, 2-21
Institution File Data Review/Check, 2-4
Maintenance and Troubleshooting, 2-64
LOOKUP^XUAF4, 5-17
M
Mail Groups, 7-2
REDACTED, 2-13
XUMF ERROR, 1-10, 2-63, 2-64, 3-8, 6-19, 7-2, 7-4
XUMF INSTITUTION, 1-8, 2-42, 2-49, 2-63, 2-64, 3-6, 3-8, 6-19, 7-2, 7-4
XUMF INSTITUTION HSITES, 2-39
XUMF NPI, 1-11
XUMF SERVER, 2-49, 7-2
MAIN^XUMFI, 5-18
MAIN^XUMFP, 5-20
Maintenance, 6-5
Site, 2-63
Maintenance and Troubleshooting
Local Step-By-Step Procedures, 2-64
Master File Application ACK
HL7 Application Parameters, 6-5
Protocols, 6-6
Master File Notification
HL7 Application Parameters, 6-5
Protocols, 6-6
Master File Notification (VistA-to-VistA)
HL7 Application Parameters, 6-5
Protocols, 6-6
Master File Parameters
HL7 Application Parameters, 6-5
Protocols, 6-6
MASTER FILE PARAMETERS File (#4.001), 1-5, 1-10, 6-10
Security, 7-8
Master File Parameters Query Response
HL7 Application Parameters, 6-5
Protocols, 6-6
Master File Server (MFS), 1-5
HL7 Logical Link, 6-6
Protocols, 6-6
Master Files—What is the Problem?, 1-1
MEDICAL CENTER DIVISION File (#40.8), 2-8
Memory Constraints, 6-4
Menus
Custodial Package Menu, 6-24
Data Dictionary Utilities, xviii
DBA, 6-24
DBA IA CUSTODIAL MENU, 6-24
DBA IA ISC, 6-24
DBA IA SUBSCRIBER MENU, 6-24
Installation (KIDS), 6-3
Integration Agreements Menu, 6-24
Kernel Management Menu, 1-11, 2-40, 2-48, 2-49, 6-13, 6-14
KIDS, 6-3
Operations Management, 2-49
PackMan, 6-2
Security, 7-5
Subscriber Package Menu, 6-24
XPD INSTALLATION MENU (KIDS), 6-3
XPD MAIN (KIDS), 6-3
XUKERNEL, 1-11, 2-39, 2-40, 2-48, 2-49, 6-4, 6-13, 6-14
XUSITEMGR, 2-49
MFS Application Acknowledgement
HL7 Logical Link, 6-6
MFS Handler
HL7 Application Parameters, 6-5
Protocols, 6-6
MFS Query
HL7 Application Parameters, 6-5
Protocols, 6-6
MFS Query Response
HL7 Application Parameters, 6-5
Protocols, 6-6
Modified Fields
FACILITY TYPE File (#4.1), 4-7
INSTITUTION File (#4), 4-1
Modifying an Existing Entry, 2-53
N
NAME (CHANGED FROM) Field (#.02), 4-4
NAME Field (#.01), 3-3, 4-1
INSTITUTION File (#4), 2-2, 2-3, 2-20, 2-38, 2-42, 2-43, 2-53, 2-55, 2-57, 2-58
Names INSTITUTION vs. national
Protocol, 6-7
Template, 6-7
Namespace, 6-26
National Data Base Integration (NDBI) Procedures, 1-2
National Data Entries, 2-48
National Provider Identifier (NPI), 1-11, 2-40, 6-14, 7-7
NEW PERSON File (#200), 1-10, 2-47
Data Dictionary Modifications, 1-10
O
Obsolete Fields Removed
INSTITUTION File (#4), 4-6
Official Policies, 7-9
OFFICIAL VA NAME (CHANGED FROM) Field (#.03), 4-4
OFFICIAL VA NAME Field (#100), 2-2, 2-3, 2-20, 2-38, 2-42, 2-43, 2-47, 2-54, 2-55, 2-58, 3-4, 3-5, 4-4
Online
Documentation, xviii
Technical Information, How to Obtain, xviii
Operations, 6-4
Operations Management Menu, 2-49
Options
ACTIVE by Custodial Package, 6-24
Custodial Package Menu, 6-24
Data Dictionary Utilities, xviii
DBA IA CUSTODIAL, 6-24
DBA IA CUSTODIAL MENU, 6-24
DBA IA INQUIRY, 6-24
DBA IA SUBSCRIBER, 6-24
DBA INSTITUTION INQUIRE, 2-5
Exported, 6-11
HL START, 2-41
IMF Display Cleanup Status, 2-39, 2-41, 6-12, 7-6
IMF edit, 2-39, 2-41, 2-49, 2-50, 6-12, 7-5
Inquire, 6-24
INSTALL/CHECK MESSAGE, 6-2
Institution Edit, 2-48, 2-50, 2-53, 6-25
Institution file inquire, 2-5, 2-11, 2-50
Institution File Query / Update, 2-13, 2-14, 2-15, 2-21, 2-39, 2-40, 6-4, 6-12, 6-25, 7-6
Institution List by Parent, 2-9, 2-10
Institution List by VISN, 2-12
Institution Master File Edit, 3-1, 3-2, 6-11, 6-25, 7-1, 7-5
Kernel Management Menu, 1-11, 2-40, 6-14
List File Attributes, xviii
Load DMIS ID's, 6-11, 7-5
Load Institution (NPI) values, 1-11, 2-40, 6-14, 7-7
Operations Management, 2-49
Patch XU\*8\*335 clean 4.1 and 4, 2-39, 2-40, 6-13, 7-7
Print ACTIVE by Subscribing Package, 6-24
Security, 7-5
Start logical Links, 6-6
Start/Stop Links, 2-41
Update/refresh Institution file with IMF data, 2-40, 6-13, 7-6
*With* Parents, 6-14
*Without* Parents, 6-11
XU-INSTITUTION-E, 2-48, 2-50, 2-53, 6-25
XUKERNEL, 1-11, 2-39, 2-40, 6-14
XUMF DMIS ID LOAD, 6-11, 7-5
XUMF FORUM INSTITUTION, 3-1, 3-2, 6-11, 6-25, 7-1, 7-5, 7-8
XUMF IMF ADD EDIT, 2-39, 2-41, 2-49, 2-50, 6-12, 7-5
XUMF IMF BY PRNT, 2-9
XUMF IMF EDIT STATUS, 2-39, 2-41, 6-12, 7-6
XUMF INSTITUTION, 2-13, 2-14, 2-15, 2-21, 2-39, 2-40, 6-4, 6-12, 6-25, 7-6
XUMF LOAD INSTITUTION, 2-40, 6-13, 7-6
XUMF LOAD NPI, 1-11, 2-40, 6-14, 7-7
XUMF335 clean 4.1 and 4, 2-39, 2-40, 6-13, 7-7
XUSITEMGR, 2-49
Orientation, xvii
P
PackMan Menu, 6-2
Parameters
HL7 Application, 6-5
PARENT OF ASSOCIATION Field (#1), 2-3, 2-38, 2-42, 2-54, 2-58
PARENT^XUAF4, 5-25
Patch XU\*8\*335 clean 4.1 and 4 Option, 2-39, 2-40, 6-13, 7-7
Patches, 1-2
Patches
History, v
XU\*8.0\*206
Detailed Solution, 1-2
Purpose, 1-1
Patches
XU\*8.0\*206, 1-2
Patches
XU\*8.0\*217, 1-9
Patches
XU\*8.0\*287, 1-10
Patches
XU\*8.0\*299, 1-10
Patches
XU\*8.0\*335, 1-10
Patches
XU\*8.0\*416, 1-11
Patches
XU\*8.0\*206
Initial Cleanup Patch, 2-2
Patches
XU\*8.0\*335
Health*e*Vet Cleanup Patch, 2-3
Patches
XU\*8.0\*416, 2-40
Policies, Official, 7-9
Post Installation Instructions, 6-4
Print ACTIVE by Subscribing Package Option, 6-24
Procedures
FORUM
Processing Master File Changes, 3-1
Troubleshooting, 3-8
Local Sites
Add/Modify Local Institution Data, 2-49
Health*e*Vet Institution File Cleanup Process, 2-41
Initial Institution File Cleanup Process, 2-21
Institution File Data Review/Check, 2-4
Maintenance and Troubleshooting, 2-64
Processing Master File Changes
Step-By-Step Procedures, 3-1
Processing Master Files Change Notifications, 3-1
Production (FORUM)
Institution Master File Administrator Duties, 3-1
Protocols, 6-6
Cleanup Process, 6-7
DS Pub Man\~~L, 6-6
DTS Term Srv\~~L, 6-6
DTS Terminology Server, 6-6
Master File Application ACK, 6-6
Master File Notification, 6-6
Master File Notification (VistA-to-VistA), 6-6
Master File Parameters, 6-6
Master File Parameters Query Response, 6-6
Master File Server (MFS), 6-6
MFS Handler, 6-6
MFS Query, 6-6
MFS Query Response, 6-6
XUMF AUTO, 6-7
XUMF CHCK, 6-7
XUMF DSTA, 6-7
XUMF LLCL, 6-7
XUMF MFK, 6-6
XUMF MFN, 6-6
XUMF MFP MFQ, 6-6
XUMF MFP MFR, 6-6
XUMF MFQ, 6-6
XUMF MFR, 6-6
XUMF MFS, 6-6
XUMF NAME, 6-7
XUMF NATL, 6-7
XUMF RDSN, 6-7
XUMF RDSN MENU, 6-7
XUMF SERVER, 6-6
Purging, 6-14, 7-3
Purpose
Institution File Redesign (IFR)
Kernel Patch XU\*8.0\*206, 1-1
Q
Query Server, 1-7
Question Mark Help, xviii
R
Reader, Assumptions About the, xix
REALIGNED FROM Field (#.06), 4-4
HISTORY Multiple Field (#999), 2-2, 2-20
REALIGNED TO Field (#.05), 4-4
HISTORY Multiple Field (#999), 2-2, 2-20
Reference Materials, xix
A, 1
Reference Type
Controlled Subscription
MAIN^XUMFI, 5-18
MAIN^XUMFP, 5-20
Supported
\$\$ACTIVE^XUAF4, 5-1
\$\$CIRN^XUAF4, 5-2
\$\$ID^XUAF4, 5-3
\$\$IDX^XUAF4, 5-4
\$\$IEN^XUAF4, 5-4
\$\$IEN^XUMF, 5-5
\$\$LEGACY^XUAF4, 5-6
\$\$LKUP^XUAF4, 5-7
\$\$MADD^XUAF4, 5-7
\$\$NAME^XUAF4, 5-8
\$\$NNT^XUAF4, 5-8
\$\$NS^XUAF4, 5-9
\$\$O99^XUAF4, 5-9
\$\$PADD^XUAF4, 5-10
\$\$PRNT^XUAF4, 5-11
\$\$RF^XUAF4, 5-11
\$\$RT^XUAF4, 5-12
\$\$STA^XUAF4, 5-13
\$\$TF^XUAF4, 5-13
\$\$WHAT^XUAF4, 5-14
CDSYS^XUAF4, 5-14
CHILDREN^XUAF4, 5-15
F4^XUAF4, 5-16
LOOKUP^XUAF4, 5-17
PARENT^XUAF4, 5-25
SIBLING^XUAF4, 5-26
References, 7-8
Controlled Subscription, 5-1, 6-23
General Instructions for Obtaining IAs from FORUM, 6-24
Supported, 5-1, 6-22
Relations
External, 6-20
Internal, 6-25
Remote Systems, 7-2
Requesting a New Station Number, 1-2
Required clean up actions (CHCK)
Action, 2-20, 2-35
Protocol, 6-7
Template, 6-7
Requirements
Software, 6-20
Resolve duplicate station numbers (RDSN)
Action, 2-18, 2-30
Protocol, 6-7
Revision History, iii
Documentation, iii
Patches, v
Routines, 6-8
XUAF4, 6-8
XUMF, 6-8
XUMF218A, 6-8
XUMF261P, 6-8
XUMF299P, 6-8
XUMF33, 6-8
XUMF333, 6-8
XUMF4, 6-8
XUMF416, 6-8
XUMF4A, 6-8
XUMF4F, 6-8
XUMF4H, 6-8
XUMF4L0H, 6-8
XUMF4L1, 6-8
XUMF4L2, 6-8
XUMF512F, 6-8
XUMFEIMF, 6-8
XUMFENV, 6-3, 6-8
XUMFH, 6-8
XUMFH4, 6-8
XUMFHM, 6-8
XUMFHPQ, 6-8
XUMFHPR, 6-9
XUMFI, 6-9
XUMFI0, 6-9
XUMFMFE, 6-9
XUMFMFI, 6-9
XUMFP, 6-9
XUMFP4, 6-9
XUMFP4C, 6-9
XUMFP4Z, 6-9
XUMFP512, 6-9
XUMFP513, 6-9
XUMFPFT, 6-9
XUMFPMFS, 6-9
XUMFPOST, 4-6, 6-3, 6-9
XUMFPZL7, 6-9
XUMFR, 6-9
XUMFX, 6-9
XUMFXACK, 6-9
XUMFXH, 6-9
XUMFXHL7, 6-9
XUMFXI, 6-9
XUMFXP, 6-9
XUMFXP1, 6-9
XUMFXP2, 6-9
XUMFXR, 6-9
S
Security, 7-1
Archiving and Purging, 7-3
Electronic Signatures, 7-4
Files, 7-8
Interfaces, 7-3
Keys, 7-8
XUMF INSTITUTION, 2-39, 2-41, 2-49, 3-1, 6-11, 7-1, 7-5, 7-8
XUMGR, 1-10, 2-47
Mail Groups, 7-2
Menus/Options, 7-5
Official Policies, 7-9
References, 7-8
Remote Systems, 7-2
SIBLING^XUAF4, 5-26
Software
Interfaces, 6-18, 7-3
Product Security, 7-1
Requirements, 6-20
Software-wide Variables, 6-26
Special Operations, 6-4
ST. ADDR. 1 (MAILING) Field (#4.01), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
ST. ADDR. 2 (MAILING) Field (#4.02), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
Start logical Links Option, 6-6
Start/Stop Links Option, 2-41
STATE (MAILING) Field (#4.04), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
STATE Field (#.02), 1-10, 2-3, 2-38, 2-42, 2-43, 3-4, 4-1
INSTITUTION File (#4), 2-2, 2-3, 2-20, 2-38, 2-42, 2-43, 2-53, 2-55, 2-57, 2-58, 4-6
STATION NAME Field (#7), 2-20
STATION NUMBER Field (#99), 3-3
INSTITUTION File (#4), 2-2, 2-5, 2-9, 2-10, 2-11, 2-13, 2-14, 2-17, 2-18, 2-20, 2-23, 2-24, 2-28, 2-29, 2-32, 2-48, 2-54, 2-55, 2-58, 2-59, 3-2, 3-3, 3-5, 4-3, 4-4, 4-5, 4-6, 5-4, 5-6, 5-9, 5-11, 5-13, 5-16, 5-18, 6-15, 6-16
STATUS Field (#11)
INSTITUTION File (#4), 2-2, 2-19, 2-20, 2-48, 2-53, 2-55, 2-57, 2-58, 4-2
STATUS Field (#3), 1-10, 2-39
FACILITY TYPE File (#4.1), 4-7
Step-By-Step Procedures
FORUM
Processing Master File Changes, 3-1
Troubleshooting, 3-8
Local Sites
Add/Modify Local Institution Data, 2-49
Health*e*Vet Institution File Cleanup Process, 2-41
Initial Institution File Cleanup Process, 2-21
Institution File Data Review/Check, 2-4
Maintenance and Troubleshooting, 2-64
STREET ADDR. 1 Field (#1.01), 1-9, 2-3, 2-38, 2-42, 2-43, 4-1
STREET ADDR. 2 Field (#1.02), 1-9, 2-3, 2-38, 2-42, 2-43, 4-1
Subscriber Package Menu, 6-24
Supported Reference Integration Agreements, 5-1, 6-22
Symbols
Found in the Documentation, xvii
Systems Management Guide, III-1
T
Table of Contents, vii
Tables and Figures, xi
Taxonomy Codes, 1-11, 2-40, 6-14, 7-7
TCP/IP ADDRESS Field, 2-41
Templates, 6-7
Cleanup Process, 6-7
XUMF CHCK, 6-7
XUMF DSTA, 6-7
XUMF LLCL, 6-7
XUMF NAME, 6-7
XUMF NATL, 6-7
Track Station Number Changes, 1-8
Transport Global, 6-2, 6-3
Troubleshooting
FORUM, 3-8
Step-By-Step Procedures, 3-8
Site, 2-63
Type
Acronyms
B, 1
U
Update/refresh Institution file with IMF data Option, 2-40, 6-13, 7-6
URLs
Adobe Acrobat Quick Guide Web Address, xx
Adobe Home Page Web Address, xx
HSD&D Home Page Web Address, xix
IFR Home Page Web Address, xix
ISS
Acronyms Home Page Web Address, Glossary, 2
Glossary Home Page Web Address, Glossary, 2
Kernel Home Page Web Address, xix
VistA Documentation Library (VDL) Home Page Web Address, xx
Use this Manual, How to, xvii
User Guide, I-1
V
VA TYPE CODE Field, 6-10
Variables, 6-26
Verify Address Updates, 2-50
VHA DIRECTIVE 97-058, 1-4, 7-8
VistA Documentation Library (VDL)
Home Page Web Address, xx
W
Web Pages
Adobe Acrobat Quick Guide Web Address, xx
Adobe Home Page Web Address, xx
HSD&D Home Page Web Address, xix
IFR Home Page Web Address, xix
ISS
Acronyms Home Page Web Address, Glossary, 2
Glossary Home Page Web Address, Glossary, 2
Kernel Home Page Web Address, xix
VistA Documentation Library (VDL) Home Page Web Address, xx
Write Identifiers
INSTITUTION File (#4), 4-6
X
XPD INSTALLATION MENU (KIDS), 6-3
XPD MAIN Menu (KIDS), 6-3
XUAF4
\$\$ACTIVE^XUAF4, 5-1
\$\$CIRN^XUAF4, 5-2
\$\$ID^XUAF4, 5-3
\$\$IDX^XUAF4, 5-4
\$\$IEN^XUAF4, 5-4
\$\$LEGACY^XUAF4, 5-6
\$\$LKUP^XUAF4, 5-7
\$\$MADD^XUAF4, 5-7
\$\$NAME^XUAF4, 5-8
\$\$NNT^XUAF4, 5-8
\$\$NS^XUAF4, 5-9
\$\$O99^XUAF4, 5-9
\$\$PADD^XUAF4, 5-10
\$\$PRNT^XUAF4, 5-11
\$\$RF^XUAF4, 5-11
\$\$RT^XUAF4, 5-12
\$\$STA^XUAF4, 5-13
\$\$TF^XUAF4, 5-13
\$\$WHAT^XUAF4, 5-14
CDSYS^XUAF4, 5-14
CHILDREN^XUAF4, 5-15
F4^XUAF4, 5-16
LOOKUP^XUAF4, 5-17
PARENT^XUAF4, 5-25
SIBLING^XUAF4, 5-26
XUAF4 Routines, 6-8
XU-INSTITUTION-E Option, 2-48, 2-50, 2-53, 6-25
XUKERNEL Menu, 1-11, 2-39, 2-40, 2-48, 2-49, 6-4, 6-13, 6-14
XUMF
\$\$IEN^XUMF, 5-5
XUMF ACK
HL7 Logical Link, 6-6
XUMF AUTO
Protocol, 6-7
XUMF CHCK
Protocol, 6-7
Template, 6-7
XUMF DMIS ID LOAD Option, 6-11, 7-5
XUMF DSTA
Protocol, 6-7
Template, 6-7
XUMF ERROR
Bulletin, 6-5
Mail Group, 7-2
XUMF ERROR Mail Group, 1-10, 2-63, 2-64, 3-8, 6-19, 7-4
XUMF FORUM
HL7 Logical Link, 6-6
XUMF FORUM Field, 2-41
XUMF FORUM INSTITUTION Option, 3-1, 3-2, 6-11, 6-25, 7-1, 7-5, 7-8
XUMF IMF ADD EDIT Option, 2-39, 2-41, 2-49, 2-50, 6-12, 7-5
XUMF IMF BY PRNT Option, 2-9
XUMF IMF EDIT STATUS Option, 2-39, 2-41, 6-12, 7-6
XUMF INSTITUTION
Bulletin, 6-5
Mail Group, 7-2
Option, 2-13, 2-14, 2-15, 2-21, 6-4, 6-12, 6-25, 7-6
Security Key, 3-1, 6-11, 7-1, 7-5, 7-8
XUMF INSTITUTION HSITES Mail Group, 2-39
XUMF INSTITUTION Mail Group, 1-8, 2-42, 2-49, 2-63, 2-64, 3-6, 3-8, 6-19, 7-4
XUMF INSTITUTION Option, 2-39, 2-40
XUMF INSTITUTION Security Key, 2-39, 2-41, 2-49, 6-11, 7-5
XUMF LLCL
Protocol, 6-7
Template, 6-7
XUMF LOAD INSTITUTION Option, 2-40, 6-13, 7-6
XUMF LOAD NPI Option, 1-11, 2-40, 6-14, 7-7
XUMF MFK
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF MFN
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF MFP MFQ
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF MFP MFR
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF MFQ
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF MFR
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF MFS
HL7 Application Parameter, 6-5
Protocols, 6-6
XUMF NAME
Protocol, 6-7
Template, 6-7
XUMF NATL
Protocol, 6-7
Template, 6-7
XUMF NPI Mail Group, 1-11
XUMF RDSN
Protocol, 6-7
XUMF RDSN MENU
Protocol, 6-7
XUMF Routines, 6-8
XUMF SERVER
HL7 Application Parameter, 6-5
Mail Group, 7-2
Protocols, 6-6
XUMF SERVER Mail Group, 2-49
XUMF218 Routines, 6-8
XUMF218A Routines, 6-8
XUMF261P Routines, 6-8
XUMF299 Routines, 6-8
XUMF333 Routines, 6-8
XUMF335 clean 4.1 and 4 Option, 2-39, 2-40, 6-13, 7-7
XUMF4 Routines, 6-8
XUMF416 Routines, 6-8
XUMF4A Routines, 6-8
XUMF4F Routines, 6-8
XUMF4H Routines, 6-8
XUMF4L0 Routines, 6-8
XUMF4L1 Routines, 6-8
XUMF4L2 Routines, 6-8
XUMF512F Routines, 6-8
XUMFEIMF Routines, 6-8
XUMFENV Routines, 6-3, 6-8
XUMFH Routines, 6-8
XUMFH4 Routines, 6-8
XUMFHM Routines, 6-8
XUMFHPQ Routines, 6-8
XUMFHPR Routines, 6-9
XUMFI
MAIN^XUMFI, 5-18
XUMFI Routines, 6-9
XUMFI0 Routines, 6-9
XUMFMFE Routines, 6-9
XUMFMFI Routines, 6-9
XUMFP
MAIN^XUMFP, 5-20
XUMFP Routines, 6-9
XUMFP4 Routines, 6-9
XUMFP4C Routines, 6-9
XUMFP4Z Routines, 6-9
XUMFP512 Routines, 6-9
XUMFP513 Routines, 6-9
XUMFPFT Routines, 6-9
XUMFPMFS Routines, 6-9
XUMFPOST Routines, 4-6, 6-3, 6-9
XUMFPZL7 Routines, 6-9
XUMFR Routines, 6-9
XUMFX Routines, 6-9
XUMFXACK Routines, 6-9
XUMFXH Routines, 6-9
XUMFXHL7 Routines, 6-9
XUMFXI Routines, 6-9
XUMFXP Routines, 6-9
XUMFXP1 Routines, 6-9
XUMFXP2 Routines, 6-9
XUMFXR Routines, 6-9
XUMGR Security Key, 1-10, 2-47
XUSITEMGR Menu, 2-49
Z
ZIP (MAILING) Field (#4.05), 1-9, 2-3, 2-38, 2-42, 2-43, 4-2
ZIP Field (#1.04), 1-10, 2-3, 2-38, 2-42, 2-43, 4-2
