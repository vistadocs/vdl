---
consolidated_title: "mental health assistant phase 3 installation guide"
app_code: YS
doc_type: IG
master_source: "YS*5.01*85 Mental Health Assistant Phase 3 Installation Guide"
master_pub_date: December 2007
consolidated_from: 8 versions
prior_versions:
  - "YS*5.01*103 Mental Health Assistant Phase 3 Installation Guide"
  - "YS*5.01*104 Mental Health Assistant Phase 3 Installation Guide"
  - "YS*5.01*105 Mental Health Assistant Phase 3 Installation Guide"
  - "YS*5.01*130 Mental Health Assistant Phase 3 Installation Guide"
  - "YS*5.01*134 Mental Health Assistant Phase 3 Installation Guide"
  - "YS*5.01*150 Mental Health Assistant Phase 3 Installation Guide"
  - "YS*5.01*93 Mental Health Assistant Phase 3 Installation Guide"
---

> ![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/001.png)

> MENTAL HEALTH ASSISTANT VERSION 3 (MHA3) INSTALLATION GUIDE

> PATCH YS\*5.01\*85

> Version 5.01

> December 2007

> Department of Veterans Affairs

> VistA Health System Design & Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Preface](#preface)
  - [Section 508 of the Rehabilitation Act](#section-508-of-the-rehabilitation-act)
- [Software and Documentation Retrieval Information](#software-and-documentation-retrieval-information)
  - [MHA3 Documentation Website Locations](#mha3-documentation-website-locations)
    - [VistA Mental Health Version 5.01 Home Page:](#vista-mental-health-version-501-home-page)
    - [VistA Documentation Library (VDL):](#vista-documentation-library-vdl)
    - [Anonymous Software Directory](#anonymous-software-directory)
    - [MHA3 Software and Documentation Files Retrieval Formats](#mha3-software-and-documentation-files-retrieval-formats)
- [Introduction](#introduction)
  - [Overview](#overview)
- [Enhancements](#enhancements)
  - [VistA Mental Health Assistant NEW Features in MHA3:](#vista-mental-health-assistant-new-features-in-mha3)
- [Security Information](#security-information)
  - [Security Management](#security-management)
    - [Security Features:](#security-features)
    - [Remote Systems:](#remote-systems)
    - [Archiving/Purging:](#archivingpurging)
    - [Contingency Planning:](#contingency-planning)
    - [Interfacing:](#interfacing)
    - [Electronic Signatures:](#electronic-signatures)
    - [Menus](#menus)
    - [Security Keys:](#security-keys)
    - [File Security:](#file-security)
    - [References:](#references)
    - [Official Policies:](#official-policies)
- [Pre-Installation Information](#pre-installation-information)
  - [Recommended Users:](#recommended-users)
    - [Information Resources Management (IRM) Staff](#information-resources-management-irm-staff)
    - [Mental Health Clinicians](#mental-health-clinicians)
    - [Test Sites](#test-sites)
  - [Windows Conventions](#windows-conventions)
  - [VistA Operating System](#vista-operating-system)
  - [VistA Operating System Performance Capacity](#vista-operating-system-performance-capacity)
  - [MHA Central Processing Unit (CPU) Requirement](#mha-central-processing-unit-cpu-requirement)
  - [MHA Software Application Installation Time](#mha-software-application-installation-time)
  - [Users on the System](#users-on-the-system)
  - [Backup Routines](#backup-routines)
  - [Kernel Installation and Distribution System (KIDS)](#kernel-installation-and-distribution-system-kids)
  - [Namespace](#namespace)
  - [MHA3 Software Application Requirements](#mha3-software-application-requirements)
  - [Required Patch](#required-patch)
  - [MHA3 Menu/Options Changes](#mha3-menuoptions-changes)
    - [YS Broker1 \[YS BROKER1\] Option](#ys-broker1-ys-broker1-option)
  - [Database Integration Agreements (DBIAs)](#database-integration-agreements-dbias)
  - [New VistA Mental Health Files](#new-vista-mental-health-files)
  - [Routine Summary](#routine-summary)
- [Installation Instructions](#installation-instructions)
  - [Server:](#server)
    - [MHA 3 Installation Example:](#mha-3-installation-example)
  - [MHA3 Installation File Structure and Use](#mha3-installation-file-structure-and-use)
- [Post Installation Instructions](#post-installation-instructions)
  - [Create TIU Document Definitions:](#create-tiu-document-definitions)
  - [Client Software:](#client-software)
  - [MHA3 Files Retrieval Locations and Formats](#mha3-files-retrieval-locations-and-formats)
    - [MHA3 Files Retrieval Locations](#mha3-files-retrieval-locations)
  - [Mental Health Assistant Install Windows Illustrations](#mental-health-assistant-install-windows-illustrations)
    - [Installing Mental Health Assistant on your Computer](#installing-mental-health-assistant-on-your-computer)
    - [Choose Destination Location](#choose-destination-location)
    - [Folder Does Not Exist](#folder-does-not-exist)
    - [Select Start Menu Folder](#select-start-menu-folder)
    - [Ready to Install](#ready-to-install)
    - [Installing Mental Health Assistant 3](#installing-mental-health-assistant-3)
    - [Completing the Mental Health Assistant 3 Setup Wizard](#completing-the-mental-health-assistant-3-setup-wizard)
- [Installing SecureDesktop Functionality in MHA3](#installing-securedesktop-functionality-in-mha3)
- [Setting up VistA MHA3 on CPRS GUI Tools Menu](#setting-up-vista-mha3-on-cprs-gui-tools-menu)
  - [Setting up VistA so that individual MHA3 assessments are also listed on the CPRS GUI Tools Menu](#setting-up-vista-so-that-individual-mha3-assessments-are-also-listed-on-the-cprs-gui-tools-menu)
- [Files with New Entries Added](#files-with-new-entries-added)
  - [PROTOCOL file (#101) New Entries](#protocol-file-101-new-entries)
  - [HL7 APPLICATION PARAMETER file (#771) New Entry](#hl7-application-parameter-file-771-new-entry)
<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 54%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Revisio n</strong></th>
<th><strong>Description</strong></th>
<th><strong>Author(s)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>12/2007</td>
<td><blockquote>
<p>1.0</p>
</blockquote></td>
<td><blockquote>
<p>Initial version</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td>04/2008</td>
<td>2.0</td>
<td>Updated pages 24, 62 &amp; 63 for changes in Patch YS*5.01*93</td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>
> THIS PAGE INTENTIONALLY LEFT BLANK
> [*Preface iv*](#preface)
> [Section 508 of the Rehabilitation Act iv](#preface)
> [MHA3 overview iv](#preface)
> [*Software and Documentation Retrieval Information 1*](#software-and-documentation-retrieval-information)
> [MHA3 Documentation Website Locations 1](#software-and-documentation-retrieval-information)
> [VistA Mental Health Version 5.01 Home Page: 1](#software-and-documentation-retrieval-information) [VistA Documentation Library (VDL): 1](#software-and-documentation-retrieval-information) [Anonymous Software Directory 1](#software-and-documentation-retrieval-information) [MHA3 Software and Documentation Files Retrieval Formats 2](#mha3-software-and-documentation-files-retrieval-formats)
[MHA3 Folders and Files 3](#_bookmark3)
[*Introduction 5*](#introduction)
> [Overview 5](#introduction)
> [*Enhancements 6*](#enhancements)
> [VistA Mental Health Assistant NEW Features in MHA3 6](#enhancements)
> [*Security Information 7*](#security-information)
> [Security Management 7](#security-information)
> [Security Features: 7](#security-information) [SecureDesktop 7](#security-information) [Mail Group: 7](#security-information) [YS MHA-MHNDB 7](#security-information)
> [Alerts: 7](#security-information) [Remote Systems: 8](#remote-systems) [Example: YTQ RPCs 8](#remote-systems) [Archiving/Purging: 10](#archivingpurging)
> [Menus 10](#archivingpurging) [Security Keys: 10](#archivingpurging) [File Security: 11](#file-security) [References: 11](#file-security)
> [Official Policies: 11](#file-security)
> [*Pre-Installation Information 11*](#file-security)
> [Recommended Users 11](#file-security)
> [Information Resources Management (IRM) Staff 11](#file-security) [Mental Health Clinicians 11](#file-security) [Test Sites 11](#file-security)
> [Windows Conventions 13](#windows-conventions)
> [VistA Operating System 13](#windows-conventions)
> [VistA Operating System Performance Capacity 13](#windows-conventions)
> [MHA Central Processing Unit (CPU) Requirement 13](#windows-conventions)
> [MH TESTS AND SURVEYS file (#601.71) 17](#new-vista-mental-health-files) [MH QUESTIONS file (#601.72) 17](#new-vista-mental-health-files) [MH INTRODUCTIONS file (#601.73) 17](#new-vista-mental-health-files) [MH RESPONSE TYPES file (#601.74) 17](#new-vista-mental-health-files) [MH CHOICES file (#601.75) 17](#new-vista-mental-health-files)
> [MH CHOICETYPES file (#601.751) 18](#mh-choicetypes-file-601.751) [MH INSTRUMENT CONTENT file (#601.76) 18](#mh-choicetypes-file-601.751) [MH BATTERIES file (#601.77) 18](#mh-choicetypes-file-601.751) [MH BATTERY CONTENTS file (#601.78) 18](#mh-choicetypes-file-601.751) [MH BATTERY USERS file (#601.781) 18](#mh-choicetypes-file-601.751) [MH SKIPPED QUESTIONS file (#601.79) 18](#mh-choicetypes-file-601.751) [MH SECTIONS file (#601.81) 18](#mh-choicetypes-file-601.751)
> [MH RULES file (#601.82) 19](#mh-rules-file-601.82)
> [MH INSTRUMENTRULES file (#601.83) 19](#mh-rules-file-601.82)
> [MH ADMINISTRATIONS file (#601.84) 19](#mh-rules-file-601.82)
> [MH ANSWERS file (#601.85) 19](#mh-rules-file-601.82) [MH SCALEGROUPS file (#601.86) 19](#mh-rules-file-601.82) [MH SCALES file (#601.87) 20](#mh-scales-file-601.87)
> [MH DISPLAY file (#601.88) 20](#mh-scales-file-601.87) [MH CHOICEIDENTIFIERS file (#601.89) 20](#mh-scales-file-601.87) [MH SCORING KEYS file (#601.91) 20](#mh-scales-file-601.87) [MH RESULTS file (#601.92) 20](#mh-scales-file-601.87) [MH REPORT file (#601.93) 20](#mh-scales-file-601.87)
> [Routine Summary 21](#routine-summary)
> [*Installation Instructions 23*](#installation-instructions)
> [Server 23](#installation-instructions)
> [MHA 3 Installation Example: 25](#mha-3-installation-example)
> [MHA3 Installation File Structure and Use 30](#mha3-installation-file-structure-and-use)
> [*Post Installation Instructions 33*](#_bookmark20)
> [Create TIU Document Definitions 33](#_bookmark20)
> [Client Software 34](#_bookmark21)
> [IRM Staff 34](#_bookmark21)
> [MHA3 Files Retrieval Locations and Formats 34](#_bookmark21)
> [MHA3 Files Retrieval Locations 35](#_bookmark22) [MHA3 Files Retrieval Formats 36](#_MHA3_Files_Retrieval_Formats)
> [Mental Health Assistant Install Windows Illustrations 38](#_bookmark24)
> [Installing Mental Health Assistant on your Computer 38](#_bookmark24)
> [Choose Destination Location 39](#choose-destination-location) [Folder Does Not Exist 40](#folder-does-not-exist) [Select Start Menu Folder 41](#select-start-menu-folder) [Ready to Install 42](#ready-to-install) [Installing Mental Health Assistant 3 43](#installing-mental-health-assistant-3) [Completing the Mental Health Assistant 3 Setup Wizard 44](#completing-the-mental-health-assistant-3-setup-wizard)
> [Uninstalling MHA3 45](#uninstalling-mha3)
> [*Installing SecureDesktop Functionality in MHA3 46*](#installing-securedesktop-functionality-in-mha3)
> [Uninstalling SecureDeskstop 55](#uninstalling-securedeskstop)
> [*Setting up VistA MHA3 on CPRS GUI Tools Menu 57*](#setting-up-vista-mha3-on-cprs-gui-tools-menu)
> [Setting up VistA so that individual MHA3 assessments are also listed on the CPRS GUI Tools](#_bookmark35) [Menu 59](#_bookmark35)
> [*Files with New Entries Added 61*](#_bookmark36)
> [PROTOCOL file (#101) New Entries 61](#_bookmark36)
> [HL7 APPLICATION PARAMETER file (#771) New Entry 62](#hl7-application-parameter-file-771-new-entry)

# Preface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Veterans Health Information Systems and Architecture (VistA) Mental Health Assistant Version 3 (MHA3) Installation Guide Patch YS\*5.01\*85 provides detailed instructions and requirements for installing and implementing the Graphical User Interface (GUI) software application.

## Section 508 of the Rehabilitation Act

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 overview

> Introduction: This section includes an overview of the major functions, purposes, and how the GUI software application accomplishes the objectives.

> Enhancements: This section contains software changes exported by MHA Version 3, Patch YS\*5.01\*85.

> Security Information: This section addresses any unique legal requirements and responsibilities pertaining to the Mental Health Assistant Version 3, software application and necessary security measures to protect the integrity of the software and its data.

> Pre-installation Information: This section provides information needed prior to installing MHA Version 3, patch YS\*5.01\*85.

> Installation Instructions: This section contains instructions and examples of MHA Version 3, patch YS\*5.01\*85 installation process.

> Post Installation Instruction: This provides directions for implementing the VistA Mental Health Package enhancements to interact with the MHA Version 3, software application.

# Software and Documentation Retrieval Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## MHA3 Documentation Website Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA MHA3 Installation Guide (i.e., YS50185_MHA3_IG.pdf and YS50185_MHA3_IG.doc), User Manual (i.e., YS50185_MHA3_UM.pdf and YS50185_MHA3_UM.doc) are available in MS Word Format (doc) and Portable Document Format (pdf) at the following Website locations:

### VistA Mental Health Version 5.01 Home Page:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

### VistA Documentation Library (VDL):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

### Anonymous Software Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OIFOs</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP ADDRESS</strong></p>
</blockquote></th>
<th><strong>DIRECTORY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

### MHA3 Software and Documentation Files Retrieval Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 Patch YS\*5.01\*85 exports the following folders and files:

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 27%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FILE NAMES</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>CONTENTS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RETRIEVAL FORMATS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS_501_85.KID</td>
<td>MHA Server Components</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>YS50185_SETUP_1_0_3_36.exe</td>
<td><blockquote>
<p>Mental Health Assistant</p>
</blockquote></td>
<td><p>BINARY</p>
<p>This file is the complete install for the Mental Health Assistant GUI</p>
<p>Version 1.0.3.36, client.</p></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>YS50185_SD_SETUP_1_0_2_77.exe</p>
</blockquote></td>
<td>SecureDesktop for Mental Health Assistant</td>
<td><p>BINARY</p>
<p>This file is the complete install for the optional SecureDesktop component for Mental Health Assistant GUI Version</p>
<p>1.0.3.36, client.</p></td>
</tr>
<tr class="even">
<td>YS_MHA.exe</td>
<td>MHA3 Executable</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS_MHA_SD_INSTALLGINA.exe</td>
<td><p>Activate SecureDesktop Executable</p>
<p>DLL used by SecureDesktop</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>YS_MHA.DLL</td>
<td><p>DLL interface to Clinical Reminders functions in CPRS. This DLL is deployed to C:\Program Files\vista\Common</p>
<p>Files</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>MHA3_DLL_Scoring.dll</td>
<td>Required by YS_MHA.DLL</td>
<td><p>BINARY</p>
<p>DLL used by MHA3 for scoring complex instruments.</p></td>
</tr>
<tr class="even">
<td>YS_MHA.JCF</td>
<td><p>JAWS screen-reader</p>
<p>configuration file for use with MHA3</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>dwlGina2.dll</td>
<td>Required security DLL</td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YS_MHA_SD_UNINSTALLGINA.exe</td>
<td><p>Deactivate</p>
<p>SecureDesktop Executable</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS_MHA_VASD.exe</td>
<td>SecureDesktop’s main executable</td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>YS_MHA.HLP</td>
<td>Online help file for the ASI</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS_MHA.GID</td>
<td><blockquote>
<p>Help file configuration.</p>
</blockquote></td>
<td><p>BINARY</p>
<p>Index file used by YS_MHA.HLP.</p></td>
</tr>
<tr class="even">
<td>ANSWER file folder</td>
<td>Offline records that have</td>
<td><blockquote>
<p>FOLDER</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 27%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><span id="_bookmark3" class="anchor"></span>not been uploaded</th>
<th><p>C:\Documents and Settings\&lt;USER PROFILE&gt;\Application Data\MHA3\Answer</p>
<p>Files</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>INSTRUMENT file folder</p>
</blockquote></td>
<td>MH Instruments for Offline administration</td>
<td><p>FOLDER</p>
<p>C:\Documents and Settings\&lt;USER PROFILE&gt;\Application Data\MHA3\Instrument Files</p></td>
</tr>
<tr class="even">
<td><blockquote>
<p>YS50185_MHA3_IG.pdf</p>
</blockquote></td>
<td><p>Mental Health Assistant</p>
<p>Version 3 (MHA3)</p>
<p>Installation Guide Patch YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS50185_MHA3_IG.doc</td>
<td><p>Mental Health Assistant</p>
<p>Version 3 (MHA3)</p>
<p>Installation Guide Patch YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>YS50185_MHA3_UM.pdf</td>
<td><p>Mental Health Assistant Version 3 (MHA3) User</p>
<p>Manual Patch YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS50185_MHA3_UM.doc</td>
<td><p>Mental Health Assistant Version 3 (MHA3) User Manual Patch</p>
<p>YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

#### MHA3 Folders and Files

> Example: MHA3 Patch YS\*5.01\*85 folders and files.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/002.png)

> Example: Files installed by the YS50185_SETUP_1_0_3_36.exe installer and Files added to the MHA3 folder after installing the SecureDesktop functionality.

> ![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/003.png)

> 4 VistA MHA 3 Patch YS\*5.01\*85 December 2007

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA Mental Health Assistant (MHA) is the graphical user interface (GUI) for the VistA Mental Health Package (MHP). MHA was developed to create an effective and efficient tool for mental health clinicians and their patients to use for the administration and scoring of assessment instruments and interviews. Additionally, results are displayed in report and graphical formats.

> MHA and MHP support mental health assessments (e.g., psychological testing, structured interviews, and staff rating scales) that are not available elsewhere in the Computerized Patient Record System (CPRS)/Veterans Information System and Technology Architecture (VistA).

> MHA has enjoyed widespread usage among mental health clinicians over the past several years, and the current revisions of MHA and MHP initiate steps toward re-engineering VistA Mental Health functionality.

> The Veterans Health Administration (VHA) Action Agenda for implementing the President's New Freedom Commission on Mental Health recommendations regarding the use of information technology to enhance the care of Mental Health patients states, “VHA should make the integration of MHA and HealtheVet Desktop (HeVD) an explicit goal and should provide the OI with sufficient resources to accomplish this goal in collaboration with the Mental Health Strategic Healthcare Group (MHSHG) Informatics Section. The integration should eliminate the need for Mental Health clinicians to change applications. Further, the integration should make appropriate Mental Health assessment tools available to clinicians outside Mental Health (e.g., depression and alcohol screening instruments should be made available to primary care clinicians).”

> This revision of MHA creates a closer integration with CPRS, by placing the MHA GUI on the CPRS Tools Menu. Additionally, functionality was created to allow a site to place an individual instrument on the Tools menu, allowing widespread access to that specific instrument without having to issue the menu for the MHP to all clinicians.

> Additional functionality that strengthens the tie to the patient’s medical record is the creation of a progress note in CPRS when an instrument is completed through MHA.

> Furthermore, MHA maintains and strengthens its ties to the Clinical Reminders program, which allows for the presentation of specific instruments through reminder dialogs to all clinicians who resolve reminders.

> Additionally, the Psychological Instrument files of the MHP have been restructured to initiate the migration toward re-engineering and placing MHA as a component of Health*e*Vet Desktop when it is implemented.

> To better meet the needs of clinicians and patients in different programs, particularly non- traditional settings, MHA can now run in a standalone mode to administer instruments offline for later uploading to VistA.

# Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3, Patch YS\*5.01\*85 is exporting the following software enhancements:

## VistA Mental Health Assistant NEW Features in MHA3:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Completely re-organized the VistA Mental Health database files to simplify migration to Health Data Repository (HDR).
- MHA3 <u>must</u> be invoked from the CPRS Tools menu, for interaction with VistA and patient selection.
- Patient-selection is done entirely by interaction with CPRS.
- MHA3 can run in standalone mode, but only for administering offline tests—which later must be uploaded to VistA
- MHA3 allows the CPRS Tools menu to invoke any number of single types of instruments, without the need to go directly to the MHA3 Main form. For instance, a CAGE menu item can be added to the Tools menu, which would invoke only a CAGE data entry form.
- Major functionality (GAF, ASI, Results, etc.) is now presented on individual forms, as opposed to as tabs on one main form.
- MHA3 provides a new Battery Wizard form to simplify creating batteries of instruments.
- There is a new & improved SecureDesktop component that now uses stronger code to prevent hacking.
- “Clerk entry” data-entry-mode form for psych tests has been removed.
- All completed administrations now automatically generate a progress note for review in CPRS.
- All test scores are now saved in VistA, instead of calculated on-the-fly.
- There is a hospital Location associated with an administered instrument, for progress notes purposes.
- The accompanying MHA3 help file is supplied only for describing the functions of the ASI Manager forms. All other tests and interview have built-in help that is retrieved directly from the MHP when using the “Description” pop-up menu function in the Instrument Manager.
- MHA3 recreates a debug log file named “mha3_debug.log” for each MHA3 session. This file can be emailed to developers to assist in remote debugging. No patient-identifying data is collected in this file.
- This patch includes 6 new instruments in MH TESTS AND SURVEYS file (#601.71). The instruments are the Braden Scale for Predicting Pressure Ulcer Risk (Braden Scale), Morse Fall Scale (Morse Fall Scale), the PTSD Screen (PTSD 4Q), BOMC: The Six-Item Blessed Orientation-Memory-Concentration Test, TBI 2ND LEVEL EVAL: Traumatic Brain Injury: 2nd Level Evaluation and the PHQ-2. Additionally, modifications have been made to the AUD-C to add skip logic and to the PHQ-9 to add a tenth question assessing impact of symptoms on overall functioning.

> December 2007 VistA MHA 3 Patch YS\*5.01\*85 1

# Security Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section addresses any unique legal requirements and responsibilities pertaining to the Mental Health Assistant Version 3, software application and necessary security measures to protect the integrity of the software and its data.

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no unique legal requirements pertaining to Mental Health Assistant software application with the exception that some of the psychological tests are copyrighted. Copyrighted tests are used by permission of the copyright holders. Use of these tests must be consistent with contracts between VHA and copyright holders.

### Security Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### SecureDesktop

> SecureDesktop is a set of security features intended to prevent unattended patients taking on-line tests from using the Personal Computer (PC) for other purposes. The SecureDesktop features construct a screen to cover the entire PC desktop. Non-alphanumeric keys are trapped to keep the patient from using the task bar and operating system functions (such as Task Manager). The Patient Entry button on the Instrument Administrator form is the only instrument data entry method that activates the SecureDesktop features. The Patient Entry button should only be used for the on-line patient administration of data entry of forms, instruments and surveys. The SecureDesktop security features cannot be defeated once the Patient Entry button becomes active. Excessive non-alphanumeric keystrokes are interpreted as “hacking” efforts and MHA is terminated. At the conclusion of the patient’s data entry session, MHA is terminated. Upon termination of the Windows session the user is logged off and the PC is shut down, which means that the user has to enter their network user name and password to log back on to the desktop.

#### Mail Group:

> <u>YS MHA-MHNDB</u>

> This group receives error messages from the HL7 system when problems occur when sending messages to the Mental Health national database.

#### Alerts:

> Alerts are not required for this release.

### Remote Systems:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All GAF scores entered through the Mental Health Assistant GAF form are dynamically sent to the National Patient Care Database (NPCD) at the Austin Automation Center (AAC).

> All Mental Health Assessment data entered through the Mental Health Assistant Instrument Administrator form are dynamically sent from local VistA servers to the NMHDS Oracle databases at the VA Pittsburgh Healthcare System (Highland Dr.).

> VistA MHA3 contains the following Remote Procedures (RPCs):

#### Example: YTQ RPCs

> Example: YTQ RPCs *(Continued)*

### Archiving/Purging:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 software does not include archiving and/or purging capabilities.

### Contingency Planning:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each facility using the MHA software application must develop a local contingency plan to be used in the event of application problems in a live environment. The facility contingency plan must identify procedures used for maintaining the functionality provided by the software in the event of a system outage.

### Interfacing:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The non-menu option, YS BROKER1 \[YS BROKER1\] contains the context necessary to interface MHA Version 3, software application to the V*ist*A database.

### Electronic Signatures:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA Version 3, Addiction Severity Index (ASI) software component utilizes the electronic signature functionality.

### Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 software does not contain any menu options of particular interest to Information Security Officers (ISOs).

### Security Keys:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3, software application did not release any new security keys. However, the YSP security key is required to control access to the results of “non-exempt” tests. Holders of the YSP security key are controlled (i.e., given out by the Chief of Psychology or a senior psychologist at a facility that does not have a Chief of Psychology). The Chief of Psychology or senior psychologist also determines which tests are “exempt” (i.e., the results can be seen by anyone), and which are

> “non-exempt” (i.e., require the YSP key to see the results).

### File Security:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is no file security associated with the release of MHA Version 3 software application.

### References:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Kernel V. 8.0 Systems Manual

### Official Policies:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There is no official policy unique to the MHA Version 3 software application regarding the modification of the software and distribution of the product.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following information contains recommendations and requirements that should be acknowledged prior to installing VistA Mental Health Assistant Version 3 Patch YS\*5.01\*85:

## Recommended Users:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Information Resources Management (IRM) Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IRM staff is recommended for installing and supporting MHA3, Patch YS\*5.01\*85 requirements.

### Mental Health Clinicians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is recommended that Mental Health clinicians enter the MH patient demographics data and define the MH interviews parameters.

### Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA MHA3 Patch YS\*5.01\*85 has been tested by the following Veteran Affairs Medical Centers (VAMCs) and Healthcare Network Systems (HCS):

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Test Sites/Integrated</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Operating System Platform</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Test Site Size</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Atlanta, GA VAMC</td>
<td><blockquote>
<p>Cache/VMS</p>
</blockquote></td>
<td><blockquote>
<p>Large</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>Buffalo, NY (Upstate New</p>
<p>York HCS)</p></td>
<td><blockquote>
<p>Cache/VMS</p>
</blockquote></td>
<td><blockquote>
<p>Large/<strong>Integrated</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Honolulu, HI (VA Pacific</td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Islands HCS)</th>
<th><blockquote>
<p>Cache/VMS</p>
</blockquote></th>
<th><blockquote>
<p>Medium</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Martinez, CA (Northern</p>
<p>California Healthcare System)</p></td>
<td><blockquote>
<p>Cache/VMS</p>
</blockquote></td>
<td><blockquote>
<p>Large</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Windows Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 software application uses a Graphical User Interface (GUI) for the startup, setup, and assignment functions.

## VistA Operating System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mental Health V. 5.01 Package currently runs on the standard hardware platforms used by the Department of Veterans Affairs Health Care System facilities. These systems consist of standard or upgraded Alpha AXP clusters, and run either Cache-VMS or Cache-NT and the Open M product.

## VistA Operating System Performance Capacity

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no significant changes in the performance capacity of the VistA operating system once the Mental Health Assistant Version 3 Patch YS\*5.01\*85 is installed. The software application should not create any appreciable global growth or network transmission problems. There are no memory constraints.

## MHA Central Processing Unit (CPU) Requirement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 software application for Windows XP Operating System CPU requirement is a minimum of 133 MHz.

## MHA Software Application Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA3 Patch YS\*5.01\*85 installation time takes at least 10 minutes during off peak hours

## Users on the System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA users may remain on the system. However, installation of Patch YS\*5.01\*85, should be done during off peak hours.

## Backup Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is highly recommended that a backup of the transport global be performed before installing the VistA Mental Health Assistant Version 3, Patch YS\*5.01\*85.

## Kernel Installation and Distribution System (KIDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mental Health Assistant Version 3 Patch YS\*5.01\*85 distribution is using KIDS.

## Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mental Health Assistant Version 3 Patch YS\*5.01\*85 namespace is YS and YT.

## MHA3 Software Application Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following software applications MUST be installed prior to installing MHA3 Patch YS\*5.01\*85:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>SOFTWARE APPLICATIONS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>VERSIONS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Kernel</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VA FileMan</td>
<td><blockquote>
<p>22.0</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Mailman</td>
<td><blockquote>
<p>8.0</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RPC Broker</td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Toolkit</td>
<td><blockquote>
<p>7.3</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Mental Health</td>
<td><blockquote>
<p>5.01</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td><blockquote>
<p>26</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Required Patch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following patch MUST be installed prior to installing MHA3 Patch YS\*5.01\*85:

#### Software Applications Patch

> Mental Health V. 5.01 YS\*5.01\*76

## MHA3 Menu/Options Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### YS Broker1 \[YS BROKER1\] Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The non-menu option, YS BROKER1 \[YS BROKER1\] contains the context necessary to interface the V*ist*A Mental Health Assistant Version 3 software application to the VistA database.

## Database Integration Agreements (DBIAs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following DBIAs were approved for the release of VistA MHA software application:

#### DBIA \#3266

> \$\$DOB^DPTLK1 YTQAPI11

> Calling routine passes the Patient's DFN and obtains the corresponding date of birth for that patient. If the patient's primary eligibility is 'Employee' then "SENSISTIVE" is passed in place of the date of birth.

> In SUBSCRIBING PACKAGE

#### DBIA \#3267

> \$\$SSN^DPTLK1 YTQAPI11

> On a given patient will display the patient's ssn identifier; except for employees. In SUBSCRIBING PACKAGE

#### DBIA \#1889

> \$\$DATA2PCE^PXAPI YTQTIU

> Provide a utility for ancillary packages such as Laboratory, Surgery, Medicine, Radiology, Text Integration Utility (TIU) and Computerized Patient Record System (CPRS) to non- interactively (silently) add/edit/delete data, including encounter, provider, diagnosis and procedure information.

> In SUBSCRIBING PACKAGE

#### DBIA \#4113

> COMMSG^PXRMSXRM YTQPXRM

> This API will send a MailMan message providing a notification that the indexing of a global is complete.

> DETIME^PXRMSXRM YTQPXRM

> This API will write out the elapsed time that it took to index a global. ERRMSG^PXRMSXRM YTQPXRM

> This API will send a message if errors were found while Clinical Reminders were indexing the global.

> In SUBSCRIBING PACKAGE

#### DBIA \#3351

> \$\$WHATITLE^TIUPUTU YTQTIU

> Call the extrinsic function as follows, to determine the IEN of a given title:

> S TIUTTL=\$\$WHATITLE^TIUPUTU("ADVERSE REACTION/ALLERGY")

> I TIUTTL'\>0 Q

> where the single input parameter for the extrinsic function is the name of the title to be identified.

> Note that the function will return the IEN of the specified title, or -1, if the text passed in the input parameter cannot be resolved as a valid TITLE.

> In SUBSCRIBING PACKAGE

#### DBIA \#3375

> MAKE^TIUSRVP YTQTIU

> Clinical Procedures will be using the MAKE^TIUSRVP API to create TIU Document records and the DELETE^TIUSRVP API to delete TIU DOCUMENT records.

> In SUBSCRIBING PACKAGE

#### DBIA \#3535

> UPDATE^TIUSRVP YTQTIU

> This API updates the record named in the TIUDA parameter, with the information contained in the TIUX(Field \#) array. The

> body of the modified TIU document should be passed in the TIUX("TEXT",i,0) subscript, where i is the line number (i.e., the "TEXT" node should be ready to MERGE with a word processing field). Any filing errors which may occur will be returned in the single valued ERR parameter (which is passed by reference).

#### DBIA \#2944

> TGET^TIUSRVR1 YTQTIU

> This API returns the textual portion of a TIU document Record. It's also callable via RPC TIU GET RECORD TEXT.

#### DBIA# 325

> ADM^VADPT2 YTQHL7

> Used to determine if a patient is an inpatient on a specified date. In SUBSCRIBING PACKAGE

#### DBIA \#4114

> YTQPXRM7 calls –

> ^PXRMINDX(601.2,

> Mental Health has the right to do a direct set and a direct kill on all entries with the first subscript number 601.2.

> In SUBSCRIBING PACKAGE

#### DBIA# 3341

> ^XMB(3.8, 2 MEMBER XMB(3.8, Write w/Fileman In SUBSCRIBING PACKAGE

#### DBIA# 4290

> This DBIA will allow any packages with the DBA approval to be able to read from the Clinical Reminders index.

> GLOBAL REFERENCE: ^PXRMINDX(601.2,

> The index is on file 601.2, Psych Instrument Patient. The structure is:

> ^PXRMINDX(601.2,"IP",INS,DFN,DATE,DAS)

> ^PXRMINDX(601.2,"PI",DFN,INS,DATE,DAS)

> where INS is a pointer to the MH Instrument file. The API to retrieve the associated data is ENDAS^YTAPI10(.YSDATA,DAS). The API is documented in DBIA \#4442

> KEYWORDS: CLINICAL REMINDERS CLINICAL REMINDERS INDEX PXRM

> PXRMINDX

## New VistA Mental Health Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following files were created for the MHA GUI Version 3:

#### MH TESTS AND SURVEYS file (#601.71)

> This file defines the interviews, surveys and tests available in the Mental Health Assistant. Attributes of the instruments include authoring credits, target populations, normative samples and copyright information. Actions available including privileging, reporting of full item content and transmission to the Mental Health National Database are also specified.

#### MH QUESTIONS file (#601.72)

> This file contains a listing of all questions for all Psychological Interviews, Surveys and Tests. This allows usage of questions by multiple instruments. Each question can also linked to an entry in MH INTRODUCTIONS file (#601.73), MH CHOICES file (#601.75), MH CHOICETYPES

> file (#601.751), and the Hint field (#8) in the MH QUESTIONS file (#601.72).

#### MH INTRODUCTIONS file (#601.73)

> This file contains the introductory information given at the beginning of each instrument or at the beginning of a new section of an instrument. The introduction text motivates, gives instructions and sets the frame for the task the patient must complete. The same introduction text can be used by multiple instruments.

#### MH RESPONSE TYPES file (#601.74)

> This file contains what type of response from the user is required for a question. Response types contained in the file include MCHOICE (multiple choice), Integers, Strings, Dates, Memos and Currency. These entries are pointed to the MH QUESTIONS file (#601.72).

#### MH CHOICES file (#601.75)

> This file contains the individual selections possible in a multiple choice question.

#### Examples are:

> Yes or No True or False

1.  Abraham Lincoln
2.  George Washington
3.  George W. Bush
4.  Richard Nixon

> For instruments first defined in the legacy system MH INSTRUMENT file (#601), a single character is specified for a multiple choice answer. If George Washington was the choice selected the legacy value would be 2. Choices are pointed to by the MH CHOICETYPES file (#601.751) which is a collection of choices. Choices are referenced in the MH ANSWERS file (#601.85) as a pointer to the full response.

#### MH CHOICETYPES file (#601.751)

> This file contains a collection of choices from MH CHOICES file (#601.75) and their display sequence. This allows sets of choices to be specified by the MH QUESTIONS file (#601.72). An example of an entry would be: 1. True, 2. False, 3. Undecided. Each multiple choice question must specify a ChoiceType. This way a ChoiceType can be used by multiple instruments and multiple questions.

#### MH INSTRUMENT CONTENT file (#601.76)

> This file specifies which entries from the MH QUESTIONS file (#601.72) are parts of which instrument in the MH TESTS AND SURVEYS file (#601.71). It is the “table of contents” for an interview, survey or test. Also specified are the sequence of questions and display attributes for the introductions, questions and choices. Display attributes can be bold, underlined and font size for the introductions, questions and choices.

#### MH BATTERIES file (#601.77)

> This file contains a list of interview, survey and test order sets.

#### MH BATTERY CONTENTS file (#601.78)

> Ties the entries in the MH BATTERY CONTENTS file (#601.78) to the instruments in the MH TESTS AND SURVEYS file (#601.71).

#### MH BATTERY USERS file (#601.781)

> This file contains a list of all interviews, surveys and tests associated with an entry in the MH BATTERIES file (#601.77). The order of presentation of the interviews, surveys and tests within a battery and which battery belongs to which user in the NEW PERSON file (#200) is also specified.

#### MH SKIPPED QUESTIONS file (#601.79)

> This file specifies the questions to be skipped (by question IEN) if a rule is met for a given question in a given instrument.

#### MH SECTIONS file (#601.81)

> This file specifies sections within an interview, survey and test. The first MH QUESTIONS file (#601.72) is specified along with captions (tab and overall). Display characteristics can also be set.

#### MH RULES file (#601.82)

> This file contains the rules used in administering an interview, survey or test. A rule is an action that is performed when a specified question is answered in a specified manner. An example of a rule would be to enter ‘Not applicable’ to the Question, “Are you pregnant?” if the patient has had a hysterectomy. Rules are complex logic based entries that enables the user to create complex scripts.

#### MH INSTRUMENTRULES file (#601.83)

> This file ties together an instrument in the MH TESTS AND SURVEYS file (#601.71), a question in the MH QUESTIONS file (#601.72) and a rule in the MH RULES file (#601.82). This allows a rule to be used in multiple instruments and for different questions.

#### MH ADMINISTRATIONS file (#601.84)

> The MH ADMINISTRATIONS file (#601.84) contains the data collected during the administration of a specified instrument from the MH TESTS AND SURVEYS file (#601.71) given to a patient at a specific date and time. For each administration of a specified instrument from the MH TESTS AND SURVEYS file (#601.71) there will be an entry in this file. An entry in this file does not store the results of the instrument’s administration but is an index to the instrument’s administration. The entry indicates whether the instrument has been completed, who ordered the instrument, how many questions were answered and if the test has been electronically signed.

#### MH ANSWERS file (#601.85)

> When a patient answers a question, the results are stored in this file. An entry for each question answered, in each administration is stored. Each entry has an MH ADMINISTRATON ID field(#.01) of the MH ADMINISTRATION file (#601.84), a Question NUMBER field (#.01) of the MH QUESTIONS file (601.72) and the response.

#### MH SCALEGROUPS file (#601.86)

> ScaleGroups are collections of MH SCALES file (#601.87) that are logically displayed together. Information needed to graph the scales is stored here. This includes the ordinate title, minimum and maximum values, graph increments and grid lines. All scales need to be associated with a MH SCALEGROUP to be displayed. MH SCALEGROUPS file (#601.86) and MH SCALES file (#601.87) allow multiple scoring possibilities within a single instrument.

#### MH SCALES file (#601.87)

> A MH SCALE is one dimension of measurement in an instrument. An example may simply be a TOTAL as in a spelling test or multiple scales in a personality disorder instrument (depression, anxiety, thought disorder etc.). Each scale has at least one associated entry in the MH SCALEGROUP file (#601.86) and an entry in the MH SCORING KEYS file (#601.91).

#### MH DISPLAY file (#601.88)

> This file contains the entries to set the Windows display attributes for the MH QUESTIONS file (#601.72), MH INTRODUCTIONS file (#601.73), and the MH RESPONSE TYPES file

> (#601.74). Windows display attributes include fonts, bolding, underline, colors, and columns.

#### MH CHOICEIDENTIFIERS file (#601.89)

> This file specifies the displayed numeric options that go along with a multiple choice item. Choice type identifiers can be numbered starting from one, from zero or remain unnumbered.

#### MH SCORING KEYS file (#601.91)

> This file contains the scoring keys. The scoring keys are the "answer sheet" for the specified scale entry in the MH SCALES file (#601.87). When an answer the matches the Target value (i.e., is correct) a specified value is added to the score. An example would be: if the question is “How much is 5 plus 3” the target value would be 8 and 10 points would be added to the total score (grade) in a ten question test to make a possible score of 100.

#### MH RESULTS file (#601.92)

> This file contains results of the scored output of completed instruments.

#### MH REPORT file (#601.93)

> This file contains the reporting format for a specified instrument. Input into this file must be entered only through the Mental Health Editor software.

## Routine Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ROUTINE SUMMARY:

> ================

> The following routines are included in this patch. The second line of each of these routines now looks like: ;;5.01;MENTAL HEALTH; \*\*\[Patch List\]\*\*;Dec 30, 1994

> Checksums Values

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 25%" />
<col style="width: 29%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><blockquote>
<p><strong>Old</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>New</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Patch List</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS85POST</td>
<td><blockquote>
<p>2059692</p>
</blockquote></td>
<td><blockquote>
<p>2059560</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YS85PRE</td>
<td><blockquote>
<p>813879</p>
</blockquote></td>
<td><blockquote>
<p>813879</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTAPI5</td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td><blockquote>
<p>12417658</p>
</blockquote></td>
<td><blockquote>
<p>62,85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTAUIRR</td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td><blockquote>
<p>14880327</p>
</blockquote></td>
<td><blockquote>
<p>37,85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTDOMR</td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td><blockquote>
<p>26438095</p>
</blockquote></td>
<td><blockquote>
<p>31,85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTKIL</td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td><blockquote>
<p>8970368</p>
</blockquote></td>
<td><blockquote>
<p>37,85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTPCL</td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td><blockquote>
<p>7363737</p>
</blockquote></td>
<td><blockquote>
<p>66,85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI</td>
<td>15475641</td>
<td><blockquote>
<p>15475641</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI1</td>
<td>27189337</td>
<td><blockquote>
<p>27189337</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI10</td>
<td>24613112</td>
<td><blockquote>
<p>24613112</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI11</td>
<td>22157825</td>
<td><blockquote>
<p>22157825</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI12</td>
<td>20141561</td>
<td><blockquote>
<p>20141561</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI13</td>
<td>19997427</td>
<td><blockquote>
<p>19997427</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI14</td>
<td><blockquote>
<p>6830812</p>
</blockquote></td>
<td><blockquote>
<p>6830812</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI15</td>
<td>25671527</td>
<td><blockquote>
<p>25671527</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI16</td>
<td>13185422</td>
<td><blockquote>
<p>13185422</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI2</td>
<td>21244483</td>
<td><blockquote>
<p>21244483</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI3</td>
<td>23768089</td>
<td><blockquote>
<p>23768089</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI4</td>
<td><blockquote>
<p>28692651</p>
</blockquote></td>
<td><blockquote>
<p>28692651</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI5</td>
<td><blockquote>
<p>23263110</p>
</blockquote></td>
<td><blockquote>
<p>23263110</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI6</td>
<td><blockquote>
<p>5268725</p>
</blockquote></td>
<td><blockquote>
<p>5268725</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI7</td>
<td><blockquote>
<p>18902958</p>
</blockquote></td>
<td><blockquote>
<p>18902958</p>
</blockquote></td>
<td><blockquote>
<p>*85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQAPI8</td>
<td><blockquote>
<p>32413314</p>
</blockquote></td>
<td><blockquote>
<p>32771511</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQAPI9</td>
<td><blockquote>
<p>22741073</p>
</blockquote></td>
<td><blockquote>
<p>22741073</p>
</blockquote></td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YTQHL7</td>
<td><blockquote>
<p>31149138</p>
</blockquote></td>
<td>31149138</td>
<td><blockquote>
<p>85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>YTQKIL</td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
<td><blockquote>
<p>5269849</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQLIB</td>
<td><blockquote>
<p>8410129</p>
</blockquote></td>
<td><blockquote>
<p>8410129</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQPRT</td>
<td>25124936</td>
<td>25124936</td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQPXRM</td>
<td><blockquote>
<p>4498627</p>
</blockquote></td>
<td><blockquote>
<p>4498627</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQPXRM1</td>
<td><blockquote>
<p>12743110</p>
</blockquote></td>
<td><blockquote>
<p>12743110</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQPXRM2</td>
<td><blockquote>
<p>14658221</p>
</blockquote></td>
<td><blockquote>
<p>14658221</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQPXRM3</td>
<td><blockquote>
<p>16585590</p>
</blockquote></td>
<td><blockquote>
<p>16585590</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQPXRM4</td>
<td><blockquote>
<p>21974840</p>
</blockquote></td>
<td><blockquote>
<p>21974840</p>
</blockquote></td>
<td>85</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 27%" />
<col style="width: 30%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>YTQPXRM5</th>
<th><blockquote>
<p>19969917</p>
</blockquote></th>
<th><blockquote>
<p>19969917</p>
</blockquote></th>
<th>85</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YTQPXRM6</td>
<td><blockquote>
<p>16689405</p>
</blockquote></td>
<td><blockquote>
<p>17034666</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQPXRM7</td>
<td><blockquote>
<p>21919160</p>
</blockquote></td>
<td><blockquote>
<p>21919160</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI001</td>
<td><blockquote>
<p>16371213</p>
</blockquote></td>
<td><blockquote>
<p>16371213</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI002</td>
<td>110963388</td>
<td>110963388</td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI003</td>
<td>107420027</td>
<td>107420027</td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI004</td>
<td>105189787</td>
<td>105189787</td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI005</td>
<td>104556455</td>
<td>104556455</td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI006</td>
<td>104012683</td>
<td>104012683</td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI007</td>
<td>103468973</td>
<td>103468973</td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI008</td>
<td>100582283</td>
<td>100582283</td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI009</td>
<td><blockquote>
<p>99865202</p>
</blockquote></td>
<td><blockquote>
<p>99888363</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI00A</td>
<td><blockquote>
<p>99888363</p>
</blockquote></td>
<td><blockquote>
<p>99132958</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI00B</td>
<td>101279645</td>
<td>101279645</td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI00C</td>
<td>102188832</td>
<td>102188832</td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI00D</td>
<td><blockquote>
<p>98549063</p>
</blockquote></td>
<td><blockquote>
<p>98549063</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI00E</td>
<td><blockquote>
<p>96890307</p>
</blockquote></td>
<td><blockquote>
<p>96890307</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI00F</td>
<td><blockquote>
<p>97231174</p>
</blockquote></td>
<td><blockquote>
<p>97231174</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI00G</td>
<td><blockquote>
<p>96151494</p>
</blockquote></td>
<td><blockquote>
<p>96151494</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI00H</td>
<td><blockquote>
<p>96468871</p>
</blockquote></td>
<td><blockquote>
<p>96468871</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI00I</td>
<td><blockquote>
<p>100432284</p>
</blockquote></td>
<td><blockquote>
<p>100432284</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQQI00J</td>
<td><blockquote>
<p>95575288</p>
</blockquote></td>
<td><blockquote>
<p>95575288</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="even">
<td>YTQQI00K</td>
<td><blockquote>
<p>25448044</p>
</blockquote></td>
<td><blockquote>
<p>25448044</p>
</blockquote></td>
<td>85</td>
</tr>
<tr class="odd">
<td>YTQTIU</td>
<td><blockquote>
<p>11026585</p>
</blockquote></td>
<td><blockquote>
<p>11026585</p>
</blockquote></td>
<td>85</td>
</tr>
</tbody>
</table>

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the ‘LOAD A DISTRIBUTION’ option on the PackMan menu. The Host File name is YS_501_85.KID. Answer YES to the question:

> “Want to Continue with Load? YES//”

2.  The patch has now been loaded into a Transport global on your system. You now need to use KIDS to install the Transport global. On the KIDS menu, under the ‘Installation’ menu, use the following options:

> Print Transport Global

> Compare Transport Global to Current System Verify Checksums in Transport Global Backup a Transport Global

3.  Users may remain on the system, but installation should be done at off peak hours.
4.  Installation will take MORE than five minutes.
5.  From the ‘Installation Menu’ of the KIDS menu, run the option ‘Install Package(s)’ Select the package ‘YS\*5.01\*85’ and proceed with install.
6.  When prompted “Want KIDS to INHIBIT LOGONs during the install//” respond NO. When prompted “Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//” respond NO.
7.  Place the MENTAL HEALTH ASSISTANT VERSION 3 USER MANUAL in a location that can be accessed by MHA users.
8.  Please refer to the INSTALL WINDOWS ILLUSTRATION section of the MENTAL HEALTH ASSISTANT VERSION 3 INSTALLATION GUIDE to install the MHA software.
9.  Place the option YS BROKER1 \[YS BROKER1\] on the Mental Health users secondary menu.
10. The Secure Desktop feature in the MHA software is a security

> feature that locks down computers when patients are completing assessments directly in MHA. Because it locks down all other applications on the computer when activated, it must be loaded directly on the PC where it will be used. It should only be loaded on machines that will be used for patient administered assessments. It should not be pushed out to all machines on the

> network. More detailed information is found in the MHA VERSION 3 INSTALLATION GUIDE.

11. Place the option YS BROKER1 \[YS BROKER1\] on the Mental Health users secondary menu.
12. Enter appropriate members into the Mail Group YS MHA-MHNDB to the system, but installation should be done at off peak hours.
13. Place the MHA application on the CPRS Tools menu.
14. Create progress note title of "Mental Health Diagnostic Study Note" in the progress note hierarchy. This is needed for MHA to automatically pass a note to CPRS from instrument administrations completed within MHA.
15. A new entry is also created in File 870, the HL Logical Link file.

> This entry is YS MHAT. The logical link named YS MHAT is used by the HL7 package to send VistA ADT HL7 messages containing patient demographics, patient administration and patient answers.

> secondary menu.

### MHA 3 Installation Example:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Programmer Options Option: KIDS \<ENTER\> Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: INSTALL \<ENTER\>

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> PU Patch Update

> Select Installation Option: 1\<ENTER\> Load a Distribution Enter a Host File: USER\$:\[MH USER, One\] YS_501_85.KID Use your site specific directory and path

> KIDS Distribution saved on Dec 04, 2007@14:01:27 Comment: MHA3 INSTALL

> This Distribution contains Transport Globals for the following Package(s):

> YS\*5.01\*85 Install Completed

> was loaded on Dec 04, 2007@14:01:27 OK to continue with Load? NO// YES

> Distribution OK!

> Want to Continue with Load? YES// Loading Distribution...

> \<CPM\> Select Installation Option: 2\<ENTER\> Verify Checksums in Transport Global

> Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution

> This Distribution was loaded on Dec 04, 2007@16:24:16 with a headed of MHA INSTALL; Created on Dec 04, 2007@14:01:27

> It consists of the following installs: YS\*5.01\*85

> 57 Routines checked, 0 failed.

> Since we are providing screen shots lets include the results so sites can validate the routine checksums from running this option.

> \<CPM\> Select Installation Option: 3\<ENTER\> Print Transport Global Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution 12/4/07@16:24:16

> =\> MHA3 INSTALL; Created on Dec 04, 2007@14:01:27

> Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution

> This Distribution was loaded on Dec 04, 2007@16:24:16 with a headed of MHA INSTALL; Created on Dec 04, 2007@14:01:27

> It consists of the following installs: YS\*5.01\*85

> \<CPM\> Select Installation Option: 5\<ENTER\> Backup a Transport Global Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution 12/4/07@16:24:16

> =\> MHA3 INSTALL; Created on Dec 04, 2007@14:01:27

> Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution

> This Distribution was loaded on Dec 04, 2007@16:24:16 with a headed of MHA INSTALL; Created on Dec 04, 2007@14:01:27

> It consists of the following installs: YS\*5.01\*85

> Subject: Backup of YS\*5.01\*85 install on Dec 4th, 2007 Replace

> Loading Routines for YS\*5.01\*85............................................

> \<CPM\> Select Installation Option: 6\<ENTER\> Install Package(s)

> Checking Install for Package YS\*5.01\*85

> Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution 12/4/07@16:24:16

> =\> MHA3 INSTALL; Created on Dec 04, 2007@14:01:27

> Select INSTALL NAME: YS\*5.01\*85 Loaded from Distribution

> This Distribution was loaded on Dec 04, 2007@16:24:16 with a headed of MHA INSTALL; Created on Dec 04, 2007@14:01:27

> It consists of the following installs: YS\*5.01\*85 Install Questions for YS\*5.01\*85

> Incoming Files:

> 601.6 MH MULTIPLE SCORING (including data) Note: You already have the 'MH MULTIPLE SCORING' File. I will OVERWRITE your data with mine.

71. MH TESTS AND SURVEYS (including data) Note: You already have the 'MH TESTS AND SURVEYS' File. I will OVERWRITE your data with mine.
72. MH QUESTIONS (including data) Note: You already have the 'MH QUESTIONS' File. I will OVERWRITE your data with mine.
73. MH INTRODUCTIONS (including data) Note: You already have the 'MH INTRODUCTIONS' File. I will OVERWRITE your data with mine.
74. MH RESPONSE TYPES (including data) Note: You already have the 'MH RESPONSE TYPES' File. I will OVERWRITE your data with mine.
75. MH CHOICES (including data) Note: You already have the 'MH CHOICES' File. I will OVERWRITE your data with mine.

> 601.751 MH CHOICETYPES (including data) Note: You already have the 'MH CHOICETYPES' File. I will OVERWRITE your data with mine.

76. MH INSTRUMENT CONTENT (including data) Note: You already have the 'MH INSTRUMENT CONTENT' File. I will OVERWRITE your data with mine.
77. MH BATTERIES

> Note: You already have the 'MH BATTERIES' File.

78. MH BATTERY CONTENTS

> Note: You already have the 'MH BATTERY CONTENTS' File.

> 601.781 MH BATTERY USERS

> Note: You already have the 'MH BATTERY USERS' File.

> 601.79 MH SKIPPED QUESTIONS (including data) Note: You already have the 'MH SKIPPED QUESTIONS' File. I will OVERWRITE your data with mine.

81. MH SECTIONS (including data) Note: You already have the 'MH SECTIONS' File. I will OVERWRITE your data with mine.
82. MH RULES (including data) Note: You already have the 'MH RULES' File. I will OVERWRITE your data with mine.
83. MH INSTRUMENTRULES (including data) Note: You already have the 'MH INSTRUMENTRULES' File. I will OVERWRITE your data with mine.
84. MH ADMINISTRATIONS

> Note: You already have the 'MH ADMINISTRATIONS' File.

85. MH ANSWERS

> Note: You already have the 'MH ANSWERS' File.

86. MH SCALEGROUPS (including data) Note: You already have the 'MH SCALEGROUPS' File. I will OVERWRITE your data with mine.
87. MH SCALES (including data) Note: You already have the 'MH SCALES' File. I will OVERWRITE your data with mine.
88. MH DISPLAY (including data) Note: You already have the 'MH DISPLAY' File. I will OVERWRITE your data with mine.
89. MH CHOICEIDENTIFIERS (including data) Note: You already have the 'MH CHOICEIDENTIFIERS' File. I will OVERWRITE your data with mine.
91. MH SCORING KEYS (including data) Note: You already have the 'MH SCORING KEYS' File. I will OVERWRITE your data with mine.
92. MH RESULTS

> Note: You already have the 'MH RESULTS' File.

93. MH REPORT (including data) Note: You already have the 'MH REPORT' File. I will OVERWRITE your data with mine.

> Incoming Mail Groups:

> Enter the Coordinator for Mail Group 'YS MHA-MHNDB':

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Example: Installation of YS_501_85.KID

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/004.png)

> NOTE: SYSTEM HANGS WHILE INSTALLING DATA, COULD BE UP TO 10 MINUTES.

## MHA3 Installation File Structure and Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Files or Folder</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS_MHA.exe</td>
<td><p>MHA3’s main executable program, which is invoked by CPRS Tools Menu (when running</p>
<p>online) or by the MHA3 desktop shortcut (when running offline).</p></td>
</tr>
<tr class="even">
<td>YS_MHA.HLP</td>
<td><p>MHA3’s Help file, which only contains help</p>
<p>for the ASI module. Online instruments provide their own online help from Vista.</p></td>
</tr>
<tr class="odd">
<td>dwlGina2.dll</td>
<td><p>Critical component of the SecureDesktop system.</p>
<p>This DLL is responsible for preventing unauthorized users from using the CTRL- ALT-DEL keystroke combination to access system menus.</p>
<p>To activate this DLL and provide access to Patient Entry functions in MHA3, a user with Administrator privilege must run the YS_MHA_SD_INSTALLGINA.exe program. Driver is located in C:\Windows\System32 folder</p></td>
</tr>
<tr class="even">
<td>YS_MHA.JCF</td>
<td>JAWS screen-reader configuration file for use with MHA3</td>
</tr>
<tr class="odd">
<td><p>YS_MHA.DLL</p>
<p>MHA3_DLL_Scoring.dll</p></td>
<td><p>DLLs that interface to Clinical Reminders</p>
<p>functions in CPRS. These DLLs are deployed to C:\Program Files\vista\ Common Files</p></td>
</tr>
<tr class="even">
<td>YS_MHA_SD_INSTALLGINA.exe</td>
<td><p>Executable program that is used to activate the dwlGina.dll module and provide access to <strong>Patient Entry</strong> functions in all subsequent MHA3 sessions. Activation needs to occur</p>
<p>only once. ONLY ADMINISTRATORS SHOULD RUN THIS PROGRAM.</p></td>
</tr>
<tr class="odd">
<td>YS_MHA_SD_UNINSTALLGINA.exe</td>
<td><p>Executable program that is used to deactivate the dwlGina.dll module and remove access to <strong>Patient Entry</strong> functions in all subsequent MHA3 sessions. De-activation needs to occur only once. ONLY ADMINISTRATORS</p>
<p>SHOULD RUN THIS PROGRAM.</p></td>
</tr>
<tr class="even">
<td>YS_MHA_VASD.exe</td>
<td>SecureDesktop’s main executable program, which is invoked by the MHA3 executable at the point when the user chooses Patient Entry mode.</td>
</tr>
</tbody>
</table>

> *Continued-----*

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Files or Folder</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Purpose</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Sub-folders</td>
<td>MHA3 relies on data contained in the following subfolders located in the Application Data folder under the user’s profile storage area. This is typically C:\Documents and Settings\&lt;user name&gt;\Application Data\MHA3.</td>
</tr>
<tr class="even">
<td>Answer Files</td>
<td><p>This is the name of the subfolder used to temporarily store patient responses given during any off-line MHA3 sessions. These response files are removed as soon as their contents are uploaded to VistA. The answer files reside in this folder and the file names are based on the instrument-type and the time-date of</p>
<p>administration.</p></td>
</tr>
<tr class="odd">
<td>Instrument Files</td>
<td><p>This is the name of the subfolder containing definition files for all the various instruments that are available via MHA3. MHA3 uses these files to define the characteristics of questions and other elements that instruments have as they are presented to the user. The file names typically consist of a combination of the instrument acronym and the date-time of the last time that the definition was changed</p>
<p>The contents of these instrument definition files mirror the contents found in VistA, and are synchronized each time MHA3 is started on the PC.</p>
<p>The local files are encrypted and remain unchanged, until a newer version of an instrument definition is present on VistA. If a new or updated instrument definition is detected in VistA, the local equivalent file in this folder is updated automatically.</p></td>
</tr>
</tbody>
</table>

> Examples: A typical MHA3 file tree after installing MHA3:

> C:\Program Files\Vista\YS\MHA3 YS_MHA.exe YS_MHA.HLP YS_MHA.JCF

> Uninst000.dat uninst000.exe

> C:\Program Files\Vista\Common Files YS_MHA.DLL

> MHA3_DLL_Scoring.dll

> C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3 is an example path. The actual path will vary with the current user’s configuration.

#### C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3\Answer Files

> This is usually empty, unless there are off-line records that haven’t been uploaded to VistA yet. Example filename: 2~3050623-134647~AUDIT.adm.

#### C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3\\ Instrument Files

> There are usually a large number of files in this folder; all of them are instrument definition files. Example filename: AUDIT~3040624.res.

> Example: Files added to the MHA3 file tree after installing the optional SecureDesktop software:

> c:\Program Files\Vista\YS\MHA3 YS_MHA_SD_INSTALLGINA.exe YS_MHA_SD_UNINSTALLGINA.exe

> YS_MHA_VASD.exe

> C:\Windows\System32

> dwlGina2.dll

> <span id="_bookmark20" class="anchor"></span>After the VistA Mental Health Assistant Version 3 Patch YS\*5.01\*85, has been successfully installed the following instructions must be applied for the software application to function as designed:

# Post Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Create TIU Document Definitions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following progress note title needs to be added to the TIU Document Definition hierarchy using the TIU option Create Document Definitions.

> The title can be entered under the site-appropriate Document Class.

> The title is needed in order to generate a progress note in CPRS from a test administration in MHA. The title was recommended by the Clinical Documents New Title Request Committee in order to be consistent with TIU standardization terminology.

- Mental Health Diagnostic Study

> When the title is set up in TIU, a note will be automatically generated in CPRS, and the note will contain the results of the tests administered in that session of MHA. The note will be linked to the visit location selected at the onset of the testing session, and the visit will be passed as historical.

> Exceptions to this would be any test that is restricted with the YSP key. Administrations of such tests will not pass a progress note to CPRS, in line with the restricted view of the test results to holders of the YSP key.

> Additionally, if an instrument is administered through a clinical reminder dialog, the results that pass will be based on the clinical reminder dialog set up, and will be sent to the note that is active during the processing of reminder dialogs. A separate note will not be created for those results of MHA instruments administered through clinical reminder dialogs.

- Mental Health Assistant and Clinical Reminders

> In the current released versions of MHA and clinical reminders, a limited number of MHA instruments can be placed in clinical reminder dialogs. Any MHA instrument can be used in the reminder logic as a finding.

> Patch YS\*5.01\*85, MHA3, restructures the MH files and allows for usage of an increased number of types of responses in its instruments.

> Clinical reminders has also written a patch, PXRM\*2.0\*6, that allows reminders to work with the new file structure in MHA. The clinical reminders patch will provide the functionality to use any MHA instrument in a reminder dialog. Some of the functionality won’t be available until version 27 of CPRS is released. Until then, any test that includes free text responses cannot be

> <span id="_bookmark21" class="anchor"></span>included in a reminder dialog the Blessed Orientation Memory Concentration test (BOMC) and the Traumatic Brain Injury (TBI) 2<sup>nd</sup> Level Evaluation are two tests that include free text responses in MHA3).

> If a MHA instrument is restricted to users holding the YSP key, then only those users could administer that test if presented in a clinical reminder dialog.

> Clinical reminders also introduces a parameter with patch PXRM\*2.0\*6 that allows a site to set the maximum number of questions a test can have and still be used in a clinical reminder dialog. The concern is that longer tests really should be administered through the MHA GUI rather than a reminder dialog.

> In version 27 of CPRS, a dll will be introduced that enhances how MHA instruments are handled in clinical reminder dialogs. When that is available, MHA instruments that include free text responses can be administered through clinical reminder dialogs.

> With patch PXRM\*2.0\*6, clinical reminders will be able to work with MHA instruments at the level of the scale score and individual question response in the finding logic.

> Additional features are described in more depth in the documentation for PXRM\*2.0\*6.

## Client Software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IRM Staff:

## MHA3 Files Retrieval Locations and Formats

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark22" class="anchor"></span>MHA Version 3, software files are available on the following OIFOs ANONYMOUS. SOFTWARE directories. All sites are encouraged to use their FTP capability to obtain these files. Use the FTP address “download.vista.med.va.gov” (without the quotes) to connect to the first available FTP server where the files are located.

### MHA3 Files Retrieval Locations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>OIFOs</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>FTP ADDRESS</strong></p>
</blockquote></th>
<th><strong>DIRECTORY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

> <span id="_MHA3_Files_Retrieval_Formats" class="anchor"></span><u>MHA3 Files Retrieval Formats</u>

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 29%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>FILE NAMES</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>CONTENTS</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>RETRIEVAL FORMATS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS_501_85.KID</td>
<td>MHA Server Components</td>
<td>ASCII</td>
</tr>
<tr class="even">
<td>YS50185_SETUP_1_0_3_36.exe</td>
<td>Mental Health Assistant</td>
<td><p>BINARY</p>
<p>This file is the complete install for the Mental Health Assistant GUI</p>
<p>Version 1.0.3.36, client.</p></td>
</tr>
<tr class="odd">
<td>YS50185_SD_SETUP_1_0_2_77.exe</td>
<td>SecureDesktop for Mental Health Assistant</td>
<td><p>BINARY</p>
<p>This file is the complete install for the optional SecureDesktop component for Mental Health Assistant GUI</p>
<p>Version 1.0.3.36, client.</p></td>
</tr>
<tr class="even">
<td>YS_MHA.exe</td>
<td>MHA3 Executable</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS_MHA_SD_INSTALLGINA.exe</td>
<td><p>Activate SecureDesktop Executable</p>
<p>DLL used by SecureDesktop</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>dwlGina2.dll</td>
<td><blockquote>
<p>Required security DLL</p>
</blockquote></td>
<td><blockquote>
<p>BINARY</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>YS_MHA.JCF</td>
<td><p>JAWS screen-reader configuration file for use</p>
<p>with MHA3</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td><p>YS_MHA.DLL</p>
<p>MHA3_DLL_Scoring.dll</p></td>
<td><p>DLLs that interface to Clinical Reminders functions in CPRS. These DLLs are deployed to C:\Program</p>
<p>Files\vista\Common Files</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS_MHA_SD_UNINSTALLGINA.exe</td>
<td><p>Deactivate SecureDesktop</p>
<p>Executable</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td>YS_MHA_VASD.exe</td>
<td>SecureDesktop’s main executable</td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS_MHA.HLP</td>
<td><p>Online help file for the</p>
<p>ASI</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td><blockquote>
<p>ANSWER file folder</p>
</blockquote></td>
<td><p>Offline records that not</p>
<p>been uploaded</p></td>
<td>FOLDER</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>INSTRUMENT file folder</p>
</blockquote></td>
<td><p>MH Instruments for</p>
<p>Offline administration</p></td>
<td>FOLDER</td>
</tr>
<tr class="even">
<td>YS50185_MHA3_IG.pdf</td>
<td><p>Mental Health Assistant Version 3 (MHA3) Installation Guide Patch</p>
<p>YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
<tr class="odd">
<td>YS50185_MHA3_IG.doc</td>
<td><p>Mental Health Assistant Version 3 (MHA3) Installation Guide Patch</p>
<p>YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 29%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>YS50185_MHA3_UM.pdf</th>
<th><p>Mental Health Assistant</p>
<p>Version 3 (MHA3) User Manual Patch YS*5.01*85</p></th>
<th>BINARY</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>YS50185_MHA3_UM.doc</td>
<td><p>Mental Health Assistant</p>
<p>Version 3 (MHA3) User Manual Patch YS*5.01*85</p></td>
<td>BINARY</td>
</tr>
</tbody>
</table>

1.  <span id="_bookmark24" class="anchor"></span>Copy the YS50185_SETUP_1_0_3_36.exe to an empty (temporary or scratch) directory.
2.  Run the YS50185_SETUP_1_0_3_36.exe file (i.e., double click on it). This starts the MHA3, installation process. (See the Mental Health Assistant Install Windows Illustrations section on the following pages).
3.  If the optional SecureDesktop functionality is desired, be sure to first install MHA3 running YS50185_SETUP_1_0_3_36.EXE file and then run the file named YS50185_SD_SETUP_1_0_2_77.exe

## Mental Health Assistant Install Windows Illustrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following illustrates the Mental Health Assistant Install windows. When the default responses are accepted, MHA3 is installed into the appropriate V*ist*A directory on the user’s workstation.

### Installing Mental Health Assistant on your Computer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Double click on YS50185_SETUP_1_0_3_36.exe

> Example: From the Mental Health Assistant Welcome dialog box, click on the Next command button (located at the bottom of the window) to continue with the install. The Choose Destination Location dialog box will appear.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/005.png)

### Choose Destination Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: The Choose Destination Location dialog box text asks “Which directory do you want to install this program into? We strongly recommend that, while the drive may be modified, the default directory structure be used (Drive:\Program Files\Vista\YS\MHA3).

> To install to the directory displayed below, click on the Next button.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/006.png)

> To install to a different directory, click Browse and select another directory.

### Folder Does Not Exist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: The Folder Does Not Exist dialog box text asks “The folder: C:\Program Files\Vista\YS\MHA3 does not exist. Would you like the folder to be created?

> To create the folder displayed below, click Yes.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/007.png)

> If the button No is clicked the folder is not created and you are returned to the Select Destination dialog box.

### Select Start Menu Folder

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: The Select Start Menu Folder dialog box text asks “Where should Setup place the program’s shortcuts? We strongly recommend that the program’s shortcuts be placed in the Start Menu Folder.

> To install to the folder displayed below, click Next.

> To install to a different folder, click Browse and select another directory.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/008.png)

### Ready to Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: The Ready to Install dialog box text states “Setup is now ready to begin installing Mental Health Assistant 3 on your computer. Click Install to continue with the installation, or click Back if you want to review or change any settings. Destination location: C:\Program Files\Vista\YS\MHA3. Start Menu folder: Mental Health Assistant 3.

> To continue the setup, Click Install.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/009.png)

### Installing Mental Health Assistant 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example: The Mental Health Assistant 3 Installing dialog box text states “Please wait while Setup installs Mental Health Assistant 3 on your computer.”

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/010.png)

### Completing the Mental Health Assistant 3 Setup Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Click on the Finish command button (located within the Setup - Mental Health Assistant 3 dialog box bottom right side) to exit Setup.

> Example: The Setup - Mental Health Assistant 3 dialog box text displays “Setup has finished installing Mental Health Assistant 3 on your computer. The application may be launched by selecting the installed icons.”

> The first time “Instrument Administrator” is launched, it may take a couple of minutes to load all of the instruments. Subsequent launches of “Instrument Administrator” should be much quicker.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/011.png)

#### Uninstalling MHA3

1.  Click on the Start Button
2.  Click on All Programs
3.  Find the Mental Health Assistant 3 icon group
4.  Click on the Uninstall Mental Health Assistant entry, as shown below.

> Example: MHA3 menu entries on the Windows Start menu. Click on the Uninstall Mental Health Assistant entry.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/012.png)

> Example: Confirmation screen to remove Mental Health Assistant 3. Click on Yes.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/013.png)

> Example: Confirmation screen to that Mental Health Assistant 3 has been uninstalled. Click on the Ok button. MHA3 is now uninstalled.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/014.png)

> <u>NOTE: YS_MHA.dll & MHA3_DLL_Scoring.dll from the Program Files\Vista\Common files</u> <u>folder</u> DLLs are simply place-holders until a future YS patch is released to coincide with CPRS 27+

> If the uninstall option is ran it removes the Mental Health dll files specifically. YS_MHA.DLL is needed to support PXRM\*2\*6 clinical reminders.

# Installing SecureDesktop Functionality in MHA3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The optional Patient-Entry functions built into MHA3 are disabled by default and by design, and should only be enabled if there is a need to use MHA3 for patient-self-administered assessments. If SecureDesktop is installed, it must be installed after MHA3 is installed.

> SecureDesktop files are installed or uninstalled using a separate setup file than the one for installing MHA3. All the files necessary to use SecureDesktop are bundled in a single setup file. The SecureDesktop files MUST be installed to the same folder as the one containing the main MHA3 file (YS_MHA.exe)—this is why MHA3 must be installed first.

> PRIOR to installing the Secure Desktop, the Patient Entry button on MHA3’s Instrument Administrator form is disabled, and these functions are not available to the user.

> Example: To start the installation process, execute the file named

> YS50185_SD_SETUP_1_0_2_77.exe

> This action will display the following Setup – SecureDesktop for Mental Health Assistant 3

> screen. Click on the Next button to continue the installation process.

> ![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/015.png)

> Example: Folder selection screen. Click on the Next button.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/016.png)

> Example: Folder Exists screen. If MHA3 is already installed—as recommended, the Folder Exists confirmation dialog is shown. Click on the Yes button to install to that folder.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/017.png)

> Example: Select Start Menu Folder screen. To continue creating the program’s shortcuts in the

> Start Menu Folder - click on the Next button.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/018.png)

> Example: Ready to Install screen. Click on the Install button to continue with installing SecureDesktop for Mental Health Assistant 3 on your computer.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/019.png)

> Example: Install progress screen.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/020.png)

> Example: Restart computer screen. Click Finish, to complete the installation procedure.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/021.png)

> Example: Before installing SecureDesktop, the Patient Entry button on MHA3’s Instrument Administrator form is disabled, and these functions are not available to the user, as shown below.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/022.png)

> Example: After installing SecureDesktop and running YS_MHA_SD_INSTALLGINA.exe, the Patient Entry button on MHA3’s Instrument Administrator form is enabled, and these functions become available to the user, as shown below.

> A test must also be selected in order to activate the Patient Entry button.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/023.png)

- MHA3 is properly installed.
- The PC’s operating system is Windows XP
- The dwlGina2 DLL has been installed successfully. This is done automatically, when installing SecureDesktop.
- The PC was rebooted after installing SecureDekstop

#### Uninstalling SecureDeskstop

1.  Click on the Start Button
2.  Click on All Programs
3.  Find the Mental Health Assistant 3 icon group
4.  Click on the Uninstall SecureDesktop for MHA3 entry, as shown below.

> Example: MHA3 menu entries on the Windows Start menu. Click on the Uninstall SecureDesktop for MHA3 entry.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/024.png)

> Example: Confirmation screen to remove SecureDesktop. Click on Yes.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/025.png)

> Example: Confirmation screen to restart computer. You must restart the computer after uninstalling SecureDesktop. Click on the Yes button. Be sure to save any unsaved data before you click on Yes. The Patient-Entry feature will no longer be available on MHA3.

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/026.png)

# Setting up VistA MHA3 on CPRS GUI Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This procedure configures VistA so that “Mental Health Assistant” appears as a choice on a user’s Tools menu on the CPRS desktop software. Unlike previous versions of MHA, where this was optional, Version 3 of VistA MHA MUST be started from the CPRS Tools Menu. Selecting this choice from the CPRS Tools menu will offer the user full MHA3 functionality, based on a user’s particular access permissions in VistA.

> The basic steps for setting up VistA MHA3 on the Tools menu are no different from doing it for other applications. The main difference lies in how the Name=Command entry is formatted. The following text capture is taken from the CPRS Setup documentation, to serve as an example of how to perform this step for MHA3:

> Example: Setting up VistA MHA3 on the CPRS Tools menu.

> From the previous example, adjust according to your own system’s settings, such as New Person

> Name and other parameters—consult the CPRS Setup Guide for the meaning of these parameters. The pertinent portion of the example is the “Name=Command:” field. This field should be entered exactly as shown, in a single line—<u>no line-breaks allowed</u>, including all the % parameters that follow the filename and path to the MHA3 executable file.

> The path shown represents a typical path used during a default installation. If your path is different, adjust accordingly. ALL five parameters must be included as shown above, in the precise order in which they are found in the example. Here is what the Name=Command line should look like:

> Example: Mental Health Assistant=C:\Progra~1\Vista\YS\MHA3\YS_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

> Sequence number 2 is shown in the example, but, if you have other entries in the Tools Menu, then the next free sequence number will do just fine.

> After this step is completed, a new choice will appear in the user’s CPRS Tools Menu labeled “Mental Health Assistant”. Clicking on this menu entry will start MHA3 with a selected patient synchronized to the one currently selected in CPRS.

> Refer to the CPRS Setup Guide, dated August 2000, for more information about this procedure.

> <span id="_bookmark35" class="anchor"></span>Setting up VistA MHA 3 on CPRS GUI Tools Menu

## Setting up VistA so that individual MHA3 assessments are also listed on the CPRS GUI Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This procedure configures VistA so that you can add a variable number of individual, specific assessment-types choices, to the Tools menu in the CPRS GUI. This is in addition, or instead of, the Mental Health Assistant choice described above. This step is optional and will have no effect on the procedure described above.

> The steps for setting up individual assessment types are identical to setting up MHA3, with one significant difference: The Name=Command line has one added parameter at the end of the parameter list. This parameter indicates the “code” name of the instrument to be added to the Tools menu. In this example, CAGE is added to the Tools menu. Here is what the Name=Command line should look like to add CAGE:

> Example: Mental Health Assistant=C:\Progra~1\Vista\YS\MHA3\YS_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF CAGE

> As above, this entire Name=Command line should be on one line—no carriage returns, and the next open sequence number on the menu will work fine.

> Example: Two new entries on the CPRS Tools menu; Mental Health Assistant and CAGE (individual assessment type).

![](ys-5-01-85-mental-health-assistant-phase-3-installation-guide/027.png)

# Files with New Entries Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VistA Mental Health patch YS\*5.01\*85 is exporting new entries to the following files:

## PROTOCOL file (#101) New Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PROTOCOL file (#101) contains the following two new protocols that support HL7 messaging for the Mental Health Assistant (MHA) GUI interface.

> Example: PROTOCOL file (#101) two new protocol entries.

## HL7 APPLICATION PARAMETER file (#771) New Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> HL7 APPLICATION PARAMETER file (#771) contains the following new entry:

> The Mental Health Assistant (MHA) GUI application uses the following entry to send messages to the National Mental Health Database.

> Example: HL7 APPLICATION PARAMETER file (#771) new entry

> The entry is distributed as inactive to allow testing without entry in the

> national database.

Files with New Entries Added

> HL LOGICAL LINK file (#870) new Entry

> HL LOGICAL LINK file (#870) contains the following new entry:

> The Mental Health Assistant GUI application uses the following entry to identify MHA related logical link interfaces on VistA. The logical link named YS MHAT is used by the HL7 package to send VistA ADT HL7 messages containing patient demographics, patient administration and patient answers.

> Example: HL LOGICAL LINK file (#870) contains the following new entry:

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: YS*5.01*103 Mental Health Assistant Phase 3 Installation Guide

## Edit TIU Document Definitions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following progress note title needs to be added to the Text Integration Utility (TIU) Document Definition hierarchy using the TIU option Create Document Definitions \[TIUFC CREATE DDEFS MGR\].

The title is needed in order to link an MHA progress note to a selected Consult.

- MENTAL HEALTH CONSULT NOTE is the national note title used by MHA. If this note title already exists, do not add a second one.
- Create a new note with this title under PROGRESS NOTES and then under CONSULTS:

> <u>Edit Document Definitions Jul 21, 2011@13:32:05 Page: 1 of</u>

> BASICS

> <u>+ Name Type</u>

> 2 PROGRESS NOTES CL

> 3 +ADVANCE DIRECTIVE DC

> 4 +HISTORICAL TITLES DC

> 5 +CRISIS NOTE DC

> 6 +CLINICAL WARNING DC

> 19 +CONSULTS DC

> 20 CARDIOLOGY CONSULTS TL

> 21 CARE COORDINATION HOME TELEHEALTH SCREENING CONSULT TL

> 22 DENTAL CONSULT TL

> 23 DERMATOLOGY CONSULTS TL

> 24 FALLS ASSESSMENT TL

> 25 LABORATORY CONSULTS TL

> 26 MEDICINE CONSULTS TL

> 27 MENTAL HEALTH CONSULT NOTE TL

After the installation, you can assign a different note title for each test if you so desire by using the following menu path and option.

MHS MANAGER \[YSMANAGER\]

MHA3 Utilities \[YTQ MHA3 MENU\]

Stop/Re-start Progress Notes for an Instrument \[YTQ PNOTE FLAG\]

Example of linking note title to a test:

Select MH TESTS AND SURVERYS NAME: MORSE FALL SCALE \<-select test

GENERATE PNOTE: Yes// \<-answer Yes

TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// \<-take default

CONSULT NOTE TITLE: \<-select note title

Some tests require the user to have the YSP security key.

### ### Clinicians

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is recommended that clinicians enter the patient demographics data and define the interviews parameters. Any user who would normally use CPRS should also have access to MHA.

## MHA3 Software Application Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA3 Patch YS\*5.01\*103 installation time takes at least 10 minutes during off peak hours.

## Client: GUI Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This version of the client software must be installed as a new installation.

## ## IRM Staff:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** USERS installing SecureDesktop software on a Windows XP environment must have Administrator privileges on the PC Workstation platform.

1\. Copy the YS_501_103_SETUP.exe to an empty (temporary or scratch) directory.

> 2\. Run the YS_501_103_SETUP.exe file (i.e., double click on it). This starts the MHA3, installation process. (See the Mental Health Assistant Install Windows Illustrations section on the following pages).

> 3\. If the optional SecureDesktop functionality is desired, be sure to first install MHA3 using YS_501_103_SETUP.EXE file and then run the file named YS50185_SD_SETUP_1_0_2_77.exe (Released with Patch YS\*5.01\*85).

> As an alternate method of installing the software, ensure that the YS_MHA.exe and borlndmm.dll files are placed in the C:\Program Files\Vista\YS\MHA3 directory (workstation or application server). The two files YS_MHA_A.dll and YS_MHA_AUX.dll must be placed in the C:\Program Files\Vista\Common Files on the workstations of all users.

> <u>IMPORTANT</u>: VA policy requires that the two files YS_MHA_A.dll and YS_MHA_AUX.dll be placed in the C:\Program Files\Vista\Common Files on the workstation of all users.

## Mental Health Assistant Install, Windows Illustrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following illustrates the Mental Health Assistant Install windows. When the default responses are accepted, MHA3 is installed into the appropriate V*ist*A directory on the user’s workstation.

### Installing Mental Health Assistant on your Computer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Double click on YS_501_103_Setup.exe

Example: From the Mental Health Assistant Welcome dialog box, click on the Next command button (located at the bottom of the window) to continue with the install. The Choose Destination Location dialog box will appear.

 ![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/002.png)

<span id="_Toc319647283" class="anchor"></span><u>Choose Destination Location</u>

Example: The Choose Destination Location dialog box text asks “Which directory do you want to install this program into? We strongly recommend that, while the drive may be modified, the default directory structure be used (Drive:\Program Files\Vista\YS\MHA3).

To install to the directory displayed below, click on the Next button.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/003.png)

To install to a different directory, click Browse and select another directory.

<span id="_Toc319647284" class="anchor"></span><u>Folder Does Not Exist</u>

Example: The Folder Does Not Exist dialog box text asks “The folder: C:\Program Files\Vista\YS\MHA3 does not exist. Would you like the folder to be created?

To create the folder displayed below, click Yes.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/004.png)

If the button No is clicked the folder is not created and you are returned to the Select Destination dialog box.

<span id="_Toc319647285" class="anchor"></span><u>Select Start Menu Folder</u>

Example: The Select Start Menu Folder dialog box text asks “Where should Setup place the program’s shortcuts? We strongly recommend that the program’s shortcuts be placed in the Start Menu Folder.

To install to the folder displayed below, click Next.

To install to a different folder, click Browse and select another directory.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/005.png)

<span id="_Toc319647286" class="anchor"></span><u>Select Additional Tasks</u>

Example: Which additional tasks should be performed?

To install desktop icon, check the box.

To install quick launch, check the box, click Next.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/006.png)  
<u>Ready to Install</u>

Example: The Ready to Install dialog box text states “Setup is now ready to begin installing Mental Health Assistant 3 on your computer. Click Install to continue with the installation, or click Back if you want to review or change any settings. Destination location: C:\Program Files\Vista\YS\MHA3. Start Menu folder: Mental Health Assistant 3.

To continue the setup, Click Install.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/007.png)

### Installing Mental Health Assistant 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Mental Health Assistant 3Installing dialog box text states “Please wait while Setup installs Mental Health Assistant 3 on your computer.”

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/008.png)

### Completing the Mental Health Assistant 3 Setup Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the Finish command button (located within the Setup - Mental Health Assistant 3 dialog box bottom right side) to exit Setup.

Example: The Setup - Mental Health Assistant 3 dialog box text displays “Setup has finished installing Mental Health Assistant 3 on your computer. The application may be launched by selecting the installed icons.”

The first time “Instrument Administrator” is launched, it may take a couple of minutes to load all of the instruments. Subsequent launches of “Instrument Administrator” should be much quicker.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/009.png)

### Non-M Software Distributed with Mental Health Assistant 3 (MHA3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to Technical Manual/Security Guide.

Examples: A typical MHA3 file tree after installing MHA3:

C:\Program Files\Vista\YS\MHA3

> YS_MHA.exe

YS_MHA.HLP (From Patch YS\*5.01\*85)

YS_MHA.JCF (From Patch YS\*5.01\*85)

Borlndmm.dll

Unins000.dat  
unins000.exe

C:\Program Files\Vista\Common Files

> YS_MHA_A.dll  
> YS_MHA_AUX.dll

C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3 is an example path. The actual path will vary with the current user’s configuration.

C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3\Answer Files

This is usually empty, unless there are off-line records that haven’t been uploaded to VistA yet. Example filename: 2~3050623-134647~AUDIT.adm.

C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3\\ Instrument Files

There are usually a large number of files in this folder; all of them are instrument definition files. Example filename: AUDIT~3040624.res.

Example: Files added to the MHA3 file tree after installing the optional SecureDesktop software from Patch YS\*5.01\*85, YS50185_SD_SETUP_1_0_2_77.exe.

c:\Program Files\Vista\YS\MHA3

> YS_MHA_SD_INSTALLGINA.exe

> YS_MHA_SD_UNINSTALLGINA.exe

> YS_MHA_VASD.exe

C:\Windows\System32

dwlGina2.dll

#### # Post Installation Instructions

## Uninstalling MHA3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Click on the Start Button
2.  Click on All Programs
3.  Find the Mental Health Assistant 3 icon group
4.  Click on the Uninstall Mental Health Assistant entry, as shown below.

Example: MHA3 menu entries on the Windows Start menu. Click on the Uninstall Mental Health Assistant entry.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/010.png)

Example: Confirmation screen to remove Mental Health Assistant 3. Click on Yes.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/011.png)

Example: Confirmation screen to that Mental Health Assistant 3 has been uninstalled. Click on the Ok button. MHA3 is now uninstalled.

![](ys-5-01-103-mental-health-assistant-phase-3-installation-guide/012.png)

## SecureDesktop & Screen Pass : How to correct Windows-Registry problems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

According to the Birch Grove Software site:

> “Screen Pass is a screen locking system for Windows® that extends the capability of the standard workstation lock and gives network administrators complete control over idle workstations.

> With Screen Pass, network administrators can enforce screensaver password use, screensaver timeout, and screen saver selection. Advanced features include automatic logout, automatic shutdown, customizable administrator override, and auditing of all logon/logoff and lock/unlock events.

> Intended primarily for workstations connected to Novell Netware or Microsoft networks, Screen Pass can be distributed and managed remotely with or without group policy. The central management feature makes Screen Pass ideal for small, medium, and large networks - anywhere that security of idle workstations is a concern.”

Screen Pass installs its own version of a gina.dll and it may take precedence over the one used by Secure Desktop. If SecureDesktop does operate properly these changes may be necessary in the Windows Registry:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GinaDLL=dwlgina2.dll

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GinaDLL_ScreenPass=msgina2.dll

See Remedy Ticket \# HD0000000278953.

## SecureDesktop : How to correct dwlGina2.dll problems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A dwlGina2.dll error problem may occur when a non-administrator uninstalls MHA3 without an administrator first de-activating SecureDesktop.

Here is how to fix it:

1\. Turn off defective PC, if on.

2\. Start the PC and Windows in SAFE mode.

3\. Logon as Administrator.

4\. Find the media containing the YS_MHA_SD_UNINSTALLGINA.exe file. These files are typically found at C:\Program Files\Vista\YS\MHA3. Run YS_MHA_SD_UNINSTALLGINA.exe. Click Yes, to uninstall it.

5\. Reboot in normal mode.

If this doesn’t work, then modify step five by first finding and running YS_MHA_SD_INSTALLGINA.exe. Click Yes, to install it. Then follow the remainder of step five.

## Setting up VistA MHA3 on CPRS GUI Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **WARNING:** THIS STEP IS MANDATORY, TO COMPLETE THE VistA MHA3 INSTALLATION PROCESS.

This procedure configures VistA so that “Mental Health Assistant” appears as a choice on a user’s Tools menu on the CPRS desktop software. Unlike previous versions of MHA, where this was optional, Version 3 of VistA MHA MUST be started from the CPRS Tools Menu. Selecting this choice from the CPRS Tools menu will offer the user full MHA3 functionality, based on a user’s particular access permissions in VistA.

The basic steps for setting up VistA MHA3 on the Tools menu are no different from doing it for other applications. The main difference lies in how the Name=Command entry is formatted. The following text capture is taken from the CPRS Setup documentation, to serve as an example of how to perform this step for MHA3:

Example: Setting up VistA MHA3 on the CPRS Tools menu, GUI Parameters \[ORW PARAM GUI\]

Select GUI Parameters Option: tmGUI\<ENTER\> Tool Menu Items

CPRS GUI Tools Menu may be set for the following:\<ENTER\>

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Division DIV \[REGION 5\]

4 System SYS \[OEX.REDACTED\]

Enter selection: 1\<ENTER\> User NEW PERSON

Select NEW PERSON NAME: MHPROVIDER,ONE\<ENTER\> CPF

------------- Setting CPRS GUI Tools Menu for User: MHPROVIDER,ONE----------

Sequence: ? \<ENTER\>

Enter the sequence in which this menu item should appear.

Select Sequence: 2

Are you adding 2 as a new Sequence? Yes//\<ENTER\>YES

Sequence: 2// \<Enter\>

Name=Command: Mental Health Assistant=C:\Progra~1\Vista\YS\MHA3\YS_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

From the previous example, adjust according to your own system’s settings, such as New Person Name and other parameters—consult the CPRS Setup Guide for the meaning of these parameters. The pertinent portion of the example is the “Name=Command:” field. This field should be entered exactly as shown, in a single line—<u>no line-breaks allowed</u>, including all the % parameters that follow the filename and path to the MHA3 executable file.

The path shown represents a typical path used during a default installation. If your path is different, adjust accordingly. <u>ALL five parameters must be included as shown above, in the precise order in which they are found in the example</u>. Here is what the Name=Command line should look like:

Example: Mental Health Assistant=C:\Progra~1\Vista\YS\MHA3\YS_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

Sequence number 2 is shown in the example, but, if you have other entries in the Tools Menu, then the next free sequence number will do just fine. (Sometimes when cutting and pasting, unseen control characters can be included in the text and will cause the command line to malfunction.)

After this step is completed, a new choice will appear in the user’s CPRS Tools Menu labeled “Mental Health Assistant”. Clicking on this menu entry will start MHA3 with a selected patient synchronized to the one currently selected in CPRS.

Refer to the Computerized Patient Record System (CPRS) Setup Guide for more information about this procedure.

## Setting up VistA MHA3 on CPRS GUI Tools Menu for SecureDesktop

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## If your site uses an APPLICATION SERVER for access MHA3, you will need to create a 2nd instance under CPRS tools. SecureDesktop MUST access MHA3 from the LOCAL MACHINE that SecureDesktop is loaded. You cannot use MHA3 from an application server for SecureDesktop

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: Setting up VistA MHA3 on the CPRS Tools menu for SecureDesktop, GUI Parameters \[ORW PARAM GUI\]

Select GUI Parameters Option: tm GUI\<ENTER\> Tool Menu Items

CPRS GUI Tools Menu may be set for the following:\<ENTER\>

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

3 Division DIV \[REGION 5\]

4 System SYS \[OEX.REDACTED\]

Enter selection: 1\<ENTER\> User NEW PERSON

Select NEW PERSON NAME: MHPROVIDER,ONE\<ENTER\> CPF

------------- Setting CPRS GUI Tools Menu for User: MHPROVIDER,ONE----------

Sequence: ? \<ENTER\>

Enter the sequence in which this menu item should appear.

Select Sequence: 2

Are you adding 2 as a new Sequence? Yes//\<ENTER\> YES

Sequence: 2// \<Enter\>

Name=Command: MHA3_Patient Entry=C:\Progra~1\Vista\YS\MHA3\YS_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

From the previous example, adjust according to your own system’s settings, such as New Person Name and other parameters—consult the CPRS Setup Guide for the meaning of these parameters. The pertinent portion of the example is the “Name=Command:” field. This field should be entered exactly as shown, in a single line—no line-breaks allowed, including all the % parameters that follow the filename and path to the MHA3 executable file.

ALL five parameters must be included as shown above, in the precise order in which they are found in the example. Here is what the Name=Command line should look like:

Example: MHA3_Patient Entry=C:\Progra~1\Vista\YS\MHA3\YS_MHA.exe s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

Sequence number 2 is shown in the example, but, if you have other entries in the Tools Menu, then the next free sequence number will do just fine. (Sometimes when cutting and pasting, unseen control characters can be included in the text and will cause the command line to malfunction.)

After this step is completed, a new choice will appear in the user’s CPRS Tools Menu labeled “MHA3_Patient Entry”. Clicking on this menu entry will start MHA3 with a selected patient synchronized to the one currently selected in CPRS and if SecureDesktop is installed on that machine, the Patient Entry Button will be enabled.

### From: YS*5.01*105 Mental Health Assistant Phase 3 Installation Guide

### MHA3, software application did not release any new security keys. However, the YSP security key is required to control access to the results of “non-exempt” tests. Holders of the YSP security key are controlled (i.e., given out by the Chief of Psychology or a senior psychologist at a facility that does not have a Chief of Psychology). The Chief of Psychology or senior psychologist also determines which tests are “exempt” (i.e., the results can be seen by anyone), and which are “non-exempt” (i.e., require the YSP key to see the results).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Version Check

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MHA3 uses a Dynamic Link Library (DLL) file to verify, score and create reports for some instruments. The DLL is YS_MHA_AUX.dll. Starting with the release of Patch YS\*5.01\*105, MHA3 will verify that the proper YS_MHA_AUX.dll is installed and available for use. If the DLL is outdated, or not present, the user will be notified and in some instances, MHA will not continue.

The MENU TEXT field (#1) of the YS BROKER1 option in OPTION file (#19) is re-named. This change is important because the version numbers listed in the MENU TEXT value are used by the MHA GUIs to determine if the GUI invoked by the user is current.

 

  Before patch: YS BROKER1 version 1.0.3.45~1.0.3.45~1.0.3.45

After patch: YS BROKER1 version 1.0.3.60~1.0.3.60~1.0.3.60

## Client: GUI Software Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** This version of the client software must be installed as a new installation.

IRM Staff:NOTE: USERS installing SecureDesktop software on a Windows environment must have Administrator privileges on the PC Workstation platform.

1\. Copy the YS_501_105_SETUP.exe to temporary (or scratch) directory.

> 2\. Run the YS_501_105_SETUP.exe file (i.e., double click on it). This starts the MHA3, installation process. (See the Mental Health Assistant Install Windows Illustrations section on the following pages).

> 3\. If the optional SecureDesktop functionality is desired, be sure to first install MHA3 using YS_501_105_SETUP.EXE file and then run the file named YS50185_SD_SETUP_1_0_2_77.exe (Released with Patch YS\*5.01\*85).

> As an alternate method of installing the software, ensure that the YS_MHA.exe and borlndmm.dll files are placed in the C:\Program Files\Vista\YS\MHA3 directory (workstation or application server). The two files YS_MHA_A.dll and YS_MHA_AUX.dll must be placed in the C:\Program Files\Vista\Common Files on the workstations of all users.

> <u>IMPORTANT</u>: VA policy requires that the two files YS_MHA_A.dll and YS_MHA_AUX.dll be placed in the C:\Program Files\Vista\Common Files on the workstation of all users.

### Mental Health Assistant Installation, Windows Illustrations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following illustrates the Mental Health Assistant Setup windows. When the default responses are accepted, MHA3 is installed into the appropriate V*ist*A directory on the user’s workstation.

### Installing Mental Health Assistant on your Computer 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Double click on YS_501_105_Setup.exe

Example: From the Mental Health Assistant Welcome dialog box, click on the Next command button (located at the bottom of the window) to continue with the installation. The Choose Destination Location dialog box will appear.

 ![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/002.png)

<span id="_Toc361744489" class="anchor"></span>Choose Destination LocationExample: The Choose Destination Location dialog box text asks “Which directory do you want to install this program into? We strongly recommend that, while the drive may be modified, the default directory structure be used (Drive:\Program Files (x86)\Vista\YS\MHA).

To install to the directory displayed below, click on the Next button.

![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/003.png)

To install to a different directory, click Browse and select another directory.

> **NOTE:** If you are using a WIN XP machine, your directory will look like the following: C:\Program Files\Vista\YS\MHA3  
<span id="_Toc361744491" class="anchor"></span>

Select Start Menu FolderExample: The Select Start Menu Folder dialog box text asks “Where should Setup place the program’s shortcuts? We strongly recommend that the program’s shortcuts be placed in the Start Menu Folder.

To install to the Mental Health Assistant 3 folder, click Next.

To install to a different folder, click Browse and select another directory.

![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/004.png)

<span id="_Toc361744492" class="anchor"></span>Select Additional TasksExample: Which additional tasks should be performed?

To install desktop icon, check the box.

To install quick launch, check the box.

Click Next.

![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/005.png)  
Ready to InstallExample: The Ready to Install dialog box text states “Setup is now ready to begin installing Mental Health Assistant 3 on your computer. Click Install to continue with the installation, or click Back if you want to review or change any settings. Destination location: C:\Program Files\\x86)\Vista\YS\MHA3. Start Menu folder: Mental Health Assistant 3.

To continue the setup, Click Install.

![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/006.png)

### Installing Mental Health Assistant 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Example: The Mental Health Assistant 3Installing dialog box text states “Please wait while Setup installs Mental Health Assistant 3 on your computer.”

![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/007.png)

### Completing the Mental Health Assistant 3 Setup Wizard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on the Finish command button (located within the Setup - Mental Health Assistant 3 dialog box bottom right side) to exit Setup.

Example: The Setup - Mental Health Assistant 3 dialog box text displays “Setup has finished installing Mental Health Assistant 3 on your computer. The application may be launched by selecting the installed icons.”

The first time “Instrument Administrator” is launched, it may take a couple of minutes to load all of the instruments. Subsequent launches of “Instrument Administrator” should be much quicker.

![](ys-5-01-105-mental-health-assistant-phase-3-installation-guide/008.png)

### Non-M Software Distributed with Mental Health Assistant 3 (MHA3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Please refer to the [MHA3 Technical Manual and Security Guide](http://www.va.gov/vdl/application.asp?appid=78) for additional information.

Examples: A typical MHA3 file tree after installing MHA3:

C:\Program Files\\x86)\Vista\YS\MHA3

> YS_MHA.exe

YS_MHA.HLP (From Patch YS\*5.01\*85)

YS_MHA.JCF (From Patch YS\*5.01\*85)

Borlndmm.dll

Unins000.dat  
unins000.exe

C:\Program Files\\x86)\Vista\YS\MHA3

> YS_MHA_A.dll  
> YS_MHA_AUX.dll

C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3 is an example path. The actual path will vary with the current user’s configuration.

C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3\Answer Files

This is usually empty, unless there are off-line records that haven’t been uploaded to VistA yet. Example filename: 2~3050623-134647~AUDIT.rsc.

> **IMPORTANT:** the location of the answer and instrument files depends on whether your workstation is running Windows XP or Windows 7.

For Windows 7, the directory paths are:

 1) C:\Users\\username\_\AppData\Roaming\MHA3\Instrument Files
  2) C:\Users\\username\_\AppData\Roaming\MHA3\Answer Files

C:\Documents and Settings\VHAXXXCliniJ.VHAXX\Application Data\MHA3\\ Instrument Files

Usually, there are many files in this folder; all of them are instrument definition files. Example filename: AUDIT~3040624.rsc.

Example: Files added to the MHA3 file tree after installing the optional SecureDesktop software from Patch YS\*5.01\*85, YS50185_SD_SETUP_1_0_2_77.exe.

c:\Program Files\\x86)\Vista\YS\MHA3

> YS_MHA_SD_INSTALLGINA.exe

> YS_MHA_SD_UNINSTALLGINA.exe

> YS_MHA_VASD.exe

C:\Windows\System32

dwlGina2.dll

#### # Post Installation Instructions

## SecureDesktop & Screen Pass: How to correct Windows-Registry problems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

According to the Birch Grove Software site:

> “Screen Pass is a screen locking system for Windows® that extends the capability of the standard workstation lock and gives network administrators complete control over idle workstations.

> With Screen Pass, network administrators can enforce screensaver password use, screensaver timeout, and screen saver selection. Advanced features include automatic logout, automatic shutdown, customizable administrator override, and auditing of all logon/logoff and lock/unlock events.

> Intended primarily for workstations connected to Novell Netware or Microsoft networks, Screen Pass can be distributed and managed remotely with or without group policy. The central management feature makes Screen Pass ideal for small, medium, and large networks - anywhere that security of idle workstations is a concern.”

Screen Pass installs its own version of a gina.dll and it may take precedence over the one used by Secure Desktop. If SecureDesktop does operate properly these changes may be necessary in the Windows Registry:

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GinaDLL=dwlgina2.dll

HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon\GinaDLL_ScreenPass=msgina2.dll

See Remedy Ticket \# HD0000000278953.

## SecureDesktop: How to correct dwlGina2.dll problems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A dwlGina2.dll error problem may occur when a non-administrator uninstalls MHA3 without an administrator first de-activating SecureDesktop.

Here is how to fix it:

1\. Turn off defective PC, if on.

2\. Start the PC and Windows in SAFE mode.

3\. Logon as Administrator.

4\. Find the media containing the YS_MHA_SD_UNINSTALLGINA.exe file. These files are typically found at C:\Program Files\Vista\YS\MHA3. Run YS_MHA_SD_UNINSTALLGINA.exe. Click Yes, to uninstall it.

5\. Reboot in normal mode.

If this doesn’t work, then modify step five by first finding and running YS_MHA_SD_INSTALLGINA.exe. Click Yes, to install it. Then follow the remainder of step five.

### From: YS*5.01*104 Mental Health Assistant Phase 3 Installation Guide

## Install Patch YS\*5.01\*96 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Only the KID build is needed for Patch YS\*5.01\*96 to be installed. The installation of YS\*501_96_SETUP.exe is not needed. It is replaced by YS_501_104_SETUP.exe.

### From: YS*5.01*150 Mental Health Assistant Phase 3 Installation Guide

### Suicide Prevention Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](ys-5-01-150-mental-health-assistant-phase-3-installation-guide/001.png)
> March 2020

### Submitted as CLIN 0001AX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Contract VA118-16-D-1007, Task Order VA11817F10070006
> *.*
> Revision History
<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><blockquote>
<p><strong>Version</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Change</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Project Manager</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Technical Writer</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>March 2020</p>
</blockquote></td>
<td><blockquote>
<p>1.9</p>
</blockquote></td>
<td><blockquote>
<p>Updated version for Patch 150</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>June 2019</p>
</blockquote></td>
<td><blockquote>
<p>1.8</p>
</blockquote></td>
<td><blockquote>
<p>Updated version for Patch 145</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>May 2019</p>
</blockquote></td>
<td><blockquote>
<p>1.7</p>
</blockquote></td>
<td><blockquote>
<p>Updated version for Patch 147</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>February</p>
</blockquote></td>
<td><blockquote>
<p>1.6</p>
</blockquote></td>
<td><blockquote>
<p>Updated version for Patches 138, 139</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>September 2018</p>
</blockquote></td>
<td><blockquote>
<p>1.5</p>
</blockquote></td>
<td><blockquote>
<p>Updated version for Patch 136</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>August 2018</p>
</blockquote></td>
<td><blockquote>
<p>1.4</p>
</blockquote></td>
<td><blockquote>
<p>Updated version numbers for Patch 134</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>March 2018</p>
</blockquote></td>
<td><blockquote>
<p>1.3</p>
</blockquote></td>
<td><blockquote>
<p>Updated Title and Footers;</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><blockquote>
<p>Booz Allen SPP Project Team</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>August 2014</p>
</blockquote></td>
<td><blockquote>
<p>1.2</p>
</blockquote></td>
<td><blockquote>
<p>Updated Title page</p>
<p>Updated Revision History, p. i-ii</p>
<p>Updated Table of Contents, pp. iii-iv</p>
<p>Changed ICD9 reference to ICD</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>29 February</p>
<p>2012</p>
</blockquote></td>
<td><blockquote>
<p>1.1</p>
</blockquote></td>
<td><blockquote>
<p>Added table “MHA3 Patch YS*5.01*129</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom Mental Health patch YS\*5.01\*150 will be deployed and installed, as well as how it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

## Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is assumed that this patch is being installed into a fully patched Veterans Health Information System and Technology Architecture (VistA) system. In particular patch YS\*5.01\*123 must be installed prior to the installation of this patch.

## Constraints

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There are no constraints beyond the installation into an up-to-date VistA system.

## Timeline

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The deployment and installation are scheduled to run from June 2019 through July 2019 as depicted in the Master Deployment Schedule in the Suicide Prevention Program (SPP) Project Management Plan.

## Site Readiness Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section discusses the locations that will receive the YS\*5.01\*150 deployment.

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA Update (YS\*5.01\*150) will be deployed to each VistA instance. This includes local sites as well as regional data centers. The executable and associated files will also be deployed to client workstations.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for national release, MHA Update (YS\*5.01\*150) will be deployed to all VistA systems.

> The Production IOC testing sites are:

- <span class="mark">REDACTED</span>

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Other than a fully patched VistA system, there is no other preparation required.

## Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Facility Specifics (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When MHA Update (YS\*5.01\*150) is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package.

## Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mental Health patch YS\*5.01\*123 and YS\*5.01\*147 must be installed prior to the installation of YS\*5.01\*150. The environment checks for YS\*5.01\*150 will verify this.

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See previous section for required Mental Health patches.

> This patch installs new instruments that will consume about 2MB of disk space in the ^XTMP global during installation. The growth of the ^YTT global will be about 1MB.

> This patch can be loaded with users in the system but it is recommended that it be installed when user activity is low. Installation time will be less than 5 minutes.

> It is recommended that you use the “Backup a Transport Global” option that is referenced in the installation instructions. This will be useful should it be decided to back out the installation.

> To ensure the integrity of the transport global, use the “Verify Checksums in Transport Global” to compare the checksums with the list that follows:

> The checksums below are new checksums and can be checked with CHECK1^XTSUMBLD.

> Routine Name: YS150PST

> Before: n/a After: B9122642 \*\*150\*\* Routine Name: YTQAPI2D

> Before: B7153551 After: B6639144 \*\*147,150\*\* Routine Name: YTSACE

> Before: n/a After: B2551823 \*\*150\*\* Routine Name: YTSBSL23

> Before: n/a After: B3044905 \*\*150\*\*

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 18%" />
<col style="width: 15%" />
<col style="width: 20%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>Routine Name:</th>
<th>YTSCMQ</th>
<th colspan="3"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B2552097</p>
</blockquote></td>
<td>150</td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSEAT26</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B6312697</p>
</blockquote></td>
<td>150</td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSFOCI</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B4656413</p>
</blockquote></td>
<td>150</td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSMHRM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B2499615</p>
</blockquote></td>
<td>150</td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSNUDEC</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B13752134</p>
</blockquote></td>
<td><blockquote>
<p>150</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSSIP30</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B5052592</p>
</blockquote></td>
<td>150</td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSSIPST</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B5906306</p>
</blockquote></td>
<td>150</td>
</tr>
<tr class="even">
<td>Routine Name:</td>
<td>YTSSWEM</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Before:</p>
</blockquote></td>
<td>n/a</td>
<td><blockquote>
<p>After:</p>
</blockquote></td>
<td><blockquote>
<p>B6610853</p>
</blockquote></td>
<td>150</td>
</tr>
</tbody>
</table>

> Routine list of preceding patches: 123,147

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Installation of MHA Update (YS\*5.01\*150) requires the following:

- Programmer access to VistA instance and ability to install KIDS build.
- Citrix Access Gateway (CAG) installs – access/ability to upload to the CAG.
- Network Share installs – access/ability to upload executable to the network share location.
- Individual workstation installs – access/ability to push executable and supporting files to required work stations.

## Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

3.  From this menu, you may elect to use the following options (When prompted for the INSTALL NAME, enter YS\*5.01\*150):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Use the Install Package(s) option and select the package YS\*5.01\*150
1.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", answer NO.
2.  When prompted "Want to DISABLE Scheduled Options and Menu Options and Protocols? NO//", answer NO.

## Post Install for Instruments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To get Progress Notes to show in CPRS Notes, use one of the following procedures - MHA3 Utilities or FileMan (see samples below).

> After you have changed the PNote field, TIU Title Field or the Consult Note Title Field, make sure the: LAST EDIT DATE in the MH TESTS AND SURVEYS ( \#601.71) file is updated with the current date and time.

> <u>Progress Note Field requirements for 150 instruments.</u> These instruments should have the Write Full Text, PNote, and R Privilege fields populated with either a Yes/No, as indicated in the table below:

<table>
<colgroup>
<col style="width: 53%" />
<col style="width: 14%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Instrument Name</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Write Full Text</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Generate P- Note</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>R Privilege</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The Florida Obsessive Compulsive Inventory (FOCI)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="even">
<td>The Short Warwick–Edinburgh Mental Well-being Scale (SWEMWBS)</td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>YSP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Mental Health Recovery Measure-10 (MHRM-10)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Eating Attitudes Test-26 Item (EAT-26)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Adverse Childhood Experiences (ACE)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Composite Morningness Questionnaire (CMQ)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SHORT INVENTORY OF PROBLEMS - AD (SIP- AD-30)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="even">
<td><p>SHORT INVENTORY OF PROBLEMS - AD (SIP-</p>
<p>AD-Start)</p></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Borderline Symptom List 23 (BSL-23)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Nursing Delirium Screening Scale (NuDESC)</td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>Yes</p>
</blockquote></td>
<td><blockquote>
<p>n/a</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>AD8</td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>No</p>
</blockquote></td>
<td><blockquote>
<p>YSP</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Instructions using the MHA3 Utilities Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> “Stop/Re-Start Progress Notes for an Instrument” on the MHA3 Utilities menu (YTQ MHA3 MENU) can be used to edit the PNote Field (Progress Note), TIU Title Field, and Consult Note Title Field without having to go into FileMan.

> Based on what the PNote field should read, either Yes to show the Progress Note, or No to not show the Progress note, you would need to either “Start” or “Stop” the Progress Note field for the Instrument.

> If a progress note is Yes and should appear, but it is NOT appearing, then you should use the START PROGRESS NOTES instructions below.

> If a progress note is No and should NOT appear, but it IS appearing, then you should use the STOP PROGRESS NOTES instructions below.

> START PROGRESS NOTES:

1.  Stop/Re-Start Progress Notes for an Instrument
2.  Print Test Form
3.  Detailed Definition
4.  Delete Patient Data
6.  Test Usage
7.  Instrument Exchange

> 5 Exempt Test

> Select MHA3 Utilities \<SPPNXT\> Option: 1 Stop/Re-Start Progress Notes for an Instrument

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] GENERATE PNOTE: No// Y Yes

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

> STOP PROGRESS NOTES:

1.  Stop/Re-Start Progress Notes for an Instrument
2.  Print Test Form
3.  Detailed Definition
4.  Delete Patient Data
6.  Test Usage
7.  Instrument Exchange

> 5 Exempt Test

> Select MHA3 Utilities \<SPPNXT\> Option: 1 Stop/Re-Start Progress Notes for an Instrument

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] GENERATE PNOTE: Yes// N No

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// CONSULT NOTE TITLE: MENTAL HEALTH CONSULT NOTE//

> UPDATING LAST EDIT DATE IN FILEMAN IF YOU USE MHA3 UTILITIES:

> Select OPTION: ENTER OR EDIT FILE ENTRIES

> Input to what File: MH TESTS AND SURVEYS// (250 entries) EDIT WHICH FIELD: ALL// LAST

1.  LAST EDIT DATE
2.  LAST EDITED BY CHOOSE 1-2: 1 LAST EDIT DATE THEN EDIT FIELD:

> Select MH TESTS AND SURVEYS NAME: \[Insert instrument name here\] LAST EDIT DATE: FEB 5,2019@19:31// Now (MAR 04, 2019@06:10)

### FileMan Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The user needs to access FileMan and choose option ‘ENTER OR EDIT FILE ENTRIES’.
2.  In ‘Input to what File’ enter MH TESTS AND SURVEYS
3.  For EDIT WHICH FIELD: – GENERATE PNOTE
4.  For THEN EDIT FIELD: TIU TITLE
5.  For THEN EDIT FIELD: CONSULT NOTE TITLE
6.  Last Edit Date: (Enter Current Date)

> Press return and at the prompt: Select MH TESTS AND SURVEYS NAME: enter name of instrument

> For field ‘GENERATE PNOTE:’ enter “YES” or “NO”, depending on the instructions provided for each instrument in this Install Guide. For FIELD ‘TIU TITLE:’ enter the TIU Title as defined by your site

> For FIELD ‘CONSULT NOTE TITLE:’ enter the title of the CONSULT NOTE as defined by your site

> For LAST EDIT DATE: enter current date

> Exit FileMan and your notes should now save to CPRS Notes.

> <u>Example for Instrument: ‘CES’</u>

> Select OPTION: ?

> Answer with OPTION NUMBER, or NAME Choose from:

1.  ENTER OR EDIT FILE ENTRIES
2.  PRINT FILE ENTRIES
3.  SEARCH FILE ENTRIES
4.  MODIFY FILE ATTRIBUTES
5.  INQUIRE TO FILE ENTRIES
6.  UTILITY FUNCTIONS
7.  OTHER OPTIONS
8.  DATA DICTIONARY UTILITIES
9.  TRANSFER ENTRIES

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

> Input to what File: MH TESTS AND SURVEYS// (250 entries) EDIT WHICH FIELD: ALL// GENERATE PNOTE

> THEN EDIT FIELD: TIU TITLE

> THEN EDIT FIELD: CONSULT NOTE TITLE THEN EDIT FIELD: LAST EDIT DATE

> Select MH TESTS AND SURVEYS NAME: CES GENERATE PNOTE: Yes// Yes

> TIU TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE//

> CONSULT NOTE TITLE: MENTAL HEALTH DIAGNOSTIC STUDY NOTE// LAST EDIT DATE: FEB 5,2019@19:31// Now (MAR 04, 2019@06:10)

## Installation Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To verify that everything is installed properly, do the following:

- Launch CPRS.
- From the CPRS menu, select Tools, then Mental Health Assistant (MHA).
- ![](ys-5-01-150-mental-health-assistant-phase-3-installation-guide/002.png)As MHA starts you should see the splash screen with version 1.0.3.75 displayed in the lower right corner.

> When MHA prompts for user credentials, it should use the Personal Identity Verification (PIV) Personal Identification Number (PIN) prompt, rather than access/verify codes.

![](ys-5-01-150-mental-health-assistant-phase-3-installation-guide/003.png)

> If MHA prompts for a PIV PIN as it is starting, the software has been installed properly. (If the Single Sign-On Integration (SSOi) servers are not available, you will see the usual access/verify prompt.)

> After installation, notify mental health package users that the following new Suicide and Depression Screening instruments are available:

<table>
<colgroup>
<col style="width: 71%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Instrument</p>
</blockquote></th>
<th><blockquote>
<p><strong>Identifier</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The Florida Obsessive Compulsive Inventory (FOCI)</td>
<td>FOCI</td>
</tr>
<tr class="even">
<td>The Short Warwick–Edinburgh Mental Well-being Scale (SWEMWBS)</td>
<td>SWEMWBS</td>
</tr>
<tr class="odd">
<td>Mental Health Recovery Measure-10 (MHRM-10)</td>
<td>MHRM-10</td>
</tr>
<tr class="even">
<td>Eating Attitudes Test-26 Item (EAT-26)</td>
<td>EAT-26</td>
</tr>
<tr class="odd">
<td>Adverse Childhood Experiences (ACE)</td>
<td>ACE</td>
</tr>
<tr class="even">
<td>Composite Morningness Questionnaire (CMQ)</td>
<td>CMQ</td>
</tr>
<tr class="odd">
<td>SHORT INVENTORY OF PROBLEMS - AD (SIP-AD-30)</td>
<td>SIP-AD-30</td>
</tr>
<tr class="even">
<td>SHORT INVENTORY OF PROBLEMS - AD (SIP-AD-Start)</td>
<td>SIP-AD-START</td>
</tr>
<tr class="odd">
<td>Borderline Symptom List 23 (BSL-23)</td>
<td>BSL-23</td>
</tr>
<tr class="even">
<td>Nursing Delirium Screening Scale (NuDESC)</td>
<td>NuDESC</td>
</tr>
<tr class="odd">
<td>AD8</td>
<td>AD8</td>
</tr>
</tbody>
</table>

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Database Tuning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> It is possible to partially back-out the installation of YS\*5.01\*150. This would involve restoring instrument specifications to their previous state and then restoring the saved routines. The back- out of changes to the data dictionary would require a patch to a patch.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please contact VistA support and the development team before attempting a back-out. The back- out procedure will still leave some changes in place. In addition, the installation of subsequent patches may be problematic if YS\*5.01\*150 is not installed.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A back-out should only be considered if there is a patient safety issue, if MHA no longer functions, or if there is some other catastrophic failure.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The risks vary depending on what is causing the failure of the system. The main risk is that the Mental Health package would be left in an unknown configured state.

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA system manager determines if a back-out of YS\*5.01\*150 should be considered.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you wish to restore newly installed instruments to their previous state, you must do that <u>before</u> any other back-out steps. See the instructions for restoring the previous instrument state in the Rollback Procedure section to do this.

> To back-out routines, you must have already selected the “Backup a Transport Global” option during the installation process. To restore the previous routines:

1.  Choose the PackMan message containing the backup you created during installation.
2.  Invoke the INSTALL/CHECK MESSAGE PackMan option.
3.  Select Kernel Installation & Distribution System Option: Installation
4.  Use the Install Package(s) option to install the previously saved routines.

> If you need to back-out data dictionary modifications, remove protocols, options, or templates, you will need to contact the development team for a patch.

## Back-out Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](ys-5-01-150-mental-health-assistant-phase-3-installation-guide/004.png)A successful back-out may be verified by running MHA and seeing a splash screen with the highlighted version number:

> MHA should prompt for access/verify instead of PIV PIN and run successfully.

> Verification of the back-out procedure would be the resolution of the problem that caused the need for the back-out.

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> YS\*5.01\*150 adds new and updates existing mental health instruments. It is possible to roll back these changes within one week of the installation.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A rollback might be considered if the behavior of mental health instruments appears to be adversely affected after installation of YS\*5.01\*150. The VistA support and product development team should be contacted to determine if there is an alternative fix short of a rollback.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A rollback could adversely impact future installations of mental health instruments and cause problems with scoring existing mental health instruments.

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The VistA system manager determines if a rollback of mental health instruments distributed by YS\*5.01\*150 should be considered.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> These steps assume that there is a compelling reason to rollback specific instruments to their previous state.

> For instruments that have been inactivated by YS\*5.01\*150 that need to be made active again:

- Using FileMan, edit the OPERATIONAL field (#10) and the LAST EDIT DATE field (#18) in the MH TESTS AND SURVEYS file (601.71). Select the instrument that requires re-activation.
- Change the value of the OPERATIONAL field from “Dropped” back to “Yes”
- Change the value of the LAST EDIT DATE field to ‘NOW’.

> Should it be required to move instruments back to being scored in YS_MHA_AUX DLL, contact the Mental Health development team for a routine that can find the appropriate records and make the replacement.

> Optionally, if you want to see how many records will be restored, choose “Trial Install” then select the number of the backup you wish to restore.

> When you are ready to restore an instrument, choose “Install Exchange Entry” then select the number of the backup you want to restore.

## Rollback Verification Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Verify the restore by checking to see that the instrument behaves as it did prior to the install.

## Appendix A - Acronyms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Acronym</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CAG</td>
<td><blockquote>
<p>Citrix Access Gateway</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CD</td>
<td><blockquote>
<p>Critical Decision</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DIBO&amp;RG</td>
<td><blockquote>
<p>Deployment, Installation, Back-out, and Rollback Guide</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IOC</td>
<td><blockquote>
<p>Initial Operating Capability</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>MHA</td>
<td><blockquote>
<p>Mental Health Assistant</p>
</blockquote></td>
</tr>
<tr class="even">
<td>PIN</td>
<td><blockquote>
<p>Personal Identification Number</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PIV</td>
<td><blockquote>
<p>Personal Identity Verification</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SPP</td>
<td><blockquote>
<p>Suicide Prevention Package</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SQA</td>
<td><blockquote>
<p>Software Quality Assurance</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SSOi</td>
<td><blockquote>
<p>Single Sign-On Integration</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Acronym</strong></th>
<th><blockquote>
<p><strong>Definition</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VA</td>
<td><blockquote>
<p>Department of Veterans Affairs</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VAMC</td>
<td><blockquote>
<p>Veterans Affairs Medical Center</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VIP</td>
<td><blockquote>
<p>Veteran-focused Integration Process</p>
</blockquote></td>
</tr>
<tr class="even">
<td>VistA</td>
<td><blockquote>
<p>Veterans Health Information System and Technology Architecture</p>
</blockquote></td>
</tr>
</tbody>
</table>

### From: YS*5.01*130 Mental Health Assistant Phase 3 Installation Guide

### Deployment Topology (Targeted Architecture)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MHA Update (YS\*5.01\*130) will be deployed to each VistA instance. This includes local sites as well as regional data centers. The executable and associated files will also be deployed to client workstations. For the web application portion, it is deployed in the Microsoft Azure cloud environment.

### Site Information (Locations, Deployment Recipients)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The initial deployment will be to Initial Operating Capability (IOC) sites for verification of functionality. Once testing is completed and approval is given for national release, MHA Update (YS\*5.01\*130) will be deployed to all VistA systems.

> The Production IOC testing sites are:

- Milwaukee Veterans Affairs Medical Center (VAMC)
- Orlando VAMC

### Site Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Other than a fully patched VistA system, there is no other preparation required.

### Facility Specifics (optional)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### Hardware

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IPad, Kiosk

### Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> N/A

### Communications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When MHA Update (YS\*5.01\*130) is released, the released-patch notification will be sent from the National Patch Module to all personnel who have subscribed to notifications for the Mental Health package.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The MHA Web Patient Entry (YS\*5.01\*130) Windows client is being released as a host file. The preferred method is to retrieve files from download.vista.med.va.gov.

> This transmits the files from the first available server. Sites may also elect to retrieve files directly from a specific server.

> Sites may retrieve the software and/or documentation using Secure File Transfer Protocol (SFTP) from the ANONYMOUS.SOFTWARE directory at: <span class="mark">REDACTED</span>

> Documentation can also be found on the VA Software Documentation Library at: [<u>http://www.va.gov/vdl/</u>](http://www.va.gov/vdl/)

> MHA Web Patient Entry file

| Files to be downloaded | File Contents  | Download Format |
|------------------------|----------------|-----------------|
| YS_501_130.ZIP         | MHA executable | Binary          |

### YS\*5.01\*130 KIDS Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This patch can be loaded with users in the system, but it is recommended that it be installed when user activity is low. Installation time will be less than 5 minutes.

1.  Choose the PackMan message containing this patch and invoke the INSTALL/CHECK MESSAGE PackMan option.
2.  Start up the Kernel Installation and Distribution System Menu \[XPD MAIN\]:

> Edits and Distribution ... Utilities ...

> Installation ...

> Select Kernel Installation & Distribution System Option: Installation

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

3.  From this menu, you may elect to use the following options (when prompted for the INSTALL NAME, enter YS\*5.01\*130):
1.  Backup a Transport Global - This option will create a backup message of any routines exported with this patch. It will not backup any other changes such as DD's or templates.
2.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when this patch is installed. It compares all components of this patch (routines, DD's, templates, etc.).
3.  Verify Checksums in Transport Global - This option will allow you to ensure the integrity of the routines that are in the transport global.
4.  Use the Install Package(s) option and select the package: YS\*5.01\*130.
1.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//", answer NO.
2.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//", answer NO.
3.  When prompted "Want to DISABLE Scheduled Options and Menu Options and Protocols? NO//", answer NO.

### YS\*5.01\*130 GUI Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ZIP file contains the updated MHA GUI executable file. Download the ZIP file and extract the file.

> The following methods of installation are available. Sites' choice of which method(s) to use will depend upon Regional/VISN policies, Local Area Network (LAN) performance or other local circumstances. User requirements, physical location and methods of connection to the VA network may warrant more than one of the options below to be used.

#### Network (shared) installation:

> This method is typically the simplest to maintain, providing the local network infrastructure is robust enough to handle the additional traffic caused by users running the MHA GUI executable (YS_MHA.exe) across the LAN.

> The MHA executable (YS_MHA.exe) is copied to a network shared location.

> Since MHA is launched from the CPRS toolbar, CPRS must know where to find it on the network drive (see Section 4.5.3 below). Use the parameter, ”ORWT TOOLS MENU”, to enter the network location of YS_MHA.exe.

> *Note:* MHA no longer uses the file, YS_MHA_AUX.dll, so it is not necessary to update the YS MHA_AUX DLL LOCATION parameter.

#### Citrix installation:

> The MHA executable (YS_MHA.exe) and supporting files are installed and run from a remote workstation, and the user views the remote workstation’s screen on their local workstation.

> For the local site users, this method is on a similar level to the Network (shared) installation above. The users' workstations require only an appropriate shortcut (and the necessary Citrix Access Group (CAG) infrastructure).

> Note: For issues with CAG, please contact your local or national help desk.

> For the Citrix Farm administrator, this method involves installations on the host in a similar manner to the manual installation method outlined below.

#### Manual install:

> This method is used primarily for advanced users and at testing locations.

> Note: You may need to have a user with Administrator rights complete this step.

> The following steps will update an existing installation of MHA, if one exists on the workstation. These steps use the default file locations.

1.  Locate the YS_501_130.ZIP file and unzip it.
2.  Copy the unzipped YS_MHA.exe to C:\Program Files x86)\Vista\YS\MHA\\

> If desired, you may use different directories than those specified above, but you must also update the ORWT TOOLS MENU parameters to reflect the file location.

#### SCCM install:

> An SCCM package is available for deployment to workstations at a site. To deploy via SCCM, request that the “Mental Health Assistant ” program be deployed.

### Setting Connector Proxy User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To create a connector proxy user:

1.  You must hold the Kernel XUMGR key.
2.  Add a new connector proxy user by using the Foundations menu on your M system and choosing the Enter/Edit Connector Proxy User option.
3.  The account requires no additional information from what is prompted for by the option.
4.  Leave the connector proxy user's Primary Menu empty.
5.  The IP and port of VistaLink listener on IOC cloud is mentioned below:

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 34%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>Example</th>
<th><blockquote>
<p>IP#</p>
</blockquote></th>
<th><blockquote>
<p>PORT# / TCP</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Milwaukee</td>
<td><blockquote>
<p>XXXXX</p>
</blockquote></td>
<td><blockquote>
<p>XXXX /TCP</p>
</blockquote></td>
</tr>
</tbody>
</table>

6.  Securely communicate the access code and verify code for the connector proxy user to the following personal:

> <span class="mark">REDACTED</span>

- Do not enter divisions for a connector proxy user
- Do not enter a primary menu
- Do not also use the connector proxy user as a test "end-user"
- Utilize the user only as a connector proxy user

### Setting MHA on the CPRS Tools Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This procedure configures VistA so that “Mental Health Assistant” appears as a choice on a user’s Tools menu on the CPRS desktop software. Unlike previous versions of MHA, where this was optional, Version 3 of VistA MHA MUST be started from the CPRS Tools Menu. Selecting this choice from the CPRS Tools menu will offer the user full MHA3 functionality, based on a user’s access permissions in VistA.

> The basic steps for setting up VistA MHA3 on the Tools menu are no different from doing it for other applications. The main difference lies in how the Name=Command entry is formatted. The following text capture is taken from the CPRS Setup documentation, to serve as an example of how to perform this step for MHA3:

> Example: Setting up VistA MHA3 on the CPRS Tools menu, GUI Parameters \[ORW PARAM GUI\]

> From the previous example, adjust according to your own system’s settings, such as directory path, New Person Name and other parameters—consult the CPRS Setup Guide for the meaning of these parameters. The pertinent portion of the example is the “Name=Command:” field. This field should be entered in a single line—<u>no line-breaks allowed</u>, including all the % parameters that follow the filename and path to the MHA3 executable file.

> The path shown represents a typical path used during a default installation. If your path is different, adjust accordingly. ALL five parameters must be included as shown above, in the precise order in which they are found in the example. Here is what the Name=Command line should look like:

> Mental Health Assistant=”C:\Program Files (x86)\Vista\YS\MHA3\YS_MHA.exe” s=%SRV p=%PORT c=%DFN u=%DUZ m=%MREF

> Sequence number 2 is shown in the example, but, if you have other entries in the Tools Menu, then the next free sequence number will do just fine. (Sometimes when cutting and pasting, unseen control characters can be included in the text and will cause the command line to malfunction.)

> After this step is completed, a new choice will appear in the user’s CPRS Tools Menu labeled “Mental Health Assistant”. Clicking on this menu entry will start MHA3 with a selected patient synchronized to the one currently selected in CPRS.

> Refer to the Computerized Patient Record System (CPRS) Setup Guide for more information about this procedure.

## Post-Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After the KIDS build for YS\*5.01\*130 is installed, the existing MHA executable (1.0.3.75) and the new MHA executable (1.0.3.80) will both still function. A simultaneous update of the Windows executable is not required. This provides the option of having some users continue with the existing executable while others (perhaps those with access to iPads or kiosks) use the new executable. Adding another MHA item to the CPRS Tools menu can accomplish this. These are the basic steps:

- Rename the new "YS_MHA.exe" to something like "YS_MHA_130.exe" and place it in the directory where you currently have YS_MHA.exe.
- Edit the parameter, ORWT TOOLS MENU, and add a temporary item named something like "MHA Patient Entry" that invokes the executable that you just renamed. (See Setting MHA on the CPRS Tools Menu).
- When you are ready for all users to use the new executable, simply delete the YS_MHA.exe file and rename "YS_MHA_130.exe" to "YS_MHA.exe". Don't forget to remove the temporary item from the ORWT TOOLS MENU.

> If your site's workstations are all Windows 10 and you are not using "Secure Desktop" with MHA anymore, you can just move to the new YS_MHA.exe immediately, without adding a new item to the CPRS Tools menu.

## Prerequisite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Users should have access to the VA government Azure subscription. An active zero account is required to access the Azure dashboard. A GFE laptop or desktop with elevated privileges and an active VA VPN connection are necessary. The following software is also required:

1)  Reflections Workspace
2)  WinSCP
3)  GitBash

> This guide assumes no existing production virtual machines exist.

## SSH Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Using GitBash(Windows) or a bash terminal(Linux/Mac), create an SSH key pair that is used to SSH into Linux without using a password. Open a Git Bash terminal (Windows) or bash shell (Linux/Mac) and use ssh_keygen to create an SSH key pair.

> \$ ssh-keygen -t rsa -b 2048

> This command generates public and private keys with the default name of id_rsa in the ~/.ssh directory. Save this file for later.

## Create a VM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/004.png)Sign in to the Azure portal available [<u>here</u>.](https://portal.azure.us/%23%40vaazuregov.onmicrosoft.com/dashboard/private/da2c856d-39c7-46eb-8e29-7ea861eb900b)

> Select “Sign in using an X.509 certificate”

> The system would respond with a list of certificates. Select the valid certificate for your zero token and enter your PIN.

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/005.png)On successful authentication, the user is navigated to Azure portal as shown below:

> Click Resource groups in the left panel of the Azure portal, the portal shows available resource groups as shown below:

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/006.png)

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/007.png)We are creating virtual machines for production, select the SPP-PROD-INT-SOUTH-PROD-RG resource group.

> In the list of resources, select the AzureBaseFeb2019-image.

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/008.png)

> Click “Create VM” at the top of the portal

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/009.png)

> Enter details as shown:

> Resource group: Leave the default selected.

> Virtual Machine Name: Enter the name of the virtual machine (eg. vac21appspp200)

> Size: Find and select “Standard F8s”

> Administration type: Since we are creating administrative account, select SSH public key, type your user name, then paste your public key into the text box. Remove any leading or trailing white space in your public key.

> User Name: sppAdmin

> SSH Key: Copy and paste the public part of the SSH key here. Press Next : Disks

> Leave Premium SSD selected. Select Next : Networking

> Select default virtual network and any available subnet for this resource group. Since VM is not accessible from public network, select None for Public IP address.

> Select “Allow selected ports and select all options from the list (HTTP, HTTPS, SSH, RDP) Press Review + Create

> Click Create button. It will take a few minutes for VM to be deployed. Once deployed, the following screen will display the notifications box in the right column.

![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/010.png)

> Push Pin to dashboard button, all resources created are displayed in the resource group.

> Push Go to resource button and the following screen is displayed.

![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/011.png)

1.  Connect to the virtual machine

> Configure Reflections to Connect to Cloud

> Configure a session to connect to a cloud server and Configure Reflections Security to generate publick key.

1.  Open up MicroFocus Reflections
2.  Go to File, New VT Terminal
3.  Click on Secure Shell for the Connection
4.  Enter the IP address, (10.245.195.212) (This is an example. Please check the IP’s of the virtual machines across resource groups)
5.  Enter sppprodadmin for the user name and Kerberos for the ssh configuration scheme.
6.  Check the Configure additional settings checkbox

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/012.png)

7.  Click OK
8.  Click on Set Up Connection Security

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/013.png)

9.  Click on the User Keys tab

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/014.png)

10. Click on Generate
11. Keep the Key Type as RSA and Key Length as 2048
12. Enter a passphrase that you will remember and click Create.

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/015.png)

13. Leave the key name and location default and click Save

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/016.png)

14. You should see a successful key generated:

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/017.png)

15. Click Close
16. This key will be used for authentication.

> WinSCP: It’s a popular free open source SFTP client, FTP client SFTP and FTP client for Windows, a powerful file manager that will improve your productivity.

> Add the private key to the cloud server for authentication. Please contact the administrator for private-key.ppk Download and install from [<u>https://winscp.net/eng/download.php</u>](https://winscp.net/eng/download.php)

> What is SSH private and public key:

> Password authentication is the default method most SSH (Secure Shell) clients use to authenticate with remote servers, but it suffers from potential security vulnerabilities.

> An alternative to password authentication is public key authentication, in which we generate and store on your computer a pair of cryptographic keys and then configure our server to recognize and accept your keys.

> Because a password isn’t required at login, we are able to able to log in to servers from within scripts or automation tools that we need to run unattended. SSH public-key authentication relies on asymmetric

> cryptographic algorithms that generate a pair of separate keys (a key pair), one "private" and the other "public". You keep the private key a secret and store it on the computer you use to connect to the remote system

1.  Create FTP connection to the cloud. This tool enables to move Jar file to the virtual machine. Click New Site, the following window will open. Enter the IP address of the virtual machine. Leave port default value

![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/018.png)

2.  Find the key you just created. It will be in the folder: C:\Users\\username}\Documents\Micro Focus\Reflection\\ssh
3.  Open the file using a text editor that is the version WITH the .pub extension. (Note – Use the “Open With” option

> and choose your text editor)

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/019.png)

4.  Using the text editor, CAREFULLY put all the hexadecimal characters on one line.

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/020.png)

![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/021.png)

5.  Copy the string into your buffer.
6.  Connect to the cloud server using WinSCP. Your default directory will be /home/sppadmin.
7.  Change directory to the hidden subfolder .ssh by clicking on the blue /home/sppadmin/ bar.

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/022.png)

8.  Add to the end of the directory string /.ssh

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/023.png)

9.  Edit the authorized_keys file

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/024.png)

10. Add on to the end of the file:
    1.  Type in ssh-rsa
    2.  Paste in your string
    3.  Press the Save icon

![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/025.png)

11. Close WinSCP
12. Connect to the cloud server
1.  Go to Reflections
2.  Use the connection you configured to the cloud server.
3.  A Reflections Secure Shell popup should appear. Click OK

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/026.png)

4.  ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/027.png)You should then be logged in
5.  If it prompts for a password, then the key configuration is incorrect. Make sure that in your connection settings that your new key is checked:

> ![](ys-5-01-130-mental-health-assistant-phase-3-installation-guide/028.png)

> Please contact the administrator for private-key.ppk

#### Software Installation

> Connect to the cloud server as shown above (13)

#### Login as root user:

> \$ sudo su –

#### Update the server

> yum update -y --exclude=BESAgent --exclude=CentrifyDC --exclude=CentrifyDC-curl -- exclude=CentrifyDC-openldap --exclude=CentrifyDC-openssh --exclude=CentrifyDC- openssl \>/tmp/yum-out 2\>&1 &

#### Install GCC

> \# yum install -y gcc-c++ make

> Loaded plugins: product-id, rhnplugin, search-disabled-repos, subscription-:manager This system is not registered with RHN Classic or Red Hat Satellite.

> You can use rhn_register to register.

> Red Hat Satellite or RHN Classic support will be disabled. rhel-7-server-rpms \| 3.5 kB 00:00

> (1/3): rhel-7-server-rpms/7Server/x86_64/group \| 856 kB 00:01

> (2/3): rhel-7-server-rpms/7Server/x86_64/updateinfo \| 3.1 MB 00:01

> (3/3): rhel-7-server-rpms/7Server/x86_64/primary_db \| 52 MB 00:02 Package 1:make-3.82-23.el7.x86_64 already installed and latest version Resolving Dependencies

> ---\> Package gcc-c++.x86_64 0:4.8.5-36.el7 will be installed

> --\> Processing Dependency: gcc = 4.8.5-36.el7 for package: gcc-c++-4.8.5-36.el7. x86_64

> --\> Processing Dependency: libstdc++ = 4.8.5-36.el7 for package: gcc-c++-4.8.5-3 6.el7.x86_64

> --\> Processing Dependency: libstdc++-devel = 4.8.5-36.el7 for package: gcc-c++-4

> .8.5-36.el7.x86_64

> --\> Processing Dependency: libmpc.so.3()(64bit) for package: gcc-c++-4.8.5-36.el 7.x86_64

> --\> Processing Dependency: libmpfr.so.4()(64bit) for package: gcc-c++-4.8.5-36.e l7.x86_64

> --\> Running transaction check

> ---\> Package gcc.x86_64 0:4.8.5-36.el7 will be installed

> --\> Processing Dependency: cpp = 4.8.5-36.el7 for package: gcc-4.8.5-36.el7.x86\_ 64

> --\> Processing Dependency: libgomp = 4.8.5-36.el7 for package: gcc-4.8.5-36.el7. x86_64

> --\> Processing Dependency: glibc-devel \>= 2.2.90-12 for package: gcc-4.8.5-36.el 7.x86_64

> --\> Processing Dependency: libgcc \>= 4.8.5-36.el7 for package: gcc-4.8.5-36.el7. x86_64

> ---\> Package libmpc.x86_64 0:1.0.1-3.el7 will be installed

> ---\> Package libstdc++.x86_64 0:4.8.5-28.el7_5.1 will be updated

> ---\> Package libstdc++.x86_64 0:4.8.5-36.el7 will be an update

> ---\> Package libstdc++-devel.x86_64 0:4.8.5-36.el7 will be installed

> ---\> Package mpfr.x86_64 0:3.1.1-4.el7 will be installed

> --\> Running transaction check

> ---\> Package cpp.x86_64 0:4.8.5-36.el7 will be installed

> ---\> Package glibc-devel.x86_64 0:2.17-260.el7 will be installed

> --\> Processing Dependency: glibc = 2.17-260.el7 for package: glibc-devel-2.17-26 0.el7.x86_64

> --\> Processing Dependency: glibc-headers = 2.17-260.el7 for package: glibc-devel

> -2.17-260.el7.x86_64

> --\> Processing Dependency: glibc-headers for package: glibc-devel-2.17-260.el7.x 86_64

> ---\> Package libgcc.x86_64 0:4.8.5-28.el7_5.1 will be updated

> ---\> Package libgcc.x86_64 0:4.8.5-36.el7 will be an update

> ---\> Package libgomp.x86_64 0:4.8.5-28.el7_5.1 will be updated

> ---\> Package libgomp.x86_64 0:4.8.5-36.el7 will be an update

> --\> Running transaction check

> ---\> Package glibc.x86_64 0:2.17-222.el7 will be updated

> --\> Processing Dependency: glibc = 2.17-222.el7 for package: glibc-common-2.17-2 22.el7.x86_64

> ---\> Package glibc.x86_64 0:2.17-260.el7 will be an update

> ---\> Package glibc-headers.x86_64 0:2.17-260.el7 will be installed

> --\> Processing Dependency: kernel-headers \>= 2.2.1 for package: glibc-headers-2. 17-260.el7.x86_64

> --\> Processing Dependency: kernel-headers for package: glibc-headers-2.17-260.el 7.x86_64

> ---\> Package glibc-common.x86_64 0:2.17-222.el7 will be updated

> ---\> Package glibc-common.x86_64 0:2.17-260.el7 will be an update

> ---\> Package kernel-headers.x86_64 0:3.10.0-957.el7 will be installed

> --\> Finished Dependency Resolution

> --\> Finding unneeded leftover dependencies Found and removing 0 unneeded dependencies Dependencies Resolved

> =====================================================================

> ===========

> Package Arch Version Repository Size

> =====================================================================

> ===========

> Installing:

> gcc-c++ x86_64 4.8.5-36.el7 rhel-7-server-rpms 7.2 M Installing for dependencies:

> cpp x86_64 4.8.5-36.el7 rhel-7-server-rpms 6.0 M gcc x86_64 4.8.5-36.el7 rhel-7-server-rpms 16 M glibc-devel x86_64 2.17-260.el7 rhel-7-server-rpms 1.1 M glibc-headers x86_64 2.17-260.el7 rhel-7-server-rpms 683 k

> kernel-headers x86_64 3.10.0-957.el7 rhel-7-server-rpms 8.0 M libmpc x86_64 1.0.1-3.el7 rhel-7-server-rpms 51 k libstdc++-devel x86_64 4.8.5-36.el7 rhel-7-server-rpms 1.5 M mpfr x86_64 3.1.1-4.el7 rhel-7-server-rpms 203 k Updating for dependencies:

> glibc x86_64 2.17-260.el7 rhel-7-server-rpms 3.6 M glibc-common x86_64 2.17-260.el7 rhel-7-server-rpms 11 M libgcc x86_64 4.8.5-36.el7 rhel-7-server-rpms 102 k libgomp x86_64 4.8.5-36.el7 rhel-7-server-rpms 157 k libstdc++ x86_64 4.8.5-36.el7 rhel-7-server-rpms 304 k Transaction

> Summary==============================================================

> ==================

> Install 1 Package (+8 Dependent packages) Upgrade ( 5 Dependent packages) Total download size: 56 M

> Downloading packages:

> Delta RPMs disabled because /usr/bin/applydeltarpm not installed. (1/14): cpp-4.8.5-36.el7.x86_64.rpm \| 6.0 MB 00:01

> (2/14): gcc-4.8.5-36.el7.x86_64.rpm \| 16 MB 00:01

> ………….

> (14/14): mpfr-3.1.1-4.el7.x86_64.rpm \| 203 kB 00:00

> Total 8.5 MB/s \| 56 MB 00:06 Running transaction check

> Running transaction test Transaction test succeeded Running transaction

> Updating : libgcc-4.8.5-36.el7.x86_64 1/19

> Updating : glibc-2.17-260.el7.x86_64 2/19

> …………… Installing : glibc-headers-2.17-260.el7.x86_64 \[##################################### \] 19/19

#### Install Node.js

1.  Install Node.js YUM repository \# yum install -y gcc-c++ make

> \# curl -sL https://rpm.nodesource.com/setup_8.x \| sudo -E bash –

2.  Install Node.js

> \# sudo yum install -y nodejs

3.  Check Node.js and NPM version \# node -v

> =\> v8.15.0

> \#npm -v

> =\>6.4.1

#### Install Yarn package management

> \# curl -sL https://dl.yarnpkg.com/rpm/yarn.repo \| sudo tee /etc/yum.repos.d/yarn.repo \# yum install yarn

#### Docker

> Docker is free and open-source software. It automates the deployment of any application as a lightweight, portable, self-sufficient container that will run virtually anywhere. Typically, you develop software on your laptop/desktop. You can build a container with your app, and it can test run on your computer. It will scale in cloud, VM, and more.

#### Install Docker

1.  \# yum remove docker docker-common docker-selinux docker-engine-selinux docker-engine docker-ce
2.  \# yum install -y yum-utils device-mapper-persistent-data lvm2 \# yum-config-manager --add-repo
3.  vi /etc/yum/pluginconf.d/search-disabled-repos.conf modify notify_only=0
4.  \# yum install docker-ce --skip-broken

#### Start Docker

> systemctl start docker.service

#### Docker Status

> \#systemctl status docker.service

> =\> //? docker.service - Docker Application Container Engine

> // Loaded: loaded (/usr/lib/systemd/system/docker.service; enabled; vendor preset: disabled)

> // Active: active (running) since Wed 2018-11-21 13:43:34 CST; 26s ago

> // Docs: [<u>https://docs.docker.com</u>](https://docs.docker.com/)

> // Main PID: 80981 (dockerd)

> // Tasks: 27

> // Memory: 51.7M

> // CGroup: /system.slice/docker.service

> // +-80981 /usr/bin/dockerd -H unix://

> // +-81007 containerd --config /var/run/docker/containerd/containerd....

> Nov 21 13:43:33 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:33 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:33 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:33 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:33 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:34 SPP-NPROD-INT-SOUTH-PROD-RG dockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:34 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:34 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:34 SPP-NPROD-INT-SOUTH-PROD-RGdockerd\[80981\]: time="2018-11- 21T13:...

> Nov 21 13:43:34 SPP-NPROD-INT-SOUTH-PROD-RGsystemd\[1\]: Started Docker Applicati...

> Hint: Some lines were ellipsized, use -l to show in full.

#### Stop Docker

> \# systemctl stop docker.service

#### Restart Docker

> \# systemctl restart docker.service

#### Deploy Production Jar to the cloud (IOC/Production)

1.  Rename \<Jar file\> to patientEntry\<env\>.jar for Patient Entry and staffEntry\<env\>.jar for Staff Entry aka Patient Plan
2.  Move Production Jar file (patientEntry\<env\>.jar / staffEntry\<env\>.jar ) to /home/sppadmin location in VM as explained above using WINSCP
3.  Login as sudo: \# sudo su \<Password\>. Please contact administrator for password.
4.  Navigate to /workspace/virtualization/encryptedPassword. Vim settings.env file and change the value for jasypt.encryptor.password

> jasypt.encryptor.password=\<value\>, save the file.

5.  Run the Production Jar in docker

> Navigate to /workspace/virtualization/\<application\>/\<env\> \# cp /home/sppadmin/\<Jar File\> .

#### Patient Entry:

> \##Navigate to /workspace/ virtualization/patient-entry cd /workspace/ virtualization//patient-entry

> cp /home/sppadmin/ patientEntry\<env\>.jar . \##Create docker image file:

> docker build -t patiententry --build-arg jar-file=patientEntry\<env\>.jar . --no-cache

> \## Run Docker container

> docker run -dit -p\<proper_port\>:8443 --env- file=/workspace/virtualization/encryptedPassword/settings.env -v "\$(pwd)":/src –name=patiententry --cpus=3 --memory=6144m --memory-swap=7168m

> --restart always patiententry

> docker ps

> You will see status like:

#### CONTAINER ID IMAGE COMMAND CREATED STATUS PORTS NAMES

> ff4de5a3ef25 patiententry "/bin/sh -c 'java -j…" 4 days ago Up 4 days 0.0.0.0:8082-\>8443/tcp patiententry

#### Staff Entry (Patient Plan):

> \##Navigate to /workspace/ virtualization//patient-plan cd /workspace/ virtualization//patient-plan

> cp /home/sppadmin/ staffEntryIOC.jar. \## Create docker image file:

> docker build -t staffentry --build-arg jar-file=staffEntry.jar . --no-cache \## Run Docker Container

> docker run -dit -p\<proper_port\>:8443 --env- file=/workspace/virtualization/encryptedPassword/settings.env -v "\$(pwd)":/src –name=staffentry --cpus=3 --memory=6144m --memory-swap=7168m -

> -restart always staffentry

> docker ps

> You will see status like:

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 16%" />
<col style="width: 24%" />
<col style="width: 22%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>CONTAINER ID</strong></th>
<th><blockquote>
<p><strong>IMAGE</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>COMMAND</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>CREATED</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>STATUS</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>PORTS</strong></td>
<td><blockquote>
<p><strong>NAMES</strong></p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

> 31be835a4f61 staffentry "/bin/sh -c 'java -j…" 4 days ago Up 4 days 0.0.0.0:8083-\>8443/tcp staffentry

## Building the Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The application is built from the mha-web/mha-web-parent directly. For a production ready application, use the command *mvn clean install -PbuildAll -DskipTests*. This will build all the jars with production flags for the UI so that the code is minimized and additional logging is disabled. Three jars are built by this command, mha-patient-web-\<version\>-SNAPSHOT.jar, mha-clinician-web-\<version\>- SNAPSHOT.jar, and mha-admin-web-\<version\>-SNAPSHOT.jar.

## Properties and Data Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Properties files are a way of controlling what settings are active at a given time. Our properties files control the following behavior:

- Server Port
- Server key-store & trust-store settings (files, passwords, protocols and settings)
- MySQL database connection settings
- Logging settings
- JWT Secret
- Password encryption secret

> Properties files reside in the mha-web/mha-env-config project. Each properties file is a duplicate of the others with settings specific to the environment of the folder it resides in. For IOC/Production, the template file in the ioc folder should be used and filled in according to that environment. Keys and passwords should never be shared between development and production environments.

> The local properties file used for local development is packaged in the jar. Placing an environment specific properties file on the classpath of the jar will override those settings. In this way we can use the same jar for all environments without rebuilding the jar.

## Encrypted Passwords

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Passwords can be encrypted/decrypted with a library called jasypt. For IOC/Production environments, generate a random 256bit key using the Jasypt library or any online tool. Then use the key with the EncodePassword.java file in /mha-web/mha-model/src/test/java/com/va/med/mha/model/security to encrypt the passwords. Copy and paste the encrypted passwords into the properties file. Encrypt the passwords for any datasources. The password for the keystore cannot be encrypted.

> To encrypt a value use the following command:

> java -cp ~/.m2/repository/org/jasypt/jasypt/1.9.3/jasypt-1.9.3.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI input='\<password_to_encrypt\>' password=\<encryption_key\>

> Take the outputted value and put it inside ENC() tags in the properties file. Make sure the encryption key you use in the command and the encryption key you have on your path are the same.

> Also create a key for the system variable called jasypt.encryptor.password. This can be accomplished a few different ways. The easiest is to add the value to the system path via an environment variable. You can also set the variable on the terminal or script that you start the application in. Finally you can pass it as an argument in the command to start the application. To generate an encryption key, use a site like [<u>randomkeygen.com</u>](https://www.randomkeygen.com/) to generate a 256-bit key, preferably on a different machine. Copy the value generated and set it on the path in the desired way. For our cloud environments, this goes in the

> /workspace/virtualization/encryptedPassword/settings.env file that is used with the docker command to start the container.

## Keystores

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Create keystore with Certificate for IOC/Production. A different password should be used for Dev/IOC/Production environments. Put the name of the keystore along with the password in the properties file.

## Enabling Strong Encryption

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order for encryption to work, support must potentially be added to the JRE. The JRE by default only ships with relatively weak encryption support to meet export control laws. Unlimited strength encryption must be added for the encryption set up below to work. Policy files to enable unlimited strength encryption can be downloaded [<u>here</u>](https://www.oracle.com/technetwork/java/javase/downloads/jce8-download-2133166.html). Copy these files to the \<JDK/JRE install directory\>/jre/lib/security/policy/unlimited folder.

> Note: As of Java 8 Update 161, unlimited strength encryption is enabled by default.

## Encrypting/Decrypting Passwords

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The application now uses encrypted passwords in order to protect access to the database. This requires some configuration in order to work. We use the Jasypt library to encrypt and decrypt the passwords outside and inside the application. The current unencrypted passwords are in the Resources directory. If these unencrypted passwords are every changed, they must be re-encrypted and replaced in the respective properties file in /mha-web/src/main/resources/ folder.

> To set up the encryption, you must have the encryption key on the path for the application. This can be accomplished a few different ways. The easiest is to add the value to the system path via an environment variable. You can also set the variable on the terminal or script that you start the

> application in. Finally you can pass it as an argument in the command to start the application. To generate an encryption key, use a site like [<u>randomkeygen.com</u>](https://www.randomkeygen.com/) to generate a 256-bit key, preferably on a different machine. Copy the value generated and set it on the path in the desired way.

> Then to encrypt a value use the following command:

> java -cp ~/.m2/repository/org/jasypt/jasypt/1.9.3/jasypt-1.9.3.jar org.jasypt.intf.cli.JasyptPBEStringEncryptionCLI input='\<password_to_encrypt\>' password=\<encryption_key\>

> Take the outputted value and put it inside ENC() tags in the properties file. Make sure the encryption key you use in the command and the encryption key you have on your path are the same.

> Note: *<u>Once the production Jar file is created, we are ready deploy in the cloud. Please navigate to 7.5 of Cloud</u> <u>Setup</u>*.

## JWT Secret

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A new secret key needs to be generated for dev, pre-prod, and production environments. This is a random 64 character string that can be generated manually or using an online generator.
