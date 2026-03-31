---
title: Network Health Exchange Version 5 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: AFJX
app_name: Network Health Exchange (NHE)
section: INF
app_status: active
pkg_ns: AFJX
patch_ver: 5
patch_id: AFJX*5
group_key: "AFJX:AFJX:5"
file_numbers: []
security_keys: []
menu_options: 6
description: Network Health Exchange (NHE) was developed at the REDACTED Veterans Affairs Medical Center (VAMC) and has evolved over several iterations. The Network Health Exchange is a Veterans Health Information Systems and Technology Architecture (VistA) component that provides clinicians with quick and easy
audience: 
keywords: 
  - network
  - health
  - exchange
  - patient
  - span
  - options
  - figure
  - table
  - sample
  - class
page_count: 0
word_count: 7679
section_count: 7
table_count: 30
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=79"
---

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [## Orientation](#orientation)
  - [# Introduction](#introduction)
    - [Overview](#overview)
    - [Software Operation](#software-operation)
    - [# User Menu](#user-menu)
    - [Network Health Exchange Options Menu](#network-health-exchange-options-menu)
    - [# Manager Menu](#manager-menu)
    - [# Site Management Functions](#site-management-functions)
    - [Records for Sensitive Patients](#records-for-sensitive-patients)
  - [## Glossary](#glossary)
  - [## Index](#index)
![](network-health-exchange-version-5-user-manual/001.png)
NETWORK HEALTH EXCHANGE (NHE)USER MANUAL
February 1996
VistA Health Systems Design & Development (HSD&D)
Infrastructure and Security Services (ISS)

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
<td>02/1996</td>
<td>1.0</td>
<td>Initial Network Health Exchange V. 5.1 software documentation creation.</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>09/27/04</td>
<td>2.0</td>
<td><p>Reformatted document to follow ISS styles and guidelines.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: MMPDPATIENT,[N] or KMPDUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., KMPDPATIENT, ONE, KMPDPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/16/05</td>
<td>2.1</td>
<td><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc44314849" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table i: Documentation revision history [iii](#_Toc44314849)

Table ii: Documentation symbol descriptions [ix](#_Ref6202021)

Figure 1‑1: Network Health Exchange first screen [1-2](#_Toc83705188)

Figure 2‑1: NHE User's Menu [2-1](#_Toc83705189)

Table 2‑1: User menu options [2-2](#_Toc83705190)

Figure 2‑2: Sample alerts pending notification [2-2](#_Toc83705191)

Figure 2‑3: Sample information returned message [2-3](#_Toc83705192)

Figure 2‑4: Sample dialogue from the Brief (12 months) Medical Record Information option [2-4](#_Toc83705193)

Figure 2‑5: Sample alerts pending notification [2-5](#_Toc83705194)

Figure 2‑6: Sample dialogue from the Total Medical Record Information option [2-6](#_Toc83705195)

Figure 2‑7: Sample alerts pending notification [2-6](#_Toc83705196)

Figure 2‑8: Sample dialogue from the Brief (12 months) Pharmacy Information option [2-7](#_Toc83705197)

Figure 2‑9: Sample alerts pending notification [2-8](#_Toc83705198)

Figure 2‑10: Sample dialogue from the Total Pharmacy Information option [2-9](#_Toc83705199)

Figure 2‑11: Sample alerts pending notification [2-9](#_Toc83705200)

Figure 2‑12: Sample dialogue from the Print (Completed Requests Only) option (1 of 3) [2-11](#_Toc83705201)

Figure 2‑13: Sample dialogue from the Print (Completed Requests Only) option (2 of 3) [2-12](#_Toc83705202)

Figure 2‑14: Sample dialogue from the Print (Completed Requests Only) option (3 of 3) [2-12](#_Toc83705203)

Figure 2‑15: Sample dialogue from the [2-14](#_Toc83705204)

Figure 2‑16: Sample dialogue from the Print By Type of Information (Completed Requests) option [2-15](#_Toc83705205)

Figure 2‑17: Sample report from the Print By Type of Information (Completed Requests) option [2-16](#_Toc83705206)

Figure 3‑1: Network Health Exchange Manager Menu [3-1](#_Toc83705207)

Table 2‑2: Manager Menu Options [3-1](#_Toc83705208)

Figure 3‑2: Sample dialogue from the Network Health Exchange Add/Edit Sites—Adding a site [3-2](#_Toc83705209)

Figure 3‑3: Sample dialogue from the Network Health Exchange Add/Edit Sites option—Editing a

site [3-3](#_Toc83705210)

Figure 3‑4: Sample dialogue from the Network Health Exchange Inquiry option [3-4](#_Toc83705211)

Figure 3‑5: Sample dialogue from the Network Health Exchange Options option (1 of 2) [3-5](#_Toc83705212)

Figure 3‑6: Sample dialogue from the Network Health Exchange Options option (2 of 2) [3-6](#_Toc83705213)

Table 2‑3: Site management functions [4-1](#_Toc83705214)

Figure 4‑1: Sample dialogue from the AFJXNH ADD PATIENTS option [4-2](#_Toc83705215)

Figure 4‑2: Sample dialogue from the AFJXNH PURGE NIGHTLY option [4-4](#_Toc83705216)

Figure 4‑3: Sample warning message displayed to users requesting information on a sensitive patient record [4-6](#_Toc83705217)

Figure 4‑4: Sample Sensitive Record Accessed bulletin (1 of 2) [4-7](#_Toc83705218)

Figure 4‑5: Sample Sensitive Record Accessed bulletin (2 of 2) [4-7](#_Toc83705219)

## ## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the use of the Network Health Exchange (NHE) software within Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure and Security Services (ISS) software products.

The main body of the manual is divided into three sections:

- User Menu
- Manager Menu
- Site Management Functions

  Each of the three sections begins with an overview and then describes each menu option or function in detail.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                   |                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Symbol                                        | Description                                                                                      |
| ![](network-health-exchange-version-5-user-manual/002.png) | Used to inform the reader of general information including references to additional reading material |
| ![](network-health-exchange-version-5-user-manual/003.png) | Used to caution the reader to take special notice of critical information                            |

<span id="_Ref6202021" class="anchor"></span>Table ii: Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will be in the "000" or "666."
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- The "\<Enter\>" found within these snapshots indicate that the user should press the Enter key on their keyboard.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                   |                                                                                                                                  |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

|                                                   |                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/005.png) | Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case. |

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                   |                                                                                                                            |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

Help at Prompts

VistA software provides online help and commonly used system default prompts. In character-based mode, users are strongly encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA software.

To retrieve online documentation in the form of Help in VistA character-based software:

- Enter a single question mark ("?") at a field/prompt to obtain a brief description. If a field is a pointer, entering one question mark ("?") displays the HELP PROMPT field contents and a list of choices, if the list is short. If the list is long, the user will be asked if the entire list should be displayed. A YES response will invoke the display. The display can be given a starting point by prefacing the starting point with an up-arrow ("^") as a response. For example, ^M would start an alphabetic listing at the letter M instead of the letter A while ^127 would start any listing at the 127th entry.
- Enter two question marks ("??") at a field/prompt for a more detailed description. Also, if a field is a pointer, entering two question marks displays the HELP PROMPT field contents and the list of choices.
- Enter three question marks ("???") at a field/prompt to invoke any additional Help text that may be stored in Help Frames.

Obtaining Data Dictionary Listings

Technical information about files and the fields in files is stored in data dictionaries. You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                   |                                                                                                                                                                                                              |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/007.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- M programming language

It provides an overall explanation of the use of the Network Health Exchange (NHE) software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the VHA OI Health Systems Design & Development (HSD&D) Home Page at the following Web address:

> [REDACTED](http://vaww.vista.med.va.gov/)

Reference Materials

Readers who wish to learn more about Infrastructure and Security Services (ISS) documentation should consult the following:

- *Network Health Exchange (NHE) Release Notes*
- *Network Health Exchange (NHE) Installation Guide*
- *Network Health Exchange (NHE) Technical Manual*
- *Network Health Exchange (NHE) User Manual* (this manual)
- The Network Health Exchange Home Page at the following Web address:

> [REDACTED](http://vaww.vista.med.va.gov/nhe/index.asp)

> This site contains additional information and documentation.

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-user-manual/008.png)</td>
<td><p>For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/iss/acrobat/index.asp">http://vista.med.va.gov/iss/acrobat/index.asp</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

VistA documentation can be downloaded from the Enterprise VistA Support (EVS) anonymous directories or from the Health Systems Design and Development (HSD&D) VistA Documentation Library (VDL) Web site:

> <http://www.va.gov/vdl/>

VistA documentation and software can also be downloaded from the Enterprise VistA Support (EVS) anonymous directories:

- Albany OIFO [REDACTED](ftp://ftp.fo-albany.med.va.gov)
- Hines OIFO [REDACTED](ftp://ftp.fo-hines.med.va.gov)
- Salt Lake City OIFO [REDACTED](ftp://ftp.fo-slc.med.va.gov)
- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/009.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

## # Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Network Health Exchange (NHE) was developed at the REDACTED Veterans Affairs Medical Center (VAMC) and has evolved over several iterations. The Network Health Exchange is a Veterans Health Information Systems and Technology Architecture (VistA) component that provides clinicians with quick and easy access to patients' information from any site where they have been treated. NHE provides the computer mechanism for VAMC clinicians to retrieve clinical patient data from other medical centers. The requester is notified of returned patient data through an alert that appears with the VistA menu system. Patient data is displayed in a format similar to the integrated clinical reports found in Health Summary and can be viewed onscreen or printed.

The NHE software accesses several VistA files which contain information concerning clinic visits, diagnoses, prescriptions, laboratory tests, radiology exams, and hospital admissions. It enables clinicians to request a total or brief medical or pharmacy record for a specified patient from a specified site or sites. This permits clinical staff to take advantage of the vast amount of clinical data supported through VistA.

Network Health Exchange is based on the Health Summary software. However, NHE does not make calls to Health Summary so it is not necessary for a site to have Health Summary installed in order to use NHE nor is familiarity with Health Summary required in order to use NHE.

The Network Health Exchange is another tool, similar to Patient Data Exchange (PDX). As compared to PDX, however, Network Health Exchange offers fewer retrieval options and requires less input by the user, resulting in simpler, faster access to patient data.

The Network Health Exchange was the first phase of the Master Patient Index/Patient Demographics (MPI/PD project, which was formerly known as the Clinical Information Resource Network \[CIRN\] Project). The primary goal of the MPI/PD project is to assure full access to patients' information for primary care providers, regardless of location of care. NHE was released as an interim bridge to a more fully integrated clinical patient data exchange system.

### Software Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NHE is used to retrieve and print patient data. You can request a total or brief medical or pharmacy record for a specified patient from a specified site quickly and easily. The return of a request is signalled by an alert. It is easy to add and edit sites with which data will be exchanged and to monitor the the messages containing incoming and outgoing requests.

- Network Health Exchange menu options for users are described in the "User Menu" chapter in this manual. In order to initiate the request for data from another VA facility, you simply enter the patient's name (last,first) or Social Security Number, select the data type (Clinical or only Pharmacy) and amount of patient data you would like returned (full history or last 12 months). Information can be either viewed on the screen or printed.
- NHE Manager Menu provides options to add or edit sites in the local VAMC NETWORK HEALTH AUTHORIZED SITES file, to inquire to the tracking file about a previous message, or to access the Network Health Exchange menu options. These options are described in the "Manager Menu" chapter in this manual.
- Site Management Functions include three servers and two functions for system managers to maintain the NHE software at their site. These utilities are described in the "Site Management Functions" chapter in this manual.

The first NHE screen you see is the following:

> VVVV VVAA

> VVVV VVAAAA

> VVVV VVAAAAAA

> VVVV VVAA AAAA

> VVVV VVAA AAAA

> VVVV VVAA AAAA

> VVVVVVAA AAAA

> VVVVAA AAAAAAAAAAA

> NETWORK HEALTH EXCHANGE

> Developed at REDACTED VA

> V5.1

> This report will come back to you as an ALERT. To read or

> print the report, type 'VA' on any screen where you see the

> following:

> Enter "VA VIEW ALERTS to review alerts

> You may also use the print options \#5 or \#6 on the Network

> Health Exchange menu.

> Press the 'Return' key to continue

<span id="_Toc83705188" class="anchor"></span>Figure 1‑1: Network Health Exchange first screen

### # User Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Network Health Exchange software comprises two menus, the first of which is described in this chapter and illustrated below:

The DHCP Network Health Exchange Options Menu is shown below. It is the main user menu and can be accessed from the Network Health Exchange first screen. It permits the retrieval of patient information from another VAMC site and allows that information to be viewed onscreen or printed. It is intended to be used by health professionals who have direct patient care responsibilities and have need for clinical information. (If your site has added its own patients, you can make requests for data on patients at your own local facility.)

### Network Health Exchange Options Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen shows the NHE Options Menu, (the User options).

NHE Network Health Exchange Options

DHCP Network Health Exchange Menu User: NHEUSER,ONE

==========================================================================

1 - Brief (12 months) Medical Record Information

2 - Total Medical Record Information

3 - Brief (12 months) Pharmacy Information

4 - Total Pharmacy Information

5 - Print (Completed Requests Only)

6 - Print By Type of Information (Completed Requests)

> **NOTE:** This package does not make calls to the Health Summary package

so sites that do not have Health Summary installed can still use

this package. However, any subsequent updates or changes to the

Health Summary package will not be reflected in this package unless

it is updated.

Select 1-6:

> <span id="_Toc83705189" class="anchor"></span>Figure 2‑1: NHE User's Menu

Each option is described in the next section, User Menu Options.

User Menu Options

The User menu has six options. These options request patient data to be viewed or printed. The first four options are for requesting information from another medical center. They differ only in the type and amount of information retrieved. The last two options are for printing patient information.

Some sites have added their own patients to the NHE NETWORK PATIENT file so that users can request data on patients at their own local site. You may want to ask if your site is set up this way.

The table below shows what each option will give you. For example, if you choose option 1, the report that comes back will give you all patient information that is available for the past twelve months for the individual you specified.

| Option | Option Text                                   | Description                                                                             |
|------------|---------------------------------------------------|---------------------------------------------------------------------------------------------|
| 1      | Brief (12 months) Medical Record Information      | All information available online for the past 12 months for the individual you specified    |
| 2      | Total Medical Record Information                  | All information available in the system with no time limit for the individual you specified |
| 3      | Brief (12 months) Pharmacy Information            | Pharmacy information for the past 12 months for the individual you specified                |
| 4      | Total Pharmacy Information                        | All Pharmacy information with no time limit for the individual you specified                |
| 5      | Print (Completed Requests Only)                   | Print any previously completed requests in the system                                       |
| 6      | Print By Type of Information (Completed Requests) | Print one or more sections of previously completed data                                     |

<span id="_Toc83705190" class="anchor"></span>Table 2‑1: User menu options

ALERTS Notify You of Returned Information

After you choose Option 1, 2, 3, or 4 and request patient information, when you log back in to the system again and the information has been retrieved, you will see a message like this on your screen:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

<span id="_Toc83705191" class="anchor"></span>Figure 2‑2: Sample alerts pending notification

or, if you continue to be logged on to the system, when the information is returned, you will see a message like this:

NETWORK data completed for REDACTED \<BRIEF\> NHEPATIENT 000111111 REDACTED

Enter "VA VIEW ALERTS to review alerts

<span id="_Toc83705192" class="anchor"></span>Figure 2‑3: Sample information returned message

Type "VA and the system will give you the number(s) of your message(s) so that you can retrieve the patient information you requested.

Patient data can be displayed at the time the alert is processed or can be viewed at a later time.

|                                                   |                                                                                                                                                                  |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/010.png) | Records for patients in the database.with an SSN containing five leading zeroes (00000), two leading EEs or ZZs or a P will *not* be sent across to other sites. |

#### Option 1—Brief (12 months) Medical Record Information

> 1 - Brief (12 months) Medical Record Information

> (All information available in the system for the past 12 months)

This option shows a dialogue similar to this one:

Select 1-6: 1

Would you like to look for any previous requests on file ? NO// \<Enter\>

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

THIS OPTION WILL REQUEST BRIEF PATIENT DATA FROM ANOTHER VAMC

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can't request information if the patient is not already on file.

SOCIAL SECURITY \# or NAME: 000666666 \<Enter\> NHEPATIENT,SIX 01-01-40 000666666 NO NSC VETERAN

Request patient information from: all \<Enter\> LOCAL AREA SITES 16000,16000A

Request patient information from: \<Enter\>

Sending Patient Data Request.........

Network Area Recipients:

REDACTED.VA.GOV 612

REDACTED.VA.GOV 662

Local Message ID 31192

Your request has been submitted for completion

SOCIAL SECURITY \# or NAME:

<span id="_Toc83705193" class="anchor"></span>Figure 2‑4: Sample dialogue from the Brief (12 months) Medical Record Information option

ALERTS Notify You of Returned Information

After you choose Option 1, 2, 3, or 4 requesting patient information and the information has been retrieved, you will see a message on your screen like this:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

<span id="_Toc83705194" class="anchor"></span>Figure 2‑5: Sample alerts pending notification

Type "VA on any screen where you see the message displayed in Figure 2‑5 and the system will give you the number(s) of your message(s) so that you can retrieve the patient information you requested.

You will have to exit from the NHE options in order to see this message on your screen.

Patient data can be displayed at the time the alert is processed or can be viewed at a later time.

#### Option 2—Total Medical Record Information

> 2 - Total Medical Record Information

> (All information available in the system with no time limit)

This option shows a dialogue similar to this one:

Select 1-6: 2

Would you like to look for any previous requests on file ? NO// \<Enter\>

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

THIS OPTION WILL REQUEST PATIENT DATA FROM ANOTHER VAMC

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can't request information if the patient is not already on file.

SOCIAL SECURITY \# or NAME: 000222222\<Enter\> NHEPATIENT,TWO 01-01-30 000222222 NO NSC VETERAN

Request patient information from: 662 \<Enter\> REDACTED.VA.GOV 662

Request patient information from: \<Enter\>

Sending Patient Data Request.........

Local Message ID 31195

Your request has been submitted for completion

SOCIAL SECURITY \# or NAME:

<span id="_Toc83705195" class="anchor"></span>Figure 2‑6: Sample dialogue from the Total Medical Record Information option

ALERTS Notify You of Returned Information

After you choose Option 1, 2, 3, or 4 requesting patient information, when you log back in to the system again and the information has been retrieved, you will see a message on your screen like this:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

<span id="_Toc83705196" class="anchor"></span>Figure 2‑7: Sample alerts pending notification

Type "VA on any screen where you see the message displayed in Figure 2‑7 and the system will give you the number(s) of your message(s) so that you can retrieve the patient information you requested.

You will have to exit from the NHE options in order to see this message on your screen.

Patient data can be displayed at the time the alert is processed or can be viewed at a later time.

#### Option 3—Brief (12 months) Pharmacy Information

> 3 -Brief (12 months) Pharmacy Information

> (Pharmacy information for the past 12 months)

This option shows a dialogue similar to this one:

Select 1-6: 3

Would you like to look for any previous requests on file ? NO// \<Enter\>

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

THIS OPTION WILL REQUEST BRIEF PHARMACY DATA FROM ANOTHER VAMC

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can't request information if the patient is not already on file.

SOCIAL SECURITY \# or NAME: 000333333\<Enter\> NHEPATIENT,THREE 01-01-55 000333333 NO NSC VETERAN

Request patient information from: SANFRAN \<Enter\> CISCO.VA.GOV 662

Request patient information from: \<Enter\>

Sending Patient Data Request.........

Local Message ID 31200

Your request has been submitted for completion

A copy of this request was also sent to your 'IN' mail basket

SOCIAL SECURITY \# or NAME:

<span id="_Toc83705197" class="anchor"></span>Figure 2‑8: Sample dialogue from the Brief (12 months) Pharmacy Information option

ALERTS Notify You of Returned Information

After you choose Option 1, 2, 3, or 4 requesting patient information, when you log back in to the system again and the information has been retrieved, you will see a message on your screen like this:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

<span id="_Toc83705198" class="anchor"></span>Figure 2‑9: Sample alerts pending notification

Type "VA on any screen where you see the message displayed in Figure 2‑9 and the system will give you the number(s) of your message(s) so that you can retrieve the patient information you requested.

You will have to exit from the NHE options in order to see this message on your screen.

Patient data can be displayed at the time the alert is processed or can be viewed at a later time.

#### Option 4—Total Pharmacy Information

> 4 -Total Pharmacy Information

> (All Pharmacy information with no time limit)

This option shows a dialogue similar to this one:

Select 1-6: 4

Would you like to look for any previous requests on file ? NO// \<Enter\>

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

THIS OPTION WILL REQUEST PATIENT PHARMACY DATA FROM ANOTHER VAMC

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

You can't request information if the patient is not already on file.

SOCIAL SECURITY \# or NAME: 000444444\<Enter\> NHEPATIENT,FOUR 01-01-21 000444444 NO NSC VETERAN

Request patient information from: SANFRAN \<Enter\> CISCO.VA.GOV 662

Request patient information from: \<Enter\>

Sending Patient Data Request.........

Local Message ID 31201

Your request has been submitted for completion

SOCIAL SECURITY \# or NAME:

<span id="_Toc83705199" class="anchor"></span>Figure 2‑10: Sample dialogue from the Total Pharmacy Information option

ALERTS Notify You of Returned Information

After you choose Option 1, 2, 3, or 4 requesting patient information, when you log back in to the system again and the information has been retrieved, you will see a message on your screen like this:

You have PENDING ALERTS

Enter "VA VIEW ALERTS to review alerts

<span id="_Toc83705200" class="anchor"></span>Figure 2‑11: Sample alerts pending notification

Type "VA on any screen where you see the message dispalyed in Figure 2‑11 and the system will give you the number(s) of your message(s) so that you can retrieve the patient information you requested.

You will have to exit from the NHE options in order to see this message on your screen.

Patient data can be displayed at the time the alert is processed or can be viewed at a later time.

#### Option 5—Print (Completed Requests Only)

> 5 - Print (Completed Requests Only)

> (Print any previously completed requests in the system)

This option shows a dialogue similar to this one:

Select 1-6: 5

Which requests would you like Y) Your Own A) All ^) None Y// A

THIS REPORT CAN BE SENT TO A PRINTER OR READ ON THE SCREEN

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Message \# Subject Date Sent

========================================================================

1 \<NHBP\> NHEPATIENT 000666666 REDACTED.VA.G 01/10/96

2 \<BRIEF\> NHEPATIENT 000666666 REDACTED.VA.G 01/30/96@1422

3 \<NHBP\> NHEPATIENT 000777777 REDACTED.VA.GO 01/25/96

Type one number eg. 1 or up to ten numbers separated by commas eg. 1,2,3,4,5,6,7

,8,9,10: 1

DEVICE: HOME// VIRTUAL TERMINAL

NHEPATIENT,SIX 000-66-6666 DOB: 1930

------------------------------- DEM - Demographics -------------------

Address: 123 MAIN STREET Phone:

SAN FRANCISCO CALIFORNIA 94105 County:SAN FRANCISCO

Marital Status: NEVER MARRIED

Religion: UNKNOWN/NO PREFERENCE

Period of Service: KOREAN

Branch of Service: ARMY 00/00/50 TO 00/00/52

Combat: NO POW: NO

Eligibility: NSC Status: VERIFIED

Eligible for care?: YES

-----------------------------ADRs & Allergies ---------------------------

Allergy/Reaction:

NO KNOWN DRUG ALLERGIES

------------------- Outpatient Medications (Brief) -----------------------

Fill Exp/Canc

Press return to continue or "^" to quit: \<Enter\>

<span id="_Toc83705201" class="anchor"></span>Figure 2‑12: Sample dialogue from the Print (Completed Requests Only) option (1 of 3)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*CONFIDENTIAL Patient Data\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------- Outpatient Medications (Brief) -----------------------

Fill Exp/Canc

Drug Qty Stat Date Date

DIAZEPAM SUS-REL. 15MG 30 A 12/08/95 06/09/96

HYDROCORTISONE CREAM 1% 1 OZ TUBE 1 A 12/08/95 06/09/96

--------------------------- IV Pharmacy -------------------------------

Drug Dose Stat Start Stop

No data available

------------------------------ Unit Dose -------------------------------

Press return to continue or "^" to quit: \<Enter\>

<span id="_Toc83705202" class="anchor"></span>Figure 2‑13: Sample dialogue from the Print (Completed Requests Only) option (2 of 3)

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*CONFIDENTIAL Patient Data\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

Drug Dose Stat Start Stop Instr

\*\*\*\*\*\*\*\*\*END OF CONFIDENTIAL Patient Data from REDACTED.VA.GOV\*\*\*\*\*\*\*\*\*\*\*\*

<span id="_Toc83705203" class="anchor"></span>Figure 2‑14: Sample dialogue from the Print (Completed Requests Only) option (3 of 3)

Option 5—Report Sample

This option allows you to send the report to a printer or view it on your screen.

The printed report will look like this:

> NHEPATIENT,SIX 000-66-6666 DOB: 1930

> ------------------------------- DEM - Demographics ----------------------

> Address: 123 MAIN STREET Phone:

> SAN FRANCISCO CALIFORNIA 94105 County: SAN FRANCISCO

> Marital Status: NEVER MARRIED

> Religion: UNKNOWN/NO PREFERENCE

> Period of Service: KOREAN

> Branch of Service: ARMY 00/00/50 TO 00/00/52

> Combat: NO POW: NO

> Eligibility: NSC Status: VERIFIED

> Eligible for care?: YES

> -----------------------------ADRs & Allergies -----------------------------

> Allergy/Reaction:

> NO KNOWN DRUG ALLERGIES

> ----------------------- Admission/Discharge------------------------------

> No data available

> ----------------------------- Discharge Summary --------------------------

> IMPORTANT: UNSIGNED/UNCOSIGNED SUMMARIES HAVE NOT BEEN REVIEWED BY PHYSICIAN(S)

> -----------------------------ADRs & Allergies -----------------------------

> Allergy/Reaction:

> NO KNOWN DRUG ALLERGIES

> ----------------------- Admission/Discharge------------------------------

> No data available

> ----------------------------- Discharge Summary --------------------------

> IMPORTANT: UNSIGNED/UNCOSIGNED SUMMARIES HAVE NOT BEEN REVIEWED BY PHYSICIAN(S)

> No data available

> ----------------------------- Disabilities ----------------------------

> Eligibility: NSC VERIFIED Total S/C %:

> Disabilities

> ---------------

> ------------------- Outpatient Medications (Brief) -----------------------

> Fill Exp/Canc

> Drug Qty Stat Date Date

> No data available

> -------------------------- Chem & Hematology --------------------------

> \*\* NOTE: THE RESULTS IN THIS SECTION ARE FOR THE LAST 6 MONTHS ONLY \*\*

> Date/Time Specimen Test Units Result Ref Range

> No data available

> ------------------------------ Microbiology ---------------------------

> No data available

> --------------------------- Surgical Pathology -------------------------

> No data available

> ------------------------------ Cytopathology --------------------------

> No data available

> --------------------------- Radiology Profile -------------------------

> No data available

> --------------------------- Radiology Status --------------------------

> No data available

> ---------------------------- Surgery Reports --------------------------

> ------------------------------ ICD Procedures -------------------------

> 10/02/90 MAGNET REMOVAL CORNEA FB 11.0

> 09/16/90 MAGNET REMOVAL CORNEA FB 11.0

> ------------------------------ ICD Surgeries --------------------------

> No data available

> ------------------------------ Past Clinic Visits ----------------------

> Date/Time Clinic

> No data available

> ------------------------------ Future Clinic Visits --------------------

> Date/Time Clinic

> No data available

> ------------------------------ Medicine Summary -----------------------

> No data available

> ------------------- Pulmonary Function Tests Summary --------------------

> No Pulmonary data available

> ------------------------- CN - Crisis Notes ----------------------------

> No data available

> -------------------------- Progress Notes -----------------------------

> NOTE: MANUAL NOTES EXIST. AUTOMATED NOTES ARE NOT MEANT TO BE INCLUSIVE.

> No data available

> \*\*\*\*\*\*\*\*\*END OF CONFIDENTIAL Patient Data from SAN FRANCISCO.VA.GOV\*\*\*\*\*\*\*\*

<span id="_Toc83705204" class="anchor"></span>Figure 2‑15: Sample dialogue from the

#### Option 6—Print By Type of Information (Completed Requests)

> 6 - Print By Type of Information (Completed Requests)

> (Print one or more sections of previously completed data)

This option shows a dialogue similar to this one:

Select 1-6: 6

Which requests would you like Y) Your Own A) All ^) None Y// A

THIS REPORT CAN BE SENT TO A PRINTER OR READ ON THE SCREEN

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Message \# Subject Date Sent

============================================================================

1 \<NHBP\> NHEPATIENT 000666666 REDACTED.VA.G 01/10/96

2 \<BRIEF\> NHEPATIENT 000666666 REDACTED.VA.G 01/30/96@1422

3 \<NHBP\> NHEPATIENT 000777777 REDACTED.VA.GO 01/25/96

Type the number of the report you would like to review

or print: 2

Choose type: icd

1 ICD Procedures

2 ICD Surgeries

CHOOSE 1-2: 1

DEVICE: HOME// \<Enter\> VIRTUAL TERMINAL

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*CONFIDENTIAL Patient Data\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

------------------------------ ICD Procedures -------------------------

10/02/90 MAGNET REMOVAL CORNEA FB 11.0

09/16/90 MAGNET REMOVAL CORNEA FB 11.0

Choose type:

<span id="_Toc83705205" class="anchor"></span>Figure 2‑16: Sample dialogue from the Print By Type of Information (Completed Requests) option

Option 6—Report Sample

This option allows you to send the report to a printer or view it on your screen.

The printed report will look like this:

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*CONFIDENTIAL Patient Data\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> ------------------------------ ICD Procedures -------------------------

> 10/02/90 MAGNET REMOVAL CORNEA FB 11.0

> 09/16/90 MAGNET REMOVAL CORNEA FB 11.0

<span id="_Toc83705206" class="anchor"></span>Figure 2‑17: Sample report from the Print By Type of Information (Completed Requests) option

### # Manager Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second of the two NHE menus, the Manager Menu, is described in this chapter.

The Network Health Exchange Manager menu is shown below (Figure 3‑1). It is by individuals responsible for the operation of the local Network Health Exchange software. The Network Health Exchange Options (the User options described in the User Menu chapter) are also available from the Manager menu as Option 3 (see below).

Network Health Exchange Manager

1 Network Health Exchange Add/Edit Sites\[AFJXNHEX EDIT SITES\]

2 Network Health Exchange Inquiry \[AFJXNHEX INQUIRE\]

3 Network Health Exchange Options \[AFJXNHEX REQUEST\]

<span id="_Toc83705207" class="anchor"></span>Figure 3‑1: Network Health Exchange Manager Menu

Manager Menu Options

The Manager menu has three options. The table below shows what each option will do for you.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 32%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Option Text</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>1</strong></td>
<td><strong>Add/Edit Sites</strong></td>
<td><p>Edit and add sites that can receive requests (sites in the station's VAMC NETWORK HEALTH EXCHANGE file).</p>
<p><em>If the 'Include in All' question is answered Y or <strong>&lt;Enter&gt;</strong> is pressed, the site will be included when 'All' is chosen. See INCLUDE IN ALL field below.</em></p></td>
</tr>
<tr class="even">
<td><strong>2</strong></td>
<td><strong>Inquiry</strong></td>
<td>Inquire about a previous message ID, or Date/Time Received, or Patient SSN, or Requestor Name, or Requesting Place.</td>
</tr>
<tr class="odd">
<td><strong>3</strong></td>
<td><strong>Options</strong></td>
<td>Request patient data and allow the viewing or printing of returned data. These are the same as the User Menu options.</td>
</tr>
</tbody>
</table>

<span id="_Toc83705208" class="anchor"></span>Table 3‑1: Manager Menu Options

#### Option 1—Add/Edit Sites

> 1 - Network Health Exchange Add/Edit Sites

> To enter a new or edit a present Network Health Authorized site.

Adding a Site

This option shows a dialogue similar to this one when you add a new site:

Select Network Health Exchange Manager Menu Option: 1 \<Enter\> Network Health Exchange Add/Edit Sites

Select VAMC NETWORK HEALTH AUTHORIZED SITES NAME: TESTSITE.VA.GOV

Are you adding 'TESTSITE.VA.GOV' as

a new VAMC NETWORK HEALTH AUTHORIZED SITES (the 8TH)? Y\<Enter\> (Yes)

VAMC NETWORK HEALTH AUTHORIZED SITES STATION NUMBER: 99999

NAME: TESTSITE.VA.GOV// \<Enter\>

STATION NUMBER: 99999// \<Enter\>

NICKNAME: TS

INCLUDE IN 'ALL'?: Y\<Enter\> YES

SEND UPDATE TO NETWORK FILE?: Y\<Enter\> YES

\# DAYS TO KEEP TRACKING DATA?: 90

ACCEPT NETWORK FILE UPDATE?: Y \<Enter\> YES

UPDATE NETWORK IDENTIFIER ?: Y \<Enter\> YES

<span id="_Toc83705209" class="anchor"></span>Figure 3‑2: Sample dialogue from the Network Health Exchange Add/Edit Sites—Adding a site

Fields

NAME: The names of sites you will request and receive data from. The NAME field entry must match the entry in your DOMAIN file (#4.2) *exactly*.

STATION NUMBER: The ALL LOCAL AREA SITES field should have site numbers entered separated by commas for those sites you wish to request data from when selecting ALL LOCAL AREA SITES.

NICKNAME: The 1 - 3 character(s) that will be displayed on Patient Lookup (if Update Network Identifier is set to YES) that will signify this site entry, (i.e., W for REDACTED or San Francisco for San Francisco). If a patient has been seen at more than one site, these nicknames are concatenated together without punctuation (i.e., WSF is displayed if a patient has been seen at REDACTED *and* San Francisco VAMCs).

INCLUDE IN 'ALL'? Enter YES to include this entry as one of the sites requests will be sent to if the user selects the ALL LOCAL AREA SITES entry.

|                                                   |                                                                                                  |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/011.png) | Unless you enter NO at this prompt, the site will be included in the ALL LOCAL AREA SITES group. |

SEND UPDATE TO NETWORK FILE? This field determines whether you want to send your nightly updates to another site to update their VAMC NETWORK PATIENT file (#537010). Any new patients seen at your site will be sent to this site and added to their VAMC NETWORK PATIENT file (#537010) as having data at your site. If your site's entry at this site is set to update the patient identifier, then that site's nickname for your site will be updated and displayed at patient lookup.

ACCEPT NETWORK FILE UPDATE? This field determines whether you want to accept the nightly update from another site. A site may want to send you their update but you may not want to accept because they are not part of your network.

UPDATE NETWORK IDENTIFIER? If yes, then the NETWORK IDENTIFIER field in the PATIENT file (#2) will be updated with the NICKNAME for this site entry and displayed at patient lookup.  
  
> **NOTE:** Network Identifiers from multiple sites are concatenated (strung) together.

|                                                   |                                                                                                                                                             |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/012.png) | Records for patients in the database.with an SSN containing five leading 0s (zeroes), two leading EEs or ZZs or a P will not be sent across to other sites. |

Editing a Site

In order to edit information about a site, you must enter the domain name exactly as it is written in the file.

Select Network Health Exchange Manager Menu Option: 1 \<Enter\> Network Health Exchange Add/Edit Sites

Select VAMC NETWORK HEALTH AUTHORIZED SITES NAME: testsite.va.gov \<Enter\> 99999

NAME: TESTSITE.VA.GOV// \<Enter\>

STATION NUMBER: 99999// \<Enter\>

NICKNAME: TS// \<Enter\>

INCLUDE IN 'ALL'?: YES// n \<Enter\> NO

SEND UPDATE TO NETWORK FILE?: YES// \<Enter\>

\# DAYS TO KEEP TRACKING DATA?: 90// \<Enter\>

ACCEPT NETWORK FILE UPDATE?: YES// \<Enter\>

UPDATE NETWORK IDENTIFIER ?: YES// \<Enter\>

<span id="_Toc83705210" class="anchor"></span>Figure 3‑3: Sample dialogue from the Network Health Exchange Add/Edit Sites option—Editing a site

#### Option 2—Network Health Exchange Inquiry

> 2 - Network Health Exchange Inquiry

> To inquire to the NHEX tracking file that stores data on all incoming and outgoing requests about the message ID, date/time received, patient SSN, requestor name, or requesting place.

This option shows a dialogue similar to this one:

Select Network Health Exchange Manager Option: 2\<Enter\> Network Health Exchange Inquiry

Select VAMC NETWORK HEALTH EXCHANGE MESSAGE ID: ?

Answer with VAMC NETWORK HEALTH EXCHANGE MESSAGE ID, or

DATE/TIME RECEIVED, or PATIENT SSN, or REQUESTOR NAME, or

REQUESTING PLACE

Do you want the entire 9-Entry VAMC NETWORK HEALTH EXCHANGE List? Y \<Enter\> (Yes)

Choose from:

29607 10-31-95 000555555 NHEPATIENT,FIVE REDACTED.VA.GOV

29608 10-31-95 000666666 NHEPATIENT,SIX REDACTED.VA.GOV

29609 10-31-95 000777777 NHEPATIENT,SEVEN REDACTED.VA.GOV

29610 10-31-95 000888888 NHEPATIENT,EIGHT REDACTED.VA.GOV

29611 10-31-95 000999999 NHEPATIENT,NINE REDACTED.VA.GOV

29612 10-31-95 000101010 NHEPATIENT,TEN REDACTED.VA.GOV

29613 10-31-95 000111111 NHEPATIENT,ELEVEN REDACTED.VA.GOV

29614 10-31-95 000121212 NHEPATIENT,TWELVE REDACTED.VA.GOV

29615 11-01-95 000131313 NHEPATIENT,THIRTEE REDACTED.VA.GOV

Select VAMC NETWORK HEALTH EXCHANGE MESSAGE ID: 29615 \<Enter\> 11-01-95 000131313 NHEPATIENT,THIRTEEN REDACTED.VA.GOV

MESSAGE ID: 29615

DATE/TIME RECEIVED: NOV 01, 1995@13:24:22

PATIENT SSN: 000131313 REQUESTOR DUZ: 9225

REQUESTOR NAME: NHEUSER,TWO REQUESTING PLACE: REDACTED.VA.GOV

PATIENT DATA FOUND?: YES REQUEST TYPE: BRIEF

SENSITIVE PATIENT?: NO OUTGOING REQUEST?: YES

DATE/TIME COMPLETED: NOV 01, 1995@14:22:47

Press Return to continue

<span id="_Toc83705211" class="anchor"></span>Figure 3‑4: Sample dialogue from the Network Health Exchange Inquiry option

#### Option 3—Options

> 3 - Network Health Exchange Options

> The NHE User Menu with its six options for requesting and printing patient information.

> Reports can be sent to a printer or read on the screen.

If you choose this option, you will see the main NHE menu, as shown below:

Select Network Health Exchange Manager Option: 3 \<Enter\> Network Health Exchange Options

VVVV VVAA

VVVV VVAAAA

VVVV VVAAAAAA

VVVV VVAA AAAA

VVVV VVAA AAAA

VVVV VVAA AAAA

VVVVVVAA AAAA

VVVVAA AAAAAAAAAAA

NETWORK HEALTH EXCHANGE

Developed at REDACTED VA

V5.1

This report will come back to you as an ALERT. To read or

print the report, type 'VA' on any screen where you see the

following:

Enter "VA VIEW ALERTS to review alerts

You may also use the print options \#5 or \#6 on the Network

Health Exchange menu.

Press the 'Return' key to continue

<span id="_Toc83705212" class="anchor"></span>Figure 3‑5: Sample dialogue from the Network Health Exchange Options option (1 of 2)

When you press Enter, you will see:

DHCP Network Health Exchange Menu User: NHEUSER,ONE

==========================================================================

1 - Brief (12 months) Medical Record Information

2 - Total Medical Record Information

3 - Brief (12 months) Pharmacy Information

4 - Total Pharmacy Information

5 - Print (Completed Requests Only)

6 - Print By Type of Information (Completed Requests)

> **NOTE:** This package does not make calls to the Health Summary package

so sites that do not have Health Summary installed can still use

this package. However, any subsequent updates or changes to the

Health Summary package will not be reflected in this package unless

it is updated.

Select 1-6:

<span id="_Toc83705213" class="anchor"></span>Figure 3‑6: Sample dialogue from the Network Health Exchange Options option (2 of 2)

### # Site Management Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are utilities for system managers to maintain the NHE software at their site.

The functions are activated by directly accessing the utility or by changing the time the routine is run.

The site management functions are:

- AFJXNH ADD PATIENTS Network Health Exchange Add Patients
- AFJXNH PURGE NIGHTLY Network Health Exchange Nightly Purge
- AFJXNETP Network Health Patient Server
- AFJXNHDONE Network Health Exchange Alert Send Server
- AFJXSERVER Network Health Exchange Data Server

| Utility Function  | Description                                                                                                   |
|-----------------------|-------------------------------------------------------------------------------------------------------------------|
| Add Patients      | Nightly adds patients to VAMC NETWORK PATIENT file (#537010).                                                     |
| Nightly Purge     | Nightly purges messages from the mailbox of NETWORK,HEALTH EXCHANGE.                                              |
| Patient Server    | Takes bulletin from nightly Add Patient task and attempts to add patient to VAMC NETWORK PATIENT file (# 537010). |
| Alert Send Server | Sends alert back to user that request is complete and allows user to print the requested clinical data.           |
| Data Server       | Processes patient data request.                                                                                   |

<span id="_Toc83705214" class="anchor"></span>Table 4‑1: Site management functions

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 44%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="network-health-exchange-add-patients-option" class="unnumbered">Network Health Exchange Add Patients Option</h3></td>
<td><strong>[AFJXNH ADD PATIENTS]</strong></td>
</tr>
</tbody>
</table>

This routine should be scheduled nightly to add patients to the VAMC NETWORK PATIENT file (#537010). Your ADPAC or IRM staff should schedule it.

NAME: AFJXNH ADD PATIENTS

MENU TEXT: Network Health Exchange Add Patients

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: NETWORK HEALTH EXCHANGE

DESCRIPTION: SCHEDULE NIGHTLY TO ADD PATIENTS TO NETWORK PATIENT FILE

ROUTINE: AFJXPNHA TIMESTAMP: 55977,50814

\*QUEUED TO RUN AT WHAT TIME:

\*RESCHEDULING FREQUENCY:UPPERCASE MENU TEXT: NETWORK HEALTH EXCHANGE ADD PATIENTS

From the Systems Manager Menu, choose Taskman Management, Schedule/ Unschedule Options, then the AFJXNH ADD PATIENTS option. Your computer dialogue should look similar to this:

Select Systems Manager Menu Option: TASK\<Enter\> man Management

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

Select Taskman Management Option: SCHE \<Enter\> dule/Unschedule Options

Select OPTION to schedule or reschedule: AFJXNH ADD PATIENTS\<Enter\> Network Health Exchange Add Patients

...OK? Yes// \<Enter\> (Yes)

\(R\)

Edit Option Schedule

Option Name: AFJXNH ADD PATIENTS

Menu Text: Network Health Exchange Add Patients TASK ID: 19446

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: DEC 26,1995@03:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET: JSD

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

<span id="_Toc83705215" class="anchor"></span>Figure 4‑1: Sample dialogue from the AFJXNH ADD PATIENTS option

|                                                   |                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/013.png) | If you wish more detailed information, please refer to the "Menu Manager Options" topic in the *Kernel Systems Manaul*. |

|                                                   |                                                                                                                                                             |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/014.png) | Records for patients in the database.with an SSN containing five leading 0s (zeroes), two leading EEs or ZZs or a P will not be sent across to other sites. |

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="network-health-exchange-nightly-purge-option" class="unnumbered">Network Health Exchange Nightly Purge Option</h3></td>
<td><strong>[AFJXNH PURGE NIGHTLY]</strong></td>
</tr>
</tbody>
</table>

This routine purges messages each night from the NETWORK,HEALTH EXCHANGE mailbox.

NAME: AFJXNH PURGE NIGHTLY

MENU TEXT: Network Health Exchange Nightly Purge

TYPE: run routine CREATOR: POSTMASTER

PACKAGE: NETWORK HEALTH EXCHANGE

DESCRIPTION: PURGE MESSAGES NIGHTLY FROM MAILBOX OF NETWORK HEALTH EXCHANGE

GENERIC USER.

ROUTINE: AFJXPNHX

UPPERCASE MENU TEXT: NETWORK HEALTH EXCHANGE NIGHTLY

PURGE

From the Systems Manager Menu, choose Taskman Management, Schedule/ Unschedule Options, then the AFJXNH PURGE NIGHTLY option. Your computer dialogue should look similar to this:

Select Systems Manager Menu Option: TASK \<Enter\> man Management

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

Select Taskman Management Option: SCHE \<Enter\> dule/Unschedule Options

Select OPTION to schedule or reschedule: AFJXNH PURGE NIGHTLY Network Health Exchange Purge Nightly

...OK? Yes// \<Enter\> (Yes)

\(R\)

Edit Option Schedule

Option Name: AFJXNH PURGE NIGHTLY

Menu Text: Network Health Exchange Purge Nightly TASK ID: 19446

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

QUEUED TO RUN AT WHAT TIME: DEC 26,1995@03:30

DEVICE FOR QUEUED JOB OUTPUT:

QUEUED TO RUN ON VOLUME SET: JSD

RESCHEDULING FREQUENCY: 1D

TASK PARAMETERS:

SPECIAL QUEUEING:

<span id="_Toc83705216" class="anchor"></span>Figure 4‑2: Sample dialogue from the AFJXNH PURGE NIGHTLY option

|                                                   |                                                                                                                         |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/015.png) | If you wish more detailed information, please refer to the "Menu Manager Options" topic in the *Kernel Systems Manaul*. |

<table>
<colgroup>
<col style="width: 58%" />
<col style="width: 41%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="network-health-patient-server-option" class="unnumbered">Network Health Patient Server Option</h3></td>
<td><strong>[AFJXNETP]</strong></td>
</tr>
</tbody>
</table>

This routine runs as a background job, at night when the VistA system is less busy than during normal business hours. It takes a bulletin from the nightly Add Patient task and attempts to add the patient to the VAMC NETWORK PATIENT file (#537010).

NAME: AFJXNETP

MENU TEXT: Network Health Patient Server

TYPE: server CREATOR: POSTMASTER

PACKAGE: NETWORK HEALTH EXCHANGE

DESCRIPTION: TAKES BULLETIN FROM NIGHTLY ADD PATIENT TASK AND ATTEMPTS TO ADD PATIENT TO FILE 537010.

ROUTINE: AFJXPNHT SERVER ACTION: RUN IMMEDIATELY

SERVER AUDIT: NO SUPRESS BULLETIN: YES, SUPRESS IT

SERVER REPLY: NO REPLY (DEFAULT)

UPPERCASE MENU TEXT: NETWORK HEALTH PATIENT SERVER

|                                                   |                                                                                                                                                                                                                                                                                                                                                             |
|---------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-user-manual/016.png) | To maximize efficiency, you may want to create a resource device that the server will use. This enables you to limit the number of jobs that are running from the server. For a description of how this is done, see the "Setting Up a Resource Device" topic in the "Installation Procedures" section of the *Network Health Exchange Installation Guide*. |

<table>
<colgroup>
<col style="width: 72%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="network-health-exchange-alert-send-server-option" class="unnumbered">Network Health Exchange Alert Send Server Option</h3></td>
<td><strong>[AFJXNHDONE]</strong></td>
</tr>
</tbody>
</table>

This routine sends an alert back to the user that a request is complete and allows the user to print or view onscreen the requested clinical data.

NAME: AFJXNHDONE

MENU TEXT: Network Health Exchange Alert Send Server

TYPE: server CREATOR: POSTMASTER

PACKAGE: NETWORK HEALTH EXCHANGE

DESCRIPTION: SEND ALERT BACK TO USER THAT REQUEST IS COMPLETE AND ALLOW TO PRINT

ROUTINE: AFJXSFAL SERVER ACTION: RUN IMMEDIATELY

SERVER AUDIT: NO SUPRESS BULLETIN: YES, SUPRESS IT

SERVER REPLY: NO REPLY (DEFAULT)

UPPERCASE MENU TEXT: NETWORK HEALTH EXCHANGE ALERT

SERVER

<table>
<colgroup>
<col style="width: 72%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td><h3 id="network-health-exchange-data-server-option" class="unnumbered">Network Health Exchange Data Server Option</h3></td>
<td><strong>[AFJXSERVER]</strong></td>
</tr>
</tbody>
</table>

Option for server for patient data request. This will process the request.

NAME: AFJXSERVER

MENU TEXT: Network Health Exchange Data Server

TYPE: server CREATOR: POSTMASTER

PACKAGE: NETWORK HEALTH EXCHANGE

DESCRIPTION: OPTION FOR SERVER FOR PATIENT DATA REQUEST. THIS WILL PROCESS THE REQUEST.

ROUTINE: AFJXALRT SERVER BULLETIN: XQSERVER

SERVER ACTION: RUN IMMEDIATELY SERVER AUDIT: NO

SUPRESS BULLETIN: YES, SUPRESS IT SERVER REPLY: NO REPLY (DEFAULT)

UPPERCASE MENU TEXT: NETWORK HEALTH EXCHANGE DATA SERVER

### Records for Sensitive Patients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Requests for information on sensitive patients are tracked and recorded in order to protect the restricted nature of those records.

A user who requests information for a sensitive patient will see a message like the following:

> WARNING

> RESTRICTED RECORD

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \* This record is protected by the Privacy Act of 1974. If you elect \*

> \* to proceed, you will be required to prove you have a ned to know.

> \* Accessing this patient is tracked, and your station Security Officer \*

> \* will contact you for your justification. \*

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> Do you want to continue processing this patient record? No//

<span id="_Toc83705217" class="anchor"></span>Figure 4‑3: Sample warning message displayed to users requesting information on a sensitive patient record

When a user requests sensitive patient information, it causes a Sensitive Record Accessed bulletin to be sent to the mailgroup which ordinarily receives Sensitive Patient bulletins. The bulletin will be similar to one of the following:

Subj: NETWORK HEALTH EXCHANGE REQUESTED FOR SENSITIVE PATIENT \[#35313\]

22 Feb 96 17:04 6 Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

SENSITIVE PATIENT DATA REQUESTED

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Data for SENSITIVE patient: NHEPATIENT,FOURTEEN NNNNNNNNN

has been requested by: NHEUSER,THREE@VAMC.SITE.VA.GOV

<span id="_Toc83705218" class="anchor"></span>Figure 4‑4: Sample Sensitive Record Accessed bulletin (1 of 2)

Subj: RESTRICTED PATIENT RECORD ACCESSED \[#35296\] 22 Feb 96 16:58 5 Lines

From: USER,THREE in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

The following sensitive patient record has been accessed:

Patient Name: NHEPATIENT,FOURTEEN

Soc Sec Num : NNNNNNNNN

Option Used : Network Health Exchange Options ...

<span id="_Toc83705219" class="anchor"></span>Figure 4‑5: Sample Sensitive Record Accessed bulletin (2 of 2)

## ## Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The glossary contains basic terms, acronyms, and definitions used throughout the VistA system, as well as terms specific to the NHE software.

|                                                 |                                                                                                                                                                                                                                                                                                                                                                                                       |
|-------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ADPAC                                           | Automated Data Processing (ADP) Application Coordinator (see Application Coordinator, below).                                                                                                                                                                                                                                                                                                         |
| ALERTS                                          | Brief on-line notices that are issued to users as they complete a cycle through the menu system. Alerts are designed to provide interactive notification of pending computing activities, such as the need to reorder supplies or review a patient's clinical test results. Along with the alert message is an indication that the View Alerts common option should be chosen to take further action. |
| APPLICATION COORDINATOR                         | Designated individuals responsible for user-level management and maintenance of a software application (e.g., Laboratory). Also abbreviated as ADPAC (ADP Application Coordinator).                                                                                                                                                                                                                   |
| BULLETINS                                       | Electronic mail messages that are automatically delivered by MailMan under certain conditions. For example, a bulletin can be set up to fire when database changes occur, such as adding a record to the file of users. Bulletins are fired by bulletin-type cross references.                                                                                                                        |
| EXTRACTOR                                       | A specialized routine designed to scan data files and copy or summarize data for use by another process.                                                                                                                                                                                                                                                                                              |
| FREE TEXT                                       | A type of data field whose permissible values are any combination of numbers, letters, and symbols.                                                                                                                                                                                                                                                                                                   |
| IDCU                                            | The Integrated Data Communications Utility, a wide area network used by VA to interconnect computers for transmitting data between VA sites.                                                                                                                                                                                                                                                          |
| INTERNAL ENTRY NUMBER (IEN)                     | The number used to identify an entry within a file. Every record has a unique internal entry number.                                                                                                                                                                                                                                                                                                  |
| IRM                                             | Information Resource Management. A service at VA medical centers responsible for computer management and system security.                                                                                                                                                                                                                                                                             |
| ISO                                             | Information Security Officer. Person responsible for information security at each VA Medical Center. Works in conjunction with Regional Security Officers (RISOs).                                                                                                                                                                                                                                    |
| MAIL MESSAGE                                    | An entry in the MESSAGE file (#3.9). The VistA electronic mail system (MailMan) supports local and remote networking of messages.                                                                                                                                                                                                                                                                     |
| MAS                                             | Medical Administration Service.                                                                                                                                                                                                                                                                                                                                                                       |
| MIRMO                                           | Medical Information Resources Management Office.                                                                                                                                                                                                                                                                                                                                                      |
| MIS                                             | Management Information System.                                                                                                                                                                                                                                                                                                                                                                        |
| NATIONAL NETWORK HEALTH EXCHANGE (NHE) REGISTRY | This VistA software consists of two major components: 1) a local registry for use within a VA health care facility, and 2) a National Registry reflecting the events of care for patients at all VA facilities.                                                                                                                                                                                       |
| RISO                                            | Regional Information Security Officer. Regional representative of VA Medical Center Information Security Officers (ISOs).                                                                                                                                                                                                                                                                             |
| SECURE MENU DELEGATION (SMD)                    | A controlled system whereby menus and keys can be allocated by people other than IRM staff, such as application coordinators, who have been so authorized.                                                                                                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-user-manual/017.png)</td>
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

## ## Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A

Acronyms (ISS)

Home Page Web Address, Glossary, 2

Add Patients, 4-2

Add/Edit Sites, 3-2

Adding a Site, 3-2

AFJXNETP Option, 4-6

AFJXNH ADD PATIENTS Option, 4-2

AFJXNH PURGE NIGHTLY Option, 4-4

AFJXNHDONE Option, 4-6

AFJXSERVER Option, 4-7

Alert Send Server, 4-1, 4-6

Alerts, 2-2

ALL. See ALL LOCAL AREA SITES

ALL LOCAL AREA SITES entry, 3-3

ALL LOCAL AREA SITES Field, 3-2

Assumptions About the Reader, xi

B

Brief (12 months) Medical Record Information Option, 2-4

Brief (12 months) Pharmacy Information Option, 2-7

C

Callout Boxes, x

Contents, v

D

Data Dictionary

Data Dictionary Utilities Menu, xi

Listings, xi

Data Server, 4-7

DHCP Network Health Exchange Options Menu, 2-1

Documentation

Revisions, iii

Symbols, ix

DOMAIN File (#4.2), 3-2

E

Editing a Site, 3-4

EVS Anonymous Directories, xii

F

Fields

ALL LOCAL AREA SITES, 3-2

NAME, 3-2

Figures and Tables, vii

Files

DOMAIN (#4.2), 3-2

MESSAGE (#3.9), Glossary, 1

NHE NETWORK PATIENT, 2-2

NHEX Tracking File, 3-5

VAMC NETWORK HEALTH AUTHORIZED SITES, 1-1

VAMC NETWORK HEALTH EXCHANGE, 3-1

VAMC NETWORK PATIENT (#537010), 3-3, 4-1, 4-2, 4-6

Fles

PATIENT (#2), 3-3

Functions

Site Management, 4-1

G

Glossary, 1

Glossary (ISS)

Home Page Web Address, Glossary, 2

H

Help

At Prompts, x

Online, x

Home Pages

Adobe Acrobat Quick Guide Web Address, xii

Adobe Web Address, xii

Health Systems Design and Development (HSD&D) Web Address, xi

ISS Acronyms Home Page Web Address, Glossary, 2

ISS Glossary Home Page Web Address, Glossary, 2

Network Health Exchange Home Page Web Address, xii

VDL Home Page Web Address, xii

How to

Obtain Technical Information Online, x

Use this Manual, ix

I

Inquiry, Network Health Exchange, 3-5

Introduction, 1-1

ISS Acronyms

Home Page Web Address, Glossary, 2

ISS Glossary

Home Page Web Address, Glossary, 2

L

List File Attributes Option, xi

M

Mailbox

NETWORK,HEALTH EXCHANGE, 4-4

Mailbox of NETWORK,HEALTH EXCHANGE

Nightly purges, 4-1

Manager Menu, 3-1

Manager Menu Options, 3-1

Managing the Operation of NHE, 3-1

Medical Record Information, Brief (12 months), 2-4

Medical Record Information, Total, 2-6

Menu Structure, 2-1

Menus

Data Dictionary Utilities, xi

DHCP Network Health Exchange Options Menu, 2-1

MESSAGE file (#3.9), Glossary, 1

N

NAME Field, 3-2

Network Health Exchange

Home Page Web Address, xii

Network Health Exchange Add Patients Option, 4-2

Network Health Exchange Add/Edit Sites Option, 3-2

Network Health Exchange Alert Send Server Option, 4-6

Network Health Exchange Data Server Option, 4-7

Network Health Exchange Inquiry Option, 3-5

Network Health Exchange Nightly Purge Option, 4-4

Network Health Exchange Options Option, 3-6

Network Health Patient Server Option, 4-6

Network Identifier, Update, 3-2

NETWORK,HEALTH EXCHANGE Mailbox, 4-4

NHE Menu Structure, 2-1

NHE NETWORK PATIENT File, 2-2

NHEX Tracking File, 3-5

Nightly Purge, 4-4

O

Obtaining Data Dictionary Listings, xi

Online

Documentation, x

Help Frames, xi

Technical Information, How to Obtain, x

Options

AFJXNETP, 4-6

AFJXNH ADD PATIENTS, 4-2

AFJXNH PURGE NIGHTLY, 4-4

AFJXNHDONE, 4-6

AFJXSERVER, 4-7

Brief (12 months) Medical Record Information, 2-4

Brief (12 months) Pharmacy Information, 2-7

DHCP Network Health Exchange Options Menu, 2-1

List File Attributes, xi

Manager Menu Options, 3-1

Network Health Exchange Add Patients, 4-2

Network Health Exchange Add/Edit Sites, 3-2

Network Health Exchange Alert Send Server Option, 4-6

Network Health Exchange Data Server, 4-7

Network Health Exchange Inquiry, 3-5

Network Health Exchange Nightly Purge, 4-4

Network Health Exchange Options, 3-6

Network Health Patient Server, 4-6

Print (Completed Requests Only), 2-11

Print By Type of Information (Completed Requests), 2-15

Taskman Management, Schedule/ Unschedule Options, 4-3, 4-5

Total Medical Record Information, 2-6

Total Pharmacy Information, 2-9

User Menu Options, 2-2

Orientation, ix

Overview, 1-1

P

Patches

Revisions, iii

PATIENT File (#2), 3-3

Patient Lookup, 3-2

Patient Server, 4-1, 4-6

Pharmacy Information, Brief (12 months), 2-7

Pharmacy Information, Total, 2-9

Print (Completed Requests Only) Option, 2-11

Print By Type of Information (Completed Requests) Option, 2-15

Pseudo patient, 2-3, 3-3, 4-3

Q

Question Mark Help, x

R

Reader, Assumptions About the, xi

Records for Sensitive Patients, 4-7

Reference Materials, xii

Revision History

Documentation, iii

Patches, iii

S

Sensitive Patients, 4-7

Site Management Functions, 4-1

Software Operation, 1-1

Symbols Found in the Documentation, ix

T

Taskman Management, Schedule/ Unschedule Options Option, 4-3, 4-5

Test patient, 2-3, 3-3, 4-3

Total Medical Record Information Option, 2-6

Total Pharmacy Information Option, 2-9

U

Update Network Identifier, 3-2

UPDATE NETWORK IDENTIFIER, 3-3

URLs

Adobe Acrobat Quick Guide Web Address, xii

Adobe Home Page Web Address, xii

Health Systems Design and Development (HSD&D) Home Page Web Address, xi

Use this Manual, How to, ix

User Menu, 2-1, 3-6

User Menu Options, 2-2

Using

Adobe Acrobat Reader, xii

Utilities for System Managers, 4-1

V

VAMC NETWORK HEALTH AUTHORIZED SITES File, 1-1

VAMC NETWORK HEALTH EXCHANGE File, 3-1

VAMC NETWORK PATIENT File (#537010), 3-3, 4-1, 4-2, 4-6

VDL

Home Page Web Address, xii

W

Web Pages

Adobe Acrobat Quick Guide Web Address, xii

Adobe Home Page Web Address, xii

Health Systems Design and Development (HSD&D) Home Page Web Address, xi

ISS Acronyms Home Page Web Address, Glossary, 2

ISS Glossary Home Page Web Address, Glossary, 2

Network Health Exchange Home Page Web Address, xii

VDL Home Page Web Address, xii