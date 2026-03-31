---
title: DI*21*38 Site Manual
doc_type: SM
doc_label: Site Manual / Systems Management Guide
doc_layer: patch
doc_subject: Site Manual
app_code: SQLI
app_name: SQL Interface
section: INF
app_status: active
pkg_ns: DI
patch_ver: 21
patch_id: DI*21*38
group_key: "SQLI:DI:21"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - sqli
  - fileman
  - table
  - tables
  - column
  - access
  - contents
  - span
  - projection
  - vendor
page_count: 0
word_count: 16722
section_count: 8
table_count: 62
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_sm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_sm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=25"
---

![](di-21-38-site-manual/001.png)

VA FILEMANSQL INTERFACE (SQLI)SITE MANUAL

Patch DI\*21.0\*38

October 1997

VistA Health Systems Design & Development (HSD&D)

Infrastructure & Security Services (ISS)

## Revision History

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
<td>10/97</td>
<td>1.0</td>
<td>Initial SQL Interface (SQLI), Patch DI*21.0*38 software documentation creation.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/19/05</td>
<td>2.0</td>
<td><p>Reformatted document to follow current ISS standards. No other major content changes made.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: KMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc56819157" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

Revision History [iii](#revision-history)

Figures and Tables [ix](#figures-and-tables)

SQLI Web Site—Companion to this Manual [xi](#sqli-web-sitecompanion-to-this-manual)

Orientation [xiii](#orientation)

1\. Introduction [1-1](#introduction)

What Other Software is Required to View VA FileMan Data Through SQL? [1-2](#what-other-software-is-required-to-view-va-fileman-data-through-sql)

Mapping VA FileMan to SQL without SQLI [1-2](#mapping-va-fileman-to-sql-without-sqli)

Advantages of Mapping to VA FileMan through SQLI [1-3](#advantages-of-mapping-to-va-fileman-through-sqli)

Developer Notes [1-4](#developer-notes)

2\. Installing an M-to-SQL System Using SQLI [2-1](#installing-an-m-to-sql-system-using-sqli)

Components of an M-to-SQL System Using SQLI [2-1](#components-of-an-m-to-sql-system-using-sqli)

Steps to Provide Relational Access to VA FileMan [2-1](#steps-to-provide-relational-access-to-va-fileman)

A. Determine Desired Type(s) of Access to VA FileMan Data [2-2](#a.-determine-desired-types-of-access-to-va-fileman-data)
B. Choose and Purchase M-to-SQL Vendor's Software [2-4](#_Toc93914476)
C. Anticipate Training Needs [2-5](#c.-anticipate-training-needs)
D. Install and Configure M-to-SQL System [2-6](#d.-install-and-configure-m-to-sql-system)
E. Do the First SQLI Projection and Mapping [2-7](#e.-do-the-first-sqli-projection-and-mapping)

SQLI Implementation Notes [2-11](#sqli-implementation-notes)

3\. SQLI System Management [3-1](#sqli-system-management)

Re-projecting SQLI when File Structures Change [3-1](#re-projecting-sqli-when-file-structures-change)

Determining the Current Status of the Projection [3-2](#determining-the-current-status-of-the-projection)

Scheduling the SQLI Projection on a Regular Basis [3-2](#scheduling-the-sqli-projection-on-a-regular-basis)

SQLI Projection and Vendor Mapping as One Task [3-3](#sqli-projection-and-vendor-mapping-as-one-task)

Troubleshooting Errors that Abort SQLI [3-4](#troubleshooting-errors-that-abort-sqli)

Errors Messages from SQLI Projections [3-4](#errors-messages-from-sqli-projections)

DBA Security: Managing Access to VA FileMan Data [3-8](#dba-security-managing-access-to-va-fileman-data)

Ensuring the Accuracy of the Mapping [3-9](#ensuring-the-accuracy-of-the-mapping)

How to Purge SQLI Data [3-9](#how-to-purge-sqli-data)

4\. SQLI for End-Users [4-1](#sqli-for-end-users)

Ways to Access VA FileMan Data through M-to-SQL [4-2](#ways-to-access-va-fileman-data-through-m-to-sql)

Naming Issues [4-3](#naming-issues)

SQLI Naming Rules [4-3](#sqli-naming-rules)

VA FileMan Files as Tables [4-4](#va-fileman-files-as-tables)

Table Naming [4-4](#table-naming)

Table Names for Subfiles [4-4](#table-names-for-subfiles)

Schemas [4-5](#schemas)

Column Names for Fields [4-5](#column-names-for-fields)

DBA Reports: Table and Column Naming [4-7](#dba-reports-table-and-column-naming)

Data Format of Columns [4-8](#data-format-of-columns)

Base vs. External Data Values for Columns [4-8](#_Toc93914502)

Internal Entry Number (IEN) Column [4-8](#internal-entry-number-ien-column)

Word-processing Fields [4-9](#word-processing-fields)

Joining Tables [4-10](#joining-tables)

Primary Keys [4-10](#primary-keys)

Recreating a Pointer Field Relationship between Tables [4-11](#recreating-a-pointer-field-relationship-between-tables)

Joining Tables Using Foreign Keys [4-11](#joining-tables-using-foreign-keys)

Flattening of Subfiles into Standalone Tables [4-12](#flattening-of-subfiles-into-standalone-tables)

Recreating the Relationship between a Subfile and its Parents [4-14](#recreating-the-relationship-between-a-subfile-and-its-parents)

Business Rules [4-15](#business-rules)

Insert/Update/Delete Commands [4-15](#insertupdatedelete-commands)

5\. SQLI Technical Information [5-1](#sqli-technical-information)

SQLI File List [5-1](#sqli-file-list)

SQLI File Diagram [5-2](#sqli-file-diagram)

Global Translation, Journaling, and Protection [5-3](#global-translation-journaling-and-protection)

SQLI Routine List [5-3](#sqli-routine-list)

SQLI Options [5-4](#sqli-options)

Application Program Interfaces (APIs) [5-6](#application-program-interfaces-apis)

SETUP^DMSQ: Generate SQLI Projection (Interactive) [5-6](#setupdmsq-generate-sqli-projection-interactive)

KW^DMSQD(): Add Keywords [5-7](#kwdmsqd-add-keywords)

ALLF^DMSQF: Generate SQLI Projection (Non-Interactive) [5-8](#allfdmsqf-generate-sqli-projection-non-interactive)

ALLS^DMSQS: Cardinality of All Tables [5-8](#allsdmsqs-cardinality-of-all-tables)

STATS^DMSQS(): Cardinality of One Table [5-9](#statsdmsqs-cardinality-of-one-table)

\$\$CN^DMSQU(): Column Name [5-9](#cndmsqu-column-name)

\$\$FNB^DMSQU(): Table Name [5-10](#fnbdmsqu-table-name)

\$\$SQLI^DMSQU(): SQL Identifier [5-11](#sqlidmsqu-sql-identifier)

\$\$SQLK^DMSQU(): SQL Identifier (Not a Keyword) [5-11](#sqlkdmsqu-sql-identifier-not-a-keyword)

Other Supported References [5-13](#other-supported-references)

SQLI Files, Fields, and Cross-references [5-13](#sqli-files-fields-and-cross-references)

Direct Mode Utilities [5-13](#direct-mode-utilities)

Glossary Glossary-[1](#glossary)

Appendix A—Case Studies A-[1](#appendix-acase-studies)

Index Index-[1](#index)

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## SQLI Web Site—Companion to this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SQLI Web site is an *online companion* to this manual. It contains the most recent information about SQLI, including additional material *not* published in this manual.

Areas on the SQLI Web site include:

- Latest News
- Documentation, including any updates
- FAQs (compiled from ongoing site experiences)
- Troubleshooting Tips (compiled from ongoing installation experiences)
- Demonstrations of SQLI projects
- Case Studies (updated beyond this manual's publication date)
- Vendor/Product Listings (added to as companion products to SQLI become available)

Check the SQLI Web site *before* you install SQLI to get acquainted with the latest installation issues and solutions that the SQLI team is able to provide.

Also check the SQLI Web site periodically *after* you start using SQLI, to get the latest information, ideas, troubleshooting tips, and other SQLI news.

The SQLI Web site is located at the following Web address:

> <http://vista.med.va.gov/sqli/index.asp>

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

The purpose of this manual is to provide information about the SQL Interface (SQLI) software (i.e., VA FileMan Patch DI\*21.0\*38).

This manual provides guidance about how VA FileMan files and fields may be projected through SQL and ODBC. It does *not* attempt to explain relational database concepts, SQL queries, or how to access ODBC data sources. For this information, you should consult the documentation provided with the relational database products you are using. You may want to purchase training in these areas as well.

Throughout this manual, advice and instructions are offered regarding the use of the SQL Interface (SQLI) software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                       |
| ![](di-21-38-site-manual/002.png) | Used to inform the reader of general information including references to additional reading material. |
| ![](di-21-38-site-manual/003.png)                                                              | Used to caution the reader to take special notice of critical information.                            |

<span id="_Ref345831418" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will be in the "000" or "666."
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- HL7 messages, "snapshots" of computer online displays (i.e., roll-and-scroll screen captures/dialogues) and computer source code, if any, are shown in a *non*-proportional font and enclosed within a box.
- User's responses to online prompts will be boldface type. The following example is a screen capture of computer dialogue, and indicates that the user should enter two question marks:

> Select Primary Menu option: ??

- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments, if any, are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

VA FileMan and SQL Terminology

The following table lists the equivalent terminology between VA FileMan and SQL:

| VA FileMan   | SQL |
|------------------|---------|
| n/a              | Schema  |
| File or Multiple | Table   |
| Field            | Column  |
| Field Type       | Domain  |
| Record           | Row     |

<span id="_Toc93909180" class="anchor"></span>Table iii: A FileMan and SQL terminology equivalents

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/005.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in any VistA character-based product:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/006.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language
- Relational Database Concepts
- SQL Queries
- How to access ODBC Data Sources

It provides an overall explanation of configuring and using the SQL Interface (SQLI) software contained in VA FileMan Patch DI\*21.0\*38. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about the SQL Interface (SQLI) software should consult the following:

- *VA FileMan SQLI Site Manual* (this manual)
- *VA FileMan SQLI Vendor Manual* (targeted for M-to-SQL vendors)
- SQLI Home Page (for more information on SQLI) at the following temporary Web address:

> <http://vista.med.va.gov/sqli/index.asp>

> This site contains additional information and documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](di-21-38-site-manual/007.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following Web address:</p>
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
| ![](di-21-38-site-manual/008.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [SQLI Web Site—Companion to this Manual](#sqli-web-sitecompanion-to-this-manual)
  - [Orientation](#orientation)
- [Introduction](#introduction)
    - [What Other Software is Required to View VA FileMan Data Through SQL?](#what-other-software-is-required-to-view-va-fileman-data-through-sql)
    - [Mapping VA FileMan to SQL without SQLI](#mapping-va-fileman-to-sql-without-sqli)
    - [Advantages of Mapping to VA FileMan through SQLI](#advantages-of-mapping-to-va-fileman-through-sqli)
    - [Developer Notes](#developer-notes)
- [Installing an M-to-SQL System Using SQLI](#installing-an-m-to-sql-system-using-sqli)
    - [Components of an M-to-SQL System Using SQLI](#components-of-an-m-to-sql-system-using-sqli)
    - [Steps to Provide Relational Access to VA FileMan](#steps-to-provide-relational-access-to-va-fileman)
    - [SQLI Implementation Notes](#sqli-implementation-notes)
- [SQLI System Management](#sqli-system-management)
    - [Re-projecting SQLI when File Structures Change](#re-projecting-sqli-when-file-structures-change)
    - [Determining the Current Status of the Projection](#determining-the-current-status-of-the-projection)
    - [Scheduling the SQLI Projection on a Regular Basis](#scheduling-the-sqli-projection-on-a-regular-basis)
    - [SQLI Projection and Vendor Mapping as One Task](#sqli-projection-and-vendor-mapping-as-one-task)
    - [Troubleshooting Errors that Abort SQLI](#troubleshooting-errors-that-abort-sqli)
    - [Errors Messages from SQLI Projections](#errors-messages-from-sqli-projections)
    - [DBA Security: Managing Access to VA FileMan Data](#dba-security-managing-access-to-va-fileman-data)
    - [Ensuring the Accuracy of the Mapping](#ensuring-the-accuracy-of-the-mapping)
    - [How to Purge SQLI Data](#how-to-purge-sqli-data)
- [SQLI for End-Users](#sqli-for-end-users)
    - [Ways to Access VA FileMan Data through M-to-SQL](#ways-to-access-va-fileman-data-through-m-to-sql)
    - [Naming Issues](#naming-issues)
    - [Data Format of Columns](#data-format-of-columns)
    - [Joining Tables](#joining-tables)
    - [Business Rules](#business-rules)
- [SQLI Technical Information](#sqli-technical-information)
    - [SQLI File List](#sqli-file-list)
    - [SQLI File Diagram](#sqli-file-diagram)
    - [Global Translation, Journaling, and Protection](#global-translation-journaling-and-protection)
    - [SQLI Routine List](#sqli-routine-list)
    - [SQLI Options](#sqli-options)
    - [Application Program Interfaces (APIs)](#application-program-interfaces-apis)
    - [Other Supported References](#other-supported-references)
  - [## Glossary](#glossary)
  - [Appendix A—Case Studies](#appendix-acase-studies)
  - [Index](#index)
From an operational point of view, VA FileMan is a hierarchical database, because it supports multiples (nested tables). However, the nature of VA FileMan's underlying file and data dictionary structures allow its files and multiples to be viewed as relational tables as well.
M-to-SQL vendors have provided relational access to VA FileMan data in the past by scanning VA FileMan's internal data dictionary structures, and interpreting the information found there to provide a relational view of the underlying data.
SQLI insulates the M-to-SQL vendors from direct access to VA FileMan's internal data dictionaries by projecting all information needed for a relational view of VA FileMan in a supported manner. Instead of accessing internal data dictionary structures, M-to-SQL vendors need only scan the SQLI's projection to build their relational view of VA FileMan data.
![](di-21-38-site-manual/009.png)
<span id="_Toc93909181" class="anchor"></span>Figure 1‑1: Relational view of VA FileMan
Why Map VA FileMan to SQL?
SQL (Structured Query Language) is the predominant language and set of facilities for working with relational tables.
The reason to access VA FileMan data through SQL is to take advantage of features provided both by SQL and by Commercial Off-the-Shelf (COTS) software. For example, if a vendor's M-to-SQL product can act as an ODBC data source, this provides direct access to VA FileMan data for ODBC-enabled Windows software!
Some ways you can work with VA FileMan data using an M-to-SQL product include:
- Query VA FileMan data through SQL.
- Manipulate VA FileMan data in Open Database Connectivity (ODBC) aware applications. This is possible if the M-to-SQL product can act as an ODBC data source. In this case, VA FileMan data can be accessed and manipulated by ODBC-compatible applications (e.g., Access, Excel, ReportSmith, Crystal Reports, etc.).
- Make VA FileMan data accessible over an Intranet or the Internet using an ODBC-aware Web server.

### What Other Software is Required to View VA FileMan Data Through SQL?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To enable SQL access to VA FileMan data at your site, you need to purchase an M-to-SQL product (software that can view structured M globals as relational tables through SQL).
The M-to-SQL vendor must also provide SQLI mapper software that map their SQL data dictionaries, based on SQLI's projection, to directly access VA FileMan data.

### Mapping VA FileMan to SQL without SQLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several commercial vendors have already implemented SQL interfaces to the VA FileMan database, by mapping directly to VA FileMan's internal data dictionary structures. Despite their success, you should consider using an M-to-SQL product that can construct its mapping to the supported relational view of VA FileMan data structures provided by SQLI.

### Advantages of Mapping to VA FileMan through SQLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI publishes all of the information M-to-SQL vendors need to access VA FileMan data through SQL. It places a layer between M-to-SQL vendors and VA FileMan's data dictionary, projecting the format for SQL access to VA FileMan files in a uniform manner. This approach results in a number of advantages, compared to vendors mapping directly against VA FileMan's internal data dictionary:
| SQLI Feature                                                                                                                                                                                                                 | Advantage                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| SQLI projects VA FileMan files as tables and VA FileMan field types as SQL data types, functions, and domains.                                                                                                                   | Insulates M-to-SQL vendors from directly accessing VA FileMan's data dictionary structures, which are subject to change. |
| SQLI provides standard interpretations of data structures such as pointer fields, variable pointer fields, word-processing fields, multiples, and internal entry numbers. It also provides a standard treatment of primary keys. | Enables standard approaches to writing queries across all VA sites.                                                      |
| SQLI publishes standard SQLI identifiers for each VA FileMan file and field.                                                                                                                                                     | Enables one site's SQL queries to work across all VA sites.                                                              |
| SQLI provides a standard layer in VA FileMan for SQL access features.                                                                                                                                                            | The presence of SQLI lays the groundwork for deeper integration of SQL access with VA FileMan.                           |
| SQLI provides code for many of the data retrieval tasks inherent in accessing VA FileMan data through SQL.                                                                                                                       | Should save vendor work, and encourage uniform approaches to retrieving VA FileMan data among vendors.                   |
<span id="_Toc93909182" class="anchor"></span>Table 1‑1: Advantages of mapping to VA FileMan through SQLI

### Developer Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As a developer, you may want to work with VA FileMan data relationally, using embedded SQL commands. You might then wonder if SQLI and its APIs would help you in doing this.
SQLI does not itself provide an API for directly accessing VA FileMan data. Nor is it able to provide access to VA FileMan data relationally on its own. Instead, it provides a framework for M-to-SQL vendors to access VA FileMan's internal data dictionary information. M-to-SQL vendors are then able to provide relational access to VA FileMan data.
As a developer, to work with VA FileMan data relationally your application should make use of services provided by COTS M-to-SQL software. Your application can then use SQL statements to access VA FileMan data, either directly or in conjunction with ODBC-aware client applications. Using services provided by the COTS M-to-SQL product (and, optionally, ODBC-aware client software), your application can:
- Run SQL queries on VA FileMan data
- Implement business rules using SQL stored procedures
- Create and use database views
- Optionally incorporate business rules (as SQL stored procedures) in database views

# Installing an M-to-SQL System Using SQLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Components of an M-to-SQL System Using SQLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Providing SQL access to your VA FileMan data requires using a number of software components, all working together. VistA's SQLI software product is one component of several needed for a complete system.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Component</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>SQLI</strong></td>
<td>Part of VA FileMan. Projects VA FileMan's internal data dictionary information in a format tailored for use by M-to-SQL vendors.</td>
</tr>
<tr class="even">
<td><strong>M-to-SQL Product</strong></td>
<td><p>Must be purchased from a vendor. It should:</p>
<ul>
<li><p>Provide SQL services</p></li>
<li><p>Be able to map its SQL data dictionaries so that SQL tables can reference data stored in M globals.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>SQLI Mapper</strong></td>
<td>Provided by the vendor of the M-to-SQL product. This utility reads the information published by SQLI to map the M-to-SQL product's SQL data dictionaries to reference VA FileMan data.</td>
</tr>
<tr class="even">
<td><strong>ODBC Drivers</strong></td>
<td>(optional) If the M-to-SQL software can act as an ODBC data source, the vendor can provide ODBC workstation drivers.</td>
</tr>
</tbody>
</table>

<span id="_Toc93909183" class="anchor"></span>Table 2‑1: Components of an M-to-SQL system using SQLI

### Steps to Provide Relational Access to VA FileMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A. Determine Desired Type(s) of Access to VA FileMan Data

> B. Choose and Purchase M-to-SQL Vendor's Software

> C. Anticipate Training Needs

> D. Install and Configure M-to-SQL System

> E. Do the First SQLI Projection and Mapping

#### A. Determine Desired Type(s) of Access to VA FileMan Data

Two general types of access to VA FileMan data have been demonstrated through M-to-SQL products:

- SQL host-based queries on VA FileMan data
- ODBC client access to VA FileMan data

The type of access you need affects your purchasing decision for M-to-SQL products, and your infrastructure needs for end-users.

#### SQL Host-based Queries on VA FileMan Data

A host-based query is simply an SQL query done through an M-to-SQL vendor's native software interface. To enable host-based queries, you only need to set up an M-to-SQL product to access VA FileMan data. The M-to-SQL product should provide some type of interface to allow SQL queries. Typically this is a character-based SQL interface, allowing queries to be entered and results returned on a character-based terminal.

![](di-21-38-site-manual/010.png)

<span id="_Toc93909184" class="anchor"></span>Figure 2‑1: Sample system configuration (host-based queries)

#### ODBC Client Access to VA FileMan Data

ODBC (Open Database Connectivity) is the most common way to connect MS-Windows clients to host-based database systems. ODBC insulates MS-Windows client programs from the details of connecting to a specific database; instead, the client connects to an ODBC driver. The ODBC driver in turn connects to a database that can act as an ODBC data source. The driver handles the details of accessing the database in question.

If you purchase M-to-SQL software that can act as an ODBC data source, then MS-Windows clients can access your VA FileMan data through ODBC. For this level of support, in addition to the requirements for host-based queries:

- The M-to-SQL database software must also be able to act as an ODBC data source.
- The M-to-SQL vendor must provide ODBC drivers for client workstations to connect to the M-to-SQL ODBC data source.
- A TCP/IP network must connect the client workstations to the M-to-SQL database software.
- The client software must be ODBC-enabled.

![](di-21-38-site-manual/011.png)

<span id="_Toc93909185" class="anchor"></span>Figure 2‑2: Sample system configuration (ODBC)

#### B. Choose and Purchase M-to-SQL Vendor's Software

The purpose of using SQLI at your site is to take advantage of a vendor-provided M-to-SQL product.

A key factor in choosing a vendor's M-to-SQL product is the availability and pricing of an SQLI mapper utility from the vendor. This utility reads the information published by SQLI to map the M-to-SQL product's SQL data dictionaries to reference VA FileMan data. The availability and pricing of an SQLI mapper utility is within the purview of the M-to-SQL vendor.

Performance and cost-per-user are factors to consider for most software; M-to-SQL software is no exception.

Other factors beyond performance and cost to consider when choosing a vendor's software are:

- ODBC Support
- SQLI Mapper Implementation

#### ODBC Support

Some M-to-SQL products can act as ODBC data sources. As described in the previous section, to enable ODBC access to VA FileMan data, the M-to-SQL product must:

- Act as an ODBC data source.
- Provide ODBC client drivers for end-user workstations to access the ODBC data source.

#### SQLI Mapper Implementation

M-to-SQL vendors map their SQL data dictionaries to the SQLI projection. There is a considerable amount of freedom for vendors in how they use the information in SQLI to project tables and columns, and data values. Because the mapping process is up to the vendor, the level of implementation of SQLI's projection of VA FileMan can vary among vendors. Also, the SQL implementations themselves vary from vendor to vendor, which can affect how some types of data (e.g., word-processing fields) are presented.

Also, some features that are available through host-based queries may not be available through ODBC.

Some of the issues to consider when evaluating a vendor's SQLI mapper are:

- Namespacing. Has the vendor received a formal namespace from the VHA DBA? If not, does the vendor's namespace conflict with a VA namespace?
- Programming SAC (Standards and Conventions). Does the vendor's code conform to VA's Programming SAC?
- Pointer fields. Will the end-user see resolved external values through host-based queries? Through ODBC?
- Pointer fields. Is the internal pointer value available to perform joins with through host-based queries? Through ODBC?
- Set of codes fields. Will the end-user see resolved external values through host-based queries? Through ODBC?
- Word-processing fields. Are they presented as columns using a memo-like data type at the "parent" table level (i.e., the entire contents of the word-processing field is available as a column value), or as standalone tables where each line of text is an individual row that must be joined with the "parent" table? If a memo-like data type is used, how is truncation handled if word-processing field data exceeds the maximum size of the memo field?
- Foreign keys. Is foreign key or similar functionality implemented that makes joins based on pointer fields and multiples easier?
- Update/Insert/Delete. The first version of SQLI does not provide specific support for writes to the database. Does the vendor's M-to-SQL implementation disable update/insert/delete access to tables mapped from SQLI? If not, how has the vendor implemented these operations?
- DBA control. Is a full suite of DBA features available to restrict access to SQL tables (and hence, VA FileMan data)?

#### C. Anticipate Training Needs

#### DBA Training

The security mechanism for VA FileMan files accessed through M-to-SQL software is the M-to-SQL software's Database Administrator (DBA) mechanism. Your DBA should be fully trained in the security features of your SQL software, before you implement SQL access to VA FileMan data.

First, you should designate who will be the DBA(s) for your M-to-SQL product. A DBA is an SQL user with all SQL privileges, including the ability to create other SQL users, and to grant and revoke access.

Then, the designated DBA(s) should familiarize themselves and be trained in all aspects of security in the M-to-SQL database software, including:

- Setting up SQL users
- Granting and revoking user, schema, table, column, and view privileges
- Creating database views
- Listing and auditing all users and privileges

#### End-User Training

Your end-users will need to be trained in whatever software they'll use to access VA FileMan data. Skills needed by your end-users (depending on what products they will use to access data) may include:

- Relational database concepts (tables, columns, primary keys, joins, etc.)
- Writing SQL queries
- Accessing ODBC data sources from Windows software (Excel, Access, etc.).
- Understanding how VA FileMan fields are projected through SQL and ODBC.

This manual does *not* attempt to explain relational database concepts, SQL queries, or how to access ODBC data sources. If training in these areas is needed, your users should consult the documentation provided with the products they are using and/or pursue training in these areas as well.

This manual does provide information about how VA FileMan files and fields may be projected through SQL and ODBC (please refer to the "SQLI for End-Users" chapter).

#### D. Install and Configure M-to-SQL System

#### Required VistA Software

- Kernel V. 8.0, fully patched—needed to install KIDS (Kernel Installation and Distribution System) distribution of SQLI.
- VA FileMan V. 21.0, fully patched.
- The SQLI software (i.e., VA FileMan Patch DI\*21.0\*38), installed.

#### Skills Required

- Configure M system parameters such as stack buffer, line buffer, and global structure size (these parameters may vary among M vendors).
- Manage globals, including global placement, protection, translation, and journaling characteristics.
- Create and schedule options.
- Install, configure, and operate third-party SQL products.
- Perform SQL queries.
- Use DBA (database administrator) functions in the third-party SQL products to manage access to SQL tables.

#### Disk Space Needed

The SQLI projection of a VA FileMan database containing all current national VistA software uses approximately 30 megabytes of disk space. Use of locally developed files could add additional space to the mapping, so a total of up to 40 megabytes of disk space usage can be anticipated.

The M-to-SQL database software will also use disk space, both for the SQL implementation itself, and also for the SQL data dictionaries generated by the vendor's SQLI mapping software. The space used will vary among vendors; consult their documentation for more information on the disk space usage.

#### Set Up M-to-SQL System

Installing and configuring M-to-SQL database software is an essential part of the method of mapping VA FileMan data relationally.

#### If No M-to-SQL Service Exists

1.  Prepare a volume set and UCI having global access to ^DIC, ^DD and all application globals. When choosing the UCI and volume set for the M-to-SQL software, remember that the SQL database software may create large temporary tables when performing queries, which could consume significant amounts of disk space.
2.  Set up the UCI, stack buffer, line buffer and global node size according to SQL vendor recommendations.
3.  Verify that the routine namespaces and global usage of the SQL vendor do not conflict with VA or local usage.
4.  Load, initialize and check vendor M-to-SQL software as recommended by the vendor.

#### If M-to-SQL Service Exists

Sites with existing M-to-SQL services may have some or all of their VA FileMan files already mapped in their SQL product's data dictionaries. If these mappings in the SQL product data dictionaries are not removed, there is a high potential for conflicting table names if the SQL mapping is done to a new schema, or for inappropriate merging if the SQL mapping is done to the same schema. It's best to start with a clean slate.

1.  From the vendor SQL data dictionary, delete *table definitions only* that were previously mapped directly from ^DD. Make sure that doing this does not delete the associated *data*. Follow vendor recommendations.
2.  Archive and delete all vendor software and files associated with mapping directly from ^DD. Follow vendor recommendations.
3.  Verify that the routine namespaces and global usage of the SQL vendor do not conflict with VA or local usage.

#### E. Do the First SQLI Projection and Mapping

The first SQLI projection of VA FileMan files will be the hardest, because the projection process uncovers most of the anomalies in your system's data dictionary structures. When it encounters an anomaly that it has *not* been designed to handle gracefully, the SQLI projection process will likely crash. Each time an anomaly is encountered, you need to fix the anomaly and then re-run the SQLI projection until it is able to complete.

> 1\. Check the SQLI Web site for the latest information and troubleshooting tips.

> 2\. Confirm that VA FileMan Patch DI\*21.0\*38 (i.e., SQLI software) is loaded.

> 3\. You should have already designated who will be the DBA (database administrator) on the SQL system. Make sure the DBA has changed the default DBA password. The DBA's account assigns security to SQL tables, create schemas, grant access to tables, etc. through SQL commands. It is essential that this account be secure.

> 4\. It is *not* necessary to remove users or tasks from the system when running the SQLI projection, or to inhibit logons.

> 5\. (optional) Run VA FileMan's Check/Fix DD Structure option \[DI DDUCHK\] for all files on your system (for a range, start with the lowest numbered file, and go to the highest numbered file on your system). Answer Yes when it asks whether it should "Remove Erroneous Nodes". This will correct some of the data dictionary anomalies in advance that might otherwise cause the SQLI mapping process to abort.

|                                                                                                                |                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/012.png) | For more information on the FileMan's Check/Fix DD Structure option \[DI DDUCHK\], please refer to the *VA FileMan Advanced User Manual.* |

> 6\. Install and configure the vendor supplied SQLI mapper software as recommended by vendor. This would typically be an add-on to the already-installed vendor M-to-SQL product.

> 7\. Using vendor tools, perform any pre-mapping initialization the SQLI mapper vendor specifies, including loading the SQLI_KEY_WORD file (#1.52101) with any keywords specific to your M-to-SQL vendor.

> 8\. Using the SQLI Regenerate SQLI Projection option \[DMSQ PROJECT\] (Figure 2‑3), create the SQLI projection. This compiles the VA FileMan data dictionary into the SQLI files. It takes several hours to compile a large application set, depending on the number of files to project, the speed of your system, and the load on your system.

> Make sure no changes to the VA FileMan data dictionaries are made while the SQLI projection is running (no patches or software should be installed, and no programmers should directly modify VA FileMan data dictionary definitions.)

> Select SQLI (VA FileMan) Option: Regenerate SQLI Projection

> This process takes several hours. Want to Continue? NO// YES

> Running this job on your terminal (HOME device) will tie up

> your terminal for the several hours it takes to run, but you

> will see the job's status as it's running.

> Queuing will send it to the background for processing. The

> status will be apparent from the printed output (if there's an

> error, it's text will be printed). TaskMan/Kernel tools can also

> be used to determine whether the job ran to completion or not.

> Don't send this directly to a printer (without queuing) unless

> you are prepared to tie up your terminal AND the printer for

> the duration of the process.

> DEVICE: HOME// \<Enter\>

> Table 4676 Time elapsed: 00:50:12 (HH:MM:SS)

> Columns of 4676 Time elapsed: 03:11:59 (HH:MM:SS)

> Foreign key 5258 Time elapsed: 03:25:25 (HH:MM:SS)

> Index 4676 Time elapsed: 04:31:18 (HH:MM:SS)

<span id="_Ref93885533" class="anchor"></span>Figure 2‑3: Regenerate SQLI Projection option—Sample user dialogue and report

> You can use the Find Out SQLI Status option \[DMSQ DIAGNOSTICS\] to determine the current status of the currently running or last completed SQLI projection.

> If the mapping encounters an anomaly in the data dictionary structure (which it will probably do several times during your first mapping) it will abort with an error. You need to determine and fix the data dictionary anomaly that aborted the projection process, and then re-run the SQLI projection from the beginning.

|                                                                                                                |                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/013.png) | For a complete troubleshooting procedure for data dictionary anomalies, please refer to the "Troubleshooting Errors that Abort SQLI" topic in the "SQLI System Management" chapter in this manual. |

> After a full run of the SQLI projection completes, check out errors generated by the process.

|                                                                                                                |                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/014.png) | For more information on errors generated, please refer to the "Errors Messages from SQLI Projections" topic in Chapter 3 in this manual. |

> 9\. Now that the SQLI projection has been built, you're ready to map the vendor M-to-SQL product's data dictionaries based on the SQLI projection.  

> Run the vendor-provided SQLI mapper as recommended by the vendor. This mapper uses the information published by SQLI to set up the M-to-SQL vendor's SQL data dictionaries. It will probably take several hours to compile a large application set, depending on the number of files to map, the speed of your system, and the load on your system.

> 10\. The person who is acting as the SQL DBA may now set up SQL users and grant them the appropriate privileges to access only the tables that they need.

After the First Mapping

1.  Update existing queries. If you had M-to-SQL services in place prior to installing SQLI, and you ran SQL queries on VA FileMan data, you should debug your existing VA FileMan SQL queries. Make sure that they still operate correctly in the new SQLI environment. Primarily you will need to correct any schema, table and column names in your queries that may have changed.
1.  (optional) Check disk space. You may want to monitor the disk space used both by SQLI (for its projection of VA FileMan data dictionaries) and by your M-to-SQL product (for its mapping of VA FileMan data structures).

#### Provide Access to SQLI Options

The following options are intended for IRM use to manage SQLI:

| Option Text                   | Option Name   | Locked? |
|-----------------------------------|-------------------|-------------|
| Regenerate SQLI Projection        | DMSQ PROJECT      | XUPROGMODE  |
| Print Errors from Last Projection | DMSQ PRINT ERRORS | NA          |
| Purge SQLI Data                   | DMSQ PURGE        | XUPROGMODE  |

<span id="_Toc93909187" class="anchor"></span>Table 2‑2: SQLI IRM-related options

The following options are intended for DBAs and other interested users:

| Option Text          | Option Name              | Locked? |
|--------------------------|------------------------------|-------------|
| Table Statistics Reports | DMSQ TS MENU                 | NA          |
| Site Statistics Reports  | DMSQ PS MENU                 | NA          |
| Suggest Table Groupings  | DMSQ SUGGEST TABLE GROUPINGS | NA          |

<span id="_Toc93909188" class="anchor"></span>Table 2‑3: SQLI DBA-related and other user options

### SQLI Implementation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- .001 Number Fields. The optional .001 number field for a file, if defined, represents the IEN of entries. Such fields are *not* projected as columns by SQLI. You can access this value using the TABLE_ID column (the IEN column), which SQLI does project for all tables.
- Asterisked Files. Any files or subfiles whose names start with an asterisk are not projected in SQLI. Note: Adding an asterisk to the beginning of a field name is a VA Programming SAC convention to mark the field as obsolete.
- Dangling Pointers. It is possible that a VA FileMan field may contain a pointer to a file not actually present at a given site. If so, the field is projected as a normal pointer field would be, but without the corresponding output format that permits navigation along a pointer chain to resolve the external value of the pointer. Such fields are flagged in the SQLI_ERROR_LOG file (#1.52192) during SQLI generation as "Pointer to Absent Files". Foreign keys for such fields are not constructed.
- Field Attributes *Not* Projected. Along with number, the following field attributes are projected by SQLI: Label, field length, type, specifier, global subscript location, pointer, multiple-valued, and the first line of the field's description. Other field attributes, including output transforms and pointer screens, are not projected.

|                                                                                                                |                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/015.png) | For more information about field attributes, please refer to the "Global File Structure" chapter in the *VA FileMan Programmer Manual*. |

- File Attributes *Not* Projected. Only file name and number are projected. Other file attributes, such as Special Lookup and Screens, are not.

|                                                                                                                |                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/016.png) | For more information about file attributes, please refer to the "Global File Structure" chapter in the *VA FileMan Programmer Manual*. |

- Files *Not* in ^DIC. Only files with entries in ^DIC (the dictionary of files) are projected. This means only VA FileMan-compatible files are projected.
- Internal VA FileMan Tables *Not* Projected. Certain tables used by VA FileMan internally (numbered below two) are not projected. Errors are logged during SQLI projection in the SQLI_ERROR_LOG file (#1.52192). VA FileMan DD numbers in this category include: .001, .1, .12, .15, .21, .3, 1.001, and 1.01.
- Multiline Computed Fields. Values are not returned for multiline computed fields, since DBS calls *cannot* retrieve multiline computed fields. An example of a multiline computed field is a backward extended pointer reference.
- Non-regular Cross-references. Only regular VA FileMan cross-references are projected. VA FileMan Trigger, KWIC (Key Word in Context), MUMPS, Mnemonic, Soundex, and Bulletin type indexes are absent from SQLI. Cross-references are only projected for possible optimizations by M-to-SQL vendors.
- Output Transforms. Output transforms are not projected. If formatting needs to be applied, it can be applied at the SQL vendor column level. For more elaborate output transforms that may call routines for processing, the logic will need to be reproduced in the context of the query. Depending on your M-to-SQL product's capability, the external value of a field (after the output transform is applied) could be returned by a user-defined function that invokes the VA FileMan \$\$EXTERNAL^DILF API call.
- Variable Pointers. Variable pointers are projected as text only. Their text value is resolved, but presented as text.

# SQLI System Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Re-projecting SQLI when File Structures Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patch or installation changes the structure of VA FileMan files, the SQL data dictionaries of the M-to-SQL product that accesses those files *must* be updated. Otherwise, users accessing data through the SQL data dictionaries may access inaccurate or erroneous data, or may error out.

To update your M-to-SQL product's SQL data dictionaries:

#### Disable SQL Access while Remapping

> When running either the SQLI projection or the vendor's SQLI mapping utilities, disable access to your SQL users. To shut down ODBC access, shut down the ODBC data source listener process on the SQL server. To prevent host-based query access, use whatever utility the SQL vendor provides.

2. Perform Any Pre-mapping Initialization the SQLI Mapper Vendor Specifies

> This including loading the SQLI_KEY_WORD file (#1.52101) with any keywords specific to your M-to-SQL vendor. This should be done each time SQLI is projected, because there could be new keywords (for example, a new user-defined SQL function could impact the keyword list.)

#### Run the Regenerate SQLI Projection Option \[DMSQ PROJECT\]

> The Regenerate SQLI Projection option \[DMSQ PROJECT\] purges and then rebuilds the SQLI projection for all VA FileMan files on the system. Errors during the compilation are logged in the SQLI_ERROR_LOG file (#1.52192).

> Select SQLI (VA FileMan) Option: Regenerate SQLI Projection

> This process takes several hours. Want to Continue? NO// YES

> Running this job on your terminal (HOME device) will tie up

> your terminal for the several hours it takes to run, but you

> will see the job's status as it's running.

> Queuing will send it to the background for processing. The

> status will be apparent from the printed output (if there's an

> error, it's text will be printed). TaskMan/Kernel tools can also

> be used to determine whether the job ran to completion or not.

> Don't send this directly to a printer (without queuing) unless

> you are prepared to tie up your terminal AND the printer for

> the duration of the process.

> DEVICE: HOME// \<Enter\>

> Table 4676 Time elapsed: 00:50:12 (HH:MM:SS)

> Columns of 4676 Time elapsed: 03:11:59 (HH:MM:SS)

> Foreign key 5258 Time elapsed: 03:25:25 (HH:MM:SS)

> Index 4676 Time elapsed: 04:31:18 (HH:MM:SS)

<span id="_Toc93909189" class="anchor"></span>Figure 3‑1: Regenerate SQLI Projection—Sample user dialogue and report

#### Remap M-to-SQL

> Once you have regenerated the SQLI projection, use the vendor-provided SQLI mapping utility to remap the M-to-SQL data dictionaries to the new SQLI projection.

### Determining the Current Status of the Projection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Find Out SQLI Status option \[DMSQ DIAGNOSTICS\] to determine the current status of the currently running or last completed SQLI projection.

### Scheduling the SQLI Projection on a Regular Basis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may want to schedule a re-projection of SQLI and a full vendor SQLI remapping to run automatically, perhaps once per month. This is to make sure all VA FileMan data dictionary changes get reflected in the SQLI projection.

You can use TaskMan to schedule the Regenerate SQLI Projection option \[DMSQ PROJECT\] on a regular basis. This regenerates the SQLI projection.

|                                                                                                                |                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/017.png) | To see how you can modify this option so that it can also invoke the vendor's utilities, please refer to the "SQLI Projection and Vendor Mapping as One Task," topic below. Then, a complete remapping (SQLI' projection plus the vendor's SQLI mapping) can be performed on a regular basis. |

### SQLI Projection and Vendor Mapping as One Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Regenerate SQLI Projection option \[DMSQ PROJECT\] does *not* automatically perform the vendor side of the mapping. It only creates the SQLI projection. You may want to schedule a task that does both sides (SQLI and vendor) to completely regenerate the SQLI system. To run all of the programs necessary to completely refresh the SQL view of VA FileMan, you can make a local version of the DMSQ PROJECT option. This local option can invoke the necessary vendor utilities in its Entry and Exit actions, with SQLI's projection being run as the option's main routine. This local option can then be scheduled through TaskMan.

Scheduling the Vendor Mapping

If the vendor who supplies your SQLI mapper has made that utility Kernel-compatible, you can run both the SQLI Projection and the vendor SQLI mapping as a single task.

To do this, copy SQLI's DMSQ PROJECT option to a local option (perhaps DMSQZ PROJECT). Then, modify the Entry Action and Exit Action fields of your local DMSQZ PROJECT option as follows:

ENTRY ACTION: ;vendor's keyword call could go here

EXIT ACTION: ;vendor's mapper call could go here

<span id="_Toc93909190" class="anchor"></span>Figure 3‑2: Modifying the Entry Action and Exit Action fields to run both the SQLI Projection and vendor SQLI mapping as a single task

Any vendor utility that should run before the SQLI projection should be called in the Entry Action of your local DMSQZ PROJECT option. Updating the SQLI_KEY_WORD file (#1.52101) is a typical task to run before the SQLI projection.

Any vendor utility that should run after the SQLI projection should be called in the Exit Action of your local DMSQZ PROJECT option. The vendor SQLI mapping is a typical task to run after the SQLI projection. If the SQLI projection errors out, the Exit Action will not be executed.

Kernel Compatibility

For a vendor's utilities to be Kernel compatible, they should conform to the VA Programming SAC. This includes the setting and killing of variables, the ways that devices are used, and not interfering with Kernel error trapping.

For TaskMan compatibility, the vendor SQLI mapper must be able to run non-interactively. Also, if the vendor's utilities need to write to host files, OpenVMS sites must be running TaskMan in a DCL context.

|                                                                                                                |                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/018.png) | For more information on running TaskMan in a DCL context, please refer to the *Kernel Systems Manual*. |

### Troubleshooting Errors that Abort SQLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If a very unusual non-standard data dictionary structure is present in a VA FileMan file's data dictionary, it's possible that either the SQLI regeneration or the vendor remapping process could encounter a hard error. If a hard error occurs, you should try the following steps:

1.  Determine the file and field that was being processed at the time the hard error occurred. Use the Find Out SQLI Status option \[DMSQ DIAGNOSTICS\] to determine on what file and field the projection process stopped. You can also look at the error trap and at the last entries in the SQLI files to help figure out in what file and field the projection process stopped.
1.  Try to determine if there is anything unusual in the VA FileMan data dictionary for that file and/or field.
1.  If there is no obvious problem in the file's data dictionary, run VA FileMan's Check/Fix DD Structure option for the file in question, to check and fix any irregularities this option finds in the data dictionary.

|                                                                                                                |                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/019.png) | For more information on the Check/Fix DD Structure option, please refer to the *VA FileMan Advanced User Manual.* |

2.  Try running the RUNONE^DMSQ direct mode utility for the file in question. This utility tries to remap a single file. If it succeeds, you have probably fixed the data dictionary anomaly. If it fails, you probably need to continue to look for the problem. This utility is for diagnostic testing purposes only, and is not supported as a means of rebuilding a file's SQLI projection.
3.  If the RUNONE^DMSQ direct mode utility fails, check the SQLI Web site. A list of known issues that cause trouble for SQLI will be posted there. Its URL is:

> <http://vista.med.va.gov/sqli/index.asp>

4.  If the problem still cannot be determined, obtain support (through NOIS, Remedy, or other current support process) if you cannot resolve the problem in the preceding steps.
5.  As a last resort, if it is a local file or subfile, you could mark the file name obsolete with an asterisk (e.g., \*FILE). The SQLI projection ignores files whose names begin with "\*".

Once you have fixed the data dictionary anomaly that caused the SQLI projection to crash, run the SQLI projection again.

### Errors Messages from SQLI Projections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To list the non-fatal error messages generated during the initial or subsequent projections of VA FileMan data dictionaries by SQLI, use the Print Errors from Last Projection option \[DMSQ PRINT ERRORS\]. You can also examine the contents of the SQLI_ERROR_LOG file (#1.52192) directly through VA FileMan.

Errors are to be expected during SQLI projection. When SQLI encounters a non-standard data dictionary structure, it may not project the field or file. For example, some of VA FileMan's internal files (those numbered less than two) show up as errors in the SQLI error listing.

Typically, the result of encountering an error condition is that the file or field in question will not be projected. So, in most cases you do not need to review the error list unless there's a particular file or field you need that did not get projected.

#### SQLI Error Messages

The following is a complete list of error messages that can be reported when generating the SQLI projection.

COLUMN: CAN'T GET FIELD ELEMENTS

COLUMN: DECIMAL DEFAULT IS NEGATIVE

COLUMN: FIELD TYPE NOT KNOWN TO SQLI

COLUMN: INSERT OF COLUMN ELEMENT FAILED

COLUMN: INSERT OF COLUMN RECORD FAILED

COLUMN: INVALID FIELD LABEL

COLUMN: NO ASSOCIATED TABLE

COLUMN: NO CORRESPONDING TABLE ELEMENT

COLUMN: NULL FIELD TYPE (DOMAIN)

DATA TYPE: INSERT OF DATA TYPE RECORD FAILED

DOMAIN: INSERT OF DOMAIN RECORD FAILED

FIELD: CALL TO RETRIEVE ATTRIBUTES FAILED

FILE: CAN'T BUILD SQL NAME

FILE: INSERT OF TABLE FAILED

FILE: NO DESCRIPTION

FILE: NO GLOBAL ROOT

FILE: NO NAME

FILE: NOT FILEMAN COMPATIBLE

FILE: NULL DESCRIPTION

FILE: OBSOLETE

FILE: SUBFILE WITHOUT PARENT

FOREIGN KEY: ANCESTOR FOREIGN KEY COLUMN INSERT FAILED

FOREIGN KEY: ANCESTOR FOREIGN KEY INSERT FAILED

FOREIGN KEY: COLUMN ELEMENT INSERT FAILED

FOREIGN KEY: NO ANCESTOR PRIMARY KEY

FOREIGN KEY: NO ASSOCIATED PRIMARY KEY

FOREIGN KEY: NO POINTED-TO COLUMN AT LEVEL

FOREIGN KEY: NO POINTED-TO FILE IN SPECIFIER

FOREIGN KEY: NO PRIMARY KEY TABLE ELEMENT

FOREIGN KEY: NO TABLE FOR POINTED-TO FILE

FOREIGN KEY: TABLE ELEMENT INSERT FAILED

INDEX PRIMARY KEY: CAN'T GET COLUMN'S TABLE ELEMENT

INDEX PRIMARY KEY: CAN'T GET DATA FOR MASTER TABLE

INDEX PRIMARY KEY: COLUMN ELEMENT INSERT FAILED

INDEX PRIMARY KEY: COLUMN INSERT FAILED

INDEX PRIMARY KEY: MISSING COLUMN POINTER

INDEX PRIMARY KEY: MISSING TABLE RECORD

INDEX PRIMARY KEY: TABLE ELEMENT INSERT FAILED

INDEX PRIMARY KEY: TABLE MISSING COLUMN POINTER

INDEX: COLUMN ELEMENT INSERT FAILED

INDEX: COLUMN INSERT FAILED

INDEX: IRREGULAR FORMAT

INDEX: MISSING DATA DICTIONARY DATA

INDEX: NO ASSOCIATED COLUMN RECORD

INDEX: PRIMARY KEY ELEMENT INSERT FAILED

INDEX: PRIMARY KEY INSERT FAILED

INDEX: TABLE DOMAIN INSERT FAILED

INDEX: TABLE INSERT FAILED

KEY FORMAT: LONG_CHARACTER INSERT FAILED

ONEF: NO PARENT STRUCTURE

OUTPUT FORMAT: INSERT OF POINTER OUTPUT FORMAT FAILED

OUTPUT FORMAT: INSERT OF SET-OF-CODES OUTPUT FORMAT FAILED

OUTPUT FORMAT: INSERT OF VARIABLE POINTER OUTPUT FORMAT FAILED

PRIMARY KEY: CAN'T GET TABLE DATA

PRIMARY KEY: CAN'T GET TABLE'S FILE \#

PRIMARY KEY: DOMAIN INSERT FAILED

PRIMARY KEY: TABLE ELEMENT INSERT FAILED

SCHEMA: RECORD INSERT FAILED

STATS: KEY COUNT INSERT FAILED

STATS: RECORD INSERT FAILED

SUBFILE: BAD UP-LINK TO PARENT

<span id="_Toc93909191" class="anchor"></span>Figure 3‑3: SQLI error messages

#### Errors Generated During SQL Access

Besides errors that occur while projecting SQLI, it is possible that errors may occur when an M-to-SQL product mapped to VA FileMan data attempts to access the VA FileMan data. Possible causes are:

- Conditions in the M database that the M-to-SQL vendor did not anticipate.
- Conditions in VA FileMan data that the SQLI mapper vendor did not anticipate.

When this type of error occurs, you should first look at the data being accessed to see if there is anything unusual about that data. If nothing appears unusual, you should contact the M-to-SQL vendor and SQLI mapper vendor for assistance troubleshooting the error.

### DBA Security: Managing Access to VA FileMan Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQL includes ANSI-standard security mechanisms for SQL security. You should use these mechanisms, implemented through your M-to-SQL software's DBA functions, to provide security for VA FileMan data projected through SQL.

#### Selectively Grant Access to VA FileMan Data

Recommendations for administering security on VA FileMan files projected through SQLI to an SQL system are as follows:

1.  By default, VA FileMan files projected as tables are assigned to a schema named "SQLI". Do *not* grant blanket access to all files in the SQLI schema (in effect, every table) to end-users.
1.  Decide what sets of tables, rows and columns are needed for each set of users.
2.  Define *views* of the database for your users that reflect specific sets of tables, rows, and columns that are useful to specific user groups.
3.  Grant access both by view and by table, as appropriate, to your SQL end-users and/or user groups.
1.  Regularly audit your list of users and user groups along with their access to tables, rows, columns, and views.

#### Do Not Allow Updates to VA FileMan File Data from SQL

This release of the SQLI software (i.e., VA FileMan Patch DI\*21.0\*38) does *not* provide any support for vendors to implement commands that write to VA FileMan files (INSERT, UPDATE, DELETE). This lack of support does *not* prevent a vendor from implementing these commands, however.

One significant problem with direct writes from SQL is that VA business rules are typically stored in application code, not in the file data dictionaries. So many business rules would not be executed when updating a VA FileMan file from SQL.

So, except for situations in which you are sure all business rules will be executed, the DBA should make sure that no users are granted the following SQL privileges:

- DELETE
- INSERT
- UPDATE
- REFERENCES (data dictionary edit privileges)

### Ensuring the Accuracy of the Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Data Must Be VA FileMan-Compatible

Mapping SQL data dictionaries to the SQLI projection of VA FileMan data dictionaries assumes that the stored data, including indexes, is in a format that matches its VA FileMan data dictionary definition. If this is not the case (as can happen when data is hard-set into VA FileMan data globals instead of through an API call), the column definitions in SQL data dictionaries will not be accurate.

#### Do *Not* Map Manually

If you are using SQLI, do *not* map your SQL data dictionaries to VA FileMan data globals manually (without SQLI). SQLI takes a number of steps to ensure the integrity of the projection of the VA FileMan data dictionaries. While your M-to-SQL software will most likely have an option to map globals directly to the SQL data dictionaries, make sure that all VA FileMan data is mapped from the SQLI projection.

### How to Purge SQLI Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you decide to stop using SQLI, you may want to purge the SQLI data files and possibly your M-to-SQL vendor's SQL data dictionaries as well. To do this, you can use the Purge SLQI Data option \[DMSQ PURGE\]:

Select SQLI (VA FileMan) Option: Purge SQLI Data

Removes all records from SQLI files. Continue? NO// \<YES\>

<span id="_Toc93909192" class="anchor"></span>Figure 3‑4: Purge SLQI Data option—Sample user dialogue

Use your M-to-SQL vendor's comparable utility, if available, to purge all SQL data dictionaries mapped to VA FileMan file structures.

# SQLI for End-Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter provides guidelines for end-users on how to interpret and work with VA FileMan data when it is viewed relationally, as projected by SQLI.

As an end-user of VA FileMan data accessed through SQL, you may or may not need to know any of the information in this chapter:

- If you are accessing data through an application such as a pre-designed Web page that fully shields you from the underlying details of where pieces of data has come from, you probably do not need to know any of the information in this chapter.
- If, on the other hand, you are accessing the SQL table equivalents of VA FileMan data directly, either through SQL or through ODBC, and are dealing with tables, columns and rows, you probably do need to know the information provided in this chapter.

The main issues for end-users accessing the SQL table equivalents of VA FileMan data directly (as compared to accessing the same information through VA FileMan) are:

- Ways to access VA FileMan data through M-to-SQL.
- Naming (tables and columns).
- Data format (columns).
- Joining Tables.
- Business rules.

### Ways to Access VA FileMan Data through M-to-SQL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Using an M-to-SQL product to provide relational access to VA FileMan data opens up a world of new possibilities when it comes to working with VA FileMan data.

For example, you may be able to:

- Directly Access the VistA Database from Windows Applications

> If your site implements relational access such that ODBC access is enabled, you can use any ODBC-aware Windows application to directly access VA FileMan files. This means you can use your favorite Windows-based ODBC-aware applications to directly load, format and print records from the VistA database.  

> To do this otherwise, you would need to use the VA FileMan Export Tool. You would export data to a host file in either character-delimited or width-delimited format, transfer the host file from the site computer to your personal computer, and then import the data into the PC-based application in the specified format.

- Query the VistA Database Using SQL

> If your site implements M-to-SQL access to VA FileMan data, you should be able to query the VistA database using the native SQL interface of the M-to-SQL product. This may enable you to create different types of reports than you typically create using VA FileMan's report options.

- Build Web Applications

> Once VA FileMan data is accessible via ODBC, it is possible to build Web interfaces to retrieve records in the VistA database and format and display those records as Web pages. Building Web applications is a task most likely undertaken by site developers.

### Naming Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### SQLI Naming Rules

SQLI provides standard naming for VA FileMan files and fields, as projected into SQL tables and columns. SQLI ensures that the names used in the SQL projection of VA FileMan do *not* violate SQL's or ODBC's rules for element naming. The naming rules used by SQLI include:

- Illegal characters such as spaces are replaced with underscores.
- Names more than 30 characters long are compressed by abbreviating each word in the name until a length of 30 characters is reached.
- Names must start with a letter from A to z.
- Names may contain only the letters A through z, digits 0 through 9 and the underscore character "\_".

#### Consistency of Naming Supports Query Sharing between Sites

By using consistent naming algorithms for files and fields, SQLI increases the likelihood that table and column names generated for national files and fields between VA sites are the same. This allows queries to be shared between sites using SQLI with minimal changes. Only under unusual circumstances will the naming algorithms produce a different field or file name between sites.

#### VA FileMan Files as Tables

When looking at a VA FileMan database through a relational database, as projected by SQLI, the following should be accessible as tables:

- VA FileMan files.
- VA FileMan subfiles (each subfile is projected as a standalone table).
- (optional) VA FileMan word-processing fields.

You would expect VA FileMan files projected as tables in a relational system, and they are projected as such by SQLI.

However, VA FileMan subfiles are also projected as standalone tables. This may not be your ordinary way of thinking about data that is in subfiles. However, this "flattening" of VA FileMan subfiles into standalone tables is necessary to project VA FileMan data relationally. It also may provide you new ways to analyze data that has been stored in subfiles.

#### Table Naming

The picture below (Figure 4‑1) shows a partial list of table names for VA FileMan top-level files and subfiles, as retrieved by Microsoft Access through ODBC.

|                                                                                                                |                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/020.png) | This client software lists table names appended to a schema name (in this case, SQLI). |

![](di-21-38-site-manual/021.png)

<span id="_Ref93888478" class="anchor"></span>Figure 4‑1: Partial list of SQLI table names for VA FileMan top-level files and subfiles

#### Table Names for Subfiles

A subfile (also called a multiple) is essentially a file-within-a-file: A hierarchical, record-specific multiple field. For example, a patient file might have an "Appointments" subfile. This file-within-a-file can contain one or more entries for the patient's appointments. Subfiles can themselves contain subfiles.

When viewed from a relational database, VA FileMan subfiles are "flattened" and presented as standalone tables.

|                                                                                                                |                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/022.png) | For more information about how subfiles are flattened, please refer to the "Flattening of Subfiles into Standalone Tables" topic in this chapter. |

Tables derived from subfiles use names based on top-level filename, all parent subfile names, and the subfile name itself, separated by "\_"s.

For example, suppose that CASE_CARTS is a table projected for a top level file (CASE CARTS). The following are the table names projected for subfiles within the CASE CARTS file:

| VA FileMan Subfile Name  | Table Name Projected   |
|------------------------------|----------------------------|
| ITEMS                        | CASE_CARTS_ITEMS           |
| OPERATION CODES              | CASE_CARTS_OPERATION_CODES |
| SPECIAL INSTRUCTIONS/REMARKS | CASE_CARTS_SPEC_INST_REM   |

<span id="_Toc93909194" class="anchor"></span>Table 4‑1: Sample projected table names for subfiles

#### Schemas

SQLI projects all VA FileMan files as part of a single schema, "SQLI". Your relational database software may or may not make use of the schema designation of files.

#### Column Names for Fields

Column names are based on the field names. Adjustments in the projected name are only made if the original name violates SQL or ODBC naming rules.

In the example below, compare the projected column names for the SQLI_TERMINAL_TYPE table to the data dictionary (DD) field names for the fields in the TERMINAL TYPE file (#3.2).

|                                                                                                                |                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/023.png) | The IEN column as well, which corresponds to the IENs of entries rather than to a data dictionary field. |

![](di-21-38-site-manual/024.png)

<span id="_Toc93909195" class="anchor"></span>Figure 4‑2: Projected column names for the SQLI_TERMINAL_TYPE table to the DD field names for the fields in the TERMINAL TYPE file (#3.2)

#### DBA Reports: Table and Column Naming

A number of reports are available from SQLI options that provide statistical information about the SQLI projection of VA FileMan data.

In particular, the following reports provide a complete listing of the original VA FileMan naming of files and fields, compared to the naming by SQLI of the same files and fields:

- Table Name Listing (VA FileMan vs. SQLI)
- Field Listing by File (Brief)
- Field Listing by File (Full)

These reports are available from the main SQLI menu, under two options:

- Table Statistics Reports
- Site Statistics Reports

A full listing of available reports is as follows:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="table-statistics-reports" class="unnumbered"><br />
Table Statistics Reports</h5></td>
<td><strong>[DMSQ TS MENU]</strong></td>
</tr>
</tbody>
</table>

Field Listing by File (Brief) \[DMSQ TS FIELDS BRIEF\]

Field Listing by File (Full) \[DMSQ TS FIELDS FULL\]

List Subfile Links (Brief) \[DMSQ TS SUBFILE BRIEF\]

List Incoming Pointer/Subfile Links (Full) \[DMSQ TS PTR SUBFILE FULL\]

List Pointer and Parent Links (Brief) \[DMSQ TS PTR PARENT BRIEF\]

List Pointer and Parent Links (Full) \[DMSQ TS PTR PARENT FULL\]

Pointer Statistics by Individual Table \[DMSQ TS PTR STATS\]

Pointer Statistics (Summary) \[DMSQ TS PTR STATS SUMMARY\]

Table Name Listing (VA FileMan vs. SQLI) \[DMSQ TS NAMES\]

<span id="_Toc93909196" class="anchor"></span>Figure 4‑3: Table Statistics Reports menu options

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="site-statistics-reports" class="unnumbered"><br />
Site Statistics Reports</h5></td>
<td><strong>[DMSQ PS MENU]</strong></td>
</tr>
</tbody>
</table>

Table Total (Excluding Index Tables) \[DMSQ PS TOTAL TABLES\]

Column Total (All Tables) \[DMSQ PS TOTAL COLUMNS\]

Index Table Total \[DMSQ PS TOTAL INDEXES\]

Table Element Totals, By Type \[DMSQ PS TOTAL TABLE ELEMENTS\]

Column Totals, by Table \[DMSQ PS TOTAL TABLE COLS\]

Column Totals, by Table (Ordered by \# of Columns) \[DMSQ PS TOTAL TABLE COLS A\]

Columns in Regular Tables Total \[DMSQ PS TOTAL COLUMNS REG\]

Columns in Regular Tables, Excluding ID Columns \[DMSQ PS COLUMNS REG NOID\]

Columns by Domain \[DMSQ PS COLUMNS BY DOMAIN\]

<span id="_Toc93909197" class="anchor"></span>Figure 4‑4: Site Statistics Reports menu options

### Data Format of Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan field types roughly correspond to SQL data types. This section describes the specifics of how the data format of individual VA FileMan field types is affected when that data is viewed through SQL.

#### Base vs. External Data Values for Columns

Your M-to-SQL vendor may provide syntax for retrieving the base value of a column (as opposed to its external value).

When you do comparisons, such as a join that involves a pointer field, you may want the comparison to be done with the internal value of the field (IEN) rather than the external value (text name), to ensure the join is done as VA FileMan would do it. A join on "SMITH, JOHN" might match multiple entries, whereas a join on "15553" would match a single entry.

When viewing data through ODBC, on the other hand, the base form of column values may be what is returned, rather than the external form. This may present difficulty if, through ODBC, you want the external form of a VA FileMan Set of Codes field.

The following table lists VA FileMan field types where base vs. external format may be an issue:

| Field Type   | Base                                 | External           |
|------------------|------------------------------------------|------------------------|
| Pointer          | IEN of pointed-to entry                  | Resolved pointer value |
| Variable Pointer | IEN of pointed-to entry;file global root | Resolved pointer value |
| Set of Codes     | Internal Code                            | External Code          |

<span id="_Toc93909198" class="anchor"></span>Table 4‑2: VA FileMan field types (base vs. external format)

Your SQL vendor may provide syntax in their SQL for retrieving the base value of a column, or for resolving the external value of a column. This syntax is vendor specific; check with your SQL vendor for more information.

#### Internal Entry Number (IEN) Column

In VA FileMan, each entry in a file has an internal entry number (IEN). When working with VA FileMan data from within VA FileMan, you usually do not see the IEN of a record; you only see the field values of the record.

On the other hand, when you work with tables projected for VA FileMan files as projected by SQLI, each table provides an IEN column to display the IEN of each VA FileMan entry. The name of the IEN column is the table name concatenated with "\_ID". The IEN column for each table is important, because it is used as the primary key for each record.

Tables projected for subfiles provide an IEN column not only for the IEN of subfile entries, but also IEN columns for all file levels above the original subfile. Thus, with all the IENs for all file levels available, each subfile record is uniquely identified.

#### Word-processing Fields

VA FileMan stores word-processing fields in a manner very similar to how it stores multiples. Each line of text in a word-processing field is stored as if it is an entry in a multiple field.

SQLI projects multiples to M-to-SQL vendors in two ways:

- As standalone tables (each line of text is one row in the table).
- As columns for vendors who support a HUGE_CHARACTER or MEMO data type.

Your M-to-SQL vendor may present word-processing fields in an appropriate MEMO-like data type. The main problem with memo data types is that they usually come with a size constraint. VA FileMan word-processing fields, on the other hand, are unlimited in size. So truncation could occur if a word-processing field is encountered whose size exceeds the size defined as the maximum for a MEMO column.

If your M-to-SQL vendor does not provide an appropriate MEMO-like data type, word-processing fields may instead be available as standalone tables. In this case, you will need to join each line (stored as individual rows in the word-processing field table) with its parent table to access both at the same time.

### Joining Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When viewed through VA FileMan, VA FileMan files can be joined in several ways. Pointer fields join an entry in one file with an entry in another file. Multiples are joined with their parent entries. Joins can be done on the fly in VA FileMan's Print File Entries module.

When viewed through SQL, you must perform joins between tables derived from VA FileMan files explicitly. Primary keys and IEN columns are projected by SQLI to aid in this process.

#### Primary Keys

The primary key of a table identifies any row in the table uniquely. SQLI projects designated keys for VA FileMan-derived tables in a standard fashion:

- Tables for top-level VA FileMan files have a single-element key, which is the IEN column for the table in question. The IEN column is named as the table name appended with "\_ID". Just as IENs provide uniqueness for VA FileMan records, the IEN column provides uniqueness for VA FileMan table rows.
- Tables for subfiles and word-processing fields have multi-element primary keys, with one IEN column present in the table for each parent file, plus one IEN column for the IEN of the subfile entry itself.

Primary keys are very useful when you need to join tables. Because they uniquely identify rows, they can be used to recreate the "join" relationships present in the original VA FileMan files, both for pointer fields and for multiples linking to their parents.

For an example of the primary key projected for a top-level file, take the table projected for the NEW PERSON file. A one-part primary key is projected for the NEW_PERSON table; it is the IEN column for the table (NEW_PERSON_ID).

For an example of the primary key projected for a subfile, take the table projected for the DIVISION subfile in the NEW PERSON file (#200). A two-part primary key is projected for the NEW_PERSON_DIVISION table, based on the following two columns (both present in the NEW_PERSON_DIVISION table):

NEW_PERSON_ID *(IEN column of original parent entry)*

NEW_PERSON_DIVISION_ID *(IEN column of original subfile entry)*

<span id="_Toc93909199" class="anchor"></span>Figure 4‑5: Sample two-column primary key from the NEW_PERSON_DIVISION table

#### Recreating a Pointer Field Relationship between Tables

For columns derived from pointer fields, the base value of the column is the IEN of the pointed-to entry. You can join the base value of the pointer field column to the IEN column (primary key) of the pointed-to table. Use a where clause in your query to relate the pointer field column to the primary key of the pointed-to file:

WHERE POINTER_COLUMN = POINTED_TO_FILE_ID

<span id="_Toc93909200" class="anchor"></span>Figure 4‑6: Sample WHERE clause (1 of 2)

For example, to join the PATIENT table to the NEW_PERSON table based on the PATIENT.PRIMARY_PHYSICIAN column (which is derived from a pointer field to the NEW PERSON file), a WHERE clause would be:

WHERE PATIENT.PRIMARY_PHYSICIAN=NEW_PERSON.NEW_PERSON_ID

<span id="_Toc93909201" class="anchor"></span>Figure 4‑7: Sample WHERE clause (2 of 2)

Although you *could* join two tables based on the resolved text value of a pointer column, it's better to use the base value of the pointer column. This preserves referential integrity by assuring that identical resolved .01 field values would *not* be joined in ways that do not reflect the original pointer relationship.

Losing Rows When a Pointer Field Column is Null

In the simple query example above, there is a problem when entries in the PATIENT table do not have a value in the column for PRIMARY_PHYSICIAN. When the tables are joined based on the PRIMARY_PHYSICIAN column, all rows in PATIENT where PRIMARY_PHYSICIAN is null are excluded from the join.

One way to get around this is to use an "outer join". Even if there is no matching row in a subfile's table, a row from the top-level file's table will be included in an outer join. Consult your SQL vendor's documentation to see if outer joins are supported, and, if so, what the outer join syntax is.

Another way to get around this is to use foreign keys (described in the next section).

#### Joining Tables Using Foreign Keys

A foreign key provides an explicit link between two SQL tables. The tables are in a sense "pre-joined". Using the foreign key in a query, you can access columns in the linked table, without having to perform a join yourself.

SQLI publishes foreign keys for M-to-SQL vendors to make use of, in the following standard situations:

| Situation                                        | Foreign Key(s) Provided                                                                                                                                                |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Column based on pointer field                        | In the table containing the pointer field column, one for the pointed-to file, named *pointer_field_name*\_FK. The join is from the pointer field to the pointed-to table. |
| Table projected for subfile or word-processing field | In the subfile or word-processing field's table, one for each parent table, each named *parent_table*\_PFK. Each join links the subfile to its original VA FileMan parent. |

<span id="_Toc93909202" class="anchor"></span>Table 4‑3: SQLI foreign keys—M-to-SQL vendors

One advantage of using foreign keys rather than joins is that rows are not lost when the value of a join column is null. One way to think of this is that the "join" is being performed in the select clause of the query (which is where you can use foreign keys to include fields from other tables), rather than the where clause.

For example, a foreign key (i.e., NEW_PERSON_FK@NAME) can be used in the select clause to obtain the value of the column NAME from the NEW_PERSON table, rather than doing a join to NEW_PERSON in a where clause. A row is returned even if the NAME column of the corresponding row in the NEW_PERSON file is null.

Not all M-to-SQL vendors support the SQL concept of foreign keys. For those that do, the syntax to use foreign keys may be vendor-specific, so consult your M-to-SQL vendor's documentation for more information.

#### Flattening of Subfiles into Standalone Tables

VA FileMan subfiles allows one record to store one or more repeating "subrecords." This form of data representation, while not supported in the relational model, is very useful for storing certain types of data, such as the set of one or more appointments for a patient.

In VA FileMan, a listing of PATIENT records, including the APPOINTMENT subfile records, might look like:

PATIENT LIST Oct 3,1997 14:58 PAGE 5

NAME APPOINTMENT

---------------------------------------------------------------------------

FMPATIENT, ONE 12/01/1997

FMPATIENT, TWO 11/15/1997

12/15/1997

FMPATIENT, THREE

FMPATIENT, FOUR 02/15/1998

04/01/1998

FMPATIENT, FIVE 11/30/1997

01/30/1998

<span id="_Toc93909203" class="anchor"></span>Figure 4‑8: Sample patient records with appointments

In the relational model, repetitive information from VA FileMan multiples such as appointments are stored in standalone tables. In this example, one table holds the patient names while another holds the appointments. You can use the Patient_ID IEN column to link each row in the Patient_Appointment table (Figure 4‑9) to the appropriate Patient table row (Figure 4‑10):

![](di-21-38-site-manual/025.png)

<span id="_Ref93826089" class="anchor"></span>Figure 4‑9: Patient_Appointment table—Sample entries

![](di-21-38-site-manual/026.png)

<span id="_Ref93826090" class="anchor"></span>Figure 4‑10: Patient table—Sample entries

In the examples above, no record appears in the Patient_Appointment table (Figure 4‑9) for patient FMPATIENT,THREE, who has no appointments.

|                                                                                                                |                                                                                                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-site-manual/027.png) | The IENs in the PATIENT_APPOINTMENT_ID column appear as dates. This is because the .001 field of the subfile is defined as a Date/Time type. This results in date/times being used as the internal entry number for appointment records. |

#### Recreating the Relationship between a Subfile and its Parents

One of the challenges of working with VA FileMan data relationally is the splitting or flattening of subfiles that occurs in a relational view, and how to re-join the resulting subfile tables with their parent tables.

For a table projected for a subfile, a multi-part primary key is provided that provides the IEN of each parent entry up to and including the top-level entry that originally enclosed the subfile. This means that the table for the subfile includes columns ending with "\_ID", each one containing the IEN of one of the subfile entry's parents.

You can use these primary key "\_ID" columns in a join to recreate the relationship between a row in a subfile table and its parents.

For example, APPOINTMENT is a multiple in the PATIENT file (#2). Therefore, the table for the subfile, PATIENT_APPOINTMENT, has a two-column primary key, with the following columns:

| Primary Key Column | Function                             |
|------------------------|------------------------------------------|
| PATIENT_APPOINTMENT_ID | IEN of subfile entry                     |
| PATIENT_ID             | IEN of subfile's parent entry in PATIENT |

<span id="_Toc93909206" class="anchor"></span>Table 4‑4: Two-column primary key

To recreate the relationship between rows in the PATIENT_APPOINTMENT table with the "parent" PATIENT table, you could do:

SELECT \* FROM PATIENT, PATIENT_APPOINTMENT

WHERE PATIENT.PATIENT_ID = PATIENT_APPOINTMENT.PATIENT_ID

<span id="_Toc93909207" class="anchor"></span>Figure 4‑11: Recreating data relationships via M code

Losing Parent Table Rows when Joining with Subfile Tables

When you join rows in a subfile table with rows in its parent table(s), you will not lose any rows from the subfile table under ordinary circumstances. This is because subfile rows always have corresponding rows in parent tables to join with.

However, rows in the parent tables are "lost" from the join if, in the original VA FileMan file, they did not have entries in their multiples. This is a problem if your query is trying to retrieve rows from parent tables regardless of whether or not they had subfile entries.

As with joins on pointer fields, one way to get around this is to use an *outer join*. Another way to get around this is to use foreign keys, if your M-to-SQL implementation supports them. In both cases, the syntax is vendor-specific, so consult your M-to-SQL vendor's documentation for more information.

### Business Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although some business rules for VistA data are implemented in the data dictionaries of VA FileMan files, many business rules are not in the data dictionaries. Instead, these business rules are in application code. When you access VA FileMan data directly, either through VA FileMan's native interface (the Enter or Edit File Entries, Search File Entries, and Print File Entries options) or through SQL, you are bypassing any business rules not in the data dictionary.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](di-21-38-site-manual/028.png)</td>
<td>As described in the "<br />
SQLI Implementation Notes" topic in Chapter 2, output transforms are <em>not</em> projected by SQLI, so any business rules implemented in the output transform of a field are <em>not</em> used for data you access through SQL.</td>
</tr>
</tbody>
</table>

The same cautions that apply to accessing VA FileMan data directly through VA FileMan's native interface also apply to accessing that data through SQL: the data you are seeing may not be as the application developer intended it to be viewed, if the business rules are in application code. You must be careful to ensure that the data you are viewing is in the form you believe it to be in, and that you are aware of any business rules that would otherwise transform that data.

#### Insert/Update/Delete Commands

You may want to update VA FileMan files from SQL. Explicit support for vendors to implement Insert, Update, and Delete operations is *not* implemented in the first version of the SQLI software (i.e., VA FileMan Patch DI\*21.0\*38).

A caution for implementing these types of access to VA FileMan data is that business rules are quite often not stored in VA FileMan data dictionaries. In particular, business rules for how to put data into the database quite often reside in application code, not in the data dictionary of a file. Bypassing VistA application code and updating directly from SQL cannot execute business rules stored solely in application code, and can cause data corruption by circumventing those business rules.

# SQLI Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### SQLI File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the files set up when VA FileMan Patch DI\*21.0\*38 (i.e., SQLI software) is installed:

| Global Storage | File Number | File Name      |
|--------------------|-----------------|--------------------|
| ^DMSQ("S",         | 1.521           | SQLI_SCHEMA        |
| ^DMSQ("K",         | 1.52101         | SQLI_KEY_WORD      |
| ^DMSQ("DT",        | 1.5211          | SQLI_DATA_TYPE     |
| ^DMSQ("DM",        | 1.5212          | SQLI_DOMAIN        |
| ^DMSQ("KF",        | 1.5213          | SQLI_KEY_FORMAT    |
| ^DMSQ("OF",        | 1.5214          | SQLI_OUTPUT_FORMAT |
| ^DMSQ("T",         | 1.5215          | SQLI_TABLE         |
| ^DMSQ("E",         | 1.5216          | SQLI_TABLE_ELEMENT |
| ^DMSQ("C",         | 1.5217          | SQLI_COLUMN        |
| ^DMSQ("P",         | 1.5218          | SQLI_PRIMARY_KEY   |
| ^DMSQ("F",         | 1.5219          | SQLI_FOREIGN_KEY   |
| ^DMSQ("ET",        | 1.52191         | SQLI_ERROR_TEXT    |
| ^DMSQ("EX",        | 1.52192         | SQLI_ERROR_LOG     |

<span id="_Toc93909208" class="anchor"></span>Table 5‑1: SQLI global and file list

SQLI is implemented as a set of VA FileMan files within a single M global, with no multiples or word-processing fields.

The organization of the files mirrors SQL2 standard Data Definition Language (DDL) syntax. Every data structure in the main SQLI files reflects some portion of the DDL commands needed to create SQL data dictionaries for VA FileMan data (essentially, the CREATE TABLE command).

Additional syntax has been added to support the definition of M global structures, virtual columns, key and output formats and other objects outside the scope of the SQL standard.

### SQLI File Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following diagram organizes the file entities in their importance to the operation of the SQLI software. It shows conceptual relationships between the files, but not a comprehensive view of the physical pointer relationships between files:

![](di-21-38-site-manual/029.png)

<span id="_Toc93909209" class="anchor"></span>Figure 5‑1: SQLI file diagram

### Global Translation, Journaling, and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Translation

Translation is recommended for the sole SQLI global (i.e., ^DMSQ). This global has the potential to be read-intensive as more and more applications are added to it in the future.

Journaling

It is not essential or recommended to journal ^DMSQ. The only VistA product using this global is VA FileMan's SQLI.

Protection

The following global protection should be set:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 27%" />
<col style="width: 26%" />
</colgroup>
<tbody>
<tr class="odd">
<td rowspan="2"><strong>Global Name</strong></td>
<td colspan="3"><strong>Protection</strong></td>
</tr>
<tr class="even">
<td><strong>DSM for OpenVMS</strong></td>
<td><strong>OpenM</strong></td>
<td><strong>MSM-DOS</strong></td>
</tr>
<tr class="odd">
<td>^DMSQ</td>
<td><p>System: RWD</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>User: RW</p></td>
<td><p>Owner: RWD</p>
<p>Group N</p>
<p>World: N</p>
<p>Network: RWD</p></td>
<td><p>System: RWD</p>
<p>World: RWD</p>
<p>Group: RWD</p>
<p>User: RWD</p></td>
</tr>
</tbody>
</table>

<span id="_Toc93909210" class="anchor"></span>Table 5‑2: SQLI file protection

### SQLI Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following routines are distributed in VA FileMan Patch DI\*21.0\*38 (i.e., SQLI software):

DMSQ, DMSQD, DMSQE, DMSQF, DMSQF1, DMSQF2, DMSQP, DMSQP1, DMSQP2, DMSQP3, DMSQP4, DMSQP5, DMSQP6, DMSQS, DMSQT, DMSQT1, DMSQU

<span id="_Toc93909211" class="anchor"></span>Figure 5‑2: SQLI routines

### SQLI Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI (VA FileMan) (DMSQ MENU)

\|

\|

------------------------------------------RUN Regenerate SQLI Projection

\[DMSQ PROJECT\]

\*\*LOCKED: XUPROGMODE\*\*

------------------------------------------WHY Find Out SQLI Status \[DMSQ

DIAGNOSTICS\]

------------------------------------------ERR Print Errors from Last

Projection \[DMSQ PRINT ERRORS\]

--------------------------------------------X Purge SQLI Data \[DMSQ PURGE\]

\*\*LOCKED: XUPROGMODE\*\*

---DD Table Statistics Reports \[DMSQ -----DD1 Field Listing by File (Brief)

TS MENU\] \[DMSQ TS FIELDS BRIEF\]

\|

\|-------------------------------DD2 Field Listing by File (Full)

\| \[DMSQ TS FIELDS FULL\]

\|

\|-------------------------------IN1 List Subfile Links (Brief)

\| \[DMSQ TS SUBFILE BRIEF\]

\|

\|-------------------------------IN2 List Incoming Pointer/Subfile

\| Links (Full) \[DMSQ TS PTR

\| SUBFILE FULL\]

\|

\|------------------------------OUT1 List Pointer and Parent Links

\| (Brief) \[DMSQ TS PTR PARENT

\| BRIEF\]

\|

\|------------------------------OUT2 List Pointer and Parent Links

\| (Full) \[DMSQ TS PTR PARENT

\| FULL\]

\|

\|------------------------------CNT1 Pointer Statistics by

\| Individual Table \[DMSQ TS PTR

\| STATS\]

\|

\|------------------------------CNT2 Pointer Statistics (Summary)

\| \[DMSQ TS PTR STATS SUMMARY\]

\|

\|------------------------------NAME Table Name Listing (VA FileMan

vs. SQLI) \[DMSQ TS NAMES\]

-CNTS Site Statistics Reports \[DMSQ ------TBL Table Total (Excluding Index

PS MENU\] Tables) \[DMSQ PS TOTAL TABLES\]

\|

\|--------------------------------1C Column Total (All Tables)

\| \[DMSQ PS TOTAL COLUMNS\]

\|

\|------------------------------INDX Index Table Total \[DMSQ PS

\| TOTAL INDEXES\]

\|

\|------------------------------ELEM Table Element Totals, By Type

\| \[DMSQ PS TOTAL TABLE ELEMENTS\]

\|

\|--------------------------------2C Column Totals, by Table \[DMSQ

\| PS TOTAL TABLE COLS\]

\|

\|--------------------------------3C Column Totals, by Table

\| (Ordered by \# of Columns)

\| \[DMSQ PS TOTAL TABLE COLS A\]

\|

\|--------------------------------4C Columns in Regular Tables

\| Total \[DMSQ PS TOTAL COLUMNS

\| REG\]

\|

\|------------------------------FLDS Columns in Regular Tables,

\| Excluding ID Columns \[DMSQ PS

\| COLUMNS REG NOID\]

\|

\|-------------------------------DOM Columns by Domain \[DMSQ PS

COLUMNS BY DOMAIN\]

------------------------------------------GRP Suggest Table Groupings \[DMSQ

SUGGEST TABLE GROUPINGS\]

<span id="_Toc93909212" class="anchor"></span>Figure 5‑3: SQLI options—Menu tree

### Application Program Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following SQLI APIs are supported references that can be called from application code (listed alphabetically by routine name and by tag name within routine name).

#### SETUP^DMSQ: Generate SQLI Projection (Interactive)

|                      |                                                                                                                                                                                          |     |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Reference Type   | Supported                                                                                                                                                                                |     |
| Category         | SQLI                                                                                                                                                                                     |     |
| IA \#            |                                                                                                                                                                                          |     |
| Description      | This API interactively generates the SQLI projection. It purges the contents of the SQLI files and builds a new projection. Load keywords with the KW^DMSQD prior to calling ALLF^DMSQF. |     |
| Format           | SETUP^DMSQ                                                                                                                                                                               |     |
| Input Parameters | none                                                                                                                                                                                     |     |
| Output           | none                                                                                                                                                                                     |     |

#### KW^DMSQD(): Add Keywords

<table>
<colgroup>
<col style="width: 19%" />
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
<td colspan="2">SQLI</td>
</tr>
<tr class="odd">
<td><strong>IA #</strong></td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td><strong>Description</strong></td>
<td colspan="2"><p>For M-to-SQL vendors. Adds reserved keywords to the SQLI_KEY_WORD file (#1.52101)—words that should <em>not</em> be used in the naming of files, fields, and other entities. Make sure that a site populates the SQLI_KEY_WORD file (#1.52101) with any reserved words <em>before</em> the site generates the SQLI projection.</p>
<p>The SQLI_KEY_WORD file (#1.52101) does <em>not</em> come populated by SQLI. Therefore, M-to-SQL vendors should use the KW^DMSQD entry point with which to populate the SQLI_KEY_WORD file (#1.52101):</p>
<ul>
<li><p>The standard set of reserved keywords for SQL as defined by the ANSI standard for SQL.</p></li>
<li><p>The keywords for ODBC as defined by Microsoft.</p></li>
<li><p>Any keywords specific to your (vendor) M-to-SQL product.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>Format</strong></td>
<td colspan="2">KW^DMSQD(global_root [,.output_array])</td>
</tr>
<tr class="even">
<td><strong>Input Parameters</strong></td>
<td>global_root:</td>
<td><p>(required) Global root of global location containing keywords. For example, if you pass $NA(^TMP("SQA",$J)) as the global reference, then the array of keywords should be in the format:</p>
<p>^TMP("SQA",132414124,1)=keyword1</p>
<p>^TMP("SQA",132414124,2)=keyword2</p>
<p>(etc.)</p></td>
</tr>
<tr class="odd">
<td></td>
<td>.output_array</td>
<td>(optional) Pass by reference. The array in which error messages should be returned.</td>
</tr>
<tr class="even">
<td><strong>Output</strong></td>
<td>output_array</td>
<td>Any error messages that result from trying to add keywords are returned in this array, if the array is passed as a parameter to the call.</td>
</tr>
</tbody>
</table>

Example

\>D KW^DMSQD(\$NA(^TMP("SQA",\$J)))

#### ALLF^DMSQF: Generate SQLI Projection (Non-Interactive)

|                      |                                                                                                                                                                                              |     |
|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Reference Type   | Supported                                                                                                                                                                                    |     |
| Category         | SQLI                                                                                                                                                                                         |     |
| IA \#            |                                                                                                                                                                                              |     |
| Description      | This API non-interactively generates the SQLI projection. It purges the contents of the SQLI files and builds a new projection. Load keywords with the KW^DMSQD prior to calling ALLF^DMSQF. |     |
| Format           | ALLF^DMSQF                                                                                                                                                                                   |     |
| Input Parameters | none                                                                                                                                                                                         |     |
| Output           | none                                                                                                                                                                                         |     |

#### ALLS^DMSQS: Cardinality of All Tables

|                      |                                                                                                                                                                                                                                     |     |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|
| Reference Type   | Supported                                                                                                                                                                                                                           |     |
| Category         | SQLI                                                                                                                                                                                                                                |     |
| IA \#            |                                                                                                                                                                                                                                     |     |
| Description      | For M-to-SQL vendors. Calculates T_ROW_COUNT (SQLI_TABLE file \[#1.5215\]) and P_ROW_COUNT (SQLI_PRIMARY_KEY file \[#1.5218\]), for *all* tables projected by SQLI. You can call this after the SQLI projection has been generated. |     |
| Format           | ALLS^DMSQS                                                                                                                                                                                                                          |     |
| Input Parameters | none                                                                                                                                                                                                                                |     |
| Output           | none                                                                                                                                                                                                                                |     |

#### STATS^DMSQS(): Cardinality of One Table

|                      |                                                                                                                                                                                                                                                  |                                                                             |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                                                                                                        |                                                                             |
| Category         | SQLI                                                                                                                                                                                                                                             |                                                                             |
| IA \#            |                                                                                                                                                                                                                                                  |                                                                             |
| Description      | For M-to-SQL vendors. Calculates T_ROW_COUNT (SQLI_TABLE file \[#1.5215\]) and P_ROW_COUNT (SQLI_PRIMARY_KEY file \[#1.5218\]), for a given table. Call this if you need the cardinality of any table that has *already* been projected by SQLI. |                                                                             |
| Format           | STATS^DMSQS(tableien)                                                                                                                                                                                                                            |                                                                             |
| Input Parameters | tableien:                                                                                                                                                                                                                                        | (required) IEN of the table to generate T_ROW_COUNT and P_ROW_COUNT values. |
| Output           | none                                                                                                                                                                                                                                             |                                                                             |

#### \$\$CN^DMSQU(): Column Name

|                      |                                                                                                                                                                   |                                                                                                |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                         |                                                                                                |
| Category         | SQLI                                                                                                                                                              |                                                                                                |
| IA \#            |                                                                                                                                                                   |                                                                                                |
| Description      | One of SQLI's internal naming functions. Returns a column name unique for a given SQLI table, making sure the name is *not* in the SQLI_KEY_WORD file (#1.52101). |                                                                                                |
| Format           | \$\$CN^DMSQU(table,column,name)                                                                                                                                   |                                                                                                |
| Input Parameters | table:                                                                                                                                                            | (required) Internal record number of table in SQLI_TABLE file (#1.5215).                       |
|                      | column:                                                                                                                                                           | (required) Internal record number of column in question, in SQLI_TABLE_ELEMENT file (#1.5216). |
|                      | name:                                                                                                                                                             | (required) Proposed name to use for column (literal string).                                   |
| Output           | returns:                                                                                                                                                          | Returns the unique column name.                                                                |

Example

\> W \$\$CN^DMSQU(297,3407,"NAME")

NAME

#### \$\$FNB^DMSQU(): Table Name

|                      |                                                                                                                                                                                                                                           |                                                                          |
|----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                                                                                                 |                                                                          |
| Category         | SQLI                                                                                                                                                                                                                                      |                                                                          |
| IA \#            |                                                                                                                                                                                                                                           |                                                                          |
| Description      | One of SQLI's internal naming functions. Returns a unique table name compared with existing SQLI_TABLE file (#1.5215) entries in the same schema, making sure the table name is *not* a keyword (in the SQLI_KEY_WORD file \[#1.52101\]). |                                                                          |
| Format           | \$\$FNB^DMSQU(file,table)                                                                                                                                                                                                                 |                                                                          |
| Input Parameters | file:                                                                                                                                                                                                                                     | (required) VA FileMan file/subfile number.                               |
|                      | table:                                                                                                                                                                                                                                    | (required) Internal record number of table in SQLI_TABLE file (#1.5215). |
| Output           | returns:                                                                                                                                                                                                                                  | Returns the unique table name.                                           |

Example

\> W \$\$FNB^DMSQU(1,580)

FILE1

#### \$\$SQLI^DMSQU(): SQL Identifier

|                      |                                                                                                                                                                             |                                                                          |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                                   |                                                                          |
| Category         | SQLI                                                                                                                                                                        |                                                                          |
| IA \#            |                                                                                                                                                                             |                                                                          |
| Description      | One of SQLI's internal naming functions. Returns valid SQL identifier based on the input string. Does *not* check for conflicts with SQLI_KEY_WORD file (#1.52101) entries. |                                                                          |
| Format           | \$\$SQLI^DMSQU(string,length)                                                                                                                                               |                                                                          |
| Input Parameters | string:                                                                                                                                                                     | (required) Initial string for which you wish to generate SQL identifier. |
|                      | length:                                                                                                                                                                     | (required) Maximum length of the generated identifier.                   |
| Output           | returns:                                                                                                                                                                    | Returns the valid SQL identifier based on the input string.              |

Example

\> W \$\$SQLI^DMSQU("FILE",30)

FILE

#### \$\$SQLK^DMSQU(): SQL Identifier (Not a Keyword)

|                      |                                                                                                                                                                                      |                                                                          |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| Reference Type   | Supported                                                                                                                                                                            |                                                                          |
| Category         | SQLI                                                                                                                                                                                 |                                                                          |
| IA \#            |                                                                                                                                                                                      |                                                                          |
| Description      | One of SQLI's internal naming functions. Returns valid SQL identifier based on the input string, making sure the identifier is *not* a keyword (in SQLI_KEY_WORD file \[#1.52101\]). |                                                                          |
| Format           | \$\$SQLK^DMSQU(string,length)                                                                                                                                                        |                                                                          |
| Input Parameters | string:                                                                                                                                                                              | (required) Initial string for which you wish to generate SQL identifier. |
|                      | length:                                                                                                                                                                              | (required) Maximum length of the generated identifier.                   |
| Output           | returns:                                                                                                                                                                             | Returns the valid SQL identifier based on the input string.              |

Example

\> W \$\$SQLK^DMSQU("FILE",30)

FILE1

### Other Supported References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### SQLI Files, Fields, and Cross-references

All of SQLI's files, fields, and cross-references as distributed in VA FileMan Patch DI\*21.0\*38 (i.e., SQLI software) can be referenced directly without integration agreements. This enables M-to-SQL vendors to create SQLI mapping utilities using the SQLI file structures. Specifically, these are the files in the 1.52 to 1.53 number range, all stored in ^DMSQ.

#### Direct Mode Utilities

Direct mode utilities can be used from programmer mode, but developers may not call them from within applications.

|                         |                                                                                                                                                                                                                                                                                                                                                                            |
|-------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Direct Mode Utility | Description                                                                                                                                                                                                                                                                                                                                                            |
| MAIN^DMSQE              | This routine is used by the Print Errors from Last Projection option \[DMSQ PRINT ERRORS\] to list errors generated during the most recent SQLI projection.                                                                                                                                                                                                                |
| RUNONE^DMSQ             | This routine is provided as a troubleshooting utility only. When the SQLI projection aborts due to a data dictionary anomaly, you can use RUNONE^DMSQ to run a "test" projection for a single file or subfile. Primarily this enables you to test whether or not you fixed the data dictionary anomaly, before starting a new SQLI projection for all files on the system. |

<span id="_Toc93909213" class="anchor"></span>Table 5‑3: SQLI Direct mode utilities

## ## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| BASE VALUE            | The stored value of a column in SQL, not transformed in any way.                                                                                                                                                                                                          |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CARDINALITY           | The cardinality of a table is its number of rows; the cardinality of a domain is the number of possible values in the domain.                                                                                                                                             |
| COLUMN                | A set of values for a particular value sequence in a row, for each row in a table (akin to a VA FileMan field). All values in a column must be of the same data type or domain.                                                                                           |
| DATA TYPE             | A set of possible values. SQL has its own set of standard data types; SQL vendors often implement additional data types.                                                                                                                                                  |
| DATA DICTIONARY       | A file that defines a file's structure, to include a file's fields and relationships to other files.                                                                                                                                                                      |
| DBA                   | Database Administrator for an SQL system. The DBA has, by default, full privileges to every object in the database.                                                                                                                                                       |
| DBS                   | Database Server. DBS is a non-interactive VA FileMan API. It makes no writes to the screen. It provides client/server access to VA FileMan data. DBS calls of particular interest to M-to-SQL vendors using SQLI include \$\$GET1^DIQ, FIELD^DID, and \$\$EXTERNAL^DILFD. |
| DCL                   | Data Control Language. The set of SQL statements through which access to the database is controlled.                                                                                                                                                                      |
| DDL                   | Data Definition Language. The set of SQL statements through which objects are created and modified in the database.                                                                                                                                                       |
| DML                   | Data Manipulation Language. The set of SQL statements through which data is modified.                                                                                                                                                                                     |
| DOMAIN                | A set of permissible values. A domain is based on a data type, but may contain further constraints on what values are valid for the domain.                                                                                                                               |
| EXTRACT STORAGE       | When the storage location for a particular VA FileMan field is designated to be by position on a global node, instead of being character-delimited.                                                                                                                       |
| FIELD TYPE            | The type of VA FileMan field. There are nine FileMan field types. VA FileMan field types loosely correspond to the concept of *data type*.                                                                                                                                |
| FOREIGN KEY           | A foreign key acts as a ready-to-use join between two tables. It matches a set of columns in one table to the primary key in another table.                                                                                                                               |
| HIERARCHICAL DATABASE | A database structure in which files can own or belong to each other. Often referred to as a parent-child structure.                                                                                                                                                       |
| IEN                   | Internal entry number. This is the numeric subscript beneath a file's global root under which all of the data for a given VA FileMan file entry is stored.                                                                                                                |
| IEN COLUMN            | A column SQLI projects to contain the IEN of a VA FileMan entry.                                                                                                                                                                                                          |
| JOIN                  | In SQL, a join is when two or more tables are combined into a single table based on column values in an SQL SELECT statement.                                                                                                                                             |
| M-TO-SQL PRODUCT      | Software that can view structured M globals as relational tables through SQL.                                                                                                                                                                                             |
| MULTIPLE-VALUED FIELD | A VA FileMan filed that allows more than one value for a single entry. See also Subfile.                                                                                                                                                                                  |
| ODBC                  | Open Database Connectivity. ODBC is Microsoft's solution to enable client access to heterogeneous databases.                                                                                                                                                              |
| OUTER JOIN            | A join between two tables, where rows from one table are present in the joined table, even when there are no corresponding rows from the other table.                                                                                                                     |
| OUTPUT FORMATS        | Output formats are provided by SQLI to convert column base values into a format suitable for external use by end-users.                                                                                                                                                   |
| PRIMARY KEY           | A designated set of columns in a table whose values uniquely identify any row in the table.                                                                                                                                                                               |
| QUERY                 | An SQL command that extracts information from an SQL database.                                                                                                                                                                                                            |
| RELATIONAL DATABASE   | A database that is a collection of tables, and whose operations follow the relational model.                                                                                                                                                                              |
| ROW                   | A sequence of values in a table, representing one logical record.                                                                                                                                                                                                         |
| SCHEMA                | A schema defines a portion of an SQL database as being owned by a particular user.                                                                                                                                                                                        |
| SQL                   | Structured Query Language, the predominant language and set of facilities for working with relational data. The current ANSI (American National Standards Institute) standard for SQL is X3.135-1992.                                                                     |
| SQLI MAPPER           | Software written by an M-to-SQL vendor that maps the vendor's SQL data dictionaries directly to VA FileMan data, using the information projected by SQLI.                                                                                                                 |
| SUBFILE               | The data structure of a multiple-valued field. In many respects, a subfile has the same characteristics as a file.                                                                                                                                                        |
| TABLE                 | A collection of rows, where each row is the equivalent of a record. A base table (one not derived from another table) is the SQL equivalent of a database file.                                                                                                           |
| TABLE ELEMENT         | a column, primary key, or foreign key that is part of a table.                                                                                                                                                                                                            |
| VIEW                  | A user-defined subset of tables, based on a SELECT statement, containing only selected rows and columns.                                                                                                                                                                  |
| .01 FIELD             | A field that exists for every VA FileMan file, and that is used as the primary lookup value for a record.                                                                                                                                                                 |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](di-21-38-site-manual/030.png)</td>
<td><p>For a comprehensive list of commonly used infrastructure- and security-related terms and definitions, please visit the ISS Glossary Web page at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/glossary.asp">http://vista.med.va.gov/iss/glossary.asp</a></p>
</blockquote>
<p>For a list of commonly used acronyms, please visit the ISS Acronyms Web site at the following Web address:</p>
<blockquote>
<p><a href="http://vista/med/va/gov/iss/acronyms/index.asp">http://vista/med/va/gov/iss/acronyms/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Appendix A—Case Studies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Case studies are provided in this appendix to give concrete information about how sites are implementing SQLI, what kinds of projects they are trying out, and what kind of experiences they have had using SQLI.

Additional case studies after the publication of this manual may be added to the SQLI Web site:

> <http://vista.med.va.gov/sqli/index.asp>

Profile: San Francisco VA Medical Center (VAMC)Configuration Information

Site Name: San Francisco VAMC

Site M implementation: DSM for OpenVMS AXP

Which database? (production, etc.): Production

M-to-SQL product used: KB_SQL V. 3.5

Size of M-to-SQL license chosen (#users): 8

Installation Information

- Did IRM install SQLI and M-to-SQL product? Yes
- Time to generate full SQLI projection + SQLI mapping: 5 1/2 hours
- Disk space used by SQLI projection: 43 megabytes
- Disk space used by M-to-SQL mapping: 40 megabytes

User Information

- Purpose of SQL access to VA FileMan data: Web-based telephone directory (for the first SQL project).
- Who are the end users: Web users, including on-site VAMC staff, affiliated medical school users, and VA intranet-wide users.
- Who is DBA? IRM.
- Methods of user access: Web browser.

Project-Specific Details

The station's telephone directory is served out on Web pages. Several methods of lookup are provided so that you do not have to scan the entire directory list.

The telephone directory application is based on the use of Active Server Pages (ASPs). ASPs use server-side scripting to retrieve records from a database and return them as table rows in pre-formatted Web pages.

Microsoft's Visual InterDev was used to build the server-side scripting in the ASPs. Each embedded script that executes on the server uses ODBC to perform a particular database query.

The Web server (a Pentium running Windows NT) is set up with an ODBC driver that connects over TCP/IP to KB_SQL running on the production M system.

KB_SQL acts as an ODBC data source, with an ODBC listener process running continuously. KB_SQL's data dictionaries are mapped based on SQLI to directly access VA FileMan data as tables.

![](di-21-38-site-manual/031.png)

<span id="_Toc93909214" class="anchor"></span>Figure 5‑4: Sample "Staff Directory" application (GUI window) at the San Francisco, CA VAMC

Pages that Retrieve a List of VA FileMan Records

For a Web page that is going to list multiple records, a table is used, with one record listed per table row. Using Visual InterDev, a data range header and data range footer control is inserted on the Web page. The data range header performs a "select" query (or can reference a stored procedure, which executes a "select" query on the server).

Between the controls, HTML code is used that creates a single row within a table (but not the table itself). A retrieved column value can be inserted in the row's table cells using the ASP syntax \<%= DataRangeHdr1("column_name") %\>. When the page is displayed, one table row is displayed per retrieved record.

Pages that Retrieve and Display a Single VA FileMan Record

For a Web page that retrieves and displays a single record, you can present the data from the record in any format you choose (not just in a table). Using Visual InterDev, a data command control is inserted on the Web page. This control contains a query that should retrieve a single table row. Then, in the HTML elsewhere on the Web page, you can insert values from the record using the ASP syntax \<% DataCommand1("column_name") %\>.

Hurdles

- Variable Pointer Fields  
  >   
  > When accessing a variable pointer field through ODBC, only the unresolved internal value of the pointer field was returned. To get the resolved external value of a variable pointer field, a new free text field was made for the file in question. A trigger cross-reference was added to the variable pointer field. The trigger obtains the resolved variable pointer field value and stuffs it into the free text field. This free text field can then be retrieved through KB_SQL.
- Foreign Keys - How to Use through ODBC  
  >   
  > KB_SQL supports the use of foreign key syntax, which allows the values of fields in tables that have a "join" relationship to be accessed without having to do an actual join between the two tables. The main advantage of KB_SQL's foreign key (implicit join) syntax over joins is that rows are not lost when the values of join columns are blank. For example, if you are joining two tables based on the column for a pointer field, some entries may have a null value for the pointer field - but that table row was still desired.  
  >   
  > KB_SQL's foreign key syntax works correctly when a query is done entirely in KB_SQL. When query results are returned through ODBC, however, there is an error because ODBC does not recognize columns retrieved through resolving foreign keys. The solution was to define an alias for the resolved foreign key (e.g., SERVICE_SECTION_FK@NAME AS SERV_NAME). The column values are returned through ODBC under the alias SERV_NAME.
- Stored Procedures - Increased Performance  
  >   
  > KB_SQL stored procedure provide a performance advantage over executing an SQL query passed whole through ODBC to KB_SQL. This is because stored procedures call a query that is already compiled in KB_SQL, whereas a query issued directly is compiled by KB_SQL each time prior to being executed.

Profile: Brooklyn VA Medical CenterConfiguration Information:

Site Name: Brooklyn VAMC/VISN 3

Site M implementation: DSM

Which database? (Production, etc.): Test now; Production eventually

M-to-SQL product used: KB_SQL

Size of M-to-SQL license chosen (#users): 8

Size of Site Database: 1 gigabyte (Test)

Installation Information

- Did IRM install SQLI and M-to-SQL product? No; KB Systems did
- Number of tables projected: 4000
- Length of running SQLI mapper, and SQLI mapper: 3.25 hours (both together)
- Size of SQLI files after projection: 25 megabytes
- Disk space used by M-to-SQL mapping: 25 megabytes

User Information

- Purpose of SQL access to VA FileMan data: Let users export data to their PCs so they can create their own custom reports.
- Who are the end users: IRM and selected end-users.
- Who is DBA? An IRM developer.
- Methods of user access: Through the MedRecord Gateway for Windows product.

Project-Specific Details

The goal of this project is to enable end-users to create their own custom reports on VA FileMan data. Without this project, end-users typically have IRM create custom VA FileMan reports for them. IRM will also generate some of its own reports using the tools provided by this project, as well as creating traditional VA FileMan reports.

The product used as the front end to this project is MedRecord Gateway for Windows (MGW) from Strategic Reporting Systems, Inc. It runs as an ActiveX control in the Internet Explorer Web browser.

The MGW part of the solution is analogous to a GUI client version of the VA FileMan Export tool, using a forms-driven SQL-based interface. The View Manager module allows privileged users to create views for end-users. The Wizard module allows Web users to authenticate themselves, create a query against tables or a pre-defined view in a GUI interface, retrieve the corresponding table rows and load them directly into Excel (currently) and ReportSmith (future).

The total solution, wherein users can enter queries and get the results in Excel or ReportSmith, amounts to an alternative report generator module for VA FileMan.

View Manager Module

MGW's View Manager module allows IRM and other users with sufficient privileges to define views for use by other end-users. It is implemented as an ActiveX control that is used through a Web browser.

Wizard Module

MGW's Wizard client module is analogous to VA FileMan's Export tool, with a number of advantages including a forms-driven GUI interface for query creation and seamless retrieval of data from host to client. It can be used as a client to access a VA FileMan database, a Microsoft SQL Server database, and a Microsoft Access database. The Wizard module is implemented as an ActiveX control that is used through a Web browser.

Connection to the VA FileMan database (through KB_SQL and SQLI) is handled with the KB_SQL ODBC driver, which is installed on each client. The ActiveX control uses the ODBC driver transparently to retrieve data from the server.

Data is retrieved using the following six basic steps:

1.  Select tables or view for the query.
2.  Select the fields to use in the query.
3.  Set query criteria.
4.  Choose the sort order for the returned table rows.
5.  Execute query (rows are returned to the Wizard ActiveX control.)
6.  Export data from the Wizard control to Microsoft Excel.

Screen captures[^1] of a simple query on the NEW PERSON file (#200) using the MGW Wizard module follow:

![](di-21-38-site-manual/032.png)

<span id="_Toc93909215" class="anchor"></span>Figure 5‑5: Step \#1: Select tables or view

![](di-21-38-site-manual/033.png)

<span id="_Toc93909216" class="anchor"></span>Figure 5‑6: Step \#2: Select the fields

![](di-21-38-site-manual/034.png)

<span id="_Toc93909217" class="anchor"></span>Figure 5‑7: Step \#3: Select Criteria—Names that begin with "F"

![](di-21-38-site-manual/035.png)

<span id="_Toc93909218" class="anchor"></span>Figure 5‑8: Step \#4: Choose sort order

![](di-21-38-site-manual/036.png)

<span id="_Toc93909219" class="anchor"></span>Figure 5‑9: Step \#5: Execute a query

![](di-21-38-site-manual/037.png)

<span id="_Toc93909220" class="anchor"></span>Figure 5‑10: Step \#6: Export to Microsoft Excel

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$
\$\$CN^DMSQU, 5-10
\$\$FNB^DMSQU, 5-11
\$\$SQLI^DMSQU, 5-12
\$\$SQLK^DMSQU, 5-13
A
Access
Managing Access to VA FileMan Data, 3-10
Selectively Grant Access to VA FileMan Data, 3-10
Acronyms (ISS)
Home Page Web Address, Glossary, 3
Advantages of Mapping to VA FileMan through SQLI, 1-3
After the First Mapping, 2-10
ALLF^DMSQF, 5-8
ALLS^DMSQS, 5-8
Anticipate Training Needs, 2-5
APIs
\$\$CN^DMSQU, 5-10
\$\$FNB^DMSQU, 5-11
\$\$SQLI^DMSQU, 5-12
\$\$SQLK^DMSQU, 5-13
ALLF^DMSQF, 5-8
ALLS^DMSQS, 5-8
KW^DMSQD, 5-7
SETUP^DMSQ, 5-6
STATS^DMSQS, 5-9
Appendix A—Case Studies, A, 1
Application Program Interfaces (APIs), 5-6
Assumptions About the Reader, xv
Asterisked Files, 2-11
B
Base Values, 4-8
Build Web Applications, 4-2
Business Rules, 4-15
Do *Not* Allow Updates to VA FileMan File Data from SQL, 3-10
C
Callout Boxes, xiv
Case Studies, A, 1
Check/Fix DD Structure Option, 2-8, 3-6
Choose and Purchase M-to-SQL Vendor's Software, 2-4
Column Names for Fields, 4-5
Columns
Base vs. External Data Values, 4-8
Data Format, 4-8
DBA Reports, 4-7
IEN, 4-8
Commands
Delete, 4-15
Insert, 4-15
Update, 4-15
Companion to this Manual
SQLI Web Site, xi
Compatibility
Kernel, 3-4
VA FileMan, 3-11
Components of an M-to-SQL System Using SQLI, 2-1
Configure M-to-SQL System, 2-6
Consistency of Naming Supports Query Sharing between Sites, 4-3
Contents, v
Cross-references, 5-14
Non-regular, 2-12
D
Dangling Pointers, 2-11
Data Dictionary
Data Dictionary Utilities Menu, xv
Listings, xv
Data Format of Columns, 4-8
Data Must Be VA FileMan-Compatible, 3-11
DBA, 2-8, 3-10
Managing Access to VA FileMan Data, 3-10
Reports, 4-7
Training, 2-5
Delete Command, 4-15
Determine Desired Type(s) of Access to VA FileMan Data, 2-2
Determining the Current Status of the Projection, 3-2
Developers
Note to Developers, 1-4
DI DDUCHK Option, 2-8
Direct Mode Utilities, 5-14
MAIN^DMSQE, 5-14
RUNONE^DMSQ, 3-6, 5-14
Directly Access the VistA Database from Windows Applications, 4-2
Disable SQL Access while Remapping, 3-1
Disk Space Needed, 2-6
DMSQ
RUNONE^DMSQ, 3-6, 5-14
SETUP^DMSQ, 5-6
DMSQ DIAGNOSTICS Option, 2-9, 3-2, 3-6
DMSQ PRINT ERRORS Option, 3-7, 5-14
DMSQ PROJECT Option, 2-8, 3-1, 3-2, 3-4
DMSQ PS MEN Option, 4-7
DMSQ PURGE Option, 3-11
DMSQ TS MENU Option, 4-7
DMSQD
KW^DMSQD, 5-7
DMSQE
MAIN^DMSQE, 5-14
DMSQF
ALLF^DMSQF, 5-8
DMSQS
ALLS^DMSQS, 5-8
STATS^DMSQS, 5-9
DMSQU
\$\$CN^DMSQU, 5-10
\$\$FNB^DMSQU, 5-11
\$\$SQLI^DMSQU, 5-12
\$\$SQLK^DMSQU, 5-13
Do *Not* Allow Updates to VA FileMan File Data from SQL, 3-10
Do *Not* Map Manually, 3-11
Do the First SQLI Projection and Mapping, 2-8
Documentation
Revisions, iii
Symbols, xiii
E
End-User Training, 2-5
Ensuring the Accuracy of the Mapping, 3-11
Enter or Edit File Entries Option, 4-15
Errors
Generated During SQL Access, 3-9
Messages, 3-8
Messages from SQLI Projections, 3-7
Troubleshooting Errors that Abort SQLI, 3-6
EVS Anonymous Directories, xvii
External Values, 4-8
F
Fields, 5-14
.001 Number, 2-11
Attributes Not Projected, 2-11
Column Names for Fields, 4-5
Multiline Computed Fields, 2-11
Word-processing Fields, 4-9
Figures and Tables, ix
File Diagram, 5-2
Files, 5-1, 5-14
Asterisked, 2-11
Attributes *Not* Projected, 2-11
Journaling, 5-3
NEW PERSON (#200), 7
Not in ^DIC, 2-11
Protection, 5-3
SQLI_ERROR_LOG (#1.52192), 2-11, 3-1, 3-7
SQLI_KEY_WORD (#1.52101), 2-8, 3-1, 3-4, 5-7, 5-10, 5-11, 5-12, 5-13
SQLI_PRIMARY_KEY (#1.5218), 5-8, 5-9
SQLI_TABLE (#1.5215), 5-8, 5-9, 5-10, 5-11
SQLI_TABLE_ELEMENT (#1.5216), 5-10
TERMINAL TYPE (#3.2), 4-5
Translation, 5-3
VA FileMan Files as Tables, 4-4
Find Out SQLI Status Option, 2-9, 3-2, 3-6
Flattening of Subfiles into Standalone Tables, 4-12
FORUM, iv
G
Globals, 5-1
Journaling, 5-3
Protection, 5-3
Translation, 5-3
Glossary, 1
Glossary (ISS)
Home Page Web Address, Glossary, 3
Granting Access, 3-10
Selectively Grant Access to VA FileMan Data, 3-10
H
Help
At Prompts, xv
Online, xv
Home Pages
Adobe Acrobat Quick Guide Web Address, xvi
Adobe Web Address, xvi
Health Systems Design and Development (HSD&D) Web Address, xvi
ISS Acronyms Home Page Web Address, Glossary, 3
ISS Glossary Home Page Web Address, Glossary, 3
SQLI Home Page Web Address, xi, xvi
VistA Documentation Library (VDL) Home Page Web Address, xvii
Host-based Queries, 2-2
How to
Obtain Technical Information Online, xiv
Purge SQLI Data, 3-11
Use this Manual, xiii
I
IEN Column, 4-8
If M-to-SQL Service Exists, 2-7
If No M-to-SQL Service Exists, 2-7
Implementation Notes, 2-11
Insert Command, 4-15
Install and Configure M-to-SQL System, 2-6
Installing SQLI, 2-1–2-12
Internal VA FileMan Tables Not Projected, 2-11
Introduction, 1-1
ISS Acronyms
Home Page Web Address, Glossary, 3
ISS Glossary
Home Page Web Address, Glossary, 3
J
Joining Tables, 4-10–4-15
Using Foreign Keys, 4-11
Journaling, 5-3
Files, 5-3
K
Kernel, 3-2, 3-4
Kernel Compatibility, 3-4
Keys
Primary, 4-10
KW^DMSQD, 5-7
L
List File Attributes Option, xv
Losing Parent Table Rows when Joining with Subfile Tables, 4-14
Losing Rows When a Pointer Field Column is Null, 4-11
M
MAIN^DMSQE, 5-14
Managing SQLI, 3-1–3-11
Mapping
Do *Not* Map Manually, 3-11
Ensuring the Accuracy of the Mapping, 3-11
VA FileMan to SQL without SQLI, 1-2
Menus
Data Dictionary Utilities, xv
Messages
SQLI Error Messages, 3-8
MGW Wizard, 7
M-to-SQL Service
Exists, 2-7
None Exists, 2-7
M-to-SQL Software, 2-3, 2-4
M-to-SQL System, 2-6
Multiline Computed Fields, 2-11
N
Naming
Columns for Fields, 4-5
Consistency, 4-3
DBA Reports, 4-7
Issues, 4-3
Rules, 4-3
Subfiles, 4-5
Tables, 4-4
NEW PERSON File (#200), 7
Non-regular Cross-references, 2-12
Notes
Developers, 1-4
Implementation, 2-11
O
Obtain Technical Information Online, How to, xiv
Obtaining Data Dictionary Listings, xv
ODBC
Client Access to VA FileMan Data, 2-3
Support, 2-4
ODBC drivers, 2-1
Online
Documentation, xv
Help Frames, xv
Options, 5-4
Check/Fix DD Structure, 2-8, 3-6
DBA-related Options, 2-10
DI DDUCHK, 2-8
DMSQ DIAGNOSTICS, 2-9, 3-2, 3-6
DMSQ PRINT ERRORS, 3-7, 5-14
DMSQ PROJECT, 2-8, 3-1, 3-2, 3-4
DMSQ PS MEN, 4-7
DMSQ PURGE, 3-11
DMSQ TS MENU, 4-7
Enter or Edit File Entries, 4-15
Find Out SQLI Status, 2-9, 3-2, 3-6
IRM-related Options, 2-10
List File Attributes, xv
Print Errors from Last Projection, 3-7, 5-14
Print File Entries, 4-15
Provide Access to SQLI Options, 2-10
Purge SLQI Data, 3-11
Regenerate SQLI Projection, 3-1, 3-2, 3-4
Run the Regenerate SQLI Projection, 2-8
Search File Entries, 4-15
Site Statistics Reports, 4-7
Table Statistics Reports, 4-7
Orientation, xiii
Other Supported References, 5-14
Output Transforms, 2-12
P
Patches
Revisions, iv
Perform Any Pre-mapping Initialization the SQLI Mapper Vendor Specifies, 3-1
Pointers
Dangling, 2-11
Losing Rows When a Pointer Field Column is Null, 4-11
Recreating a Pointer Field Relationship between Tables, 4-11
Variable, 2-12
Primary Keys, 4-10
Print Errors from Last Projection Option, 3-7, 5-14
Print File Entries Option, 4-15
Profiles
Brooklyn VA Medical Center, 5
San Francisco VA Medical Center (VAMC), A, 2
Projection and Vendor Mapping as One Task, 3-4
Protection, 5-3
Files, 5-3
Provide Access to SQLI Options, 2-10
Purge SLQI Data Option, 3-11
Purging
SQLI Data, 3-11
Q
Query the VistA Database Using SQL, 4-2
Question Mark Help, xv
R
Reader, Assumptions About the, xv
Recreating a Pointer Field Relationship between Tables, 4-11
Recreating the Relationship between a Subfile and its Parents, 4-14
Reference Materials, xvi
Regenerate SQLI Projection Option, 2-8, 3-1, 3-2, 3-4
Regenerating Projection, 3-1
Remapping, 3-1
Reports
DBA, 4-7
Re-projecting SQLI when File Structures Change, 3-1
Required VistA Software, 2-6
Revision History, iii
Documentation, iii
Patches, iv
Routines, 5-3
Run the Regenerate SQLI Projection Option \[DMSQ PROJECT\], 3-1
RUNONE^DMSQ, 3-6, 5-14
S
Scheduling the Projection, 3-2
Scheduling the Vendor Mapping, 3-4
Schemas, 4-5
Search File Entries Option, 4-15
Security
Do *Not* Allow Updates to VA FileMan File Data from SQL, 3-10
Managing Access to VA FileMan Data, 3-10
Training, 2-5
Selectively Grant Access to VA FileMan Data, 3-10
Set Up M-to-SQL System, 2-7
SETUP^DMSQ, 5-6
Site Statistics Reports Option, 4-7
Skills Required, 2-6
SQL and VA FileMan Terminology, xiv
SQL Host-based Queries on VA FileMan Data, 2-2
SQL Training, xiii
SQLI
Advantages of Mapping to VA FileMan through SQLI, 1-3
APIs, 5-6
Cross-references, 5-14
Direct Mode Utilities, 5-14
Fields, 5-14
File Diagram, 5-2
Files, 5-1, 5-14
For End-Users, 4-1
Globals, 5-1, 5-3
Home Page Web Address, xi, xvi
Implementation Notes, 2-11
Installing, 2-1–2-12
Managing, 3-1–3-11
Mapper Implementation, 2-4
Naming Rules, 4-3
Options, 5-4
Projection and Vendor Mapping as One Task, 3-4
Purging Data, 3-11
Routines, 5-3
System Management, 3-1
Technical Information, 5-1
Troubleshooting Errors that Abort SQLI, 3-6
SQLI Web Site
Companion to this Manual, xi
SQLI_ERROR_LOG File (#1.52192), 2-11, 3-1, 3-7
SQLI_KEY_WORD File (#1.52101), 2-8, 3-1, 3-4, 5-7, 5-10, 5-11, 5-12, 5-13
SQLI_PRIMARY_KEY File (#1.5218), 5-8, 5-9
SQLI_TABLE File (#1.5215), 5-8, 5-9, 5-10, 5-11
SQLI_TABLE_ELEMENT File (#1.5216), 5-10
SQLI_TERMINAL_TYPE Table, 4-5
STATS^DMSQS, 5-9
Steps to Provide Relational Access to VA FileMan, 2-1
Supported References, 5-5–5-15
Symbols Found in the Documentation, xiii
T
Table Statistics Reports Option, 4-7
Tables
DBA Reports, 4-7
Flattening of Subfiles into Standalone Tables, 4-12
Internal VA FileMan Tables Not Projected, 2-11
Joining, 4-10
Losing Rows When a Pointer Field Column is Null, 4-11
Names for Subfiles, 4-5
Naming, 4-4
Recreating a Pointer Field Relationship between Tables, 4-11
SQLI_TERMINAL_TYPE, 4-5
VA FileMan Files as Tables, 4-4
TaskMan, 3-2, 3-4
Technical Information, 5-1–5-15
TERMINAL TYPE File (#3.2), 4-5
Terminology
VA FileMan and SQL, xiv
Training, 2-5
End-User, 2-5
SQL, xiii
Transforms
Output, 2-12
Translation, 5-3
Files, 5-3
Troubleshooting
Errors that Abort SQLI, 3-6
U
Update Command, 4-15
Updates
Do *Not* Allow Updates to VA FileMan File Data from SQL, 3-10
URLs
Adobe Acrobat Quick Guide Web Address, xvi
Adobe Home Page Web Address, xvi
Health Systems Design and Development (HSD&D) Home Page Web Address, xvi
Use this Manual, How to, xiii
Using
Adobe Acrobat Reader, xvi
V
VA FileMan and SQL Terminology, xiv
VA FileMan Files as Tables, 4-4
Variable Pointers, 2-12
Vendor Mapping
Scheduling, 3-4
VistA Documentation Library (VDL)
Home Page Web Address, xvii
W
Ways to Access VA FileMan Data through M-to-SQL, 4-2
Web Pages
Adobe Acrobat Quick Guide Web Address, xvi
Adobe Home Page Web Address, xvi
Health Systems Design and Development (HSD&D) Home Page Web Address, xvi
ISS Acronyms Home Page Web Address, Glossary, 3
ISS Glossary Home Page Web Address, Glossary, 3
SQLI Home Page Web Address, xi, xvi
VistA Documentation Library (VDL) Home Page Web Address, xvii
What Other Software is Required to View VA FileMan Data Through SQL?, 1-2
Why Map VA FileMan to SQL?, 1-2
Wizard
MGW, 7
Word-processing Fields, 4-9
[^1]: <sup>\*</sup> Images used by permission of Strategic Reporting Systems, Inc.
