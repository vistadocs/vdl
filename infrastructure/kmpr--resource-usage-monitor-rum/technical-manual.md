---
title: KMPR Version 2 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: KMPR
app_name: Resource Usage Monitor (RUM)
section: INF
app_status: active
pkg_ns: KMPR
patch_ver: 2
patch_id: KMPR*2
group_key: "KMPR:KMPR:2"
file_numbers: []
security_keys: []
menu_options: 6
description: 
audience: 
keywords: 
  - kmpr
  - table
  - software
  - resource
  - usage
  - contents
  - monitor
  - collection
  - class
  - background
page_count: 0
word_count: 8153
section_count: 5
table_count: 75
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Resource_Usage_Mon/kmpr2_0tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Resource_Usage_Mon/kmpr2_0tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=130"
---

![](kmpr-version-2-technical-manual/001.png)

RESOURCE USAGE MONITOR (RUM)

TECHNICAL MANUAL

June 2003

VistA Health Systems Design & Development (HSD&D)

Development and Infrastructure Support (DaIS)

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
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
<td></td>
</tr>
<tr class="even">
<td>06/27/03</td>
<td>1.0</td>
<td>Initial Resource Usage Monitor V. 2.0 software documentation creation.</td>
<td>REDACTED</td>
<td></td>
</tr>
<tr class="odd">
<td>11/17/03</td>
<td>1.1</td>
<td>Updated documentation for format and minor miscellaneous edits (no change pages issued)</td>
<td>REDACTED</td>
<td></td>
</tr>
<tr class="even">
<td>01/12/05</td>
<td>1.2</td>
<td><p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
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
<td colspan="2">REDACTED</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td colspan="2"></td>
</tr>
</tbody>
</table>

<span id="_Toc56819915" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

Figures and Tables

## Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Services' Resource Usage Monitor (RUM) Project Team consists of the following Development and Infrastructure Service (DaIS) personnel:

- REDACTED

Capacity Planning (CP) Services' RUM Project Team would like to thank the following sites/organizations/personnel for their assistance in reviewing and/or testing the RUM V. 2.0 software and documentation (names within teams are listed alphabetically):

- REDACTED

### ## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of Resource Usage Monitor (RUM) software and the functionality it provides for Veterans Health Information Systems and Technology Architecture (VistA) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                       |
| ![](kmpr-version-2-technical-manual/002.png) | Used to inform the reader of general information including references to additional reading material. |
| ![](kmpr-version-2-technical-manual/003.png)                                                              | Used to caution the reader to take special notice of critical information.                            |

Table ii: Documentation symbol descriptions

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
| ![](kmpr-version-2-technical-manual/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                                                                                |                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/005.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. Please refer to the *Resource Usage Monitor (RUM) Technical Manual* for further information. |

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
| ![](kmpr-version-2-technical-manual/006.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment
- VA FileMan data structures and terminology
- Microsoft Windows
- M programming language

It provides an overall explanation of configuring the Resource Usage Monitor (RUM) interface and the changes contained in Resource Usage Monitor (RUM) software, version 2.0. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about the Resource Usage Monitor (RUM) software should consult the following:

- *Resource Usage Monitor (RUM) Release Notes & Installation Guide*
- *Resource Usage Monitor (RUM) User Manual*
- *Resource Usage Monitor (RUM) Technical Manual* (this manual)
- Capacity Planning (CP) Services' Home Page (for more information on Capacity Planning) at the following Web address:

> <http://vista.med.va.gov/capman/default.htm>

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
<td>![](kmpr-version-2-technical-manual/007.png)</td>
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
| ![](kmpr-version-2-technical-manual/008.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Acknowledgements](#acknowledgements)
    - [## Orientation](#orientation)
- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
    - [Implementation](#implementation)
    - [Maintenance](#maintenance)
- [Files](#files)
    - [Files](#files-1)
    - [Templates](#templates)
- [Global Translation, Journaling, and Protection](#global-translation-journaling-and-protection)
    - [Translation](#translation)
    - [Journaling](#journaling)
    - [Protection](#protection)
- [Routines](#routines)
- [Exported Options](#exported-options)
    - [Options With Parents](#options-with-parents)
    - [Options Without Parents](#options-without-parents)
    - [Protocols](#protocols)
- [# Archiving and Purging](#archiving-and-purging)
    - [Archiving](#archiving)
    - [Purging](#purging)
- [Callable Routines](#callable-routines)
- [External Relations](#external-relations)
    - [VistA Software Requirements](#vista-software-requirements)
    - [DBA Approvals and Integration Agreements](#dba-approvals-and-integration-agreements)
- [Internal Relations](#internal-relations)
    - [Option Dependencies](#option-dependencies)
    - [Relationship of RUM Software with VistA](#relationship-of-rum-software-with-vista)
    - [Namespace](#namespace)
- [Software-wide and Key Variables](#software-wide-and-key-variables)
- [SAC Exemptions](#sac-exemptions)
- [Software Product Security](#software-product-security)
    - [Security Management](#security-management)
    - [Mail Groups and Alerts](#mail-groups-and-alerts)
    - [Remote Systems](#remote-systems)
    - [Interfacing](#interfacing)
    - [Electronic Signatures](#electronic-signatures)
    - [Security Keys](#security-keys)
    - [File Security](#file-security)
    - [Official Policies](#official-policies)
  - [Glossary](#glossary)
  - [Index](#index)
This distribution contains the Resource Usage Monitor (RUM) software, version 2.0. This version of the software can be installed over any previous test versions of RUM without any adverse problems.
The Resource Usage Monitor (RUM) software is a fully automated support tool developed by Capacity Planning (CP) Services. It entails the capture of all system and Veterans Health Information Systems and Technology Architecture (VistA) option workload specifics from participating sites. This workload data is then summarized on a weekly basis and is automatically transferred via network mail (i.e., MailMan) to the Capacity Planning National Database.
The Veterans Health Administration (VHA) developed the Resource Usage Monitor (RUM) software in order to obtain more accurate information regarding the current and future VistA system and option workload at the VA Medical Centers (VAMCs).
Installing the RUM software creates the collection process mechanism and other necessary components of the software. The fully automated data collection mechanism entails capturing all system and VistA option workload specifics at the site into a temporary ^KMPTMP("KMPR") temporary collection global. The collection mechanism is continuously monitoring each process on the system while trapping system and VistA option workload data.
On a nightly basis, the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] moves the data within the ^KMPTMP("KMPR") temporary collection global to the RESOURCE USAGE MONITOR file (#8971.1). Upon completion, the data within the ^KMPTMP("KMPR") temporary collection global is purged.
Every Sunday night, the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] monitors the RESOURCE USAGE MONITOR file to ensure that only a maximum of three weeks’ worth of data is maintained at the site.
Also, each Sunday night, the RUM Background Driver option automatically compresses the information contained within the RESOURCE USAGE MONITOR file (#8971.1) into weekly statistics. These weekly statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes. The site also receives a summary of the system workload data in the form of an electronic turn-around message.
|                                                                                                                |                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/009.png) | For a sample of the electronic turn-around message, please refer to the "Software Management" topic in Chapter 2 in the *Resource Usage Monitor (RUM) User Manual*. |
The data is also available on Capacity Planning (CP) Services' Web site at the following Web addresses:
- Statistics—Provides statistics for each listed site:
> <http://vista.med.va.gov/capman/Statistics/Default.htm>
- Projections—Provides data trends for each listed site:
> <http://vista.med.va.gov/capman/TrendSetter/Default.htm>
IRM staff utilizes the options that are available at the site to manage this software. IRM staff responsible for capacity planning tasks at the site can use these options to review system workload trends. Additionally, the IRM staff can review specific workload information for any given VistA option.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

After the initial setup procedures are performed as detailed in the *Resource Usage Monitor (RUM) Release Notes & Installation Guide*, and IRM staff starts the collection process with the software-supplied option, the software basically operates transparent to IRM with minimal impact on system resources. The software uses the Kernel-supplied TaskMan utility to schedule a background task and it is then rescheduled to run on a regular nightly basis. The nightly time frame for data file upload was chosen in order to keep temporary global information to a minimum size.

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/010.png) | For more information on initial setup procedures, please refer to "Preliminary Consideration" topic in the *Resource Usage Monitor (RUM) Release Notes & Installation Guide*. |

|                                                                                                                |                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/011.png) | For more information on RUM and RUM-related options, please refer to Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

### Implementation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### ^KMPR Global

The Resource Usage Monitor (RUM) software creates the ^KMPR global to store the RESOURCE USAGE MONITOR file (#8971.1) information. This global will be trimmed (records deleted) each Sunday by the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] task to contain a maximum of 21 days of data.

IRM staff should ensure that adequate disk space exists for the ^KMPR global after volume set placement for this global has been determined. The following are sample VistA Composite Index (VCI) estimates:

- VCI 1 Site—75 MB
- VCI 3 Site—40 MB

|                                                                                                                |                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/012.png) | For more information on the ^KMPR global, please refer to Chapter 4, "Global Translation, Journaling, and Protection," in this manual. |

#### ^KMPTMP("KMPR") Global

The Resource Usage Monitor (RUM) software utilizes the ^KMPTMP("KMPR") temporary collection global to store RUM data. This global will contain one day's worth of data at maximum. The ^KMPTMP("KMPR") temporary collection global will be purged automatically by the nightly RUM Background Driver \[KMPR BACKGROUND DRIVER\] task. This option is scheduled to run every night at 1 a.m.

In terms of allocating the necessary disk space to accommodate the size and expected growth of ^KMPTMP, this value will vary somewhat depending on the size and overall workload level at the medical center. In general, sites should allow approximately 117,760,000 bytes (i.e., 115,000 DSM blocks or 57,500 Cache blocks) for ^KMPTMP and ensure that an appropriate reference entry for this global exists in the translation table.

|                                                                                                                |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/013.png) | For more information on the ^KMPTMP("KMPR") temporary collection global, please refer to Chapter 4, "Global Translation, Journaling, and Protection," in this manual. |

#### RUM Background Driver Option

The IRM staff should use the Status of RUM Collection option \[KMPR STATUS COLLECTION\] to ensure that the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is scheduled to run every day at 1 a.m.

If the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is not shown as being scheduled to run in the future, the IRM staff should use TaskMan's Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], to schedule the KMPR BACKGROUND DRIVER option to run every day at 1 a.m.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-technical-manual/014.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/015.png) | For more information on the Background Driver option, please refer to the "RUM Background Driver Option" topic in Chapter 7, "Exported Options," in this manual. |

#### Collecting RUM Data

The IRM staff should invoke the Start RUM Collection option \[KMPR START COLLECTION\] to begin the collection of system and VistA option workload data.

|                                                                                                                |                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/016.png) | For more information on the Start RUM Collection option, please refer to the "STR—Start RUM Collection Option" topic in the Chapter 7, "Exported Options," in this manual. |

### Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information throughout this manual is meant to help IRM in the maintenance of the software. The discussion that follows covers the options available to assist IRM in that maintenance.

#### RUM Manager Menu

All options for the RUM Manager Menu \[KMPR RUM MANAGER MENU\] can be found under the Capacity Management menu \[XTCM MAIN\]. The XTCM MAIN menu is found under the Eve menu and should be assigned to IRM staff member(s) who support(s) this software and other capacity planning tasks.

|                                                                                                                |                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/017.png) | For more information on the RUM Manger Menu, please refer to the "RUM Manager Menu" topic in the Chapter 7, "Exported Options," in this manual. |

#### RUM Background Driver Option

The IRM staff should first invoke the Status of RUM Collection option \[KMPR STATUS COLLECTION\], which is located under the RUM Manager Menu \[KMPR RUM MANAGER MENU\] to ensure that the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is scheduled to run every day at 1 a.m.

If the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is not shown as being scheduled to run in the future, use TaskMan's Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], to schedule the KMPR BACKGROUND DRIVER option to run every day at 1 a.m.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-technical-manual/018.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

|                                                                                                                |                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/019.png) | For more information on the Background Driver option, please refer to the "RUM Background Driver Option" topic in the Chapter 7, "Exported Options," in this manual. |

#### Collecting RUM Data

The IRM staff should invoke the Start RUM Collection option \[KMPR START COLLECTION\] to begin the collection of system and VistA option workload data.

|                                                                                                                |                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/020.png) | For more information on the Start RUM Collection option, please refer to the "STR—Start RUM Collection Option" topic in the Chapter 7, "Exported Options," in this manual. |

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software consists of two globals with one file, the RESOURCE USAGE MONITOR file (#8971.1).

This chapter describes the RUM-related file including the file number, file name, global location, and description of the file.

|                                                                                                                |                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/021.png) | For more information on the RUM globals, please refer to Chapter 4, "Global Translation, Journaling, and Protection," in this manual. |

### Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 19%" />
<col style="width: 21%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File Number</strong></th>
<th><strong>File Name</strong></th>
<th><strong>Global</strong></th>
<th><strong>File Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>8971.1</td>
<td>RESOURCE USAGE MONITOR</td>
<td>^KMPR(8971.1</td>
<td><p>This file stores system and VistA option workload information.</p>
<p>No data comes with the file.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc56819917" class="anchor"></span>Table 3‑1: RUM file list

### Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Resource Usage Monitor (RUM) software does *not* contain any templates.

# Global Translation, Journaling, and Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following globals are distributed with the Resource Usage Monitor (RUM) software:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Global</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^KMPR</td>
<td><p>The ^KMPR global contains data for the RESOURCE USAGE MONITOR file. This global only contains the RESOURCE USAGE MONITOR file (#8971.1).</p>
<p>Each Sunday this global will be trimmed (records deleted) automatically to contain a maximum of 21 days of data. This global is trimmed by the RUM Background Driver option [KMPR BACKGROUND DRIVER], which is scheduled to run every day at 1 a.m.</p></td>
</tr>
<tr class="even">
<td>^KMPTMP("KMPR")</td>
<td><p>The ^KMPTMP temporary collection global is the storage location for inter-process temporary data. The Resource Usage Monitor (RUM) software uses the ^KMPTMP("KMPR") sub-node to temporarily store one day's worth of data at maximum.</p>
<p>The contents of this sub-node are deleted by the RUM Background Driver option [KMPR BACKGROUND DRIVER], which is scheduled to run every day at 1 a.m.<br />
<br />
In terms of allocating the necessary disk space to accommodate the size and expected growth of ^KMPTMP, this value will vary somewhat depending on the size and overall workload level at the medical center. In general, sites should allow approximately 117,760,000 bytes (i.e., 115,000 DSM blocks or 57,500 Cache blocks) for ^KMPTMP and ensure that an appropriate reference entry for this global exists in the translation table.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc56819918" class="anchor"></span>Table 4‑1: RUM global descriptions

|                                                                                                                |                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/022.png) | This version of the Resource Usage Monitor (RUM) software deletes obsolete RUM data from the temporary ^XTMP("KMPR") global. |

### Translation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the translation requirements/recommendations for the RUM globals:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Global</strong></th>
<th><strong>Translation</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^KMPR</td>
<td>Mandatory, if the operating system supports this function.</td>
</tr>
<tr class="even">
<td>^KMPTMP("KMPR")</td>
<td>Recommended. As per the <em>Kernel Technical Manual</em>:<br />
<br />
The ^KMPTMP temporary collection global should be translated, if the operating system supports this function.</td>
</tr>
</tbody>
</table>

<span id="_Toc56819919" class="anchor"></span>Table 4‑2: RUM global translation requirements/recommendations

### Journaling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the journaling requirements/recommendations for the RUM globals:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Global</strong></th>
<th><strong>Journaling</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^KMPR</td>
<td>Mandatory, if the operating system supports this function.</td>
</tr>
<tr class="even">
<td>^KMPTMP("KMPR")</td>
<td><em>Not</em> recommended. As per the <em>Kernel Technical Manual</em>:<br />
<br />
The ^KMPTMP temporary collection global should <em>not</em> be journaled.</td>
</tr>
</tbody>
</table>

<span id="_Toc56819920" class="anchor"></span>Table 4‑3: RUM global journaling requirements/recommendations

### Protection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists the protection settings for the RUM globals:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 37%" />
<col style="width: 41%" />
</colgroup>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2"><strong>Protection</strong></td>
</tr>
<tr class="even">
<td><strong>Global Name</strong></td>
<td><strong>DSM for OpenVMS</strong></td>
<td><strong>Caché</strong></td>
</tr>
<tr class="odd">
<td>^KMPR</td>
<td><p>System: RW</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>User: RW</p></td>
<td><p>Owner: RW</p>
<p>Group: RW</p>
<p>World: RW</p>
<p>Network: RW</p></td>
</tr>
<tr class="even">
<td>^KMPTMP("KMPR")</td>
<td><p>System: RW</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>User: RW</p></td>
<td><p>Owner: RW</p>
<p>Group: RW</p>
<p>World: RW</p>
<p>Network: RW</p></td>
</tr>
</tbody>
</table>

> <span id="_Ref345829034" class="anchor"></span>Table 4‑4: RUM global protection settings

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter contains a list of the routines exported with the Resource Usage Monitor (RUM) software. A brief description of the routines is provided.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine Name</strong></th>
<th><strong>Routine Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPRBD01<br />
<br />
KMPRBD02<br />
<br />
KMPRBD03<br />
<br />
KMPRBD04</td>
<td><p>Routines that are called by the RUM Background Driver [KMPR BACKGROUND DRIVER] option.<br />
<br />
On a nightly basis, these routines:</p>
<ul>
<li><blockquote>
<p>Take data from the ^KMPTMP("KMPR") temporary collection global and transfer it to the RESOURCE USAGE MONITOR (#8971.1) file.</p>
</blockquote></li>
<li><blockquote>
<p>Purge the ^KMPTMP("KMPR") temporary collection global.</p>
</blockquote></li>
</ul>
<p>Every Sunday night, these routines:</p>
<ul>
<li><p>Ensure that the RESOURCE USAGE MONITOR file (#8971.1) contains a maximum of 21 days of data.</p></li>
<li><p>Compress weekly statistics from the data within the RESOURCE USAGE MONITOR file (#8971.1) and upload this information to the Capacity Planning National Database.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>KMPRENV</td>
<td>An environment check routine that determines whether Kernel patch XU*8.0*186 has been installed. The Resource Usage Monitor V. 2.0 software installation requires that Kernel patch XU*8.0*186 be installed first.</td>
</tr>
<tr class="odd">
<td>KMPRP1</td>
<td>Routine called by the RUM Data for an Option option [KMPR PRINT OPTION DATA].</td>
</tr>
<tr class="even">
<td>KMPRP2</td>
<td>Routine called by the Print Hourly Occurrence Distribution option [KMPR PRINT HOURLY OCCURRENCE]</td>
</tr>
<tr class="odd">
<td>KMPRPG01</td>
<td>Routine called by the RUM Data for All Nodes (Graph) option [KMPR GRAPH ALL NODES].</td>
</tr>
<tr class="even">
<td>KMPRPG02</td>
<td>Routine called by the RUM Data for Single Node (Graph) option [KMPR GRAPH HOURLY SINGLE NODE].</td>
</tr>
<tr class="odd">
<td>KMPRPN03</td>
<td>Routine called by the Package Resource Usage option [KMPR PRINT NODE PERCENT].</td>
</tr>
<tr class="even">
<td>KMPRPOST</td>
<td><p>A post-install routine that does the following:</p>
<ul>
<li><blockquote>
<p>Deletes obsolete Resource Usage Monitor (RUM) data from the ^XTMP("KMPR") global.</p>
</blockquote></li>
<li><blockquote>
<p>Checks and reschedules, if necessary, the RUM Background Driver [KMPR BACKGROUND DRIVER] task.</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td>KMPRSS</td>
<td>Routine has multiple entry points. One entry point displays the current status of the Resource Usage Monitor (RUM) collection routines. Another entry point informs the RUM collection routines to begin collecting system and VistA option workload data. Another entry point informs the RUM collection routines to stop collecting data.</td>
</tr>
<tr class="even">
<td>KMPRUTL<br />
<br />
KMPRUTL1<br />
<br />
KMPRUTL2<br />
<br />
KMPRUTL3</td>
<td>Generic utility routines that are called by varying Resource Usage Monitor (RUM) routines.</td>
</tr>
</tbody>
</table>

<span id="_Toc56819922" class="anchor"></span>Table 5‑1: RUM routine list

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are exported with the Resource Usage Monitor (RUM) software.

### Options *With* Parents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Options are listed in the order that they appear in the RUM Manager Menu:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option Name</strong></th>
<th><strong>Option Menu Text</strong></th>
<th><strong>Type</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>KMPR RUM MANAGER MENU</td>
<td>RUM Manager Menu</td>
<td>Menu</td>
</tr>
<tr class="even">
<td>KMPR STATUS COLLECTION</td>
<td>Status of RUM Collection option</td>
<td>Run Routine:<br />
<br />
STAT^KMPRSS</td>
</tr>
<tr class="odd">
<td>KMPR START COLLECTION</td>
<td>Start RUM Collection option</td>
<td>Run Routine:<br />
<br />
START^KMPRSS</td>
</tr>
<tr class="even">
<td>KMPR STOP COLLECTION</td>
<td>Stop RUM Collection option</td>
<td>Run Routine:<br />
<br />
STOP^KMPRSS</td>
</tr>
<tr class="odd">
<td>KMPR REPORTS MENU</td>
<td>RUM Reports menu</td>
<td>Menu</td>
</tr>
<tr class="even">
<td>KMPR GRAPH ALL NODES</td>
<td>RUM Data for All Nodes (Graph) option</td>
<td>Run Routine:<br />
<br />
EN^KMPRPG01</td>
</tr>
<tr class="odd">
<td>KMPR GRAPH HOURLY SINGLE NODE</td>
<td>RUM Data by Date for Single Node (Graph) option</td>
<td>Run Routine:<br />
<br />
EN^KMPRPG02</td>
</tr>
<tr class="even">
<td>KMPR PRINT OPTION DATA</td>
<td>RUM Data for an Option option</td>
<td>Run Routine:<br />
<br />
EN^KMPRP1</td>
</tr>
<tr class="odd">
<td>KMPR PRINT HOURLY OCCURRENCE</td>
<td>Print Hourly Occurrence Distribution option</td>
<td>Run Routine:<br />
<br />
KMPRP2</td>
</tr>
<tr class="even">
<td>KMPR PRINT NODE PERCENT</td>
<td>Package Resource Usage option</td>
<td>Run Routine:<br />
<br />
EN^KMPRPN03</td>
</tr>
</tbody>
</table>

<span id="_Toc56819923" class="anchor"></span>Table 6‑1: RUM exported options *with* parents

#### RUM Manager Menu

\[KMPR RUM MANAGER MENU\]

The RUM Manager Menu \[KMPR RUM MANAGER MENU\] is located under the Capacity Management menu \[XTCM MAIN\] menu.

The KMPR RUM MANAGER MENU and XTCM MAIN menu options should be assigned to the IRM staff member(s) who support(s) this software and other capacity planning tasks.

The RUM Manager Menu contains the following options:

STA Status of RUM Collection \[KMPR STATUS COLLECTION\]

STR Start RUM Collection \[KMPR START COLLECTION\]

STP Stop RUM Collection \[KMPR STOP COLLECTION\]

RPT RUM Reports ... \[KMPR REPORTS MENU\]

<span id="_Toc56819924" class="anchor"></span>Figure 6‑1: RUM Manager menu

#### STA—Status of RUM Collection Option

\[KMPR STATUS COLLECTION\]

The Status of RUM Collection option \[KMPR STATUS COLLECTION\] displays the current status of the Resource Usage Monitor (RUM) collection routines. This option identifies whether RUM is currently running. Additionally, this option shows the reschedule frequency of the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] and whether the ^KMPTMP("KMPR") temporary collection global is currently present.

|                                                                                                                |                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/023.png) | This option has been enhanced with the RUM V. 2.0 software. |

|                                                                                                                |                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/024.png) | For more information on this option, please refer to the "STA—Status of RUM Collection Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### STR—Start RUM Collection Option

\[KMPR START COLLECTION\]

The Start RUM Collection option \[KMPR START COLLECTION\] informs the Resource Usage Monitor (RUM) collection routines to begin collecting system and VistA option workload data.

|                                                                                                                |                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/025.png) | For more information on this option, please refer to the "STR—Start RUM Collection Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### STP—Stop RUM Collection Option

\[KMPR STOP COLLECTION\]

The Stop RUM Collection option \[KMPR STOP COLLECTION\] informs the Resource Usage Monitor (RUM) collection routines to stop collecting data.

|                                                                                                                |                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/026.png) | For more information on this option, please refer to the "STP—Stop RUM Collection Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### RPT—RUM Reports Menu

\[KMPR REPORTS MENU\]

The RUM Reports menu \[KMPR REPORTS MENU\] contains various reports that generate report information from the system and VistA option workload statistics accumulated within the RESOURCE USAGE MONITOR file (#8971.1).

The RUM Reports menu consists of the following options:

GAN RUM Data for All Nodes (Graph) \[KMPR GRAPH ALL NODES\]

GSN RUM Data by Date for Single Node (Graph) \[KMPR GRAPH HOURLY SINGLE NODE\]

PDO RUM Data for an Option \[KMPR PRINT OPTION DATA\]

PHO Print Hourly Occurrence Distribution \[KMPR PRINT HOURLY OCCURRENCE\]

PRU Package Resource Usage \[KMPR PRINT NODE PERCENT\]

<span id="_Toc26607902" class="anchor"></span>Figure 6‑2: RUM Reports menu options

|                                                                                                                |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/027.png) | For more information on this option, please refer to the "RPT—RUM Reports Menu" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### GAN—RUM Data for All Nodes (Graph) Option

\[KMPR GRAPH ALL NODES\]

The RUM Data for All Nodes (Graph) option \[KMPR GRAPH ALL NODES\] displays a bar graph and totals of the selected system workload data element statistics for *all* system nodes within a given date range.

|                                                                                                                |                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/028.png) | For more information on this option, please refer to the "GAN—RUM Data for All Nodes (Graph)" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### GSN—RUM Data by Date for Single Node (Graph) Option

\[KMPR GRAPH HOURLY SINGLE NODE\]

The RUM Data by Date for Single Node (Graph) option \[KMPR GRAPH HOURLY SINGLE NODE\] displays a bar graph and totals of the selected system workload data element statistics for a *single* node for each day within a given date range.

|                                                                                                                |                                                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/029.png) | For more information on this option, please refer to the "GSN—RUM Data by Date for Single Node (Graph) Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### PDO—RUM Data for an Option

\[KMPR PRINT OPTION DATA\]

The RUM Data for an Option option \[KMPR PRINT OPTION DATA\] lists all the system workload data element statistics within a given date range for any of the following:

- Option
- Protocol
- Remote Procedure Call (RPC)

|                                                                                                                |                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/030.png) | For more information on this option, please refer to the "PDO—RUM Data for an Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### PHO—Print Hourly Occurrence Distribution Option

\[KMPR PRINT HOURLY OCCURRENCE\]

The Print Hourly Occurrence Distribution option \[KMPR PRINT HOURLY OCCURRENCE\] lists the system workload hourly occurrence for any of the following:

- Option/Task
- Protocol
- Remote Procedure Call (RPC)

|                                                                                                                |                                                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/031.png) | For more information on this option, please refer to the "PHO—Print Hourly Occurrence Distribution Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

#### PRU—Package Resource Usage Option

\[KMPR PRINT NODE PERCENT\]

The Package Resource Usage option \[KMPR PRINT NODE PERCENT\] displays the statistics for a specified VistA software application namespace per computer node. The printout shows the system workload as a percent of the totals that the given software application namespace was running as either an option, protocol, Remote Procedure Call (RPC), or background task.

|                                                                                                                |                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/032.png) | For more information on this option, please refer to the "PRU—Package Resource Usage Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

### Options *Without* Parents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following option does not appear on any menu:

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 39%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Option Name</strong></td>
<td><strong>Option Menu Text</strong></td>
<td><strong>Type</strong></td>
</tr>
<tr class="even">
<td>KMPR BACKGROUND DRIVER</td>
<td>RUM Background Driver</td>
<td>Run Routine:<br />
<br />
KMPRBD01</td>
</tr>
</tbody>
</table>

<span id="_Toc56819926" class="anchor"></span>Table 6‑2: RUM exported options *without* parents

#### RUM Background Driver Option

\[KMPR BACKGROUND DRIVER\]

The RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is *not* assigned to any menu. This option is scheduled through TaskMan to start the Resource Usage Monitor (RUM) software's background routine.

This option will compress the Resource Usage Monitor statistics located in ^KMPTMP("KMPR") into daily statistics. This option must be queued to run each day on off hours.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-technical-manual/033.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

This option should be rescheduled with the Schedule/Unschedule Options option \[XUTM SCHEDULE\] located under the Taskman Management menu \[XUTM MGR\].

|                                                                                                                |                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/034.png) | For more information on this option, please refer to the "RUM Background Driver Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

### Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software does *not* export any protocols with this version.

# # Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software contains one file called RESOURCE USAGE MONITOR. This file will automatically be trimmed (records deleted) by the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] to contain a maximum of 21 days of data.

Since the Resource Usage Monitor (RUM) software automatically maintains a fixed amount of data at the site, archiving functions are not necessary and are not provided.

|                                                                                                                |                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/035.png) | For more information on the RUM Background Driver option, please refer to the "RUM Background Driver Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

### Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resource usage data is accumulated into the ^KMPTMP("KMPR") temporary collection global and is killed every day at 1 a.m. by the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] after being moved into the RESOURCE USAGE MONITOR file (#8971.1).

|                                                                                                                |                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/036.png) | For more information on the ^KMPTMP("KMPR") global, please refer to the "^KMPTMP("KMPR") Global" topic in Chapter 2, "Implementation and Maintenance," and in Chapter 4, "Global Translation, Journaling, and Protection," in this manual. |

The RESOURCE USAGE MONITOR file. will be automatically trimmed (records deleted) by the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] to contain a maximum of 21 days of data.

Since the Resource Usage Monitor (RUM) software automatically maintains a fixed amount of data at the site, purging functions are not necessary and are *not* provided.

|                                                                                                                |                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/037.png) | For more information on the RESOURCE USAGE MONITOR file, please refer to Chapter 3, "File," in this manual. |

|                                                                                                                |                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/038.png) | For more information on the RUM Background Driver option, please refer to the "RUM Background Driver Option" topic in Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

# Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Resource Usage Monitor (RUM) software does *not* provide any callable routine entry points (i.e., Application Program Interfaces \[APIs\]) that are available for general use.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VistA Software Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software relies on the following VistA software to run effectively (listed alphabetically):

|                           |             |                                              |
|---------------------------|-------------|----------------------------------------------|
| Software              | Version | Patch Information                        |
| Capacity Management Tools | 1.0         | Patch KMPD\*1.0\*1.                          |
| Health Level Seven (HL7)  | 1.6         | Fully patched, including Patch HL\*1.6\*103. |
| Kernel                    | 8.0         | Fully patched, including Patch XU\*8.0\*186. |
| Kernel Toolkit            | 7.3         | Fully patched.                               |
| MailMan                   | 8.0         | Fully patched.                               |
| VA FileMan                | 22.0        | Fully patched.                               |

<span id="_Toc56819927" class="anchor"></span>Table 9‑1: External Relations—VistA software

This version of Resource Usage Monitor (RUM) software uses Kernel's %ZOSVKR routine that utilizes system-specific calls.

All operating system interfaces on which the Resource Usage Monitor (RUM) software is dependent have been encapsulated into the Kernel %ZOSVKR routine. The %ZOSVKR routine contains code that enables use of the \$VIEW function to get job table information from the operating system.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-technical-manual/039.png)</td>
<td>The Kernel %ZOSVKR routine was first introduced with the issuance of Kernel Patch XU*8.0*107 and was updated with Kernel Patch XU*8.0*186.<strong><br />
<br />
</strong>Kernel Patch XU*8*107 also installed Resource Usage Monitor (RUM) data collection routines for DSM for OpenVMS sites.</td>
</tr>
</tbody>
</table>

### DBA Approvals and Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Database Administrator (DBA) maintains a list of Integration Agreements (IAs) or mutual agreements between software developers allowing the use of internal entry points or other software-specific features that are not available to the general programming public.

This version of Resource Usage Monitor (RUM) software is not dependent on any agreements.

To obtain the current list of IAs, if any, to which the Capacity Planning (CP) Services' RUM software (KMPR) is a custodian:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Custodial Package Menu option \[DBA IA CUSTODIAL MENU\].

> 5\. Choose the ACTIVE by Custodial Package option \[DBA IA CUSTODIAL\].

> 6\. When this option prompts you for a package, enter CAPACITY MANAGEMENT - RUM or KMPR

> 7\. All current IAs to which the Capacity Planning (CP) Services' RUM software is a custodian are listed.

To obtain detailed information on a specific integration agreement:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Inquire option \[DBA IA INQUIRY\].

> 5\. When prompted for "INTEGRATION REFERENCES," enter the specific integration agreement number of the IA you would like to display.

> 6\. The option then lists the full text of the IA you requested.

To obtain the current list of IAs, if any, to which the Capacity Planning (CP) Services' RUM software (KMPR) is a subscriber:

> 1\. Sign on to the FORUM system (forum.va.gov).

> 2\. Go to the DBA menu \[DBA\].

> 3\. Select the Integration Agreements Menu option \[DBA IA ISC\].

> 4\. Select the Subscriber Package Menu option \[DBA IA SUBSCRIBER MENU\].

> 5\. Choose the Print ACTIVE by Subscribing Package option \[DBA IA SUBSCRIBER\].

> 6\. When prompted with "START WITH SUBSCRIBING PACKAGE," enter KMPR (in uppercase). When prompted with "GO TO SUBSCRIBING PACKAGE," enter KMPR (in uppercase).

> 7\. All current IAs to which the Capacity Planning (CP) Services' RUM software is a subscriber are listed.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Option Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All options in the Resource Usage Monitor (RUM) software, under the RUM Manager Menu \[KMPR MANAGER MENU\], can function independently.

Only TaskMan's Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\], can invoke the RUM Background Driver option \[KMPR BACKGROUND DRIVER\].

|                                                                                                                |                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/040.png) | For more information regarding the Resource Usage Monitor (RUM) options, please refer to Chapter 4, "RUM Options," in the *Resource Usage Monitor (RUM) User Manual*. |

### Relationship of RUM Software with VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### HL7 V. 1.6

This version of Resource Usage Monitor (RUM) software requires that VistA HL7 Patch HL\*1.6\*103 be installed prior to the installation of the RUM V. 2.0 software. This patch updated the following three APIs, which are used for calculating the volume of HL7 activity at a site over a user-defined period of time:

- \$\$CM^HLUCM
- \$\$CM2^HLUCM
- \$\$CM2F^HLUCM

These APIs calculate the volume of HL7 activity over a period of time. The information collected includes the following:

- Total number characters in the messages.
- Total Number of messages or message units.
- Total time elapsed for transmission of messages.

|                                                                                                                |                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/041.png) | For more information regarding VistA HL7 Patch HL\*1.6\*103 and the APIs, please refer to the HL\*1.6\*103 patch description in the Patch Module on FORUM. |

#### Capacity Management (CM) Tools V. 1.0

This version of Resource Usage Monitor (RUM) software requires that Capacity Management (CM) Tools Version 1.0 and Patch KMPD\*1.0\*1 be installed prior to the installation of the RUM V. 2.0 software. This software application also requires that the VistA HL7 software application, fully patched, also be installed.

#### Kernel V. 8.0

This version of Resource Usage Monitor (RUM) software uses Kernel's %ZOSVKR routine that utilizes system-specific calls. The Kernel %ZOSVKR routine was first introduced with the issuance of Kernel Patch XU\*8.0\*107 and was updated with Kernel Patch XU\*8.0\*186.

|                                                   |                                                                                                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-technical-manual/042.png) | This distribution of the Resource Usage Monitor (RUM) software is dependent on Kernel Patch XU\*8.0\*186. Kernel Patch \#186 (i.e., XU\*8.0\*186) is included in the KMPR2_0.KID file and is installed *before* the RUM V. 2.0 software. |

### Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Services has been given the KMP\* namespace for both routines and global(s). The Resource Usage Monitor (RUM) software utilizes the KMP<u>R</u> namespace for its routines and global. Therefore, you should review your translation table setting(s) to determine the proper placement for the KMP\* global namespace.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-technical-manual/043.png)</td>
<td>The Resource Usage Monitor (RUM) software utilizes Capacity Planning (CP) Services KMPU*-namespaced routines.<br />
<br />
The KMPU*-namespaced routines are generic utility routines that were introduced with the issuance of the RUM V. 1.0 software but are not specific to the RUM software.</td>
</tr>
</tbody>
</table>

# Software-wide and Key Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software does *not* employ the use of software-wide or key variables.

# SAC Exemptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Resource Usage Monitor (RUM) software does *not* have any Programming Standards and Conventions (SAC) exemptions.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* special legal requirements involved in the use of the RUM software.

### Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Resource Usage Monitor (RUM) software creates the following mail group:

> KMP-CAPMAN.

This version of the Resource Usage Monitor (RUM) software does *not* make use of alerts.

### Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Resource Usage Monitor (RUM) software transmits weekly RUM statistics to the Capacity Planning National Database located at the Albany OI Field Office.

### Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No *non*-VA products are embedded in or required by this version of the Resource Usage Monitor (RUM) software, other than those provided by the underlying operating systems.

This version of Resource Usage Monitor (RUM) software uses Kernel's %ZOSVKR routine that utilizes system-specific calls. The Kernel %ZOSVKR routine was first introduced with the issuance of Kernel Patch XU\*8.0\*107 and was updated with Kernel Patch XU\*8.0\*186.

All operating system interfaces on which the Resource Usage Monitor (RUM) software is dependent have been encapsulated into the Kernel %ZOSVKR routine. The %ZOSVKR routine contains code that enables use of the \$VIEW function to get job table information from the operating system.

### Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* electronic signatures used within this version of the Resource Usage Monitor (RUM) software.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* specific security keys exported with this version of the Resource Usage Monitor (RUM) software.

### File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This version of the Resource Usage Monitor (RUM) software establishes the following security over its files:

| File Number | File Name          | DD | RD | WR | DEL | LAYGO | AUDIT |
|-----------------|------------------------|--------|--------|--------|---------|-----------|-----------|
| 8971.1          | RESOURCE USAGE MONITOR | @      | @      | @      | @       | @         | @         |

<span id="_Toc56819928" class="anchor"></span>Table 13‑1: RUM VA FileMan file protection

### Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are *no* special legal requirements involved in the use of Resource Usage Monitor (RUM)'s interface.

Distribution of the Resource Usage Monitor (RUM) software is unrestricted.

## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                       |                                                                                                                                                                                                                                                                    |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BIO REFERENCE         | Buffered I/O reference. A system workload data element that gives the number of times that a buffered access has been called because of M routine code execution. Terminals and printers are normally considered to be a buffered device within the M environment. |
| CAPACITY PLANNING     | The process of assessing a system's capacity and evaluating its efficiency relative to workload in an attempt to optimize system performance. (Formerly known as Capacity Management.)                                                                             |
| CPU TIME              | A system workload data element that gives the amount of time that the processor has spent executing M routine code.                                                                                                                                                |
| DIO REFERENCE         | Disk (Direct) I/O reference. A system workload data element that gives the number of times that a disk access has been requested because of M routine code execution.                                                                              |
| ELAPSED TIME          | A system workload data element that gives the amount of actual time that has passed while executing M routine code.                                                                                                                                                |
| GLO REFERENCE         | Global reference. A system workload data element that gives the number of times that a global variable name has been called because of M routine code execution.                                                                                               |
| NUMBER OF OCCURRENCES | A system workload data element that gives a total measure of the number of VistA option executions.                                                                                                                                                                |
| PAGE FAULTS           | A system workload data element that gives the number of times that a job had to use non-physical (i.e., paged) memory.                                                                                                                                             |
| RUM                   | Resource Usage Monitor. A fully automated support tool developed by the Capacity Planning (CP) Services, which entails the daily capture of system and VistA option workload information from participating sites.                                     |
| TURN-AROUND MESSAGE   | The mail message that is returned to the KMP-CAPMAN mail group detailing the system workload change over the previous reported session.                                                                                                                            |
<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-technical-manual/044.png)</td>
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

## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A
Acknowledgements, ix
Acronyms (ISS)
Home Page Web Address, Glossary, 1
ACTIVE by Custodial Package Option, 9-2
Alerts, 13-1
Application Workload, 6-4
Archiving, 7-1
Assumptions About the Reader, xiii
B
Background Job
RUM Background Driver Scheduling Frequency, 2-1, 2-2, 2-3, 4-1, 6-5, 7-1
C
Callable Routines, 8-1
Callout Boxes, xii
Capacity Management
Menu, 2-3, 6-1
Capacity Planning
Home Page Web Address, xiii
National Database, 1-1, 5-1, 13-1
Projections Home Page Web Address, 1-1
Statistics Home Page Web Address, 1-1
Capacity Planning Patches
KMPD\*1.0\*1, 9-1
Collecting RUM Data, 2-2, 2-3
Collection Global
KMPTMP("KMPR"), 1-1, 2-1, 2-2, 2-3, 4-1, 4-2, 5-1, 6-2, 6-5, 7-1
XTMP("KMPR") Collection Global, 4-1, 5-2
Contents, v
Custodial Package Menu, 9-2
D
Data Dictionary
Data Dictionary Utilities Menu, xii
Listings, xii
Databases
Capacity Planning National Database, 1-1, 5-1, 13-1
DBA Approvals and Integration Agreements, 9-2
DBA IA CUSTODIAL MENU, 9-2
DBA IA CUSTODIAL Option, 9-2
DBA IA INQUIRY Option, 9-2
DBA IA ISC Menu, 9-2
DBA IA SUBSCRIBER MENU, 9-2
DBA IA SUBSCRIBER Option, 9-2
DBA Menu, 9-2
Dependencies
Options, 10-1
Documentation
Revisions, iii
Symbols, xi
DSM for OpenVMS, 9-1
E
Electronic Signatures, 13-1
EN^KMPRPN03 Routine, 6-1
Eve Menu, 2-3
EVS Anonymous Directories, xiv
Exemptions
SAC, 12-1
Exported Options, 6-1
External Relations, 9-1
F
Figures and Tables, vii
FileMan File Protection, 13-2
Files, 3-1
RESOURCE USAGE MONITOR (#8971.1), 1-1, 2-1, 2-2, 2-3, 3-1, 4-1, 5-1, 6-3, 6-5, 7-1, 13-2
Security, 13-2
G
Globals
Journaling, 4-2
KMPR, 2-1
KMPR(8971.1, 3-1
KMPTMP("KMPR"), 1-1, 2-1, 2-2, 2-3, 4-1, 4-2, 5-1, 6-2, 6-5, 7-1
Protection, 4-2
Translation, 4-1
Translation, Journaling, and Protection, 4-1
XTMP("KMPR") Collection Global, 4-1, 5-2
Glossary, 1
Glossary (ISS)
Home Page Web Address, Glossary, 1
Graphs, Workload
All Nodes, 6-3
Single Node, 6-3
H
Help
At Prompts, xii
Online, xii
HL7 Patches
HL\*1.6\*103, 9-1
Home Pages
Adobe Acrobat Quick Guide Web Address, xiv
Adobe Web Address, xiii
Capacity Planning Home Page Web Address, xiii
Capacity Planning Projections Home Page Web Address, 1-1
Capacity Planning Statistics Home Page Web Address, 1-1
ISS Acronyms Home Page Web Address, Glossary, 1
ISS Glossary Home Page Web Address, Glossary, 1
VHA OI HSD&D Home Page Web Address, xiii
VistA Documentation Library (VDL) Home Page Web Address, xiv
How to
Obtain Technical Information Online, xii
Use this Manual, xi
I
Implementation, 2-1
Implementation and Maintenance, 2-1
Inquire Option, 9-2
Integration Agreements, 9-2
Menu Option, 9-2
Integration Agreements Menu Option, 9-2
Interfacing, 13-1
Internal Relations, 10-1
Introduction, 1-1
ISS Acronyms
Home Page Web Address, Glossary, 1
ISS Glossary
Home Page Web Address, Glossary, 1
J
Journaling, 4-2
K
Kernel Patches
XU\*8\*107, 9-1
XU\*8.0\*107, 9-1, 10-2, 13-1
XU\*8.0\*186, 5-1, 9-1, 10-2, 13-1
Keys, 13-1
KMP-CAPMAN Mail Group, 13-1
KMPR BACKGROUND DRIVER Option, 1-1, 2-1, 2-2, 2-3, 4-1, 5-1, 5-2, 6-2, 6-5, 7-1, 10-1
KMPR Global, 2-1
KMPR GRAPH ALL NODES Option, 5-1, 6-1, 6-3
KMPR GRAPH HOURLY SINGLE NODE Option, 5-1, 6-1, 6-3
KMPR MANAGER MENU, 10-1
KMPR PRINT HOURLY OCCURRENCE Option, 5-1, 6-1, 6-4
KMPR PRINT NODE PERCENT Option, 5-1, 6-1, 6-4
KMPR PRINT OPTION DATA Option, 5-1, 6-1, 6-4
KMPR REPORTS MENU, 6-1, 6-3
KMPR RUM MANAGER MENU, 2-3, 6-1, 6-2
KMPR START COLLECTION Option, 2-2, 2-3, 6-1, 6-2
KMPR STATUS COLLECTION Option, 2-2, 2-3, 6-1, 6-2
KMPR STOP COLLECTION Option, 6-1, 6-2
KMPR(8971.1 Global, 3-1
KMPRBD01 Routine, 5-1, 6-5
KMPRBD02 Routine, 5-1
KMPRBD03 Routine, 5-1
KMPRBD04 Routine, 5-1
KMPRENV Routine, 5-1
KMPRP1 Routine, 5-1, 6-1
KMPRP2 Routine, 5-1, 6-1
KMPRPG01 Routine, 5-1, 6-1
KMPRPG02 Routine, 5-1, 6-1
KMPRPN03 Routine, 5-1
KMPRPOST Routine, 5-2
KMPRSS Routine, 5-2, 6-1
KMPRUTL Routine, 5-2
KMPRUTL1 Routine, 5-2
KMPRUTL2 Routine, 5-2
KMPRUTL3 Routine, 5-2
KMPTMP("KMPR") Global, 1-1, 2-1, 2-2, 2-3, 4-1, 4-2, 5-1, 6-2, 6-5, 7-1
L
List File Attributes Option, xii
M
Mail Groups
KMP-CAPMAN, 13-1
Mail Groups and Alerts, 13-1
Maintenance, 2-3
Menu/Option Assignment, 6-2
Menus
Assignment, 6-2
Capacity Management, 2-3, 6-1
Custodial Package Menu, 9-2
Data Dictionary Utilities, xii
DBA, 9-2
DBA IA CUSTODIAL MENU, 9-2
DBA IA ISC, 9-2
DBA IA SUBSCRIBER MENU, 9-2
DBA Option, 9-2
Eve, 2-3
Integration Agreements Menu, 9-2
KMPR MANAGER MENU, 10-1
KMPR REPORTS MENU, 6-1, 6-3
KMPR RUM MANAGER MENU, 2-3, 6-1, 6-2
RUM Manager Menu, 2-3, 6-1, 10-1
RUM Reports, 6-1, 6-3
Subscriber Package Menu, 9-2
Taskman Management, 2-2, 2-3, 6-5, 10-1
XTCM MAIN, 2-3, 6-1, 6-2
XUTM MGR, 2-2, 2-3, 6-5, 10-1
N
Namespace, 10-2
National Database
Capacity Planning, 1-1, 5-1, 13-1
O
Obtain Technical Information Online, How to, xii
Obtaining Data Dictionary Listings, xii
Official Policies, 13-2
Online
Documentation, xii
Help Frames, xii
Option Workload, 6-4
Option/Task Workload, 6-4
Options
ACTIVE by Custodial Package, 9-2
Assignment, 6-2
by Date for Single Node (Graph), 6-1
Capacity Management, 2-3, 6-1
Custodial Package Menu, 9-2
DBA, 9-2
DBA IA CUSTODIAL, 9-2
DBA IA CUSTODIAL MENU, 9-2
DBA IA INQUIRY, 9-2
DBA IA ISC, 9-2
DBA IA SUBSCRIBER MENU, 9-2
DBA IA SUBSCRIBER Option, 9-2
DBA Option, 9-2
Dependencies, 10-1
Eve, 2-3
Exported, 6-1
With Parents, 6-1
Without Parents, 6-5
Inquire, 9-2
Integration Agreements Menu, 9-2
KMPR BACKGROUND DRIVER, 1-1, 2-1, 2-2, 2-3, 4-1, 5-1, 5-2, 6-2, 6-5, 7-1, 10-1
KMPR GRAPH ALL NODES, 5-1, 6-1, 6-3
KMPR GRAPH HOURLY SINGLE NODE Option, 5-1
KMPR MANAGER MENU, 10-1
KMPR PRINT HOURLY OCCURRENCE, 5-1, 6-1, 6-4
KMPR PRINT NODE PERCENT, 5-1, 6-1, 6-4
KMPR PRINT OPTION DATA, 5-1, 6-1, 6-4
KMPR REPORTS MENU, 6-1, 6-3
KMPR RUM MANAGER MENU, 2-3, 6-1, 6-2
KMPR START COLLECTION, 2-2, 2-3, 6-1, 6-2
KMPR STATUS COLLECTION, 2-2, 2-3, 6-1, 6-2
KMPR STOP COLLECTION, 6-1, 6-2
List File Attributes, xii
Package Resource Usage, 5-1, 6-1, 6-4
PH HOURLY SINGLE NODE, 6-1, 6-3
Print ACTIVE by Subscribing Package, 9-2
Print Hourly Occurrence Distribution, 5-1, 6-1, 6-4
Routine called by the RUM Data for All Nodes (Graph) Option, 5-1
RUM Background Driver, 1-1, 2-1, 2-2, 2-3, 4-1, 5-2, 6-2, 6-5, 7-1, 10-1
RUM Data by Date for Single Node (Graph), 6-3
RUM Data for All Nodes (Graph), 6-1, 6-3
RUM Data for an Option, 5-1, 6-1, 6-4
RUM Data for Single Node (Graph), 5-1
RUM Manager Menu, 2-3, 6-1, 10-1
RUM Reports, 6-1, 6-3
Schedule/Unschedule Options, 2-2, 2-3, 6-5, 10-1
Single, 6-5
Start RUM Collection, 2-2, 2-3, 6-1, 6-2
Status of RUM Collection, 2-2, 2-3, 6-1, 6-2
Stop RUM Collection, 6-1, 6-2
Subscriber Package Menu, 9-2
Taskman Management, 2-2, 2-3, 6-5, 10-1
*With* Parents, 6-1
*Without* Parents, 6-5
XTCM MAIN, 2-3, 6-1, 6-2
XUTM MGR, 2-2, 2-3, 6-5, 10-1
XUTM SCHEDULE, 2-2, 2-3, 6-5, 10-1
Orientation, xi
P
Package Resource Usage Option, 5-1, 6-1, 6-4
Patches
HL\*1.6\*103, 9-1
KMPD\*1.0\*1, 9-1
Revisions, iv
XU\*8\*107, 9-1
XU\*8.0\*107, 9-1, 10-2, 13-1
XU\*8.0\*186, 5-1, 9-1, 10-2, 13-1
Policies, Official, 13-2
Print ACTIVE by Subscribing Package Option, 9-2
Print Hourly Occurrence Distribution Option, 5-1, 6-1, 6-4
Protection, 4-2
Protocol Workload, 6-4
Protocols, 6-5
Purging, 7-1
Q
Question Mark Help, xii
R
Reader, Assumptions About the, xiii
Reference Materials, xiii
Relations
External, 9-1
Internal, 10-1
Relationship of RUM Software with
CM Tools V. 1.0, 10-1
Kernel V. 8.0, 10-2
VistA, 10-1
VistA HL7 V. 1.6, 10-1
Remote Systems, 13-1
Reports
Package Resource Usage, 5-1, 6-4
Print Hourly Occurrence Distribution, 5-1, 6-4
Routine called by the RUM Data for All Nodes (Graph) Option, 5-1
RUM Data by Date for Single Node (Graph), 6-3
RUM Data for All Nodes (Graph), 6-3
RUM Data for an Option, 5-1, 6-4
RUM Data for Single Node (Graph), 5-1
RUM Reports, 6-3
RESOURCE USAGE MONITOR File (#8971.1), 1-1, 2-1, 2-2, 2-3, 3-1, 4-1, 5-1, 6-3, 6-5, 7-1, 13-2
Revision History, iii
Documentation, iii
Patches, iv
Routine called by the RUM Data for All Nodes (Graph) Option, 5-1
Routines
%ZOSVKR, 9-1, 10-2, 13-1
Callable, 8-1
EN^KMPRPN03, 6-1
KMPRBD01, 5-1, 6-5
KMPRBD02, 5-1
KMPRBD03, 5-1
KMPRBD04, 5-1
KMPRENV, 5-1
KMPRP1, 5-1, 6-1
KMPRP2, 5-1, 6-1
KMPRPG01, 5-1, 6-1
KMPRPG02, 5-1, 6-1
KMPRPN03, 5-1
KMPRPOST, 5-2
KMPRSS, 5-2, 6-1
KMPRUTL, 5-2
KMPRUTL1, 5-2
KMPRUTL2, 5-2
KMPRUTL3, 5-2
List, 5-1
RPC Workload, 6-4
RUM Background Driver Option, 1-1, 2-1, 2-2, 2-3, 4-1, 5-2, 6-2, 6-5, 7-1, 10-1
RUM Data by Date for Single Node (Graph) Option, 6-1, 6-3
RUM Data for All Nodes (Graph) Option, 6-1, 6-3
RUM Data for an Option Option, 5-1, 6-1, 6-4
RUM Data for Single Node (Graph) Option, 5-1
RUM Manager Menu, 2-3, 6-1, 10-1
RUM Reports Menu, 6-1, 6-3
S
SAC Exemptions, 12-1
Schedule/Unschedule Options Option, 2-2, 2-3, 6-5, 10-1
Security, 13-1
Files, 13-2
Keys, 13-1
Security Management, 13-1
Signatures, Electronic, 13-1
Single Options, 6-5
Software Product Security, 13-1
Software-wide and Key Variables, 11-1
Start RUM Collection Option, 2-2, 2-3, 6-1, 6-2
Status of RUM Collection Option, 2-2, 2-3, 6-1, 6-2
Stop RUM Collection Option, 6-1, 6-2
Subscriber Package Menu Option, 9-2
Symbols Found in the Documentation, xi
T
Tables and Figures, vii
Taskman Management Menu, 2-2, 2-3, 6-5, 10-1
Templates, 3-1
Translation, 4-1
U
URLs
Adobe Acrobat Quick Guide Web Address, xiv
Adobe Home Page Web Address, xiii
Using
Adobe Acrobat Reader, xiii
V
VA FileMan File Protection, 13-2
Variables
Key, 11-1
Software-wide, 11-1
VHA OI HSD&D Home Page Web Address, xiii
VistA Documentation Library (VDL)
Home Page Web Address, xiv
VistA Software Requirements, 9-1
W
Web Pages
Adobe Acrobat Quick Guide Web Address, xiv
Adobe Home Page Web Address, xiii
Capacity Planning Home Page Web Address, xiii
Capacity Planning Projections Home Page Web Address, 1-1
Capacity Planning Statistics Home Page Web Address, 1-1
ISS Acronyms Home Page Web Address, Glossary, 1
ISS Glossary Home Page Web Address, Glossary, 1
VHA OI HSD&D Home Page Web Address, xiii
VistA Documentation Library (VDL) Home Page Web Address, xiv
Workload
All Nodes, 6-3
Data, 1-1
Protocol, 6-4
RPC, 6-4
Single Node, 6-3
Trends, 1-2
VistA Applications, 6-4
VistA Options, 1-1, 1-2, 2-2, 2-3, 3-1, 5-2, 6-2, 6-3, 6-4
VistA Options/Tasks, 6-4
X
XTCM MAIN Menu, 2-3, 6-1, 6-2
XTMP("KMPR") Collection Global, 4-1, 5-2
XUTM MGR Menu, 2-2, 2-3, 6-5, 10-1
XUTM SCHEDULE Option, 2-2, 2-3, 6-5, 10-1
Z
ZOSVKR Routine, 9-1, 10-2, 13-1
