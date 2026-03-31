---
title: DI*21*38 Vendor Guide DRAFT
doc_type: UG
doc_label: User Guide
doc_layer: patch
doc_subject: Vendor Guide DRAFT
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
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - sqli
  - class
  - fileman
  - column
  - strong
  - span
  - primary
  - contents
  - format
page_count: 0
word_count: 20317
section_count: 7
table_count: 38
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: October 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_vendor.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/SQL_Interface_(SQLI)/sqli_vendor.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=25"
---

![](di-21-38-vendor-guide-draft/001.png)

VA FILEMANSQL INTERFACE (SQLI)VENDOR GUIDE(DRAFT)

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
<td>01/18/98</td>
<td>1.0</td>
<td>Initial SQL Interface (SQLI), Patch DI*21.0*38 software documentation creation.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>05/11/98</td>
<td>1.1</td>
<td><p>Added explanation of P_START_AT and P_END_IF for index tables.</p>
<p>Changed documentation of pointer domains from Numeric to Integer.</p>
<p>Corrected table to note that all Computed fields except Numeric are projected as CHARACTER data type.</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
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

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

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
| ![](di-21-38-vendor-guide-draft/002.png) | Used to inform the reader of general information including references to additional reading material. |
| ![](di-21-38-vendor-guide-draft/003.png)                                                              | Used to caution the reader to take special notice of critical information.                            |

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
| ![](di-21-38-vendor-guide-draft/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

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
| ![](di-21-38-vendor-guide-draft/005.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

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
| ![](di-21-38-vendor-guide-draft/006.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

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

- *VA FileMan SQLI Site Manual*
- *VA FileMan SQLI Vendor Manual* (this manual; targeted for M-to-SQL vendors)
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
<td>![](di-21-38-vendor-guide-draft/007.png)</td>
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
| ![](di-21-38-vendor-guide-draft/008.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
    - [What is VA FileMan?](#what-is-va-fileman)
    - [What is SQLI?](#what-is-sqli)
    - [What is the Purpose of this Manual?](#what-is-the-purpose-of-this-manual)
- [Building an SQLI Mapper](#building-an-sqli-mapper)
    - [Information Provided by SQLI](#information-provided-by-sqli)
    - [Organization of SQLI Information](#organization-of-sqli-information)
    - [SQLI Entity-Relationship Diagram](#sqli-entity-relationship-diagram)
    - [Guidelines for SQLI Mappers](#guidelines-for-sqli-mappers)
- [# Parsing the SQLI Projection](#parsing-the-sqli-projection)
    - [About the Examples in this Chapter](#about-the-examples-in-this-chapter)
    - [Using the {B}, {E}, {I}, {K}, and {V} Placeholders](#using-the-b-e-i-k-and-v-placeholders)
    - [Example File](#example-file)
    - [Starting Point: SQLISCHEMA File](#starting-point-sqlischema-file)
    - [Find the Projected Table for a File](#find-the-projected-table-for-a-file)
    - [Processing Tables](#processing-tables)
    - [About Table Elements](#about-table-elements)
    - [Processing Columns](#processing-columns)
    - [Find a Table Element's Column Entry](#find-a-table-elements-column-entry)
    - [IEN Columns](#ien-columns)
    - [Find the Primary Key for a Given Table](#find-the-primary-key-for-a-given-table)
    - [Assembling Record Locations](#assembling-record-locations)
    - [Retrieving Column Values](#retrieving-column-values)
    - [Column Value Conversions](#column-value-conversions)
    - [Foreign Keys](#foreign-keys)
- [VA FileMan and SQL](#va-fileman-and-sql)
    - [VA FileMan, SQL, and the Relational Model](#va-fileman-sql-and-the-relational-model)
    - [VA FileMan File Definition Structures](#va-fileman-file-definition-structures)
    - [VA FileMan Field Types](#va-fileman-field-types)
    - [VA FileMan Subfiles (Multiples)](#va-fileman-subfiles-multiples)
    - [Mapping VA FileMan Fields to SQL Data Types](#mapping-va-fileman-fields-to-sql-data-types)
    - [VA FileMan Indexes](#va-fileman-indexes)
- [File References](#file-references)
    - [SQLISCHEMA File](#sqlischema-file)
    - [SQLIKEYWORD File](#sqlikeyword-file)
    - [SQLIDATATYPE File](#sqlidatatype-file)
    - [SQLIDOMAIN File](#sqlidomain-file)
    - [SQLIKEYFORMAT File](#sqlikeyformat-file)
    - [SQLIOUTPUTFORMAT File](#sqlioutputformat-file)
    - [SQLITABLE File](#sqlitable-file)
    - [SQLITABLEELEMENT File](#sqlitableelement-file)
    - [SQLICOLUMN File](#sqlicolumn-file)
    - [SQLIPRIMARYKEY File](#sqliprimarykey-file)
    - [SQLIFOREIGNKEY File](#sqliforeignkey-file)
    - [SQLIERRORTEXT File](#sqlierrortext-file)
    - [SQLIERRORLOG File](#sqlierrorlog-file)
- [Application Program Interfaces (APIs)—Supported References](#application-program-interfaces-apissupported-references)
- [Other Issues](#other-issues)
    - [Domain Cardinality](#domain-cardinality)
    - [SQLI and Schemas](#sqli-and-schemas)
    - [SQL Identifier Naming Algorithms](#sql-identifier-naming-algorithms)
    - [VA Business Rules and Insert/Update/Delete Operations](#va-business-rules-and-insertupdatedelete-operations)
    - [SQLI Implementation Notes](#sqli-implementation-notes)
  - [Glossary](#glossary)
  - [## Appendix A—Quick Reference Card](#appendix-aquick-reference-card)
  - [Index](#index)

### What is VA FileMan?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan is a database management system (DBMS) which is used at DVA medical facilities. It is implemented in the M programming language.
With the release of VA FileMan Version 21 in December of 1994, VA FileMan introduced a silent Database Server (DBS) programming API, which set the stage for extending database access to non-host users on local and wide area networks. SQLI, for example, makes extensive use of VA FileMan's DBS API.

### What is SQLI?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan's SQLI (SQL Interface) product projects a relational view of VA FileMan data dictionaries for use by M-to-SQL vendors. This provides a supported mechanism for M-to-SQL vendors to access VA FileMan's internal data dictionaries. M-to-SQL vendors can use SQLI to map their SQL data dictionaries directly to VA FileMan data. By doing this they view and access VA FileMan data as native SQL tables.

### What is the Purpose of this Manual?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual is designed to help you, the M-to-SQL vendor, create and maintain an SQLI mapper utility. An SQLI mapper utility reads the projection of VA FileMan's data dictionaries provided by SQLI. It maps your M-to-SQL product's data dictionaries based on SQLI's projection so that your M-to-SQL product can directly access VA FileMan data as relational tables.
This manual may also be useful if you are providing technical support for an SQLI system; it can help provide an understanding of how SQLI works.

# Building an SQLI Mapper

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To map your M-to-SQL product's data dictionaries to directly access VA FileMan data, based on the information projected by SQLI, you will need to create an SQLI mapper utility. This SQLI mapper utility should read the published information on each VA FileMan file from the SQLI's projection. It should use this information to generate DDL commands (or use some similar method) that map your SQL data dictionaries directly to VA FileMan data.

![](di-21-38-vendor-guide-draft/009.png)

<span id="_Toc94346431" class="anchor"></span>Figure 2‑1: SQLI mapper utility diagram

### Information Provided by SQLI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI's projection of VA FileMan data dictionaries provides:

- A complete projection of VA FileMan files and fields as relational tables.
- Pre-defined SQL-compatible names for tables, columns, and keys.
- Global locations to retrieve data elements directly.
- Code to retrieve data elements through API calls.
- Code to convert retrieved data elements from internal FileMan format to base and external column formats.
- A standard set of strategies for VA FileMan field types whose projection in relational terms is non-trivial (pointer fields, variable pointer fields, word-processing fields, and subfiles).

This information is published in a way that is tailored to use by an M-to-SQL vendor. It relieves you from having to access VA FileMan's internal data dictionary structures to determine certain parameters that are not explicit in VA FileMan. Also, using SQLI should insulate your code from proposed changes in the VA FileMan data dictionary.

### Organization of SQLI Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI is implemented as a set of VA FileMan files within a single M global, with no multiples or word-processing fields.

The organization of the files mirrors SQL2 standard Data Definition Language (DDL) syntax. Every data structure in the main SQLI files reflects some portion of the DDL commands needed to create SQL data dictionaries for VA FileMan data (essentially, the CREATE TABLE command).

Additional syntax has been added to support the definition of M global structures, virtual columns, key and output formats and other objects outside the scope of the SQL standard.

### SQLI Entity-Relationship Diagram

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This diagram organizes the file entities in their importance to the operation of the SQLI package. It shows conceptual relationships between the files, but not a comprehensive view of the physical pointer relationships between files.

![](di-21-38-vendor-guide-draft/010.png)

<span id="_Toc94346432" class="anchor"></span>Figure 2‑2: SQLI entity-relationship diagram

### Guidelines for SQLI Mappers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### VA Programming Standards and Conventions

Be aware that your code will be running in VA production accounts along with VA code. Adherence to the VA Programming SAC (Standards and Conventions) is highly recommended. This includes guidelines about the setting and killing of variables, the ways that devices are used, and not interfering with the error trapping provided by VA's Kernel package.

Obtaining a formal namespace from the VA's DBA (Database Administrator) is also advised.

#### Populating the SQLI_KEY_WORD File

The SQLI_KEY_WORD file (#1.52101) stores any words that SQLI should not use for SQL entity names. At any given site, it may not be populated with any keywords at all. So you (the M-to-SQL vendor) should use SQLI's KW^DMSQD entry point to populate this SQLI_KEY_WORD file (#1.52101):

- Any keywords specific to your (vendor) M-to-SQL product.
- The standard set of reserved keywords for SQL as defined by the ANSI standard for SQL.
- The keywords for ODBC as defined by Microsoft.

Also, in your instructions to sites using your SQLI mapper, make sure that adding your keywords to the SQLI_KEY_WORD file (#1.52101) is done *prior* to the site generating their first SQLI projection.

#### Data Dictionary Synchronization

To aid sites with data dictionary synchronization, your SQLI mapper utility should provide entry points for the following functions:

- Remapping your SQL data dictionary for *all* tables projected by SQLI.
- Remapping your SQL data dictionary for *one* table projected by SQLI.

#### Kernel Compatibility

Besides conforming to the VA Programming SAC, be aware that sites will probably want to run your utilities as background tasks using TaskMan, a module of VA's Kernel package. Sites are likely to want to create a single "task" that calls your keyword utility, runs the VA SQLI projection, and then runs your SQLI mapper.

To be compatible with running as a background task in TaskMan, your keyword utility and SQLI mapper should:

- Not issue any READs or in any way make either entry point interactive. This allows the entry point to run in the background. If you need to ask questions, separate that section of code from the actual SQLI mapper code.
- Not issue USE commands. The "current device" is already opened and available when an entry point is run as a task in the Kernel environment. If you need to use USE commands (e.g., to write to a host file), make sure you store the value of the current device so you can return to it.
- For output, issue WRITE commands. Do *not* use escape sequences, however; any output should be able to print on a simple line printer.

|                                                                                                                |                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/011.png) | For more information on background tasks in the Kernel environment, please refer to the "TaskMan" section of the *Kernel Systems Manual*. |

# # Parsing the SQLI Projection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter gives examples of how to traverse SQLI's indexes and retrieve the information needed to map your SQL data dictionaries.

Retrieving the information stored in the SQLI files involves traversing their indexes and retrieving the field values stored in their indexes and in the entries themselves.

|                                                                                                                |                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/012.png) | Full descriptions of the SQLI file and index structures are contained in the "File References" chapter in this manual. You may also want to refer to Appendix A—Quick Reference Card in this manual. |

The global location of each SQLI file and its associated fields and indexes are stable, supported references. You can reference these locations directly.

### About the Examples in this Chapter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The specific approaches provided in this chapter are suggestions only, and do not cover all of the ways you can retrieve information from SQLI.

### Using the {B}, {E}, {I}, {K}, and {V} Placeholders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI provides M executable code and expressions in certain fields. This M code provided by SQLI can use the following placeholder symbols:

| Symbol      | Usage                                                             |
|-----------------|-----------------------------------------------------------------------|
| {B}         | Base value of a column—used for computation                           |
| {E}         | External value of a column—used for display                           |
| {I}         | Internal value of a VA FileMan field—used for storage                 |
| {K\[1..n\]} | Key value—{K} is the current key, {K1} is the first key, etc. |
| {V\[1..n\]} | Value—used for function arguments and output value                    |

<span id="_Toc94346433" class="anchor"></span>Table 3‑1: Placeholder symbols and usage

#### Field Value Placeholders: {I}, {B} and {E}

- The {I} placeholder is used to represent Internal values, that is, the VA FileMan internal value of a field.
- The {B} placeholder is used to represent Base values, that is, the base value of a column.
- The {E} placeholders is used to represent External values, that is, the externally formatted view of the field that a user should see.

#### Key Placeholders: {K1}, {K2}, etc.

These placeholders represent portions of the primary key for a table column, numbered corresponding to the P_SEQUENCE values of a primary key. They are used primarily in the C_FM_EXEC field of the SQLI_COLUMN file (#1.5217). Substitute the appropriate primary key values to assemble a global reference to retrieve a particular column value. For example:

^DMSQ("C",672,3) = S {V}=\$\$GET^DMSQU(9.4901,"{K3},{K2},{K1},",.03)

<span id="_Toc94346434" class="anchor"></span>Figure 3‑1: Key Placeholders: {K1}, {K2}, etc.

In this case, {K3} represents the value of the part of the primary key whose P_SEQUENCE is 3; {K2} represents the part of the primary key whose P_SEQUENCE is 2; and {K1} represents the part of the primary key whose P_SEQUENCE is 1. This call retrieves the value of a column from its corresponding VA FileMan field.

#### Return Value Placeholder: {V}

This placeholder is used to denote where to place a variable that should receive a return value. One example of where the {V} "value" placeholder is used is in the SQLI_COLUMN file (#1.5217), in M code provided by the C_FM_EXEC field. For example:

^DMSQ("C",485,3) = S {V}=\$\$GET^DMSQU(1.1,"{K1},",.04)

<span id="_Toc94346435" class="anchor"></span>Figure 3‑2: Return Value Placeholder: {V}

In this case, substitute the variable name you want the output of the \$\$GET function returned in, for the {V} placeholder, before executing the M code.

### Example File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Throughout this chapter, a simple VA FileMan file, DA RETURN CODES file, is projected by SQLI. Here is a condensed VA FileMan data dictionary listing of this file:

CONDENSED DATA DICTIONARY---DA RETURN CODES FILE (#3.22)

UCI: VAH,FLD VERSION: 8.0

STORED IN: ^%ZIS(3.22,

--------- -----------------------------------------------------------

FIELD FIELD

NUMBER NAME

.01 DA Return String (RF), \[0;1\]

2 Terminal Type String (RFX), \[0;2\]

3 DESCRIPTION (Multiple-3.223), \[1;0\]

.01 DESCRIPTION (WL), \[0;1\]

<span id="_Toc94346436" class="anchor"></span>Figure 3‑3: Sample condensed VA FileMan data dictionary (DD) listing of the DA RETURN CODES file

The following is a global map VA FileMan data dictionary (DD) listing of this file:

GLOBAL MAP DATA DICTIONARY \#3.22 -- DA RETURN CODES FILE

STORED IN ^%ZIS(3.22, (15 ENTRIES) SITE: KERNEL UCI: KRN,KDE

---------------------------------------------------------------------------

This file holds the translation between the ANSI DA return code and the name in the terminal type file that should be used.

CROSS REFERENCED BY: DA Return String(B), DA Return String(B1)

^%ZIS(3.22,D0,0)= (#.01) DA Return String \[1F\] ^ (#2) Terminal Type String

==\>\[2F\] ^

^%ZIS(3.22,D0,1,0)=^3.223^^ (#3) DESCRIPTION

^%ZIS(3.22,D0,1,D1,0)= (#.01) DESCRIPTION \[1W\] ^

<span id="_Toc94346437" class="anchor"></span>Figure 3‑4: Sample global map VA FileMan data dictionary (DD) listing of the DA RETURN CODES file

### Starting Point: SQLI_SCHEMA File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of SQLI maps all VA FileMan files to a single schema, SQLI. So for the time being, you can assume that all tables are projected within the same schema (SQLI). Therefore, your starting point when processing the information in SQLI should be the SQLI_TABLE file (#1.5215; *not* the SQLI_SCHEMA file \[#1.521\]).

In the future, however, SQLI may project tables in more than one schema. At that point in time, an index may be added on the T_SCHEMA field of the SQLI_TABLE file (#1.5215), such that you can loop through schemas, and within schemas process tables.

### Find the Projected Table for a File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Within a given schema, you CAN loop through each table and process the information for that table.

To find the SQLI_TABLE file (#1.5215) entry for a particular VA FileMan file, you can look up the file's number in the "C" cross-reference of the SQLI_TABLE file (#1.5215). For example, to determine the corresponding SQLI_TABLE file (#1.5215) entry for the DA RETURN CODES file (#3.22), do the following:

\> W \$O(^DMSQ("T","C",3.22,""))

97

<span id="_Toc94346438" class="anchor"></span>Figure 3‑5: Sample code to determine the corresponding SQLI_TABLE file for a particular VA FileMan file

Therefore the internal entry number (IEN) of the SQLI_TABLE file (#1.5215) entry for DA RETURN CODES is 97. That entry in the SQLI_TABLE file (#1.5215) looks like the following:

NUMBER: 97 T_NAME: DA_RETURN_CODES

T_SCHEMA: SQLI

T_COMMENT: This file holds the translation between the ANSI DA return c

T_VERSION_FM: 1 T_FILE: DA_RETURN_CODES

T_UPDATE: JUL 31, 1997 T_GLOBAL: ^%ZIS(3.22,{K})

<span id="_Toc94346439" class="anchor"></span>Figure 3‑6: Sample DA RETURN CODES file entry in the SQLI_TABLE file (#1.5215)

### Processing Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When processing a table, once you have the table's IEN in the SQLI_TABLE file (#1.5215), the next thing to do is loop through the set of table elements for that table.

One way to find the table elements for a given SQLI_TABLE file (#1.5215) entry is to look up that entry's IEN in the "D" index of the SQLI_TABLE_ELEMENT file (#1.5216), and find each matching table element:

S EL="" F S EL=\$O(^DMSQ("E","D",tableien,EL)) Q:EL'\]""

<span id="_Toc94346440" class="anchor"></span>Figure 3‑7: Sample code finding the table elements for a given table

However, using the "F" index of the SQLI_TABLE_ELEMENT file (#1.5216), you can see both how many and also what type of table elements were projected for a table.

For example, in the case of the DA_RETURN_CODES table (IEN \#97):

Global ^DMSQ("E","F",97

DMSQ("E","F",97

^DMSQ("E","F",97,"C",256) =

^DMSQ("E","F",97,"C",2273) =

^DMSQ("E","F",97,"C",2274) =

^DMSQ("E","F",97,"C",2275) =

^DMSQ("E","F",97,"P",255) =

Global ^

<span id="_Toc94346441" class="anchor"></span>Figure 3‑8: Sample showing how many and what types of table elements exist for a given table

This shows that five table elements (four columns and one primary key) are projected for the DA_RETURN_CODES table.

### About Table Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every entry in the SQLI_TABLE_ELEMENT file (#1.5216) is associated with at least one entry in the SQLI_COLUMN (#1.5217), SQLI_PRIMARY_KEY (#1.5218), or SQLI_FOREIGN_KEY file (#1.5219). The associated entries contain the details of each table element, and associate themselves with table elements by pointing to the SQLI_TABLE_ELEMENT file (#1.5216).

For columns, only a single column in the SQLI_COLUMN file (#1.5217) will point to any given column-type table element.

For primary keys however, one or more entries in the SQLI_PRIMARY_KEY file (#1.5218) will point to the single primary key table element for any given table. This is because some primary keys have many parts. Pointing to a single primary key table element is how these many parts in the SQLI_PRIMARY_KEY file (#1.5218) are organized into a single comprehensive primary key.

Likewise for foreign keys, one or more entries in the SQLI_FOREIGN_KEY file (#1.5219) will point to the single foreign key table element for any given foreign key.

### Processing Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following example (Figure 3‑9) looks at the column-type table element entries for the DA_RETURN_CODES table. These provide the relational specifications for each table element:

NUMBER: 256 E_NAME: DA_RETURN_CODES_ID

E_DOMAIN: INTEGER E_TABLE: DA_RETURN_CODES

E_TYPE: Column

E_COMMENT: Primary key \#1 of table DA_RETURN_CODES

NUMBER: 2273 E_NAME: DA_RETURN_STRING

E_DOMAIN: CHARACTER E_TABLE: DA_RETURN_CODES

E_TYPE: Column

E_COMMENT: This field holds the string returned from sending a ANSI DA to

NUMBER: 2274 E_NAME: TERMINAL_TYPE_STRING

E_DOMAIN: CHARACTER E_TABLE: DA_RETURN_CODES

E_TYPE: Column

E_COMMENT: This is the string that should be used in a lookup to the terminal type

NUMBER: 2275 E_NAME: DESCRIPTION

E_DOMAIN: WORD_PROCESSING E_TABLE: DA_RETURN_CODES

E_TYPE: Column

E_COMMENT: The description of the description field is that of holding the description

<span id="_Ref93978014" class="anchor"></span>Figure 3‑9: Sample column-type table element entries for the DA_RETURN_CODES table

### Find a Table Element's Column Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For table elements that correspond to columns, use the "B" index of the SQLI_COLUMN file (#1.5217) to find the corresponding column entry in SQLI.

For example, for the column-type table element entry \#2273, the corresponding column is as follows:

\> W \$O(^DMSQ("C","B",2273,""))

1734

<span id="_Toc94346443" class="anchor"></span>Figure 3‑10: Sample code to find corresponding columns by using table elements

This entry, in the SQLI_COLUMN file (#1.5217), looks like the following:

NUMBER: 1734 C_TABLE_ELEMENT: DA_RETURN_STRING

C_WIDTH: 70 C_FILE: 3.22

C_FIELD: .01 C_NOT_NULL: Required

C_SECURE: Not secure C_VIRTUAL: Base column

C_PARENT: DA_RETURN_CODES_ID C_PIECE: 1

C_GLOBAL: ,0)

<span id="_Toc94346444" class="anchor"></span>Figure 3‑11: Sample entry in the SQLI_COLUMN file

### IEN Columns

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI projects one internal entry number (IEN) column for every top-level VA FileMan table. This column is intended to be used by you to store the IEN of each record. This IEN is important for a number reasons, one of which is that SQLI projects the primary key of each table based on the IEN column. So you need provide IEN columns for each table. In the case of the DA_RETURN_CODES table, the IEN column is the DA_RETURN_CODES_ID column.

For subfiles, one IEN column is projected in SQLI for each of the subfile's parents. This allows the projected table to store the IEN for each "parent" file entry as these entries exist in VA FileMan. This allows end-users to reassemble the relationships in SQL for a subfile table that exist in VA FileMan.

### Find the Primary Key for a Given Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the "F" index in the SQLI_TABLE_ELEMENT file (#1.5216), and search for the single entry with a type of "P":

S PKEY=\$O(^DMSQ("E","F",tableien,"P",""))

<span id="_Toc94346445" class="anchor"></span>Figure 3‑12: Sample code searching for a primary key (type of "P") for a given table

This returns a single entry in that represents the primary key of the table in question. In the case of the DA_RETURN_CODES table, the primary key is as follows:

\> W \$O(^DMSQ("E","F",97,"P",""))

255

<span id="_Toc94346446" class="anchor"></span>Figure 3‑13: Sample code to obtain the primary key for the DA_RETURN_CODES table

There is only one entry in the SQLI_TABLE_ELEMENT file (#1.5216) for a table's primary key. The way a primary key is projected in SQLI is that one or more corresponding entries in the SQLI_PRIMARY_KEY file (#1.5218) contain the actual parts of the primary key. They all point back to the single entry in the SQLI_TABLE_ELEMENT file (#1.5216) to compose a single, combined primary key. Each SQLI_PRIMARY_KEY file (#1.5218) entry's P_SEQUENCE field identifies the order in which that part of the primary key should be assembled.

The following example (Figure 3‑14) looks at the primary key projected for the DA_RETURN_CODES table. Use the SQLI_PRIMARY_KEY file (#1.5218)'s "B" index to discover how many parts are in the DA RETURN CODES file's (#3.22) primary key, based on its primary key table element:

Global ^DMSQ("P","B",255

DMSQ("P","B",255

^DMSQ("P","B",255,159) =

Global ^

<span id="_Ref94060668" class="anchor"></span>Figure 3‑14: Sample showing the number of parts of a primary key for the DA RETURN CODES file

In this case, the primary key is a single-part key. That entry looks like the following:

NUMBER: 159 P_TBL_ELEMENT: DA_RETURN_CODES_PK

P_COLUMN: DA_RETURN_CODES_ID P_SEQUENCE: 1

P_START_AT: 0 P_END_IF: '{K}

<span id="_Toc94346448" class="anchor"></span>Figure 3‑15: Sample of a single-part key

Each part of the primary key, as stored in the SQLI_PRIMARY_KEY file (#1.5218), points to the column upon which that part of the primary key is based. In this case, this part of the primary key (which is the only part) is based on the IEN column for the table.

#### Primary Key for a Projected Subfile

The DA RETURN CODES file (#3.22) contains a word-processing field, which is stored like a subfile by VA FileMan. Therefore its primary key has more than one part.

If the IEN in the SQLI_TABLE file (#1.5215) for the DA_RET_CODES_DESCRIPTION file is 98, then the entry in the SQLI_TABLE_ELEMENT file (#1.5216) for its primary key can be obtained as follows:

\> W \$O(^DMSQ("E","F",98,"P",""))

257

<span id="_Toc94346449" class="anchor"></span>Figure 3‑16: Sample code for obtaining the primary key for the SQLI_TABLE_ELEMENT file

The matching entries in the SQLI_PRIMARY_KEY file (#1.5218) are as follows:

Global ^DMSQ("P","B",257

DMSQ("P","B",257

^DMSQ("P","B",257,160) =

^DMSQ("P","B",257,161) =

<span id="_Toc94346450" class="anchor"></span>Figure 3‑17: Sample entries in the SQLI_PRIMARY_KEY file (1 of 2)

These entries look like the following:

NUMBER: 160

P_TBL_ELEMENT: DA_RET_CODES_DESCRIPTION_PK

P_COLUMN: DA_RETURN_CODES_ID P_SEQUENCE: 1

P_START_AT: 0 P_END_IF: '{K}

NUMBER: 161

P_TBL_ELEMENT: DA_RET_CODES_DESCRIPTION_PK

P_COLUMN: DA_RET_CODES_DESCRIPTION_ID P_SEQUENCE: 2

P_START_AT: 0 P_END_IF: '{K}

<span id="_Toc94346451" class="anchor"></span>Figure 3‑18: Sample entries in the SQLI_PRIMARY_KEY file (2 of 2)

These are the two parts to the DA_RET_CODES_DESCRIPTION table's primary key.

P_COLUMN for sequence 1 of the primary key points to the IEN column in the subfile table that stores the IEN of what, in VA FileMan, would be the subfile's parent entry. P_COLUMN for sequence 2 of the primary key points to the IEN column in the subfile table that stores the IEN of what, in VA FileMan, would be the IEN of the subfile entry.

Therefore, the primary key for the subfile's table combines the IEN of entries in each VA FileMan file level above the subfile's table, plus the IEN column of the subfile's table itself.

#### \$ORDERING to Loop Through a File's Data Entries

The P_START_AT and P_ENDIF fields in the SQLI_PRIMARY_KEY file (#1.5218) provide the initial value for a \$ORDER loop through a file's actual data entries and the expression to complete the loop.

The following example (Figure 3‑19) assumes that the table only contains a single element in the primary key (i.e., the table is for a top-level VA FileMan file). The loop would need to be more complex to loop through entries for a subfile.

;IEN = internal entry number of record to retrieve

;PSTARTAT = P_START_AT value for table's single-part primary key.

;PENDIF = P_END_IF value for table's single-part primary key.

;DMG = global storage for entries in this table. It is assumed

; to be a top-level table, with a single-part primary key.

;

S IEN=PSTARTAT,EXIT=\$P(PENDIF,"{K}")\_"IEN"\_\$P(PENDIF,"{K}",2)

F S IEN=\$O(@(\$P(DMG,"{K}")\_IEN\_")")) D I @EXIT Q

.I @EXIT Q

.;code to retrieve entry would go here

.W !,IEN

<span id="_Ref94061017" class="anchor"></span>Figure 3‑19: Sample code for a simple loop of entries in a subfile for the primary key

### Assembling Record Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can assemble the global location of any record given the following pieces of information:

- Each primary key entry in the SQLI_PRIMARY_KEY file (#1.5218) for the table.
- For each primary key entry, the C_GLOBAL value of the corresponding column.
- The column values for each column upon which the primary key is based.

Combine in order of P_SEQUENCE the C_GLOBAL value for each column that is part of a table's primary key. You end up with a string that that is a full global reference, with placeholders for each IEN. For example:

^DPT({K},.373,{K})

<span id="_Toc94346453" class="anchor"></span>Figure 3‑20: Sample full global reference location of a record with placeholders for each IEN

The following sample routine loops through each column in a table's primary key in order of P_SEQUENCE, retrieves the C_GLOBAL value for each column, and assembles the global reference for file entries for that table:

; DMT: table number in question

; DMK: placeholder string

; DMEP: primary key element

; DM: primary key column sequence (P_SEQUENCE)

; DMC: column for a part of the primary key

; DMCG: C_GLOBAL value for column

; DMG: accumulated global root

;

S DMK="{K}",DMG=""

S DMEP=\$O(^DMSQ("E","F",DMT,"P",""))

S DM=0 F S DM=\$O(^DMSQ("P","C",DMEP,DM)) Q:DM="" D

. S DMS=DM,DMC=\$O(^DMSQ("P","C",DMEP,DM,""))

. S DMCG=^DMSQ("C",DMC,1),DMG=DMG_DMCG_DMK

S DMG=DMG\_")" W DMG

<span id="_Toc94346454" class="anchor"></span>Figure 3‑21: Sample routine that loops through each column in a table's primary key to assemble the global reference for file entries for that table

The string you generate will look exactly like the value in the SQLI_TABLE file (#1.5215)'s T_GLOBAL field.

To determine the storage location of a particular entry in that table, replace the Placeholders:{K}s with the value of each part of the primary key for the entry. In the above example, the first {K} would be replaced by the part of the subfile's primary key whose P_SEQUENCE is 1, and the second {K} with the part of subfile's primary key whose P_SEQUENCE is 2.

### Retrieving Column Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each VA FileMan field type except computed has a fixed global storage location within each corresponding VA FileMan entry. Appending the value in a column's C_GLOBAL field to the storage location of the record in question yields the node that the corresponding field is stored in.

- For fields using normal storage, SQLI provides the ^-delimited piece of the data node in the C_PIECE field.
- For fields using extract storage, SQLI provides the extract from and extract to positions for the data node in the C_EXTRACT_FROM and C_EXTRACT_THRU fields.

Data you retrieve from VA FileMan data globals is in internal VA FileMan format. Sometimes you can use this data without conversions of any kind. However:

- Domain conversions are provided when the internal VA FileMan format differs from the base column format (see the "Column Value Conversions" topic that follows).
- Output formats are provided for columns whose external format differs from the base column format (see the "Column Value Conversions" topic that follows).

Retrieving Column Values through a DBS Call

The SQLI_COLUMN file (#1.5217) provides code in the C_FM_EXEC field to retrieve the external field value a DBS call, for columns derived from the following VA FileMan field types:

- Computed
- Pointer
- Variable Pointer

This code is useful for resolving the external value for pointer field types. A pointer field in one file can point to a pointer field in another file and so forth, resulting a long pointer chain until you finally reach a non-pointer field to access the external value of the original pointer field.

Also, a DBS call is also the only way to retrieve the value for computed fields, which have no permanent storage. A value of 1 in the C_VIRTUAL field indicates which columns are based on computed fields. For such columns, use the M code in the C_FM_EXEC field to retrieve the computed field value.

### Column Value Conversions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI provides column conversions for some columns. Base-to-internal conversions are provided in the SQLI_DOMAIN file (#1.5212). Base-to-external conversions are provided in the SQLI_OUTPUT_FORMAT file (#1.5214).

#### Domain Conversions (Base to Internal)

Some domains created by SQLI provide conversions between VA FileMan internal {I} format to SQL base {B} data format. No conversion is provided when the SQL base and VA FileMan internal form for a column are the same.

Specifically, for columns whose domains are date-time valued (FM_DATE and FM_MOMENT), the domains in the SQLI_DOMAIN file (#1.5212) provide conversions in the DM_BASE_EXEC and DM_INT_EXEC fields. Also, the FM_BOOLEAN domain provides conversions in the DM_INT_EXPR and DM_BASE_EXPR fields.

You should always check the SQLI_DOMAIN file (#1.5212) when processing columns to determine if a domain conversion is provided.

#### Output Format Conversions (Base to External)

Given the base column value derived from a VA FileMan field, entries in the SQLI_OUTPUT_FORMAT file (#1.5214) provide M code to generate the external value to present to the end-user for the column in question.

Columns do *not* need an output format if the *base* column data format is the same as its *external* data format. Output formats are therefore provided only for columns derived from Pointer and Set of Codes VA FileMan field types.

Output formats that affect a column can be designated for individual columns, for all columns in a given SQLI_DOMAIN file (#1.5212) domain, and for all columns whose domain is a given SQLI_DATA_TYPE file (#1.5211) data type.

The order of precedence for which output format to use, if there is more than one, is as follows:

1.  C_OUTPUT_FORMAT in the column's SQLI_COLUMN file (#1.5217) entry
2.  DM_OUTPUT_FORMAT in the associated domain's SQLI_DOMAIN file (#1.5212) entry
3.  D_OUTPUT_FORMAT in the associated data type's SQLI_DATA_TYPE file (#1.5211) entry

You should always check the SQLI_OUTPUT_FORMAT file (#1.5214) when processing columns to determine if an output format conversion is provided.

### Foreign Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Your M-to-SQL product may or may not support foreign keys. If it does, you can use the foreign keys projected by SQLI to make it easier for the end-user to recreate certain relationships that are explicit in the original VA FileMan data.

SQLI projects foreign keys in the following standard situations:

| Situation                                        | Foreign Key(s) Provided                                                                                                                                                |
|------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Column based on pointer field                        | In the table containing the pointer field column, one for the pointed-to file, named *pointer_field_name*\_FK. The join is from the pointer field to the pointed-to table. |
| Table projected for subfile or word-processing field | In the subfile or word-processing field's table, one for each parent table, each named *parent_table*\_PFK. Each join links the subfile to its original VA FileMan parent. |

<span id="_Toc94346455" class="anchor"></span>Table 3‑2: Standard situations where SQLI provides foreign keys

One advantage of foreign key syntax over joins is that rows are not lost when the value of a join column is null. For example, foreign key syntax (e.g., NEW_PERSON_FK@NAME) can be used in the select clause to obtain the value of the column NAME from the NEW_PERSON table, rather than doing a join to NEW_PERSON in a where clause. A row is returned even if the NAME column of the corresponding row in the NEW_PERSON file (#200) is null.

To find all of the foreign keys for a given table, use the "F" index of the SQLI_TABLE_ELEMENT file (#1.5216), and search for all entries with a type of "F":

S COL="" F S COL=\$O(^DMSQ("E","F",tableien,"F",COL)) Q:COL'\]""

<span id="_Toc94346456" class="anchor"></span>Figure 3‑22: Sample code finding all foreign keys for a given table

Pointer Fields

In the case of foreign keys set up to mimic the relationship provided by *pointer* fields, the name of the foreign key is the pointer field's name followed by "\_FK". For example:

Pointer field column: TEMPORARY_STATE

Pointer field from table: NEW_PERSON

Pointer field to table: STATE

Foreign key name: TEMPORARY_STATE_FK

Subfiles and Parent Foreign Keys

Tables derived from *subfiles*, including those for word-processing fields, have foreign keys projected by SQLI to each table that is a higher file level (up to the top-level file that is the highest parent of the subfile). These foreign keys within a subfile's table are named with the pointed-to table name followed by "\_PFK" (parent foreign key). For example:

Subfile table: NEW_PERSON_ALERT_DATE_TIME

Parent table: NEW_PERSON

Foreign key name: NEW_PERSON_PFK

Every foreign key to a given table has the same domain as the primary key of that table. While not supported by SQL, this convention makes entity relationships more explicit and should help vendors maintain referential integrity constraints during mapping.

# VA FileMan and SQL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA FileMan, SQL, and the Relational Model

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the equivalent terminology between VA FileMan (projected as a relational database), SQL, and the Relational Model:

| VA FileMan   | SQL | Relational Model |
|------------------|---------|----------------------|
| File or Multiple | Table   | Relation             |
| Field            | Column  | Attribute            |
| Label            | Name    | Name                 |
| Field Type       | Domain  | Domain               |
| Record           | Row     | Tuple                |

<span id="_Toc94346457" class="anchor"></span>Table 4‑1: Terminology between VA FileMan, SQL, and the Relational Model

### VA FileMan File Definition Structures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The entities that together form a VA FileMan file definition (data dictionary) are contained at the following locations:

| Data Dictionary Element | Location                             |
|-----------------------------|------------------------------------------|
| Dictionary of Files         | ^DIC(Filenumber,                         |
| Attribute Dictionary        | ^DD(Filenumber,                          |
| Field Definition Nodes      | ^DD(Filenumber, fieldnumber,             |
| File Header                 | Zero subscript of the file's global root |

<span id="_Toc94346458" class="anchor"></span>Table 4‑2: VA FileMan DD elements and their locations

You should not need to access any of this information directly. All relevant information about file definitions needed for projecting VA FileMan data is published by SQLI.

|                                                                                                                |                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/013.png) | For more information on file definition structures, please refer to the "Global File Structure" chapter in the *VA FileMan Programmer Manual*. |

### VA FileMan Field Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists each of the nine possible VA FileMan field types.

|                                                                                                                |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/014.png) | More information on the specifics of each field type can be found in the *VA FileMan Advanced User Manual*. |

| Field Type       | Description                                                                                                                                  |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Computed         | Value is computed on-the-fly (no permanent storage)                                                                                              |
| Date             | Time can be mandatory, optional, or not allowed                                                                                                  |
| Free Text        | Free Text, up to 250 characters in length                                                                                                        |
| MUMPS            | Contains MUMPS code                                                                                                                              |
| Numeric          | Can be integer or decimal-valued                                                                                                                 |
| Pointer          | Points to .01 field of an entry in another file (value is IEN of pointed-to entry)                                                               |
| Set of codes     | Restricts a user to just a few possible values. Codes have an internal and external format.                                                      |
| Variable Pointer | Like a pointer field, except that the pointer may be to an entry in one of several files.                                                        |
| Word-processing  | This is a memo-type field, with no size limit, implemented in a subfile-like structure. It stores multiple lines of text, and has no size limit. |

<span id="_Toc94346459" class="anchor"></span>Table 4‑3: VA FileMan field types

### VA FileMan Subfiles (Multiples)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan entries can contain "multiple-valued" fields, known as multiples or subfiles. A subfile is essentially a file-within-a-file. For example, a PATIENT file (#2) entry might have an "Appointments" multiple-valued field. This file-within-a-file can contain one or more entries for the patient's appointments. Multiples can themselves contain multiple-valued fields.

Viewed from within VA FileMan, multiples are hierarchical. Data storage for an entry's multiple field is contained descendant from the same subscript as data for the entry itself. However, it is possible to conceptually "flatten" multiples and project them as if they are standalone tables, especially since they are defined in a similar fashion to standalone files in VA FileMan's attribute dictionary. SQLI handles multiples in this fashion.

### Mapping VA FileMan Fields to SQL Data Types

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan field types do *not* correspond exactly to the SQL concept of data types, but are projected in ways that ultimately result in categorization by data type.

You can determine the original VA FileMan field type of a column through the associated domain's DM_FILEMAN_FIELD_TYPE field. This is a set of codes field, the value of which represents the original VA FileMan field type of the column (and domain) in question.

#### IEN Columns

SQLI provides a column for the original IEN of each VA FileMan record. The name for the IEN column is based on the table name followed by "\_ID". For example, the PATIENT file (#2) has a single column primary key, PATIENT_ID.

#### Computed Fields

Projection of Computed fields is complicated mildly by the fact that SQL DDL syntax supports only base data, while Data Manipulation Language supports expressions. Columns for VA FileMan computed fields are flagged with the C_VIRTUAL field in the SQLI_COLUMN file (#1.5217). You can retrieve their computed value with the code in each column's C_FM_EXEC field, which uses DBS calls.

A number of different computed field return value types are possible: Multiline, Boolean-valued, Free text, Date, and Numeric.

|                                                                                                                |                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/015.png) | Multiline computed fields are *not* supported by the DBS or by SQLI; a character error message is returned by the SQLI-provided M code as the value for a multiline computed field. |

#### Date Fields

Code is provided in the two VA FileMan-specific date domains, FM_DATE and FM_MOMENT, to convert between internal VA FileMan formatted dates and date/times, and column "base format" \$HOROLOG dates and date/times. The code is in the DM_INT_EXEC and DM_BASE_EXEC fields.

#### Free Text, Numeric, and MUMPS Fields

No conversion is needed for the Free Text, Numeric, or MUMPS field types; internal, base, and external formats are identical.

#### Pointer Fields

The Pointer field type conforms to SQL's Foreign Key constraint, and is projected as such in SQLI. VA FileMan, however, allows direct reference to a pointer field, returning the text value of the primary identifier of the row reached by recursively following the pointer chain until the identifier is not itself a pointer. This usage is projected in SQLI by giving pointers an integer domain and an output format that uses the DBS to return the resolved value. For example:

OF_NAME: FOREIGN_FORMAT_PTOF OF_DATA_TYPE: INTEGER

OF_COMMENT: Output format for pointer to FOREIGN_FORMAT

OF_EXT_EXPR: \$S('{B}:"",1:\$\$GET^DMSQU(.44,{B}\_",",.01))

<span id="_Toc94346460" class="anchor"></span>Figure 4‑1: VistA Pointer field types

Substitute the base value of the column for {B}, and the expression returns the resolved external text value of the pointer field.

#### Set of Codes Fields

An output format is provided for *each* distinct Set of Codes "set" to display the long form of the base column value (which should be the code only). These output format entries are pointed to from SQLI_COLUMN file (#1.5217) entries. For example:

OF_NAME: M_MERGE_O_OVERWRITE OF_DATA_TYPE: CHARACTER

OF_COMMENT: Set output format

OF_EXT_EXPR: \$P(\$P(";m:MERGE;o:OVERWRITE;",";"\_{B}\_":",2),";")

<span id="_Toc94346461" class="anchor"></span>Figure 4‑2: VistA Set of Code field types

Substitute the base value of the field (which the same as its VA FileMan internal form for Set of Codes field types) for {B}, and the expression returns the external value of the code.

#### Variable Pointer Fields

The Variable Pointer data type is not relationally atomic, the only true violation of the relational model in VA FileMan. In SQLI, a column for a variable pointer field has a character domain, and an output format that returns the VA FileMan display value from whichever of the VA FileMan files each entry actually points to.

Summary: How SQLI Translates VA FileMan Field Types into SQL Columns

<table style="width:100%;">
<colgroup>
<col style="width: 15%" />
<col style="width: 22%" />
<col style="width: 35%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>FM Field Type</strong></th>
<th><strong>FM Internal Format</strong></th>
<th><strong>SQL Domain, Data Type, Base Format</strong></th>
<th><strong>SQL External Format</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td rowspan="5"><strong>Computed</strong></td>
<td>Date valued:</td>
<td>CHARACTER domain, data type.</td>
<td></td>
</tr>
<tr class="even">
<td>Multiline-valued:</td>
<td>Base format: same as FM internal format.</td>
<td>Same as base format.</td>
</tr>
<tr class="odd">
<td>Free Text:</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Boolean-valued:</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>Numeric-valued:</td>
<td>See Numeric FM Field Type.</td>
<td></td>
</tr>
<tr class="even">
<td><strong>Date</strong></td>
<td><p>yyymmdd.hhmmss<br />
<br />
yyy: #yrs. since 1700</p>
<p>mm: month (00-12)</p>
<p>dd: day (00-31)</p>
<p>hh: hour (00-23)</p>
<p>mm: minute (01-59)</p>
<p>ss: seconds (01-59)</p></td>
<td><p>Date only: FM_DATE domain; DATE data type.</p>
<p>Date w/Time optional: FM_MOMENT domain, MOMENT data type.</p>
<p>Date w/Time required: FM_DATE_TIME domain, MOMENT data type.</p>
<p>Base format is date/time in $HOROLOG format.</p></td>
<td><p>User-friendly version of date. For example:</p>
<p>JUL 31, 1997</p></td>
</tr>
<tr class="odd">
<td><strong>Free Text</strong></td>
<td>Free text.</td>
<td><p>CHARACTER domain, data type.</p>
<p>Base format: same as FM internal format.</p></td>
<td>Same as base format.</td>
</tr>
<tr class="even">
<td><strong>MUMPS</strong></td>
<td>Free text.</td>
<td><p>FM_MUMPS domain, CHARACTER data type.</p>
<p>Base format: same as FM internal format.</p></td>
<td>Same as base format.</td>
</tr>
<tr class="odd">
<td><strong>Numeric</strong></td>
<td>Numeric.</td>
<td><p>NUMERIC or INTEGER domain and data type.</p>
<p>Base format: same as FM internal format.</p></td>
<td>Same as base format.</td>
</tr>
<tr class="even">
<td><strong>Pointer</strong></td>
<td>Integer IEN of the pointed-to entry.</td>
<td><p>POINTER domain.</p>
<p>INTEGER data type.</p></td>
<td>External .01 field value of pointed-to entry (pointer chain must be followed) (provided by an output format).</td>
</tr>
<tr class="odd">
<td><strong>Set of Codes</strong></td>
<td>Internally stored "code", typically shorter than the external form.</td>
<td><p>SET_OF_CODES domain; CHARACTER data type.</p>
<p>Base format: same as FM internal format.</p></td>
<td>External value that the code stands for (provided by an output format).</td>
</tr>
<tr class="even">
<td><strong>Variable Pointer</strong></td>
<td><p>IEN;global file root</p>
<p>For example:</p>
<p>4;DIC(42,</p></td>
<td><p>VARIABLE_POINTER domain; CHARACTER data type.</p>
<p>Base format: External .01 field value of pointed-to entry at end of pointer chain.</p></td>
<td>External .01 field value of pointed-to entry (pointer chain must be followed) (provided by an output format).</td>
</tr>
<tr class="odd">
<td><strong>Word-processing</strong></td>
<td>Memo-type field, no size limit, stored in a subfile.</td>
<td><p>WORD_PROCESSING domain and data type.</p>
<p>Base format: A set of rows in a table, one row per textline.</p></td>
<td>Optionally make available as a memo field; otherwise, same as base format.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346462" class="anchor"></span>Table 4‑4: SQLI translation from VA FileMan field types to SQL columns

#### Word-processing Fields

VA FileMan Word-processing fields are stored similarly to multiples, and are projected by SQLI in two ways:

- As a standalone table (each line of text is one entry in the table).
- As columns for vendors who support a HUGE_CHARACTER or MEMO data type.

If you have an appropriate MEMO-like data type, you could place word-processing text into a column of this data type, and decide whether or not to make the word-processing tables available to your users.

The main problem with memo data types is that they usually come with a size constraint, and consume additional resources when you increase the maximum size. VA FileMan word-processing fields, on the other hand, are unlimited in size. Thus, you could choose a default size such as 32K for your memo-type columns. In case truncation occurs, you should return an error for word-processing fields whose contents exceed your default size.

### VA FileMan Indexes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan regular-type cross references are projected by SQLI as tables. Other types of cross-references (Trigger, KWIC, MUMPS, Mnemonic, Soundex, and Bulletin) are not projected. Cross-references are primarily for vendor optimization, and should not be made available as tables to end-users.

Tables derived from cross-references use names based on the name of the indexed table followed by "\_Xs\_" where "s" is the index subscript, followed by the name of the column indexed (PATIENT_XB_NAME, PATIENT_XSSN_SOCIAL_SEC_NUMBER, etc.) Compression is used such that all names are no longer than 30 characters. For example:

PATIENT_CANCER_STATUS_CODE (*table name*)

PATIENT_CANC_STAT_CODE_XB_NAME (*"B" index table name - compressed*)

<span id="_Toc94346463" class="anchor"></span>Figure 4‑3: Sample naming convention of tables derived from cross-reference

A table is projected for a cross-reference if its T_MASTER_TABLE field is populated. For multiples, there are two kinds of references, both of which are projected as tables by SQLI: regular and whole-file cross-references.

The following example shows the various parts of the table projected for a simple cross-reference for a top level file (the PATIENT file \[#2\]):

NUMBER: 4650 T_NAME: PATIENT_XB_NAME

T_SCHEMA: SQLI T_COMMENT: Index of PATIENT by NAME

T_MASTER_TABLE: PATIENT T_VERSION_FM: 1

T_UPDATE: MAY 05, 1997 T_GLOBAL: ^DPT("B",{K},{K})

<span id="_Toc94346464" class="anchor"></span>Figure 4‑4: Table projected for "B" index of the PATIENT file (#2)

\>D ^%G

Global ^DMSQ("E","F",4650

DMSQ("E","F",4650

^DMSQ("E","F",4650,"C",53797) =

^DMSQ("E","F",4650,"C",53798) =

^DMSQ("E","F",4650,"P",53796) =

NUMBER: 53796 E_NAME: PATIENT_XB_NAME_PK

E_DOMAIN: PATIENT_XB_NAME_ID E_TABLE: PATIENT_XB_NAME

E_TYPE: Primary key

E_COMMENT: Primary key header for PATIENT_XB_NAME

NUMBER: 53797 E_NAME: NAME

E_DOMAIN: CHARACTER E_TABLE: PATIENT_XB_NAME

E_TYPE: Column

E_COMMENT: Index Primary Key \#1 for PATIENT_XB_NAME.NAME

NUMBER: 53798 E_NAME: PATIENT_ID

E_DOMAIN: INTEGER E_TABLE: PATIENT_XB_NAME

E_TYPE: Column

E_COMMENT: Index Primary Key \#2 for PATIENT_XB_NAME.PATIENT_ID

<span id="_Toc94346465" class="anchor"></span>Figure 4‑5: Table elements projected for PATIENT_XB_NAME

\>D ^%G

Global ^DMSQ("C","B",53797:53798

DMSQ("C","B",53797:53798

^DMSQ("C","B",53797,43834) =

^DMSQ("C","B",53798,43835) =

Global ^

NUMBER: 43834 C_TABLE_ELEMENT: NAME

C_GLOBAL: ^DPT("B",

NUMBER: 43835 C_TABLE_ELEMENT: PATIENT_ID

C_PARENT: NAME C_GLOBAL: ,

<span id="_Toc94346466" class="anchor"></span>Figure 4‑6: Columns projected for PATIENT_XB_NAME

\>D ^%G

Global ^DMSQ("P","C",53796

DMSQ("P","C",53796

^DMSQ("P","C",53796,1,8529) =

^DMSQ("P","C",53796,2,8530) =

NUMBER: 8429 P_TBL_ELEMENT: PATIENT_XB_NAME_PK

P_COLUMN: NAME P_SEQUENCE: 1

NUMBER: 8530 P_TBL_ELEMENT: PATIENT_XB_NAME_PK

P_COLUMN: PATIENT_ID P_SEQUENCE: 2

<span id="_Toc94346467" class="anchor"></span>Figure 4‑7: Primary key projected for PATIENT_XB_NAME

![](di-21-38-vendor-guide-draft/016.png)

<span id="_Toc94346468" class="anchor"></span>Figure 4‑8: Partial index listing

In the example above, the primary key is a two-part key, based on two columns: the "NAME" and "PATIENT_ID" columns. The global path to "entries" in the index table is *^DPT("B",{K},{K})*.

|                                                                                                                |                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/017.png) | One part of the key is not IEN-based, but instead is the indexed value. |

For indexes whose indexed value exceeds 30 characters, a "key format" is provided that provides the transformation between the actual indexed column's field values, and the truncated-to-30 character version of the column values that appears in the index. For more information, see the description of the SQLI_KEY_FORMAT file (#1.5213).

# File References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the descriptions of SQLI files that follow, each file description contains:

- Global root of the SQLI file.
- VA FileMan data dictionary number of the SQLI file.
- All available cross references for traversing the SQLI file's entries.
- A listing of each field, with the field name, type, location, and description.
- Additional information about the purpose of the file and its fields.
- A description of the format of any code fragments supplied by this file.

|                                                                                                                |                                                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/018.png) | In the tables on the following pages, SQLI field names followed by an asterisk (e.g., "S_NAME\*") are never NULL when the SQLI files are populated by SQLI. This documentation convention is used to indicate that such fields are key fields for each SQLI file. |

### SQLI_SCHEMA File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("S",

VA FileMan Number: 1.521

Indexes:

B: ^DMSQ("S","B",\$E(S_NAME,1,30),ien)=""

<span id="_Toc94346469" class="anchor"></span>Figure 5‑1: SQLI_SCHEMA file—Index

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>S_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Schema name (valid SQL identifier).</td>
</tr>
<tr class="even">
<td>S_SECURITY</td>
<td>Free Text</td>
<td>1;1</td>
<td>Not yet implemented; for future use. M routine to check security privileges on a particular schema.</td>
</tr>
<tr class="odd">
<td>S_DESCRIPTION</td>
<td>Free Text</td>
<td>0;2</td>
<td>A short description of the mapped application group.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346470" class="anchor"></span>Table 5‑1: SQLI_SCHEMA file—Fields

Purpose: The SQLI_SCHEMA file (#1.521) provides a place for SQLI to associate tables with a schema name. This allows each VA FileMan file to be automatically mapped to a schema.

Currently, SQLI automatically projects all tables as part of one schema, "SQLI". SQLI does not provide facilities for dividing VA FileMan files into separate schemas.

### SQLI_KEY_WORD File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("K",

VA FileMan Number: 1.52101

Indexes:

B: ^DMSQ("K","B",\$E(KEY_WORD,1,30),ien)=""

<span id="_Toc94346471" class="anchor"></span>Figure 5‑2: SQLI_KEY_WORD file—Index

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KEY_WORD</td>
<td>Free Text</td>
<td>0;1</td>
<td>SQL, ODBC, or vendor keyword to reserve.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346472" class="anchor"></span>Table 5‑2: SQLI_KEY_WORD file—Field

Purpose: This file is the collection point for keywords that should not be used for SQL entity names. You can add any keywords specific to your own SQL implementation through the KW^DMSQD entry point.

The SQLI_KEY_WORD file (#1.52101) may *not* be populated with any key words at all. So you (the M-to-SQL vendor) should use the KW^DMSQD entry point to populate this SQLI_KEY_WORD file (#1.52101):

- Any keywords specific to your (vendor) M-to-SQL product
- The standard set of reserved keywords for SQL as defined by the ANSI standard for SQL
- The keywords for ODBC as defined by Microsoft

In your instructions to sites using your SQLI mapper, make sure that adding your keywords to the SQLI_KEY_WORD file (#1.52101) is done *prior* to the site generating their first SQLI projection.

### SQLI_DATA_TYPE File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("DT",

VA FileMan Number: 1.5211

Indexes:

B: ^DMSQ("DT","B",\$E(D_NAME,1,30),ien)=""

<span id="_Toc94346473" class="anchor"></span>Figure 5‑3: SQLI_DATA_TYPE file—Indexes

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>D_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Data type name (should be a valid SQL identifier).</td>
</tr>
<tr class="even">
<td>D_COMMENT</td>
<td>Free Text</td>
<td>0;2</td>
<td>Brief description.</td>
</tr>
<tr class="odd">
<td>D_OUTPUT_STRATEGY</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 1,</p>
<p>1-245</p></td>
<td>Not yet implemented; for future use. Intended for future data types (pictures, formatted word-processing, etc.) that VA FileMan might support in the future.</td>
</tr>
<tr class="even">
<td>D_OUTPUT_FORMAT</td>
<td>Pointer to SQLI_<br />
OUTPUT_<br />
FORMAT</td>
<td>0;3</td>
<td>Not implemented in the first version of SQLI. Pointer to an Output Format to use for columns whose domains point to this data type.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346474" class="anchor"></span>Table 5‑3: SQLI_DATA_TYPE file—Fields

Purpose: The SQLI_DATA_TYPE file (#1.5211) is a simple list of SQL standard data types (BOOLEAN, CHARACTER, DATE, INTEGER, MEMO, MOMENT, NUMERIC, TIME) with one additional type, PRIMARY_KEY. This allows the custom VA FileMan domains in the SQLI_DOMAIN file (#1.5212) to always be associated with a specific base SQL data type.

SQL data types determine the SQL rules for comparing values from different domains, and the operators that may be used on them. So each domain in the SQLI_DOMAIN file (#1.5212) has an explicit SQL data type that SQL vendors should use.

|                                                                                                                |                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/019.png) | The PRIMARY_KEY data type (and domain) is unique to SQLI. It is used to relate primary keys to foreign keys unambiguously. |

### SQLI_DOMAIN File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("DM",

VA FileMan Number: 1.5212

Indexes:

B: ^DMSQ("DM","B",\$E(DM_NAME,1,30),ien)=""

C: ^DMSQ("DM","C",\$E(DM_TABLE,1,30),ien)=""

D: ^DMSQ("DM","D",\$E(DM_FILEMAN_FIELD_TYPE,1,30),ien)=""

E: ^DMSQ("DM","E",\$E(DM_DATA_TYPE,1,30),ien)=""

<span id="_Toc94346475" class="anchor"></span>Figure 5‑4: SQLI_DOMAIN file—Indexes

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DM_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Domain name (valid SQL identifier).</td>
</tr>
<tr class="even">
<td>DM_DATA_TYPE*</td>
<td>Pointer to SQLI_DATA_<br />
TYPE</td>
<td>0;2</td>
<td>Pointer to the SQL data type to use for this domain.</td>
</tr>
<tr class="odd">
<td>DM_COMMENT</td>
<td>Free Text</td>
<td>0;3</td>
<td>Brief description.</td>
</tr>
<tr class="even">
<td>DM_TABLE</td>
<td>Pointer to SQLI_TABLE</td>
<td>0;4</td>
<td>If this domain is for a primary or foreign key, points to the table of the primary key.</td>
</tr>
<tr class="odd">
<td>DM_WIDTH</td>
<td>Numeric</td>
<td>0;5</td>
<td>Maximum width of external value.</td>
</tr>
<tr class="even">
<td>DM_SCALE</td>
<td>Numeric</td>
<td>0;6</td>
<td>Default number of decimal places, for NUMERIC data types only.</td>
</tr>
<tr class="odd">
<td>DM_OUTPUT_FORMAT</td>
<td>Pointer to SQLI_OUTPUT_FORMAT</td>
<td>0;7</td>
<td>Not implemented in the first version of SQLI. Pointer to an Output Format to use for columns that use this domain.</td>
</tr>
<tr class="even">
<td>DM_INT_EXPR</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 1,</p>
<p>1-245</p></td>
<td>M expression to convert base value to internal (VA FileMan) format.</td>
</tr>
<tr class="odd">
<td>DM_INT_EXEC</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 2,</p>
<p>1-245</p></td>
<td>M execute statement to convert base value to internal (VA FileMan) format.</td>
</tr>
<tr class="even">
<td>DM_BASE_EXPR</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 3,</p>
<p>1-245</p></td>
<td>M expression to convert internal (VA FileMan) value to base format.</td>
</tr>
<tr class="odd">
<td>DM_BASE_EXEC</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 4,</p>
<p>1-245</p></td>
<td>M execute statement to convert internal (VA FileMan) value to base format.</td>
</tr>
<tr class="even">
<td>DM_FILEMAN_FIELD_<br />
TYPE</td>
<td>Set of codes</td>
<td>0;8</td>
<td><blockquote>
<p>'F' FOR FREE TEXT</p>
<p>'N' FOR NUMERIC</p>
<p>'P' FOR POINTER</p>
<p>'D' FOR DATE</p>
<p>'W' FOR WORD-PROCESSING</p>
<p>'K' FOR MUMPS</p>
<p>'C' FOR CALCULATED</p>
<p>'B' FOR BOOLEAN</p>
<p>'S' FOR SET</p>
<p>'V' FOR VARIABLE POINTER</p>
</blockquote>
<p>Original VA FileMan field type for all elements using this domain, for domains derived from VA FileMan fields. Boolean means Boolean Computed.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc94346476" class="anchor"></span>Table 5‑4: SQLI_DOMAIN file—Fields

Purpose: Each entry in the SQLI_DOMAIN file (#1.5212) is a custom domain, which defines a set of values from which all objects of this domain must be drawn. In SQLI, all table elements (columns, primary keys, and foreign keys) have a domain that restricts them to their domain set.

Each domain points to a data type (from the SQLI_DATA_TYPE file \[#1.5211\]) which should be used as the SQL data type for this domain. Other fields in the SQLI_DOMAIN file (#1.5212) also constrain the set of possible values for the domain. For more information see Mapping VA FileMan Fields to SQL Data Types earlier in this chapter.

#### Code Fragment Formats

DM_INT_EXPR: \$S({B}="":0,1:{B})  
*(provide {B}, evaluates to internal FileMan form)*

DM_BASE_EXPR: \$S({I}:{I},1:"")  
(*provide {I}, evaluates to base form)*

DM_INT_EXEC: S %H={B} D YMD^%DTC S {I}=X  
*(provide {B}, get {I} back)*

DM_BASE_EXEC: N %H,X S X={I} D H^%DTC S {B}=%H  
*(provide {I}, get {B} back)*

### SQLI_KEY_FORMAT File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("KF",

VA FileMan Number: 1.5213

Indexes:

B: ^DMSQ("KF","B",\$E(KF_NAME,1,30),ien)=""

C: ^DMSQ("KF","C",\$E(KF_DATA_TYPE,1,30),ien)=""

<span id="_Toc94346477" class="anchor"></span>Figure 5‑5: SQLI_KEY_FORMAT file—Indexes

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 20%" />
<col style="width: 11%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KF_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Key format name.</td>
</tr>
<tr class="even">
<td>KF_DATA_TYPE*</td>
<td>Pointer to SQLI_DATA_TYPE</td>
<td>0;2</td>
<td>Pointer to data type used by associated primary key (should always point to PRIMARY_KEY data type).</td>
</tr>
<tr class="odd">
<td>KF_COMMENT</td>
<td>Free Text</td>
<td>0;3</td>
<td>Brief description.</td>
</tr>
<tr class="even">
<td>KF_INT_EXPR</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 1,</p>
<p>1-245</p></td>
<td>M expression to convert internal value <strong>{I}</strong> of indexed field to index primary key value <strong>{K}</strong>.</td>
</tr>
<tr class="odd">
<td>KF_INT_EXEC</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 2,</p>
<p>1-245</p></td>
<td>M executable code to set internal value <strong>{I}</strong> of indexed field to index primary key value <strong>{K}</strong>.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346478" class="anchor"></span>Table 5‑5: SQLI_KEY_FORMAT file—Fields

Purpose: Use the conversions provided in the SQLI_KEY_FORMAT file (#1.5213) to translate between a column's value and the part of a primary key that uses that column. In most cases, a conversion from column value to key value is not needed.

Currently, the main situation in which a conversion is provided is for the VA FileMan indexes that are projected as tables. The index subscript is considered part of the primary key of the projected table for an index. Currently, the (regular) index subscript for a VA FileMan file is based on the field value, but is subject to truncation to 30 characters. So the value of the part of the key based on a column could differ from the value of the column itself. A standard key format is supplied and linked to all parts of primary keys that use index subscripts, whose indexed fields' maximum length exceeds 30 characters.

Code Fragment Formats

KF_INT_EXPR: \$E({I},1,30)  
*(provide {I}, key is returned)*

KF_INT_EXEC: S {K}=\$E({I},1,30)  
*(provide {I}, get {K} back)*

### SQLI_OUTPUT_FORMAT File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("OF",

VA FileMan Number: 1.5214

Indexes:

B: ^DMSQ("OF","B",\$E(OF_NAME,1,30),ien)=""

<span id="_Toc94346479" class="anchor"></span>Figure 5‑6: SQLI_OUTPUT_FORMAT file—Index

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OF_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Output format name.</td>
</tr>
<tr class="even">
<td>OF_DATA_TYPE*</td>
<td>Pointer to SQLI_DATA_<br />
TYPE</td>
<td>0;2</td>
<td>Pointer to the data type for which this output format applies.</td>
</tr>
<tr class="odd">
<td>OF_COMMENT</td>
<td>Free Text</td>
<td>0;3</td>
<td>Brief description.</td>
</tr>
<tr class="even">
<td>OF_EXT_EXPR</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 1,</p>
<p>1-245</p></td>
<td>M expression to convert base value to external value.</td>
</tr>
<tr class="odd">
<td>OF_EXT_EXEC</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>Node 2,</p>
<p>1-245</p></td>
<td>Will not be implemented for the first version of SQLI (patch DI*21*38). M executable code to convert base value to external value.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346480" class="anchor"></span>Table 5‑6: SQLI_OUTPUT_FORMAT file—Fields

Purpose: Given the base column value derived from a VA FileMan field, entries in the SQLI_OUTPUT_FORMAT file (#1.5214) provide M code to generate the external value to present to the end-user for the column in question.

Columns do *not* need an output format if the base column data format is the same as its external data format. Output formats are therefore provided only for columns derived from Pointer and Set of Codes VA FileMan field types.

When looking for whether an output format is provided for a column, use the column's output format if one exists. Next, check the column's domain for an output format only if one is not found for the column. Finally, check the domain's data type for an output format if one is not found for the domain.

#### Code Fragment Formats

OF_EXT_EXPR: \$S('{B}:"",1:\$\$GET^DMSQU(9.4,{B}\_",",.01))  
*(substitute base value for all {B} placeholders;  
evaluates to external format of data).*

### SQLI_TABLE File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("T",

VA FileMan Number: 1.5215

Indexes:

B: ^DMSQ("T","B",\$E(T_NAME,1,30),ien)=""

C: ^DMSQ("T","C",\$E(T_FILE,1,30),ien)=""

D: ^DMSQ("T","D",\$E(T_GLOBAL,1,30),ien)=""

E: ^DMSQ("T","E",\$E(T_MASTER_TABLE,1,30),ien)=""

<span id="_Toc94346481" class="anchor"></span>Figure 5‑7: SQLI_TABLE file—Indexes

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 11%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>T_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Table name (valid SQL identifier).</td>
</tr>
<tr class="even">
<td>T_SCHEMA*</td>
<td>Pointer to SQLI_SCHEMA</td>
<td>0;2</td>
<td>Pointer to table's schema.</td>
</tr>
<tr class="odd">
<td>T_COMMENT</td>
<td>Free Text</td>
<td>0;3</td>
<td>Brief description.</td>
</tr>
<tr class="even">
<td>T_MASTER_TABLE</td>
<td>Pointer to SQLI_TABLE</td>
<td>0;4</td>
<td>Only populated if this table is projected for an index (it points to the indexed table.)</td>
</tr>
<tr class="odd">
<td>T_VERSION_FM</td>
<td>Numeric</td>
<td>0;5</td>
<td>Reserved for future use.</td>
</tr>
<tr class="even">
<td>T_ROW_COUNT</td>
<td>Numeric</td>
<td>0;6</td>
<td>Estimated number of rows in the table. This field is not populated by the SQLI projection, but instead by the ALLS^DMSQS and STATS^DMSQS entry points.</td>
</tr>
<tr class="odd">
<td>T_FILE</td>
<td>Numeric</td>
<td>0;7</td>
<td>VA FileMan data dictionary number of file, subfile, or word-processing field the table is derived from. It is null for tables that project indexes.</td>
</tr>
<tr class="even">
<td>T_UPDATE</td>
<td>Date</td>
<td>0;8</td>
<td>Date table projection last updated.</td>
</tr>
<tr class="odd">
<td>T_GLOBAL</td>
<td>Free Text</td>
<td><p><em>extract storage</em></p>
<p>node 1, 1-245</p></td>
<td>Global location of file entries. For documentation purposes only; use the C_GLOBAL values in the SQLI_COLUMN file (#1.5217) to determine the global location of file entries in code. Placeholders:{K}s in T_GLOBAL field values signify each part of the primary key.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346482" class="anchor"></span>Table 5‑7: SQLI_TABLE file—Fields

Purpose: Entries in the SQLI_TABLE file (#1.5215) project VA FileMan files, multiple fields, word-processing fields, and indexes as tables.

### SQLI_TABLE_ELEMENT File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("E",

VA FileMan Number: 1.5216

Indexes:

B: ^DMSQ("E","B",\$E(E_NAME,1,30),ien)=""

C: ^DMSQ("E","C",\$E(E_DOMAIN,1,30),ien)=""

D: ^DMSQ("E","D",\$E(E_TABLE,1,30),ien)=""

E: ^DMSQ("E","E",\$E(E_TYPE,1,30),ien)=""

F: ^DMSQ("E","F",E_TABLE,E_TYPE,ien)=""

G: ^DMSQ("E","G",E_TABLE,E_NAME,ien)=""

<span id="_Toc94346483" class="anchor"></span>Figure 5‑8: SQLI_TABLE_ELEMENT file—Indexes

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 14%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>E_NAME*</td>
<td>Free Text</td>
<td>0;1</td>
<td>Table element name (a valid SQL identifier). Foreign keys are distinguished by the suffix _FK or _PFK, primary keys by _PK.</td>
</tr>
<tr class="even">
<td>E_DOMAIN*</td>
<td>Pointer to SQLI_DOMAIN</td>
<td>0;2</td>
<td>Pointer to the domain to use for the table element.</td>
</tr>
<tr class="odd">
<td>E_TABLE*</td>
<td>Pointer to SQLI_TABLE</td>
<td>0;3</td>
<td>Pointer to the table the element is part of.</td>
</tr>
<tr class="even">
<td>E_TYPE*</td>
<td>Set of codes</td>
<td>0;4</td>
<td><p>Type of table element:</p>
<blockquote>
<p>'C' FOR COLUMN</p>
<p>'F' FOR FOREIGN KEY</p>
<p>'P' FOR PRIMARY KEY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>E_COMMENT</td>
<td>Free Text</td>
<td>0;5</td>
<td>Brief description.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346484" class="anchor"></span>Table 5‑8: SQLI_TABLE_ELEMENT file—Fields

Purpose: In SQL Data Definition Language (DDL), a table is defined by the DDL command:

CREATE TABLE \<table-name\> (table-element-commalist)

<span id="_Toc94346485" class="anchor"></span>Figure 5‑9: DDL command to define a table

There is one entry in the SQLI_TABLE_ELEMENT file (#1.5216) for each table element (columns, primary keys, and foreign keys) that should be the included in a CREATE TABLE command for each table projected in SQLI.

Entries in this file contain the two essential elements of an attribute in the relational model: attribute-name (E_NAME) and domain (E_DOMAIN). Elements not defined in the relational model, but necessary for physical mapping and formatting of table elements are contained in SQLI_COLUMN (#1.5217), SQLI_PRIMARY_KEY (#1.5218), and SQLI_FOREIGN_KEY (#1.5219) files.

### SQLI_COLUMN File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("C",

VA FileMan Number: 1.5217

Indexes:

B: ^DMSQ("C","B",\$E(C_TABLE_ELEMENT,1,30),ien)=""

C: ^DMSQ("C","C",\$E(C_PARENT,1,30),ien)=""

D: ^DMSQ("C","D",C_FILE,C_FIELD,ien)=""

E: ^DMSQ("C","E",\$E(C_OUTPUT_FORMAT,1,30),ien)=""

<span id="_Toc94346486" class="anchor"></span>Figure 5‑10: SQLI_COLUMN file—Indexes

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>C_TBL_ELEMENT*</td>
<td>Pointer to SQLI_TABLE_<br />
ELEMENT</td>
<td>0;1</td>
<td>Pointer to the table element entry that this column is associated with.</td>
</tr>
<tr class="even">
<td>C_FILE</td>
<td>Numeric</td>
<td>0;5</td>
<td>Corresponding VA FileMan file number, if column was derived from a data dictionary field.</td>
</tr>
<tr class="odd">
<td>C_WIDTH</td>
<td>Numeric</td>
<td>0;2</td>
<td>Maximum display width of column.</td>
</tr>
<tr class="even">
<td>C_SCALE</td>
<td>Numeric</td>
<td>0;3</td>
<td>Default number of decimal points for NUMERIC data type only. If scale is specified as 0, the column is projected as INTEGER.</td>
</tr>
<tr class="odd">
<td>C_FIELD</td>
<td>Numeric</td>
<td>0;6</td>
<td>Corresponding VA FileMan field number, if column was derived from a data dictionary field.</td>
</tr>
<tr class="even">
<td>C_NOT_NULL</td>
<td>Set of codes</td>
<td>0;7</td>
<td>1 if column is required in VA FileMan; 0 if not.</td>
</tr>
<tr class="odd">
<td>C_SECURE</td>
<td>Set of codes</td>
<td>0;8</td>
<td>Not yet implemented; for future use.</td>
</tr>
<tr class="even">
<td>C_VIRTUAL</td>
<td>Set of codes</td>
<td>0;9</td>
<td>1 if column is derived from a computed field, 0 if not. If true, the corresponding field value must be retrieved using a DBS call (one is provided for this in the C_FM_EXEC field.)</td>
</tr>
<tr class="odd">
<td>C_PARENT</td>
<td>Pointer to SQLI_COLUMN(#1.5217)</td>
<td>0;10</td>
<td><p>Populated if the global reference in the C_GLOBAL field is not a global root. Points to the column containing the next higher piece of the global reference (in C_GLOBAL) to which the current file level's key value and C_GLOBAL string should be appended to create the full global reference to the column's data.</p>
<ul>
<li><blockquote>
<p>Null for computed field columns (no permanent storage).</p>
</blockquote></li>
<li><blockquote>
<p>Null for IEN columns of top-level files (already at the highest level).</p>
</blockquote></li>
<li><blockquote>
<p>Null for the first index subscript column of an index table.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="even">
<td>C_GLOBAL</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>node 1,</p>
<p>1-245</p></td>
<td>For columns with permanent storage, partial global reference for the node where the column's data is stored.</td>
</tr>
<tr class="odd">
<td>C_PIECE</td>
<td>Numeric</td>
<td>0;11</td>
<td>For normally stored VA FileMan fields: The ^-delimited piece of the VA FileMan node field is stored in.</td>
</tr>
<tr class="even">
<td>C_EXTRACT_FROM</td>
<td>Numeric</td>
<td>0;12</td>
<td>For extract-storage type VA FileMan fields: The first character extract position of the VA FileMan node the field is stored in.</td>
</tr>
<tr class="odd">
<td>C_EXTRACT_THRU</td>
<td>Numeric</td>
<td>0;13</td>
<td>For extract-storage type VA FileMan fields: The last character extract position of the VA FileMan node the field is stored in.</td>
</tr>
<tr class="even">
<td>C_COMPUTE_EXEC</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>node 2,</p>
<p>1-245</p></td>
<td>The internal M code VA FileMan uses to calculate a computed field's value. Warning: This code may depend on the existence of a full FileMan context; the code in C_FM_EXEC is a safer alternative.</td>
</tr>
<tr class="odd">
<td>C_FM_EXEC</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>node 3,</p>
<p>1-245</p></td>
<td>M code to retrieve value of computed and pointer fields. Uses the DBS $$GET1^DIQ call to retrieve the field value.</td>
</tr>
<tr class="even">
<td>C_POINTER</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>node 4,</p>
<p>1-245</p></td>
<td><p>For columns derived from set of codes fields, this field contains the pairs of internal and external forms of each code separated by semicolons. The internal and external forms of a code are separated by colons. For example:</p>
<p>y:YES;n:NO;</p>
<p>For columns derived from pointer fields, this field contains the global root of the referenced file. For example:</p>
<p>DIC(4,</p></td>
</tr>
<tr class="odd">
<td>C_OUTPUT_<br />
FORMAT</td>
<td>Pointer to SQLI_OUTPUT_FORMAT</td>
<td>0;4</td>
<td>Pointer to the output format to use for this column, if one is needed, if the external format of the data differs from the base format.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346487" class="anchor"></span>Table 5‑9: SQLI_COLUMN file—Fields

Purpose: The SQLI_COLUMN file (#1.5217) contains the formatting and physical structure specifications for each column table element in projected tables. Each entry in the SQLI_COLUMN file (#1.5217) has a single corresponding SQLI_TABLE_ELEMENT file (#1.5216) entry that provides the relational specifications (name and domain) for the column.

#### Code Fragment Formats

C_GLOBAL: *(ien columns, top-level file)* ^DIZ(662000,

*(ien columns, subfile)* ,"EX",

*(VA FileMan field columns)* ,0)

*(Note: this field does not actually hold code, but instead holds a global reference.)*

C_COMPUTE_EXEC: S X=\$S(\$D(^DIA(DIA,D0,3)):^(3),1:"\<deleted\>")  
*(raw code from DD to set X to computed field value; may require VA FileMan environment context that SQLI can't provide - in the above example, the value of D0.)*

C_FM_EXEC: S {V}=\$\$GET^DMSQU(9.4901,"{K3},{K2},{K1},",.03)  
*(uses DBS call to set the variable you substitute in {V} to the external value of the computed or pointer field. You must substitute appropriate iens for all Placeholders:{K}s to identify the entry in question.)*

### SQLI_PRIMARY_KEY File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("P",

VA FileMan Number: 1.5218

Indexes:

B: ^DMSQ("P","B",\$E(P_TBL_ELEMENT,1,30),ien)=""

C: ^DMSQ("P","C",P_TBL_ELEMENT,P_SEQUENCE,ien)=""

D: ^DMSQ("P","D",\$E(P_COLUMN,1,30),ien)=""

<span id="_Toc94346488" class="anchor"></span>Figure 5‑11: SQLI_PRIMARY_KEY file—Indexes

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 16%" />
<col style="width: 11%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>P_TBL_ELEMENT*</td>
<td>Pointer to SQLI_TABLE_ELEMENT</td>
<td>0;1</td>
<td>Associates this part of a table's primary key with the single entry in the SQLI_TABLE_ELEMENT file (#1.5216) that organizes the entire primary key.</td>
</tr>
<tr class="even">
<td>P_COLUMN*</td>
<td>Pointer to SQLI_COLUMN</td>
<td>0;2</td>
<td>Pointer to the column on which this part of a table's primary key is based.</td>
</tr>
<tr class="odd">
<td>P_SEQUENCE*</td>
<td>Numeric<br />
(integer)</td>
<td>0;3</td>
<td>Sequence number of this part of the table's primary key. Use to determine what order to combine primary key columns to assemble the global path to an entry.</td>
</tr>
<tr class="even">
<td>P_START_AT</td>
<td>Free Text</td>
<td>0;4</td>
<td>M literal to initialize initial subscript value for a $ORDER loop through this part of the list of primary keys of a table.</td>
</tr>
<tr class="odd">
<td>P_END_IF</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>node 1,</p>
<p>1-245</p></td>
<td>M expression which returns true when the $ORDER loop started at P_START_AT reaches the end of this part of the list of primary keys of a table.</td>
</tr>
<tr class="even">
<td>P_ROW_COUNT</td>
<td>Integer</td>
<td>0;5</td>
<td><p>Estimated number entries for this part of the primary key.</p>
<p>For a multi-part key for the projection of a subfile, this would be set to the estimated number of entries at the file level of this part of the key.</p>
<p>Populate this field with ALLS^DMSQS or STATS^DMSQS, after SQLI generation.</p></td>
</tr>
<tr class="odd">
<td>P_PRESELECT</td>
<td>Mumps</td>
<td><p><em>Extract Storage</em></p>
<p>node 2,</p>
<p>1-245</p></td>
<td><p>Not implemented; for future use.</p>
<p>Code to possibly reference files in other UCIs with extended reference syntax.</p></td>
</tr>
<tr class="even">
<td>P_KEY_FORMAT</td>
<td>Pointer to SQLI_KEY_FORMAT</td>
<td>0;6</td>
<td>Conversion to use when the primary key value is different from the column it is based on. For primary keys of index tables, a conversion is provided to deal with the truncation of index subscripts to 30 characters.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346489" class="anchor"></span>Table 5‑10: SQLI_PRIMARY_KEY file—Fields

Purpose: Each entry in the SQLI_PRIMARY_KEY file (#1.5218) represents one part of the primary key of a projected table.

The P_COLUMN field points to the table column on which this part of the primary key is derived from.

The entire primary key of a table is composed of one or more entries in the SQLI_PRIMARY_KEY file (#1.5218). These entries are organized into a single key by the fact that they all point to the same single entry in the SQLI_TABLE_ELEMENT file (#1.5216) representing the entire primary key, via the P_TBL_ELEMENT field.

#### Code Fragment Formats

P_START_AT: 0  
*(value to start a \$ORDER loop at, to go through a file's entries. Not necessarily = 0; the \$ORDER loop through a list of primary keys of a table starts at 0 and ends at '{K} for all regular (data) tables. Other tables (indexes) will start at null and end if null. So you can assume 'null' if P_START_AT and P_END_IF fields aren't set.*

P_END_IF: '{K}  
*(substitute for {K} the current ien; use to terminate a \$ORDER loop through a file's entries. Not necessarily = "'{K}" - see P_START_AT above.)*

### SQLI_FOREIGN_KEY File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("F",

VA FileMan Number: 1.5219

Indexes:

B: ^DMSQ("F","B",\$E(F_TBL_ELEMENT,1,30),ien)=""

<span id="_Toc94346490" class="anchor"></span>Figure 5‑12: SQLI_FOREIGN_KEY file—Index

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 20%" />
<col style="width: 10%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>F_TBL_ELEMENT*</td>
<td>Pointer to SQLI_TABLE_<br />
ELEMENT</td>
<td>0;1</td>
<td>Associates this part of a table's foreign key with the single entry in the SQLI_TABLE_ELEMENT file (#1.5216) that organizes the entire foreign key.</td>
</tr>
<tr class="even">
<td>F_PK_ELEMENT*</td>
<td>Pointer to SQLI_PRIMARY_KEY</td>
<td>0;2</td>
<td>Pointer to the part of the primary key of the referenced table, that this part of the foreign key corresponds with.</td>
</tr>
<tr class="odd">
<td>F_CLM_ELEMENT*</td>
<td>Pointer to SQLI_COLUMN</td>
<td>0;3</td>
<td>Pointer to the column in the current table whose value should be "joined" with the associated part of the primary key of the referenced table.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346491" class="anchor"></span>Table 5‑11: SQLI_FOREIGN_KEY file—Fields

Purpose: Each entry in the SQLI_FOREIGN_KEY file (#1.5219) represents one part of a foreign key of a projected table.

As with primary keys, the entire foreign key of a table is composed of one or more entries in the SQLI_FOREIGN_KEY file (#1.5219). These entries are organized into a single key by pointing to the same SQLI_TABLE_ELEMENT file (#1.5216) entry, which then represents the entire foreign key.

A foreign key "pre-specifies" an explicit join between two tables. Foreign keys are projected for a table by SQLI when a join is already explicit in VA FileMan. SQLI provides foreign keys for:

- Pointer fields. For columns derived from pointer fields, a foreign key is provided for each pointer field.
- Subfiles. For table derived from subfiles, one foreign key is provided linking the subfile table to each of its "parent" tables (i.e., one to every table that represents a file level above the subfile.)

### SQLI_ERROR_TEXT File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("ET",

VA FileMan Number: 1.52191

Indexes:

B: ^DMSQ("ET","B",\$E(ERROR_TEXT,1,30),ien)=""

<span id="_Toc94346492" class="anchor"></span>Figure 5‑13: SQLI_ERROR_TEXT file—Index

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ERROR_TEXT</td>
<td>Free Text</td>
<td>0;1</td>
<td>SQLI error message</td>
</tr>
</tbody>
</table>

<span id="_Toc94346493" class="anchor"></span>Table 5‑12: SQLI_ERROR_TEXT file—Field

Purpose: The SQLI_ERROR_TEXT" file (#1.52191) holds a list of SQLI error messages generated during the last SQLI projection. It is used by entries in the SQLI_ERROR_LOG file (#1.52192), to indicate which type of SQLI error occurred during SQLI generation.

Entries in this file are purged at the start of each SQLI generation. The file is then populated with only those errors that occur during the particular SQLI generation.

### SQLI_ERROR_LOG File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global Root: ^DMSQ("EX",

VA FileMan Number: 1.52192

Indexes:

B: ^DMSQ("EX","B",\$E(FILEMAN_FILE,1,30),ien)=""

C: ^DMSQ("EX","C",\$E(ERROR,1,30),ien)=""

D: ^DMSQ("EX","D",\$E(ERROR_DATE,1,30),ien)=""

E: ^DMSQ("EX","E",\$E(FILEMAN_ERROR,1,30),ien)=""

<span id="_Toc94346494" class="anchor"></span>Figure 5‑14: SQLI_ERROR_LOG file—Indexes

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 19%" />
<col style="width: 10%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Field Name</strong></th>
<th><strong>Type</strong></th>
<th><strong>Node;<br />
Piece</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FILEMAN_FILE</td>
<td>Numeric</td>
<td>0;1</td>
<td>VA FileMan file number being processed when error occurred.</td>
</tr>
<tr class="even">
<td>FILEMAN_FIELD</td>
<td>Numeric</td>
<td>0;2</td>
<td>VA FileMan field number being processed when error occurred.</td>
</tr>
<tr class="odd">
<td>ERROR</td>
<td>Pointer to SQLI_ERROR_TEXT</td>
<td>0;3</td>
<td>Pointer to type of error.</td>
</tr>
<tr class="even">
<td>ERROR_DATE</td>
<td>Date</td>
<td>0;4</td>
<td>Date of SQLI generation.</td>
</tr>
<tr class="odd">
<td>FILEMAN_ERROR</td>
<td>Pointer to VA FileMan DIALOG file (#.84)</td>
<td>0;5</td>
<td>If the error was generated during a DBS call, and the DBS itself returned a particular error, this points to the DIALOG file (#.84) reference returned by the DBS call.</td>
</tr>
</tbody>
</table>

<span id="_Toc94346495" class="anchor"></span>Table 5‑13: SQLI_ERROR_LOG file—Fields

Purpose: The SQLI_ERROR_LOG file (#1.52192) is a log of all errors encountered when running the SQLI generation.

You can print out the errors stored in this log directly through VA FileMan. You can also use the supplied utility, MAIN^DMSQE, to print out the errors sorted by category of error.

# Application Program Interfaces (APIs)—Supported References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SQLI provides a set of supported M routine application program interfaces (APIs). Some APIs are intended for the use of M-to-SQL vendors; others are for general use. The supported APIs are as follows:

| API Entry Point | Description                                      |
|---------------------|------------------------------------------------------|
| SETUP^DMSQ          | Generate SQLI projection (non-interactive)           |
| ALLF^DMSQF          | Generate SQLI projection (interactive)               |
| KW^DMSQD            | Load keywords into the SQLI_KEY_WORD file (#1.52101) |
| ALLS^DMSQS          | Generate cardinality of all tables                   |
| STATS^DMSQS         | Generate cardinality of one table                    |
| \$\$CN^DMSQU        | Internal SQLI naming algorithm (column)              |
| \$\$FNB^DMSQU       | Internal SQLI naming algorithm (table)               |
| \$\$SQLI^DMSQU      | Internal SQLI naming algorithm (identifier)          |
| \$\$SQLK^DMSQU      | Internal SQLI naming algorithm (identifier)          |

<span id="_Toc94346496" class="anchor"></span>Table 6‑1: SQLI APIs

For a full description of each entry point, see the "SQLI Technical Information" chapter of the *VA FileMan SQLI Site Manual*.

In addition, all of SQLI's files, fields, and cross-references as distributed in patch DI\*21\*38 can be referenced directly without integration agreements. This enables M-to-SQL vendors to create SQLI mapping utilities using the SQLI file structures. Specifically, these are the files in the 1.52 to 1.53 number range, all stored in ^DMSQ.

# Other Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Domain Cardinality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most domains have no known or absolutely determinable domain cardinality. Column types for which domain cardinality can be determined are:

- Columns for Set of Codes fields: Take the C_POINTER field from the column derived from the FileMan Set of codes field. \$L(C_POINTER,":")-1 yields the cardinality for this column.
- Columns for Pointer fields: Use the P_ROW_COUNT value of the primary key of the pointed-to table, or the T_ROW_COUNT of the pointed-to table. This assumes that P_ROW_COUNT and T_ROW_COUNT have been populated for the table in question using either STATS^DMSQS or ALLS^DMSQS APIs.

### SQLI and Schemas

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of SQLI projects all VA FileMan files as part of a single schema, "SQLI".

If SQLI were to project the same VA FileMan file as part of *more than one* schema, it would need to project distinct, separate entries for the file in the SQLI_TABLE file (#1.5215) for each schema. So to project the PATIENT file in four different schemas, four different SQLI_TABLE file (#1.5215) entries would be projected, as well as four complete sets of table elements (columns, primary keys, and foreign keys).

Ordinarily it's best not to project a given file in more than one schema; in any case, SQLI currently does not support projecting the same file in multiple schemas.

### SQL Identifier Naming Algorithms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

By using consistent naming algorithms for files and fields, SQLI ensures that SQL table names for national files and fields between VA sites are the same. In addition, the algorithms enforce syntactical correctness and uniqueness of identifiers, and the exclusion of keywords from the naming of identifiers.

The following conventions are followed for table and table element names:

- Names are 1 to 30 characters long.
- Must start with a letter from A to z.
- May contain only the letters A through z, digits 0 through 9 and the underline character "\_".
- No repeating or trailing underlines are used.
- Names are case insensitive ("a" means the same as "A").
- SQL and vendor-specific keywords may not be used as names.
- Table names must be unique within each schema.
- Table element names (column, primary key, foreign key) must be unique within each table.
- If the name is too long it is compressed by removing vowels.

Under very unusual circumstances, the naming algorithms can produce a different field or file name between sites. The known circumstances that could produce a difference are as follows:

- The names of local files or fields result in a conflict with the naming of a national file or field.
- A difference in the excluded keyword list maintained in SQLI_KEY_WORD file (#1.52101) between sites results in a naming conflict at one site, and no conflict at another.
- National packages not loaded at a particular site avoid a naming conflict that otherwise would occur.

#### Which Objects Are Processed Through Naming Algorithms?

Tables and table element (column, primary key, and foreign key) names are generated through dynamic naming algorithms. Names for domains, data types, and output formats are manually assigned SQL-compatible names, but are not processed through the SQLI naming algorithms.

### VA Business Rules and Insert/Update/Delete Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may want to update VA FileMan files from SQL. Explicit support for vendors to implement Insert, Update, and Delete operations is not implemented in the first version of SQLI (patch DI\*21\*38).

A caution for implementing these types of access to VA FileMan data is that business rules are quite often not stored in VA FileMan data dictionaries. A significant portion of the business rules in VistA applications reside in application code. Updating that does *not* go through application software cannot execute business rules stored solely in application code, and can cause data corruption by circumventing business rules.

### SQLI Implementation Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- .001 Number Fields. The optional .001 number field for a file, if defined, represents the IEN of entries. Such fields are *not* projected as columns by SQLI. You can access this value using the TABLE_ID column (the IEN column), which SQLI does project for all tables.
- Asterisked Files. Any files or subfiles whose names start with an asterisk are not projected in SQLI. Note: Adding an asterisk to the beginning of a field name is a VA Programming SAC convention to mark the field as obsolete.
- Dangling Pointers. It is possible that a VA FileMan field may contain a pointer to a file not actually present at a given site. If so, the field is projected as a normal pointer field would be, but without the corresponding output format that permits navigation along a pointer chain to resolve the external value of the pointer. Such fields are flagged in the SQLI_ERROR_LOG file (#1.52192) during SQLI generation as "Pointer to Absent Files". Foreign keys for such fields are not constructed.
- Field Attributes *Not* Projected. Along with number, the following field attributes are projected by SQLI: Label, field length, type, specifier, global subscript location, pointer, multiple-valued, and the first line of the field's description. Other field attributes, including output transforms and pointer screens, are not projected.

|                                                                                                                |                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/020.png) | For more information about field attributes, please refer to the "Global File Structure" chapter in the *VA FileMan Programmer Manual*. |

- File Attributes *Not* Projected. Only file name and number are projected. Other file attributes, such as Special Lookup and Screens, are not.

|                                                                                                                |                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ![](di-21-38-vendor-guide-draft/021.png) | For more information about file attributes, please refer to the "Global File Structure" chapter in the *VA FileMan Programmer Manual*. |

- Files *Not* in ^DIC. Only files with entries in ^DIC (the dictionary of files) are projected. This means only VA FileMan-compatible files are projected.
- Internal VA FileMan Tables *Not* Projected. Certain tables used by VA FileMan internally (numbered below two) are not projected. Errors are logged during SQLI projection in the SQLI_ERROR_LOG file (#1.52192). VA FileMan DD numbers in this category include: .001, .1, .12, .15, .21, .3, 1.001, and 1.01.
- Multiline Computed Fields. Values are not returned for multiline computed fields, since DBS calls *cannot* retrieve multiline computed fields. An example of a multiline computed field is a backward extended pointer reference.
- Non-regular Cross-references. Only regular VA FileMan cross-references are projected. VA FileMan Trigger, KWIC (Key Word in Context), MUMPS, Mnemonic, Soundex, and Bulletin type indexes are absent from SQLI. Cross-references are only projected for possible optimizations by M-to-SQL vendors.
- Output Transforms. Output transforms are not projected. If formatting needs to be applied, it can be applied at the SQL vendor column level. For more elaborate output transforms that may call routines for processing, the logic will need to be reproduced in the context of the query. Depending on your M-to-SQL product's capability, the external value of a field (after the output transform is applied) could be returned by a user-defined function that invokes the VA FileMan \$\$EXTERNAL^DILF API call.
- Variable Pointers. Variable pointers are projected as text only. Their text value is resolved, but presented as text.

## Glossary

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
<td>![](di-21-38-vendor-guide-draft/022.png)</td>
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

## ## Appendix A—Quick Reference Card

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 18%" />
<col style="width: 16%" />
<col style="width: 31%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File#</strong></th>
<th><strong>File Name</strong></th>
<th><strong>Node</strong></th>
<th><strong>Fields (Keys In Boxes)</strong></th>
<th><strong>Cross References</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1.521</td>
<td>SQLI_SCHEMA</td>
<td>^DMSQ("S",D0,0)</td>
<td>(#.01) S_NAME [1F]</td>
<td>S_NAME(B)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) S_DESCRIPTION [2F]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("S",D0,1)</td>
<td colspan="2">(#1) S_SECURITY [1F] *<em>for future use</em></td>
</tr>
<tr class="even">
<td>1.52101</td>
<td>SQLI_KEY_WORD</td>
<td>^DMSQ("K",D0,0)</td>
<td>(#.01) KEY_WORD [1F]</td>
<td>KEY_WORD(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>1.5211</td>
<td>SQLI_DATA_TYPE</td>
<td>^DMSQ("DT",D0,0)</td>
<td>(#.01) D_NAME [1F]</td>
<td>D_NAME(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) D_COMMENT [2F]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2">(#3) D_OUTPUT_FORMAT [3P] *<em>for future use</em></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("DT",D0,1)</td>
<td colspan="2">(#2) D_OUTPUT_STRATEGY [E1,245K] *<em>for future use</em></td>
</tr>
<tr class="even">
<td>1.5212</td>
<td>SQLI_DOMAIN</td>
<td>^DMSQ("DM",D0,0)</td>
<td>(#.01) DM_NAME [1F]</td>
<td>DM_NAME(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) DM_DATA_TYPE [2P]</td>
<td>DM_DATA_TYPE(E)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) DM_COMMENT [3F]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#3) DM_TABLE [4P]</td>
<td>DM_TABLE(C)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#4) DM_WIDTH [5N]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#5) DM_SCALE [6N]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td colspan="2">(#6) DM_OUTPUT_FORMAT [7P] *<em>for future use</em></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#11) DM_FILEMAN_FIELD_TYPE [8S]</td>
<td>DM_FILEMAN_FIELD_TYPE(D)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("DM",D0,1)</td>
<td>(#7) DM_INT_EXPR [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("DM",D0,2)</td>
<td>(#8) DM_INT_EXEC [E1,245K]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("DM",D0,3)</td>
<td>(#9) DM_BASE_EXPR [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("DM",D0,4)</td>
<td>(#10) DM_BASE_EXEC [E1,245K]</td>
<td></td>
</tr>
<tr class="even">
<td>1.5213</td>
<td>SQLI_KEY_FORMAT</td>
<td>^DMSQ("KF",D0,0)</td>
<td>(#.01) KF_NAME [1F]</td>
<td>KF_NAME(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) KF_DATA_TYPE [2P]</td>
<td>KF_DATA_TYPE(C)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) KF_COMMENT [3F]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("KF",D0,1)</td>
<td>(#3) KF_INT_EXPR [E1,245K]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("KF",D0,2)</td>
<td>(#4) KF_INT_EXEC [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td>1.5214</td>
<td>SQLI_OUTPUT_FORMAT</td>
<td>^DMSQ("OF",D0,0)</td>
<td>(#.01) OF_NAME [1F]</td>
<td>OF_NAME(B)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#1) OF_DATA_TYPE [2P]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#2) OF_COMMENT [3F]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("OF",D0,1)</td>
<td>(#3) OF_EXT_EXPR [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("OF",D0,2)</td>
<td colspan="2">(#4) OF_EXT_EXEC [E1,245K] *<em>for future use</em></td>
</tr>
<tr class="even">
<td>1.5215</td>
<td>SQLI_TABLE</td>
<td>^DMSQ("T",D0,0)</td>
<td>(#.01) T_NAME [1F]</td>
<td>T_NAME(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) T_SCHEMA [2P]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) T_COMMENT [3F]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#3) T_MASTER_TABLE [4P]</td>
<td>T_MASTER_TABLE(E)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#4) T_VERSION_FM [5N]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#5) T_ROW_COUNT [6N]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#6) T_FILE [7N]</td>
<td>T_FILE(C)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#7) T_UPDATE [8D]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("T",D0,1)</td>
<td>(#8) T_GLOBAL [E1,245K]</td>
<td>T_GLOBAL(D)</td>
</tr>
<tr class="odd">
<td>1.5216</td>
<td>SQLI_TABLE_ELEMENT</td>
<td>^DMSQ("E",D0,0)</td>
<td>(#.01) E_NAME [1F]</td>
<td>E_NAME(B)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#1) E_DOMAIN [2P]</td>
<td>E_DOMAIN(C)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#2) E_TABLE [3P]</td>
<td>E_TABLE(D)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#3) E_TYPE [4S]</td>
<td>E_TYPE(E)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#4) E_COMMENT [5F]</td>
<td>E_TABLE,E_NAME(G)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td>E_TABLE,E_TYPE(F)</td>
</tr>
<tr class="odd">
<td>1.5217</td>
<td>SQLI_COLUMN</td>
<td>^DMSQ("C",D0,0)</td>
<td>(#.01) C_TABLE_ELEMENT [1P]</td>
<td>C_TABLE_ELEMENT(B)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) C_WIDTH [2N]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#3) C_SCALE [3N]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#16) C_OUTPUT_FORMAT [4P]</td>
<td>C_OUTPUT_FORMAT(E)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) C_FILE [5N]</td>
<td>C_FILE,C_FIELD(D)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#4) C_FIELD [6N]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#5) C_NOT_NULL [7S]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#6) C_SECURE [8S]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#7) C_VIRTUAL [9S]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#8) C_PARENT [10P]</td>
<td>C_PARENT(C)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#10) C_PIECE [11N]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#11) C_EXTRACT_FROM [12N]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#12) C_EXTRACT_THRU [13N]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("C",D0,1)</td>
<td>(#9) C_GLOBAL [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("C",D0,2)</td>
<td>(#13) C_COMPUTE_EXEC [E1,245K]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("C",D0,3)</td>
<td>(#14) C_FM_EXEC [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("C",D0,4)</td>
<td>(#15) C_POINTER [E1,245K]</td>
<td></td>
</tr>
<tr class="even">
<td>1.5218</td>
<td>SQLI_PRIMARY_KEY</td>
<td>^DMSQ("P",D0,0)</td>
<td>(#.01) P_TBL_ELEMENT [1P]</td>
<td>P_TBL_ELEMENT(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) P_COLUMN [2P]</td>
<td>P_COLUMN(D)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) P_SEQUENCE [3N]</td>
<td>P_TBL_ELEMENT,P_<br />
SEQUENCE(C)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#3) P_START_AT [4F]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#5) P_ROW_COUNT [5N]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#7) P_KEY_FORMAT [6P]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>^DMSQ("P",D0,1)</td>
<td>(#4) P_END_IF [E1,245K]</td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>^DMSQ("P",D0,2)</td>
<td colspan="2">(#6) P_PRESELECT [E1,245K] *<em>for future use</em></td>
</tr>
<tr class="even">
<td>1.5219</td>
<td>SQLI_FOREIGN_KEY</td>
<td>^DMSQ("F",D0,0)</td>
<td>(#.01) F_TBL_ELEMENT [1P]</td>
<td>F_TBL_ELEMENT(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) F_PK_ELEMENT [2P]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) F_CLM_ELEMENT [3P]</td>
<td></td>
</tr>
<tr class="odd">
<td>1.52191</td>
<td>SQLI_ERROR_TEXT</td>
<td>^DMSQ("ET",D0,0)</td>
<td>(#.01) ERROR_TEXT [1F]</td>
<td>ERROR_TEXT (B)</td>
</tr>
<tr class="even">
<td>1.52192</td>
<td>SQLI_ERROR_LOG</td>
<td>^DMSQ("EX",D0,0)</td>
<td>(#.01) FILEMAN_FILE [1N]</td>
<td>FILEMAN_FILE(B)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#1) FILEMAN_FIELD [2N]</td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#2) ERROR [3P]</td>
<td>ERROR(C)</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>(#3) ERROR_DATE [4D]</td>
<td>ERROR_DATE(D)</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>(#4) FILEMAN_ERROR [5P]</td>
<td>FILEMAN_ERROR(E)</td>
</tr>
</tbody>
</table>

<span id="_Toc94346497" class="anchor"></span>Table A-1: SQLI Quick Reference Card

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$
\$ORDERING to Loop Through a File's Data Entries, 3-9
A
About
Table Elements, 3-5
Acronyms (ISS)
Home Page Web Address, Glossary, 3
Algorithms
SQL Identifier Naming Algorithms, 7-1
Which Objects Are Processed Through Naming Algorithms, 7-2
ALLS^DMSQS, 7-1
APIs
ALLS^DMSQS, 7-1
STATS^DMSQS, 7-1
Appendix A—Quick Reference Card, A, 1
Application Program Interfaces (APIs), 6-1
Assembling Record Locations, 3-10
Assumptions About the Reader, xiv
Asterisked Files, 7-2
B
Base to External Conversions, 3-12
Base to Internal Conversions, 3-12
Building an SQLI Mapper, 2-1
Business Rules, 7-2
C
C_COMPUTE_EXEC Field, 5-23
C_EXTRACT_FROM Field, 3-11, 5-23
C_EXTRACT_THRU Field, 3-11, 5-23
C_FIELD Field, 5-22
C_FILE Field, 5-22
C_FM_EXEC Field, 3-2, 3-11, 4-3, 5-22, 5-23
C_GLOBAL Field, 3-6, 3-10, 3-11, 4-8, 5-19, 5-23, 5-24
C_NOT_NULL Field, 5-22
C_OUTPUT_FORMAT Field, 3-12, 5-22, 5-24
C_PARENT Field, 5-23
C_PIECE Field, 3-11, 5-23
C_POINTER Field, 5-24, 7-1
C_SCALE Field, 5-22
C_SECURE Field, 5-22
C_TBL_ELEMENT Field, 5-22
C_VIRTUAL Field, 3-11, 4-3, 5-22
C_WIDTH Field, 5-22
Callout Boxes, xiii
Cardinality
Domain, 7-1
Columns
IEN, 3-7, 4-3, 5-23
Processing, 3-6
Retrieving Column Values, 3-11
Through a DBS Call, 3-11
Value Conversions, 3-11
Compatibility
Kernel, 2-5
Computed Fields, 3-11, 4-3, 5-22
Contents, v
Conversions
Columns Value Conversions, 3-11
Domain Conversions (Base to Internal), 3-12
Output Format Conversions (Base to External), 3-12
Cross-references
Non-regular, 7-3
D
D_COMMENT Field, 5-12
D_NAME Field, 5-12
D_OUTPUT_FORMAT Field, 3-12, 5-12
D_OUTPUT_STRATEGY Field, 5-12
DA RETURN CODES File (#3.22), 3-3, 3-4, 3-8
DA_RETURN_CODES Table, 3-6
Dangling Pointers, 7-2
Data Dictionary
Data Dictionary Utilities Menu, xiv
Listings, xiv
Synchronization, 2-4
Data Storage of Entries, 3-9
Date Fields, 4-3
DBS Calls, 1-1, 3-11, 4-3, 4-4, 5-22, 5-23, 5-29
Delete
Operations, 7-2
SQL, 7-2
DIALOG File (#.84), 5-29
DM_BASE_EXEC Field, 3-12, 4-3, 5-14
DM_BASE_EXPR, 5-14
DM_BASE_EXPR Field, 3-12, 5-13
DM_COMMENT Field, 5-13
DM_DATA_TYPE Field, 5-13
DM_FILEMAN_FIELD_TYPE Field, 4-3, 5-14
DM_INT_EXEC Field, 3-12, 4-3, 5-13, 5-14
DM_INT_EXPR Field, 3-12, 5-13
DM_NAME Field, 5-13
DM_OUTPUT_FORMAT Field, 3-12, 5-13
DM_SCALE Field, 5-13
DM_TABLE Field, 5-13
DM_WIDTH Field, 5-13
Documentation
Revisions, iii
Symbols, xii
Domain Cardinality, 7-1
Domain Conversions (Base to Internal), 3-12
Domains
FM_BOOLEAN, 3-12
FM_DATE, 3-12
FM_MOMENT, 3-12
E
E_COMMENT Field, 5-20
E_DOMAIN Field, 5-20
E_NAME Field, 5-20
E_TABLE Field, 5-20
E_TYPE Field, 5-20
Elements
About Table Elements, 3-5
Entity-relationship Diagram, 2-3
Entry Data Storage, 3-9
Entry Locations, 3-10
Entry Points, 6-1
ERROR Field, 5-29
ERROR_DATE Field, 5-29
ERROR_TEXT Field, 5-28
EVS Anonymous Directories, xv
F
F_CLM_ELEMENT Field, 5-27
F_PK_ELEMENT Field, 5-27
F_TBL_ELEMENT Field, 5-27
Fields
.001 Number, 7-2
Attributes Not Projected, 7-3
C_COMPUTE_EXEC, 5-23
C_EXTRACT_FROM, 3-11, 5-23
C_EXTRACT_THRU, 3-11, 5-23
C_FIELD, 5-22
C_FILE, 5-22
C_FM_EXEC, 3-2, 3-11, 4-3, 5-22, 5-23
C_GLOBAL, 3-6, 3-10, 3-11, 4-8, 5-23, 5-24
C_NOT_NULL, 5-22
C_OUTPUT_FORMAT, 3-12, 5-22, 5-24
C_PARENT, 5-23
C_PIECE, 3-11, 5-23
C_POINTER, 5-24, 7-1
C_SCALE, 5-22
C_SECURE, 5-22
C_TBL_ELEMENT, 5-22
C_VIRTUAL, 3-11, 4-3, 5-22
C_WIDTH, 5-22
Computed, 3-11, 4-3, 5-22
D_COMMENT, 5-12
D_NAME, 5-12
D_OUTPUT_FORMAT, 3-12, 5-12
D_OUTPUT_STRATEGY, 5-12
Date, 4-3
DM_BASE_EXEC, 3-12, 4-3, 5-14
DM_BASE_EXPR, 3-12, 5-13
DM_COMMENT, 5-13
DM_DATA_TYPE, 5-13
DM_FILEMAN_FIELD_TYPE, 4-3, 5-14
DM_INT_EXEC, 3-12, 4-3, 5-13, 5-14
DM_INT_EXPR, 3-12, 5-13
DM_NAME, 5-13
DM_OUTPUT_FORMAT, 3-12, 5-13
DM_SCALE, 5-13
DM_TABLE, 5-13
DM_WIDTH, 5-13
E_COMMENT, 5-20
E_DOMAIN, 5-20
E_NAME, 5-20
E_TABLE, 5-20
E_TYPE, 5-20
ERROR, 5-29
ERROR_DATE, 5-29
ERROR_TEXT, 5-28
F_CLM_ELEMENT, 5-27
F_PK_ELEMENT, 5-27
F_TBL_ELEMENT, 5-27
FILEMAN_ERROR, 5-29
FILEMAN_FIELD, 5-29
FILEMAN_FILE, 5-29
Free Text, 4-3
How SQLI Translates VA FileMan Field Types into SQL Columns, 4-5
KEY_WORD, 5-11
KF_COMMENT, 5-15
KF_DATA_TYPE, 5-15
KF_INT_EXEC, 5-15
KF_INT_EXPR, 5-15
KF_NAME, 5-15
Multiline Computed, 4-3, 7-3
Mumps, 4-3
Numeric, 4-3
OF_COMMENT, 5-17
OF_DATA_TYPE, 5-17
OF_EXT_EXEC, 5-17
OF_EXT_EXPR, 5-17
OF_NAME, 5-17
P_COLUMN, 5-25, 5-26
P_END_IF, 5-25, 5-26
P_ENDIF, 3-9
P_KEY_FORMAT, 5-26
P_PRESELECT, 5-25
P_ROW_COUNT, 5-25, 7-1
P_SEQUENCE, 3-2, 3-7, 3-8, 3-9, 3-10, 4-8, 5-25
P_START_AT, 3-8, 3-9, 5-25, 5-26
P_START_AT, 5-26
P_START_AT, 5-26
P_TBL_ELEMENT, 5-25, 5-26
PATIENT_ID, 4-3
Pointer, 3-11, 3-13, 4-4, 5-17, 5-27, 7-1
S_DESCRIPTION, 5-10
S_NAME, 5-10
S_SECURITY, 5-10
Set of Codes, 4-4, 5-17, 7-1
T_COMMENT, 5-19
T_FILE, 5-19
T_GLOBAL, 3-10, 5-19
T_MASTER_TABLE, 4-7, 5-19
T_NAME, 5-19
T_ROW_COUNT, 5-19, 7-1
T_SCHEMA, 3-3, 5-19
T_UPDATE, 5-19
T_VERSION_FM, 5-19
Types (VA FileMan), 4-2
Variable Pointer, 2-2, 3-11, 4-4
Word-processing, 2-2, 3-14, 4-6, 5-19
FieldS
DM_INT_EXPR, 3-12
Figures and Tables, ix
FILEMAN_ERROR Field, 5-29
FILEMAN_FIELD Field, 5-29
FILEMAN_FILE Field, 5-29
Files
Asterisked, 7-2
Attributes *Not* Projected, 7-3
DA RETURN CODES (#3.22), 3-3, 3-4, 3-8
Definition Structures, 4-1
DIALOG (#.84), 5-29
NEW_PERSON (#200), 3-13
Not in ^DIC, 7-3
PATIENT (#2), 4-2, 4-3, 4-7
References, 5-9
SQLI_COLUMN (#1.5217), 3-2, 3-5, 3-6, 3-11, 3-12, 4-3, 4-4, 5-19, 5-21, 5-22, 5-23, 5-24, 5-25, 5-27
SQLI_DATA_TYPE (#1.5211), 3-12, 5-12, 5-14, 5-15, 5-17
SQLI_DOMAIN (#1.5212), 3-11, 3-12, 5-12, 5-13, 5-14, 5-20
SQLI_ERROR_LOG (#1.52192), 5-28, 5-29, 7-2, 7-3
SQLI_ERROR_TEXT, 5-28
SQLI_FOREIGN_KEY (#1.5219), 3-5, 5-21, 5-27
SQLI_KEY_FORMAT (#1.5213), 4-8, 5-15, 5-26
SQLI_KEY_WORD (#1.52101), 2-4, 5-11, 6-1, 7-2
SQLI_OUTPUT_FORMAT (#1.5214), 3-11, 3-12, 5-13, 5-17, 5-24
SQLI_PRIMARY_KEY (#1.5218), 3-5, 3-7, 3-8, 3-9, 3-10, 5-21, 5-25, 5-26, 5-27
SQLI_SCHEMA (#1.521), 5-10
SQLI_SCHEMA File (#1.521), 3-3, 5-10, 5-19
SQLI_TABLE (#1.5215), 3-3, 3-4, 3-8, 3-10, 5-13, 5-19, 5-20, 7-1
SQLI_TABLE_ELEMENT (#1.5216), 3-4, 3-5, 3-7, 3-8, 3-13, 5-20, 5-21, 5-24, 5-25, 5-26, 5-27
Find a Table Element's Column Entry, 3-6
Find the Primary Key for a Given Table, 3-7
Find the Projected Table for a File, 3-4
FM_BOOLEAN Domain, 3-12
FM_DATE Domain, 3-12
FM_MOMENT Domain, 3-12
Foreign Keys, 3-5, 3-12, 3-13, 3-14, 4-4, 5-13, 5-27, 7-2
FORUM, iv
Free Text Fields, 4-3
G
Glossary, 1
Glossary (ISS)
Home Page Web Address, Glossary, 3
Guidelines
SQLI Mappers, 2-4
H
Help
At Prompts, xiv
Online, xiv
Home Pages
Adobe Acrobat Quick Guide Web Address, xv
Adobe Web Address, xv
Health Systems Design and Development (HSD&D) Web Address, xv
ISS Acronyms Home Page Web Address, Glossary, 3
ISS Glossary Home Page Web Address, Glossary, 3
SQLI Home Page Web Address, xv
VistA Documentation Library (VDL) Home Page Web Address, xv
How to
Obtain Technical Information Online, xiii
Use this Manual, xii
I
Identifier Naming Algorithms, 7-1
IEN Columns, 3-7, 4-3, 5-23
Implementation Notes, 7-2
Indexes
VA FileMan, 4-6
Information Provided by SQLI, 2-2
Insert
Operations, 7-2
SQL, 7-2
Internal VA FileMan Tables Not Projected, 7-3
Introduction, 1-1
ISS Acronyms
Home Page Web Address, Glossary, 3
ISS Glossary
Home Page Web Address, Glossary, 3
K
Kernel Compatibility, 2-5
KEY_WORD Field, 5-11
Keys
Foreign, 3-12
Keywords, 5-11, 7-2
Populating, 2-4
KF_COMMENT Field, 5-15
KF_DATA_TYPE Field, 5-15
KF_INT_EXEC Field, 5-15
KF_INT_EXPR Field, 5-15
KF_NAME Field, 5-15
L
List File Attributes Option, xiv
M
Mappers
Building, 2-1
Guidelines, 2-4
Mapping
VA FileMan Fields to SQL Data Types, 4-3
Menus
Data Dictionary Utilities, xiv
Multiline Computed Fields, 4-3, 7-3
Multiple. *See Subfiles*
Mumps Fields, 4-3
N
Naming Algorithms, 7-1
NEW_PERSON File (#200), 3-13
Non-regular Cross-references, 7-3
Notes
Implementation, 7-2
Numeric Fields, 4-3
O
Obtain Technical Information Online, How to, xiii
Obtaining Data Dictionary Listings, xiv
OF_COMMENT Field, 5-17
OF_DATA_TYPE Field, 5-17
OF_EXT_EXEC Field, 5-17
OF_EXT_EXPR Field, 5-17
OF_NAME Field, 5-17
Online
Documentation, xiv
Help Frames, xiv
Options
List File Attributes, xiv
ORDERING to Loop Through a File's Data Entries, 3-9
Organization of SQLI Information, 2-2
Orientation, xii
Other Issues, 7-1
Output Format Conversions (Base to External), 3-12
Output Transforms, 7-3
P
P_COLUMN Field, 5-25, 5-26
P_END_IF, 3-9
P_END_IF Field, 5-25, 5-26
P_ENDIF Field, 3-9
P_KEY_FORMAT Field, 5-26
P_PRESELECT Field, 5-25
P_ROW_COUNT Field, 5-25, 7-1
P_SEQUENCE Field, 3-2, 3-7, 3-8, 3-9, 3-10, 4-8, 5-25
P_START_AT, 3-9
P_START_AT Field, 3-8, 3-9, 5-25, 5-26
P_TBL_ELEMENT Field, 5-25, 5-26
Parent Foreign Keys, 3-14
Parsing the SQLI Projection, 3-1
Patches
Revisions, iv
PATIENT File (#2), 4-2, 4-3, 4-7
PATIENT_ID Field, 4-3
Placeholders, 3-1
{B}, 3-2, 3-12, 4-4, 5-14, 5-18
{E}, 3-2
{I}, 3-2, 3-12, 5-14, 5-15
{K}, 3-8, 3-10, 4-7, 4-8, 5-15, 5-19, 5-24, 5-26
{K}, 3-2
{V}, 3-2, 5-24
Pointer Fields, 3-11, 3-13, 4-4, 5-17, 5-27, 7-1
Pointers
Dangling, 7-2
Variable, 7-3
Populating
Keywords, 2-4
SQLI_KEY_WORD File (#1.52101), 2-4
Primary Keys, 3-2, 3-5, 3-7, 3-8, 3-9, 3-7–3-9, 3-10, 3-14, 4-3, 4-8, 5-13, 5-15, 5-19, 5-25, 5-26, 5-27, 7-1, 7-2
For a Projected Subfile, 3-8
Processing Columns, 3-6
Processing Tables, 3-4
Programming SAC, 2-4, 2-5
Q
Question Mark Help, xiv
Quick Reference Card, A, 1
R
Reader, Assumptions About the, xiv
Record
Data Storage, 3-9
Locations, 3-10
Reference Materials, xv
Relational Model, 4-1
Retrieving Column Values, 3-11
Through a DBS Call, 3-11
Return Value Placeholder
{V}, 3-2
Revision History, iii
Documentation, iii
Patches, iv
S
S_DESCRIPTION Field, 5-10
S_NAME Field, 5-10
S_SECURITY Field, 5-10
SAC
Programming, 2-5
Schemas, 3-3, 7-1
Set of Codes Fields, 4-4, 5-17, 7-1
SQL and VA FileMan Terminology, xiii
SQL Identifier Naming Algorithms, 7-1
SQL Training, xii
SQLI
Entity-Relationship Diagram, 2-3
Home Page Web Address, xv
Implementation Notes, 7-2
Information Provided, 2-2
Organization of Information, 2-2
Schemas, 7-1
SQLI Mapper
Building, 2-1
SQLI Mappers Guidelines, 2-4
SQLI_COLUMN File (#1.5217), 3-2, 3-5, 3-6, 3-11, 3-12, 4-3, 4-4, 5-19, 5-21, 5-22, 5-23, 5-24, 5-25, 5-27
SQLI_DATA_TYPE File (#1.5211), 3-12, 5-12, 5-14, 5-15, 5-17
SQLI_DOMAIN File (#1.5212), 3-11, 3-12, 5-12, 5-13, 5-14, 5-20
SQLI_ERROR_LOG File (#1.52192), 5-28, 5-29, 7-2, 7-3
SQLI_ERROR_TEXT, 5-28
SQLI_FOREIGN_KEY File (#1.5219), 3-5, 5-21, 5-27
SQLI_KEY_FORMAT File (#1.5213), 4-8, 5-15, 5-26
SQLI_KEY_WORD File (#1.52101), 2-4, 5-11, 6-1, 7-2
SQLI_OUTPUT_FORMAT File (#1.5214), 3-11, 3-12, 5-13, 5-17, 5-24
SQLI_PRIMARY_KEY File (#1.5218), 3-5, 3-7, 3-8, 3-9, 3-10, 5-21, 5-25, 5-26, 5-27
SQLI_SCHEMA File (#1.521), 3-3, 5-10, 5-19
SQLI_TABLE File (#1.5215), 3-3, 3-4, 3-8, 3-10, 5-13, 5-19, 5-20, 7-1
SQLI_TABLE_ELEMENT File (#1.5216), 3-4, 3-5, 3-7, 3-8, 3-13, 5-20, 5-21, 5-24, 5-25, 5-26, 5-27
Standards and Conventions, 2-4
Starting Point
SQLI_SCHEMA File (#1.521), 3-3
STATS^DMSQS, 7-1
Subfiles, 3-7, 3-8, 3-9, 3-10, 3-13, 3-14, 4-2, 4-6, 5-19, 5-24, 5-25, 5-27
Summary
How SQLI Translates VA FileMan Field Types into SQL Columns, 4-5
Supported References, 6-1
Symbols Found in the Documentation, xii
Synchronization
DD, 2-4
T
T_COMMENT Field, 5-19
T_FILE Field, 5-19
T_GLOBAL Field, 3-10, 5-19
T_MASTER_TABLE Field, 4-7, 5-19
T_NAME Field, 5-19
T_ROW_COUNT Field, 5-19, 7-1
T_SCHEMA Field, 3-3, 5-19
T_UPDATE Field, 5-19
T_VERSION_FM Field, 5-19
Table Elements, 3-4
Tables
About Table Elements, 3-5
DA_RETURN_CODES, 3-6
Find a Table Element's Column Entry, 3-6
Find the Primary Key for a Given Table, 3-7
Finding the Projected Table for a File, 3-4
Internal VA FileMan Tables Not Projected, 7-3
Processing), 3-4
TaskMan guidelines, 2-5
Terminology
VA FileMan and SQL, xiii
Training
SQL, xii
Transforms
Output, 7-3
U
Update
Operations, 7-2
SQL, 7-2
URLs
Adobe Acrobat Quick Guide Web Address, xv
Adobe Home Page Web Address, xv
Health Systems Design and Development (HSD&D) Home Page Web Address, xv
Use this Manual, How to, xii
Using
Adobe Acrobat Reader, xv
The {B}, {E}, {I}, {K}, and {V} Placeholders, 3-1
V
VA Business Rules, 7-2
VA FileMan
Field Types, 4-2
Summary, 4-5
File Definition Structures, 4-1
Indexes, 4-6
SQL, 4-1
SQL Terminology, xiii
Subfiles (Multiples), 4-2
VA FileMan, SQL, and the Relational Model, 4-1
VA Programming Standards and Conventions, 2-4
Variable Pointer Fields, 2-2, 3-11, 4-4
Variable Pointers, 7-3
VistA Documentation Library (VDL)
Home Page Web Address, xv
W
Web Pages
Adobe Acrobat Quick Guide Web Address, xv
Adobe Home Page Web Address, xv
Health Systems Design and Development (HSD&D) Home Page Web Address, xv
ISS Acronyms Home Page Web Address, Glossary, 3
ISS Glossary Home Page Web Address, Glossary, 3
SQLI Home Page Web Address, xv
VistA Documentation Library (VDL) Home Page Web Address, xv
What is
SQLI?, 1-1
The Purpose of this Manual?, 1-1
VA FileMan, 1-1
Which Objects Are Processed Through Naming Algorithms, 7-2
Word-processing Fields, 2-2, 3-14, 4-6, 5-19
