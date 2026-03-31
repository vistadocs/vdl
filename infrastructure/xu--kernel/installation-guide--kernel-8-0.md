---
title: Kernel 8.0 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - kernel
  - strong
  - installation
  - class
  - table
  - span
  - routines
  - install
  - colgroup
  - tbody
page_count: 0
word_count: 8158
section_count: 5
table_count: 44
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: July 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn8_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn8_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

![](kernel-8-0-installation-guide/001.png)

KERNELINSTALLATION GUIDE

July 1995

VistA Health Systems Design & Development (HSD&D)

Infrastructure and Security Services (ISS)

## Revision History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Documentation Revisions

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>07/95</td>
<td>1.0</td>
<td>Initial Kernel V. 8.0 software and documentation release</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/04/05</td>
<td>2.2</td>
<td><p>Kernel V. 8.0 documentation reformatting/revision.<br />
<br />
This is the initial complete reformatting of the <em>Kernel Installation Guide</em> since its original release in July 1995.</p>
<p>Reviewed document and edited for the "Data Scrubbing" and the "PDF 508 Compliance" projects.</p>
<p><strong>Data Scrubbing—</strong>Changed all patient/user TEST data to conform to HSD&amp;D standards and conventions as indicated below:</p>
<ul>
<li><blockquote>
<p>The first three digits (prefix) of any Social Security Numbers (SSN) start with "000" or "666."</p>
</blockquote></li>
<li><blockquote>
<p>Patient or user names are formatted as follows: NHEPATIENT,[N] or NHEUSER,[N] respectively, where the N is a number written out and incremented with each new entry (e.g., NHEPATIENT, ONE, NHEPATIENT, TWO, etc.).</p>
</blockquote></li>
<li><blockquote>
<p>Other personal demographic-related data (e.g., addresses, phones, IP addresses, etc.) were also changed to be generic.</p>
</blockquote></li>
</ul>
<p><strong>PDF 508 Compliance—</strong>The final PDF document was recreated and now supports the minimum requirements to be 508 compliant (i.e., accessibility tags, language selection, alternate text for all images/icons, fully functional Web links, successfully passed Adobe Acrobat Quick Check).</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>02/08/07</td>
<td>2.3</td>
<td><p>Changed Kernel document title references to:</p>
<ul>
<li><blockquote>
<p><em>Kernel Developer's Guide</em> (previously known as the <em>Kernel Programmer Manual</em>).</p>
</blockquote></li>
<li><blockquote>
<p><em>Kernel Systems Management Guide</em> (previously known as the <em>Kernel Systems Manual</em>).</p>
</blockquote></li>
</ul></td>
<td><p>Oakland, CA OIFO:</p>
<ul>
<li><blockquote>
<p>REDACTED</p>
</blockquote></li>
</ul></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc90349009" class="anchor"></span>Table i: Documentation revision history

Patch Revisions

For the current patch history related to this software, please refer to the Patch Module on FORUM.

Contents

Revision History [iii](#revision-history)

Figures and Tables [ix](#figures-and-tables)

Orientation [xi](#orientation)

1\. Introduction [1-1](#introduction)

2\. Preliminary Considerations [2-1](#preliminary-considerations)

3\. Installing Kernel V. 8.0 in a V. 7.1 Environment [3-1](#installing-kernel-v.-8.0-in-a-v.-7.1-environment)

I. Advance Preparation [3-1](#i.-advance-preparation)

1\. Confirm Distribution Files for Kernel V. 8.0 [3-1](#confirm-distribution-files-for-kernel-v.-8.0)

2\. Set Up HFS Device Named "HFS" [3-1](#set-up-hfs-device-named-hfs)

3\. Place ^XPD and ^XTMP [3-1](#place-xpd-and-xtmp)

4\. If You Are Not Using the MICOM: K ^%ZIS("H") [3-2](#if-you-are-not-using-the-micom-k-zish)

5\. Check if Any Kernel Files Have VA FileMan Audits [3-2](#check-if-any-kernel-files-have-va-fileman-audits)

6\. Review Global Protection, Translation and Journaling [3-2](#review-global-protection-translation-and-journaling)

7\. Clean the Task Files (optional) [3-5](#clean-the-task-files-optional)

8\. Identify and Save Locally Modified Routines [3-5](#identify-and-save-locally-modified-routines)

9\. Print Out Current Scheduling Information [3-5](#print-out-current-scheduling-information)

10\. Back Up System as a Safeguard before the Installation [3-6](#back-up-system-as-a-safeguard-before-the-installation)

II\. Installation Instructions [3-7](#ii.-installation-instructions)

1\. Log On [3-7](#log-on)

2\. Set Up Variables [3-7](#set-up-variables)

3\. Stop MailMan Background Filer [3-7](#stop-mailman-background-filer)

4\. Stop TaskMan [3-8](#stop-taskman)

5\. Inhibit Logons [3-8](#inhibit-logons)

6\. Kill Off Remaining Users and Tasks [3-8](#kill-off-remaining-users-and-tasks)

7\. Disable Routine Mapping (DSM for OpenVMS Only) [3-9](#disable-routine-mapping-dsm-for-openvms-only)

8\. Save Old Kernel Routines (MGR) [3-9](#save-old-kernel-routines-mgr)

9\. Check Global Protection for ^%ZOSF [3-10](#check-global-protection-for-zosf)

10\. Lift Global Protection for ^%ZUA [3-10](#lift-global-protection-for-zua)

11\. Clean Old Kernel Routines (MGR) [3-11](#clean-old-kernel-routines-mgr)

12\. Load Manager Routines [3-11](#load-manager-routines)

13\. Run the Manager Setup Routine [3-12](#run-the-manager-setup-routine)

14\. Clean Up Old Kernel Routines (VAH) [3-14](#clean-up-old-kernel-routines-vah)

15\. Install Standalone KIDS Module [3-15](#install-standalone-kids-module)

16\. Load Kernel V. 8.0 Distribution for Production Account [3-17](#load-kernel-v.-8.0-distribution-for-production-account)

17\. Verify Checksums of Loaded Distribution [3-19](#verify-checksums-of-loaded-distribution)

18\. Set Up Variables for Main Installation [3-19](#set-up-variables-for-main-installation)

19\. Install the Kernel Software [3-19](#install-the-kernel-software)

20\. When Main Installation is Done [3-28](#when-main-installation-is-done)

21\. Reset ZU [3-28](#reset-zu)

22\. Manually Update Routines on Other CPUs [3-29](#manually-update-routines-on-other-cpus)

23\. Reset ^%ZTMSH (TaskMan Header Page) Routine [3-30](#reset-ztmsh-taskman-header-page-routine)

24\. Reset Global Protection For ^%ZUA [3-30](#reset-global-protection-for-zua)

25\. Implement Routine Mapping (DSM for OpenVMS only) [3-30](#implement-routine-mapping-dsm-for-openvms-only)

26\. Restart TaskMan [3-31](#restart-taskman)

27\. Enable Logons [3-32](#enable-logons)

28\. Restart MailMan's Background Filer [3-33](#restart-mailmans-background-filer)

III\. Post-Installation Tasks [3-35](#iii.-post-installation-tasks)

1\. Review Site Parameters [3-35](#review-site-parameters)

2\. Review Option Scheduling [3-35](#review-option-scheduling)

3\. Install the OpenVMS EDT or TPU Text Editor (Optional) [3-36](#install-the-openvms-edt-or-tpu-text-editor-optional)

4\. Customize "Edit User Characteristics" (Optional) [3-37](#customize-edit-user-characteristics-optional)

4\. Virgin Installation [4-1](#virgin-installation)

Installation Instructions [4-1](#installation-instructions)

1\. Confirm Distribution Files for Kernel V. 8.0 [4-1](#confirm-distribution-files-for-kernel-v.-8.0-1)

2\. Log On, Using Console Device [4-1](#log-on-using-console-device)

3\. Inhibit Logons/Kill Off Users [4-1](#inhibit-logonskill-off-users)

4\. Set Up Global Protection, Translation and Journaling for Manager's Account Globals [4-2](#set-up-global-protection-translation-and-journaling-for-managers-account-globals)

5\. Check Global Protection for ^%ZOSF [4-2](#check-global-protection-for-zosf-1)

6\. Lift Global Protection for ^%ZUA [4-2](#lift-global-protection-for-zua-1)

7\. Load Manager Routines [4-2](#load-manager-routines-1)

8\. Run the Manager Setup Routine [4-2](#run-the-manager-setup-routine-1)

9\. Install Standalone KIDS Module [4-3](#install-standalone-kids-module-1)

10\. Set Up Variables [4-4](#set-up-variables-1)

11\. Load Kernel V. 8.0 Distribution for Production Account [4-5](#load-kernel-v.-8.0-distribution-for-production-account-1)

12\. Verify Checksums of Loaded Distribution [4-7](#verify-checksums-of-loaded-distribution-1)

13\. Install the Kernel Software [4-7](#install-the-kernel-software-1)

14\. When Main Installation is Done [4-14](#when-main-installation-is-done-1)

15\. Reset ZU [4-14](#reset-zu-1)

16\. Reset Global Protection For ^%ZUA [4-14](#reset-global-protection-for-zua-1)

17\. Implement Routine Mapping (DSM for OpenVMS only) [4-14](#implement-routine-mapping-dsm-for-openvms-only-1)

18\. Global Protection, Translation and Journaling [4-14](#global-protection-translation-and-journaling)

19\. Run ^ZISETUP to Create Devices [4-14](#run-zisetup-to-create-devices)

20\. Finish DEVICE File Entry for Console Device [4-15](#finish-device-file-entry-for-console-device)

21\. Load MailMan Routines [4-15](#load-mailman-routines)

22\. Run ^XVIRPOST Post-Install Routine [4-16](#run-xvirpost-post-install-routine)

23\. Install MailMan [4-16](#install-mailman)

24\. Finish Setting Up First User Account [4-16](#finish-setting-up-first-user-account)

25\. Set Up Device Entries for Virtual Terminals [4-18](#set-up-device-entries-for-virtual-terminals)

26\. Install Kernel Toolkit V. 7.3 [4-18](#install-kernel-toolkit-v.-7.3)

Post-Installation Tasks (Virgin Install) [4-19](#post-installation-tasks-virgin-install)

Appendix A: Installing Kernel on Other Platforms A-[1](#appendix-a-installing-kernel-on-other-platforms)

## Figures and Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

How to Use this Manual

Throughout this manual, advice and instruction are offered about the installation, numerous tools, and functionality that Kernel V. 8.0 provides for overall Veterans Health Information Systems and Technology Architecture (VistA) management. This guide also includes information about software application management (e.g., recommended settings for site parameters and scheduling time frames for tasked options).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/002.png)</td>
<td><strong>CAUTION: To protect the security of VistA systems, distribution of this software for use on any other computer system by VistA sites is prohibited. All requests for copies of Kernel for non-VistA use should be referred to the VistA site's local Office of Information Field Office (OIFO).<br />
<br />
Otherwise, there are no special legal requirements involved in the use of Kernel.</strong></td>
</tr>
</tbody>
</table>

The Kernel Installation Guide is divided into two major sections, based on the following installation types:

1.  Installing Kernel V. 8.0 in a V. 7.1 Environment.
2.  Virgin Installations.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/003.png)</td>
<td><p><strong>REF:</strong> For information on developer tools (e.g., Direct Mode Utilities and Application Program Interfgaces [APIs]), please refer to the <em>Kernel Developer's Guide</em>. Kernel and Toolkit APIs are also available in HTML format at the following Web address:</p>
<blockquote>
<p><a href="http://vista.med.va.gov/kernel/apis/index.shtml">http://vista.med.va.gov/kernel/apis/index.shtml</a></p>
</blockquote>
<p>Information on recommended system configuration and setting Kernel's site parameters, as well as lists of files, routines, options, and other components are documented in the <em>Kernel Technical Manual</em>.</p>
<p>Information about managing computer security, which in cludes a detailed description of techniques that can be used to monitor and audit computing activity, is presented in the <em>Kernel Security Tools Manual</em>.</p></td>
</tr>
</tbody>
</table>

This manual is further organized into the following sections:

> 1\. Advance Preparation

> 2\. Installation Instructions

> 3\. Post-Installation Tasks

This manual uses several methods to highlight different aspects of the material:

- Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                                |                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Symbol                                                                                                     | Description                                                                                                     |
| ![](kernel-8-0-installation-guide/004.png) | NOTE/REF: Used to inform the reader of general information including references to additional reading material. |
| ![](kernel-8-0-installation-guide/005.png)                                                              | CAUTION/DISCLAIMER: Used to caution the reader to take special notice of critical information.                  |

<span id="_Ref345831418" class="anchor"></span>Table ii. Documentation symbol descriptions

- Descriptive text is presented in a proportional font (as represented by this font).
- Conventions for displaying TEST data in this document are as follows:
  - The first three digits (prefix) of any Social Security Numbers (SSN) will begin with either "000" or "666".
  - Patient and user names will be formatted as follows: \[Application Name\]PATIENT,\[N\] and \[Application Name\]USER,\[N\] respectively, where "Application Name" is defined in the Approved Application Abbreviations document and "N" represents the first name as a number spelled out and incremented with each new entry. For example, in Kernel (KRN) test patient and user names would be documented as follows: KRNPATIENT,ONE; KRNPATIENT,TWO; KRNPATIENT,THREE; etc.
- Sample HL7 messages, "snapshots" of computer online displays (i.e., character-based screen captures/dialogues) and computer source code are shown in a *non*-proportional font and enclosed within a box. Also included are Graphical User Interface (GUI) Microsoft Windows images (i.e., dialogues or forms).
- User's responses to online prompts will be boldface.
- References to "\<Enter\>" within these snapshots indicate that the user should press the Enter key on the keyboard. Other special keys are represented within \< \> angle brackets. For example, pressing the PF1 key can be represented as pressing \<PF1\>.
- Author's comments are displayed in italics or as "callout" boxes.

|                                                                                                                |                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/006.png) | NOTE: Callout boxes refer to labels or descriptions usually enclosed within a box, which point to specific areas of a displayed image. |

- This manual refers in many places to the M programming language. Under the 1995 American National Standards Institute (ANSI) standard, M is the primary name of the MUMPS programming language, and MUMPS will be considered an alternate name. This manual uses the name M.
- Descriptions of direct mode utilities are prefaced with the standard M "\>" prompt to emphasize that the call is to be used *only in direct mode*. They also include the M command used to invoke the utility. The following is an example:

> \>D ^XUP

- All uppercase is reserved for the representation of M code, variable names, or the formal name of options, field/file names, and security keys (e.g., the XUPROGMODE key).

|                                                                                                                |                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/007.png) | NOTE: Other software code (e.g., Delphi/Pascal and Java) variable names and file/folder names can be written in lower or mixed case. |

How to Obtain Technical Information Online

Exported VistA M Server-based software file, routine, and global documentation can be generated through the use of Kernel, MailMan, and VA FileMan utilities.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/008.png)</td>
<td><p><strong>NOTE:</strong> Methods of obtaining specific technical information online will be indicated where applicable under the appropriate topic.</p>
<p><strong>REF:</strong> Please refer to the <em>Kernel Technical Manual</em> for further information.</p></td>
</tr>
</tbody>
</table>

Help at Prompts

VistA M Server-based software provides online help and commonly used system default prompts. Users are encouraged to enter question marks at any response prompt. At the end of the help display, you are immediately returned to the point from which you started. This is an easy way to learn about any aspect of VistA M Server-based software.

Obtaining Data Dictionary Listings

Technical information about VistA M Server-based files and the fields in files is stored in data dictionaries (DD). You can use the List File Attributes option on the Data Dictionary Utilities submenu in VA FileMan to print formatted data dictionaries.

|                                                                                                                |                                                                                                                                                                                                                       |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/009.png) | REF: For details about obtaining data dictionaries and about the formats available, please refer to the "List File Attributes" chapter in the "File Management" section of the *VA FileMan Advanced User Manual*. |

Assumptions About the Reader

This manual is written with the assumption that the reader is familiar with the following:

- VistA computing environment:
- Kernel—VistA M Server software
- VA FileMan data structures and terminology—VistA M Server software
- Microsoft Windows environment
- M programming language

This manual provides an overall explanation of Kernel and the functionality contained in Kernel V. 8.0. However, no attempt is made to explain how the overall VistA programming system is integrated and maintained. Such methods and procedures are documented elsewhere. We suggest you look at the various VA home pages on the World Wide Web (WWW) and VA Intranet for a general orientation to VistA. For example, go to the Veterans Health Administration (VHA) Office of Information (OI) Health Systems Design & Development (HSD&D) Home Page at the following Intranet Web address:

> <http://vista.med.va.gov/>

Reference Materials

Readers who wish to learn more about Kernel should consult the following:

- *Kernel Release Notes*
- *Kernel Installation Guide* (this manual)
- *Kernel Systems Management Guide*
- *Kernel Developer's Guide*
- *Kernel Technical Manual*
- *Kernel Security Tools Manual*
- Kernel Home Page at the following Web address:

> <http://vista.med.va.gov/kernel/index.asp>

> This site contains other information and provides links to additional documentation.

If the reader is not already familiar with VA FileMan or MailMan, the respective user, developer, and technical manuals for each should be obtained and reviewed. Other source documents describing overall VistA policy are:

- *VA Programming Standards and Conventions (SAC)*
- *MIRMO/OIFO Operations Document*

VistA documentation is made available online in Microsoft Word format and in Adobe Acrobat Portable Document Format (PDF). The PDF documents *must* be read using the Adobe Acrobat Reader (i.e., ACROREAD.EXE), which is freely distributed by Adobe Systems Incorporated at the following Web address:

> <http://www.adobe.com/>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/010.png)</td>
<td><p><strong>REF:</strong> For more information on the use of the Adobe Acrobat Reader, please refer to the <em>Adobe Acrobat Quick Guide</em> at the following Web address:</p>
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
| ![](kernel-8-0-installation-guide/011.png) | DISCLAIMER: The appearance of external hyperlink references in this manual does *not* constitute endorsement by the Department of Veterans Affairs (VA) of this Web site or the information, products, or services contained therein. The VA does *not* exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of this VA Intranet Service. |

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

  - [Revision History](#revision-history)
  - [Figures and Tables](#figures-and-tables)
  - [Orientation](#orientation)
- [Introduction](#introduction)
- [Preliminary Considerations](#preliminary-considerations)
- [Installing Kernel V. 8.0 in a V. 7.1 Environment](#installing-kernel-v-80-in-a-v-71-environment)
    - [I. Advance Preparation](#i-advance-preparation)
    - [II. Installation Instructions](#ii-installation-instructions)
    - [III. Post-Installation Tasks](#iii-post-installation-tasks)
- [Virgin Installation](#virgin-installation)
    - [Installation Instructions](#installation-instructions)
    - [Post-Installation Tasks (Virgin Install)](#post-installation-tasks-virgin-install)
  - [Appendix A: Installing Kernel on Other Platforms](#appendix-a-installing-kernel-on-other-platforms)
The purpose of this guide is to provide instructions for installing Kernel V. 8.0 (Version 8.0). It outlines the steps necessary to upgrade a computer system from Kernel V. 7.1 to Kernel V. 8.0. In addition, it describes how to install Kernel V. 8.0 on a computer system that does not have a pre-existing version of the Kernel.
Kernel V. 8.0 is installed using a new installation system, Kernel Installation and Distribution System (KIDS). KIDS is new with Kernel V. 8.0, and is a replacement for the previous export and installation system, VA FileMan's DIFROM.
Installation instructions are provided in this guide for the two VA centrally procured operating systems: DSM for OpenVMS and MSM-DOS.
Installation guidelines for other supported M systems (Intersystems M/SQL, DataTree DTM-PC, and MSM-Unix), are provided in an appendix. Kernel no longer actively supports M implementations that aren't expected to support the proposed 1995 ANSI M standard. Implementations in this category are DSM-11, M11+, and M/VX.
In these instructions, "VAH" refers to the Production Account and "MGR" refers to the Library or Manager Account. You may use different names at your site and could pencil them in to avoid confusion later on. Also, for MSM-DOS, a volume set is called a volume group.

# Preliminary Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Disk Space

The Kernel distribution (host file) occupies approximately 4 megabytes of storage space. When the distribution is loaded (into ^XTMP), it occupies approximately 3.3 megabytes. When the Kernel installation is completed, the distribution is purged from the ^XTMP global. The 3.3 megabytes from the ^XTMP global is distributed among Kernel's routines and files by the Kernel installation.

Kernel Components with Separate Installation Procedures

The following Kernel components have their own installation procedures, separate from the main Kernel installation described in this manual:

- File Access Security System (formerly known as Part 3)
- Files for running TaskMan in a DCL context

The conversion procedure to install Kernel's File Access Security system is described in the File Access Security chapter of the *Kernel Systems Management Guide*.

|                                                                                                                |                                                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/012.png) | REF: For information on how to set up Task Manager to run in a DCL Context, please refer to the Task Manager System Management: Configuration chapter of the *Kernel Systems Management Guide*. |

Movement of Kernel Site Parameters

The Kernel V. 8.0 installation moves the Kernel Site Parameters out of ^XMB. They are moved from the MAILMAN SITE PARAMETERS file (#4.3) to the KERNEL SYSTEM PARAMETERS file (#8989.3), which is stored in ^XTV. File \#4.3 remains, containing MailMan's site parameters.

One result of this is that any "Class 3" software that directly modifies the introductory text needs to be aware of its location (in the KERNEL SYSTEM PARAMETERS file \[#8989.3\]).

Movement of Option Scheduling Information

Kernel V. 8.0 moves option scheduling information out of the OPTION file (#19) and into the OPTION SCHEDULING file (#19.2). This provides greater flexibility by allowing a single option to be put on multiple schedules. One issue to note is that after the conversion, to schedule an option, the option's SCHEDULING RECOMMENDED field *must* be set to YES in the OPTION file (#19).

File Access Security Conversion

The File Access Security Conversion (formerly known as Part 3 of the Kernel installation) need not have been run prior to the Kernel V. 8.0 installation. If you have already run the conversion, there is no need to rerun it. Instructions for running the File Access Security Conversion are provided in the File Access Security chapter of the *Kernel Systems Management Guide*. Instructions are not included in the Installation Guide since the conversion is not normally run during the Kernel install.

MICOM Software Support Discontinued

Kernel V. 8.0 no longer supports the MICOM Software that was exported by previous versions of Kernel. While you may continue using this software, it is no longer supported by Kernel, and is no longer considered part of Kernel.

Impact on Journaling

The Kernel installation should not have a significant impact on journaling usage. Kernel does not bring in a significant quantity of data. Three significant conversions are performed:

- Option scheduling is moved out of the OPTION file (#19).
- Alerts are moved out of the NEW PERSON file (#200).
- Kernel site parameters are moved out of the MAILMAN SITE PARAMETERS file (#4.3).

None of these conversions should have a major impact on journaling usage.

Installing Kernel Toolkit After Installing Kernel V. 8.0

You can install Kernel Toolkit V. 7.3 after installing Kernel V. 8.0. If you do this, note the important instructions regarding Kernel V. 8.0 sites in Kernel Toolkit's Preliminary Considerations section (*Kernel Toolkit Installation Guide*). In particular:

- Do *not* install Kernel 7.1 patch \#40.
- Do clean up your production account to remove any remaining unused Kernel manager account routines (ZTMGRSET, ZOSV\*, ZOSF\*, ZTBK\*). This prevents these old routines from overwriting newer manager account routines later in the Kernel Toolkit V. 7.3 installation, when you are asked to move Kernel Toolkit routines from the production to the manager account.

|                                                   |                                                                                                                                                                                                                                                                                                     |
|---------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/013.png) | CAUTION: You should *never* install Kernel Toolkit V. 7.2 on top of Kernel V. 8.0 (doing so would break Kernel V. 8.0). Since a virgin installation of Kernel Toolkit can be done with Kernel Toolkit V. 7.3, there is no reason at all to ever load Kernel Toolkit V. 7.2 on top of Kernel V. 8.0. |

External Relations

Kernel V. 8.0 requires one of the following M implementations to be in place:

- DSM for OpenVMS, version 6.3 or greater.
- Micronetics MSM-DOS, version 4.09 or greater.

|                                                                                                                |                                                                                                                                                          |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/014.png) | REF: For more information on support for other operating systems, please refer to "Appendix A: Installing Kernel on Other Platforms" in this manual. |

A non-virgin installation of Kernel V. 8.0 requires that the following minimal software *must* already be installed on the target (core) system:

- Kernel V. 7.1 or higher.
- Kernel Toolkit V. 7.2 or V. 7.3.
- MailMan V. 7.0 or higher.
- VA FileMan V. 21 (with patch DI\*21\*6 applied) or higher.

A virgin installation of Kernel V. 8.0 requires that the following software *must* be installed or available to install as follows:

- VA FileMan V. 21 (already installed, with patch DI\*21\*6 applied) or higher.
- Kernel Toolkit V. 7.3 (available to install).
- MailMan V. 7.1 or higher (available to install).

Skills Required to Perform the Installation

Instructions for performing these functions are provided in vendor-supplied operating system manuals as well as VistA publications.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/015.png)</td>
<td><strong>REF:</strong> VAX DSM instruction is provided in the <em>VAX DSM Systems Guide</em> (Cookbook).<br />
<br />
MSM-DOS instruction is provided in the <em>486 Cookbook</em> and <em>MSM System Managers Guide</em>.<br />
<br />
<strong>NOTE:</strong> DSM for OpenVMS configurations for Alpha sites are very similar to the configurations for VAX sites.</td>
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

# Installing Kernel V. 8.0 in a V. 7.1 Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to install Kernel V.8.0 in a Kernel V.7.1 environment.

|                                                                                                                |                                                                                                                                                                    |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/016.png) | REF: If you are running on platforms other than DSM for OpenVMS or MSM-DOS, please refer to "Appendix A: Installing Kernel on Other Platforms" in this manual. |

### I. Advance Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Items listed in the Advance Preparation section are tasks that need to be performed in order for Kernel to install successfully. These tasks, however, can and should be performed prior to the *main* installation of Kernel. They can be performed without disabling access to the system or impacting the running system (with possible exception of the last item, backing up the system).

#### Confirm Distribution Files for Kernel V. 8.0

> You should receive the following files with Kernel V. 8.0:

| Name                                                  | Approx. Size (Kilobytes) | Description                                        |
|-----------------------------------------------------------|------------------------------|--------------------------------------------------------|
| KIDS8.RTN                                                 | 100K                         | Standalone KIDS routines.                              |
| KRN8.KID                                                  | 4000K                        | Kernel V. 8.0 Distribution.                            |
| KRN8.MGR                                                  | 265K                         | Kernel Manager account routines.                       |
| The following files only apply for DSM for OpenVMS sites: |                              |                                                        |
| ZTMSWDCL.COM                                              | 1K                           | DCL command file for running TaskMan in a DCL Context. |
| ZTMWDCL.COM                                               | 1K                           | DCL command file for running TaskMan in DCL Context.   |

<span id="_Toc158713821" class="anchor"></span>Table 3‑1: Kernel V. 8.0 distribution files

#### Set Up HFS Device Named "HFS"

> For KIDS to install software, you *must* set up an HFS device, and you *must name the device* "HFS".

|                                                                                                                |                                                                                                                                                                |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/017.png) | REF: For assistance creating HFS devices, please refer to the section on HFS Devices in the "Host Files" chapter of the *Kernel Systems Management Guide*. |

#### Place ^XPD and ^XTMP

> Kernel V. 8.0 brings in a new global, ^XPD. This global is used by KIDS for the BUILD (#9.6) and INSTALL (#9.7) files. These files are relatively static, since they are only updated during KIDS installations. The storage space used would typically be less than 200 kilobytes per installation, depending on the size and complexity of the software being installed. Information in these files can be purged once an installation completes.

> <u>In VAH:</u> Place the ^XPD global in an appropriate volume set on your system. Translate ^XPD across all CPUs.

> <u>In VAH:</u> If ^XTMP is not already placed, it should be placed as well. ^XTMP is the storage location for interprocess temporary data, and should be translated across all CPUs. It is a dynamic global.

#### If You Are Not Using the MICOM: K ^%ZIS("H")

> In previous versions of Kernel, a set of routines, options, and files was distributed to facilitate using the MICOM port contention device. Kernel has discontinued support for the MICOM.

> One part of Kernel's support for the MICOM involved setting a string of code in the global node ^%ZIS("H"). The value of this node varied, depending on what operating system was in use at your site.

> If your site is no longer using the MICOM, kill ^%ZIS("H"), if that node is defined:

> \> W ^%ZIS("H")

> Q

> \> K ^%ZIS("H")

> \>

<span id="_Toc158713822" class="anchor"></span>Figure 3‑1: MICOM sites: Kill ^%ZIS("H")

> If your site configuration has multiple copies of the ^%ZIS global, kill ^%ZIS("H") in every copy of ^%ZIS.

#### Check if Any Kernel Files Have VA FileMan Audits

> You should check to see if any Kernel files have VA FileMan audits enabled. If so, you should consider disabling the audits while running the Kernel installation (for performance and disk usage reasons).

|                                                                                                                |                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/018.png) | REF: A list of Kernel files is provided in the *Kernel Technical Manual*. |

#### Review Global Protection, Translation and Journaling 

> Check the global protection, translation, and journaling characteristics of the Kernel globals on your system. An outline of a possible scheme for the management of Kernel globals is presented on the following pages.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/019.png)</td>
<td><p><strong>REF:</strong> Cookbook recommendations should also be consulted:<br />
<br />
<strong>DSM for OpenVMS:</strong></p>
<p>Refer to the most recent <em>VAX DSM Systems Guide</em> (otherwise known as the VAX Cookbook) for recommendations concerning global characteristics.<br />
<br />
<strong>MSM-DOS:</strong></p>
<p>Refer to the most recent <em>486 Cookbook and MSM System Managers Guide</em> for recommendations concerning global characteristics.</p></td>
</tr>
</tbody>
</table>

> Kernel's recommendations and the cookbooks' recommendations should serve as examples as you manage your site's global configuration.

> Globals in MGR:

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/020.png) | NOTE for MSM-DOS: Kernel recommends that the manager's account should be set up on all servers: file, shadow, compute, and print. Previously, the Kernel manager's account setup was only recommended for print and compute servers. Global characteristics for manager's account globals should be reviewed accordingly, on all servers. |

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 22%" />
<col style="width: 22%" />
<col style="width: 17%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="2"><strong>Protection</strong></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Global Name</strong></th>
<th><strong>DSM for OpenVMS</strong></th>
<th><strong>MSM-DOS</strong></th>
<th><strong>Translate?</strong></th>
<th><strong>Journal?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^%ZIS</td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td>^%ZISL</td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td>^%ZOSF</td>
<td><p>System: RWP</p>
<p>World: R</p>
<p>Group: R</p>
<p>UCI: RWP</p></td>
<td><p>System: RWD</p>
<p>World: R</p>
<p>Group: R</p>
<p>User: RWD</p></td>
<td>Separate Copy per CPU</td>
<td></td>
</tr>
<tr class="even">
<td>^%ZTER</td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td>^%ZTSCH</td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td>All: RWD</td>
<td>Yes <strong>*</strong></td>
<td></td>
</tr>
<tr class="even">
<td>^%ZTSK</td>
<td><p>System: RWP</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>UCI: RWP</p></td>
<td>All: RWD</td>
<td>Yes <strong>*</strong></td>
<td></td>
</tr>
<tr class="odd">
<td>^%ZUA</td>
<td><p>System: RWP</p>
<p>World: R</p>
<p>Group: RW</p>
<p>UCI: RW</p></td>
<td><p>System: RWD</p>
<p>World: RW</p>
<p>Group: RW</p>
<p>User: RWD</p></td>
<td>Yes</td>
<td>Yes</td>
</tr>
</tbody>
</table>

> <span id="_Toc158713823" class="anchor"></span>Table 3‑2: Global settings in MGR

> \* There should be only one copy of the TaskMan globals (^%ZTSCH and ^%ZTSK) within TaskMan's reach. At VA sites, TaskMan's reach is across all CPUs. Other sites should evaluate TaskMan's reach in their configurations.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/021.png)</td>
<td><strong>REF:</strong> For more information about TaskMan's reach, please refer to the <em>Kernel Systems Management Guide</em>.<br />
<br />
<strong>NOTE:</strong> Also, at DSM for OpenVMS sites, these globals should not be in a volume set that is cluster mounted across all systems; instead, master from two nodes and DDP serve to the other nodes.</td>
</tr>
</tbody>
</table>

> Globals in VAH:

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 23%" />
<col style="width: 23%" />
<col style="width: 16%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th colspan="2"><strong>Protection</strong></th>
<th></th>
<th></th>
</tr>
<tr class="odd">
<th><strong>Global Name</strong></th>
<th><strong>DSM for OpenVMS</strong></th>
<th><strong>MSM-DOS</strong></th>
<th><strong>Translate?</strong></th>
<th><strong>Journal?</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^DIC</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td>See VA FileMan Technical Manual</td>
</tr>
<tr class="even">
<td>^HOLIDAY</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td>^TMP</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Separate Copy per CPU</td>
<td></td>
</tr>
<tr class="even">
<td>^UTILITY</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Separate Copy per CPU</td>
<td></td>
</tr>
<tr class="odd">
<td>^VA</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>^XMB</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td>See MailMan Technical Manual</td>
</tr>
<tr class="odd">
<td>^XMBS</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td>See MailMan Technical Manual</td>
</tr>
<tr class="even">
<td>^XPD</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td>^XTV</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td>Yes</td>
</tr>
<tr class="even">
<td>^XTMP</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="odd">
<td>^XUSEC</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Yes</td>
<td></td>
</tr>
<tr class="even">
<td>^XUTL</td>
<td><p>System: RWP</p>
<p>W/G/U: RW</p></td>
<td>All: RWD</td>
<td>Separate Copy per CPU</td>
<td></td>
</tr>
</tbody>
</table>

> <span id="_Toc158713824" class="anchor"></span>Table 3‑3: Global settings in VAH

#### Clean the Task Files (optional)

> For non-virgin installations: So that the post-install can run more quickly, you can optionally purge the task files using the ZTMCLEAN option (i.e., Clean Task File option) on the TaskMan Management Utilities menu. Run this option on each volume set where the TaskMan globals are located.

#### Identify and Save Locally Modified Routines

> If anyone at your site has created any routines within the Kernel namespaces, these routines *must* be saved under a local namespace or they will be overwritten by the incoming Kernel routines. Local development should not use the Kernel namespaces (X\*, Z\* subtracting out ZZ\*), but it would be well to check your accounts beforehand. This check could be done by running the %ZTP1 routine (D ^%ZTP1) to list the first lines of the Kernel routines. Check both the production and the manager's accounts.

> Also, if you have customized your ^%ZTMSH routine for customized TaskMan header pages, save it in a local namespace and then restore it after the installation.

#### Print Out Current Scheduling Information

> Kernel V. 8.0 moves option scheduling information out of the OPTION file (#19) and into the OPTION SCHEDULING file (#19.2). Ordinarily, options will be on the same schedule after the conversion as they were on before the conversion. You may want to print out your current scheduling information from the OPTION file (#19) anyway, in advance of the installation. Then you will be able to compare it to the information in the OPTION SCHEDULING file (#19.2) after the conversion.

#### Back Up System as a Safeguard before the Installation

> You should back up your system before doing the main Kernel installation. It is best to make a backup just before performing the Kernel main installation.

> Optionally, you may also want to save a list of your Kernel routines by running a routine directory (D ^%RD) for the Kernel namespaces (X\*, Z\* subtracting out XM\* and ZZ\*).

Once you have performed the steps in the "Advance Preparation" section, you are ready to begin the Kernel V. 8.0 main installation.

### II. Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to perform the main installation for Kernel V. 8.0. All users and running tasks *must* be shut down as part of the main installation. No users should use the system, nor should any tasks be allowed to run, for the duration of the Kernel V. 8.0 main installation.

#### Log On

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>BEGIN THE INSTALLATION IN THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

- Log on Using the Console

> Log on using the console, since normal logons will later be disabled.

> DSM FOR OpenVMS:

> For speed, log onto the boot node. To maneuver without access restrictions, use a privileged OpenVMS account. Also, create a large symbol table at signon, (\$ DSM/SYM=100000) so there is enough space to work.

> MSM-DOS:

> Log onto the print server, where TaskMan resides, so that queued post-installation tasks will run. Also, when logging on, increase the symbol table size to 100 (UCI,VOL:ROU:100) so that there is enough space to work.

|                                                   |                                                                                                                                                                                                                                            |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/022.png) | CAUTION: It is assumed that you have the capability to move back and forth from the manager and production accounts. After moving to another UCI, it is useful to verify your location (with W \$ZU(0) or other technique) as a safeguard. |

#### Set Up Variables

- <u>In VAH</u>: Set up Variables. Set up your DUZ and set DUZ(0) to "@" using the ^XUP and Q^DI entry points:

> \>D ^XUP *(To set DUZ when responding to the Access Code*

> *prompt. Press Enter at the OPTION prompt.)*

> \>D Q^DI *(To set DUZ(0)="@")*

<span id="_Toc158713825" class="anchor"></span>Figure 3‑2: Set up DUZ and DUZ(0) variables

#### Stop MailMan Background Filer

- <u>In VAH</u>: Stop MailMan. Use MailMan's STOP Background Filer option to shut down MailMan's background filer.

#### Stop TaskMan

- <u>In VAH</u>: Stop TaskMan. Use the Stop Task Manager option on the Taskman Management Utilities menu. Choose to shut down all active Submanagers once they finish their current tasks.

> Select Taskman Management Utilities Option: Stop Task Manager

> Are you sure you want to stop TaskMan? NO// Y

> Shutting down TaskMan.

> Should active submanagers shut down after finishing their current tasks? NO// Y

> Okay!

> Select Taskman Management Utilities Option:

> <span id="_Toc158713826" class="anchor"></span>Figure 3‑3: Stopping TaskMan: Sample user dialogue

#### Inhibit Logons

- <u>In VAH</u>: Inhibit Logons for each Volume Set. You may have local procedures to inhibit logons. In this case, use your local procedures to inhibit logons.  
  >   
  > In the absence of local procedures to disable logons, use VA FileMan (Q^DI entry point) to edit the INHIBIT LOGON field of each entry in the VOLUME SET file (#14.5).

> \>D Q^DI

> INPUT TO WHAT FILE: VOLUME SET

> EDIT WHICH FIELD: ALL// INHIBIT

> THEN EDIT FIELD: \<Enter\>

> <span id="_Toc158713827" class="anchor"></span>Figure 3‑4: Inhibiting logons—All

> DSM FOR OpenVMS:

> Select VOLUME SET: ROU// \<Enter\>

> INHIBIT LOGON?: NO// YES

> <span id="_Toc158713828" class="anchor"></span>Figure 3‑5: Inhibiting logons—DSM FOR OpenVMS

> MSM DOS:

> Select VOLUME SET: CSA// \<Enter\>

> INHIBIT LOGON?: NO// YES

> Select VOLUME SET: CSB// \<Enter\>

> INHIBIT LOGON?: NO// YES

> <span id="_Toc158713829" class="anchor"></span>Figure 3‑6: Inhibiting logons—MSM DOS

#### Kill Off Remaining Users and Tasks

- <u>In VAH</u>: Kill existing users and tasks from the system by killing off their jobs. No users or tasks should be left running on the system during the main Kernel installation. Use Kernel or operating system utilities to clear all users and tasks off of the system, including on other CPUs. The only user on the system should be the user installing Kernel V. 8.0.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE OVER TO THE MANAGER (LIBRARY) ACCOUNT</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

#### Disable Routine Mapping (DSM for OpenVMS Only)

- <u>In MGR</u>: Disable routine mapping (if applicable) on the current node, for library and production accounts.  
  >   
  > You can disable routine mapping on other cluster nodes later, once you start the main installation.

> DSM FOR OpenVMS:

> \>D ^RMAP

> <span id="_Toc158713830" class="anchor"></span>Figure 3‑7: Disabling routine mapping—DSM FOR OpenVMS

> MSM-DOS:

> Not Applicable.

#### Save Old Kernel Routines (MGR)

- <u>In MGR:</u> Optionally, save the current Kernel routines from the MGR account. You can save routines to tape or host file. You will be asked to delete these routines in an upcoming step. The namespaces to save are:

> XUCI\*

> ZT\*

> ZI\*

> ZO\*

> ZU\*

> Also, if you have customized your ^%ZTMSH routine for customized TaskMan header pages, save it in a local namespace (if you haven't already done so) and then restore it after the installation.

#### Check Global Protection for ^%ZOSF

- <u>In MGR</u>: Confirm that the ^%ZOSF global is set appropriately as illustrated below. Each CPU *must* have a separate copy of ^%ZOSF.

> DSM for OpenVMS:

> \>D ^%GLOMAN

> *(Manage globals in which UCI? MGR)*

> ^%ZOSF

> SystemWorld Group UCI

> Protection: RWP R R RWP

<span id="_Toc158713831" class="anchor"></span>Figure 3‑8: Checking global protection for ^%ZOSF—DSM for OpenVMS

> MSM-DOS:

> \>D ^%GCH

> *(Set Protection)*

> ^%ZOSF

> SystemWorld Group User

> Protection: RWD R R RWD

<span id="_Toc158713832" class="anchor"></span>Figure 3‑9: Checking global protection for ^%ZOSF—MSM-DOS

#### Lift Global Protection for ^%ZUA

- <u>In MGR</u>: Lift the protection on ^%ZUA to at least RW across all levels. This allows writing to ^%ZUA during the installation. You will be told to reset the protection after the main installation completes. (^%ZUA holds the logs of failed access attempts and programmer mode entries.) If each CPU has its own ^%ZUA, lift the protection across all CPUs.

> DSM for OpenVMS:

> \>D ^%GLOMAN

> *(Manage globals in which UCI? MGR)*

> ^%ZUA

> SystemWorld Group UCI

> Protection: RWP RW RW RW

<span id="_Toc158713833" class="anchor"></span>Figure 3‑10: Lift global protection for ^%ZUA—DSM for OpenVMS

> MSM-DOS:

> \>D ^%GCH

> *(Set Protection) (Note: no change from recommended setting!)*

> ^%ZUA

> SystemWorldGroup User

> Protection: RWD RW RW RWD

<span id="_Toc158713834" class="anchor"></span>Figure 3‑11: Lift global protection for ^%ZUA—MSM DOS

#### Clean Old Kernel Routines (MGR)

> It is optional but strongly recommended that you delete obsolete Kernel routines from the manager's account before loading in the new ones.

> DSM for OpenVMS:

> Perform this step once, for the cluster.

> MSM-DOS:

> Perform this step on all CPUs that have a manager's account, including *each compute server* and *each print server* (also, each file and shadow server, if those currently have Kernel routines set up in the manager's accounts).

- <u>In MGR</u>: Optionally delete Kernel routines from the Manager account. As a safeguard, you may want to back up the routines to a host file or to tape beforehand.

> \>D ^%ZTRDEL

> XUCI\*

> ZT\*

> ZI\*

> ZO\*

> ZU\*

<span id="_Toc158713835" class="anchor"></span>Figure 3‑12: Delete old Kernel routines in MGR

#### Load Manager Routines

> DSM for OpenVMS:

> Perform this step once, for the cluster.

> MSM-DOS:

> Perform this step on *allCPUs*, meaning each *compute, print, file, and shadow server*.

- <u>In MGR</u>: Restore routines from manager's account distribution file (KRN8.MGR) to the manager's account.

> \>D ^%RR

> Input Device ? \> KRN8.MGR

> Restoring routines from KRN8.MGR

> %ZIS %ZIS1 %ZIS2 %ZIS3 %ZIS5 %ZIS6

> %ZIS7 %ZISC %ZISP %ZISS %ZISS1 %ZISS2

> %ZISUTL %ZTER %ZTER1 %ZTLOAD %ZTLOAD1 %ZTLOAD2 %ZTLOAD3 %ZTLOAD4 %ZTLOAD5 %ZTLOAD6 %ZTLOAD7 %ZTM

> %ZTM0 %ZTM1 %ZTM2 %ZTM3 %ZTM4 %ZTM5

> %ZTM6 %ZTMOVE %ZTMS %ZTMS0 %ZTMS1 %ZTMS2

> %ZTMS3 %ZTMS4 %ZTMS7 %ZTMSH XUCIDTM XUCIMSM

> XUCIMSQ XUCIVXD ZINTEG ZIS4DTM ZIS4MSM ZIS4MSQ ZIS4VXD ZISETDTM ZISETMSM ZISETMSQ ZISETVXD ZISFDTM ZISFMSM ZISFMSQ ZISFVXD ZISHDTM ZISHMSM ZISHMSQ ZISHMSU ZISHUNT ZISHVXD ZISX ZOSFDTM ZOSFMSM ZOSFMSQ ZOSFVXD ZOSV1DTM ZOSV1VXD ZOSV2MSM ZOSV2VXD ZOSVDTM ZOSVMSM ZOSVMSQ ZOSVVXD ZTBKCDTM ZTBKCMSM ZTBKCMSQ ZTBKCVXD ZTMB ZTMCHK ZTMCHK1 ZTMDCL ZTMGRSET ZTMKU ZTMON ZTMON1 ZUA

> \>

<span id="_Toc158713836" class="anchor"></span>Figure 3‑13: Load manager routines

- <u>In MGR</u>: Run the manager's account integrity check routine (^ZINTEG) to verify the integrity of manager's routines. Report any "off-by" discrepancies to your local OIFO before proceeding with installation. Discrepancies may simply indicate that the file includes patched routines.

|                                                                                                                |                                                                                         |
|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/023.png) | NOTE: The ^ZINTEG routine will be removed during the next step (running ^ZTMGRSET). |

> \>D ^ZINTEG

<span id="_Toc158713837" class="anchor"></span>Figure 3‑14: Run the integrity check routine (^ZINTEG) in MGR

#### Run the Manager Setup Routine

> DSM for OpenVMS:

> Perform this step once, for the cluster.

> MSM-DOS:

> Perform this step on all CPUs, which means each *compute, print, file, and shadow server*.

- <u>In MGR</u>: Run the Manager Setup Routine (^ZTMGRSET).  
  >   
  > When asked what M System to install, enter the name of the M implementation you are running. This sets the first piece of ^%ZOSF("OS"). Alpha sites should choose VAX DSM(V6) as their OS.

> ^ZTMGRSET saves %-versions of all routines required for your operating system. ^ZTMGRSET also deletes all non-% routines Kernel routines in the manager's account for operating systems other than your own.

|                                                                                                                |                                                                                                                                                                                                                                 |
|----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/024.png) | NOTE: Because of this, if you run the integrity checker routine for the manager's account *after* running ^ZTMGRSET, it should report missing routines for all operating systems other than your system's operating system. |

> ^ZTMGRSET also asks some questions about your M accounts. Indicate the name and volume set of your Manager account; the name and volume set of your signon Production account; and the name of the current volume or directory set.

> ^ZTMGRSET also sets up two files stored in ^%ZUA, the Failed Access Attempt Log (#3.05) and the Programmer Mode Log (#3.07), if they're not set up already. ^ZTMGRSET also sets up TaskMan's ^%ZTSK global if it is not set up already.

> \>D ^ZTMGRSET

> ZTMGRSET Version 8.0

> HELLO! I exist to assist you in correctly initializing the MGR account or to update the current account.

> I think you are using VAX DSM(V6)

> Which MUMPS system should I install?

> 1 = M/SQL

> 2 = VAX DSM(V6)

> 3 = MSM

> 4 = DataTree

> System: 2// 2 \<Enter\>

> I will now rename a group of routines specific to your operating system.

> Loading ZOSVVXD Saved as %ZOSV

> Loading ZTBKCVXD Saved as %ZTBKC1

> Loading ZIS4VXD Saved as %ZIS4

> Loading ZISHVXD Saved as %ZISH

> Loading XUCIVXD Saved as %XUCI

> Loading ZISETVXD Saved as %ZISETUP

> Loading ZOSV1VXD Saved as %ZOSV1

> Loading ZOSV2VXD Saved as %ZOSV2

> Loading ZISFVXD Saved as %ZISF

> Loading ZTMDCL Saved as %ZTMDCL

> NAME OF MANAGER'S UCI, VOLUME SET: MGR,ROU \<Enter\>

> PRODUCTION (SIGN-ON) UCI, VOLUME SET: VAH,ROU \<Enter\>

> NAME OF VOLUME SET: ROU \<Enter\>

> ALL SET UP

> Now I will check your % globals...........

> ALL SET UP

> ALL DONE

> \>

> <span id="_Toc158713838" class="anchor"></span>Figure 3‑15: Running the manager setup routine (^ZTMGRSET)

|                                                                                                                |                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/025.png) | NOTE: After ^ZTMGRSET has been run to set up the manager's account on a CPU, you can rerun it. When rerun, it does not let you enter the operating system, nor does it re-save OS-specific routines. But it does let you update the UCI and volume set information (which updates the ^%ZOSF nodes for volume set and UCI), should you need to do this. |

> If, on the other hand, you need to rerun ^ZTMGRSET to change the operating system information or reload OS-specific routines, you will need to restore routines first, from the manager's account routine distribution file (KRN8.MGR). Once you restore the full set of routines from the KRN8.MGR, you can then rerun ^ZTMGRSET for a given CPU, and re-answer all of its questions.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Clean Up Old Kernel Routines (VAH)

> It is optional but strongly recommended that you delete obsolete Kernel routines from the production account before the main installation loads in new ones.

> DSM for OpenVMS:

> Perform this step once, for the cluster.

> MSM-DOS:

> Perform this step on *each compute server* and *each print server*.

- <u>In VAH</u>: The routines listed to the right are obsolete. Delete them from the production account.  
  >   
  > As a safeguard, you may want to back up the routines to a host file or to tape beforehand.

> \>D ^%ZTRDEL

> XUCIDSM

> XUCIM11

> XUCIM11P

> XUCIMVX

> XUFII\*

> XUINI\*

> XUTTI\*

> XUINPRE7

> XUINST

> XVIR\*

> ZIS-ZISFVXD

> ZISS\*

> ZO\*

> ZTBK\*

> ZTCPU

> ZTGBL

> ZTLOAD\*

> ZTM\*

> ZTSYINIT

> ZUDSM

> ZUM11

> ZUM11P

> ZUMVX

<span id="_Toc158713839" class="anchor"></span>Figure 3‑16: Clean up old Kernel routines in VAH

#### Install Standalone KIDS Module

> DSM for OpenVMS:

> Install the standalone KIDS module *once*, for the cluster.

> MSM-DOS:

> Install the standalone KIDS module on *each compute server* and *each print server*.

> a\. <u>In VAH</u>: Set up Variables. Set up your DUZ and set DUZ(0) to "@" using the ^XUP and Q^DI entry points:

> \>D ^XUP *(To set DUZ when responding to the Access Code prompt. Press*

> *Enter at the OPTION prompt.)*

> \>D Q^DI *(To set DUZ(0)="@")*

<span id="_Toc158713840" class="anchor"></span>Figure 3‑17: Set up DUZ and DUZ(0) variables in VAH using ^XUP and Q^DI

> b\. <u>In VAH</u>: Restore routines from the standalone KIDS distribution file (KIDS8.RTN) to the production account:

> \>D ^%RR

> Input Device ? \> KIDS8.RTN

> Restoring routines from KIDS8.RTN

> XLFDT XLFDT1 XPDCOM XPDCOMG XPDCPU XPDDCS XPDDI XPDDP XPDE XPDET XPDGCDEL XPDH

> XPDI XPDIA XPDIA1 XPDID XPDIGP XPDIJ

> XPDIK XPDIL XPDIL1 XPDIN001 XPDIN002 XPDIN003 XPDIN004 XPDIN005 XPDIN006 XPDIN007 XPDIN008 XPDIN009 XPDIN00A XPDIN00B XPDIN00C XPDIN00D XPDIN00E XPDIN00F XPDIN00G XPDIN00H XPDIN00I XPDIN00J XPDIN00K XPDIN00L XPDIN00M XPDIN00N XPDIN00O XPDIN00P XPDIN00Q XPDIN00R XPDIN00S XPDIN00T XPDINIT XPDINIT1 XPDINIT2 XPDINIT3 XPDINIT4 XPDINIT5 XPDIP XPDIPM XPDIQ XPDIR XPDIST XPDIU XPDKEY XPDKRN XPDMENU XPDNTEG XPDPINIT XPDR XPDRSUM XPDT XPDTA XPDTA1 XPDTC XPDTP XPDUTL XPDV XQDATE XQH

> XQOO XQOO1 XQOO2 XQOO3

> \>

> <span id="_Toc158713841" class="anchor"></span>Figure 3‑18: Restore routines in VAH

> c\. <u>In VAH</u>: Run the integrity check routine (^XPDNTEG) to verify the integrity of the KIDS routines:

> \>D ^XPDNTEG

> <span id="_Toc158713842" class="anchor"></span>Figure 3‑19: Run the integrity check routine (^XPDNTEG) in VAH

> Report any "off-by" discrepancies to your local OIFO before proceeding with the installation. Discrepancies may simply indicate that the file includes patched routines.

> d\. If you are an MSM-DOS site with multiple CPUs, repeat steps a-c above on *every compute server* and *every print server* so that the standalone KIDS module is installed on all compute and print servers.

> e\. <u>In VAH</u>: Run the KIDS setup routine, ^XPDINIT. You only need to do this on one CPU (not on all CPUs). This routine creates the VA FileMan files used by KIDS.

> Be sure to answer YES to write over file security codes. ^XPDINIT brings in a new file, so you *must* answer yes in order for file security to be applied to it.

> \>D ^XPDINIT

> This version (#8.0) of 'XPDINIT' was created on 22-APR-1995

> (at KERNEL, by VA FileMan V.21.0)

> I AM GOING TO SET UP THE FOLLOWING FILES:

> 9.6 BUILD

> 9.7 INSTALL

> NOTE: This package also contains SORT TEMPLATES

> NOTE: This package also contains INPUT TEMPLATES

> NOTE: This package also contains PRINT TEMPLATES

> NOTE: This package also contains FORMS

> ARE YOU SURE EVERYTHING'S OK? No// Y \<Enter\> (Yes)

> ...SORRY, JUST A MOMENT PLEASE..................

> Compiling form: XPD EDIT BUILD

> OK, I'M DONE.

> NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

> \>

> <span id="_Toc158713843" class="anchor"></span>Figure 3‑20: Running the KIDS setup routine (^XPDINIT)

#### Load Kernel V. 8.0 Distribution for Production Account 

> Once you have installed the standalone KIDS module (previous step), you can use it to load Kernel's production-account distribution.

> a\. <u>In VAH</u>: Set up Variables. Set up your DUZ and set DUZ(0) to "@" using the ^XUP and Q^DI entry points:

> \>D ^XUP *(To set DUZ when responding to the Access Code prompt. Press*

> *Enter at the OPTION prompt.)*

> \>D Q^DI *(To set DUZ(0)="@")*

<span id="_Toc158713844" class="anchor"></span>Figure 3‑21: Set up DUZ and DUZ(0) variables in VAH using ^XUP and Q^DI

> Invoke the ^XPDKRN menu to bring up the Kernel installation menu. Choose the LOAD A DISTRIBUTION option. Enter the appropriate host file name to load the Kernel V. 8.0 production distribution file (KRN8.KID).

> The distribution should contain Kernel V. 8.0 and Kernel - Virgin Install V. 8.0. Answer YES to the "Want to Continue with Load?" prompt.

> KIDS runs the environment check. If it runs successfully, KIDS loads the distribution into ^XTMP, and returns you to the M programmer's prompt. Loading the distribution may take 10 minutes or longer.

> If the environment check fails, however, you *must* determine and correct the condition that caused the failure. Once you have corrected the condition, you need to repeat the steps a-b in this section to load the Kernel distribution.

> Recovering from an Aborted Distribution Load

> If you encounter an error while loading a distribution you will be unable to re-load the distribution until you clear out what was stored during the aborted load attempt.

> To clear out the previously loaded distribution, use the Unload a Distribution option. Choose the distribution to unload. The entries in the INSTALL file (#9.7) for all transport globals in the distribution will be removed, and the transport globals themselves will be purged from the ^XTMP global.

> Once you have unloaded the distribution, you should be able to reload it.

> \> D ^XPDKRN

> Select KIDS OPTION: LOAD A DISTRIBUTION

> Enter a Host File: A:\KRN8.KID

> KIDS Distribution save on Apr 22,1995@10:15:10

> Comment: KERNEL 8.0 from ISC-SF by RSD

> This Distribution contains the following Build(s):

> KERNEL - VIRGIN INSTALL 8.0

> KERNEL 8.0

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> Insert the next diskette, \#2, and Press the return key: \<Enter\>

> Insert the next diskette, \#3, and Press the return key: \<Enter\>

> Will first run the Environment Check Routine, XVIRENV

> KERNEL - VIRGIN INSTALL 8.0 Build will not be installed, Transport Global deleted!

> Will first run the Environment Check Routine, XUINOK

> I'm checking to see if it is OK to install KERNEL v8.0 in this account.

> Checking the %ZOSV routine

> Everything looks OK, Lets continue.

> Use Kernel 8.0 to install this distribution.

> \>

> <span id="_Toc158713845" class="anchor"></span>Figure 3‑22: Loading the Kernel distribution—Sample user dialogue

#### Verify Checksums of Loaded Distribution

- <u>In VAH</u>: Invoke ^XPDKRN. Use the VERIFY CHECKSUMS IN TRANSPORT GLOBAL option to verify the integrity of the Kernel distribution:

> \>D ^XPDKRN

> KIDS 8.0

> Select KIDS OPTION: VERIFY \<Enter\> CHECKSUMS OF TRANSPORT GLOBAL

> Select INSTALL NAME: Kernel 8.0

> DEVICE: HOME// \<Enter\>

> PACKAGE: KERNEL 8.0 Apr 22, 1995 7:17 am Page 1

> -------------------------------------------------------------------

> 319 Routine checked, 0 failed.

> \>

<span id="_Toc158713846" class="anchor"></span>Figure 3‑23: Verify checksums—Sample user dialogue

> Report any "off-by" discrepancies to your local OIFO before installing Kernel. Discrepancies may simply indicate that the distribution includes patched routines.

#### Set Up Variables for Main Installation

> Choose what system you are going to perform the main installation on, and log on to that system. This installation is performed on one system only, regardless of whether you are an MSM-DOS or DSM for OpenVMS site.

- <u>In VAH</u>: Set up Variables Again. Set up your DUZ and set DUZ(0) to "@" again using the ^XUP and Q^DI entry points:

> \>D ^XUP *(To set DUZ when responding to the Access Code prompt. Press Enter*

> *at the OPTION prompt.)*

> \>D Q^DI *(To set DUZ(0)="@")*

<span id="_Toc158713847" class="anchor"></span>Figure 3‑24: Set up DUZ and DUZ(0) variables in VAH using ^XUP and Q^DI

> Also, make sure you are logged on with an expanded symbol table as described at the start of the installation instructions.

#### Install the Kernel Software

- <u>In VAH</u>: Install Kernel.

> Invoke the ^XPDKRN routine. Choose the INSTALL PACKAGE(S) option. Select KERNEL 8.0 as the software you want to install.

> KIDS runs Kernel's environment check routine a second time (the first time was when the distribution was loaded). If the environment check runs successfully, you may proceed with the main Kernel installation.

> If the environment check fails, you need to correct the condition that caused it to fail. You may also need to reload the Kernel distribution if it was purged when the environment check failed.

> Annotated Installation Dialogue

> An annotated text of the installation dialogue is listed on the following pages. It may not be an exact match of what you will see when running your installation. It is provided as a best approximation of a typical install. Explanatory notes are provided along with the dialogue that may give some indication as to why your experience may differ from the example presented here.

> \> D ^XPDKRN

> KIDS 8.0

> Select KIDS OPTION: INSTALL PACKAGE \<Enter\>(S)

> Select INSTALL NAME: KERNEL 8.0 \<Enter\> Loaded from Distribution

> This Distribution was loaded on Apr 22, 1995@13:20:44 with header of KERNEL FROM KRN,KDE

> The tape consisted of the following Install(s):

> KERNEL 8.0

> Will first run the Environment Check Routine, XUINOK

> I'm checking to see if it is OK to install KERNEL v8.0 in this account.

> Checking the %ZOSV routine

> Now to check protection on GLOBALS.

> If you get an ERROR, you need to add Write access to that global.

> Checking ^%ZIS

> Checking ^%ZISL

> Checking ^%ZTER

> Checking ^%ZUA

> Everything looks OK, Lets continue.

> Install Questions for KERNEL 8.0

> 3 USER

> Note: You already have the 'USER' File.

> 3.05 FAILED ACCESS ATTEMPTS LOG

> Note: You already have the 'FAILED ACCESS ATTEMPTS LOG' File.

> 3.07 PROGRAMMER MODE LOG

> Note: You already have the 'PROGRAMMER MODE LOG' File.

> 3.075 ERROR LOG

> Note: You already have the 'ERROR LOG' File.

> 3.076 ERROR MESSAGES (including data)

> Note: You already have the 'ERROR MESSAGES' File.

> I will MERGE my data with yours.

> 3.081 SIGN-ON LOG

> Note: You already have the 'SIGN-ON LOG' File.

> 3.1 TITLE

> Note: You already have the 'TITLE' File.

> 3.2 TERMINAL TYPE

> Note: You already have the 'TERMINAL TYPE' File.

> Want my data to overwrite yours? YES// \<Enter\>

> 3.22 DA RETURN CODES (including data)

> Note: You already have the 'DA RETURN CODES' File.

> Want my data merged with yours? YES// \<Enter\>

> 3.23 LINE/PORT ADDRESS

> 3.5 DEVICE

> Note: You already have the 'DEVICE' File.

> 3.51 SPOOL DOCUMENT

> Note: You already have the 'SPOOL DOCUMENT' File.

> 3.519 SPOOL DATA

> Note: You already have the 'SPOOL DATA' File.

> 3.54 RESOURCE

> Note: You already have the 'RESOURCE' File.

> 3.6 BULLETIN

> Note: You already have the 'BULLETIN' File.

> 4 INSTITUTION

> Note: You already have the 'INSTITUTION' File.

> 4.1 FACILITY TYPE (including data)

> Note: You already have the 'FACILITY TYPE' File.

> Want my data merged with yours? YES// \<Enter\>

> 4.11 AGENCY (including data)

> Note: You already have the 'AGENCY' File.

> Want my data to overwrite yours? YES// \<Enter\>

> 4.3 KERNEL SITE PARAMETERS

> Note: You already have the 'KERNEL SITE PARAMETERS' File.

> 6 PROVIDER

> Note: You already have the 'PROVIDER' File.

> 9.2 HELP FRAME

> Note: You already have the 'HELP FRAME' File.

> 9.4 PACKAGE

> Note: You already have the 'PACKAGE' File.

> 9.6 BUILD

> Note: You already have the 'BUILD' File.

> 9.7 INSTALL

> Note: You already have the 'INSTALL' File.

> 9.8 ROUTINE

> Note: You already have the 'ROUTINE' File.

> 14.4 TASKS

> 14.5 VOLUME SET

> Note: You already have the 'VOLUME SET' File.

> 14.6 UCI ASSOCIATION

> Note: You already have the 'UCI ASSOCIATION' File.

> 14.7 TASKMAN SITE PARAMETERS

> Note: You already have the 'TASKMAN SITE PARAMETERS' File.

> 14.8 TASK SYNC FLAG

> 16 PERSON

> Note: You already have the 'PERSON' File.

> 19 OPTION

> Note: You already have the 'OPTION' File.

> 19.081 AUDIT LOG FOR OPTIONS

> Note: You already have the 'AUDIT LOG FOR OPTIONS' File.

> 19.1 SECURITY KEY

> Note: You already have the 'SECURITY KEY' File.

> 19.2 OPTION SCHEDULING

> 40.5 HOLIDAY

> Note: You already have the 'HOLIDAY' File.

> 49 SERVICE/SECTION

> Note: You already have the 'SERVICE/SECTION' File.

> 200 NEW PERSON

> Note: You already have the 'NEW PERSON' File.

> 8989.2 KERNEL PARAMETERS

> 8989.3 KERNEL SYSTEM PARAMETERS

> 8991.5 XQAB ERRORS LOGGED

> 8992 ALERT

> 8992.1 ALERT TRACKING

> Want to MOVE routines to other CPUs? NO// YES

> Please enter the VOLUME SETS you want to update.

> *Note: Your system configuration may differ!*

> Select VOLUME SET: PSB

> Are you adding 'PSB' as a new VOLUME SET (the 1st

> for this install)? Y \<Enter\> ES

> Select VOLUME SET: CSA

> Are you adding 'CSA' as a new VOLUME SET (the 2nd

> for this install)? Y \<Enter\> ES

> Select VOLUME SET: CSB

> Are you adding 'CSB' as a new VOLUME SET (the 3rd

> for this install)? Y \<Enter\> ES

> Select VOLUME SET: CSC

> Are you adding 'CSC' as a new VOLUME SET (the 4th

> for this install)? Y \<Enter\> ES

> Select VOLUME SET: \<Enter\>

> TASKMAN is not running. You must run the routine XPDCPU in the production UCI for each of the VOLUME SETS you have listed, once the installation starts.

> Enter the Device you want to print the Install messages. You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// \<Enter\> DECSERVER

> Install Started:

> Apr 22, 1995@13:22:21

> <span id="_Toc158713848" class="anchor"></span>Figure 3‑25: Example of an installation done at the San Francisco OIFO

> MSM-DOS (with multiple compute and print servers):

> Once you have selected a device and see the "Install Started" message, *you should switch* to your other compute and print servers and run ^XPDCPU. Ideally, you should start ^XPDCPU on each print server and compute server (other than the CPU the main installation is running on) *before* the main installation finishes.

|                                                                                                                |                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/026.png) | NOTE: ^XPDCPU does not need to finish before the main installation does, it only needs to be started. See "While Main Installation is Running (Multi-CPU Systems)" later in this section for further instructions on running ^XPDCPU. |

> You have now answered all the installation questions (the pre-install and post-install routines do not ask any questions when they run). The installation runs, with its output going to the device that you specify. A sample of the installation output is listed below, again in annotated format.

> This output will scroll in a window if the installation is run on a VT100- (or higher) compatible terminal. Below the scrolling window, there is a graphical progress bar showing % completion figures for most parts of the installation, as shown on the following page.

> If you are installing from a terminal that is not VT100-compatible, installation progress is noted using the traditional dots method (.....).

> A full sample installation dialog is listed on the following pages.

> ![](kernel-8-0-installation-guide/027.png)

> <span id="_Toc158713849" class="anchor"></span>Figure 3‑26: KIDS Installation Window

> DEVICE: HOME// \<Enter\> DECSERVER

> Install Started:

> Apr 22, 1995@13:22:21

> Installing Routines:

> Apr 22, 1995@13:24:08

> Running Pre-Install Routine: ^XUINPRE

> Clean up dangling 99 nodes in the OPTION File.

> Installing Data Dictionaries: ...

> Apr 22, 1995@13:28:31

> Installing Data:

> Apr 22, 1995@13:29:24

> Installing PACKAGE COMPONENTS:

> Installing HELP FRAME

> Installing BULLETIN

> Installing SECURITY KEY

> Installing FUNCTION

> Installing PRINT TEMPLATE

> Installing SORT TEMPLATE

> Installing INPUT TEMPLATE

> Installing FORM

> Installing OPTION

> Apr 22, 1995@13:42:32

> Running Post-Install Routine: ^XUINEND

> Move KERNEL site parameters.

> Moving ALERTS from file 200 to file 8992...

> Delete CPU field from alpha/beta test sites

> Option Scheduling conversion.

> Beginning TaskMan's post-init conversion...

> Option:XMCLEAN move to new file.

> .

> .

> .

> Option: XUCM TASK NIT move to new file.

> End of TaskMan's post-init conversion.

> Check and clean out XUFILE if not running FOF.

> Load PARAM file

> TO PROTECT THE SECURITY OF DHCP SYSTEMS, DISTRIBUTION OF THIS SOFTWARE FOR USE ON ANY OTHER COMPUTER SYSTEM IS PROHIBITED. ALL REQUESTS FOR COPIES OF THE KERNEL FOR NON-DHCP USE SHOULD

> BE REFERRED TO YOUR LOCAL ISC.

> Updating Routine file... ...

> Updating KIDS files... ....

> KERNEL 8.0 Installed.

> Apr 22, 1995@13:48:28

> Install Message sent \# 983674

<span id="_Toc158713850" class="anchor"></span>Figure 3‑27: Example of an installation done at the San Francisco OIFO

#### While Main Installation is Running (Multi-CPU Systems)

> You should perform the following steps on other CPUs while the main installation runs on the first CPU:

> MSM-DOS:

> If you answered "YES" to the "Want to MOVE routines to other CPUs?" question during the main installation, you should run the ^XPDCPU routine on all print and compute servers you asked to update after you answered YES. You should start ^XPDCPU while the main installation is running.

- <u>In VAH</u>: Start ^XPDCPU on every compute and print server *other* than the one the main installation is running on (assuming you listed these CPUs to be updated when asked by the main installation). In each case, start it while the main installation is still running. Enter Kernel 8.0 when prompted for an INSTALL name. ^XPDCPU will then load routines, recompile templates, and queue a menu tree rebuild:

> \>D ^XPDCPU

> Select INSTALL NAME: Kernel 8.0

> Loading Routines

> Recompiling Template routines

> Queuing Menu Tree Rebuild

> \>

<span id="_Toc158713851" class="anchor"></span>Figure 3‑28: Running ^XPDCPU in VAH

> ^XPDCPU will not be able to complete the update of routines on other CPUs in the following situations:

- You answered NO to the "move routines to other CPUs" question, or, if you answered yes, you didn't list every CPU that needed updating.
- You didn't start ^XPDCPU on a CPU before the main installation completed.
- An error occurred during the updating of a CPU.

> In these cases, you need to wait until after the main installation completes; then, manually update routines on the other compute and print servers. See "Manually Update Routines on Other CPUs" in the list of tasks to perform when the main installation is done for more information.

> DSM for OpenVMS:

- <u>In VAH and MGR</u>: Disable routine mapping on all nodes other than the one the one that the main installation is running on.

#### If the Main Installation Errors Out

> If the Main Installation errors out, first determine the cause of the problem. Once you have found the problem and corrected it, invoke ^XPDKRN and use the RESTART INSTALL OF PACKAGE(S) option to restart the Kernel installation.

> KIDS provides the ability to restart installations that errored out at the point they errored out. This saves you, the installer, from having to re-run the entire installation over again. When you restart an aborted installation using RESTART INSTALL OF PACKAGE(S), the installation resumes from the last completed checkpoint.

#### When Main Installation is Done

> When the main installation is done, more steps need to be performed to finish setting up Kernel V. 8.0.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>CONTINUE WORKING IN THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Reset ZU

- <u>In VAH</u>: Save ZU by renaming your operating system-specific ZU routine. (You may also optionally save ZU in the Manager's account so that global protect errors will be trapped and displayed if they should occur).  
  >   
  > On multi-CPU MSM-DOS systems, you will need to reload ZU on *each print server and compute server*.

> DSM FOR OpenVMS:

> \>ZL ZUVXD ZS ZU

<span id="_Toc158713852" class="anchor"></span>Figure 3‑29: Saving ZU—DSM FOR OpenVMS

> MSM-DOS:

> \>ZL ZUMSM ZS ZU

<span id="_Toc158713853" class="anchor"></span>Figure 3‑30: Saving ZU—MSM-DOS

#### Manually Update Routines on Other CPUs

> This step is only for sites whose system has print or compute servers beyond the one that the main installation ran on. You only need to perform this step if:

- You answered NO to the "move routines to other CPUs" question, or, if you answered yes, you didn't list every CPU that needed updating.
- An error occurred during the updating of a CPU.
- You didn't start ^XPDCPU on a CPU before the main installation completed.
- You are a DSM for OpenVMS site. DSM for OpenVMS sites can't move routines to other CPUs during the main installation, but can use the manual method afterwards (for unusual CPU configurations).

> If any of these situations occur, then the routines, compiled templates, and compiled cross-references need to be manually updated on those CPU(s). To do this, perform the manual update as follows:

> a\. <u>In VAH:</u> Run the utility MOVE^XPDCPU once, on the system where the main installation completed. Enter Kernel 8.0 when prompted for an install name. This utility copies all the routines that need updating (including compiled templates and cross-references) into ^XTMP.

> \> D MOVE^XPDCPU

> Select INSTALL NAME: KERNEL 8.0

> Want to move the Routine for this Package to another CPU? YES// \<Enter\>

> Run INSTALL^XPDCPU on the other CPU to install the Routines.

> \>

> <span id="_Toc158713854" class="anchor"></span>Figure 3‑31: Running the MOVE^XPDCPU utility in VAH

> b\. <u>In VAH:</u> On each CPU that didn't get updated by ^XPDCPU during the main installation, run the utility INSTALL^XPDCPU. This loads routines from ^XTMP (where they were placed by MOVE^XPDCPU above) onto the CPU that INSTALL^XPDCPU is being run on.

> \> D INSTALL^XPDCPU

> Select INSTALL NAME: KERNEL 8.0 \<Enter\> Install Completed

> Want to install the Routine for this Package? YES// \<Enter\>

> Done

> \>

> <span id="_Toc158713855" class="anchor"></span>Figure 3‑32: Running the INSTALL^XPDCPU utility in VAH

> c\. Rebuild menus on each CPU that you have manually updated. To do this, run Kernel's Build Primary Menu Trees option.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE MANAGER (LIBRARY) ACCOUNT</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

#### Reset ^%ZTMSH (TaskMan Header Page) Routine

- <u>In MGR</u>: If you have been using a local TaskMan header page (by customizing the ^%ZTMSH routine), reload your local version of the ^%ZTMSH routine.

#### Reset Global Protection For ^%ZUA

- <u>In MGR</u>: Reset global protections for ^%ZUA. The ^%ZUA global should be cluster mounted/translated across all CPUs.

> DSM for OpenVMS:

> \>D ^%GLOMAN \<Enter\>

> *(Manage globals in which UCI? MGR)*

> ^%ZUA

> SystemWorld Group UCI

> Cluster Mounted: RWP R RW RW

<span id="_Toc158713856" class="anchor"></span>Figure 3‑33: Reset global protections for ^%ZUA—DSM for OpenVMS

> MSM-DOS:

> This is the same protection level that was set before the Kernel Installation.

> \>D ^%GCH \<Enter\>

> *(Set Protection)*

> ^%ZUA

> SystemWorld Group User

> Translated across CPUs: RWD RW RW RWD

<span id="_Toc158713857" class="anchor"></span>Figure 3‑34: Reset global protections for ^%ZUA—MSM DOS

#### Implement Routine Mapping (DSM for OpenVMS only)

- Map routines in the Manager account. The recommended set is listed below. (At a future time, you should run RTHIST reports to identify the set of routines that are used most frequently at your site. The set provided here is only a "best guess" of which routines might be worth mapping.)

> DSM FOR OpenVMS:

> Edit your command file for building mapped routine sets, and then run it.

> MSM-DOS:

> Not Applicable.

> %ZIS %ZIS1 %ZIS2 %ZIS3 %ZIS4

> %ZIS5 %ZIS6 %ZISC

> %ZOSV (*To avoid potential problems, do not map %ZOSV if you are running a version of VAX DSM less than V6.)*

> %ZTLOAD %ZTLOAD1 %ZTLOAD2 %ZTM %ZTM1

> %ZTM2 %ZTM4 %ZTM5 %ZTMS %ZTMS0

> %ZTMS1 %ZTMS2 %ZTMS3 %ZTMS4 %ZTMS7

- Map routines in the Production account. The recommended set is listed below.  
  >   
  > (At a future time, you should run RTHIST reports to identify the set of routines that are used most frequently at your site. The lists provided below are only "best guesses" of which routines might be worth mapping.)

> DSM FOR OpenVMS:

> Edit your command file for building mapped routine sets, and then run it.

> MSM-DOS:

> Not Applicable.

> XQ XQ1 XQ2 XQ12 XQ7

> XQ71 XQ72 XQ73 XQ74 XQ75

> XQ83 XQCHK XQDATE XQH XQH1

> XQH2 XQSET XQT XQT1

> XUS XUS1 XUS3 XUSCLEAN

> XUSHSH ZU

- Activate Mapped Routine Sets. Check your DSM for OpenVMS documentation for the correct procedures necessary to activate the updated mapped routine sets. If you have a multi-CPU system, activate mapping on all CPUs.

#### Restart TaskMan

- <u>In MGR</u>: Check the system status to see whether TaskMan is running.

> DSM for OpenVMS:

> For DSM for OpenVMS sites, TaskMan should have started when you rebooted to activate new mapped routine sets. Check the System Status (e.g., D ^%SY). If there is no %ZTM\* routine running,

> \>D ^ZTMB

> MSM-DOS:

> For MSM-DOS systems, you need to restart it manually. Check the System Status (e.g., D ^%SS). If there is no %ZTM\* routine running,

> \>D ^ZTMB

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Enable Logons

- <u>In VAH</u>: Enable logons from the VOLUME SET file (#14.5). This also allows TaskMan to start tasks.

> If you have local procedures to enable logons, follow those procedures to enable logons. Otherwise, if you disabled logons before the Kernel installation by editing the INHIBIT LOGON field in the Volume Set file (#14.5) for each Volume set, then edit those fields again to enable logons.

|                                                                                                                |                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/028.png) | NOTE: A menu tree rebuild will be triggered because of the extensive modifications to the menus made during the Kernel installation. While the menu trees are rebuilding, menu jumping will be disabled. |

- <u>In VAH</u>: Edit the INHIBIT LOGON field of the VOLUME SET file (#14.5) to properly enable/disable logons.

> \>D Q^DI

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: VOLUME SET

> EDIT WHICH FIELD: ALL// INHIBIT LOGONS?

> THEN EDIT FIELD: \<Enter\>

> <span id="_Toc158713858" class="anchor"></span>Figure 3‑35: Enabling logons—All

> DSM FOR OpenVMS:

> Select VOLUME SET: ROU

> INHIBIT LOGON?: YES// NO

> <span id="_Toc158713859" class="anchor"></span>Figure 3‑36: Enabling logons—DSM FOR OpenVMS

> MSM DOS:

> Select VOLUME SET: CSA

> INHIBIT LOGON?: YES// NO

> Select VOLUME SET: CSB

> INHIBIT LOGON?: YES// NO

> <span id="_Toc158713860" class="anchor"></span>Figure 3‑37: Enabling logons—MSM DOS

#### Restart MailMan's Background Filer

- <u>In VAH</u>: If you are running MailMan, restart its background filer with MailMan's START Background Filer option.

The Kernel V. 8.0 Installation is now done. Please see the following section for post-installation tasks.

### III. Post-Installation Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You should perform the following tasks after the Kernel V. 8.0 installation is completed. Users can be allowed back on the system and tasks can be allowed to run as you perform the steps in this section.

#### Review Site Parameters

> Use the Enter/Edit Kernel Site Parameters option on the Operation menu to set or adjust defaults. Type two question marks for a description of the field and suggested defaults. (Operations Management -\> Kernel Management Menu -\> Enter/Edit Kernel Site Parameters.)

|                                                                                                                |                                                                                                                               |
|----------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/029.png) | REF: For more information, please refer to the "Implementation and Maintenance" section of the *Kernel Technical Manual*. |

#### Review Option Scheduling

> Review schedules for queued options to be sure they are appropriate. Kernel does not export any scheduling data with its options. IRM *must* determine the appropriate option scheduling for the site.

> You can run two reports to help review the current scheduling of options. From the TaskMan Management menu, the Print Recommended for Queueing Options report lists all the options that developers (Kernel and other VistA software application) recommend for regular scheduling. The Print Options that are Scheduled to run option lists all options on your system that are currently scheduled.

> Kernel recommends that the following Kernel options be scheduled with the following frequencies:

| Option              | Frequency | Option Text                                     |
|-------------------------|---------------|-----------------------------------------------------|
| XQALERT DELETE OLD      | 1D            | Delete Old (\>14 d) Alerts                          |
| XQBUILDTREEQUE          | 2D            | Non-interactive Build Primary Menu Trees            |
| XQ XUTL \$J NODES       | 7D            | Clean old Job Nodes in XUTL                         |
| XUAUTODEACTIVATE        | 1D            | Automatic Deactivation of Users                     |
| XUERTRP PRINT T-1 1 ERR | 1D            | P1 Print 1 occurrence of each error for T-1 (QUEUE) |
| XUERTRP PRINT T-1 2 ERR | 1D            | P2 Print 2 occurrences of errors on T-1 (QUEUE)     |
| XUSAZONK                | 15D           | Purge of the %ZUA global                            |
| XUSCZONK                | 1D            | Purge Sign-on log                                   |
| XUTM QCLEAN             | 1D            | Queuable Task Log Cleanup                           |
| XU-SPL-PURGE            | 7D            | Purge old spool documents                           |

> <span id="_Toc158713861" class="anchor"></span>Table 3‑4: Kernel options—Recommended scheduling frequency

> To schedule these options, use Schedule/Unschedule Options on the Taskman Management menu.

> Other Option Scheduling Recommendations

- You can use the SPECIAL QUEUING field to set up the XUSER-CLEAR-ALL option to run whenever TaskMan starts up. This option clears all users signed on from the multiple sign-on restriction. This can be useful when M crashes; without running this option, anyone who was signed on before M crashed would be unable to logon afterwards depending on their multiple sign-on restriction. With this option set, however, whenever TaskMan starts up (typically when starting up the VistA system), any leftover sign-on information from before a crash is automatically cleaned out.
- MSM-DOS sites that run TaskMan only on the Print Server should schedule the XU-486 MENU COPY option to run after the menu tree rebuild has finished on the Print Server.
- Although the XT-PURGE ERRORS (Clean Error Trap) option *cannot* be scheduled to run (since it is interactive), you may want to invoke it at periodic intervals as appropriate at your site.
- The XUSERAOLD (Purge Log of Old Access and Verify Codes) option can be queued, but it is up to the site to determine how often the history of access and verify codes is purged.
- Review settings for option restriction to be sure they are appropriate. There are a variety of ways that you can restrict or prohibit option usage. Menu Manager's Edit Options can be used edit an option's settings. You can require, for example, that the output of a job be queued to run during certain time periods. The ^%INDEX option would be a candidate for such a restriction.

|                                                                                                                |                                                                                                                                                                  |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/030.png) | REF: For more information on restricting option usage, please refer to the Menu Manager: System Management chapter of the *Kernel Systems Management Guide*. |

#### Install the OpenVMS EDT or TPU Text Editor (Optional)

> DSM for OpenVMS:

> DSM for OpenVMS sites can choose to make the OpenVMS EDT and/or TPU text editor available to users as alternate editors. This is accomplished by making an entry in the ALTERNATE EDITOR file (#1.2) as shown below (Figure 3‑38).

> The EDT and TPU editors can both read and write host files on OpenVMS systems, and so should be given out only after considering file protections and the security of host files on your system. Unless proper file protections have been applied to all host files on your system, the EDT and TPU editors should not be given out beyond system management staff.

> \>D Q^DI

> VA FileMan 21

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> INPUT TO WHAT FILE: 1.2 \<Enter\> ALTERNATE EDITOR (2 entries)

> EDIT WHICH FIELD: ALL// \<Enter\>

> Select ALTERNATE EDITOR: VMSEDT \<Enter\>

> ARE YOU ADDING 'VMSEDT' AS A NEW ALTERNATE EDITOR (THE 3RD)? Y\<Enter\> (YES)

> ACTIVATION CODE FROM DIWE: G ^XTEDTVXD

> ACTIVATION CODE FROM DIWE: G TPU^XTEDTVXD

> OK TO RUN TEST: I ^%ZOSF("OS")\["VAX"

> RETURN TO CALLING EDITOR: \<Enter\>

> DESCRIPTION:

> 1\> Call to VMS EDT editor to process VA FileMan word-proc. fields.\<Enter\>

> 2\> Creates temporary VMS file in the default directory with a name \<Enter\>

> 3\> of 'DIWE\$'\_\$JOB\_'.TMP'. This version will remove the two copies\<Enter\>

> 4\> of the file that EDT leaves behind.\<Enter\>

> 5\> \<Enter\>

> EDIT Option: \<Enter\>

> Select ALTERNATE EDITOR: \<Enter\>

> <span id="_Ref92695112" class="anchor"></span>Figure 3‑38: Installing the OpenVMS EDT or TPU Text Editor—Sample user dialogue

#### Customize "Edit User Characteristics" (Optional)

> The Edit User Characteristics option, exported by Kernel on the Common Menu, allows users to edit their user attributes. When a user chooses the Edit User Characteristics option, Kernel attempts to load the ScreenMan form named XUEDIT CHARACTERISTICS, if it exists. If the form cannot be loaded on the current terminal type, Kernel invokes the scrolling-mode input template of the same name instead.

> The set of fields a user can edit through this option can be locally defined, by creating an alternative ScreenMan form and input template locally, however. The Edit User Characteristics option checks the KERNEL PARAMETER file (#8989.2) to see if the site has specified an alternate name for the ScreenMan form and input template. If the site has specified an alternate name, then the option uses the site-specified form and template.

> To replace the default Edit User Characteristics form and template, follow these steps:

> a\. Clone the Kernel default ScreenMan form.

> b\. Modify the cloned ScreenMan form.

> c\. Create and modify an input template with the same name as the cloned ScreenMan form.

> d\. Update the KERNEL PARAMETERS file (#8989.2) so that Edit User Characteristics uses the local ScreenMan form and template, rather than Kernel's default form and template.

> Once you have completed these four steps, the Edit User Characteristics option in Kernel V. 8.0 uses your locally created ScreenMan form and input template, rather than the default Kernel ScreenMan form and template.

> Each of these steps is described below in detail:

> a. Clone the Kernel Default ScreenMan Form

> Use VA FileMan's CLONE^DDS entry point (documented in the *VA FileMan Programmer's Manual*) to clone the NEW PERSON file's XUEDIT CHARACTERISTICS form. The current namespace for that form (and associated blocks) is XU; the local version be saved with a namespace of ZZXU.

> b. Modify the Cloned ScreenMan Form

> Use VA FileMan's new visual Form Editor to locally modify the cloned ScreenMan form (documented in the *VA FileMan User Manual*) so that it edits the fields you want it to edit.

> c. Create and Modify an Input Template

> Before the ScreenMan form can be used in the Edit User Characteristics option, you *must* create an input template in the NEW PERSON file (#200) with the same name as the form created in step a. There are two ways to do this:

> 1\. Edit the XUEDIT CHARACTERISTICS template and save it under the same name you used for the cloned ScreenMan form.

> OR

> 2\. Create an input template from scratch and save it under the same name you used for the cloned ScreenMan form.

> d. Update the KERNEL PARAMETERS File

> Finally, instruct Kernel to use your new form when the user requests the Edit User Characteristics option. Do this by entering a replacement name for the XUEDIT CHARACTERISTICS entry in the KERNEL PARAMETERS file (#8989.2). Use VA FileMan to do this:

> Select VA FileMan Option: Enter or Edit File Entries

> INPUT TO WHAT FILE: OPTION// KERNEL PARAMETERS \<Enter\> (5 entries)

> EDIT WHICH FIELD: ALL// \<Enter\>

> Select KERNEL PARAMETERS NAME: XUEDIT CHARACTERISTICS

> NAME: XUEDIT CHARACTERISTICS Replace \<Enter\>

> TYPE: I// \<Enter\>

> DEFAULT: \<Enter\>

> REPLACEMENT: ZZXUEDIT CHARACTERISTICS

> Select KERNEL PARAMETERS NAME:

<span id="_Toc158713863" class="anchor"></span>Figure 3‑39: Updating the KERNEL PARAMETERS file (#8989.2)—Sample user dialogue

# Virgin Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For a virgin install, you *must* have already established library and production UCIs. Also, VA FileMan V. 21 *must* already be installed.

Differences between the data installed on your system during the Virgin Install (versus installing Kernel V. 8.0 in a V. 7.1 environment) are as follows:

- More VA FileMan files are installed by the Virgin Install.
- More TERMINAL TYPE entries (for printers) are brought in by the Virgin Install.

### Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Confirm Distribution Files for Kernel V. 8.0

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>BEGIN THE INSTALLATION IN THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Log On, Using Console Device

> Choose what system you are going to perform the main installation on, and log on to that system, using the console device. This installation is performed on *one system only*, regardless of whether you are an MSM-DOS or DSM for OpenVMS site.

> Use the *console device*, since Kernel will initially be configured to recognize only the console device.

> DSM FOR OpenVMS:

> Use a privileged OpenVMS account. Also, create a large symbol table at sign-on, (\$ DSM/SYM=100000) so there is enough space to work.

> MSM-DOS:

> When logging on, increase the symbol table size to 100 (UCI,VOL:ROU:100) so that there is enough space to work.

#### Inhibit Logons/Kill Off Users

> Inhibit logons, if there is the possibility of anyone accessing the system while the Kernel installation is running. Kill off any M users on the system.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE MANAGER (LIBRARY) ACCOUNT</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

#### Set Up Global Protection, Translation and Journaling for Manager's Account Globals

> You *do not* need to set up globals in the production account at this time.

> Manager's account only: Initialize Kernel globals.

> Set up Kernel's Manager account globals, which are listed in the Review Global Protection, Translation, and Journaling section.

> As you create and place the globals in the Manager's account, set their characteristics (protection, translation, and journaling) as recommended in the Review Global Protection, Translation, and Journaling section. But only set up globals in the Manager's account.

> DSM for OpenVMS:

> Use the ^%GLOMAN utility.

> MSM-DOS:

> Use the ^%GCH utility.

#### Check Global Protection for ^%ZOSF

#### Lift Global Protection for ^%ZUA

#### Load Manager Routines

#### Run the Manager Setup Routine

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Install Standalone KIDS Module

> DSM for OpenVMS:

> Install the standalone KIDS module *once*, for the cluster.

> MSM-DOS:

> Install the standalone KIDS module on *each compute server* and *each print server*.

> a\. <u>In VAH</u>: Restore routines from the standalone KIDS distribution file (KIDS8.RTN) to the production account:

> \>D ^%RR \<Enter\>

> Input Device ? \> KIDS8.RTN \<Enter\>

> Restoring routines from KIDS8.RTN

> XLFDT XLFDT1 XPDCOM XPDCOMG XPDCPU XPDDCS XPDDI XPDDP XPDE XPDET XPDGCDEL XPDH

> XPDI XPDIA XPDIA1 XPDID XPDIGP XPDIJ

> XPDIK XPDIL XPDIL1 XPDIN001 XPDIN002 XPDIN003 XPDIN004 XPDIN005 XPDIN006 XPDIN007 XPDIN008 XPDIN009 XPDIN00A XPDIN00B XPDIN00C XPDIN00D XPDIN00E XPDIN00F XPDIN00G XPDIN00H XPDIN00I XPDIN00J XPDIN00K XPDIN00L XPDIN00M XPDIN00N XPDIN00O XPDIN00P XPDIN00Q XPDIN00R XPDIN00S XPDIN00T XPDINIT XPDINIT1 XPDINIT2 XPDINIT3 XPDINIT4 XPDINIT5 XPDIP XPDIPM XPDIQ XPDIR XPDIST XPDIU XPDKEY XPDKRN XPDMENU XPDNTEG XPDPINIT XPDR XPDRSUM XPDT XPDTA XPDTA1 XPDTC XPDTP XPDUTL XPDV XQDATE XQH

> XQOO XQOO1 XQOO2 XQOO3

> \>

<span id="_Toc158713864" class="anchor"></span>Figure 4‑1: Restoring routines in VAH

> b\. <u>In VAH</u>: Run the integrity check routine (^XPDNTEG) to verify the integrity of the KIDS routines:

> \>D ^XPDNTEG

<span id="_Toc158713865" class="anchor"></span>Figure 4‑2: Run the integrity check routine (^XPDNTEG) in VAH

> Report any "off-by" discrepancies to your local OIFO before proceeding with the installation. Discrepancies may simply indicate that the file includes patched routines.

> c\. If you are an MSM-DOS site with multiple CPUs, repeat steps a-b above on *every compute server* and *every print server* so that the standalone KIDS module is installed on all compute and print servers.

> d\. <u>In VAH</u>: Run the KIDS setup routine, ^XPDINIT. You only need to do this on one CPU (not on all CPUs). This routine creates the VA FileMan files used by KIDS.

> Answer YES to write over file security codes; ^XPDINIT brings in new files, so you should answer yes to apply file security.

> \>D ^XPDINIT

> This version (#8.0) of 'XPDINIT' was created on 22-APR-1995

> (at KERNEL, by VA FileMan V.21.0)

> I AM GOING TO SET UP THE FOLLOWING FILES:

> 9.6 BUILD

> 9.7 INSTALL

> NOTE: This package also contains SORT TEMPLATES

> NOTE: This package also contains INPUT TEMPLATES

> NOTE: This package also contains PRINT TEMPLATES

> NOTE: This package also contains FORMS

> ARE YOU SURE EVERYTHING'S OK? No// Y \<Enter\> (Yes)

> ...SORRY, JUST A MOMENT PLEASE..................

> Compiling form: XPD EDIT BUILD

> OK, I'M DONE.

> NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

> \>

> <span id="_Toc158713866" class="anchor"></span>Figure 4‑3: Running the KIDS setup routine (^XPDINIT) in VAH

#### Set Up Variables

- <u>In VAH</u>: Set up Variables. Set up your DUZ and set DUZ(0) to "@" using the Q^DI entry point, and use direct set commands to create three additional variables (DUZ=.5, IO=IO(0), and IOST=""):

> \>D Q^DI *(To set DUZ(0)="@")*

> VA FileMan 21.0

> Select OPTION: \<Enter\>

> \>S DUZ=.5,IO=IO(0),IOST=""

> \>

> <span id="_Toc158713867" class="anchor"></span>Figure 4‑4: Set up DUZ and DUZ(0) variables in VAH using Q^DI

#### Load Kernel V. 8.0 Distribution for Production Account

- <u>In VAH</u>: Invoke ^XPDKRN to bring up the Kernel Installation menu. Choose the LOAD A DISTRIBUTION option.

> Device Name Prompt

> For Device Name, enter the device name appropriate for your operating system to open the distribution host file. Enter two question marks ("??") to list suggesting values (based on operating system).

> DSM for OpenVMS:

> Enter the full distribution file name at this prompt, including path.

> MSM-DOS:

> Enter the device number for host files.

> Device Parameters Prompt

> For Device Parameters, enter the device parameters appropriate for your operating system. Enter two question marks to list suggested values (based on operating system).

> DSM for OpenVMS:

> Enter READONLY at this prompt.

> MSM-DOS:

> Enter, in parentheses, the full distribution file name, including path, a colon, and "R" in quotation marks. For example, if the distribution file is in drive a:, you would enter ("A:\KRN8.KID":"R") including the parentheses.

> Want to Continue with Load? Prompt

> The distribution should contain Kernel V. 8.0 and Kernel - Virgin Install V. 8.0. Answer YES to the "Want to Continue with Load?" prompt.

> KIDS runs the environment check. If it runs successfully, KIDS loads the distribution into ^XTMP, and returns you to the M programmer's prompt. If the environment check fails, however, you *must* determine and correct the condition that caused the failure. Once you have corrected the condition, you need to repeat the instructions in this section to load the Kernel distribution.

> \>D ^XPDKRN

> KIDS 8.0

> Select KIDS OPTION: LOAD A DISTRIBUTION

> Device Name: ?

> Device Name is either the name of the HFS file or the name of the HFS Device.

> i.e. for MSM enter 51

> for DSM enter DISK\$USER::\[ANONYMOUS\]:KRN8.KID

> Device Name: KRN8.KID

> Device Parameters: ?

> Device Parameter is the Open parameter this M operating system needs to

> open the Device Name.

> i.e. for MSM enter ("B:\KRN8.KID":"R")

> for DSM enter READONLY

> Device Parameters: READONLY

> KIDS Distribution save on Apr 22, 1995@10:15:10

> Comment: Kernel 8.0 from ISC-SF by RSD

> This Distribution contains Transport Globals for the following Package(s):

> KERNEL 8.0

> KERNEL - VIRGIN INSTALL 8.0

> Want to Continue with Load? YES// \<Enter\>

> Loading Distribution...

> Will first run the Environment Check Routine, XVIRENV

> Will first run the Environment Check Routine, XUINOK

> I'm checking to see if it is OK to install KERNEL v8.0 in this account.

> Checking the %ZOSV routine

> Everything looks OK, Lets continue.

> Use KERNEL - VIRGIN INSTALL 8.0 to install this Distribution.

> \>

> <span id="_Toc158713868" class="anchor"></span>Figure 4‑5: Loading the Kernel V. 8.0 distribution

> Recovering from an Aborted Distribution Load

> If you encounter an error while loading a distribution you will be unable to re-load the distribution until you clear out what was stored during the aborted load attempt.

> To clear out the previously loaded distribution, use the Unload a Distribution option. Choose the distribution to unload. The entries in the INSTALL file (#9.7) for all transport globals in the distribution will be removed, and the transport globals themselves will be purged from the ^XTMP global.

> Once you have unloaded the distribution, you should be able to reload it.

#### Verify Checksums of Loaded Distribution

- <u>In VAH</u>: Invoke ^XPDKRN. Use the VERIFY CHECKSUMS OF TRANSPORT GLOBAL option to verify the integrity of the two Kernel distributions (KERNEL 8.0 and KERNEL - VIRGIN INSTALL 8.0):

> \>D ^XPDKRN

> KIDS 8.0

> Select KIDS OPTION: VERIFY \<Enter\> CHECKSUMS OF TRANSPORT GLOBAL

> Select INSTALL NAME: Kernel 8.0

> PACKAGE: KERNEL 8.0 Apr 22, 1995 7:17 am Page 1

> -------------------------------------------------------------------

> 319 Routine checked, 0 failed.

> \>D ^XPDKRN

> KIDS 8.0

> Select KIDS OPTION: VERIFY \<Enter\> CHECKSUMS OF TRANSPORT GLOBAL

> Select INSTALL NAME: KERNEL - VIRGIN INSTALL 8.0

> PACKAGE: KERNEL - VIRGIN INSTALL 8.0 Apr 22, 1995 7:17 am Page 1

> -------------------------------------------------------------------

> 2 Routine checked, 0 failed.

> \>

<span id="_Toc158713869" class="anchor"></span>Figure 4‑6: Verify checksums (Virgin installs)—Sample user dialogue

> Report any "off-by" discrepancies to your local OIFO before installing Kernel. Discrepancies may simply indicate that the distribution includes patched routines.

#### Install the Kernel Software

- <u>In VAH</u>: Install Kernel.

> Make sure that your variables are still set up. Set up your DUZ and set DUZ(0) to "@" using the Q^DI entry point, and use direct set commands to create three additional variables, as in a previous step (DUZ, IO, and IOST).

> Invoke the ^XPDKRN routine again. Choose the INSTALL PACKAGE(S) option. Select KERNEL - VIRGIN INSTALL 8.0 as the software you want to install.

> KIDS runs Kernel's environment check routine a second time (the first time was when the distribution was loaded). If the environment check runs successfully, you may proceed with the main Kernel installation.

> If the environment check fails, you need to correct the condition that caused it to fail. You may also need to reload the Kernel distribution if it was purged when the environment check failed.

> Annotated Installation Dialogue

> An annotated text of the installation dialogue is listed on the following pages. It may not be an exact match of what you will see when running your installation. It is provided as a best approximation of a typical installation. Explanatory notes are provided along with the dialogue that may give some indication as to why your experience may differ from the example presented here.

> \>D ^XPDKRN

> KIDS 8.0

> Select KIDS OPTION: INSTALL PACKAGE \<Enter\> (S)

> Select INSTALL NAME: KERNEL - VIRGIN INSTALL 8.0 \<Enter\> Loaded from Distribution

> This Distribution was loaded on Apr 22, 1995@15:28:01 with header of Kernel 8.0 from ISC-SF by RSD ;Created on Apr 11,1995@10:00:07

> The tape consisted of the following Install(s):

> KERNEL - VIRGIN INSTALL 8.0

> KERNEL 8.0

> Will first run the Environment Check Routine, XVIRENV

> Install Questions for KERNEL - VIRGIN INSTALL 8.0

> 3.2 TERMINAL TYPE (including data)

> 3.8 MAIL GROUP

> 4.2 DOMAIN

> 5 STATE (including data)

> 7 PROVIDER CLASS

> 7.1 SPECIALITY

> 10 RACE (including data)

> 11 MARITAL STATUS (including data)

> 13 RELIGION (including data)

> Will first run the Environment Check Routine, XUINOK

> I'm checking to see if it is OK to install KERNEL v8.0 in this account.

> Checking the %ZOSV routine

> Now to check protection on GLOBALS.

> If you get an ERROR, you need to add Write access to that global.

> Checking ^%ZIS

> Checking ^%ZISL

> Checking ^%ZTER

> Checking ^%ZUA

> Everything looks OK, Lets continue.

> Install Questions for KERNEL 8.0

> 3 USER

> 3.05 FAILED ACCESS ATTEMPTS LOG

> 3.07 PROGRAMMER MODE LOG

> 3.075 ERROR LOG

> 3.076 ERROR MESSAGES (including data)

> 3.081 SIGN-ON LOG

> 3.1 TITLE

> 3.2 TERMINAL TYPE (including data)

> 3.22 DA RETURN CODES (including data)

> 3.23 LINE/PORT ADDRESS

> 3.5 DEVICE

> 3.51 SPOOL DOCUMENT

> 3.519 SPOOL DATA

> 3.54 RESOURCE

> 3.6 BULLETIN

> 4 INSTITUTION

> 4.1 FACILITY TYPE (including data)

> 4.11 AGENCY (including data)

> 4.3 KERNEL SITE PARAMETERS

> 6 PROVIDER

> 9.2 HELP FRAME

> 9.4 PACKAGE

> Note: You already have the 'PACKAGE' File.

> 9.6 BUILD

> Note: You already have the 'BUILD' File.

> 9.7 INSTALL

> Note: You already have the 'INSTALL' File.

> 9.8 ROUTINE

> 14.4 TASKS

> 14.5 VOLUME SET

> 14.6 UCI ASSOCIATION

> 14.7 TASKMAN SITE PARAMETERS

> 14.8 TASK SYNC FLAG

> 16 PERSON

> 19 OPTION

> 19.081 AUDIT LOG FOR OPTIONS

> 19.1 SECURITY KEY

> 19.2 OPTION SCHEDULING

> 40.5 HOLIDAY

> 49 SERVICE/SECTION

> 200 NEW PERSON

> 8989.2 KERNEL PARAMETERS

> 8989.3 KERNEL SYSTEM PARAMETERS

> 8991.5 XQAB ERRORS LOGGED

> 8992 ALERT

> 8992.1 ALERT TRACKING

> Install Started for KERNEL - VIRGIN INSTALL 8.0 :

> Apr 22, 1995@15:40:01

> Installing Routines...

> Apr 22, 1995@15:40:02

> Installing Data Dictionaries: ...........

> Apr 12, 1995@15:40:20

> Installing Data:

> Apr 12, 1995@15:40:39

> Installing PACKAGE COMPONENTS:

> Apr 12, 1995@15:40:40

> Updating Routine file... ...

> Updating KIDS files... ..

> KERNEL - VIRGIN INSTALL 8.0 Installed.

> Apr 12, 1995@15:40:41

> Install Started for KERNEL 8.0:

> Apr 12, 1995@15:40:42

> Installing Routines:.................................

> ..............................................

> Apr 22, 1995@15:41:08

> Running Pre-Install Routine: ^XUINPRE

> Clean up dangling 99 nodes in the OPTION File.

> Installing Data Dictionaries: ......................................................

> ..

> Apr 22, 1995@15:42:15

> Installing Data:

> Apr 22, 1995@15:42:27

> Installing PACKAGE COMPONENTS:

> Installing HELP FRAME................................ ..............................................

> Installing BULLETIN..........

> Installing SECURITY KEY..............

> Installing FUNCTION...............

> Installing PRINT TEMPLATE............................ ...............

> Installing SORT TEMPLATE..........................

> Installing INPUT TEMPLATE......................

> Installing FORM..............

> Installing OPTION.................................... ..................................

> Apr 22, 1995@15:45:14

> Running Post-Install Routine: ^XUINEND

> Move KERNEL site parameters.

> Moving ALERTS from file 200 to file 8992 ...

> Delete CPU field from alpha/beta test sites

> Option Scheduling conversion.

> Beginning TaskMan's post-init conversion...

> End of TaskMan's post-init conversion.

> Check and clean out XUFILE if not running FOF.

> Load PARAM file

> TO PROTECT THE SECURITY OF DHCP SYSTEMS, DISTRIBUTION OF THIS SOFTWARE FOR USE ON ANY OTHER COMPUTER SYSTEM IS PROHIBITED. ALL REQUESTS FOR COPIES OF THE KERNEL FOR NON-DHCP USE SHOULD BE REFERRED TO YOUR LOCAL ISC.

> Updating Routine file... ...

> Updating KIDS files... ....

> KERNEL 8.0 Installed.

> Apr 22, 1995@15:45:57

> No link to PACKAGE file

> NO Install Message sent

<span id="_Toc158713870" class="anchor"></span>Figure 4‑7: Example of virgin installation done at the San Francisco OIFO—Sample user dialogue

#### While Main Installation is Running (Multi-CPU Systems)

> No further action is necessary while the main installation is running.

#### If the Main Installation Errors Out

> If the Main Installation errors out, first determine the cause of the problem. Once you have found the problem and corrected it, invoke ^XPDKRN and use the RESTART INSTALL OF PACKAGE(S) option to restart the Kernel installation.

> KIDS provides the ability to restart installations that errored out at the point they errored out. This saves you, the installer, from having to re-run the entire installation over again. When you restart an aborted installation using RESTART INSTALL OF PACKAGE(S), the installation resumes from the last completed checkpoint.

#### When Main Installation is Done

> When the main installation is done, more steps need to be performed to finish setting up Kernel V. 8.0.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>CONTINUE WORKING IN THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Reset ZU

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE MANAGER (LIBRARY) ACCOUNT</strong></p>
<p><strong>(e.g., MGR)</strong></p></td>
</tr>
</tbody>
</table>

#### Reset Global Protection For ^%ZUA

#### Implement Routine Mapping (DSM for OpenVMS only)

#### Global Protection, Translation and Journaling

> Review global protection, translation, and journaling.

#### Run ^ZISETUP to Create Devices

> <u>In MGR:</u> If you have physical ports on your new CPU, run the device setup utility to create devices (D ^ZISETUP). This utility sets up a small set of entries in the DEVICE file (#3.5) for certain devices on your system. You will need to edit the device entries that are added, because they won't have their SUBTYPE fields filled in.

> DSM for OpenVMS:

> ^ZISETUP may set up entries for operator's consoles, TTxx devices, TXxx devices, LPxx devices, and MUxx devices (depending on information available from the system).

> MSM-DOS:

> ^ZISETUP sets up entries for HFS devices, SDP devices, magtape devices, and terminals (depending on information available on the system).

> \>D ^ZISETUP

> THIS ROUTINE INITIALIZES THE DEVICE FILE WITH CURRENT PORT NUMBERS

> OK? Y \<Enter\>

> There must be a prefix for a new device because the Device Name and the \$I cannot be the same. This is being for the Single Device File.

> Please Enter a Prefix for New Devices: VAH// \<Enter\>

> OPA0:

> OPA1:

> ALL SETUP

<span id="_Toc158713871" class="anchor"></span>Figure 4‑8: Creating devices in VAH by running ^ZISETUP—Sample user dialogue

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>NOW MOVE BACK TO THE PRODUCTION ACCOUNT</strong></p>
<p><strong>(e.g., VAH)</strong></p></td>
</tr>
</tbody>
</table>

#### Finish DEVICE File Entry for Console Device

> <u>In VAH:</u> On MSM-DOS systems, you can identify DEVICE file (#3.5) entry for the console device by its \$I value (which is 1). On DSM for OpenVMS systems, the console device has a \$I value of "OPA0:".

> Use FileMan (D Q^DI) to edit the DEVICE file (#3.5) entry for your console device. Fill in the SUBTYPE field in the DEVICE file (#3.5) for the console device. In most cases, setting the SUBTYPE to a value of C-VT100 is adequate.

#### Load MailMan Routines

> In order to create run ^XVIRPOST (next step), you need to load the routines for the MailMan V. 7.1 (or higher) software. Do not run the installation for MailMan; however; just load the routines. You will install MailMan in a later step.

#### Run ^XVIRPOST Post-Install Routine

> <u>In VAH:</u> The post-install routine for the virgin install, ^XVIRPOST, creates important first entries in several Kernel files. Run ^XVIRPOST, and follow the onscreen instructions for answering questions:

> \>D ^XVIRPOST

> Post init for virgin install

> Now to add yourself to the NEW PERSON file.

> Select NEW PERSON NAME: KRNUSER,ONE

> Are you adding 'KRNUSER,ONE' as a new NEW PERSON (the 3RD)? Y \<Enter\> (Yes)

> Checking SOUNDEX for matches.

> No matches found.

> NEW PERSON INITIAL: OK

> NEW PERSON MAIL CODE: \<Enter\>

> We have added FORUM to the domain file.

> Now you need to enter the NETWORK MailMan domain name that will be use on the network and for the name of the Kernel site parameter entry.

> Use the format 'xxx.VA.GOV'

> Select DOMAIN NAME: YOURSITE.VA.GOV

> Are you adding 'YOURSITE.VA.GOV' as a new DOMAIN (the 2ND)?

> Y \<Enter\> (Yes)

> Now lets add your Institution.

> Select INSTITUTION NAME: YOURINST

> Are you adding 'YOURINST' as a new INSTITUTION (the 1ST)?

> Y \<Enter\> (Yes)

> INSTITUTION STATE: CAL

> INSTITUTION FACILITY TYPE: OIFO \<Enter\> OFFICE OF INFORMATION

> FIELD OFFICE

> INSTITUTION STATION NUMBER: 999

> Now to add 'IRM' to the service/section file.

> \>

<span id="_Toc158713872" class="anchor"></span>Figure 4‑9: Running ^XVIRPOST post-install routine in VAH—Sample user dialogue

#### Install MailMan

> In order to edit the first Kernel user (next step), you need to install MailMan V. 7.1. Install MailMan from the console device. Follow the instructions in the *MailMan Installation Guide* to install MailMan. *Be sure to christen your domain* after the installation; to do this, D ^XUP and choose to run MailMan's Christen a Domain option.

#### Finish Setting Up First User Account

> <u>In VAH:</u> Use VA FileMan (D Q^DI) to edit the entry in the NEW PERSON file (#200) you created when running ^XVIRPOST. This first account should be for you, the system manager. Note that there will actually be three entries in the NEW PERSON file (#200), the Postmaster and Shared,Mail being the first two.

> You will be able to enter values for all needed fields except the PRIMARY MENU field. Fill in the following fields (three dots indicate skipped fields):

> Want to edit ACCESS CODE (Y/N): Y \<Enter\> *)*

> FILE MANAGER ACCESS CODE: \#

> ...

> SSN: 000999999

> ...

> Select KEY:

> ...

> SERVICE/SECTION:

<span id="_Toc158713873" class="anchor"></span>Figure 4‑10: Setting up first user account—Sample user dialogue

> Now, to finish off this account:

> a\. Exit FileMan and return to the M prompt.

> b\. Kill all local variables.

> c\. Use the ^XUP entry point to sign on as the new user (enter the access code of the new user). For terminal type name, in most cases entering C-VT100 and pressing \<Enter\> should be sufficient.

> d\. When asked for a menu option, enter EVE as the menu option.

> e\. From the main menu, choose User Management. Then choose Edit an Existing User. For a user to edit, enter your new account. Fill in the PRIMARY MENU OPTION field with the option EVE. Exit and save the changes you made to the new account.

> f\. Return to the main menu (System Manager) by pressing \<Enter\>. Choose the Operations Management menu. Then choose the Kernel Management menu. Then choose the Enter/Edit Kernel Site Parameters option.

> Edit the only entry in the file. On the first ScreenMan screen of the entry, fill in a value for DEFAULT INSTITUTION. On the second ScreenMan screen of this option, make an entry for your main volume set, and fill in the Max Sign-ons and Log RT? values for the volume set entry. Set Max Sign-ons to a reasonable value for your system, and set Log RT? to NO. For example:

> Vol Set Max Sign-ons Log RT?

> ROU 150 NO

<span id="_Toc158713874" class="anchor"></span>Figure 4‑11: Sample Max Sign-ons for main volume set

> g\. Halt off, and then from the M prompt, log on as the new user using the ^ZU entry point (D ^ZU). For Verify Code, just press Enter. You will then be asked for a verify code (enter a new one).

> At this point, the first account (for you, the system manager) should be set up. You will be presented with the System Manager's menu and will be able to add other users and assign keys by using the Kernel options.

> Give yourself (the new user) the VA FileMan access code "@". Consult your OIFO or other VA contact person for instructions if you do not know the procedure for doing this.

#### Set Up Device Entries for Virtual Terminals

> <u>In VAH:</u> If you have additional terminal devices beyond the console device that need to access Kernel, you may want to set up virtual terminal device entries for virtual terminals.

|                                                                                                                |                                                                                                                                                                      |
|----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](kernel-8-0-installation-guide/031.png) | REF: For more information on virtual terminal devices, please refer to the "Device Handler: System Management" chapter of the *Kernel Systems Management Guide*. |

#### Install Kernel Toolkit V. 7.3

> Due to interdependencies between Kernel and Kernel Toolkit, the final installation step is to install Kernel Toolkit V. 7.3. Please note the important instructions regarding Kernel V. 8.0 sites in Kernel Toolkit V. 7.3's Preliminary Considerations section (*Kernel Toolkit Installation Guide*). Also, never install Kernel Toolkit V. 7.2 on top of Kernel V. 8.0 (doing so would break Kernel V. 8.0).

You are now done installing Kernel V. 8.0. The task of configuring Kernel is described in the Post-Installation Tasks (Virgin Install) section that follows. Depending on the complexity of your site, it may take some time to configure Kernel. You should allow adequate time to perform the configuration.

### Post-Installation Tasks (Virgin Install)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. <u>In VAH:</u> Set up/Review Kernel Site Parameters.

> For advice on setting up Kernel and VistA system in general, please refer to the appropriate cookbook for your operating system/hardware type.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/032.png)</td>
<td><p><strong>REF:</strong></p>
<p><strong>DSM for OpenVMS:</strong></p>
<p>Refer to the most recent <em>VAX DSM Systems Guide</em> (otherwise known as the VAX Cookbook).<br />
<br />
<strong>MSM-DOS:</strong></p>
<p>Refer to the most recent <em>486 Cookbook and MSM System Managers Guide</em>.</p></td>
</tr>
</tbody>
</table>

> Edit the KERNEL SYSTEM PARAMETERS (#8989.3) and TASKMAN SITE PARAMETERS (#14.7) files. Include your UCIs in TaskMan's UCI ASSOCIATION file (#14.6). Configure Task Manager.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](kernel-8-0-installation-guide/033.png)</td>
<td><strong>REF:</strong> For more information on the UCI ASSOCIATION file (#14.6) and configuring Task Manager, please refer to the "Task Manager System Management: Configuration" chapter of the <em>Kernel Systems Management Guide</em>.<br />
<br />
For information on setting up site parameters, please refer to the Implementation and Maintenance section of the <em>Kernel Technical Manual</em> and the system management chapters in the <em>Kernel Systems Management Guide</em>.</td>
</tr>
</tbody>
</table>

> 2\. Update Routines on other CPUs.

> If you are setting up a multi-CPU system where each CPU has its own Manager and Production UCIs, you will need to set up the manager's account and Kernel's routines for each CPU (but you do not need to do a full installation for each CPU).

> DSM for OpenVMS systems usually cluster mount the disk(s) holding the Manager and Production UCIs, in which case no further action is necessary.

> MSM-DOS systems, on the other hand, are typically set up with each CPU having its own Manager and Production UCIs. For MSM-DOS multi-CPU systems, follow these guidelines to configure additional CPUs:

> a\. Set up Manager and Production UCIs on each additional CPU.

> b\. Translate globals to the new UCIs (manager and production), create non-translated globals, and review global translation, protection, and journaling.

> c\. Load the manager's account routines, and run the manager's account setup routine ^ZTMGRSET, in the Manager UCI of each CPU you are setting up.

> d\. Load the KIDS standalone routines in the production UCI for each CPU you are setting up, but do not run ^XPDINIT since this has already been done once.

> e\. On the CPU you did the main installation on, run MOVE^XPDCPU to make the Kernel V. 8.0 routines available to the new CPUs via the translated ^XTMP global.

> f\. In the production UCI on each of the new CPUs, run INSTALL^XPDCPU to load the Kernel V. 8.0 routines from the ^XTMP global.

> Following these steps should install Kernel on each additional CPU.

> 3\. Start Up Task Manager.

> <u>In MGR:</u> D ^ZTMB. This enables background tasks to run in Kernel.

4\. Review Option Scheduling.

> 5\. Obtain and Load Data for the DOMAIN file (#4.2).

> Merge incoming with existing data (do *not* overwrite). Obtain the file from one of your other production accounts or from an OIFO).

6\. Optionally Install the OpenVMS EDT or TPU Text Editor.

7\. Optionally Customize the Edit User Characteristics Template.

8\. Enable Logons.

9\. Install Additional Files and Software.

> To install additional VistA VA FileMan files, load the software application responsible for the maintenance of that file.

## Appendix A: Installing Kernel on Other Platforms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel provides full support for the following centrally procured M implementations used by VA:

- DSM for OpenVMS
- MSM-DOS

Kernel provides secondary support for the following M implementations:

- Intersystems M/SQL
- DataTree DTM-PC

When you run ^ZTMGRSET to set up the manager's account, one of the questions you *must* answer is what M implementation should Kernel install support for. Intersystems M/SQL and DataTree DTM-PC are available choices, along with DSM for OpenVMS and MSM-DOS. Routines and ^%ZOSF global nodes appropriate to the chosen M implementation are loaded by ^ZTMGRSET.

Kernel also supports MSM-Unix. A difference between installing Kernel on MSM-Unix vs. MSM-DOS is that for MSM-Unix, the ^ZTMGRSET routine restores ^%ZISH from ^%ZISHMSU, rather than ^%ZISHMSM.

If you are running on a platform other than the platforms above, your M vendor may be able to provide some additional instructions about installing Kernel and FileMan on your platform. You can also contact your OIFO for any special instructions on how to install with Kernel V. 8.0.

Kernel no longer actively supports M implementations that aren't expected to support the proposed 1995 ANSI M standard. Implementations in this category are DSM-11, M11+, and M/VX.