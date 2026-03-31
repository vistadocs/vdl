---
title: KMPR Version 2 User Manual
doc_type: UM
doc_label: User Manual
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
menu_options: 11
description: The Resource Usage Monitor (RUM) software is intended for use by Information Resource Management (IRM) staff responsible for the capacity planning functions at their site. The RUM software allows a site to review system and Veterans Health Information Systems and Technology Architecture (VistA) opti
audience: 
keywords: 
  - background
  - kmpr
  - collection
  - driver
  - table
  - class
  - span
  - resource
  - time
  - usage
page_count: 0
word_count: 8607
section_count: 4
table_count: 51
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Resource_Usage_Mon/kmpr2_0um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Resource_Usage_Mon/kmpr2_0um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=130"
---

![](kmpr-version-2-user-manual/001.png)

RESOURCE USAGE MONITOR (RUM)USER MANUAL

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

<span id="_Toc56823239" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
- [Contents](#contents)
  - [Acknowledgements](#acknowledgements)
    - [## Orientation](#orientation)
- [Introduction](#introduction)
- [# RUM Software Overview and Use](#rum-software-overview-and-use)
    - [Functional Description](#functional-description)
    - [Data Collection Process](#data-collection-process)
    - [Statistics and Projections](#statistics-and-projections)
    - [Software Management](#software-management)
- [# RUM Options](#rum-options)
    - [<table>](#table)
  - [Glossary](#glossary)
- [## Index](#index)
Figures and Tables

## Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Capacity Planning (CP) Services' Resource Usage Monitor Project Team consists of the following Development and Infrastructure Service (DaIS) personnel:
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
| ![](kmpr-version-2-user-manual/002.png) | Used to inform the reader of general information including references to additional reading material. |
| ![](kmpr-version-2-user-manual/003.png)                                                              | Used to caution the reader to take special notice of critical information.                            |
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
| ![](kmpr-version-2-user-manual/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |
- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field and file names, and security keys (e.g., the XUPROGMODE key).
How to Obtain Technical Information Online
Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.
|                                                                                                                |                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/005.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. Please refer to the *Resource Usage Monitor (RUM) Technical Manual* for further information. |
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
| ![](kmpr-version-2-user-manual/006.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |
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
- *Resource Usage Monitor (RUM) User Manual* (this manual)
- *Resource Usage Monitor (RUM) Technical Manual*
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
<td>![](kmpr-version-2-user-manual/007.png)</td>
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
- REDACTED OIFO REDACTED
- Salt Lake City OIFO REDACTED
- Preferred Method REDACTED
> This method transmits the files from the first available FTP server.
|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/008.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software is intended for use by Information Resource Management (IRM) staff responsible for the capacity planning functions at their site. The RUM software allows a site to review system and Veterans Health Information Systems and Technology Architecture (VistA) option workload information.

The RUM software is strongly dependent on the site to schedule and run the background task on a regular basis. Menus and options are provided locally at the site to allow IRM staff to accomplish and monitor this task.

The collection task obtains system and VistA option information from the site and automatically transfers this data via network mail (i.e., VistA MailMan) to the Capacity Planning National Database.

The Veterans Health Administration (VHA) developed the RUM software in order to obtain more accurate information regarding the current and future system and VistA option workload at VA sites (e.g., VA Medical Centers \[VAMCs\]).

The purpose of this manual is to provide information about the Resource Usage Monitor (RUM) software. This manual defines the use of this software as a resource to IRM staff responsible for capacity planning functions at the site. It also highlights the use of the options that are available at the site.

# # RUM Software Overview and Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Functional Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software application provides fully automated support tools developed by Capacity Planning Services. It entails the daily capture of system and VistA option workload information from participating sites. This workload data is then summarized on a weekly basis and is automatically transferred, via network mail (i.e., VistA MailMan) to the Capacity Planning National Database. The site also receives a summary of the system workload data in the form of an electronic turn-around message.

|                                                                                                                |                                                                             |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/009.png) | For sample site e-mail message, please refer to Figure 2‑1 in this chapter. |

The IRM staff utilizes the options that are available at the site to manage the RUM software. IRM staff responsible for capacity planning tasks at the site can use these options to review system workload trends. Additionally, the IRM staff can review specific workload information for any given VistA option.

|                                                                                                                |                                                                                                   |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/010.png) | For more information on the RUM options, please refer to Chapter 3 "RUM Options," in this manual. |

The current version of the software is compatible with all current operating system platforms at VA sites and has minimal impact on IRM support staff.

### Data Collection Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installing the RUM software creates the collection process mechanism and other necessary components of the software. The fully automated data collection mechanism entails capturing all system and VistA option workload specifics at the site into a temporary ^KMPTMP("KMPR") collection global. The collection mechanism is continuously monitoring each process on the system while trapping system and VistA option workload data.

On a nightly basis, the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] moves the data within the ^KMPTMP("KMPR") collection global to the RESOURCE USAGE MONITOR file (#8971.1) and the temporary data within the ^KMPTMP("KMPR") global is purged.

|                                                                                                                |                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/011.png) | For more information on the RUM Background Driver option \[KMPR BACKGROUND DRIVER\], please refer to the "RUM Background Driver" topic in Chapter 3 "RUM Options," in this manual. |

### Statistics and Projections

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Every Sunday night, the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] monitors the RESOURCE USAGE MONITOR file to ensure that only a maximum of three weeks’ worth of data is maintained at the site.

Also, each Sunday night, the RUM Background Driver option automatically compresses the information contained within the RESOURCE USAGE MONITOR file (#8971.1) into weekly statistics. These weekly statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes.

The data is also available on Capacity Planning (CP) Services' Web site at the following Web addresses:

- Statistics—Provides statistics for each listed site:

> [REDACTED](http://vista.med.va.gov/capman/Statistics/Default.htm)

- Projections—Provides data trends for each listed site:

> [REDACTED](http://vista.med.va.gov/capman/TrendSetter/Default.htm)

### Software Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Resource Usage Monitor (RUM) software is managed by IRM staff through the RUM Manager Menu \[KMPR RUM MANAGER MENU\], which is located under the Capacity Management menu \[XTCM MAIN\]. The XTCM MAIN menu is found under the Eve menu and should be assigned to IRM staff member(s) who support(s) this software and other capacity management tasks.

This software utilizes the KMP-CAPMAN mail group, which can be edited with the Capacity Management Mail Group Edit option \[KMP MAIL GROUP EDIT\] option, which is located under the Capacity Management menu \[XTCM MAIN\]

|                                                                                                                |                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/012.png) | For more information on RUM software management and maintenance, please refer to the *Resource Usage Monitor (RUM) Technical Manual*. |

In addition to the summary workload data automatically transferred to the Capacity Planning National Database on a weekly basis, the site also receives a summary of the system workload data in the form of an electronic turn-around message, as shown below:

Subj: REDACTED.MED.VA.GOV (06-01-2003) RUM Report \[#7354404\] 06/10/03@10:23

53 lines

From: RUM NATIONAL DATABASE SERVER In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------------

\* RESOURCE USAGE MONITOR \*

CPU Workload Activity Report

Monday - Friday (8 a.m. - 5 p.m.)

M Commands/sec

Node Name 05-11-2003 05-18-2003 05-25-2003 06-01-2003

--------- ---------- ---------- ---------- ----------

578A01 95,911 111,802 117,809 119,509

578A02 83,865 113,740 111,005 117,521

578A03 101,470 130,290 147,895 180,654

578A04 21,154 7,296 3,904 4,292

578A05 23,580 12,156 22,511 5,754

578A06 28,266 25,384 9,821 11,323

578A07 14,006 12,127 6,963 8,879

---------- ---------- ---------- ----------

368,252 412,795 419,908 447,932

M Commands - A system workload data element that gives the number of

distinct commands that have been executed while executing

M routine code.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Disk Workload Activity Report

Monday - Friday (8 a.m. - 5 p.m.)

Glo References/sec

Node Name 05-11-2003 05-18-2003 05-25-2003 06-01-2003

--------- ---------- ---------- ---------- ----------

578A01 14,745 17,537 18,458 18,343

578A02 12,872 17,598 16,999 18,073

578A03 13,925 14,735 18,398 24,365

578A04 2,615 788 251 2,520

578A05 1,434 1,634 2,721 2,677

578A06 3,960 3,594 1,145 3,465

578A07 1,666 1,397 670 3,034

---------- ---------- ---------- ----------

51,217 57,283 58,642 72,477

Glo References - A system workload data element that gives the number of

times that a global variable name has been called because

of M routine code execution.

\*\*\*\*\*

Additional RUM Reports are available on the Capacity Planning

Web Page at http://vista.med.va.gov/capman/default.htm Click on

the 'Statistics' and 'Projections' left-hand links.

<span id="_Ref43690700" class="anchor"></span>Figure 2‑1: Sample MailMan message showing summary workload data at a site

# # RUM Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This chapter discusses the Resource Usage Monitor (RUM) options.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="rum-manager-menu" class="unnumbered">RUM Manager Menu</h3></td>
<td><strong>[KMPR RUM MANAGER MENU]</strong></td>
</tr>
</tbody>
</table>

The RUM Manager Menu \[KMPR RUM MANAGER MENU\] is located under the Capacity Management menu \[XTCM MAIN\], as shown below:

Select Operations Management Option: cm\<Enter\> Capacity Management

RUM RUM Manager Menu ...

TLS CM Tools Manager Menu ...

VPM VAX/ALPHA Capacity Management ...

Move Host File to Mailman

Response Time Log Menu ...

Select Capacity Management Option: rum\<Enter\> RUM Manager Menu

<span id="_Toc56823242" class="anchor"></span>Figure 3‑1: Accessing the RUM Manager Menu

The RUM Manager Menu contains the following options:

\* Resource Usage Monitor 2.0 \*

STA Status of RUM Collection \[KMPR STATUS COLLECTION\]

STR Start RUM Collection \[KMPR START COLLECTION\]

STP Stop RUM Collection \[KMPR STOP COLLECTION\]

RPT RUM Reports ... \[KMPR REPORTS MENU\]

<span id="_Toc56823243" class="anchor"></span>Figure 3‑2: RUM Manager Menu options

Each of these options is discussed in greater detail in the topics that follow.

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="status-of-rum-collection" class="unnumbered">Status of RUM Collection</h4>
<p>(Synonym: <strong>STA</strong>)</p></td>
<td><strong>[KMPR STATUS COLLECTION]</strong></td>
</tr>
</tbody>
</table>

The Status of RUM Collection option \[KMPR STATUS COLLECTION\] displays the current status of the RUM collection routines. This option identifies the following information (see Figure 3‑4):

- STATUS—Indicates whether or not the RUM software is currently running and collecting data.
- RUM BACKGROUND DRIVER—Indicates the option name of the RUM Background Driver \[KMPR BACKGROUND DRIVER\].
- QUEUED TO RUN AT—Indicates the date that the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is scheduled to first run at the site *and* the regularly scheduled time when the RUM Background Driver option should run at a site. The job will run at this scheduled time depending on the Rescheduling Frequency indicated.

|                                                                                                                |                                                                                                                                                                                                                                        |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/013.png) | The installation of the RUM software creates and sets this field automatically. It does the same thing as TaskMan's Schedule/Unschedule Option, which saves the installer the job of having to set up the Background Driver job later. |

- RESCHEDULING FREQUENCY—Indicates the frequency at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is run.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-user-manual/014.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the t^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

- TASK ID—This is the TaskMan task ID scheduled to run the Background Driver job.
- QUEUED BY—This is the person who schedules the Background Driver job to run via TaskMan.

|                                                                                                                |                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/015.png) | The installation of the RUM software creates and sets this field automatically. It sets it to the name of the person doing the installation of the RUM V. 2.0 software. |

- DAILY BACKGROUND LAST START—Indicates the most recent date and time at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] last daily run was started.
- DAILY BACKGROUND LAST STOP—Indicates the most recent date and time at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] last daily run was stopped.
- DAILY BACKGROUND TOTAL TIME—Indicates the total time at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] took in its most recent daily run.
- WEEKLY BACKGROUND LAST START—Indicates the most recent date and time at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] last weekly run was started.
- WEEKLY BACKGROUND LAST STOP—Indicates the most recent date and time at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] last weekly run was stopped.
- WEEKLY BACKGROUND TOTAL TIME—Indicates the total time at which the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] took in its most recent weekly run.
- TEMPORARY COLLECTION GLOBAL—Indicates if the ^KMPTMP("KMPR") temporary collection global is present or not on the system. When RUM is started the ^KMPTMP global will be populated with data.

The Status of RUM Collection option \[KMPR STATUS COLLECTION\] checks to ensure that the RUM Background Driver option \[KMPR BACKGROUND DRIVER \] has been scheduled to run every night (see Figure 3‑4).

If the Status of RUM Collection option determines that the background task has *not* been scheduled properly, the Status of RUM Collection option will ask to queue the background task to run every night at 1 a.m., as shown below:

Select Capacity Management Option: rum \<Enter\> RUM Manager Menu

\* Resource Usage Monitor 2.0 \*

STA Status of RUM Collection

STR Start RUM Collection

STP Stop RUM Collection

RPT RUM Reports ...

Select RUM Manager Menu Option: sta \<Enter\> Status of RUM Collection

RUM is on but the option 'KMPR BACKGROUND DRIVER' is not scheduled to run

Do you want me to queue this option to run every night at 1 a.m.? YES// \<Enter\>

<span id="_Toc56823244" class="anchor"></span>Figure 3‑3: Running the Status of RUM Collection option when the Background Driver job has *not* been scheduled

Selecting "YES" after the "Do you want me to queue this option to run every night at 1 a.m.? YES//" prompt will cause the KMPR BACKGROUND DRIVER option to be entered into the OPTION SCHEDULING file (#19.2) with a QUEUED TO RUN AT WHAT TIME field entry of "Tomorrow @ 1 a.m." and a RESCHEDULING FREQUENCY field entry of "1D" (i.e., every day), see Figure 3‑4.

|                                                                                                                |                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/016.png) | This option has been enhanced with the RUM V. 2.0 software. |

RUM Environment

Status......................: STOPPED!

RUM Background Driver.......: KMPR BACKGROUND DRIVER

QUEUED TO RUN AT............: Feb 20, 2003@01:00

RESCHEDULING FREQUENCY......: 1D

TASK ID.....................: 3052

QUEUED BY...................: KMPRUSER, ONE E (Active)

Daily Background last start.:

Daily Background last stop..:

Daily Background total time.:

Weekly Background last start:

Weekly Background last stop.:

Weekly Background total time:

Temporary collection global

^KMPTMP("KMPR").............: NOT Present

Enter RETURN to continue or '^' to exit: \<Enter\>

<span id="_Ref33413993" class="anchor"></span>Figure 3‑4: Sample output from the Status of RUM Collection option *before* starting the RUM collection

After pressing the Enter key the following report is displayed:

RUM Environment

\# of Oldest Recent

File Entries Date Date

------------------------------------ ------- ------ ------

8971.1 - RESOURCE USAGE MONITOR 0

RUM routines...........: No Problems

<span id="_Toc56823246" class="anchor"></span>Figure 3‑5: Sample output from the Status of RUM Collection option *before* starting the RUM collection (continued)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="start-rum-collection" class="unnumbered">Start RUM Collection</h4>
<p>(Synonym: <strong>STR</strong>)</p></td>
<td><strong>[KMPS START COLLECTION]</strong></td>
</tr>
</tbody>
</table>

The Start RUM Collection option \[KMPS START COLLECTION\] initiates the Resource Usage Monitor (RUM) collection routines to begin collecting system and VistA option workload data.

You should first invoke the Status of RUM Collection option \[KMPR STATUS COLLECTION\] to ensure that the RUM Background Driver option \[KMPR BACKGROUND DRIVER \] is scheduled to run every day at 1 a.m.

|                                                                                                                |                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/017.png) | For more information on the Status of RUM Collection option, please refer to the "Status of RUM Collection" topic in this chapter. |

If the RUM Background Driver option \[KMPR BACKGROUND DRIVER \] is *not* shown as being scheduled to run in the future, use TaskMan's Schedule/Unschedule Options option \[XUTM SCHEDULE\], located under the Taskman Management menu \[XUTM MGR\] to schedule the KMPR BACKGROUND DRIVER option, to run every day at 1 a.m.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-user-manual/018.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

To start the RUM collection, do the following:

Select RUM Manager Menu Option: str\<Enter\> Start RUM Collection

Do you want to start Resource Usage Monitor collection? YES// ?

Answer YES to start collecting Resource Usage Monitor data.

Do you want to start Resource Usage Monitor collection? YES// \<Enter\>

Resource Usage Monitor collection is started.

<span id="_Toc56823247" class="anchor"></span>Figure 3‑6: Running the Start RUM Collection option

When we do another status check after starting the RUM collection, we see the following:

RUM Environment

Status......................: Running

RUM Background Driver.......: KMPR BACKGROUND DRIVER

QUEUED TO RUN AT............: Feb 06, 2003@01:00

RESCHEDULING FREQUENCY......: 1D

TASK ID.....................: 3052

QUEUED BY...................: KMPRUSER, ONE E (Active)

Daily Background last start.:

Daily Background last stop..:

Daily Background total time.:

Weekly Background last start:

Weekly Background last stop.:

Weekly Background total time:

Temporary collection global

^KMPTMP("KMPR").............: NOT Present

Enter RETURN to continue or '^' to exit: \<Enter\>

<span id="_Toc56823248" class="anchor"></span>Figure 3‑7: Sample output from the Status of RUM Collection option *after* starting the RUM collection

As soon as users begin accessing menu options the ^KMPTMP("KMPR") global will be present. The Daily Background and Weekly Background data will be displayed as appropriate, as shown below:

RUM Environment

Status......................: Running

RUM Background Driver.......: KMPR BACKGROUND DRIVER

QUEUED TO RUN AT............: Feb 20, 2003@01:00

RESCHEDULING FREQUENCY......: 1D

TASK ID.....................: 3052

QUEUED BY...................: KMPRUSER, ONE E (Active)

Daily Background last start.: 2/19/03@01:00

Daily Background last stop..: 2/19/03@01:00

Daily Background total time.:

Weekly Background last start: 2/16/03@01:00:01

Weekly Background last stop.: 2/16/03@01:00:01

Weekly Background total time:

Temporary collection global

^KMPTMP("KMPR").............: Present

<span id="_Toc56823249" class="anchor"></span>Figure 3‑8: Sample output from the Status of RUM Collection option *after* running the RUM collection for several weeks

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="stop-rum-collection" class="unnumbered">Stop RUM Collection</h4>
<p>(Synonym: <strong>STP</strong>)</p></td>
<td><strong>[KMPR STOP COLLECTION]</strong></td>
</tr>
</tbody>
</table>

The Stop RUM Collection option \[KMPR STOP COLLECTION\] stops the Resource Usage Monitor (RUM) collection routines from collecting data.

|                                                                                                                |                                                                                   |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/019.png) | This option does *not* stop the RUM Background Driver \[KMPR BACKGROUND DRIVER\]. |

Select RUM Manager Menu Option: stp \<Enter\> Stop RUM Collection

Do you want to stop Resource Usage Monitor collection? YES// ?

Answer YES to stop collecting Resource Usage Monitor data.

Do you want to stop Resource Usage Monitor collection? YES// \<Enter\>

Resource Usage Monitor collection is stopped.

<span id="_Toc56823250" class="anchor"></span>Figure 3‑9: Running the Stop RUM Collection option

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h4 id="rum-reports" class="unnumbered">RUM Reports</h4>
<p>(Synonym: <strong>RPT</strong>)</p></td>
<td><strong>[KMPR REPORTS MENU]</strong></td>
</tr>
</tbody>
</table>

The RUM Reports menu option \[KMPR REPORTS MENU\] is available on the RUM Manager Menu, as shown below:

Select RUM Manager Menu Option: rpt \<Enter\> RUM Reports

GAN RUM Data for All Nodes (Graph)

GSN RUM Data by Date for Single Node (Graph)

PDO RUM Data for an Option

PHO Print Hourly Occurrence Distribution

PRU Package Resource Usage

Select RUM Reports Option:

<span id="_Toc56823251" class="anchor"></span>Figure 3‑10: Accessing the RUM Reports menu options

The RUM Reports menu \[KMPR REPORTS MENU\] contains various report options that generate report information from the system and VistA option workload statistics accumulated within the RESOURCE USAGE MONITOR file (#8971.1).

The RUM Reports menu contains the following options:

GAN RUM Data for All Nodes (Graph) \[KMPR GRAPH ALL NODES\]

GSN RUM Data by Date for Single Node (Graph) \[KMPR GRAPH HOURLY SINGLE NODE\]

PDO RUM Data for an Option \[KMPR PRINT OPTION DATA\]

PHO Print Hourly Occurrence Distribution \[KMPR PRINT HOURLY OCCURRENCE\]

PRU Package Resource Usage \[KMPR PRINT NODE PERCENT\]

<span id="_Toc56823252" class="anchor"></span>Figure 3‑11: RUM Reports menu options

Each of these options is discussed in greater detail in the topics that follow.

All of the report options except KMPR PRINT HOURLY OCCURRENCE provide information on the following workload data elements:

| Data Element | Description                                                                                                                                                                                  |
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CPU Time         | The amount of time that the processor has spent executing M routine code.                                                                                                                        |
| Elapsed Time     | The amount of actual time that has passed while executing M routine code.                                                                                                                        |
| M Commands       | The number of distinct commands that have been executed while executing M routine code.                                                                                                          |
| GLO References   | The number of times that a global variable name has been called because of M routine code execution.                                                                                             |
| DIO References   | The number of times that a disk access has been requested because of M routine code execution.                                                                                                   |
| BIO References   | The number of times that a buffered access has been called because of M routine code execution. Terminals and printers are normally considered to be a buffered device within the M environment. |
| Page Faults      | The number of times that a job had to use non-physical (i.e., paged) memory.                                                                                                                     |
| Occurrences      | A total measure of the number of VistA option executions.                                                                                                                                        |

<span id="_Ref42924562" class="anchor"></span>Table 3‑1: RUM report system workload data elements

|                                                                                                                |                                                                                                                                                                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/020.png) | For more information on the statistics and projections (trends) based on data obtained from these report options, please refer to the "Statistics and Projections" topic in Chapter 2, "RUM Software Overview and Use," in this manual. |

|                                                                                                                |                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/021.png) | Generating the reports can sometimes take a while. Users may wish to queue the printouts, when feasible. |

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rum-data-for-all-nodes-graph" class="unnumbered">RUM Data for All Nodes (Graph)</h5>
<p>(Synonym: <strong>GAN</strong>)</p></td>
<td><strong>[KMPR REPORTS MENU]</strong></td>
</tr>
</tbody>
</table>

The RUM Data for All Nodes (Graph) report option \[KMPR GRAPH ALL NODES\] displays a bar graph and totals of the selected system workload data element for *all* system nodes within a given date range.

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/022.png) | For more information on the system workload data elements, please refer to Table 3‑1 in this chapter. |

M Commands Workload

The following example shows the prompts and user responses for the RUM Data for All Nodes (Graph) report option for the M Commands data element:

Select RUM Reports Option: gan \<Enter\> RUM Data for All Nodes (Graph)

Data for All Nodes (Graph)

This option displays data in a graphical format. Please make

note that this output is intended for comparison/trends only,

and should not be used for detailed analysis.

Select one of the following:

1 CPU Time

2 Elapsed Time

3 M Commands

4 GLO References

5 DIO References

6 BIO References

7 Page Faults

8 Occurrences

Enter Key Data Element for Searching RUM Data: 3\<Enter\> M Commands

Start with Date: 11/8/98// \<Enter\> (NOV 08, 1998)

End with Date: 11/24/98// \<Enter\> (NOV 24, 1998)

compiling data for: 11/8/1998.....11/9/1998...........11/10/1998..........

11/11/1998.....11/12/1998...........11/13/1998..........

<span id="_Toc56823254" class="anchor"></span>Figure 3‑12: Running the RUM Data for All Nodes (Graph) report option—M Commands data element

The following is a sample report/graph generated for the M Commands data element for *all* system nodes at a site:

RUM Data for All Nodes

Node From Nov 08, 1998 to Nov 24, 1998

┌────┬────┬────┬────┬────┬────┬────┬────┬────┬────┬──┐

999A01 │ │ │ │ │ │ │ │ │ │ │ │\<0.00\>

│ │ │ │ │ │ │ │ │ │ │ │

999A02 │▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ │ │ │ │ │ │\<1.19\>

│ │ │ │ │ │ │ │ │ │ │ │

999A03 │▒▒▒▒▒▒▒▒▒▒▒▒ │ │ │ │ │ │ │ │ │\<0.54\>

│ │ │ │ │ │ │ │ │ │ │ │

999A04 │▒▒▒▒▒▒▒▒▒▒ │ │ │ │ │ │ │ │ │\<0.43\>

│ │ │ │ │ │ │ │ │ │ │ │

999A05 │▒▒▒▒▒▒▒▒▒▒ │ │ │ │ │ │ │ │ │\<0.41\>

│ │ │ │ │ │ │ │ │ │ │ │

999A06 │▒▒▒▒▒▒▒▒ │ │ │ │ │ │ │ │ │ │\<0.36\>

│ │ │ │ │ │ │ │ │ │ │ │

999A07 │▒▒▒▒▒▒▒▒▒▒▒ │ │ │ │ │ │ │ │ │\<0.46\>

├────┼────┼────┼────┼────┼────┼────┼────┼────┼────┼──┘

0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0 \<x10k\>

M Commands/per sec

Press \<RET\> to continue

<span id="_Toc56823255" class="anchor"></span>Figure 3‑13: Sample output from the RUM Data for All Nodes (Graph) report option—M Commands data element

The bar graph in this example gives a total amount of the M Commands per second for each system node from November 8, 1998 to November 24, 1998. For example, we see that there were 1.19 x 10K M commands per second for system node 999A02. That equates to 11.9K or 12,185.6 bytes per second during that time period.

|                                                                                                                |                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/023.png) | The granularity of the graphical output is representative of the actual workload amounts. |

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rum-data-by-date-for-single-node-graph" class="unnumbered">RUM Data by Date for Single Node (Graph)</h5>
<p>(Synonym: <strong>GSN</strong>)</p></td>
<td><strong>[KMPR GRAPH HOURLY SINGLE NODE]</strong></td>
</tr>
</tbody>
</table>

The RUM Data by Date for Single Node (Graph) report option \[KMPR GRAPH HOURLY SINGLE NODE\] displays a bar graph and totals of the selected system workload data element for a *single* node for each day within a given date range.

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/024.png) | For more information on the system workload data elements, please refer to Table 3‑1 in this chapter. |

M Commands Workload

The following example shows the prompts and user responses for the RUM Data by Date for Single Node (Graph) report option for the M Commands data element:

Select RUM Reports Option: gsn \<Enter\> RUM Data by Date for Single Node (Graph)

RUM Data by Date for Single Node

This option displays data in a graphical format. Please make

note that this output is intended for comparison/trends only,

and should not be used for detailed analysis.

Select one of the following:

1 CPU Time

2 Elapsed Time

3 M Commands

4 GLO References

5 DIO References

6 BIO References

7 Page Faults

8 Occurrences

Enter Key Data Element for Searching RUM Data: 3\<Enter\> M Commands

Start with Date: 11/8/98// \<Enter\> (NOV 08, 1998)

End with Date: 11/24/98// \<Enter\> (NOV 24, 1998)

Select one of the following:

1 999A01

2 999A02

3 999A03

4 999A04

5 999A05

6 999A06

7 999A07

Select Node: 2\<Enter\> 999A02

compiling data for: 11/8/1998.....11/9/1998...........11/10/1998..........

11/11/1998.....11/12/1998...........11/13/1998..........

<span id="_Toc56823256" class="anchor"></span>Figure 3‑14: Running the RUM Data by Date for Single Node (Graph) report option—M Commands data element

The following is a sample report/graph generated for the M Commands data element for a *single* system node at a site:

RUM Data by Date for Node '999A07'

From Nov 08, 1998 to Nov 24, 1998

M Commands/per sec \<x10k\>

1.0\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

0.9\_│\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_▒\_\_\_\_\_\_\_\_\_\_\_\_\_\_│

0.8\_│\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_▒\_\_\_▒\_\_\_\_\_\_\_\_\_\_│

0.7\_│\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_▒\_\_\_▒\_\_\_\_\_\_\_\_\_\_│

0.6\_│\_\_\_\_▒\_\_\_▒\_\_\_\_\_\_\_▒\_▒\_▒\_▒\_\_\_\_\_\_\_▒\_▒│

0.5\_│\_\_▒\_▒\_\_\_▒\_▒\_\_\_\_\_▒\_▒\_▒\_▒\_▒\_\_\_\_\_▒\_▒│

0.4\_│\_\_▒\_▒\_\_\_▒\_▒\_\_\_\_\_▒\_▒\_▒\_▒\_▒\_\_\_\_\_▒\_▒│

0.3\_│\_\_▒\_▒\_\_\_▒\_▒\_\_\_\_\_▒\_▒\_▒\_▒\_▒\_\_\_\_\_▒\_▒│

0.2\_│\_\_▒\_▒\_\_\_▒\_▒\_\_\_\_\_▒\_▒\_▒\_▒\_▒\_\_\_\_\_▒\_▒│

0.1\_│\_\_▒\_▒\_▒\_▒\_▒\_\_\_\_\_▒\_▒\_▒\_▒\_▒\_\_\_\_\_▒\_▒│

0.0\_│▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒\_▒│

D 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

a 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

t / / / / / / / / / / / / / / / / /

e 8 9 1 1 1 1 1 1 1 1 1 1 2 2 2 2 2

/ / 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4

9 9 / / / / / / / / / / / / / / /

8 8 9 9 9 9 9 9 9 9 9 9 9 9 9 9 9

8 8 8 8 8 8 8 8 8 8 8 8 8 8 8

Press \<RET\> to continue

<span id="_Toc56823257" class="anchor"></span>Figure 3‑15: Sample output from the RUM Data by Date for Single Node (Graph) report option—M Commands data element

The bar graph in this example gives a total amount of the M Commands per second for the 999A07 system node for each day from November 8, 1998 to November 24, 1998. For example, we see that there were 1.0 x 10K M commands per second for system node 999A07 on November 17, 1998. That equates to 10K or 10,240 bytes per second on that day.

|                                                                                                                |                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/025.png) | The granularity of the graphical output is representative of the actual workload amounts. |

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="rum-data-for-an-option" class="unnumbered">RUM Data for an Option</h5>
<p>(Synonym: <strong>PDO</strong>)</p></td>
<td><strong>[KMPR PRINT OPTION DATA]</strong></td>
</tr>
</tbody>
</table>

The RUM Data for an Option report option \[KMPR PRINT OPTION DATA\] lists all the system workload data element statistics within a given date range for any of the following:

- Option
- Protocol
- Remote Procedure Call (RPC)

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/026.png) | For more information on the system workload data elements, please refer to Table 3‑1 in this chapter. |

Option Workload

The Option workload report output from the RUM Data for an Option report option lists the occurrence of the data element statistics for a specified option, as well as the total amounts within a given date range.

The following example shows the prompts and user responses for the RUM Data for an Option report option for the data element statistics for the DG REGISTER PATIENT option at a site:

Select RUM Reports Option: PDO \<Enter\> RUM Data for an Option

RUM Data by Option/Protocol/RPC

Select one of the following:

1 Option

2 Protocol

3 RPC

Enter response: 1 \<Enter\> Option

Select Option: ?

Answer with OPTION NAME, or ROUTINE

Do you want the entire 16078-Entry OPTION List? N \<Enter\> (No)

Select Option: DG REGISTER PATIENT \<Enter\> Register a Patient run routine REGISTRATION

Start with Date: 1/26/03// \<Enter\> (JAN 26, 2003)

End with Date: 2/11/03// \<Enter\> (FEB 11, 2003)

Device: HOME// \<Enter\> TELNET DEVICE

...compiling data...

<span id="_Toc56823258" class="anchor"></span>Figure 3‑16: Running the RUM Data for an Option report option—Option workload

The following is a sample report of the Option workload data element statistics for the DG REGISTER PATIENT option at a site:

RUM Data for Option: DG REGISTER PATIENT

N. FLORIDA/S. GEORGIA HCS (573)

For Jan 26, 2003 to Feb 11, 2003

per Occurrence Totals

CPU Time................. 0.12 2,838.53

Elapsed Time............. 32.76 799,967.48

M Commands............... 12,413 303,102,961

GLO References........... 1,702 41,551,207

DIO References........... 81 1,975,130

BIO References........... 131 3,207,391

Page Faults.............. 0 1,666

Occurrences.............. 24,419

<span id="_Toc56823259" class="anchor"></span>Figure 3‑17: Sample report output from the RUM Data for an Option report option—Option workload

Protocol Workload

The Protocol workload report output from the RUM Data for an Option report option lists the occurrence of the data element statistics for a specified protocol, as well as the total amounts within a given date range.

The following example shows the prompts and user responses for the RUM Data for an Option report option for the OR EVSEND PS protocol workload at a site:

Select RUM Reports Option: PDO \<Enter\> RUM Data for an Option

RUM Data by Option/Protocol/RPC

Select one of the following:

1 Option

2 Protocol

3 RPC

Enter response: 2\<Enter\> Protocol

Select Protocol: OR EVSEND PS\<Enter\> OE/RR =\> PHARMACY MESSAGE EVENT

Start with Date: 1/26/03// \<Enter\> (JAN 26, 2003)

End with Date: 2/11/03// \<Enter\> (FEB 11, 2003)

Device: HOME// \<Enter\> TELNET DEVICE

...compiling data...

<span id="_Toc56823260" class="anchor"></span>Figure 3‑18: Running the RUM Data for an Option report option—Protocol workload

The following is a sample report of the Protocol workload data element statistics for the OR EVSEND PS protocol at a site:

RUM Data for Option: OR EVSEND PS

N. FLORIDA/S. GEORGIA HCS (573)

For Jan 26, 2003 to Feb 11, 2003

per Occurrence Totals

CPU Time................. 0.00 644.00

Elapsed Time............. 0.01 1,890.94

M Commands............... 326 52,374,584

GLO References........... 90 14,528,108

DIO References........... 0 36,194

BIO References........... 0 8

Page Faults.............. 0 0

Occurrences.............. 160,659

<span id="_Toc56823261" class="anchor"></span>Figure 3‑19: Sample report output from the RUM Data for an Option report option—Protocol workload

RPC Workload

The Remote Procedure Call (RPC) workload report output from the RUM Data for an Option report option lists the occurrence of the data element statistics for a specified RPC, as well as the total amounts within a given date range.

The following example shows the prompts and user responses for the RUM Data for an Option report option for the ORB DELETE ALERT RPC workload at a site:

Select RUM Reports Option: PDO \<Enter\> RUM Data for an Option

RUM Data by Option/Protocol/RPC

Select one of the following:

1 Option

2 Protocol

3 RPC

Enter response: 3 \<Enter\> RPC

Select RPC: ORB DELETE ALERT

Start with Date: 1/26/03// \<Enter\> (JAN 26, 2003)

End with Date: 2/11/03// \<Enter\> (FEB 11, 2003)

Device: HOME// \<Enter\> TELNET DEVICE

...compiling data...

<span id="_Toc56823262" class="anchor"></span>Figure 3‑20: Running the RUM Data for an Option report option—RPC workload

The following is a sample report of the RPC workload data element statistics for the ORB DELETE ALERT RPC at a site:

RUM Data for Option: ORB DELETE ALERT

N. FLORIDA/S. GEORGIA HCS (573)

For Jan 26, 2003 to Feb 11, 2003

per Occurrence Totals

CPU Time................. 0.01 448.97

Elapsed Time............. 0.09 6,167.11

M Commands............... 445 29,146,108

GLO References........... 73 4,809,557

DIO References........... 6 401,818

BIO References........... 0 6

Page Faults.............. 0 0

Occurrences.............. 65,440

<span id="_Toc56823263" class="anchor"></span>Figure 3‑21: Sample report output from the RUM Data for an Option report option—RPC workload

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="print-hourly-occurrence-distribution" class="unnumbered">Print Hourly Occurrence Distribution</h5>
<p>(Synonym: <strong>PHO</strong>)</p></td>
<td><strong>[KMPR PRINT HOURLY OCCURRENCE]</strong></td>
</tr>
</tbody>
</table>

The Print Hourly Occurrence Distribution report option \[KMPR PRINT HOURLY OCCURRENCE\] is new with the RUM V. 2.0 software. It lists the system workload hourly occurrence for any of the following:

- Option/Task
- Protocol
- Remote Procedure Call (RPC)

Option/Task Workload

The Option/Task workload report output from the Print Hourly Occurrence Distribution report option lists the hourly occurrence of the specified option or task by system node, as well as the total amounts and number of users for the given time period.

The following example shows the prompts and user responses for the Print Hourly Occurrence Distribution report option for the XMREAD option at a site:

Select RUM Reports Option: PHO \<Enter\> Print Hourly Occurrence Distribution

Hourly Occurrence Distribution

Select one of the following:

1 Option/Task

2 Protocol

3 RPC

Enter response: 1 \<Enter\> Option/Task

Select Option/Task: XMREAD \<Enter\> Read/Manage Messages run routine MAILMAN

Select DATE : (5/11/2003 - 5/30/2003): T-1

Device: HOME// \<Enter\> TELNET DEVICE

Compiling data................................................................

................................................................................

<span id="_Toc56823264" class="anchor"></span>Figure 3‑22: Running the Print Hourly Occurrence Distribution report option—Option/Task

The user can only pick a single date within the date range presented. The KMPRP2 routine determines the earliest and most recent dates in the RESOURCE USAGE MONITOR file (#8971.1) and displays it to the user.

The following is a sample report generated from the Option workload for the XMREAD option at a site:

N. FLORIDA/S. GEORGIA HCS (573)

Hourly Occurrence Distribution for XMREAD

For May 29, 2003

================================================================================

Hour A01 A02 A03 A04 Total Total

Occ User

================================================================================

00 2 3 1 6 12 10

01 0 2 3 7 12 11

02 3 1 4 6 14 13

03 2 1 2 2 7 7

04 0 4 10 1 15 11

05 3 5 3 1 12 12

06 12 24 8 21 65 48

07 47 58 12 65 182 156

08 131 146 47 165 489 358

09 99 112 24 126 361 249

10 70 94 23 110 297 211

11 103 116 30 90 339 240

12 85 83 18 58 244 170

Press RETURN to continue or '^' to exit: \<Enter\>

N. FLORIDA/S. GEORGIA HCS (573)

Hourly Occurrence Distribution for XMREAD

For May 29, 2003

================================================================================

Hour A01 A02 A03 A04 Total Total

Occ User

================================================================================

13 117 116 17 85 335 210

14 95 103 27 119 344 240

15 95 108 31 106 340 235

16 54 73 16 93 236 172

17 15 27 7 11 60 44

18 4 60 16 12 92 35

19 1 25 5 1 32 16

20 3 14 1 5 23 16

21 3 9 1 5 18 14

22 3 12 5 2 22 17

23 5 8 1 1 15 11

Press RETURN to continue:

<span id="_Toc56823265" class="anchor"></span>Figure 3‑23: Sample report output from the Print Hourly Occurrence Distribution report option—Option/Task workload

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h5 id="package-resource-usage" class="unnumbered">Package Resource Usage</h5>
<p>(Synonym: <strong>PRU</strong>)</p></td>
<td><strong>[KMPR PRINT NODE PERCENT]</strong></td>
</tr>
</tbody>
</table>

The Package Resource Usage report option \[KMPR PRINT NODE PERCENT\] lists the data element statistics for a specified VistA software application (package) namespace per system node within a given date range. The printout shows the system workload as a percent of the totals that the given software application namespace was running as either an option, protocol, Remote Procedure Call (RPC), or background task.

|                                                                                                                |                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/027.png) | For more information on the system workload data elements, please refer to Table 3‑1 in this chapter. |

Select RUM Reports Option: pru \<Enter\> Package Resource Usage

Package Resource Usage

This option will display the Package Resource Usage Monitor statistics.

The printout summarizes the statistics of the options, protocols and

tasks for a selected namespace as percentages.

Select Software Namespace (case sensitive): ?

This response can be free text.

Select Package Namespace (case sensitive): LR

Start with Date: 11/8/98// \<Enter\> (NOV 08, 1998)

End with Date: 11/24/98// \<Enter\> (NOV 24, 1998)

Device: HOME// \<Enter\> Telnet

...compiling data...11/8/1998.....11/9/1998...........11/10/1998..........

11/11/1998.....11/12/1998...........11/13/1998..........

<span id="_Toc56823266" class="anchor"></span>Figure 3‑24: Running the Package Resource Usage report option

Sample generated report of the data element statistics for the LR namespaced VistA application at a site. The report is split across several pages and the data is listed by node:

Package Resource Usage

MEDICAL CENTER

Node 999A01 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 0.0 0.0 0.0 0.0 0.0 100.0

Elapsed Time 0.0 0.0 0.0 0.0 0.0 100.0

M Commands 0.0 0.0 0.0 0.0 0.0 100.0

GLO References 0.0 0.0 0.0 0.0 0.0 100.0

DIO References 0.0 0.0 0.0 0.0 0.0 100.0

BIO References 0.0 0.0 0.0 0.0 0.0 100.0

Page Faults 0.0 0.0 0.0 0.0 0.0 100.0

Occurrences 0.0 0.0 0.0 0.0 0.0 100.0

Node 999A02 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 0.0 1.7 0.0 0.0 6.2 92.2

Elapsed Time 0.0 0.1 0.0 0.0 5.1 94.8

M Commands 0.0 1.4 0.0 0.0 5.3 93.3

GLO References 0.0 2.3 0.0 0.0 7.9 89.8

DIO References 0.0 0.3 0.0 0.0 4.5 95.1

BIO References 0.0 0.0 0.0 0.0 7.6 92.4

Page Faults 0.0 0.3 0.0 0.0 2.0 97.7

Occurrences 0.0 16.3 0.0 0.0 11.9 71.8

Node 999A03 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 0.0 1.2 0.0 0.0 8.2 90.6

Elapsed Time 0.0 0.0 0.0 0.0 4.1 95.8

M Commands 0.0 1.0 0.0 0.0 8.0 91.1

GLO References 0.0 1.5 0.0 0.0 9.8 88.7

DIO References 0.0 0.3 0.0 0.0 5.8 93.9

BIO References 0.0 0.0 0.0 0.0 7.3 92.7

Page Faults 0.0 0.1 0.0 0.0 1.4 98.5

Occurrences 0.0 13.0 0.0 0.0 9.4 77.6

Node 999A04 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 2.2 5.5 0.0 0.0 0.0 92.3

Elapsed Time 3.7 2.7 0.0 0.0 0.0 93.6

M Commands 1.5 5.2 0.0 0.0 0.0 93.3

GLO References 1.6 4.9 0.0 0.0 0.0 93.5

DIO References 3.3 2.9 0.0 0.0 0.0 93.8

BIO References 1.8 0.8 0.0 0.0 0.0 97.4

Page Faults 0.7 0.1 0.0 0.0 0.0 99.1

Occurrences 0.7 8.0 0.0 0.0 0.0 91.4

Node 999A05 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 2.5 2.7 0.0 0.0 0.0 94.8

Elapsed Time 2.5 1.1 0.0 0.0 0.0 96.4

M Commands 2.3 2.4 0.0 0.0 0.0 95.3

GLO References 2.2 2.4 0.0 0.0 0.0 95.4

DIO References 3.3 1.6 0.0 0.0 0.0 95.1

BIO References 1.3 0.3 0.0 0.0 0.0 98.4

Page Faults 0.5 0.0 0.0 0.0 0.0 99.4

Occurrences 0.4 4.6 0.0 0.0 0.0 95.0

Node 999A06 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 2.6 6.4 0.0 0.0 0.0 91.0

Elapsed Time 4.2 3.0 0.0 0.0 0.0 92.8

M Commands 2.0 6.0 0.0 0.0 0.0 92.0

GLO References 2.0 5.7 0.0 0.0 0.0 92.2

DIO References 4.2 3.5 0.0 0.0 0.0 92.3

BIO References 2.0 0.9 0.0 0.0 0.0 97.1

Page Faults 1.1 0.2 0.0 0.0 0.0 98.8

Occurrences 0.8 9.2 0.0 0.0 0.0 89.9

Node 999A07 from Nov 08, 1998 to Nov 24, 1998

'LR' Namespace

% % % % % All Other

Options Protocols RPC HL7 Tasks Packages

CPU Time 1.6 3.6 0.0 0.0 0.0 94.8

Elapsed Time 3.1 1.7 0.0 0.0 0.0 95.2

M Commands 1.1 3.3 0.0 0.0 0.0 95.6

GLO References 1.1 3.0 0.0 0.0 0.0 95.9

DIO References 2.8 2.1 0.0 0.0 0.0 95.1

BIO References 1.6 0.5 0.0 0.0 0.0 97.8

Page Faults 1.0 0.1 0.0 0.0 0.0 98.9

Occurrences 0.5 5.8 0.0 0.0 0.0 93.7

<span id="_Toc56823267" class="anchor"></span>Figure 3‑25: Sample report output from the Package Resource Usage option

### <table>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<colgroup>
<col style="width: 45%" />
<col style="width: 54%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="rum-background-driver" class="unnumbered">RUM Background Driver</h3></td>
<td><strong>[KMPR BACKGROUND DRIVER]</strong></td>
</tr>
</tbody>
</table>

On a nightly basis, the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] moves the data within the ^KMPTMP("KMPR") collection global to the RESOURCE USAGE MONITOR file (#8971.1) and the temporary data within the ^KMPTMP("KMPR") global is purged.

Every Sunday night, the RUM Background Driver option \[KMPR BACKGROUND DRIVER\] monitors the RESOURCE USAGE MONITOR file to ensure that only a maximum of three week’s worth of data is maintained at the site.

Also, each Sunday night, the RUM Background Driver option automatically compresses the information contained within the RESOURCE USAGE MONITOR file (#8971.1) into weekly statistics. These weekly statistics are converted into an electronic mail message that is automatically transferred via network mail (i.e., VistA MailMan) and merged into a Capacity Planning National Database where this data is used for evaluation purposes. The site also receives a summary of the system workload data in the form of an electronic turn-around message.

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/028.png) | For a sample of the electronic turn-around message, please refer to the "Software Management" topic in Chapter 2, "RUM Software Overview and Use," in this manual. |

The RUM Background Driver option \[KMPR BACKGROUND DRIVER\] is *not* assigned to any menu. This option is scheduled through TaskMan to start the Resource Usage Monitor (RUM) software's background driver routine.

This option should be (re)scheduled with TaskMan's Schedule/Unschedule Options \[XUTM SCHEDULE\] located under the Taskman Management menu \[XUTM MGR\], see Figure 3‑26.

|                                                                                                                |                                                                                                                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kmpr-version-2-user-manual/029.png) | The installation of the RUM software automatically sets the Background Driver job to run daily at 1:00 a.m. It does the same thing as TaskMan's Schedule/Unschedule Option, which saves the installer the job of having to set up the Background Driver job later. |

This option lets you set the following information (see Figure 3‑27 and Figure 3‑28):

- QUEUED TO RUN AT WHAT TIME—This is the date/time you want this option to be started by TaskMan. It should be scheduled to run every day at 1 a.m.
- DEVICE FOR QUEUED JOB OUTPUT—Only enter a DEVICE if the job needs an output device.
- QUEUED TO RUN ON VOLUME SET—This is the Volume set \[:node\] upon which you want the job to run.
- RESCHEDULING FREQUENCY—This is the frequency at which you want the job to run. For the RUM Background Driver, this should be set to "1D" so that it will run every day. If this field is left blank, then the job will run only once.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kmpr-version-2-user-manual/030.png)</td>
<td>Capacity Planning (CP) Services <em>strongly</em> recommends that the RUM Background Driver option [KMPR BACKGROUND DRIVER] be scheduled to run every day at 1 a.m., because this background driver is the main mechanism by which the ^KMPTMP("KMPR") temporary collection global is purged nightly and the RESOURCE USAGE MONITOR file (#8971.1) is trimmed (records deleted) to contain a maximum of 21 days of data every Sunday night.<br />
<br />
Modification of the frequency and time may have adverse effects on the size of the ^KMPTMP("KMPR") temporary collection global and on the number of entries within the RESOURCE USAGE MONITOR file.</td>
</tr>
</tbody>
</table>

The following examples show typical displays when using TaskMan's Schedule/Unschedule Options option:

Select Systems Manager Menu Option: taskman Management

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

Select Taskman Management Option: schedule/Unschedule Options

Select OPTION to schedule or reschedule: KMPR BACKGROUND DRIVER\<RET\> RUM Background Driver

...OK? Yes// \<Enter\> (Yes)

\(R\)

<span id="_Ref44298006" class="anchor"></span>Figure 3‑26: Running TaskMan's Schedule/Unschedule Options option to set up the RUM Background Driver

Edit Option Schedule

Option Name: KMPR BACKGROUND DRIVER

Menu Text: RUM Background Driver TASK ID:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME:

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY:

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref33497127" class="anchor"></span>Figure 3‑27: Sample ScreenMan form from TaskMan's Schedule/Unschedule Options option *before* scheduling the RUM Background Driver

Edit Option Schedule

Option Name: KMPR BACKGROUND DRIVER

Menu Text: RUM Background Driver TASK ID: 2156701

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: FEB 21,2003@01:00

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET:

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND: Press \<PF1\>H for help Insert

<span id="_Ref44297916" class="anchor"></span>Figure 3‑28: Sample ScreenMan form from TaskMan's Schedule/Unschedule Options option *after* scheduling the RUM Background Driver

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
<td>![](kmpr-version-2-user-manual/031.png)</td>
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

# ## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Acknowledgements, x

Acronyms (ISS)

Home Page Web Address, Glossary, 1

Application Workload, 3-21

Assumptions About the Reader, xiv

B

Background Driver Option

DAILY BACKGROUND LAST START Field, 3-3

DAILY BACKGROUND LAST STOP Field, 3-3

DAILY BACKGROUND TOTAL TIME Field, 3-3

QUEUED BY Field, 3-3

RESCHEDULING FREQUENCY Field, 3-2

STATUS Field FREQUENCY, 3-2

TASK ID Field, 3-2

TEMPORARY COLLECTION GLOBAL Field, 3-3

WEEKLY BACKGROUND LAST START Field, 3-3

WEEKLY BACKGROUND LAST STOP Field, 3-3

WEEKLY BACKGROUND TOTAL TIME Field, 3-3

Background Job, 3-24

Scheduling Frequency, 3-25

C

Callout Boxes, xiii

Capacity Management

Mail Group Edit Option, 2-3

Menu, 2-2, 2-3, 3-1

Capacity Planning

Home Page Web Address, xiv

National Database, 2-1, 2-2, 2-4, 3-24

Projections Home Page Web Address, 2-2

Statistics Home Page Web Address, 2-2

Collection Global

KMPTMP("KMPR"), 2-1, 3-2, 3-3, 3-6, 3-24, 3-25

Contents, vi

D

DAILY BACKGROUND LAST START Field, 3-3

DAILY BACKGROUND LAST STOP Field, 3-3

DAILY BACKGROUND TOTAL TIME Field, 3-3

Data Collection Process, 2-1

Data Dictionary

Data Dictionary Utilities Menu, xiii

Listings, xiii

Databases

Capacity Planning National Database, 2-1, 2-2, 2-4, 3-24

Documentation

Revisions, iii

Symbols, xii

E

Eve Menu, 2-2

EVS Anonymous Directories, xv

F

Fields

DAILY BACKGROUND LAST START, 3-3

DAILY BACKGROUND LAST STOP, 3-3

DAILY BACKGROUND TOTAL TIME, 3-3

QUEUED BY, 3-3

QUEUED TO RUN AT, 3-2

QUEUED TO RUN AT WHAT TIME, 3-4

RESCHEDULING FREQUENCY, 3-2

RESCHEDULING FREQUENCY Field, 3-4

RUM BACKGROUND DRIVER, 3-2

STATUS, 3-2

TASK ID, 3-2

TEMPORARY COLLECTION GLOBAL, 3-3

WEEKLY BACKGROUND LAST START, 3-3

WEEKLY BACKGROUND LAST STOP, 3-3

WEEKLY BACKGROUND TOTAL TIME, 3-3

Figures and Tables, viii

Files

OPTION SCHEDULING (#19.2), 3-4

RESOURCE USAGE MONITOR (#8971.1), 2-1, 2-2, 3-2, 3-6, 3-9, 3-20, 3-24, 3-25

Functional Description, 2-1

G

Globals

KMPTMP("KMPR") Collection Global, 2-1, 3-2, 3-3, 3-6, 3-24, 3-25

Glossary, 1

Glossary (ISS)

Home Page Web Address, Glossary, 1

Graphs, Workload

All Nodes, 3-10

Single Node, 3-13

H

Help

At Prompts, xiii

Online, xiii

Home Pages

Adobe Acrobat Quick Guide Web Address, xv

Adobe Web Address, xv

Capacity Planning Home Page Web Address, xiv

Capacity Planning Projections Home Page Web Address, 2-2

Capacity Planning Statistics Home Page Web Address, 2-2

ISS Acronyms Home Page Web Address, Glossary, 1

ISS Glossary Home Page Web Address, Glossary, 1

VHA OI HSD&D Home Page Web Address, xiv

VistA Documentation Library (VDL) Home Page Web Address, xv

How to

Obtain Technical Information Online, xiii

Use this Manual, xii

I

Introduction, 2-1

ISS Acronyms

Home Page Web Address, Glossary, 1

ISS Glossary

Home Page Web Address, Glossary, 1

K

KMP MAIL GROUP EDIT Option, 2-3

KMP-CAPMAN Mail Group, 2-3

KMPR BACKGROUND DRIVER Option, 2-1, 2-2, 3-2, 3-6, 3-24

Daily Last Start, 3-3

Daily Last Stop, 3-3

Daily Run Time, 3-3

Rescheduling Frequency, 3-2, 3-4, 3-6

Weekly Last Start, 3-3

Weekly Last Stop, 3-3

KMPR GRAPH ALL NODES Option, 3-10

KMPR GRAPH HOURLY SINGLE NODE Option, 3-13

KMPR PRINT HOURLY OCCURRENCE Option, 3-19

KMPR PRINT NODE PERCENT Option, 3-21

KMPR PRINT OPTION DATA Option, 3-15

KMPR REPORTS MENU, 3-9

KMPR RUM MANAGER MENU, 2-2, 3-1, 3-9

KMPR START COLLECTION Option, 3-6

KMPR STATUS COLLECTION Option, 3-2, 3-4, 3-6

KMPR STOP COLLECTION Option, 3-8

KMPTMP("KMPR") Collection Global, 2-1, 3-2, 3-3, 3-6, 3-24

L

List File Attributes Option, xiii

M

M Commands Workload

All Nodes, 3-11

Single Node, 3-13

Mail Groups

KMP-CAPMAN, 2-3

Management of the RUM Software, 2-2

Menus

Capacity Management, 2-2, 2-3, 3-1

Data Dictionary Utilities, xiii

Eve, 2-2

KMPR REPORTS MENU, 3-9

KMPR RUM MANAGER MENU, 2-2, 3-1, 3-9

RUM Manager Menu, 2-2, 3-1, 3-9

RUM Reports, 3-9

Taskman Management, 3-6, 3-24

XTCM MAIN, 2-2, 2-3, 3-1

XUTM MGR, 3-6, 3-24

N

National Database

Capacity Planning, 2-1, 2-2, 2-4, 3-24

O

Obtain Technical Information Online, How to, xiii

Obtaining Data Dictionary Listings, xiii

Online

Documentation, xiii

Help Frames, xiii

OPTION SCHEDULING File (#19.2), 3-4

Option Workload, 3-15

Option/Task Workload, 3-19

Options

Capacity Management Mail Group Edit, 2-3

Capacity Management Menu, 2-2, 2-3, 3-1

Eve Menu, 2-2

KMP MAIL GROUP EDIT, 2-3

KMPR BACKGROUND DRIVER, 2-1, 2-2, 3-2, 3-6, 3-24

Daily Last Start, 3-3

Daily Last Stop, 3-3

Daily Run Time, 3-3

Rescheduling Frequency, 3-2, 3-4, 3-6

Weekly Last Start, 3-3

Weekly Last Stop, 3-3

KMPR GRAPH ALL NODES, 3-10

KMPR GRAPH HOURLY SINGLE NODE, 3-13

KMPR PRINT HOURLY OCCURRENCE, 3-19

KMPR PRINT NODE PERCENT, 3-21

KMPR PRINT OPTION DATA, 3-15

KMPR REPORTS MENU, 3-9

KMPR RUM MANAGER MENU, 2-2, 3-1, 3-9

KMPR START COLLECTION, 3-6

KMPR STATUS COLLECTION, 3-2, 3-4, 3-6

KMPR STOP COLLECTION, 3-8

List File Attributes, xiii

Package Resource Usage, 3-21

Print Hourly Occurrence Distribution, 3-19

Resource Usage Monitor (RUM), 3-1

RUM Background Driver, 2-1, 2-2, 3-24

Rescheduling Frequency, 3-4, 3-6

RUM Data by Date for Single Node (Graph), 3-13

RUM Data for All Nodes (Graph), 3-10

RUM Data for an Option, 3-15

RUM Manager Menu, 2-2, 3-1, 3-9

RUM Reports, 3-9

Schedule/Unschedule Options, 3-6, 3-24

Start RUM Collection, 3-6

Status of RUM Collection, 3-2, 3-4, 3-6

Stop RUM Collection, 3-8

Taskman Management, 3-6, 3-24

XTCM MAIN, 2-2, 2-3, 3-1

XUTM MGR, 3-6, 3-24

XUTM SCHEDULE, 3-6, 3-24

Orientation, xii

Overview

RUM Software, 2-1

P

Package Resource Usage Option, 3-21

Patches

Revisions, iv

Print Hourly Occurrence Distribution Option, 3-19

Projections and Statistics, 2-2

Protocol Workload, 3-15, 3-17, 3-19

Q

Question Mark Help, xiii

QUEUED BY Field, 3-3

QUEUED TO RUN AT Field, 3-2

QUEUED TO RUN AT WHAT TIME Field, 3-4

R

Reader, Assumptions About the, xiv

Reference Materials, xiv

Reports

Data for a Single Node, 3-13

Data for a Software, 3-21

Data for all nodes, 3-10

Data for an Option, 3-15

KMPR REPORTS MENU, 3-9

Print Hourly Occurrence Distribution, 3-19

RUM Reports Menu, 3-9

RESCHEDULING FREQUENCY Field, 3-2, 3-4

RESOURCE USAGE MONITOR File (#8971.1), 2-1, 2-2, 3-2, 3-6, 3-9, 3-19, 3-24, 3-25

Revision History, iii

Documentation, iii

Patches, iv

RPC Workload, 3-15, 3-18, 3-19

RUM

Functional Description, 2-1

Overview and Use of Software, 2-1

Shutdown Process, 3-8

Software Overview and Use, 2-1

Startup Process, 3-6

RUM BACKGROUND DRIVER Field, 3-2

RUM Background Driver Option, 2-1, 2-2, 3-24

Rescheduling Frequency, 3-4, 3-6

RUM Collection Routines

Current Status, 3-2

RUM Data by Date for Single Node (Graph) Option, 3-13

RUM Data for All Nodes (Graph) Option, 3-10

RUM Data for an Option, 3-15

RUM Manager Menu, 2-2, 3-1, 3-9

RUM Options, 3-1

RUM Reports Menu, 3-9

RUM Software

Management, 2-2

S

Schedule/Unschedule Options Option, 3-6, 3-24

Shutdown Process

RUM, 3-8

Software

Management, 2-2

Overview and Use, 2-1

Start RUM Collection Option, 3-6

Startup Process

RUM, 3-6

Statistics and Projections, 2-2

STATUS Field, 3-2

Status of RUM Collection Option, 3-2, 3-4, 3-6

Status of RUM Collection Routines, 3-2

Stop RUM Collection Option, 3-8

Symbols Found in the Documentation, xii

System Workload, 3-15, 3-19

T

Tables and Figures, viii

TASK ID Field, 3-2

Taskman Management Menu, 3-6, 3-24

TEMPORARY COLLECTION GLOBAL Field, 3-3

U

URLs

Adobe Acrobat Quick Guide Web Address, xv

Adobe Home Page Web Address, xv

Use of the RUM Software, 2-1

Using

Adobe Acrobat Reader, xv

V

VHA OI HSD&D Home Page Web Address, xiv

VistA Documentation Library (VDL)

Home Page Web Address, xv

W

Web Pages

Adobe Acrobat Quick Guide Web Address, xv

Adobe Home Page Web Address, xv

Capacity Planning Home Page Web Address, xiv

Capacity Planning Projections Home Page Web Address, 2-2

Capacity Planning Statistics Home Page Web Address, 2-2

ISS Acronyms Home Page Web Address, Glossary, 1

ISS Glossary Home Page Web Address, Glossary, 1

VHA OI HSD&D Home Page Web Address, xiv

VistA Documentation Library (VDL) Home Page Web Address, xv

WEEKLY BACKGROUND LAST START Field, 3-3

WEEKLY BACKGROUND LAST STOP Field, 3-3

WEEKLY BACKGROUND TOTAL TIME Field, 3-3

Workload

All Nodes, 3-10

Data, 3-24

M Commands

All Nodes, 3-11

Single Node, 3-13

Protocol, 3-15, 3-17, 3-19

RPC, 3-15, 3-18, 3-19

Single Node, 3-13

System, 3-15, 3-19

VistA Applications, 3-21

VistA Options, 3-15

VistA Options/Tasks, 3-19

X

XTCM MAIN Menu, 2-2, 2-3, 3-1

XUTM MGR Menu, 3-6, 3-24

XUTM SCHEDULE Option, 3-6, 3-24