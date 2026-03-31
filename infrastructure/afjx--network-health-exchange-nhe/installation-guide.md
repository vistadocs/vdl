---
title: Network Health Exchange Version 5 Installation Guide
doc_type: IG
doc_label: Installation Guide
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
menu_options: 2
description: 
audience: 
keywords: 
  - network
  - health
  - table
  - exchange
  - strong
  - class
  - patient
  - sites
  - installation
  - vamc
page_count: 0
word_count: 6336
section_count: 4
table_count: 39
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Network_Health_Exchg_(NHE)/nhe_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=79"
---

![](network-health-exchange-version-5-installation-guide/001.png)

NETWORK HEALTH EXCHANGE (NHE)INSTALLATION GUIDE

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
<td>REDACTED, Oakland, CA OIFO</td>
</tr>
<tr class="odd">
<td>02/16/05</td>
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
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

<span id="_Toc44314849" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

Contents

Revision History [iii](#revision-history)

Figures and Tables [vii](#figures-and-tables)

Orientation [ix](#orientation)

1\. Introduction [1-1](#introduction)

2\. Preliminary Considerations [2-1](#_Toc96423218)

Namespace and Globals [2-1](#namespace-and-globals)

Platform Requirements [2-1](#platform-requirements)

Skills Required to Perform the Installation [2-1](#skills-required-to-perform-the-installation)

Advance Preparation [2-2](#advance-preparation)

3\. Installation Overview [3-1](#_Toc96423223)

4\. Installation Procedures [4-1](#installation-procedures)

Installing NHE, the PATIENT File Identifier, and the PATIENT File Field [4-2](#installing-nhe-the-patient-file-identifier-and-the-patient-file-field)

1\. Reference Reading Material [4-2](#reference-reading-material)

2\. Verify Platform Requirements [4-2](#verify-platform-requirements)

3\. Verify MailMan Domain is Functioning [4-2](#verify-mailman-domain-is-functioning)

4\. Create ^AFJ Global [4-2](#create-afj-global)

5\. Set Privileges [4-3](#set-privileges)

6\. Run the ^AFJXINST Install Routine [4-3](#run-the-afjxinst-install-routine)

7\. (After Running the Inits) Set Up the NETWORK,HEALTH EXCHANGE User [4-5](#after-running-the-inits-set-up-the-networkhealth-exchange-user)

Setting Up the NETWORK,HEALTH EXCHANGE User [4-6](#setting-up-the-networkhealth-exchange-user)

8\. Schedule the AFJXNH PURGE NIGHTLY Job to Run Nightly [4-8](#schedule-the-afjxnh-purge-nightly-job-to-run-nightly)

9\. Set Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File [4-8](#set-up-entries-in-the-vamc-network-health-authorized-sites-file)

Setting Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File [4-10](#setting-up-entries-in-the-vamc-network-health-authorized-sites-file)

10\. Create a Resource Device [4-11](#create-a-resource-device)

Setting Up a Resource Device [4-12](#setting-up-a-resource-device)

11\. Add Entries to the VAMC NETWORK PATIENT File [4-14](#add-entries-to-the-vamc-network-patient-file)

12\. Schedule Background Options to Run Nightly [4-14](#schedule-background-options-to-run-nightly)

13\. Assign Clinical Users to the AFJXNHEX REQUEST Menu Option [4-15](#assign-clinical-users-to-the-afjxnhex-request-menu-option)

14\. Delete DGY3\* and AFJXI\* Install Routines [4-15](#delete-dgy3-and-afjxi-install-routines)

5\. Post-Installation Information [5-1](#_Toc96423243)

Namespace [5-1](#namespace)

NHE Files [5-1](#nhe-files)

Nightly Options [5-1](#nightly-options)

Servers [5-2](#servers)

Options [5-2](#options)

Post Init Routines [5-3](#post-init-routines)

Assign Menus [5-3](#assign-menus)

Domains/Network Estimates [5-4](#domainsnetwork-estimates)

6\. Sample Installation [6-1](#sample-installation)

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instructions are offered regarding the installation of the Network Health Exchange (NHE) software within Veterans Health Information Systems and Technology Architecture (VistA) Infrastructure and Security Services (ISS) software products.

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                   |                                                                                                      |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
| Symbol                                        | Description                                                                                      |
| ![](network-health-exchange-version-5-installation-guide/002.png) | Used to inform the reader of general information including references to additional reading material |
| ![](network-health-exchange-version-5-installation-guide/003.png) | Used to caution the reader to take special notice of critical information                            |

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
| ![](network-health-exchange-version-5-installation-guide/004.png) | Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

|                                                   |                                                                                                                                |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/005.png) | Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case. |

How to Obtain Technical Information Online

Exported file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

|                                                   |                                                                                                                            |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/006.png) | Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic. |

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
| ![](network-health-exchange-version-5-installation-guide/007.png) | For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment (e.g., Kernel Installation and Distribution System \[KIDS\])
- VA FileMan data structures and terminology
- M programming language

It provides an overall explanation of the use of the Network Health Exchange (NHE) software. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) for a general orientation to VistA. For example, go to the VHA OI Health Systems Design & Development (HSD&D) Home Page at the following Web address

REDACTED

Reference Materials

Readers who wish to learn more about Infrastructure and Security Services (ISS) documentation should consult the following:

- *Network Health Exchange (NHE) Release Notes*
- *Network Health Exchange (NHE) Installation Guide* (this manual)
- *Network Health Exchange (NHE) Technical Manual*
- *Network Health Exchange (NHE) User Manual*
- The Network Health Exchange Home Page at the following Web address:

REDACTED

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
<td>![](network-health-exchange-version-5-installation-guide/008.png)</td>
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

- Albany OIFO REDACTED
- Hines OIFO REDACTED
- Salt Lake City OIFO REDACTED
- Preferred Method REDACTED

> This method transmits the files from the first available FTP server.

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|---------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/009.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
- [Preliminary Considerations](#preliminary-considerations)
    - [Namespace and Globals](#namespace-and-globals)
    - [Platform Requirements](#platform-requirements)
    - [Skills Required to Perform the Installation](#skills-required-to-perform-the-installation)
    - [Advance Preparation](#advance-preparation)
- [Installation Overview](#installation-overview)
- [Installation Procedures](#installation-procedures)
    - [Installing NHE, the PATIENT File Identifier, and the PATIENT File Field](#installing-nhe-the-patient-file-identifier-and-the-patient-file-field)
    - [Setting Up the NETWORK,HEALTH EXCHANGE User](#setting-up-the-networkhealth-exchange-user)
    - [Setting Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File](#setting-up-entries-in-the-vamc-network-health-authorized-sites-file)
    - [Setting Up a Resource Device](#setting-up-a-resource-device)
- [Post-Installation Information](#post-installation-information)
- [Sample Installation](#sample-installation)
This guide provides instructions for installing Department of Veterans Affairs (VA) Network Health Exchange (NHE) Version 5.1.
The Network Health Exchange represents the first phase of the Master Patient Inde4x (MPI) Project. The primary goal of the MPI project is to assure full access to patients' information for primary care providers, regardless of location of care. NHE is being released as an interim bridge to a more fully integrated clinical patient data exchange system in the future. The clinician is notified by the software that the requested information is available. The profile can be viewed online or printed.
The NHE software accesses several Veterans Health Information Systems and Technology Architecture (VistA) files that contain information concerning the following:
- Clinic Visits
- Diagnoses
- Prescriptions
- Laboratory Tests
- Radiology Exams
- Hospital Admissions
The NHE software enables clinicians to request a total or brief medical or pharmacy record for a specified patient from a specified site or sites. This permits clinical staff to take advantage of the vast amount of clinical data supported through VistA.

# Preliminary Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Steps required to perform the installation are listed below. Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as in VistA publications. DSM for OpenVMS instructions are provided in the VAX DSM Systems Guide; and MSM-DOS instructions are provided in the 486 Cookbook and Micronetics Standard MUMPS (MSM) System Managers Guide.

Average installations take about 2 minutes when run during the day while users are on the system.

### Namespace and Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The NHE Version 5.1 software uses the "AFJX" namespace and brings in the ^AFJ global.

### Platform Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Network Health Exchange software requires a standard VistA operating environment to function correctly. At a minimum the following VistA software must be installed

- Kernel V. 8.0
- VA FileMan V. 21.0 or higher
- Kernel Toolkit V. 7.3
- MailMan V. 7.1 or higher

### Skills Required to Perform the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as VistA publications.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-installation-guide/010.png)</td>
<td>VAX DSM instruction is provided in the <em>VAX DSM Systems Guide</em> (Cookbook).<br />
<br />
DSM for OpenVMS configurations for Alpha sites are very similar to the configurations for VAX sites.</td>
</tr>
</tbody>
</table>

- Log onto the system console.
- Shutdown and bring up (boot) the system.
- Backup the system; enable/disable journaling.
- Create directories on the host file system.
- Copy files using commands of the host file system
- Switch UCIs from manager (MGR) to production (VAH).
- Load routines, from diskettes, tapes, SDP space, and/or host files.
- Enable/disable routine mapping.
- Manage globals, including global placement, protection, translation, and journaling characteristics.
- Run a system status and restore a job.
- Use ScreenMan and ScreenMan forms to edit data in a file.

### Advance Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Back up your system as a safeguard before the installation.
- Load the routines into a test account.
- Before beginning the installation procedure, establish the MailMan domain for transmission of data between your site and other VAMCs.

# Installation Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                             |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/011.png) | Sites previously running the NHE Class III version software must delete all AFJX\* routines before loading Version 5.1. |

1.  1. Reference Reading Material—Read the *Network Health Exchange (NHE) Release Notes* and *Network Health Exchange (NHE) Installation Guide* (this manual). Also, refer to the *Network Health Exchange (NHE) Technical Manual* for additional information, if desired.
2.  2. Verify Platform Requirements—Determine that your VistA environment meets the minimum platform requirements.
3.  3. Verify MailMan Domain is Functioning—Verify that the MailMan domain for transmission of data between your site and other VAMCs is functioning correctly.
4.  4. Create ^AFJ Global—Create the ^AFJ global and establish appropriate access privileges. The ^AFJ global must be translated and journalled.
5.  5. Set Privileges—Set your DUZ to a valid user number and your DUZ(0)="@" so that you will have all privileges set during the actual installation.
6.  6. Run the ^AFJXINST Install Routine—Load the NHE routines from the distribution media in the UCI where the NHE software will reside.

|                                                   |                                                                                   |
|---------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/012.png) | For an example, please refer to the "Sample Installation" chapter in this manual. |

7.  7. (After Running the Inits) Set Up the NETWORK,HEALTH EXCHANGE User

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-installation-guide/013.png)</td>
<td>For an example, please refer to the "<br />
Setting Up the NETWORK,HEALTH EXCHANGE User" topic in the Installation Procedures chapter of this manual.</td>
</tr>
</tbody>
</table>

8.  8. Schedule the AFJXNH PURGE NIGHTLY Job to Run Nightly—Schedule the AFJXNH PURGE NIGHTLY job through TaskMan. This job should run late at night or after your backup and must be scheduled after AFJXNH ADD PATIENTS.
9.  9. Set Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File—Each site needs to populate this file with the domain name of sites with which they plan to share data.

|                                                   |                                                                                                                                                                        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/014.png) | For an example, please refer to the "Setting Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File" topic in the Installation Procedures chapter of this manual. |

10. 10. Create a Resource Device

|                                                   |                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/015.png) | For an example, please refer to the "Setting Up a Resource Device" topic in the Installation Procedures chapter of this manual. |

11. 11. Add Entries to the VAMC NETWORK PATIENT File—Run the routines that add entries to the VAMC NETWORK PATIENT file (#537010).
12. 12. Schedule Background Options to Run Nightly:
- AFJXNH ADD PATIENTS
- AFJXNH PURGE NIGHTLY.
13. 13. Assign Clinical Users to the AFJXNHEX REQUEST Menu Option
14. 14. Delete DGY3\* and AFJXI\* Install Routines—Delete DGY3\* and AFJXI\* install routines—When you have completed the installation.

# Installation Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the procedures for installing Network Health Exchange V. 5.1 on your system. It contains the following sections:

- Installing NHE, the PATIENT File Identifier, and the PATIENT File Field
- Setting Up the NETWORK,HEALTH EXCHANGE User
- Setting Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File
- Setting Up a Resource Device

### Installing NHE, the PATIENT File Identifier, and the PATIENT File Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                                             |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/016.png) | Sites previously running the NHE Class III version software must delete all AFJX\* routines before loading Version 5.1. |

#### Reference Reading Material

> Before beginning the installation of the Network Health Exchange (NHE) software, please read the *Network Health Exchange (NHE) Release Notes* and *Network Health Exchange (NHE) Installation Guide* (this manual, note especially the Preliminary Considerations chapter).  

> Also, refer to the *Network Health Exchange (NHE) Technical Manual* during installation. It provides additional information related to installing, implementing, and maintaining the NHE software.

#### Verify Platform Requirements

> Verify that your VistA environment meets the minimum platform requirements for NHE (e.g., confirm the types and versions of VistA software currently installed):

- Kernel V. 8.0
- VA FileMan V. 21.0 or higher
- Kernel Toolkit V. 7.3
- MailMan V. 7.1 or higher

#### Verify MailMan Domain is Functioning

> Verify that the MailMan domain for transmission of data between your site and other VAMCs is functioning correctly. To do this, use the following menus/options:

- Systems Manager Menu
- Manage MailMan submenu
- Network Management submenu

#### Create ^AFJ Global

> Use the M utilities to create the new ^AFJ global and to establish appropriate access privileges. The ^AFJ global must be translated and journalled.

#### Set Privileges

> Set your DUZ to a valid user number and your DUZ(0)="@" so that you will have all privileges set during the actual installation.

#### Run the ^AFJXINST Install Routine

> Load the NHE routines from the distribution media in the UCI where the NHE software will reside. Copy the routines to all systems and volume sets as appropriate for your configuration.

|                                                   |                                                                                   |
|---------------------------------------------------|-----------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/017.png) | For an example, please refer to the "Sample Installation" chapter in this manual. |

> AFJXINST runs the AFJXINIT followed by DBY3INIT (Patch DGY3\*5.3\*81).

> After this routine runs, you should have the following:

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 41%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>File</strong></th>
<th><strong>Name</strong></th>
<th><strong>Description</strong></th>
<th><strong>Data Exported?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AFJX(537000,</td>
<td>VAMC NETWORK HEALTH EXCHANGE</td>
<td>Tracking file for requests</td>
<td>NO</td>
</tr>
<tr class="even">
<td>AFJX(537010,</td>
<td>VAMC NETWORK PATIENT</td>
<td>Patients seen in network area</td>
<td>NO</td>
</tr>
<tr class="odd">
<td>AFJX(537015,</td>
<td>VAMC NETWORK HEALTH TYPES</td>
<td>Components available<br />
(27 types of data)</td>
<td>YES</td>
</tr>
<tr class="even">
<td>AFJX(537025,</td>
<td>VAMC NETWORK HEALTH AUTHORIZED SITES</td>
<td>Sites you will be sending requests to and/or receiving data from. Each site populates this file with the domain names of sites with which they plan to share data.</td>
<td>NO</td>
</tr>
</tbody>
</table>

> <span id="_Toc96422122" class="anchor"></span>Table 4‑1: NHE files

| Servers | Description                                                   |
|-------------|-------------------------------------------------------------------|
| AFJXNETP    | Network Health Patient Server.                                    |
| AFJXNHDONE  | Network Health Exchange Alert Send Server.                        |
| AFJXSERVER  | NHE Patient Data Request Server. Processes requests upon receipt. |

<span id="_Toc96422123" class="anchor"></span>Table 4‑2: NHE servers

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 68%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><br />
Options</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AFJXNHEX REQUEST</td>
<td><p>USER'S MENU:</p>
<p>Sends a request via network mail to the data server at the Authorized site. General option for all clinical data users. It contains the following options:</p>
<ul>
<li><p>Brief (12 months) Medical Record Information</p></li>
<li><p>Total Medical Record Information</p></li>
<li><p>Brief (12 months) Pharmacy Information</p></li>
<li><p>Total Pharmacy Information</p></li>
<li><p>Print (Completed Requests Only)</p></li>
<li><p>Print By Type of Information (Completed Requests)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AFJXNHEX MANAGER</td>
<td><p>MANAGER'S MENU:</p>
<p>Options for coordinator or manager. Allows manager to add or edit sites, to make inquiries, and to go directly to the general options. It contains the following options:</p>
<ul>
<li><p>AFJXNHEX ADD/EDIT SITES</p></li>
<li><p>AFJXNHEX INQUIRE</p></li>
<li><p>AFJXNHEX REQUEST</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>AFJXNH ADD PATIENTS</td>
<td>Nightly scheduled option to add patients to VAMC NETWORK PATIENT file (#537010). Must be scheduled when the system is not busy, e.g., around 3:30 or 4:00 a.m.</td>
</tr>
<tr class="even">
<td>AFJXNH PURGE NIGHTLY</td>
<td>Nightly scheduled option to purge messages from NETWORK,HEALTH EXCHANGE User's mailbox. Must be scheduled after AFJXNH ADD PATIENTS.</td>
</tr>
</tbody>
</table>

<span id="_Toc96422124" class="anchor"></span>Table 4‑3: NHE options

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 61%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>File</strong></td>
<td><strong>Name</strong></td>
<td><strong>Description</strong></td>
<td><strong>Data Exported?</strong></td>
</tr>
<tr class="even">
<td>DPT(</td>
<td>PATIENT</td>
<td><p>NETWORK IDENTIFIER field (New field [#537025] in PATIENT file)</p>
<p>Identifier node (A FileMan DBS-compliant [silent] write-only identifier)</p></td>
<td>NO</td>
</tr>
</tbody>
</table>

<span id="_Toc96422125" class="anchor"></span>Table 4‑4: PATIENT file (#2) changes

#### (After Running the Inits) Set Up the NETWORK,HEALTH EXCHANGE User

> The name must be spelled exactly follows:

> NETWORK,HEALTH EXCHANGE

> Make sure you include the comma (,) and omit spaces between NETWORK, and HEALTH. Use the Kernel options to add it so that a mail box will be created.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-installation-guide/018.png)</td>
<td>For an example, please refer to the "<br />
Setting Up the NETWORK,HEALTH EXCHANGE User" topic in the Installation Procedures chapter of this manual.</td>
</tr>
</tbody>
</table>

### Setting Up the NETWORK,HEALTH EXCHANGE User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table 4‑5 is a capture of a sample setup for a NETWORK,HEALTH EXCHANGE User performed at the REDACTEDOffice of Information Field Office (OIFO).

Network Health Exchange data is stored in the form of mail messages in the NETWORK,HEALTH EXCHANGE User's mail box. These messages are accessible only through the NHE menu options. Set local parameters to manage the length of time such messages are retained.

The NETWORK,HEALTH EXCHANGE User must have an Access and Verify code to set up the required mail box. Additionally, the DISUSER flag must be set to YES (i.e., accessible through the Edit an Existing User option, as shown below \[Table 4‑5\]). Other than the required fields (e.g., INITIALS, SSN and SERVICE/SECTION), no other fields contain data.

Select Systems Manager Menu Option: user Management

Select User Management Option: add a New User to the System

Enter NEW PERSON's name (LAST,FIRST MI): NETWORK,HEALTH EXCHANGE

Are you adding 'NETWORK,HEALTH EXCHANGE' as

a new NEW PERSON (the 552ND)? YES \<Enter\> (Yes)

Checking SOUNDEX for matches.

No matches found.

Now for the Identifiers.

INITIAL: NHE

SSN: 000006789

SEX: \<Enter\>

NICK NAME: \<Enter\>

TITLE: \<Enter\>

SSN: 000006789// \<Enter\>

Select DIVISION: \<Enter\>

SERVICE/SECTION: IRM \<Enter\> INFORMATION RESOURCES MGMT. IRM

MAIL CODE: \<Enter\>

Want to edit ACCESS CODE (Y/N): YES

Enter a new ACCESS CODE \<Hidden\>: xxxxxxxx

Please re-type the new code to show that I have it right: xxxxxxxx

OK, Access code has been changed!

Want to edit VERIFY CODE (Y/N): YES

Enter a new VERIFY CODE: xxxxxxxx

Please re-type the new code to show that I have it right: xxxxxxxx

OK, Verify code has been changed!

FILE MANAGER ACCESS CODE: \<Enter\>

PRIMARY MENU OPTION: \<Enter\>

Select SECONDARY MENU OPTIONS: \<Enter\>

PREFERRED EDITOR: \<Enter\>

PAC: \<Enter\>

FILE RANGE: \<Enter\>

MULTIPLE SIGN-ON: \<Enter\>

ASK DEVICE TYPE AT SIGN-ON: \<Enter\>

AUTO MENU: \<Enter\>

TYPE-AHEAD: \<Enter\>

TIMED READ (# OF SECONDS): \<Enter\>

ALWAYS SHOW SECONDARIES: \<Enter\>

PROHIBITED TIMES FOR SIGN-ON: \<Enter\>

ALLOWED TO USE SPOOLER: \<Enter\>

CAN MAKE INTO A MAIL MESSAGE: \<Enter\>

Print User Account Access Letter? NO

Do you wish to allocate security keys? No// NO\<Enter\> (No)

<span id="_Ref96407885" class="anchor"></span>Table 4‑5: Setting up the NETWORK,HEALTH EXCHANGE user—Sample user dialogue

Now, EDIT the user you just created to set the DISUSER flag to YES:

Select User Management Option: EDIT \<Enter\> an Existing User

Select NEW PERSON NAME: NETWORK,HEALTH EXCHANGE

<span id="_Toc96422127" class="anchor"></span>Table 4‑6: Editing the NETWORK,HEALTH EXCHANGE user (1 of 3)

Edit an Existing User

NAME: NETWORK,HEALTH EXCHANGE Page 1 of 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

NAME: NETWORK,HEALTH EXCHANGE INITIAL: NHE

TITLE: NICK NAME:

SSN: 000006789 MAIL CODE:

PRIMARY MENU OPTION:

Select SECONDARY MENU OPTIONS:

Want to edit ACCESS CODE (Y/N): FILE MANAGER ACCESS CODE:

Want to edit VERIFY CODE (Y/N):

PREFERRED EDITOR:

Select DIVISION:

SERVICE/SECTION: A&MMS

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Next Page Press \<PF1\>H for help

<span id="_Toc96422128" class="anchor"></span>Table 4‑7: Editing the NETWORK,HEALTH EXCHANGE user (2 of 3)

Edit an Existing User

NAME: NETWORK,HEALTH EXCHANGE Page 2 of 3

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

TIMED READ (# OF SECONDS):

MULTIPLE SIGN-ON: AUTO MENU:

ASK DEVICE TYPE AT SIGN-ON: TYPE-AHEAD:

PROHIBITED TIMES FOR SIGN-ON:

ALLOWED TO USE SPOOLER: PAC:

CAN MAKE INTO A MAIL MESSAGE: DISUSER: YES

FILE RANGE:

TERMINATION DATE:

ALWAYS SHOW SECONDARIES:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit Save Next Page Refresh

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND: Save Press \<PF1\>H for help

Select User Management Option:

<span id="_Toc96422129" class="anchor"></span>Table 4‑8: Editing the NETWORK,HEALTH EXCHANGE user (3 of 3)

#### Schedule the AFJXNH PURGE NIGHTLY Job to Run Nightly

> Schedule the AFJXNH PURGE NIGHTLY job through TaskMan. This job should run late at night or after your backup and must be scheduled after AFJXNH ADD PATIENTS.

#### Set Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File

> Set up entries in the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025), so users can request data from these sites. Fill in the following fields:

- NAME
- STATION NUMBER
- INCLUDE IN ALL (parameter for Yes/No to include in ALL synonym)
- \# DAYS TO KEEP TRACKING DATA ONLINE
- NICKNAME
- UPDATE FIELD (must be YES).

> These are the only fields that must be filled in.

|                                                   |                                                                                                                                                                        |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/019.png) | For an example, please refer to the "Setting Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File" topic in the Installation Procedures chapter of this manual. |

### Setting Up Entries in the VAMC NETWORK HEALTH AUTHORIZED SITES File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following figure (Table 4‑9) shows a sample capture of setting up of entries in the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025) performed at the REDACTEDOffice of Information Field Office (OIFO).

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](network-health-exchange-version-5-installation-guide/020.png)</td>
<td><p>The NAME field is a Free Text field. You must type in the NAME for the site exactly as it is entered in your DOMAIN file (#4.2). For example:</p>
<blockquote>
<p>ANYVAMC.VA.GOV</p>
</blockquote></td>
</tr>
</tbody>
</table>

Select Systems Manager Menu Option: NHEM \<Enter\> Network Health Exchange Manager Menu

Select Network Health Exchange Manager Menu Option: ?

1 Network Health Exchange Add/Edit Sites

2 Network Health Exchange Inquiry

3 Network Health Exchange Options ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Network Health Exchange Manager Menu Option: 1 \<Enter\> Network Health Exchange Add/Edit Sites

Select VAMC NETWORK HEALTH AUTHORIZED SITES NAME: ANOTHERVAMC.VA.GOV

Are you adding 'ANOTHERVAMC.VA.GOV' as

a new VAMC NETWORK HEALTH AUTHORIZED SITES (the 2ND)? YES\<Enter\> (Yes)

VAMC NETWORK HEALTH AUTHORIZED SITES STATION NUMBER: 612

NAME: ANOTHERVAMC.VA.GOV// \<Enter\>

STATION NUMBER: 612// \<Enter\>

NICKNAME: M

INCLUDE IN 'ALL'?: NO\<Enter\> NO

SEND UPDATE TO NETWORK FILE?: YES\<Enter\> YES

\# DAYS TO KEEP TRACKING DATA?: 60

ACCEPT NETWORK FILE UPDATE?: YES\<Enter\> YES

UPDATE NETWORK IDENTIFIER ?: YES\<Enter\> YES

Select VAMC NETWORK HEALTH AUTHORIZED SITES NAME: ANYVAMC.VA.GOV

Are you adding 'ANYVAMC.VA.GOV' as

a new VAMC NETWORK HEALTH AUTHORIZED SITES (the 5TH)? YES\<Enter\> (Yes)

VAMC NETWORK HEALTH AUTHORIZED SITES STATION NUMBER: 662

NAME: ANYVAMC.VA.GOV// \<Enter\>

STATION NUMBER: 662// \<Enter\>

NICKNAME: SF

INCLUDE IN 'ALL'?: NO\<Enter\> NO

SEND UPDATE TO NETWORK FILE?: NO\<Enter\> NO

\# DAYS TO KEEP TRACKING DATA?: 60

ACCEPT NETWORK FILE UPDATE?: NO\<Enter\> NO

UPDATE NETWORK IDENTIFIER ?: NO\<Enter\> NO

<span id="_Ref96417702" class="anchor"></span>Table 4‑9: Setting up entries in the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025)—Sample user dialogue

Next, set up the ALL LOCAL AREA SITES entry in the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025). The STATION NUMBER field should contain all the station numbers (separated by commas) that you wish to contact for NHE data when the ALL LOCAL AREA SITES entry is selected.

Select VAMC NETWORK HEALTH AUTHORIZED SITES NAME: ALL LOCAL AREA SITES

Are you adding 'ALL LOCAL AREA SITES' as

a new VAMC NETWORK HEALTH AUTHORIZED SITES (the 6th)? YES \<Enter\> (Yes)

NAME: ALL LOCAL AREA SITES Replace \<Enter\>

STATION NUMBER: 612,662

NICKNAME: \<Enter\>

INCLUDE IN 'ALL'?: NO\<Enter\> NO

SEND UPDATE TO NETWORK FILE?: NO\<Enter\> NO

\# DAYS TO KEEP TRACKING DATA?: 60

ACCEPT NETWORK FILE UPDATE?: NO\<Enter\> NO

UPDATE NETWORK IDENTIFIER ?: NO\<Enter\> NO

<span id="_Toc96422131" class="anchor"></span>Table 4‑10: Setting up the ALL LOCAL AREA SITES entry—Sample user dialogue

#### Create a Resource Device

> Create a resource device that the service will use. This allows you to limit the number of jobs (resource slots) that will be running (TaskMan jobs), and thus, allows you to avoid overloading the system.

|                                                   |                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/021.png) | For an example, please refer to the "Setting Up a Resource Device" topic in the Installation Procedures chapter of this manual. |

### Setting Up a Resource Device 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of a resource is to provide a mechanism of limiting the number of concurrent jobs that can run at any one time.

When creating a task, the task can request the resource as an input variable for the call. The resource itself, as defined in the DEVICE file (#3.5), has a field called RESOURCE SLOTS that determines how many jobs can own it as a resource simultaneously. RESOURCE SLOTS should be set to one (1), which is the default.

The following figure (Table 4‑11) is a sample capture of setting up a resource device and affixing it to the server option.

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: EVE \<Enter\> Systems Manager Menu

Application Utilities ...

Capacity Management ...

Core Applications ...

Device Management ...

Menu Management ...

Operations Management ...

SYSTEM COMMAND OPTIONS ...

System Security ...

Taskman Management ...

User Management ...

Select Systems Manager Menu Option: DEV \<Enter\> ice Management

Change Device's Terminal Type

Device Edit

Terminal Type Edit

Hunt Group Manager ...

Display Device Data

List Terminal Types

Clear Terminal

Loopback Test of Device Port

Send Test Pattern to Terminal

Out of Service Set/Clear

Current Line/Port Address

DA Return Code Edit

Edit Devices by Specific Types ...

Edit Line/Port Addresses

Line/Port Address report

Select Device Management Option: ED

1 Edit Devices by Specific Types

2 Edit Line/Port Addresses

CHOOSE 1-2: 1 \<Enter\> Edit Devices by Specific Types

CHAN Network Channel Device Edit

HFS Host File Server Device Edit

MT Magtape Device Edit

RES Resource Device Edit

SDP SDP Device Edit

SPL Spool Device Edit

Select Edit Devices by Specific Types Option: RES \<Enter\> Resource Device Edit

Select Resource Device: AFJX RESOURCE

Are you adding 'AFJX RESOURCE' as a new DEVICE? Y \<Enter\> (Yes)

DEVICE LOCATION OF TERMINAL: IRM

DEVICE \$I: AFJX RESOURCE

DEVICE VOLUME SET(CPU): \<Enter\>

DEVICE TYPE: RES \<Enter\> RESOURCES

NAME: AFJX RESOURCE// \<Enter\>

\$I: AFJX RESOURCE// \<Enter\>

VOLUME SET(CPU): \<Enter\>

RESOURCE SLOTS: 1// 1

Select Resource Device: \<Enter\>

CHAN Network Channel Device Edit

HFS Host File Server Device Edit

MT Magtape Device Edit

RES Resource Device Edit

SDP SDP Device Edit

SPL Spool Device Edit

Select Edit Devices by Specific Types Option: \<Enter\>

\>D P^DI

VA FileMan 21.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: OPTION// 19 \<Enter\> OPTION (8267 entries)

EDIT WHICH FIELD: ALL// SERVER DEVICE

THEN EDIT FIELD: \<Enter\>

Select OPTION NAME: AFJXNETP

SERVER DEVICE: AFJX RESOURCE \<Enter\> IRM AFJX RESOURCE

Select OPTION NAME:

<span id="_Ref96418282" class="anchor"></span>Table 4‑11: setting up a resource device and affixing it to the server option

|                                                   |                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/022.png) | The JOB field in the RESOURCE file (#3.54) contains the job currently running on the system for the task and resource device. However, there may be a reason why that job does not get cleared from the field (killjob, etc.). If that is the case, and you are certain the job is not running, then KILL the entry in the field and forward the mail message to the server again. |

#### Add Entries to the VAMC NETWORK PATIENT File

> Run the routines that will add entries to the VAMC NETWORK PATIENT file (#537010) at your site and the other sites in your VISN on the date agreed upon.

> D ^AFJXPATL will send data to be included in the VAMC NETWORK PATIENT file (#537010) to the sites you have added to the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025) and for which you have filled in the fields for UPDATE NETWORK IDENTIFIER and the VAMC NETWORK PATIENT file (#537010). You will only get data from other sites if you fill in the field to accept their updates. You must answer YES for your own site to also get data added from its files to the VAMC NETWORK PATIENT file (#537010). Your own site data must be in this file so that all sites in your network area are synchronized.

> Run Post Init Routines

- If you have been previously running NHE—Run AFJXPPED (i.e., D ^ AFJXPPED) in the background to clean up the VAMC NETWORK PATIENT file (#537010). AFJXPPED goes through the VAMC NETWORK PATIENT file (#537010) and removes any patients in your database with an SSN containing five leading zeroes (00000); leading EEs, ZZs, or a P; or not pattern matching nine numeric characters. NHE screens for five leading zeroes in accordance with VHA Directive 96‑0006 and DG\*5.3\*72.
- If you have never run NHE before at your site—You do *not* need to run this option to clean up the VAMC NETWORK PATIENT file (#537010).

> Seed the VAMC NETWORK PATIENT File

> Coordinate with other sites to select dates and times for seeding the VAMC NETWORK PATIENT file (#537010). Contact the Package Release Manager. Review Implementation Guidelines.

|                                                   |                                                                                                                                                                     |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/023.png) | Records for patients in your database with an SSN containing five leading zeroes (00000), or two leading EEs, ZZs, or a P will *not* be sent across to other sites. |

#### Schedule Background Options to Run Nightly

> The following options should be scheduled to run nightly:

| Option           | Description                                                                                                                      |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| AFJXNH ADD PATIENTS  | Must be scheduled when the system is not busy, e.g., around 3:30 or 4:00 a.m.                                                        |
| AFJXNH PURGE NIGHTLY | Nightly scheduled option to purge messages from NETWORK,HEALTH EXCHANGE User's mailbox. Must be scheduled after AFJXNH ADD PATIENTS. |

<span id="_Toc96422133" class="anchor"></span>Table 4‑12: NHE options to be scheduled nightly

#### Assign Clinical Users to the AFJXNHEX REQUEST Menu Option

> Assign the following menus to the appropriate users:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 39%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Assign Option To</strong></th>
<th><strong>Option</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Clinical Users</td>
<td>Network Health Exchange Options<br />
[AFJXNHEX REQUEST]</td>
<td>This menu comprises options pertaining to the retrieval of patient information from another VAMC site. It permits the retrieval of patient information and allows that information to be viewed onscreen or printed. It is intended for health care professionals who have direct patient care and have need for clinical information.</td>
</tr>
<tr class="even">
<td>Managers</td>
<td>Network Health Exchange Manager<br />
[AFJXNHEX MANAGER]</td>
<td>This menu comprises options to manage the station’s NHE operation and also allow access to retrieve and print patient data from other VA Medical Centers. This menu is intended to be used by individuals responsible for managing the operation of the local Network Health Exchange (NHE) software. The Network Health Exchange Options [AFJXNHEX REQUEST) are also under the Manager menu.</td>
</tr>
</tbody>
</table>

<span id="_Toc96422134" class="anchor"></span>Table 4‑13: NHE menu assignments

> Menus can be assigned using the Systems Manager Menu and the User Edit submenu (for assigning primary or secondary menus).

#### Delete DGY3\* and AFJXI\* Install Routines

> Delete DGY3\* and AFJXI\* install routines when you are confident your installation has been completed correctly.

> You have now completed the NHE installation.

# Post-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                   |                                                                                                   |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------|
| ![](network-health-exchange-version-5-installation-guide/024.png) | This chapter summarizes the information that is presented in the Installation Procedures chapter. |

#### Namespace

The NHE Version 5.1 software uses the "AFJX" namespace.

#### NHE Files

Files for the NHE software are numbered from 537000 to 537025. After you run the install routines, you should have the following files:

| File Number | File Name                   |
|-----------------|---------------------------------|
| 537000          | NETWORK HEALTH EXCHANGE REQUEST |
| 537010          | NETWORK PATIENT                 |
| 537015          | NETWORK HEALTH TYPES            |
| 537025          | NETWORK HEALTH SITES            |

<span id="_Toc96422135" class="anchor"></span>Table 5‑1: NHE file list

#### Nightly Options

| Option           | Description                                                                                                                                |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| AFJXNH ADD PATIENTS  | This option must be scheduled when the system is not busy (e.g., around 3:30 or 4:00 a.m.).                                                    |
| AFJXNH PURGE NIGHTLY | This nightly scheduled option purges messages from the NETWORK,HEALTH EXCHANGE User's mailbox. It must be scheduled to run after ADD PATIENTS. |

<span id="_Toc96422136" class="anchor"></span>Table 5‑2: NHE nightly options

#### Servers

| Server | Description                           |
|------------|-------------------------------------------|
| AFJXNETP   | Network Health Patient Server             |
| AFJXNHDONE | Network Health Exchange Alert Send Server |
| AFJXSERVER | Network Patient Data Request Server       |

<span id="_Toc96422137" class="anchor"></span>Table 5‑3: NHE servers

#### Options

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Option</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AFJXNHEX REQUEST</td>
<td><p><strong>User's Menu</strong>—General options (six) for clinical users. It has the following options:</p>
<ul>
<li><p>Brief (12 months) Medical Record Information</p></li>
<li><p>Total Medical Record Information</p></li>
<li><p>Brief (12 months) Pharmacy Information</p></li>
<li><p>Total Pharmacy Information</p></li>
<li><p>Print (Completed Requests Only)</p></li>
<li><p>Print By Type of Information (Completed Requests)</p></li>
</ul></td>
</tr>
<tr class="even">
<td>AFJXNHEX MANAGER</td>
<td><p><strong>Manager's Menu</strong>—Option for coordinator to add sites and make inquiries and to access the general options menu directly. It has the following options:</p>
<ul>
<li><p>AFJXNHEX ADD/EDIT SITES</p></li>
<li><p>AFJXNHEX INQUIRE</p></li>
<li><p>AFJXNHEX REQUEST</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Toc96422138" class="anchor"></span>Table 5‑4: NHE user and manager options

#### Post Init Routines

Run the following routines after running Inits:

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>AFJXPPED</td>
<td>If you have been previously running NHE—D ^AFJXPPED will run in the background to clean up Network files.</td>
</tr>
<tr class="even">
<td>AFJXPATL</td>
<td><p>To seed the VAMC NETWORK PATIENT file (#537010)—Coordinate with other sites to select dates and times for seeding the VAMC NETWORK PATIENT file (#537010). Contact the Package Release Manager. Review Implementation Guidelines.</p>
<p>D ^AFJXPATL sends data to be included in the VAMC NETWORK PATIENT file (#537010).</p></td>
</tr>
</tbody>
</table>

<span id="_Toc96422139" class="anchor"></span>Table 5‑5: NHE post init routines

Average installations take about 2 minutes when run during the day while users are on the system.

Copy the routines to all systems and volume sets as appropriate for your configuration. Delete the install routines when you are confident your installation has completed successfully.

#### Assign Menus

Assign the following menus to users. Menus can be assigned using the Systems Manager Menu and the User Edit submenu (for assigning primary or secondary menus).

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Menu</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Network Health Exchange Options<br />
[AFJXNHEX REQUEST]</td>
<td>This menu comprises options pertaining to the retrieval of patient information from another VAMC site. It permits the retrieval of patient information and allows that information to be viewed onscreen or printed. It is intended for health care professionals who have direct patient care and have need for clinical information.</td>
</tr>
<tr class="even">
<td>Network Health Exchange Manager<br />
[AFJXNHEX MANAGER]</td>
<td>This menu comprises options to manage the station’s NHE operation and also allow access to retrieve and print patient data from other VA Medical Centers. This menu is intended to be used by individuals responsible for managing the operation of the local Network Health Exchange software. The Network Health Exchange Options (AFJXNHEX REQUEST) are also under the Manager menu.</td>
</tr>
</tbody>
</table>

<span id="_Toc96422140" class="anchor"></span>Table 5‑6: NHE menu assignments

#### Domains/Network Estimates

The NHE software brings in the VAMC NETWORK HEALTH AUTHORIZED SITES file (#537025). Each site needs to populate this file with the domain name of sites with which they plan to share data.

Each site can set local site parameters to manage the length of time that NETWORK,HEALTH EXCHANGE mail messages are retained.

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a capture of an installation of NHE Version 5.1 done at the REDACTEDOffice of Information Field Office (OIFO):

\>D ^XUP

Setting up programmer environment

Access Code: xxxxxxxx

Terminal Type set to: C-VT320

You have 2 new messages.

Select OPTION NAME: \<Enter\>

\>

\>D Q^DI

VA FileMan 21.0

Select OPTION: \<Enter\>

\>

\>W DUZ,!,DUZ(0)

10

@

\>

\>D ^AFJXINST

This version (#5.1) of 'AFJXINIT' was created on 23-JAN-1996

(at REDACTEDISC, by VA FileMan V.21.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

537000 VAMC NETWORK HEALTH EXCHANGE

> **NOTE:** You already have the 'VAMC NETWORK HEALTH EXCHANGE' File.

537010 VAMC NETWORK PATIENT

> **NOTE:** You already have the 'VAMC NETWORK PATIENT' File.

537015 VAMC NETWORK HEALTH TYPES (including data)

> **NOTE:** You already have the 'VAMC NETWORK HEALTH TYPES' File.

I will MERGE your data with mine.

537025 VAMC NETWORK HEALTH AUTHORIZED SITES

> **NOTE:** You already have the 'VAMC NETWORK HEALTH AUTHORIZED SITES' File.

SHALL I WRITE OVER FILE SECURITY CODES? No// NO (No)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? Yes// YES

(Yes)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? Yes// YES (Yes)

ARE YOU SURE EVERYTHING'S OK? No// YES (Yes)

...EXCUSE ME, I'M WORKING AS FAST AS I CAN...............................

'AFJXNETP' Option Filed

'AFJXNH ADD PATIENTS' Option Filed

'AFJXNH PURGE NIGHTLY' Option Filed

'AFJXNHDONE' Option Filed

'AFJXNHEX EDIT SITES' Option Filed

'AFJXNHEX INQUIRE' Option Filed

'AFJXNHEX MANAGER' Option Filed

'AFJXNHEX REQUEST' Option Filed

'AFJXSERVER' Option Filed.

OK, I'M DONE.

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Now installing DG\*5.3\*81

This version (#1) of 'DGY3INIT' was created on 03-JAN-1996

(at REDACTEDISC, by VA FileMan V.21.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

2 PATIENT (Partial Definition)

> **NOTE:** You already have the 'PATIENT' File.

SHALL I WRITE OVER FILE SECURITY CODES? No// NO (No)

ARE YOU SURE EVERYTHING'S OK? No// YES (Yes)

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...............

OK, I'M DONE.

NO SECURITY-CODE PROTECTION HAS BEEN MADE

\>

<span id="_Toc96422141" class="anchor"></span>Table 6‑1: Sample installation